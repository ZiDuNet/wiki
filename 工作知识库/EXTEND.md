# EXTEND.md — 用户偏好

bm25:
  mode: auto_prompt
  prompt_once: true

  thresholds:
    source_count: 10
    wiki_page_count: 50
    wiki_text_chars: 80000
    index_lines: 200
    query_read_pages: 10

  strong_thresholds:
    source_count: 20
    wiki_page_count: 100
    wiki_text_chars: 160000

  index_paths:
    - wiki

  include_raw: false
  auto_rebuild_after_ingest: true
  fallback_to_rg: true

  chunking:
    max_chars: 1800
    overlap_chars: 200

  export:
    default_format: jsonl
    include_text: true
