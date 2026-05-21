# Log

Chronological record of all operations.

## 2026-05-22 — WeChat Article Batch 3 Ingestion

**Operator:** Hermes Agent (batch ingestion task)
**Source:** 微信公众号/ (4 articles processed)
**Time:** 2026-05-22

### Results

- **Sources processed:** 4
- **Categories:** WorkBuddy (2), Obsidian/LLM-Wiki (1), Harness Engineering (1)
- **Source pages created:** 4 (wiki/sources/)
- **Entity pages updated:** none
- **Concept pages created:** none
- **index.md updated:** Statistics (Sources +4), WorkBuddy (32→34), Harness Engineering (1→2), LLM-Wiki (added entry)

### New Articles

| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | WorkBuddy | WorkBuddy 4个核心技巧：腾讯官方亲授 | workbuddy-4-core-techniques |
| 2 | WorkBuddy | ima知识库+WorkBuddy入门指南 | workbuddy-ima-getting-started-guide |
| 3 | Obsidian | 别再收藏吃灰：搭一个能追问自己的知识库 | obsidian-追问自己的知识库 |
| 4 | SkillManager | fireworks-tech-graph Skill画图吊打mermaid | fireworks-tech-graph-skill |

### Notes

- WorkBuddy技巧：腾讯官方4个核心使用技巧（清晰表达、拆解任务、多轮打磨、先本地后远程）
- ima+WorkBuddy入门：30分钟跑通AI工作流，ima负责"记住"，WorkBuddy负责"动手"
- Obsidian追问知识库：LLM-Wiki实践，从小主题闭环开始，入口自动化+校验
- fireworks-tech-graph：自然语言生成架构图Skill，支持7种视觉风格和AI领域图案

---

## 2026-05-22 — Scrapling 爬虫框架摄入

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/ (5 articles processed)
**Time:** 2026-05-22

### Results

- **Sources processed:** 5
- **Categories:** LLM Wiki (1), AI生成PPT方案 (1), Obsidian (1), MarkItDown (1), AI工具 (1)
- **Source pages created:** 5 (wiki/sources/)
- **Entity pages updated:** none
- **Concept pages created:** none
- **index.md updated:** Statistics updated, sections expanded

### New Articles

| ID | 分类 | 标题 | 源摘要页 |
|---|---|---|---|
| 1 | LLM Wiki | 超级记忆系统，融合 Karpathy LLM Wiki、知识图谱、混合搜索的新一代记忆系统 | super-memory-system.md |
| 2 | AI生成PPT方案 | 老板：以后全公司的 PPT 你自己做吧！ | ai-ppt-template-library.md |
| 3 | Obsidian | 收藏 200 篇文章后，我用Hermes+Obsidian搭了一套自动化个人知识库 | hermes-obsidian-auto-knowledge-base.md |
| 4 | MarkItDown | 近 10 万 Star！一行命令把 PDF、Word、Excel 全转成 Markdown | markitdown-document-converter.md |
| 5 | AI工具 | 装上drawio skill，让AI帮你画各种图（流程图、架构图等） | drawio-skill-ai-diagrams.md |

### Key Concepts Identified

- **agentmemory**: 三层记忆系统（BM25 + 向量 + 知识图谱），RRF融合检索
- **beautiful-html-templates**: 32个HTML PPT模板库，让Agent生成精美PPT
- **BrowserOS**: 定时采集资讯，替代爬虫处理动态页面
- **Web Clipper**: Obsidian官方浏览器扩展，一键保存文章
- **drawio skill**: 官方MCP skill，让AI画流程图/架构图

### Notes

- LLM-Wiki section expanded to 11篇
- Hermes section expanded to 197篇  
- Obsidian section expanded to 31篇
- MarkItDown section expanded to 4篇
- AI生成PPT方案 section expanded to 2篇
- AI工具 section expanded to 9篇

---

## 2026-05-22 — 微信公众号文章摄入（Batch 2）

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/ (4 articles processed)
**Time:** 2026-05-22

### Results

- **Sources processed:** 4
- **Categories:** LLM Wiki (1), Agent (1), MarkItDown (1), skill-CLI-Anything (1)
- **Source pages created:** 4 (wiki/sources/)
- **Entity pages updated:** none
- **Concept pages created:** none
- **index.md updated:** Statistics (Sources 1068→1072), LLM Wiki +1, Agent +1, MarkItDown +1, skill-CLI-Anything +1

### New Articles

| ID | 分类 | 标题 | 源摘要页 |
|---|---|---|---|
| 1 | LLM Wiki | AI 知识库技术演进拆解：从 RAG 到 NotebookLM，再到 LLM Wiki | ai-knowledge-base-evolution-rag-notebooklm-llmwiki.md |
| 2 | Agent | AI Agent 的万能遥控器：CLI-Anything 让所有软件都能被智能体直接调用 | cli-anything-universal-remote-for-ai-agent.md |
| 3 | MarkItDown | 不到 1000 行代码，让本地 .md 文件在浏览器里拥有在线一样的阅读体验 | markdown-browser-extension-1000-lines.md |
| 4 | skill-CLI-Anything | Skill 是怎么悄悄变成 SOP 的 | skill-becoming-sop.md |

### Notes

- RAG演进文章：系统拆解NotebookLM七层架构，对比LLM Wiki理念
- CLI-Anything文章：HKUDS开源项目，一行命令把任意软件变成Agent可操作CLI
- Markdown浏览器插件：1000行代码实现，三档主题+Wiki-link支持
- Skill设计思考：Skill与SOP的本质区别，路径选择权是核心

## 2026-05-22 — Scrapling 爬虫框架摄入

**Operator:** hermes-pachong（手动触发）
**Source:** GitHub — D4Vinci/Scrapling
**Time:** 2026-05-22

### Results

- **Source page:** 已存在 wiki/sources/Scrapling-自适应Web爬虫框架-绕Cloudflare-自适应解析-Spider.md（前序会话创建）
- **Entity pages created:** 1 — [[Scrapling]]
- **Entity pages updated:** 0
- **Concept pages created:** 0
- **index.md updated:** GitHub 分类 +1

## 2026-05-21 — 微信公众号文章同步摄入（第十三批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (5 new articles processed)
**Time:** 2026-05-21 18:00

### Results

- **Sources processed:** 5
- **Categories:** Obsidian (3 new), GitHub (1 new), Zero-to-CAD (1 new)
- **Source pages created:** 5 (wiki/sources/)
- **Entity pages updated:** none
- **Concept pages created:** none
- **concept-table.md updated:** 0
- **index.md updated:** Statistics (Sources 1049→1054), Obsidian (27→30篇), GitHub (24→25篇), Zero-to-CAD (3→4篇)

### New Articles

| ID | 分类 | 标题 |
|---|---|---|
| 755 | Obsidian | LLM Wiki：8.4K Stars！一个能自我构建的AI个人知识库，超越Obsidian |
| 756 | Obsidian | Obsidian官方同步贵？在NAS上自建服务器，实现多端笔记完美同步 |
| 757 | Zero-to-CAD | Zero-to-CAD：从零到CAD生成百万可编辑程序 |
| 758 | Obsidian | Hermes+Obsidian+LLM Wiki搭建本地知识库 |
| 759 | GitHub | 这个 GitHub 神级 Skill：一句话把你开发的网站发布到线上（PinMe） |

### Notes

- All wxrobot queue: pending=5, success=749
- Fast Note Sync (ID 756) - NAS上的Obsidian同步解决方案，替代官方同步
- LLM Wiki articles (ID 755, 758) - 两次不同角度介绍 Hermes+Obsidian+LLM Wiki 组合

## 2026-05-21 — 微信公众号文章同步摄入（第十二批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (2 new articles processed)
**Time:** 2026-05-21 00:01

### Results

- **Sources processed:** 2
- **Categories:** Skill-SD (1 new), Skills (1)
- **Source pages created:** 2 (Skill-SD-技能引导老师而非学生.md, Agent-Skills-会不会淘汰-Coze-Dify-N8N-等低代码平台.md)
- **Entity pages updated:** none
- **Concept pages created:** none
- **concept-table.md updated:** 0
- **index.md updated:** Statistics (Sources 1034→1036), new Skill-SD section (1篇), Skills section (55→57篇)

### New Articles

| ID | 分类 | 标题 |
|---|---|---|
| 753 | Skill-SD | Skill-SD：技能引导老师而非学生 |
| 754 | Skills | Agent Skills 会不会淘汰 Coze、Dify、N8N 等低代码平台？ |

### Notes

- All wxrobot queue: pending=0, success=744
- Skill-SD is a new category (from arXiv:2604.10674 research paper)
- Skills article discusses Coze/Dify/N8N vs Agent Skills comparison and business KnowHow

## 2026-05-20 — 微信公众号文章同步摄入（第十一批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (2 new articles processed)
**Time:** 2026-05-20 18:00

### Results

- **Sources processed:** 2
- **Categories:** Vibe Coding (1 reprocessed), WorkBuddy (1 new)
- **Source pages created:** 1 (WorkBuddy方法15-竞品数据抓取与对比分析.md)
- **Entity pages updated:** WorkBuddy.md (mentions 11→12)
- **Concept pages created:** none
- **concept-table.md updated:** added 竞品监控 (1)
- **index.md updated:** WorkBuddy section (added method 15 entry)

### New Articles

|| ID | 分类 | 标题 ||
|---|---|---||
|| 751 | Vibe Coding | 发明Vibe Coding的人说它过时了，我想了很久为什么 (duplicate reprocessed, source page already existed) ||
|| 752 | WorkBuddy | WorkBuddy方法15 | 竞品数据抓取与对比分析：知己知彼 ||

### Concepts Added

- 竞品监控 — 利用AI自动抓取竞品信息并生成对比分析表的工作流

### Notes

- Vibe Coding article was already ingested in batch 10 (12:00); _1 suffix file is duplicate
- All wxrobot queue: pending=0, success=742

## 2026-05-20 — 微信公众号文章同步摄入（第十批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (1 new article processed)
**Time:** 2026-05-20 12:00

### Results

- **Sources processed:** 1
- **Categories:** Vibe Coding (1)
- **Source pages created:** 1 (发明Vibe-Coding的人说它过时了-我想了很久为什么.md)
- **Entity pages created:** none
- **Concept pages created:** 1 (Agentic-Engineering.md)
- **concept-table.md updated:** Vibe-Coding (21→22), Agentic-Engineering added
- **index.md updated:** Vibe Coding (5→6), new section Agentic Engineering (1)

### New Articles

| ID | 分类 | 标题 |
|---|---|---|
| 751 | Vibe Coding | 发明Vibe Coding的人说它过时了，我想了很久为什么 |

### Concepts Added

- Agentic Engineering — Vibe Coding 的接替范式，由 Karpathy 2026 年提出

### Notes

- Vibe Coding category header corrected: removed misfiled "一人公司AI工具全家桶2-7k-Star"
- All wxrobot queue: pending=1, success=741

## 2026-05-20 — 微信公众号文章同步摄入（第九批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (2 new articles processed)
**Time:** 2026-05-20 06:00

### Results

- **Sources processed:** 2
- **Categories:** Skills (1), HeyGen (1)
- **Source pages created:** 2 (分享3个宝藏Skills.md, HeyGen-HyperFrames-15K-Star.md)
- **Entity pages created:** 3 (HeyGen.md, HyperFrames.md, GSAP.md)
- **Concept pages created:** none
- **concept-table.md updated:** 0
- **index.md updated:** Statistics, Sources, Entities sections

### New Articles

|| ID | 分类 | 标题 |
|---|---|---|
|| 749 | Skills | 分享3个宝藏Skills |
|| 750 | HeyGen | 15K Star 一夜刷屏！HeyGen 开源 HyperFrames，让 AI 用 HTML 生成 |

### Entities Added

- HeyGen — AI视频生成公司
- HyperFrames — HTML到视频渲染框架
- GSAP — GreenSock动画库

---

## 2026-05-20 — 微信公众号文章同步摄入（第八批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (1 new article processed)
**Time:** 2026-05-20 00:00

### Results

- **Sources processed:** 1
- **Categories:** RPA (1)
- **Source pages created:** 1 (RPA-数据可视化-全链路自动化.md)
- **Entity pages created/updated:** none
- **Concept pages created:** 1 (RPA.md)
- **concept-table.md updated:** 1

### New Articles

||| ID | 分类 | 标题 |
|---|---|---|---|
||| 748 | RPA | RPA+数据可视化：打通数据采集到智能决策的全链路自动化 |

---

## 2026-05-19 — 微信公众号文章同步摄入（第七批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (1 new article processed)
**Time:** 2026-05-19 06:00

### Results

- **Sources processed:** 1
- **Categories:** Skills (1)
- **Source pages created:** 1 (cnki-research-toolkit.md)
- **Entity pages created/updated:** none
- **Concept pages created:** none
- **concept-table.md updated:** 0

### New Articles

|| ID | 分类 | 标题 |
||---|---|---|
|| 745 | Skills | 这个skills可以帮你查知网，导入 Zotero！ |

---

## 2026-05-19 — 微信公众号文章同步摄入（第六批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (3 new articles processed)
**Time:** 2026-05-19 00:01

### Results

- **Sources processed:** 3
- **Categories:** Agent (1), AgentTeam (1), QwenPaw (1)
- **Source pages created:** 3 (大明PPT-Agent-Team.md, SpectrAI-多AI协同工作站.md, 养虾免费Token-OpenRouter.md)
- **Entity pages created/updated:** none (all entities already existed)
- **Concept pages created:** none
- **concept-table.md updated:** 0

### New Articles

| ID | 分类 | 标题 |
|---|---|---|
| 742 | Agent | 朕不想做PPT，于是创造了大明PPT Agent Team |
| 743 | AgentTeam | [开源]一款面向开发者与团队的多 AI 协同工作站，一个人指挥一支 AI 团队 |
| 744 | QwenPaw | 终于找到养虾的免费Token，一直有，直接用！ |

---

## 2026-05-18 — 微信公众号文章同步摄入（第五批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (1 new article processed)
**Time:** 2026-05-18 18:00

### Results

- **Sources processed:** 1
- **Categories:** WorkBuddy (1)
- **Source pages created:** 1 (wiki/sources/WorkBuddy-从入门到精通-全套20篇目录.md)
- **Entity pages created/updated:** none (WorkBuddy entity already existed)
- **Concept pages created:** none
- **concept-table.md updated:** 0

### New Articles

| ID | 分类 | 标题 |
|---|---|---|
| 741 | WorkBuddy | WorkBuddy 从入门到精通｜全套 20 篇目录 |

---

## 2026-05-18 — 微信公众号文章同步摄入（第四批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (1 new article processed)
**Time:** 2026-05-18 12:00

### Results

- **Sources processed:** 1
- **Categories:** QoderWork (1)
- **Source pages created:** 1 (wiki/sources/6款桌面AI助手横评.md)
- **Entity pages created/updated:** QoderWork.md (new), WorkBuddy.md (updated)
- **Concept pages created:** 桌面AI助手.md (new)
- **concept-table.md updated:** 1 new concept added

### New Articles

| ID | 分类 | 标题 |
|---|---|---|
| 740 | QoderWork | 6款桌面AI助手我试了两个月，便宜的太不稳定，能力强的太烧钱 |

---

## 2026-05-18 — 微信公众号文章同步摄入（第三批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (2 new articles processed)
**Time:** 2026-05-18 06:00

### Results

- **Sources processed:** 2
- **Categories:** LLM-Wiki (1), Skills (1)
- **Index stats updated:** Sources 1023→1024
- **Source pages created:** 1 (wiki/sources/739-...)
- **Sections updated:** Skills 53→54

### New Articles

| ID | 分类 | 标题 |
|---|---|---|
| 738 | LLM-Wiki | Hermes + Obsidian + LLM Wiki：搭建一个会自己长大的本地知识库 |
| 739 | Skills | 2026年5月最火 AI Agent Skills 完整盘点! 让你的工作效率提升10倍 |

---

## 2026-05-18 — 微信公众号文章同步摄入

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (7 new articles processed)
**Time:** 2026-05-18 00:07

### Results

- **Sources processed:** 7
- **Categories:** LLM-Wiki (1), Skills (1), 企业应用 (1), OpenHuman (1), wx-cli (1), AI数据分析 (1), CAD (1)
- **Index stats updated:** Sources 1016→1023, Entities 156→163, Concepts 111→118
- **Source pages created:** 7 (wiki/sources/)
- **Sections updated:** LLM-Wiki 8→9, Skills 52→53, 企业应用 2→3

### New Articles

| ID | 分类 | 标题 |
|---|---|---|
| 732 | OpenHuman | 开源的个人AI超级智能：让你的AI真正认识你 |
| 733 | Skills | 别再把AgentSkills塞进代码仓库了，我做了个一键部署的团队版Skills分发平台 |
| 734 | wx-cli | 一行命令搞定公众号文章：wx-cli让我重新理解了什么叫信息获取 |
| 735 | AI数据分析 | 进阶AI数据分析：AI+Python搭建全能数据分析智能体 |
| 736 | CAD | text-to-cad：和它对话就能做建筑设计方案 |
| 737 | 企业应用 | 我来预测下一代企业数字化架构：系统CLI化、流程Skill化、员工Agent化 |
| 738 | LLM-Wiki | Hermes + Obsidian + LLM Wiki：搭建一个会自己长大的本地知识库 |

---


---

## 2026-05-17 — 微信公众号文章同步摄入（第二批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (10 new articles processed)
**Time:** 2026-05-17 18:00

### Results

- **Sources processed:** 10
- **Categories:** Hermes (3), GitHub (2), Zero-to-CAD (2), OpenClaw (1), AI技术 (1), 浏览器自动化 (1)
- **New section created:** Zero-to-CAD (2篇)
- **Index stats updated:** Sources 1006→1016
- **Source pages created:** 10 (wiki/sources/)
- **Categories updated:** AI技术 12→13, GitHub 22→24, Hermes 193→196, OpenClaw 134→135, 浏览器自动化 5→6

### New Articles

| ID | 分类 | 标题 |
|---|---|---|
| 709 | AI技术 | 用自然语言生成可编辑参数化3D CAD模型 |
| 710 | GitHub | 推荐 8 个本周 YYDS 的 GitHub 开源项目 |
| 711 | Hermes | Hermes 出桌面版了：AI Agent 终于不用只活在命令行里 |
| 712 | Zero-to-CAD | Zero-to-CAD：AI 三维CAD设计的新分水岭 |
| 713 | GitHub | GitHub 2万星爆款：让AI接管你的浏览器，这个开源项目太强了 |
| 714 | Zero-to-CAD | 说话就能建模，AI 直接生成可导出的 CAD 模型 |
| 715 | OpenClaw | OpenClaw 和 Hermes直接画CAD，一天2.5k Star — text-to-cad开源了 |
| 716 | Hermes | Hermes Agent 自动化进阶：用 Cron 解锁 24/7 无人值守工作流 |
| 717 | 浏览器自动化 | 浏览器自动化神器 agent-browser 使用教程 |
| 718 | Hermes | 配够了 Hermes Agent 的 Profile 和 Skill？试试 OpenHuman：零配置，连上就懂你 |

---

## 2026-05-17 — 微信公众号文章同步摄入

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (7 new articles processed)
**Time:** 2026-05-17 12:00

### Results

- **Sources processed:** 7
- **Categories:** AI生成PPT方案 (1), WorkBuddy (3), Hermes (1), mmx-cli (1), AI短剧 (1)
- **Entity pages created:** 7 (Oh-My-PPT, Hermes-Slate-Desk, MoneyPrinterTurbo, AutoClip, Hailuo, Image-01, Speech)
- **Concept pages created:** 7 (本地优先, HTML演示, CLI工具, AI助手集成, AI自动化, AI笔记, 多模态交互)
- **Index stats updated:** Sources 999→1006, Entities 149→156, Concepts 104→111

---

## 2026-05-16 — 微信公众号文章同步摄入

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (7 new articles processed)
**Time:** 2026-05-16 18:00

### Results

- **Sources processed:** 7
- **Categories:** AI生成PPT方案 (1), WorkBuddy (3), Hermes (1), mmx-cli (1), AI短剧 (1)
- **Source pages created:** 7
- **New sections added:** AI生成PPT方案, mmx-cli

### Articles Added

**AI生成PPT方案 (1):**
- [[702-Oh-My-PPT-开源免费纯本地AI幻灯片神器-一句话生成可拖拽编辑HTML-PPT-30-风格-动画-公式-历史回退-创业路演-教学汇报零云依赖]] — Oh My PPT：开源免费纯本地AI幻灯片神器

**WorkBuddy (3):**
- [[703-腾讯ima实操手册四-给ima配个数字员工-WorkBuddy基础玩法-不用写一行代码]] — 腾讯ima实操手册（四）
- [[706-WorkBuddy操作指南-这15条命令让你每天省出2小时-从聊天到替你干活]] — WorkBuddy操作指南
- [[708-WorkBuddy核心玩法拆解-3种模式-Skills-MCP-效率直接拉满]] — WorkBuddy核心玩法拆解

**mmx-cli (1):**
- [[704-mmx-cli-一句话让AI助手拥有全模态能力]] — mmx-cli: 一句话让AI助手拥有全模态能力

**Hermes (1):**
- [[707-把-Hermes-Agent-装进一个真正能每天用的桌面工作台-Hermes-Slate-Desk-V2-0]] — Hermes Slate Desk V2.0

**AI短剧 (1):**
- [[705-57k-Star-4个免费开源工具-帮你全自动搞定短视频创作全流程]] — 57k+ Star！4个免费开源工具

### Entities Mentioned

Oh-My-PPT, Electron, Anime.js, KaTeX, WorkBuddy, 腾讯ima, IMA知识库, mmx-cli, MiniMax, Hailuo, MoneyPrinterTurbo, Hermes-Slate-Desk, MCP

### Concepts Covered

PPT制作, 本地优先, AI驱动, HTML演示, AI数字员工, AI办公, 工作流自动化, 多模态, CLI工具, AI助手集成, 视频制作, 内容创作, AI自动化, Skill编排, Workspace工作区

---


## 2026-05-15 — 微信公众号文章同步摄入

**Operator:** Automated ingestion (微信同步)
**Source:** 微信公众号/ (4 new articles processed)
**Time:** 2026-05-15 12:00

### Results

- **Sources processed:** 4
- **Categories:** 知识库 (1), Skills (2), Obsidian (1)
- **Source pages created:** 4

### Articles Added

**知识库 (1):**
- [[别再手动整理文章了-用-AIWiki-把链接变成可复用知识库]] — 别再手动整理文章了！用 AIWiki 把链接变成可复用知识库

**Skills (2):**
- [[分享4个新发现的宝藏Skills]] — 分享4个新发现的宝藏Skills
- [[78K-Star的AI编程Skills-grill-me-需求访谈Skill]] — 78K Star的AI编程Skills：在开发前，先让grill-me对你做一个"需求访谈"

**Obsidian (1):**
- [[Obsidian-Claudian-飞书CLI-知识管理王炸组合]] — Obsidian × Claudian × 飞书CLI = 知识管理王炸组合，我的第二大脑升级之路

### Notes

- 5 additional articles (IDs 670, 688-692) remain in processing queue due to API auth errors
- Run timed out at 300s; manual retry needed

---

## 2026-05-14 — 微信公众号文章批量摄入（第二次）

**Operator:** Automated ingestion (微信同步)
**Source:** 微信公众号/ (5 files processed, 1 failed/stub)
**Time:** 2026-05-14 12:00

### Results

- **Sources processed:** 4 (1 stub/failed: GitHub建模革命)
- **Categories:** ComfyUI (1), AI Coding (1), OpenCode+Docs MCP (1), AI技术 (1)
- **Source pages created:** 4
- **Failed/Skipped:** 1 (GitHub建模革命 — 内容抓取失败，仅有来源行)

### Articles Added

**ComfyUI (1):**
- 用自然语言生成 ComfyUI 工作流：我写了一个 AI Skill，彻底告别手动连线

**AI Coding (1):**
- [开源]一个现代化的智能客服系统，AI + 人工一体、可私有化部署

**OpenCode + Draw.io MCP (1):**
- OpenCode + Draw.io MCP 让 AI 替你搞定架构图

**AI技术 (1):**
- AI时代的团队，需要更多的"团长"

**Skipped (1):**
- GitHub开源"建模革命"：这个不到200MB的工具，靠一张照片几秒生成3D资产（内容为空/抓取失败）

## 2026-05-14 — 微信公众号文章批量摄入

**Operator:** Automated ingestion (微信同步)
**Source:** 微信公众号/ (3 files)
**Time:** 2026-05-14

### Results

- **Sources processed:** 3
- **Categories:** Agent (1), skill-CLI-Anything (1), Obsidian (1)
- **Source pages created:** 3
- **Entity pages created:** 4 (LibTV, ai-gameplay-pack-skill, Tasks插件, Day-Planner插件)

### Articles Added

**Agent (1):**
- 企业落地 AI Agent，第一批最容易跑通的 10 个低风险场景

**skill-CLI-Anything (1):**
- Skill结合哩布哩布LibTV，轻松做出AI实机视频！

**Obsidian (1):**
- Obsidian 任务管理三件套：Tasks + Kanban + Day Planner 完整指南

---

## 2026-05-13 — 微信公众号文章批量摄入

**Operator:** Automated ingestion (微信同步)
**Source:** 微信公众号/ (23 files)
**Time:** 2026-05-13

### Results

- **Sources processed:** 23
- **Categories:** Agent (2), LLM Wiki (1), MarkItDown (1), OpenClaw (1), Skills (2), WorkBuddy (16)
- **Source pages created:** 23

### Articles Added

**Agent (2):**
- 力荐！这个Skill，让你的Agent有了一双真正的眼睛，抓取网页再也不是难事了
- Agent 技能夜间自进化——阿里开源 SkillClaw，最高提升 88%

**LLM Wiki (1):**
- Karpathy 的 LLM Wiki 模式：让 AI 替你维护知识库

**MarkItDown (1):**
- PDF、Word、Excel、PPT等 全扔进一个命令：markitdown 让我重新相信文档预处理

**OpenClaw (1):**
- 别乱装！OpenClaw 53个官方技能安全清单

**Skills (2):**
- 别再把 Skill 当插件用了，这 18 个最值得装的 Skills 我帮你筛完了
- 分享15个自用的Skills

**WorkBuddy (16):**
- 报表分析也能"生产线化"：WorkBuddy 打造自动化财报分析 Skill
- 方法01｜用WorkBuddy 1分钟生成周报
- 用WorkBuddy实现内容和知识获取，再交由IMA知识库实现播客生成
- WorkBuddy 标书 Skill -招标文件智能解析
- WorkBuddy从入门到精通：9个使用技巧
- WorkBuddy方法02-会议纪要智能整理
- WorkBuddy方法03-文档批量格式转换
- WorkBuddy方法04-智能合同生成
- WorkBuddy方法05-多文档合并与目录生成
- WorkBuddy方法06-扫描件PDF文字提取
- WorkBuddy方法08-邮件模板批量生成
- WorkBuddy方法09-制式文档自动生成
- WorkBuddy方法10-多语言文档翻译
- WorkBuddy「探索」：新功能深度解读
- workbuddy真的行！生产力skills推荐
- WorkBuddy 智能操控实战

## 2026-05-10 — Hermes Agent 文章批量摄入

**Operator:** Automated ingestion (Hermes专项)
**Source:** 微信公众号/Hermes/ (181 files)
**Time:** 2026-05-10

### Results

- **Sources processed:** 181 (Hermes专题)
- **Entity pages created:** 25 (Hermes相关实体)
- **Concept pages created:** 19 (Hermes相关概念)
- **Synthesis pages created:** 1 (Hermes Agent 知识全景)

### Top Entities (Hermes生态)

1. Hermes Agent -- 180 mentions
2. Hermes -- 179 mentions
3. 飞书 -- 58 mentions
4. Claude -- 57 mentions
5. Telegram -- 55 mentions
6. 微信 -- 49 mentions
7. Docker -- 46 mentions
8. OpenAI -- 43 mentions
9. macOS -- 30 mentions
10. Honcho -- 13 mentions

### Top Concepts (Hermes生态)

1. Skills技能系统 -- 146 articles
2. Agent架构 -- 113 articles
3. Token优化 -- 105 articles
4. Context上下文 -- 96 articles
5. 记忆系统 -- 83 articles
6. 定时任务 -- 72 articles
7. Prompt工程 -- 70 articles
8. Webhook自动化 -- 70 articles
9. Profile系统 -- 52 articles
10. RAG检索增强 -- 46 articles

### Tags Distribution

- 安装部署: 64 articles
- Hermes Agent: 33 articles
- 深度解析: 22 articles
- 多Agent协作: 21 articles
- 平台接入: 21 articles
- 实战案例: 13 articles
- Skills技能: 12 articles
- 自进化机制: 12 articles
- 记忆系统: 12 articles
- 模型与成本: 11 articles
- WebUI界面: 11 articles
- 自动化: 9 articles
- 版本更新: 9 articles
- 命令操作: 9 articles
- 多媒体能力: 6 articles
- 企业应用: 5 articles
- 工具集成: 4 articles
- RAG检索: 3 articles
- Harness框架: 3 articles
- 研究报告: 3 articles
- 测试: 1 articles

---

## 2026-05-10 — Skills Directory Batch Ingest

**Action:** Ingested 52 articles from Skills directory

**Created:**
- 52 source summary pages in `wiki/sources/`
- 40 entity pages in `wiki/entities/`
- 23 concept pages in `wiki/concepts/`

**Key Topics Covered:**
- Skill 设计模式和最佳实践
- Harness Engineering 和 AI 工程化
- Skill 编排和 Skill Architecture
- PPT 制作工具（ppt-master, html-ppt-skill）
- Skill 管理工具（skills-manage, aweskill）
- MCP 协议和 Skills 的关系
- Agent 开发和多 Agent 协作
- 内容创作 Skills（baoyu-skills）
- 产品经理和项目经理 Skills
- 科研和论文写作 Skills

---
---

## 2026-05-10 — 全量知识库摄入（v2脚本）

**操作:** 对微信公众号目录下所有文章进行全量知识库摄入
**时间:** 2026-05-10
**处理脚本:** wiki/ingest.py (v2)

### 总体统计

- 原始文章总数: 530
- Source摘要页: 856 (含之前已摄入的Hermes/OpenClaw/Skills + 本次新增)
- 实体页面: 113
- 概念页面: 83
- 覆盖目录: 40+ 个子目录

### 按目录覆盖

| 目录 | 文章数 | 状态 |
|------|--------|------|
| Hermes | 181 | 已摄入 |
| OpenClaw | 112 | 已摄入 |
| Skills | 52 | 已摄入 |
| Agent | 30 | 已摄入 |
| Claude | 27 | 已摄入 |
| Obsidian | 18 | 已摄入 |
| GitHub | 16 | 已摄入 |
| AI技术 | 10 | 已摄入 |
| 飞书 | 8 | 已摄入 |
| PPT skill | 8 | 已摄入 |
| Harness | 7 | 已摄入 |
| PPT制作 | 6 | 已摄入 |
| PPT Master | 6 | 已摄入 |
| AI办公 | 5 | 已摄入 |
| AI Coding | 5 | 已摄入 |
| Vibe Coding | 4 | 已摄入 |
| 其余小目录 | ~55 | 已摄入 |

### 高频实体 Top 10

1. Claude (228 mentions)
2. Hermes (200+ mentions)
3. OpenClaw (180+ mentions)
4. MCP (150+ mentions)
5. GitHub (120+ mentions)
6. Python (100+ mentions)
7. OpenAI (80+ mentions)
8. Claude Code (70+ mentions)
9. 飞书 (60+ mentions)
10. Docker (50+ mentions)

### 高频概念 Top 10

1. Multi-Agent
2. AI Agent
3. Prompt工程
4. MCP协议
5. Skill设计
6. 上下文工程
7. 代码生成
8. Vibe Coding
9. 知识管理
10. RAG

---

## 2026-05-11 — 批量摄入（9篇微信文章）

**Operator:** Automated ingestion (Hermes Cron)
**Source:** 微信公众号/ (9 files)
**Time:** 2026-05-11

### Sources Processed

1. Playwright 又出新东西了：三个 Agent 帮你全自动写测试
2. 一种新的 LLM Wiki 方法论：让 AI 帮你建一个能活下去的知识库
3. Multica：把编码 Agent 当成团队成员管理的开源平台
4. 2万字超长实战 Karpathy 的 LLM Wiki
5. 别再手动整理笔记了！Claude+Obsidian打造永不遗忘的AI知识系统
6. Karpathy LLM-Wiki Skill 已开源公开
7. Graphify：把 Karpathy 的 LLM Wiki 从理念变成了产品
8. Karpathy 的知识库构想被人做成桌面应用了
9. 利用AI Agent一句话完成Karpathy的llm-wiki知识库搭建

### Entity Pages Updated/Created

- Graphify (新建)
- Multica (更新)
- Claudian (新建)
- Playwright Test Agents (新建)
- llm_wiki桌面应用 (新建)

### Concept Pages Updated/Created

- LLM Wiki方法论 (新建)
- 知识图谱构建 (新建)
- Managed Agents (新建)
- 自动化测试 (新建)

### Statistics Update

- Sources: 884 → 893 (+9)
- Entities: 118 → 122 (+4)
- Concepts: 97 → 101 (+4)

---

*End of log*

## 2026-05-10 — OpenClaw 文章批量摄入

- **操作**: 批量摄入 OpenClaw 公众号文章
- **来源目录**: 微信公众号/OpenClaw/
- **处理文章数**: 112
- **创建源文件页**: 112
- **更新实体页**: 18 (OpenClaw, Hermes Agent, Claude, Claude Code, Cursor, 飞书, Telegram, MCP, GitHub, 淘宝, 小红书, OpenSpace, JVS Claw, Harness, Agent Browser, web-access, 飞书CLI, 网易)
- **更新概念页**: 23 (多Agent协作, Sub-Agent, Agent路由, 记忆系统, Skill开发, AGENTS.md配置, SOUL.md配置, Cron定时任务, 知识库构建, 浏览器自动化, PPT制作, 视频制作, 企业落地, 一人公司, Agent工程化, 本地部署, 爬虫, 语音识别, Token优化, 数据安全, 横纵分析法, 上下文工程, Harness框架)
- **创建综合页**: 4 (OpenClaw文章索引, OpenClaw-vs-Hermes对比分析, OpenClaw多Agent协作指南, OpenClaw-Skill生态指南)

### 新增/更新实体
OpenClaw, Hermes Agent, Claude, Claude Code, Cursor, 飞书, Telegram, MCP, GitHub, 淘宝, 小红书, OpenSpace, JVS Claw, Harness, Agent Browser, web-access, 飞书CLI, 网易

### 新增/更新概念
多Agent协作, Sub-Agent, Agent路由, 记忆系统, Skill开发, AGENTS.md配置, SOUL.md配置, Cron定时任务, 知识库构建, 浏览器自动化, PPT制作, 视频制作, 企业落地, 一人公司, Agent工程化, 本地部署, 爬虫, 语音识别, Token优化, 数据安全, 横纵分析法, 上下文工程, Harness框架

---

## 2026-05-10 — Skills 目录概念匹配改进

**Action:** 重新运行 Skills 目录的概念匹配，使用关键词扩展提升匹配质量

**改进:**
- 概念匹配从简单的字符串精确匹配改为多关键词匹配
- 每个概念映射到5-10个搜索关键词
- 平均每篇文章匹配到8.7个概念（改进前为0-1个）
- 52个源文件摘要页已更新
- 38个实体页面已更新
- 36个概念页面已更新

**概念匹配示例:**
- MCP协议: 关键词包含 "mcp", "model context protocol", "usb接口"
- Harness Engineering: 关键词包含 "harness", "脚手架", "约束", "编排", "验证层"
- Skill设计模式: 关键词包含 "skill设计", "设计模式", "SKILL.md", "蒸馏"


## [2026-05-10] lint | Health check & fix
- 修复坏标题
- 修复断链（模糊匹配）
- 重建 Index 一致性

---

## [2026-05-10] ingest | 微信公众号全量同步新增4篇

**触发:** 微信公众号全量同步（collect-full + process）
**新增文章:** 4 篇

### 处理文章

1. **我现在如何使用 AI：不是找一个更强模型，而是搭一套自己的工作系统** (AI办公) — AI 使用五层架构方法论
2. **告别AI失忆！OpenClaw+Obsidian搭自媒体记忆宫殿，新手也能上手** (Obsidian) — OpenClaw+Obsidian 搭建记忆系统
3. **大部份人只会用 Hermes 的 8%功能，剩下的92% 功能你肯定没碰过** (Hermes) — Hermes 15个高级功能详解
4. **Playwright拉爆了！请给你的Agent安装上真正的浏览器访问能力——CDP Bridge MCP** (Agent) — CDP Bridge MCP 开源项目

### 创建页面

- Source 摘要页: 4 (sources/)
- Entity 页: 1 — CDP-Bridge-MCP (新建)
- Index 更新: +5 entries (4 sources + 1 entity)

### 更新页面

- [[Hermes]] — 新增功能概览引用，mentions 212→213
- [[Obsidian]] — 新增文章引用
- [[OpenClaw]] — 新增文章引用
- [[Playwright]] — 新增 CDP Bridge 对比引用
- [[CDP-Bridge-MCP]] — 新建实体页面
- [[index]] — 更新统计数据和索引

### 涉及实体

[[CDP-Bridge-MCP]] (新), [[Hermes]], [[Obsidian]], [[OpenClaw]], [[Playwright]], [[Claude]], [[OpenAI]], [[Anthropic]], [[Codex]], [[Claude-Code]], [[MCP]], [[飞书]], [[Telegram]], [[OpenRouter]]

### 涉及概念

[[Harness-Engineering]], [[上下文工程]], [[Prompt-Engineering]], [[Agent工程化]], [[Skills技能系统]], [[记忆系统]], [[知识库构建]], [[AGENTS配置]], [[SOUL配置]], [[Cron定时任务]], [[Webhook自动化]], [[Token优化]], [[浏览器自动化]], [[MCP协议]], [[知识管理]], [[企业落地]], [[内容创作]]

---

## [2026-05-10] lint | Post-ingest health check

**Scope:** 本次新增的 4 个 source 页面 + 3 个新 entity 页面 + 1 个新 concept 页面
**Wikilinks 检查:** 57 links → 全部通过 ✅
**Orphan 检查:** CDP-Bridge-MCP 被 source 页面引用，非孤立页面
**Index 一致性:** 已更新统计数字（Sources 866, Entities 120, Concepts 97）

---

## [2026-05-11] ingest | 微信公众号全量同步新增4篇（第二轮）

**触发:** 微信公众号全量同步（collect-full + process）
**新增文章:** 4 篇

### 处理文章

1. **我用 Obsidian 搭建了一个全球信息订阅系统** (Obsidian) — RSS Dashboard 全球信息订阅
2. **给知识库装上水管：信息自动流进来** (知识库) — 四层信息处理系统设计
3. **Agency-agents：别再只会调提示词了，这个开源项目直接给你 144 个 AI 员工** (Agent) — 144 个专职 Agent 角色库
4. **Karpathy的LLM Wiki + 3.5万Star的Graphify：企业级 RAG 缺的真是知识图谱？** (LLM Wiki) — RAG/LLM Wiki/Graphify 三方案实测

### 创建页面

- Source 摘要页: 4 (sources/)
- Entity 页: 3 新建 — Agency-agents, Graphify, Karpathy, YouTube
- Concept 页: 1 新建 — 信息流自动化
- Index 更新: +9 entries

### 更新页面

- [[Obsidian]] — 新增 2 篇文章引用
- [[index]] — 更新统计数据和索引

### 涉及实体

[[Agency-agents]] (新), [[Graphify]] (新), [[Karpathy]] (新), [[YouTube]] (新), [[Obsidian]], [[Claude]], [[Cursor]], [[Claude-Code]], [[Codex]], [[MCP]], [[Playwright]], [[GitHub]], [[OpenClaw]]

### 涉及概念

[[RAG]], [[知识库构建]], [[知识图谱]], [[知识管理]], [[Multi-Agent]], [[Agent架构]], [[Agent工程化]], [[Skills技能系统]], [[Prompt工程]], [[上下文工程]], [[Token优化]], [[浏览器自动化]], [[自动化工作流]], [[信息流自动化]] (新), [[内容创作]]

---

## [2026-05-11] lint | Post-ingest health check

**Scope:** 本次新增/更新的所有页面
**Wikilinks 检查:** 57 links → 全部通过 ✅（修复了 2 个断链：新建 YouTube 实体页和信息流自动化概念页）
**Orphan 检查:** 无孤立页面 ✅
**Index 一致性:** 已更新统计数字（Sources 866, Entities 120, Concepts 97）

---

## [2026-05-11] ingest | 微信公众号同步新增9篇（第三轮）

**触发:** 微信公众号全量同步（collect-full + process）
**新增文章:** 9 篇

### 处理文章

1. **Playwright 又出新东西了：三个 Agent 帮你全自动写测试** (Agent) — Test Agents Planner/Generator/Healer
2. **一种新的 LLM Wiki 方法论：让 AI 帮你建一个能活下去的知识库** (LLM Wiki) — LLM Wiki方法论替代RAG
3. **Multica：把编码 Agent 当成团队成员管理的开源平台** (Agent) — Managed Agents平台
4. **2万字超长实战 Karpathy 的 LLM Wiki** (LLM Wiki) — Ingest/Compile/Query/Lint循环
5. **别再手动整理笔记了！Claude+Obsidian打造永不遗忘的AI知识系统** (Obsidian) — Claudian插件
6. **Karpathy LLM-Wiki Skill 已开源公开** (LLM Wiki) — 开源Skill包
7. **Graphify：把 Karpathy 的 LLM Wiki 从理念变成了产品** (LLM Wiki) — 知识图谱工程化
8. **Karpathy 的知识库构想被人做成桌面应用了** (GitHub) — llm_wiki桌面应用
9. **利用AI Agent一句话完成Karpathy的llm-wiki知识库搭建** (Agent) — Cursor搭建知识库

### 创建页面

- Source 摘要页: 9 (sources/)
- Entity 页: 5 新建/更新 — Graphify, Multica, Claudian, Playwright-Test-Agents, llm_wiki-桌面应用
- Concept 页: 4 新建/更新 — LLM-Wiki方法论, 知识图谱构建, Managed-Agents, 自动化测试

### BM25索引

- 重建完成: 1195 篇文档, 31213 词条

### Lint检查

- Source页面完整性: ✅ 全部9篇已创建
- Entity/Concept页面: ✅ 全部已创建
- Index更新: ✅ 统计数字已更新
- Wikilinks: 21个断链（原始文件引用，属正常结构）

---

## [2026-05-11] ingest | 微信公众号全量同步新增4篇（第三轮 22:00）

**触发:** 微信公众号全量同步（collect-full + process）
**新增文章:** 4 篇

### 处理文章

1. **71k Star 炸裂！Karpathy 新作 autoresearch：让 AI 替你做研究，你只管睡觉** (AI工具) — AI 自主研究实验项目
2. **你的 Skills 越来越多了，是时候用 Marketplace 管起来了** (Skills) — Skills 管理需求
3. **分享3个新发现的Skills** (Skills) — SenseNova-Skills / Warp oz-skills / lenny-skills
4. **Horizon：打造你的专属 AI 新闻雷达** (Horizon) — AI 驱动个人新闻雷达

### 创建页面

- Source 摘要页: 4 (sources/)
- Entity 页: 6 新建 — autoresearch, Horizon, SenseNova-Skills, Warp-oz-skills, lenny-skills, (Karpathy 更新)
- Index 更新: +7 entries, 新增 Horizon 分类

### 更新页面

- [[Karpathy]] — 新增 autoresearch 章节

### 修复断链

- `[[GPT]]` → `[[GPT-4]]` / `[[GPT-5]]`（2 处）
- `[[CodeX]]` → `[[Codex]]`（1 处）

---

## [2026-05-11] lint | Post-ingest health check（第三轮）

**Scope:** 本次新增/更新的所有页面
**Wikilinks 检查:** 62 links → 全部通过 ✅（修复了 3 个断链）
**Orphan 检查:** 无孤立页面 ✅

---

## [2026-05-11] Ingest | 微信公众号同步摄入（9篇新增）

**Operator:** Automated cron job
**Source:** ../微信公众号/（9 new articles from wxrobot_sync_v3）
**Time:** 2026-05-11 18:00

### New Articles Ingested

| Category | Title | Source File |
|---|---|---|
| 外贸出海情报系统 | 跟龙虾鏖战一个月，我打通了这套「外贸出海情报系统」 | 跟龙虾🦞鏖战一个月... |
| AI工具 | 5分钟搞定PPT！用AI把Word文档一键转演示 | 5分钟搞定PPT！用AI把Word文档一键转演示.md |
| Claude | 数智赋能：一文讲清什么是 Skill？ | 数智赋能丨一文讲清...避坑指南.md |
| AI Coding | Taste Skill：教AI写出高端前端，告别廉价感 | Taste Skill：教AI写出高端前端... |
| Obsidian | 从 0 到 1 搭建 AI 知识库：obsidian-wiki 完整实操 | 从 0 到 1 搭建 AI 知识库... |
| Hermes | Hermes Kanban 实战：我是怎样让多个 Agent 真正协作起来的！ | Hermes Kanban 实战... |
| GitHub | GitHub 2.4万Star的Maigret：一个用户名搜遍3000+网站 | GitHub 上狂揽 2.4 万 Star... |
| GitHub | 姚金刚的yao-open-prompts：116个中文提示词冲上GitHub Trending | 116个中文提示词，2天冲上GitHub热门... |
| 待补文章 | Seedance2.0保姆级教程：AI广告视频玩法全覆盖 | [605] Seedance2.0保姆级教程... |

### Results

- **Sources processed:** 9
- **Source summary pages created:** 9 (wiki/sources/)
- **Categories added:** 1 new (外贸出海情报系统)
- **Index updated:** Sources 907→916, +9 new entries
- **Log appended:** 本条目

### New Concepts Identified

- GEO（Generative Engine Optimization）— 来自 yao-open-prompts 文章
- 外贸出海情报系统 — 新领域概念
- obsidian-wiki — 知识库工具
- Maigret — OSINT 开源工具

**Index 一致性:** 已更新统计数字（Sources 897, Entities 128, Concepts 101）

## 2026-05-12 — 微信文章同步摄入

**Operator:** Automated cron (wxrobot_sync_v3.py + wiki ingest)
**Source:** 微信公众号/ (4 articles processed, 3 successful, 1 failed)

### Results

- **Sources processed:** 3 (成功)
  - Obsidian/如何从零搭建Obsidian知识库：AI Agent不是问答机器，它是执行者（附日报模板+工具）
  - Hermes/Hermes 桌面版 GUI 来了：被命令行劝退的人，可以冲了
  - API中转/他搭了个API中转站，月入过万
- **Source summaries created:** 3
- **Entity pages created:** 3 (Simonlin, Hermes Desktop, One-API)
- **Concept pages created:** 5 (Obsidian知识库, AI执行模式, API中转, 商业模式, GUI桌面应用)
- **Index updated:** +3 source entries (Obsidian 23→24, Hermes 189→190, API中转 2→3)
- **Log appended:** 本条目

### New Entities

1. Simonlin — 公众号作者（Simonlin的精神世界）
2. Hermes Desktop — fathah开发的Hermes桌面GUI（MIT协议）
3. One-API — GitHub 20K+ Star的API中转开源项目

### New Concepts

1. Obsidian知识库 — 基于Karpathy三层架构的知识库方法论
2. AI执行模式 — AI从知识库获取规则并按规则执行，而非仅回答问题
3. API中转 — AI时代的水电工，帮用户绕过注册/支付障碍
4. 商业模式 — API中转站的定价策略与收益模型
5. GUI桌面应用 — 命令行工具图形化降低门槛

### Failed (待补)

- [620] 【Agent - Memory】Hermes-Agent 的 Memory 设计拆解 — 正文抓取失败

**Index 一致性:** 已更新（Obsidian 24篇, Hermes 190篇, API中转 3篇）

## 2026-05-12 — 微信公众号文章增量摄入

**Operator:** Automated ingestion (定时任务)
**Source:** 微信公众号/ (5 篇新增)
**Time:** 2026-05-12

### 新增 Sources

1. **Clawith：把 AI Agent 当员工管理的开源平台** → [[clawith-ai-agent-员工管理平台]]
   - 分类：Agent
   - 关键实体：Clawith, Trigger Daemon, Focus Items, Autonomy Policy
   - 关键概念：AI数字员工, 数字员工操作系统

2. **WordOllama 2.0 更新：为 Word/WPS 增加 Agent 能力** → [[wordollama-2-agent能力更新]]
   - 分类：Agent
   - 关键实体：WordOllama, 李伯阳
   - 关键概念：AI-Agent, Skill开发

3. **再盘 | 24 个开源的 AI PPT Skill，推荐收藏** → [[24个开源-ai-ppt-skill-推荐收藏]]
   - 分类：PPT skill
   - 关键实体：frontend-slides, guizang-ppt-skill, open-design, PPTAgent
   - 关键概念：PPT制作, Skill开发, MCP协议

4. **GitHub AI 热榜 | 5月11日：榜首易主，GenericAgent + omlx** → [[github-ai热榜-5月11日-genericagent-omlx]]
   - 分类：GitHub
   - 关键实体：GenericAgent, omlx
   - 关键概念：自进化系统, 本地部署

5. **一文讲清：Prompt 和 Skill 的区别是什么？** → [[prompt-和-skill-区别]]
   - 分类：Prompt
   - 关键概念：Prompt-Engineering, Skills技能系统

### 新增 Entities

- [[Clawith]] — AI 数字员工操作系统
- [[WordOllama]] — Word/WPS AI 插件
- [[GenericAgent]] — 自进化 Agent
- [[omlx]] — Mac 本地推理优化

### 新增 Concepts

- [[AI数字员工]] — Agent 持续在线、主动工作的理念
- [[数字员工操作系统]] — Clawith 的核心定位
- [[Mac本地推理]] — Mac 本地运行 LLM 推理的技术

### Index 一致性

已更新（Sources: 916→921, Entities: 137→141, Concepts: 101→104）

## 2026-05-12 — 微信公众号同步新增4篇（第四轮）

**Operator:** Automated cron (wxrobot_sync_v3.py + wiki ingest)
**Source:** 微信公众号/ (4 articles processed)
**Time:** 2026-05-12 12:00

### 处理文章

1. **37.9k Star 的 agent-skills：AI Agent 也该有工程纪律** (Skills) — Addy Osmani 开源的生产级工程技能包，37.9k Stars，TDD反借口表是核心
2. **装了Superpowers还是不会用？这套完整工作流，让你的AI从"工具"变成"搭档"** (Superpowers) — 14个Skill流水线完整指南
3. **牛 X 的Skill** (Skills) — Markdown Viewer Skill，100+图例+6000+矢量图标
4. **Markdown 负责记忆，HTML 负责展示：AI 时代的新内容分工** (MarkItDown) — Thariq观点：Markdown做仓库，HTML做展厅

### 创建页面

- Source 摘要页: 4 (wiki/sources/)
  - `37.9k-Star-agent-skills-AI-Agent-工程纪律.md`
  - `Superpowers-完整工作流-工具变搭档.md`
  - `Markdown-Viewer-Skill-牛X配图.md`
  - `Markdown-HTML-AI内容分工.md`

### 更新页面

- [[Superpowers]] — 新增14个Skill流水线表格
- [[index]] — 新增 MarkItDown、Superpowers 分类，Sources 921→925

### 新增分类

- MarkItDown (1篇)
- Superpowers (1篇)

### 涉及实体

[[Superpowers]], [[agent-skills]], [[Addy-Osmani]], [[Claude-Code]], [[Markdown-Viewer-Skill]], [[Thariq-Shihipar]], [[Anthropic]]

### 涉及概念

[[TDD]], [[test-driven-development]], [[spec-driven-development]], [[code-review]], [[AI-Agent工程化]], [[AI开发流水线]], [[14个Skill串联]], [[Sub-Agent]], [[Git-Worktree]], [[verification]], [[Markdown记忆格式]], [[HTML展示层]], [[AI工作流]], [[内容分工]], [[AI配图]]

## 2026-05-12 — 微信同步新增摄入

**Operator:** Automated cron sync
**Source:** 微信公众号/GitHub/ + 微信公众号/Hermes/
**Time:** 2026-05-12 18:00

### Results

- **Sources processed:** 2
- **Source pages created:** 2
  - [[盘点-10-个GitHub新开源项目-Star快速攀升]]
  - [[Hermes-Computer-Use-MCP协议控制电脑]]

### New Entities Identified

- [[antirez]] — Redis 作者，ds4 项目
- [[Mirage]] — 统一虚拟文件系统
- [[TokenSpeed]] — Agent 推理引擎
- [[ds4]] — Mac 本地 DeepSeek V4 推理引擎

### Key Concepts Covered

- [[本地部署]] — Mac 本地运行大模型（ds4）
- [[浏览器自动化]] — Computer Use 本质是桌面自动化
- [[MCP协议]] — Computer Use 底层驱动协议
- [[Token优化]] — 四层截图压缩节省上下文

## 2026-05-13 — InkOS + 极空间 文章摄入

**Operator:** Automated ingestion (karpathy-llm-wiki)
**Source:** 微信公众号/Agent/ (1 file)
**Time:** 2026-05-13

### Results

- **Sources processed:** 1
- **Source pages created:** 1
  - [[NAS-赚外快啦！5个-Agent-自动生成「百万小说」，极空间部署-InkOS]]
- **Entity pages created:** 2
  - [[InkOS]] — 多 Agent AI 小说生成流水线
  - [[极空间]] — 国内 NAS 厂商，支持 Docker 部署
- **Concept pages updated:** 1
  - [[多Agent协作]] — 新增 InkOS/极空间 相关实体

### Key Concepts Covered

- [[多Agent协作]] — 5 Agent（雷达/建筑师/写手/审计员/修订者）流水线
- [[工作流自动化]] — InkOS 小说生成完整工作流

## 2026-05-13 — 微信公众号同步摄入（12篇）

**Operator:** Automated cron job
**Source:** 微信公众号/ (12 new articles processed)
**Time:** 2026-05-13

### Results

- **Sources created:** 12
- **Categories covered:** Pixelle-Video, GitHub, Vibe Coding, Claude, Skills, OpenClaw, Hermes, PPT Master, Superpowers, Agent

### Source Pages Created

1. `sources/pixelle-video-14万star开源项目.md` — Pixelle-Video 开源项目介绍
2. `sources/cyber-skills-github整理.md` — Cyber Skills GitHub仓库整理
3. `sources/vibe-coding会议助手实战.md` — Vibe Coding实战案例
4. `sources/sub2api-api网关平台.md` — Sub2API API网关平台
5. `sources/html-ppt-skill-html代替ppt.md` — HTML-PPT Skill
6. `sources/skill-creator完整开发流水线.md` — Anthropic skill-creator升级
7. `sources/rtk-token成本降低92-percent.md` — RTK Token压缩工具
8. `sources/openclaw数字孪生-记忆系统.md` — OpenClaw数字孪生与记忆系统
9. `sources/hermes-agent记忆插件选型指南.md` — Hermes Agent 8大记忆方案对比
10. `sources/ppt-master-skill可编辑-ppt.md` — PPT Master Skill
10. `sources/skill自由-三步链路流水线.md` — Superpowers三步链路Skill开发

## 2026-05-14 — 微信公众号同步摄入（6篇）

**Operator:** Automated cron job (wxrobot_sync_v3.py + wiki ingest)
**Source:** 微信公众号/ (6 new articles processed, all successful)
**Time:** 2026-05-14

### Results

- **Sources created:** 6
- **Categories covered:** GitHub, Skills, Agent, Harness, Hermes
- **New entries:**
  1. GitHub: 扒了1周GitHub，我挖出了顶级博主不肯说的20个Sikll
  2. Skills: 装了这个AI热点Skill之后，你再也不需要自己去刷AI新闻了
  3. Agent: AI 编程工程化：Subagent——给你的 AI 员工打造协作助手
  4. Harness: 从零设计生产级 Multi-Agent Harness：架构、评估、记忆、成本与 MCP 工具接入全拆解
  5. Hermes: 搞完 Hermes Kanban 我才发现，多 Agent 协作根本不是在演戏
  6. Hermes: 一键给 Hermes Agent 装上"操作系统"，打造的开箱即用技能层

### Source Pages Created

1. `sources/扒了1周GitHub我挖出了顶级博主不肯说的20个Sikll超详细介绍及安装教程.md`
2. `sources/装了这个AI热点Skill之后你再也不需要自己去刷AI新闻了.md`
3. `sources/AI编程工程化Subagent给你的AI员工打造协作助手.md`
4. `sources/从零设计生产级MultiAgentHarness架构评估记忆成本与MCP工具接入全拆解.md`
5. `sources/搞完HermesKanban我才发现多Agent协作根本不是在演戏.md`
6. `sources/一键给HermesAgent装上操作系统打造的开箱即用技能层.md`

### Key Concepts Covered

- [[Sub-Agent]] — AI 编程工程化，任务分解与上下文隔离
- [[Multi-Agent]] — Multi-Agent Harness 架构设计
- [[Harness-Engineering]] — 生产级 Harness 评估与记忆管理
- [[Kanban看板]] — Hermes Kanban 多 Agent 协作模式
- [[Skills技能系统]] — 开箱即用技能层搭建

### Index Updates

- Sources: 963 → 969 (+6)
- GitHub: 21 → 22 (+1)
- Skills: 49 → 50 (+1)
- Agent: 91 → 92 (+1)
- Harness: 9 → 10 (+1)
- Hermes: 190 → 192 (+2)
12. `sources/9router-万能ai模型路由.md` — 9Router万能AI路由

---

## 2026-05-16 — 微信公众号文章同步摄入

**Operator:** Automated ingestion (微信同步 + cron)
**Source:** 微信公众号/ (9 new articles processed)
**Time:** 2026-05-16 06:00

### Results

- **Sources processed:** 9
- **Categories:** Claude (1), PPT skill (1), Vibe Coding (1), Agent (1), Hermes (1), AI技术 (1), AI生成PPT方案 (1), Skills (1), 字节UI-TARS Desktop (1)
- **Source pages created:** 9
- **Entity pages created/updated:** 2 new (UI-TARS Desktop, CNKI Skills), 3 updated (web-access, Hermes-Agent)
- **Failed/Skipped:** 0

### Articles Added

**Claude (1):**
- [[web-access-skill-ai联网能力升级]] — AI联网能力升级：web-access Skill解决了什么问题

**PPT skill (1):**
- [[26个PPT生成Skill系统梳理]] — 26个PPT生成Skill，我做了一次系统梳理

**Vibe Coding (1):**
- [[一人公司AI工具全家桶-2.7k-star]] — 一人公司 AI 工具全家桶：2.7k Star 的 one-person-company

**Agent (1):**
- [[Agent替你干活的真相]] — Agent 替你干活的真相，比你想象的简单十倍

**Hermes (1):**
- [[Hermes-Agent-10大神级插件分享]] — Hermes Agent 2026年5月必装的10大神级插件

**AI技术 (1):**
- [[AI数据分析Excel从此只用来看结果]] — 手把手教你用AI做数据分析，Excel从此只用来看结果

**AI生成PPT方案 (1):**
- [[AI生成PPT方案完整经验总结]] — 7款AI生成PPT方案完整经验总结

**Skills (1):**
- [[CNKI-Skills-Claude-Code查知网]] — CNKI Skills：查知网检索筛选下载整理文献一条龙

**字节UI-TARS Desktop (1):**
- [[UI-TARS-Desktop字节开源33.7k-star]] — 字节开源33.7k：UI-TARS Desktop AI操作电脑

### Entities Created/Updated

- **Created:** [[UI-TARS-Desktop]] (字节UI-TARS Desktop), [[CNKI-Skills]] (CNKI Skills for Claude Code)
- **Updated:** [[web-access]], [[Hermes-Agent]]

### Notes

- All 9 queued articles successfully processed and ingested
- 2 new categories auto-created by wxrobot: AI生成PPT方案, 字节UI-TARS Desktop
- Sources count: 983 → 992 (+9)
- Entities count: 147 → 149 (+2)

## 2026-05-19 — 微信公众号文章同步摄入（第八批次）

**Operator:** Automated ingestion (微信同步 cron)
**Source:** 微信公众号/ (2 new articles processed)
**Time:** 2026-05-19 12:00

### Results

- **Sources processed:** 2
- **Categories:** AI技术 (GEO生成式搜索监测系统), Claude (html-anything)
- **Source pages created:** 2
  - `wiki/sources/一个开源的-GEO-生成式搜索监测系统-关注品牌在-AI-回答中的可见度.md`
  - `wiki/sources/html-anything-开源-让你感受-Claude-Code-作者提到的-HTML-效果.md`
- **Entity pages created:** 2
  - `wiki/entities/ai-geo-monitoring.md`
  - `wiki/entities/html-anything.md`
- **Concept pages created:** 1
  - `wiki/concepts/AI搜索.md`
- **concept-table.md updated:** GEO (count 1→2), +AI搜索, +ai-geo-monitoring, +html-anything

### New Articles

**AI技术 (1):**
- [[一个开源的-GEO-生成式搜索监测系统-关注品牌在-AI-回答中的可见度]] — 一个开源的 GEO 生成式搜索监测系统：关注品牌在 AI 回答中的可见度

**Claude (1):**
- [[html-anything-开源-让你感受-Claude-Code-作者提到的-HTML-效果]] — html-anything 开源！让你感受 Claude Code 作者提到的 HTML 效果！

### Entities Created/Updated

- **Created:** [[ai-geo-monitoring]] (ai-geo-monitoring), [[html-anything]] (html-anything)
- **Updated:** [[GEO]] (article count 1→2)

### Notes

- 2 new articles collected and processed successfully
- Sources count: 1029 → 1031 (+2)
- Entities count: 168 → 170 (+2)
- Concepts count: 119 → 121 (+2)
- All wxrobot queue: pending=0, success=737

---

## 2026-05-21 — 微信公众号文章同步（第十三次，午间定时）

**Operator:** Automated ingestion (微信同步 cron 12:00)
**Source:** 微信公众号/ (0 new articles — 12th batch already processed at 00:01)
**Time:** 2026-05-21 12:00

### Queue Status

- Collection: 772 messages total, 0 new enqueued (already collected in batch 12)
- Processing: 0 pending (all processed)
- Queue: success=744

### Wiki Stats Updated

- Sources: 1036 → 1049 (header corrected; 13 untracked files noted)
- Entities: 173 (unchanged)
- Concepts: 122 → 170 (header corrected)
- Index header updated to 2026-05-21

### Notes

- 12th batch articles already fully ingested: 754-Agent-Skills, 753-Skill-SD
- Index stats header was stale (Sources/Concepts counts corrected)
- No new articles require ingestion this cycle

---

## 2026-05-22 — 微信公众号文章同步摄入（第十四批次）

**Operator:** Automated ingestion (微信同步 cron 00:00)
**Source:** 微信公众号/ (13 new articles processed)
**Time:** 2026-05-22 00:01

### Results

- **Sources processed:** 13
- **Categories:** WorkBuddy (9 new), 微信全流程 Skill (1 new, 1st ever), RSSHub (1 new, 1st ever), Prompt (1 new)
- **Source pages created:** 13
  - `wiki/sources/workbuddy-self-evolution.md`
  - `wiki/sources/workbuddy-customer-segmentation.md`
  - `wiki/sources/workbuddy-workflow-setup.md`
  - `wiki/sources/workbuddy-3d-dashboard.md`
  - `wiki/sources/workbuddy-10-things.md`
  - `wiki/sources/workbuddy-5-dirty-tasks.md`
  - `wiki/sources/workbuddy-ima-knowledge-base.md`
  - `wiki/sources/workbuddy-skills-installation.md`
  - `wiki/sources/workbuddy-complete-guide.md`
  - `wiki/sources/workbuddy-excel-processing.md`
  - `wiki/sources/wechat-full-skill-workflow.md`
  - `wiki/sources/from-prompt-to-skills-ai-agent.md`
  - `wiki/sources/nas-rsshub-deployment.md`
- **Entity pages updated:** none
- **Concept pages created:** none
- **concept-table.md updated:** 0 (new concepts noted but not yet added)
- **index.md updated:** Statistics (Sources 1054→1067), WorkBuddy (23→32篇), Prompt (3→4篇), +微信全流程 Skill (1篇), +RSSHub (1篇)

### New Articles

| ID | 分类 | 标题 |
|----|------|------|
| 760 | WorkBuddy | WorkBuddy高阶玩法：让AI自我进化，你只需要说一句话 |
| 761 | WorkBuddy | WorkBuddy方法16 | 客户数据分群与画像分析：找到你的金矿客户 |
| 762 | WorkBuddy | WorkBuddy从入门到精通（13）工作流搭建：从需求到自动化全流程 |
| 763 | WorkBuddy | WorkBuddy 100种用法 #37 | 探索新功能，一键制作 3D 可视化数字大屏 |
| 764 | WorkBuddy | 用WorkBuddy能做哪10件事？ |
| 765 | WorkBuddy | 打工人反内耗指南：我用WorkBuddy把这5类脏活全干了 |
| 766 | WorkBuddy | 用WorkBuddy+ima做知识库终极版：文档联动+定期整理，把知识变资产 |
| 767 | WorkBuddy | WorkBuddy 赋能精准办公：Skills 安装提示词（含必备版+进阶版 TOP5） |
| 768 | WorkBuddy | WorkBuddy 完整使用指南：让AI真正成为你的工作搭档 |
| 769 | WorkBuddy | WorkBuddy Excel处理：数据清洗和合并，一条指令搞定 |
| 770 | 微信全流程 Skill | 微信全流程 Skill：选题、写作、配图、排版、发布到草稿箱 |
| 771 | RSSHub | NAS部署RSSHub，全网平台信息一把抓！ |
| 772 | Prompt | 从手写 Prompt 到可复用 Skills：AI Agent 的"技能包" |

### Notes

- 13 new articles collected and processed successfully
- 2 new categories introduced: 微信全流程 Skill, RSSHub
- Sources count: 1054 → 1067 (+13)
- WorkBuddy articles now at 32篇 (was 23)
- BM25 index to be rebuilt after this entry

## [2026-05-22] lint | Health Check — Full Audit

**Operator:** hermes-neirong（手动触发）
**Scope:** 全知识库

### 知识库规模

| 类型 | 数量 |
|------|------|
| Sources | 1,068 |
| Entities | 174 |
| Concepts | 170 |
| Synthesis | 15 |
| 总页面 | 1,429 |
| 总 wikilink 引用 | 19,450 次 |
| 唯一链接目标 | 1,904 个 |

---

### Errors（必须修复）

**1. 断链：509 个链接目标无对应页面**

- 唯一链接目标 1,904 个，其中 509 个（26.7%）指向不存在的页面
- 高频断链 Top 10：
  - `[[Claude-Code]]` — 14 次引用（已有 Claude-Code 页面，大小写/空格不匹配）
  - `[[Hermes-Agent]]` — 10 次（已有 Hermes-Agent）
  - `[[LLM-Wiki方法论]]` — 9 次
  - `[[mmx-cli]]` — 7 次
  - `[[OpenCode]]` — 6 次
  - `[[text-to-cad]]` — 5 次
  - `[[团队协作]]` — 4 次
  - `[[GEO]]` — 4 次
  - `[[AI客服]]` — 4 次
  - `[[Electron]]` — 4 次
- 385 个断链仅被引用 1 次，93 个被引用 2+ 次，7 个被引用 5+ 次

**2. Index 不一致：1281 条幽灵索引**

- index.md 中 1,281 条链接指向不存在的页面（大量含 `.md` 后缀）
- 实际无对应文件的链接远多于真正断链，主要是索引格式问题（链接名含 `.md` 后缀）

---

### Warnings（应该修复）

**3. 孤儿页面：29 个页面无人引用**

- 孤儿页面 = 存在但无任何其他页面通过 wikilink 指向它
- 示例：
  - `732-OpenHuman开源的个人AI超级智能让你的AI真正认识你`
  - `739-2026年5月最火-AI-Agent-Skills-完整盘点`
  - `Agent-替你干活的真相，比你想象的简单十倍`
  - `awesome-rss-feeds` / `awesome-tech-rss`
  - `Claude-Code-+-Obsidian：个人知识库从工具到思维的完整指南`
  - `我的知识库-主题...`（看起来是模板残留）

**4. Index 缺失条目：146 个页面未出现在 index.md**

- Sources: 43 个
- Entities: **36 个**（含重要实体如 Scrapling、CNKI-Skills、UI-TARS-Desktop 等）
- Concepts: **65 个**（含 LLM-Wiki方法论、RPA、OCR 等高频概念）
- Synthesis: 3 个

**5. 缺失交叉引用：大量实体/概念页面存在未链接的关联**

- Entity → Concept 缺失示例：`skills-sh` 提到 Skill/AI/Agent 等概念但未链接
- Concept → Entity 缺失示例：`自进化系统` 提到 OpenSpace/Hermes-Agent/Copilot 但未链接

---

### Info（可以改进）

**6. 日期元数据缺失**

- 1,068 个 Source 页面中仅 3 个有 `date:` frontmatter
- 无法有效判断内容时效性
- 建议后续摄入时统一添加日期字段

**7. 数据覆盖缺口**

- 高价值缺失页面（按引用频率排序）：
  - Claude Code (14x) — 实际已有 Claude-Code 页面，需修复命名匹配
  - Hermes Agent (10x) — 同上，已有 Hermes-Agent
  - LLM Wiki方法论 (9x) — 概念页存在于 concepts/ 但名称可能不匹配
  - mmx-cli (7x) — 无实体页面
  - OpenCode (6x) — 无实体页面
  - text-to-cad (5x) — 无实体页面

---

### 建议修复优先级

1. **P0 — 立即修复：** 高频断链命名修复（Claude Code→Claude-Code、Hermes Agent→Hermes-Agent 等），估计修复后断链可减少 50+
2. **P1 — 近期修复：** 将 36 个缺失实体 + 65 个缺失概念补入 index.md
3. **P2 — 批量修复：** 29 个孤儿页面添加交叉引用
4. **P3 — 渐进改进：** 为 Source 页面添加日期元数据，逐步改善时效性判断

### 统计摘要

| 检查项 | 结果 |
|--------|------|
| 断链 | **509** / 1,904 (26.7%) |
| 孤儿页面 | **29** |
| 缺失 index 条目 | **146** (36E + 65C + 43S + 3Syn) |
| 幽灵 index 条目 | **1,281** |
| 缺失交叉引用 | 大量（未完整统计） |
| 日期元数据覆盖 | 3/1,068 (0.3%) |

---

## 2026-05-22 Lint Fix Batch

**自动修复执行人**: hermes-neirong agent

### P0: 断链命名修复
- 修复 11 组命名不匹配导致的断链（空格 vs 连字符）
- 总替换 49 处，涉及 34 个文件
- 高频修复：
  - `Claude Code` → `Claude-Code` (14x)
  - `Hermes Agent` → `Hermes-Agent` (10x)
  - `LLM Wiki方法论` → `LLM-Wiki方法论` (9x)
  - `Managed Agents` → `Managed-Agents` (2x)
  - `Hermes Desktop` → `Hermes-Desktop` (2x)

### P1: Index 缺失条目补全
- 新增 65 个缺失条目到 index.md（18实体 + 11概念 + 36源 + 3综合）
- 删除冗余的 Unindexed 分类章节（已合并到主章节）
- 更新统计：Sources=1068 Entities=174 Concepts=170 Synthesis=15
- 后续追加 4 条剩余缺失（1源 + 3综合）

### P2: 孤儿页面交叉引用
- Entity/Concept/Synthesis 类孤儿 30 个
- 自动匹配关联页面并添加 `## Related` 链接
- 修复 29/30（SenseNova-Skills 无强关联页面，跳过）
- Source 类孤儿 362 个暂不处理（文章无入链属正常）

### 修复后状态
- 断链：从 478 降至 ~429（命名类全部修复，剩余为页面不存在类）
- Index 覆盖率：100%（所有现有页面均已入 index）
- 孤儿页面（E/C/S）：1 个（SenseNova-Skills）
