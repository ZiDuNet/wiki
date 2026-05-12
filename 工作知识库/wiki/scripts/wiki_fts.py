#!/usr/bin/env python3
"""
wiki_fts.py — BM25 全文搜索脚本 for AI 知识库
用法:
  python3 wiki_fts.py build      # 构建索引
  python3 wiki_fts.py search "query" --limit 10  # 搜索
  python3 wiki_fts.py stats      # 查看索引状态
"""

import os, re, math, argparse
from collections import Counter

WIKI_ROOT = os.path.dirname(os.path.abspath(__file__)) + "/.."
INDEX_DIR = os.path.join(WIKI_ROOT, "indexes")
INDEX_FILE = os.path.join(INDEX_DIR, "bm25_index.json")

def tokenize(text):
    return re.findall(r'\b[\w]+\b', text.lower())

def build_index():
    """扫描 wiki/ 子目录建立 BM25 索引"""
    import json
    os.makedirs(INDEX_DIR, exist_ok=True)
    docs = {}
    scan_dirs = [
        os.path.join(WIKI_ROOT, "sources"),
        os.path.join(WIKI_ROOT, "entities"),
        os.path.join(WIKI_ROOT, "concepts"),
        os.path.join(WIKI_ROOT, "synthesis"),
    ]
    for scan_dir in scan_dirs:
        if not os.path.isdir(scan_dir):
            continue
        for dirpath, dirs, files in os.walk(scan_dir):
            for f in files:
                if not f.endswith('.md'): continue
                path = os.path.join(dirpath, f)
                with open(path, 'r', encoding='utf-8', errors='ignore') as fp:
                    content = fp.read()
                slug = os.path.relpath(path, WIKI_ROOT)
                docs[slug] = tokenize(content)
    
    # BM25 参数
    k1 = 1.5
    b = 0.75
    N = len(docs)
    avgdl = sum(len(d) for d in docs.values()) / N if N else 1
    
    # IDF
    df = Counter()
    for d in docs.values():
        for term in set(d):
            df[term] += 1
    
    idf = {term: math.log((N - df[term] + 0.5) / (df[term] + 0.5) + 1) 
           for term in df}
    
    import json
    data = {"docs": docs, "idf": idf, "N": N, "avgdl": avgdl, "k1": k1, "b": b}
    with open(INDEX_FILE, 'w') as f:
        json.dump(data, f)
    print(f"索引已构建: {len(docs)} 篇文档 -> {INDEX_FILE}")

def search(query, limit=10):
    """搜索 BM25 索引"""
    import json
    if not os.path.exists(INDEX_FILE):
        print("索引不存在，请先运行: python3 wiki_fts.py build")
        return []
    
    with open(INDEX_FILE) as f:
        data = json.load(f)
    
    docs = data["docs"]
    idf = data["idf"]
    N, avgdl, k1, b = data["N"], data["avgdl"], data["k1"], data["b"]
    qterms = tokenize(query)
    
    scores = {}
    for slug, doc in docs.items():
        score = 0.0
        dl = len(doc)
        tf = Counter(doc)
        for term in qterms:
            if term not in idf: continue
            tfi = tf.get(term, 0)
            score += idf[term] * (tfi * (k1 + 1)) / (tfi + k1 * (1 - b + b * dl / avgdl))
        if score > 0:
            scores[slug] = score
    
    results = sorted(scores.items(), key=lambda x: -x[1])[:limit]
    for slug, score in results:
        print(f"  [{score:.2f}] {slug}")
    return results

def stats():
    """显示索引状态"""
    import json
    if not os.path.exists(INDEX_FILE):
        print("索引不存在")
        return
    with open(INDEX_FILE) as f:
        data = json.load(f)
    import time
    mtime = os.path.getmtime(INDEX_FILE)
    print(f"文档数: {data['N']}")
    print(f"索引词条: {len(data['idf'])}")
    print(f"构建时间: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mtime))}")

if __name__ == "__main__":
    import json
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command")
    bp = sub.add_parser("build", help="构建 BM25 索引")
    bp.set_defaults(func=build_index)
    sp_stats = sub.add_parser("stats", help="索引状态")
    sp_stats.set_defaults(func=stats)
    sp = sub.add_parser("search", help="搜索")
    sp.add_argument("query", nargs="+", help="搜索词")
    sp.add_argument("--limit", type=int, default=10)
    sp.set_defaults(func=lambda args: search(" ".join(args.query), args.limit))
    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
    else:
        args.func(args) if callable(getattr(args, 'func', None)) and args.command == "search" else args.func()
