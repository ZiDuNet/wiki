# EXTEND.md — 用户偏好

bm25:
  mode: auto_prompt
  prompt_once: true

  thresholds:
    source_count: 30
    wiki_page_count: 150
    wiki_text_chars: 250000
    index_lines: 500
    query_read_pages: 15

  strong_thresholds:
    source_count: 50
    wiki_page_count: 300
    wiki_text_chars: 500000

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
