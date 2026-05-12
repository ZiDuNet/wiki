#!/usr/bin/env python3
"""
wxrobot → Obsidian 同步脚本 v4
- SQLite 任务队列：pending → processing → success / failed
- 10秒爬取间隔，重试机制，失败自动回队列末尾
- 目标：Obsidian 文件系统（/home/wushuo/文档/obsidian/AI/微信公众号/）
"""

import os, re, sys, json, sqlite3, time, random, html, shutil, traceback, hashlib
import requests, threading
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Tuple
from markdownify import MarkdownConverter, ATX
from requests.cookies import cookiejar_from_dict


class WechatConverter(MarkdownConverter):
    """自定义转换器：图片原位占位、代码块保留内容"""
    def convert_img(self, el, text, parent_tags=None):
        src = el.get('data-src') or el.get('src') or ''
        if src:
            return f'\n\n{{{{IMG:{src}}}}}\n\n'
        return ''

    def convert_code(self, el, text, parent_tags=None):
        if el.parent and el.parent.name == 'pre':
            return el.get_text()
        style = el.get('style', '')
        if any(kw in style for kw in ['white-space', 'nowrap', 'padding', 'overflow-x']):
            code_text = html.unescape(el.get_text())
            return f'\n\n```\n{code_text}\n```\n\n'
        code_text = text or el.get_text()
        return f'`{code_text}`'

    def convert_pre(self, el, text, parent_tags=None):
        code_el = el.find('code')
        if code_el:
            code_text = html.unescape(code_el.get_text())
        else:
            code_text = html.unescape(el.get_text())
        code_text = code_text.strip()
        return f'\n\n```\n{code_text}\n```\n\n'


# ========== 配置 ==========
SCRIPT_DIR = Path(__file__).parent.resolve()

WXROBOT_API = "http://nas.4dbim.cc:5055/AppStore/wxrobot/chat/list"
OBSIDIAN_VAULT = SCRIPT_DIR
ZENITH_TOKEN = "107MSQlMTc3Njc4NjY5MyQlMTc0Nzk5OTkzNCQlMDI3YjFjODViY2M2MTE4MjkxZjY0MzZhNDAzOTZm1MjIkJTE3NjMzMTEzMzc4JCVybwm4m4IPS61K2ufz6fF0Q0NZlOqfXELDCfJj2pxXMdFLgP4F02AIM8A1rz8NTU5bdKyHMvm3PnUae5CTAwMZLqcFm2dm2TF7n1m1hm2EWwYE4lfQbAtKVhvkYMe5JrHbklF1NhuLm33byx3tm2wyCohYss3m3WjXtm1Ds9Xm26yGlzMwm2biFm1vNbW7RwweEzO6MN8g3iznxm2PXQ0h6z3vy7W5Hjbj5k7l26Qm1cdbm22zz3PbSz20tSPlJXQ1ZWm2guGkRm3jxLGJgGrZm12Gm2Fjh13HwgNMm3hBTtsf4EYjAJ2nOHm3snm2tgoxoKBm3i4tbm18Qy6FTi6frhosOelJINUxLXwnVKSAm3qWMxnnm3e36Am4m4"
SIGN_COOKIE = "061WjA0NDExMTBBRjFISl8xNzc2Nzg2NjkzXzU0ODI4Mzc1NjkzMzkxNTQ4NjEm4IdjGf7upIsUg8RkTwXm10S4Va9J42anNGjS5t5cm31wtCLfS0k9m2ZSIUCKBMt84bu43gslScV8LCrjaY3l2NUBekgRLkm2Rm3DXM4ffEYAj5m2r8Z0jJrlwa6irdDM6PHbxuy5GFZB5buTHhUTUt4kzcHQNggQ85PApFPnzgWAjBe5Ec9SBnf6YXqM3kSTKLLG0Sm1nXKm2wDRG3LF7h9I2qGiB9McNm29rBHsH9hcKhbuEGxaxCrfz2Kiy4REFUusKctawSty0PzDXEA2QGRO1prKJtb4GJS1RSpUQqj7wq5R7Mhk8HhlIO65gDnsh43UaQw7m33bWUHtdCiiPunjJyMNgm4m4"

DB_PATH = str(SCRIPT_DIR / "wxrobot_sync_v3.db")
CRAWL_DELAY = 3
MAX_RETRIES = 10

MOBILE_UA = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"

# ========== LLM 分类配置 ==========
LLM_API_URL = "https://aiproxy.4dbim.cc:4443/v1/chat/completions"
LLM_API_KEY = "sk-o2iXXeFJEM9QiJcqU76lQGayoHhHF7unwJjCDV4w1nVi6Acf"
LLM_MODEL = "GLM-4-Flash-250414"
LLM_FALLBACK_MODELS = ["glm-4.7-flash", "glm-4.6v-flash", "glm-4-flash", "MiniMax-M2.5", "MiniMax-M2.7", "MiniMax-M2.1"]

# LLM 调用锁 — 防止并发触发限流
_llm_lock = threading.Lock()


# ========== 日志 ==========
def log(msg, level="INFO"):
    ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{ts}] [{level}] {msg}", flush=True)


# ========== 数据库 ==========
def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA journal_mode=WAL")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS task_queue (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            title TEXT DEFAULT '',
            author TEXT DEFAULT '',
            msg_time INTEGER DEFAULT 0,
            msg_data TEXT DEFAULT '{}',
            status TEXT DEFAULT 'pending',
            notebook_name TEXT DEFAULT '',
            file_path TEXT DEFAULT '',
            error TEXT DEFAULT '',
            retries INTEGER DEFAULT 0,
            created_at TEXT,
            updated_at TEXT,
            synced_at TEXT
        )
    """)
    # 兼容旧表结构：如果有旧的 notebook_id/doc_id 列，重命名为新列
    try:
        c.execute("SELECT notebook_id FROM task_queue LIMIT 1")
        # 旧表有 notebook_id 列，需要迁移
        c.execute("ALTER TABLE task_queue ADD COLUMN notebook_name TEXT DEFAULT ''")
        c.execute("ALTER TABLE task_queue ADD COLUMN file_path TEXT DEFAULT ''")
        c.execute("UPDATE task_queue SET notebook_name = COALESCE(notebook_id, '') WHERE notebook_name = ''")
        log("  DB schema 迁移完成（旧→新）", "WARN")
    except sqlite3.OperationalError:
        pass  # 列不存在，直接下一步
    c.execute("CREATE INDEX IF NOT EXISTS idx_status ON task_queue(status)")
    c.execute("CREATE INDEX IF NOT EXISTS idx_url ON task_queue(url)")
    c.execute("""
        CREATE TABLE IF NOT EXISTS run_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            run_mode TEXT,
            started_at TEXT,
            finished_at TEXT,
            total INTEGER DEFAULT 0,
            success INTEGER DEFAULT 0,
            failed INTEGER DEFAULT 0,
            skipped INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    return conn


def normalize_url(url: str) -> str:
    url = url.split('#')[0]
    url = re.sub(r'#rd$', '', url.strip())
    url = re.sub(r'\s+', '', url)
    return url


def enqueue_tasks(conn, messages: list):
    added = 0
    now = datetime.now().isoformat()
    for msg in messages:
        try:
            msg_data = json.loads(msg.get("msg_data", "{}"))
        except:
            msg_data = {}
        link_url = msg_data.get("link_url", "")
        if not link_url:
            continue
        clean_url = normalize_url(link_url)
        title = msg_data.get("title", "").strip()

        existing = conn.execute("SELECT id FROM task_queue WHERE url = ? OR (title != '' AND title = ?)",
                                (clean_url, title)).fetchone()
        if existing:
            continue

        conn.execute("""
            INSERT INTO task_queue (url, title, msg_time, msg_data, status, created_at, updated_at)
            VALUES (?, ?, ?, ?, 'pending', ?, ?)
        """, (clean_url, title, msg.get("msg_time", 0), json.dumps(msg_data, ensure_ascii=False), now, now))
        added += 1
    conn.commit()
    return added


def get_pending_tasks(conn, limit=100):
    rows = conn.execute("""
        SELECT id, url, title, msg_time, msg_data, retries
        FROM task_queue
        WHERE status = 'pending' AND retries <= ?
        ORDER BY retries ASC, id ASC
        LIMIT ?
    """, (MAX_RETRIES, limit)).fetchall()
    return rows


def mark_processing(conn, task_id):
    conn.execute("""
        UPDATE task_queue SET status = 'processing', updated_at = ? WHERE id = ?
    """, (datetime.now().isoformat(), task_id))
    conn.commit()


def mark_success(conn, task_id, file_path, notebook_name, title, author):
    conn.execute("""
        UPDATE task_queue
        SET status = 'success', file_path = ?, notebook_name = ?,
            title = ?, author = ?, synced_at = ?, updated_at = ?, error = ''
        WHERE id = ?
    """, (file_path, notebook_name, title, author, datetime.now().isoformat(), datetime.now().isoformat(), task_id))
    conn.commit()


def mark_failed_retry(conn, task_id, error):
    now = datetime.now().isoformat()
    row = conn.execute("SELECT retries, title, url FROM task_queue WHERE id = ?", (task_id,)).fetchone()
    if row and row[0] >= MAX_RETRIES:
        conn.execute("""
            UPDATE task_queue
            SET status = 'failed', error = ?, updated_at = ?
            WHERE id = ?
        """, (error[:500], now, task_id))
        conn.commit()
        log(f"  ❌ 放弃 (重试{row[0]}次): {row[1]} | {row[2]}", "ERROR")
        return
    conn.execute("""
        UPDATE task_queue
        SET status = 'pending', error = ?, retries = retries + 1, updated_at = ?
        WHERE id = ?
    """, (error[:500], now, task_id))
    conn.commit()


def get_stats(conn):
    stats = {}
    for row in conn.execute("SELECT status, COUNT(*) FROM task_queue GROUP BY status"):
        stats[row[0]] = row[1]
    return stats


# ========== Obsidian 文件系统操作 ==========
def ensure_folder(name: str) -> Path:
    """确保笔记本文件夹存在，返回路径"""
    folder = OBSIDIAN_VAULT / name
    folder.mkdir(parents=True, exist_ok=True)
    return folder


def get_existing_categories() -> List[str]:
    """扫描输出目录，获取已有分类文件夹列表（按名称长度降序，优先匹配更具体的）"""
    categories = []
    if not OBSIDIAN_VAULT.exists():
        return categories
    for item in OBSIDIAN_VAULT.iterdir():
        if item.is_dir() and item.name != "assets":
            categories.append(item.name)
    categories.sort(key=len, reverse=True)
    return categories


def call_llm(prompt: str, max_retries: int = 3) -> Optional[str]:
    """调用 LLM API，主模型失败自动降级到备用模型，加锁防并发限流"""
    with _llm_lock:
        models = [LLM_MODEL] + LLM_FALLBACK_MODELS
        for model in models:
            for attempt in range(max_retries):
                try:
                    resp = requests.post(
                        LLM_API_URL,
                        headers={
                            "Authorization": f"Bearer {LLM_API_KEY}",
                            "Content-Type": "application/json",
                        },
                        json={
                            "model": model,
                            "messages": [{"role": "user", "content": prompt}],
                            "thinking": {"type": "disabled"},
                            "temperature": 0.3,
                            "max_tokens": 50,
                        },
                        timeout=30,
                    )
                    resp.raise_for_status()
                    data = resp.json()
                    content = data["choices"][0]["message"]["content"].strip()
                    if content:
                        return content
                    raise Exception("LLM 返回内容为空")
                except Exception as e:
                    log(f"  [{model}] 调用失败 (尝试 {attempt + 1}/{max_retries}): {e}", "WARN")
                    if attempt < max_retries - 1:
                        time.sleep(60)
            log(f"  [{model}] 已重试{max_retries}次，切换下一个模型", "WARN")
    return None


def classify_article(title: str, description: str = "") -> str:
    """分类文章：先匹配标题中的已有分类名，匹配不上则走 LLM"""
    categories = get_existing_categories()

    # 1. 标题匹配：检查标题是否包含已有分类名（长的优先）
    title_lower = title.lower()
    for cat in categories:
        if cat.lower() in title_lower:
            return cat

    # 2. 没匹配上，交给 LLM
    cat_list_str = "、".join(categories) if categories else "（暂无分类）"
    prompt = f"""你是一个文章分类专家。请根据文章的核心主题（产品名、技术领域、应用场景）进行分类。

文章标题：{title}
文章描述：{description[:500] if description else '无'}

现有分类列表：{cat_list_str}

分类原则：
- 根据标题中提到的核心产品/技术/领域来分类，不要按用途分类
- 例如标题提到"Hermes"就归Hermes，提到"Skills"就归Skills，不要归成"效率工具"
- 标题提到具体产品名时，优先以产品名作为分类依据
- 只有现有分类确实匹配文章核心主题时才选用
- 如果现有分类都不匹配，创建一个2-6字的新分类名（用产品名或技术领域命名）

只返回分类名，不要任何其他内容。"""

    result = call_llm(prompt)
    if not result:
        return "未分类"

    # 3. 检查 LLM 返回是否匹配已有分类
    result_lower = result.lower()
    for cat in categories:
        if cat.lower() == result_lower or cat.lower() in result_lower or result_lower in cat.lower():
            return cat

    # 4. LLM 返回了新分类
    log(f"  🆕 LLM 新分类: {result}")
    return result


def safe_filename(name: str) -> str:
    """过滤文件名非法字符"""
    name = re.sub(r'[\\/:*?"<>|]', '_', name)
    name = re.sub(r'\s+', ' ', name).strip()
    return name[:200]


def write_doc(folder: Path, title: str, content: str) -> Path:
    """写入 md 文件到笔记本文件夹，返回文件路径"""
    safe_title = safe_filename(title)
    file_path = folder / f"{safe_title}.md"

    # 如果文件已存在，加序号区分
    if file_path.exists():
        for i in range(1, 100):
            file_path = folder / f"{safe_title}_{i}.md"
            if not file_path.exists():
                break

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return file_path


def save_asset(url: str, filename: str) -> Path:
    """下载图片到本地 assets 目录"""
    ext = ".jpg"
    if "png" in url.lower():
        ext = ".png"
    elif "gif" in url.lower():
        ext = ".gif"
    elif "webp" in url.lower():
        ext = ".webp"

    save_path = ASSETS_DIR / f"{filename}{ext}"
    resp = requests.get(url, headers={"User-Agent": MOBILE_UA, "Referer": "https://mp.weixin.qq.com/"}, timeout=15)
    resp.raise_for_status()
    with open(save_path, "wb") as f:
        f.write(resp.content)

    if save_path.stat().st_size < 100:
        save_path.unlink()
        return None
    return save_path


# ========== 文章抓取 ==========
def fetch_article_html(url: str) -> Tuple[Optional[str], Optional[str], List[str], str]:
    """返回: (title, html_content, image_urls, author)"""
    try:
        resp = requests.get(
            url,
            headers={
                "User-Agent": MOBILE_UA,
                "Accept": "text/html,application/xhtml+xml",
                "Accept-Language": "zh-CN,zh;q=0.9",
            },
            timeout=20,
        )
        resp.raise_for_status()
        html_text = resp.text

        title = ""
        title_match = re.search(r'<h1[^>]*class="rich_media_title"[^>]*>(.*?)</h1>', html_text, re.DOTALL)
        if title_match:
            title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()
        if not title:
            m = re.search(r'var msg_title = [\'"](.*?)[\'"]', html_text)
            if m:
                title = html.unescape(m.group(1))

        author = ""
        for pat in [
            r'<a[^>]*id="js_name"[^>]*>(.*?)</a>',
            r'<span[^>]*class="profile_nickname"[^>]*>(.*?)</span>',
            r'<meta[^>]*property="og:article:author"[^>]*content=["\']([^"\']+)["\']',
            r'var nickname = [\'"](.*?)[\'"]',
        ]:
            m = re.search(pat, html_text, re.DOTALL)
            if m:
                author = re.sub(r'<[^>]+>', '', m.group(1)).strip()
                if author:
                    break

        content_match = re.search(r'<div[^>]*id="js_content"[^>]*>(.*?)</div>\s*<script', html_text, re.DOTALL)
        if not content_match:
            content_match = re.search(r'<div[^>]*id="js_content"[^>]*>(.*?)</div>', html_text, re.DOTALL)
        if not content_match:
            return title, None, [], author

        content_html = content_match.group(1)
        content_html_unescaped = html.unescape(content_html)
        img_urls = []
        for m in re.finditer(r'data-src=["\']([^"\']+)["\']', content_html_unescaped):
            img_url = m.group(1)
            if ('mmbiz.qpic.cn' in img_url or 'wework.qpic.cn' in img_url) and img_url not in img_urls:
                img_urls.append(img_url)
        for m in re.finditer(r'<img[^>]*src=["\']([^"\']+)["\']', content_html_unescaped):
            img_url = m.group(1)
            if ('mmbiz.qpic.cn' in img_url or 'wework.qpic.cn' in img_url) and img_url not in img_urls:
                img_urls.append(img_url)

        return title, content_html_unescaped, img_urls, author
    except Exception as e:
        log(f"  抓取失败: {e}", "ERROR")
        return None, None, [], ""


def html_to_markdown(html_str: str) -> str:
    if not html_str:
        return ""

    text = html_str
    for pat in [
        r'<div[^>]*id="js_pc_qr_code"[^>]*>.*?</div>',
        r'<div[^>]*class="rich_media_tool"[^>]*>.*?</div>',
        r'<div[^>]*id="js_tags"[^>]*>.*?</div>',
        r'<div[^>]*class="mpda_bottom_handler"[^>]*>.*?</div>',
        r'<div[^>]*id="js_tags_preview_toast"[^>]*>.*?</div>',
        r'<div[^>]*class="profile_card"[^>]*>.*?</div>',
        r'<div[^>]*class="rich_media_area_extra"[^>]*>.*?</div>',
        r'<div[^>]*id="js_share_btn"[^>]*>.*?</div>',
        r'<section[^>]*class="rate_mp_wrp"[^>]*>.*?</section>',
        r'<script[^>]*>.*?</script>',
        r'<style[^>]*>.*?</style>',
    ]:
        text = re.sub(pat, '', text, flags=re.DOTALL)

    md_text = WechatConverter(
        heading_style=ATX,
        bullets='-',
        code_language='',
    ).convert(text)

    for pat, flags in [
        (r'微信扫一扫.*', re.DOTALL),
        (r'javascript:void\(0\)', re.MULTILINE),
        (r'预览时标签不可点', re.MULTILINE),
        (r'继续滑动看下一个', re.MULTILINE),
        (r'轻触阅读原文', re.MULTILINE),
        (r'向上滑动看下一个', re.MULTILINE),
        (r'喜欢此内容的人还喜欢.*', re.DOTALL),
        (r'已喜欢.*?取消', re.DOTALL),
        (r'知道了', re.MULTILINE),
        (r'[×✕]\s*分析', re.MULTILINE),
        (r'已关注\d+天', re.MULTILINE),
        (r'>\s*‍\s*', re.MULTILINE),
        (r'>\s*$', re.MULTILINE),
    ]:
        md_text = re.sub(pat, '', md_text, flags=flags)

    md_text = re.sub(r'^-\s*•\s*', '- ', md_text, flags=re.MULTILINE)
    md_text = re.sub(r'\n{3,}', '\n\n', md_text)
    md_text = re.sub(r'[ \t]+\n', '\n', md_text)
    return md_text.strip()


def download_image(url: str, idx: int, dest_dir: Path) -> Optional[str]:
    """下载图片直接到目标目录"""
    try:
        ext = ".jpg"
        if "png" in url.lower():
            ext = ".png"
        elif "gif" in url.lower():
            ext = ".gif"
        elif "webp" in url.lower():
            ext = ".webp"
        url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
        save_path = dest_dir / f"img_{url_hash}{ext}"
        if save_path.exists():
            return f"assets/img_{url_hash}{ext}"
        resp = requests.get(url, headers={"User-Agent": MOBILE_UA, "Referer": "https://mp.weixin.qq.com/"}, timeout=15)
        resp.raise_for_status()
        with open(save_path, "wb") as f:
            f.write(resp.content)
        if save_path.stat().st_size < 100:
            save_path.unlink()
            return None
        return f"assets/img_{url_hash}{ext}"
    except Exception as e:
        log(f"  下载图片失败 [{idx}]: {e}", "WARN")
        return None


# ========== wxrobot API ==========
def fetch_wxrobot_messages(offset=0, limit=200):
    ts = str(int(time.time() * 1000))
    rnd = f"{ts}_{random.randint(1000, 9999)}"
    cookies = cookiejar_from_dict({
        "_l": "zh_cn", "device_id": "027b1c85bcc6118291f6436a40396f22",
        "nas_id": "Z0441110AF1HJ", "zenithtoken": ZENITH_TOKEN,
        "username": "17633113378", "userid": "1", "isMaster": "1",
        "plat": "web", "app": "file", "version": "2.3.2026032701",
        "st": ts, "sign": SIGN_COOKIE,
        "deviceColor": "al_ti_gray", "devicePdt": "z4", "deviceMode": "z4pro+",
        "isAllFlash": "0", "device": "PC",
        "clientPublicIp": "120.245.113.195", "publicSwitch": "true",
    })
    data = {
        "offset": offset, "limit": limit, "local_msg_type": "link", "search_text": "",
        "plat": "web", "version": "2.3.2026032701",
        "device_id": "027b1c85bcc6118291f6436a40396f22", "device": "PC",
        "_l": "zh_cn", "token": ZENITH_TOKEN, "nasid": "Z0441110AF1HJ",
    }
    try:
        resp = requests.post(
            WXROBOT_API, params={"rnd": rnd, "webagent": "v2"},
            headers={"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded",
                     "User-Agent": "Mozilla/5.0", "Origin": "http://nas.4dbim.cc:5055"},
            data=data, cookies=cookies, timeout=30,
        )
        if resp.status_code == 200:
            result = resp.json()
            if result.get("code") == "200":
                return result.get("data", {}).get("list", [])
            else:
                log(f"API 返回错误: code={result.get('code')}", "ERROR")
        else:
            log(f"HTTP 错误: {resp.status_code}", "ERROR")
    except Exception as e:
        log(f"获取微信消息失败: {e}", "ERROR")
    return []


def fetch_all_messages():
    all_msgs = []
    offset = 0
    while True:
        msgs = fetch_wxrobot_messages(offset=offset, limit=200)
        if not msgs:
            break
        all_msgs.extend(msgs)
        if len(msgs) < 200:
            break
        offset += 200
        time.sleep(0.5)
    return all_msgs


# ========== 核心：处理单篇 ==========
def process_one_task(conn, task_id, url, msg_data_str, msg_time) -> bool:
    try:
        msg_data = json.loads(msg_data_str)
    except:
        msg_data = {}

    description = msg_data.get("description", "")

    # 1. 抓取文章
    title, content_html, img_urls, author = fetch_article_html(url)

    if not title:
        title = msg_data.get("title", "").strip() or f"文章_{url[-20:]}"
    if not author:
        author = msg_data.get("author_name", "")

    if not content_html:
        if description and len(description) > 30:
            log(f"  网页正文为空，使用 description 兜底 ({len(description)} chars)")
            content_html = f"<p>{description}</p>"
            img_urls = []
        else:
            mark_failed_retry(conn, task_id, f"正文抓取为空 (title={title[:50]})")
            return False

    # 2. 转 Markdown
    md_content = html_to_markdown(content_html)
    if len(md_content) < 20:
        mark_failed_retry(conn, task_id, f"正文太短 ({len(md_content)}字符)")
        return False

    # 3. 分类
    notebook_name = classify_article(title, description)
    folder = ensure_folder(notebook_name)
    log(f"  📁 分类: {notebook_name}")

    safe_title = safe_filename(title)
    from_time = datetime.fromtimestamp(msg_time).strftime('%Y-%m-%d %H:%M') if msg_time else "未知时间"

    # 4. 处理图片 — 直接下载到分类目录的 assets/ 下
    notebook_assets_dir = folder / "assets"
    notebook_assets_dir.mkdir(parents=True, exist_ok=True)
    img_map = {}
    if img_urls:
        for idx, img_url in enumerate(img_urls):
            asset_path = download_image(img_url, idx, notebook_assets_dir)
            if asset_path:
                img_map[img_url] = asset_path

        # 替换图片占位符
        for orig_url, asset_path in img_map.items():
            placeholder = f"{{{{IMG:{orig_url}}}}}"
            if placeholder in md_content:
                md_content = md_content.replace(placeholder, f"![]({asset_path})")

        # 模糊匹配残留占位符
        def fuzzy_replace(m):
            raw = m.group(1)
            for orig_url, asset_path in img_map.items():
                if raw in orig_url or orig_url in raw:
                    return f"![]({asset_path})"
            return f"![]({raw})"
        md_content = re.sub(r'\{\{IMG:(.*?)\}\}', fuzzy_replace, md_content)

    # 5. 构建文档内容
    header = f"> 📎 来源: [{author or '未知'}]({url}) | 时间: {from_time}\n\n---\n\n"
    full_md = f"{header}{md_content}\n"

    # 6. 写入文件
    file_path = write_doc(folder, title, full_md)

    if file_path.exists():
        mark_success(conn, task_id, str(file_path), notebook_name, title, author)
        img_count = len(img_map)
        log(f"  ✅ [{notebook_name}] {title[:50]} ({img_count}图)")
        return True
    else:
        mark_failed_retry(conn, task_id, "文件写入失败")
        return False


# ========== 主流程 ==========
def collect(mode="incremental"):
    log(f"===== 收集阶段 (mode={mode}) =====")
    conn = init_db()

    if mode == "full":
        messages = fetch_all_messages()
    else:
        messages = fetch_wxrobot_messages(offset=0, limit=50)

    log(f"获取到 {len(messages)} 条消息")
    added = enqueue_tasks(conn, messages)
    stats = get_stats(conn)
    conn.close()
    log(f"新增入队: {added} | 队列状态: {stats}")


def process():
    log("===== 处理阶段 =====")
    conn = init_db()

    run_id = conn.execute("""
        INSERT INTO run_log (run_mode, started_at) VALUES ('process', ?)
    """, (datetime.now().isoformat(),)).lastrowid
    conn.commit()

    success = 0
    failed = 0
    first = True

    while True:
        tasks = get_pending_tasks(conn, limit=1)
        if not tasks:
            break

        task_id, url, title, msg_time, msg_data, retries = tasks[0]

        if not first:
            delay = CRAWL_DELAY + random.uniform(0, 3)
            log(f"等待 {delay:.1f}s...")
            time.sleep(delay)
        first = False

        display_title = title[:50] if title else url[:60]
        retry_info = f" (重试#{retries})" if retries > 0 else ""
        log(f"处理 [{task_id}]: {display_title}{retry_info}")

        mark_processing(conn, task_id)

        try:
            if process_one_task(conn, task_id, url, msg_data, msg_time):
                success += 1
            else:
                failed += 1
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)[:200]}"
            log(f"  ❌ 异常: {error_msg}", "ERROR")
            traceback.print_exc()
            mark_failed_retry(conn, task_id, error_msg)
            failed += 1

    conn.execute("""
        UPDATE run_log SET finished_at=?, total=?, success=?, failed=? WHERE id=?
    """, (datetime.now().isoformat(), success + failed, success, failed, run_id))
    conn.commit()

    stats = get_stats(conn)
    conn.close()
    log(f"===== 处理完成 ✅成功:{success} ❌失败(已回队):{failed} | 队列: {stats} =====")


def status():
    conn = init_db()
    stats = get_stats(conn)
    print(f"\n{'='*50}")
    print(f"队列状态:")
    for k, v in stats.items():
        print(f"  {k}: {v}")

    recent_failed = conn.execute("""
        SELECT url, title, error, retries FROM task_queue
        WHERE status = 'pending' AND retries > 0
        ORDER BY retries DESC LIMIT 5
    """).fetchall()
    if recent_failed:
        print(f"\n重试中的任务 (Top 5):")
        for url, title, error, retries in recent_failed:
            print(f"  [{retries}次] {title[:40]} | {error[:60]}")

    runs = conn.execute("SELECT * FROM run_log ORDER BY id DESC LIMIT 3").fetchall()
    if runs:
        print(f"\n最近运行:")
        for r in runs:
            print(f"  {r[3]} → {r[4]} | 成功:{r[5]} 失败:{r[6]}")
    print(f"{'='*50}\n")
    conn.close()


def reset_failed():
    conn = init_db()
    now = datetime.now().isoformat()

    n_proc = conn.execute("SELECT COUNT(*) FROM task_queue WHERE status = 'processing'").fetchone()[0]
    if n_proc:
        conn.execute("UPDATE task_queue SET status = 'pending', updated_at = ? WHERE status = 'processing'", (now,))
        print(f"重置 processing → pending: {n_proc}")

    n_fail = conn.execute("SELECT COUNT(*) FROM task_queue WHERE status = 'failed'").fetchone()[0]
    if n_fail:
        conn.execute("UPDATE task_queue SET status = 'pending', retries = 0, error = '', updated_at = ? WHERE status = 'failed'", (now,))
        print(f"重置 failed → pending: {n_fail}")

    if "--all" in sys.argv:
        n_succ = conn.execute("SELECT COUNT(*) FROM task_queue WHERE status = 'success'").fetchone()[0]
        if n_succ:
            conn.execute("UPDATE task_queue SET status = 'pending', retries = 0, file_path = '', synced_at = '', updated_at = ? WHERE status = 'success'", (now,))
            print(f"重置 success → pending: {n_succ}")

    conn.commit()
    stats = get_stats(conn)
    print(f"\n当前队列: {stats}")
    conn.close()


if __name__ == "__main__":
    args = sys.argv[1:]

    if "--status" in args:
        status()
    elif "--collect-full" in args:
        collect(mode="full")
    elif "--collect" in args:
        collect(mode="incremental")
    elif "--reset" in args:
        reset_failed()
    elif "--full" in args:
        collect(mode="full")
        process()
    elif "--process" in args:
        process()
    else:
        collect(mode="full")
        process()
