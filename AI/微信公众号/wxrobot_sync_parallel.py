#!/usr/bin/env python3
"""
并发处理脚本 — 首次大批量同步时加速用
用法：python wxrobot_sync_parallel.py --workers 5
依赖 wxrobot_sync_v3.py 中的所有函数
"""

import sys
import time
import sqlite3
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

# 导入主脚本的所有函数和配置
from wxrobot_sync_v3 import (
    init_db, get_pending_tasks, mark_processing, mark_success,
    mark_failed_retry, process_one_task, log, CRAWL_DELAY, MAX_RETRIES,
)


def worker(task_args, worker_id):
    """单个 worker 线程处理任务"""
    task_id, url, title, msg_time, msg_data, retries = task_args
    # 每个线程用自己的 DB 连接
    conn = init_db()
    mark_processing(conn, task_id)
    try:
        ok = process_one_task(conn, task_id, url, msg_data, msg_time)
        return worker_id, task_id, ok, None
    except Exception as e:
        mark_failed_retry(conn, task_id, str(e)[:500])
        return worker_id, task_id, False, str(e)
    finally:
        conn.close()


def run_parallel(workers=5, batch_size=50):
    log(f"===== 并发处理启动 (workers={workers}) =====")
    conn = init_db()

    # 统计
    total = conn.execute("SELECT COUNT(*) FROM task_queue WHERE status = 'pending'").fetchone()[0]
    log(f"待处理任务: {total}")
    conn.close()

    success = 0
    failed = 0
    processed = 0

    with ThreadPoolExecutor(max_workers=workers) as pool:
        while True:
            # 每批取任务，每个线程独立拿自己的连接
            conn = init_db()
            tasks = get_pending_tasks(conn, limit=batch_size)
            conn.close()

            if not tasks:
                break

            futures = []
            for task in tasks:
                # 每个任务立即提交，带少量随机延迟防封
                delay = CRAWL_DELAY * 0.5 + (hash(task[0]) % 3)
                time.sleep(min(delay / workers, 0.5))
                futures.append(pool.submit(worker, task, len(futures)))

            for future in as_completed(futures):
                processed += 1
                try:
                    wid, task_id, ok, err = future.result()
                    if ok:
                        success += 1
                    else:
                        failed += 1
                    if err:
                        log(f"  ❌ Worker-{wid} 任务{task_id}异常: {err[:100]}", "ERROR")
                except Exception as e:
                    failed += 1
                    log(f"  ❌ Worker 异常: {e}", "ERROR")

                if processed % 10 == 0:
                    log(f"进度: {processed}/{total} ✅{success} ❌{failed}")

    log(f"===== 并发处理完成 ✅{success} ❌{failed} 总计{processed} =====")


if __name__ == "__main__":
    workers = 3
    for i, arg in enumerate(sys.argv):
        if arg == "--workers" and i + 1 < len(sys.argv):
            workers = int(sys.argv[i + 1])
    run_parallel(workers=workers)
