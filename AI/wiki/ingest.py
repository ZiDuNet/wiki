#!/usr/bin/env python3
"""
知识库摄入脚本 v2 - 批量处理微信公众号文章到wiki
改进：更好的slug化、哈希去重、简洁的wikilink
"""
import os
import re
import hashlib
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict

BASE_DIR = Path(r"D:/我的知识库/AI")
SOURCE_DIR = BASE_DIR / "微信公众号"
WIKI_DIR = BASE_DIR / "wiki"
SOURCES_DIR = WIKI_DIR / "sources"
ENTITIES_DIR = WIKI_DIR / "entities"
CONCEPTS_DIR = WIKI_DIR / "concepts"
SYNTHESIS_DIR = WIKI_DIR / "synthesis"

# 确保目录存在
for d in [SOURCES_DIR, ENTITIES_DIR, CONCEPTS_DIR, SYNTHESIS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# slug到文件的映射（避免冲突）
slug_map = {}

def slugify(text):
    """将文本转为简洁的slug，限制长度80"""
    text = re.sub(r'[《》【】「」『』（）\(\)\[\]\{\}。，、；：！？…—\-_·\.\,\;\:\!\?​ ]', '', text)
    text = re.sub(r'[\\/:*?"<>|#@%^&+=~`]', '', text)
    text = text.strip()
    # 空格替换为短横线
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    text = text.strip('-')
    # 限制长度为80字符
    if len(text) > 80:
        text = text[:80]
    if not text:
        text = "untitled"
    return text

def make_unique_slug(title, filepath):
    """创建唯一的slug文件名"""
    base_slug = slugify(title)
    if not base_slug or base_slug == "untitled":
        base_slug = slugify(filepath.stem)
    if not base_slug:
        base_slug = hashlib.md5(str(filepath).encode()).hexdigest()[:12]

    # 如果已经用过这个slug，加后缀
    if base_slug in slug_map:
        # 检查是否是同一个文件
        if slug_map[base_slug] == str(filepath):
            return base_slug
        # 加序号
        counter = 2
        while f"{base_slug}-{counter}" in slug_map:
            counter += 1
        base_slug = f"{base_slug}-{counter}"

    slug_map[base_slug] = str(filepath)
    return base_slug

def entity_slug(name):
    """实体slug"""
    return slugify(name)

def concept_slug(name):
    """概念slug"""
    return slugify(name)

def extract_frontmatter(content):
    """从文章开头提取来源信息"""
    source_match = re.search(r'> 📎 来源: \[([^\]]+)\]\(([^)]+)\)\s*\|\s*时间: (\S+)', content)
    source_name = source_match.group(1) if source_match else "未知"
    source_url = source_match.group(2) if source_match else ""
    source_date = source_match.group(3) if source_match else ""
    return source_name, source_url, source_date

def extract_title(content, filepath):
    """提取文章标题"""
    # 优先从内容中找第一个markdown标题
    title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
    if title_match:
        title = title_match.group(1).strip()
        # 清理标题中的格式标记
        title = re.sub(r'\*\*|__|\*|_', '', title)
        return title
    # 回退到文件名
    fname = filepath.stem
    # 尝试提取文件名中有意义的部分
    if '_' in fname:
        parts = fname.split('_')
        if len(parts) >= 2:
            return parts[-1][:80]
    return fname[:80]

def extract_tags(content, category):
    """从内容中提取标签"""
    tags = [category]
    keyword_map = {
        'Agent': ['agent', '智能体', 'multi-agent', '多智能体'],
        'Claude': ['claude', 'anthropic', 'claude code'],
        'MCP': ['mcp', 'model context protocol'],
        'GitHub': ['github', 'copilot'],
        'Obsidian': ['obsidian'],
        '飞书': ['飞书', 'lark', 'feishu'],
        'PPT': ['ppt', '幻灯片', '演示文稿', 'slides'],
        'RAG': ['rag', '检索增强'],
        'Dify': ['dify'],
        'Harness': ['harness'],
        'Prompt': ['prompt', '提示词'],
        'API': ['api', '接口'],
        'Python': ['python'],
        'OpenAI': ['openai', 'gpt', 'chatgpt'],
        'Skill': ['skill', '技能'],
        'Vibe Coding': ['vibe coding', '氛围编程'],
        'OpenClaw': ['openclaw'],
    }
    content_lower = content.lower()
    for tag, keywords in keyword_map.items():
        for kw in keywords:
            if kw in content_lower:
                if tag not in tags:
                    tags.append(tag)
                break
    return tags

# 实体关键词库（更精确，避免误匹配）
ENTITY_KEYWORDS = {
    'Claude': [r'\bclaude\b', r'Claude'],
    'Claude Code': [r'Claude[\s\-]?Code', r'claude[\s\-]?code'],
    'Anthropic': [r'\bAnthropic\b', r'anthropic'],
    'OpenAI': [r'\bOpenAI\b', r'openai'],
    'ChatGPT': [r'\bChatGPT\b', r'chatgpt'],
    'GPT-4': [r'GPT[\s\-]?4'],
    'GPT-5': [r'GPT[\s\-]?5'],
    'GitHub': [r'\bGitHub\b', r'github'],
    'GitHub Copilot': [r'GitHub[\s\-]?Copilot', r'github[\s\-]?copilot'],
    'Obsidian': [r'\bObsidian\b', r'obsidian'],
    '飞书': [r'飞书', r'\bLark\b', r'\bFeishu\b'],
    'Dify': [r'\bDify\b', r'dify'],
    'Cursor': [r'\bCursor\b'],
    'Windsurf': [r'\bWindsurf\b'],
    'VS Code': [r'VS[\s\-]?Code', r'vscode'],
    'Python': [r'\bPython\b', r'python'],
    'MCP': [r'\bMCP\b', r'Model Context Protocol'],
    'OpenClaw': [r'\bOpenClaw\b', r'openclaw', r'龙虾'],
    'Hermes': [r'\bHermes\b', r'hermes[\s\-]?agent', r'爱马仕'],
    'WorkBuddy': [r'\bWorkBuddy\b'],
    'Tabbit': [r'\bTabbit\b'],
    'QwenPaw': [r'\bQwenPaw\b'],
    'QoderWake': [r'\bQoderWake\b'],
    'PUAClaw': [r'\bPUAClaw\b'],
    'Harness': [r'\bHarness\b'],
    'LangChain': [r'\bLangChain\b'],
    'Docker': [r'\bDocker\b'],
    'Figma': [r'\bFigma\b'],
    'Notion': [r'\bNotion\b'],
    '钉钉': [r'钉钉'],
    '小红书': [r'小红书'],
    '抖音': [r'抖音'],
    '微信': [r'微信'],
    'B站': [r'[Bb]站', r'哔哩哔哩', r'bilibili'],
    'FFmpeg': [r'\bFFmpeg\b'],
    'Excel': [r'\bExcel\b'],
    'Markdown': [r'\bMarkdown\b'],
    'Mermaid': [r'\bMermaid\b'],
    'SQLite': [r'\bSQLite\b'],
    'Node.js': [r'Node\.js'],
    'React': [r'\bReact\b'],
    'Next.js': [r'Next\.js'],
    'Tailwind': [r'\bTailwind\b'],
    'Supabase': [r'\bSupabase\b'],
    'Vercel': [r'\bVercel\b'],
    'Cloudflare': [r'\bCloudflare\b'],
    'OpenRouter': [r'\bOpenRouter\b'],
    'V0': [r'\bV0\b', r'v0\.dev'],
    'Bolt': [r'\bBolt\b', r'bolt\.new'],
    'Lovable': [r'\bLovable\b'],
    'DeepSeek': [r'\bDeepSeek\b', r'deepseek'],
    'Qwen': [r'\bQwen\b', r'通义'],
    'GLM': [r'\bGLM[\-\s]?\d'],
    'Llama': [r'\bLlama\b'],
    'Midjourney': [r'\bMidjourney\b'],
    'Stable Diffusion': [r'Stable[\s\-]?Diffusion'],
    'ComfyUI': [r'\bComfyUI\b'],
    '剪映': [r'剪映'],
    'Sora': [r'\bSora\b'],
    'Gemini': [r'\bGemini\b'],
    'ReAct': [r'\bReAct\b'],
    'LoRA': [r'\bLoRA\b'],
}

CONCEPT_KEYWORDS = {
    'Multi-Agent': [r'[Mm]ulti[\s\-]?[Aa]gent', r'多智能体', r'多[\s\-]?Agent'],
    'Agent架构': [r'[Aa]gent架构'],
    'Prompt工程': [r'[Pp]rompt[\s\-]?[Ee]ngineering', r'提示词工程', r'Prompt工程'],
    'RAG': [r'检索增强生成', r'Retrieval[\s\-]?Augmented'],
    'Vibe Coding': [r'[Vv]ibe[\s\-]?[Cc]oding', r'氛围编程'],
    'MCP协议': [r'MCP协议', r'Model[\s\-]?Context[\s\-]?Protocol'],
    'Skill设计': [r'[Ss]kill设计', r'Skill黄金法则'],
    '工作流自动化': [r'[Ww]orkflow', r'工作流自动化'],
    '知识管理': [r'知识管理', r'知识库引擎', r'[Pp]ersonal[\s\-]?[Kk]nowledge'],
    '代码生成': [r'[Cc]ode[\s\-]?[Gg]eneration', r'AI编程', r'代码生成'],
    '低代码': [r'[Ll]ow[\s\-]?[Cc]ode', r'低代码', r'[Nn]o[\s\-]?[Cc]ode'],
    '微服务': [r'[Mm]icroservice', r'微服务'],
    'DevOps': [r'\bDevOps\b'],
    'TDD': [r'\bTDD\b', r'[Tt]est[\s\-]?[Dd]riven'],
    '领域驱动设计': [r'\bDDD\b', r'[Dd]omain[\s\-]?[Dd]riven', r'领域驱动'],
    '事件驱动': [r'[Ee]vent[\s\-]?[Dd]riven', r'事件驱动'],
    'AI Agent': [r'AI[\s\-]?Agent', r'AI智能体'],
    '多模态': [r'[Mm]ultimodal', r'多模态'],
    '嵌入向量': [r'\bEmbedding\b', r'向量数据库'],
    '微调': [r'[Ff]ine[\s\-]?tun', r'微调'],
    '上下文工程': [r'[Cc]ontext[\s\-]?[Ee]ngineering', r'上下文工程'],
    'Function Calling': [r'[Ff]unction[\s\-]?[Cc]alling', r'[Tt]ool[\s\-]?[Uu]se'],
    '思维链': [r'[Cc]hain[\s\-]?of[\s\-]?[Tt]hought', r'\bCoT\b', r'思维链'],
    'SOP': [r'\bSOP\b', r'标准操作流程'],
    '自动化测试': [r'[Aa]utomated[\s\-]?[Tt]est', r'自动化测试'],
    'CI/CD': [r'CI[/\s\-]?CD'],
    '代码审查': [r'[Cc]ode[\s\-]?[Rr]eview', r'代码审查'],
    'PPT设计': [r'PPT设计', r'幻灯片设计'],
    '内容创作': [r'[Cc]ontent[\s\-]?[Cc]reation', r'内容创作'],
    '视频制作': [r'视频制作'],
    '数据可视化': [r'[Dd]ata[\s\-]?[Vv]isualization', r'数据可视化'],
    '浏览器自动化': [r'[Bb]rowser[\s\-]?[Aa]utomation', r'浏览器自动化'],
    '办公自动化': [r'办公自动化'],
    '业务映射': [r'业务映射', r'业务建模'],
    '设计模式': [r'[Dd]esign[\s\-]?[Pp]attern', r'设计模式'],
    '自进化系统': [r'自进化', r'self[\s\-]?evolv'],
    '记忆系统': [r'记忆系统', r'[Mm]emory[\s\-]?[Ss]ystem'],
    '知识图谱': [r'知识图谱', r'[Kk]nowledge[\s\-]?[Gg]raph'],
}

def find_entities(content):
    """从内容中识别实体（使用正则，更精确）"""
    found = set()
    for entity, patterns in ENTITY_KEYWORDS.items():
        for pat in patterns:
            if re.search(pat, content):
                found.add(entity)
                break
    return found

def find_concepts(content):
    """从内容中识别概念（使用正则，更精确）"""
    found = set()
    for concept, patterns in CONCEPT_KEYWORDS.items():
        for pat in patterns:
            if re.search(pat, content):
                found.add(concept)
                break
    return found

def make_wikilink(slug):
    """创建wikilink"""
    return f"[[{slug}]]"

def extract_summary(content, max_len=500):
    """提取文章摘要"""
    summary_lines = []
    in_code_block = False
    for line in content.split('\n'):
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        # 跳过来源行、分隔线、图片、空行
        if (stripped.startswith('> 📎') or stripped == '---' or
            stripped.startswith('![') or not stripped or
            stripped.startswith('#') or stripped.startswith('>')):
            continue
        # 清理行内图片
        cleaned = re.sub(r'!\[.*?\]\(.*?\)', '', stripped)
        cleaned = cleaned.strip()
        if cleaned:
            summary_lines.append(cleaned)
            if sum(len(l) for l in summary_lines) > max_len * 1.5:
                break

    summary = '\n'.join(summary_lines[:20])
    if len(summary) > max_len:
        summary = summary[:max_len] + "..."
    return summary

def create_source_page(filepath, category, content, title, source_name, source_url, source_date, tags, entities, concepts):
    """创建源文件摘要页"""
    slug = make_unique_slug(title, filepath)

    now = datetime.now().strftime("%Y-%m-%d")
    created = source_date if source_date else now

    entity_links = ", ".join(sorted([make_wikilink(entity_slug(e)) for e in entities]))
    concept_links = ", ".join(sorted([make_wikilink(concept_slug(c)) for c in concepts]))
    summary = extract_summary(content)

    page = f"""---
tags: [{', '.join(tags[:8])}]
source: "{source_name}"
created: {created}
updated: {now}
category: {category}
---

# {title}

> 来源: [{source_name}]({source_url}) | {created}

## 摘要

{summary}

## 相关实体

{entity_links}

## 相关概念

{concept_links}
"""

    outpath = SOURCES_DIR / f"{slug}.md"
    outpath.write_text(page, encoding='utf-8')
    return slug

def create_entity_page(entity_name, related_sources, related_concepts, descriptions):
    """创建实体页面"""
    slug = entity_slug(entity_name)
    outpath = ENTITIES_DIR / f"{slug}.md"
    now = datetime.now().strftime("%Y-%m-%d")

    source_links = "\n".join([f"- {make_wikilink(s)}" for s in sorted(related_sources)])
    concept_links = ", ".join(sorted([make_wikilink(concept_slug(c)) for c in related_concepts]))
    desc = descriptions[0] if descriptions else f"{entity_name}是一个在多篇文章中被提及的实体。"
    # 清理描述中的特殊字符
    desc = re.sub(r'[\n\r]', ' ', desc)[:200]

    content = f"""---
type: entity
name: {entity_name}
created: {now}
updated: {now}
mentions: {len(related_sources)}
---

# {entity_name}

**类型:** 实体
**提及文章数:** {len(related_sources)}

## 简介

{desc}

## 相关概念

{concept_links}

## 相关文章

{source_links}
"""
    outpath.write_text(content, encoding='utf-8')
    return slug

def create_concept_page(concept_name, related_sources, related_entities, descriptions):
    """创建概念页面"""
    slug = concept_slug(concept_name)
    outpath = CONCEPTS_DIR / f"{slug}.md"
    now = datetime.now().strftime("%Y-%m-%d")

    source_links = "\n".join([f"- {make_wikilink(s)}" for s in sorted(related_sources)])
    entity_links = ", ".join(sorted([make_wikilink(entity_slug(e)) for e in related_entities]))
    desc = descriptions[0] if descriptions else f"{concept_name}是一个在多篇文章中被讨论的概念。"
    desc = re.sub(r'[\n\r]', ' ', desc)[:200]

    content = f"""---
type: concept
name: {concept_name}
created: {now}
updated: {now}
mentions: {len(related_sources)}
---

# {concept_name}

**类型:** 概念
**提及文章数:** {len(related_sources)}

## 简介

{desc}

## 相关实体

{entity_links}

## 相关文章

{source_links}
"""
    outpath.write_text(content, encoding='utf-8')
    return slug

def extract_description(content, name):
    """从文章中提取描述"""
    # 查找实体/概念附近的描述性文本
    patterns = [
        rf'{re.escape(name)}[是为：:]\s*(.{{10,120}})',
        rf'{re.escape(name)}\s*[—\-]\s*(.{{10,120}})',
        rf'{re.escape(name)}[，,]([^。，！？\n]{{10,120}})',
    ]
    for pat in patterns:
        match = re.search(pat, content)
        if match:
            desc = match.group(1).strip()
            desc = re.sub(r'[\n\r]', ' ', desc)
            # 清理markdown标记
            desc = re.sub(r'\*\*|__|\*|_|`', '', desc)
            if len(desc) > 150:
                desc = desc[:150] + "..."
            return desc
    return ""

def process_all():
    """处理所有文章"""
    # 收集所有md文件
    all_files = []
    for root, dirs, files in os.walk(SOURCE_DIR):
        dirs[:] = [d for d in dirs if d != '__pycache__']
        for f in files:
            if f.endswith('.md'):
                filepath = Path(root) / f
                category = filepath.parent.name
                all_files.append((filepath, category))

    print(f"共找到 {len(all_files)} 篇文章")

    stats = {
        'total': len(all_files),
        'sources_created': 0,
        'entities_created': 0,
        'concepts_created': 0,
    }

    # 全局收集
    entity_data = defaultdict(lambda: {'sources': set(), 'concepts': set(), 'descriptions': []})
    concept_data = defaultdict(lambda: {'sources': set(), 'entities': set(), 'descriptions': []})
    source_info = []

    # 第一遍：处理文章
    for i, (filepath, category) in enumerate(all_files):
        try:
            content = filepath.read_text(encoding='utf-8')
        except Exception as e:
            print(f"  跳过: {filepath.name} ({e})")
            continue

        source_name, source_url, source_date = extract_frontmatter(content)
        title = extract_title(content, filepath)
        tags = extract_tags(content, category)
        entities = find_entities(content)
        concepts = find_concepts(content)

        source_slug = create_source_page(
            filepath, category, content, title,
            source_name, source_url, source_date,
            tags, entities, concepts
        )
        source_info.append((source_slug, title, category, tags))
        stats['sources_created'] += 1

        for entity in entities:
            entity_data[entity]['sources'].add(source_slug)
            entity_data[entity]['concepts'].update(concepts)
            desc = extract_description(content, entity)
            if desc and desc not in entity_data[entity]['descriptions']:
                entity_data[entity]['descriptions'].append(desc)

        for concept in concepts:
            concept_data[concept]['sources'].add(source_slug)
            concept_data[concept]['entities'].update(entities)
            desc = extract_description(content, concept)
            if desc and desc not in concept_data[concept]['descriptions']:
                concept_data[concept]['descriptions'].append(desc)

        if (i + 1) % 100 == 0:
            print(f"  已处理 {i + 1}/{len(all_files)} 篇...")

    print(f"Source页面: {stats['sources_created']}")
    print(f"发现 {len(entity_data)} 个实体, {len(concept_data)} 个概念")

    # 第二遍：实体页面
    for entity, data in sorted(entity_data.items()):
        create_entity_page(entity, data['sources'], data['concepts'], data['descriptions'])
        stats['entities_created'] += 1

    # 第三遍：概念页面
    for concept, data in sorted(concept_data.items()):
        create_concept_page(concept, data['sources'], data['entities'], data['descriptions'])
        stats['concepts_created'] += 1

    # 更新index
    update_index(source_info, entity_data, concept_data)
    # 更新log
    update_log(stats)

    return stats

def update_index(source_info, entity_data, concept_data):
    """更新索引"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    # 按category分组
    by_cat = defaultdict(list)
    for slug, title, cat, tags in source_info:
        by_cat[cat].append((slug, title))

    src_section = ""
    for cat in sorted(by_cat.keys()):
        items = by_cat[cat]
        src_section += f"\n### {cat} ({len(items)}篇)\n\n"
        for slug, title in sorted(items, key=lambda x: x[1])[:50]:  # 每个类别最多显示50篇
            src_section += f"- [[{slug}]] - {title}\n"
        if len(items) > 50:
            src_section += f"- ...(共{len(items)}篇，省略{len(items)-50}篇)\n"

    ent_section = ""
    for entity, data in sorted(entity_data.items()):
        slug = entity_slug(entity)
        ent_section += f"- [[{slug}]] ({len(data['sources'])}篇)\n"

    con_section = ""
    for concept, data in sorted(concept_data.items()):
        slug = concept_slug(concept)
        con_section += f"- [[{slug}]] ({len(data['sources'])}篇)\n"

    content = f"""# Index

Master catalog of all wiki pages. Updated on {now}

## Sources ({len(source_info)}篇)
{src_section}

## Entities ({len(entity_data)}个)
{ent_section}

## Concepts ({len(concept_data)}个)
{con_section}

## Synthesis

"""

    (WIKI_DIR / "index.md").write_text(content, encoding='utf-8')

def update_log(stats):
    """更新日志"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    log_path = WIKI_DIR / "log.md"

    entry = f"""## {now} - 批量摄入

- 处理文章总数: {stats['total']}
- 创建Source页面: {stats['sources_created']}
- 创建实体页面: {stats['entities_created']}
- 创建概念页面: {stats['concepts_created']}

"""

    log_path.write_text(entry, encoding='utf-8')

if __name__ == '__main__':
    print("开始知识库摄入 v2...")
    stats = process_all()
    print(f"\n摄入完成!")
    print(f"  Source: {stats['sources_created']}")
    print(f"  实体: {stats['entities_created']}")
    print(f"  概念: {stats['concepts_created']}")
