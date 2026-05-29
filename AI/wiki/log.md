# Log

Chronological record of all operations.

## 2026-05-29 — 三篇微信公众号文章摄入 (A/B/C)

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. 微信公众号/Agent/awesome-agentic-ai-zh：240+ 资源，从零到构建多 Agent 系统的完整学习地图.md → wiki/sources/awesome-agentic-ai-zh-240-resources-from-zero-to-multi-agent.md
2. 微信公众号/Obsidian/知识库系列（一）：用 Obsidian 把散落的材料收成一棵树.md → wiki/sources/知识库系列一-用Obsidian把散落的材料收成一棵树.md
3. 微信公众号/AI Coding/7,800 Star！592 行代码让 AI 操控浏览器.md → wiki/sources/browser-harness-592-lines-ai-browser-control.md
**Time:** 2026-05-29
**New Sources:** 3
**New Entities:** [[WenyuChiou]], [[武见]], [[Browser-Harness]], [[何三]], [[CDP]]
**New Concepts:** [[Agent学习路线图]], [[Context-Engineering]], [[自愈式自动化]], [[CDP协议]], [[Docs-As-Code]]
**index.md updated:** Statistics (Sources 1144→1147, Entities 217→222, Concepts 216→221), Agent (102→104), AI Coding (12→13), Obsidian (34→35)

### Key Findings

**Article A - awesome-agentic-ai-zh (240+ 资源学习地图):**

1. **项目定位**：GitHub 1,743 Stars，MIT 协议，WenyuChiou 维护的 AI Agent 学习路线图
2. **三大核心**：学习路线图（8 阶段 2 路径）+ 资源整理（240+ 项目）+ 动手练习（23 个练习）
3. **两套路径**：
   - Track A — CLI Power User（8-10 周）：用现成工具提效
   - Track B — Agent Builder（16-22 周）：从零打造 Agent
4. **三层概念进化**：Prompt Engineering → Context Engineering → Harness Engineering
5. **五条延伸路线**：研究员/开发者/教师/知识工作者/日常使用者
6. **实战亮点**：Paper Summary Bot 约 350 行代码贯穿所有阶段

**Article B - 知识库系列（一）Obsidian:**

1. **核心命题**：用 Obsidian 把散落材料收成一棵树，团队协作基础
2. **仓库概念**：Docs As Code 的表达——本地文件夹、纯文本 markdown、Git 管理
3. **工作区四区域**：仓库切换/插件边栏/侧边栏/阅读区
4. **五个基本用法**：新增文件、[[wikilink]]引用、反向链接、#标签、附件
5. **高频场景**：会议记录、写材料、索引材料
6. **进阶增强**：Blue Topaz 主题、Dataview 插件、Excalidraw 画图
7. **选 Obsidian 理由**：数据自己掌控、Git 管理、关联能力强、本地优先

**Article C - Browser Harness (592 行自愈式自动化):**

1. **项目定位**：7.8k Star，browser-use 团队出品，592 行 Python
2. **颠覆思路**：基于 CDP 直连 Chrome，无框架无 recipes
3. **自愈机制**：发现缺功能 → 自己写 helper → 继续执行
4. **设计哲学**：不给轨道，直接给车——路没了自己修
5. **使用方式**：粘到 Claude Code/Codex，AI 自己读文档装依赖连浏览器
6. **同类对比**：Selenium/Playwright 是记录回放，Browser Harness 是自愈式 AI 操控

### Entities Created

| 实体 | 说明 |
|---|---|
| WenyuChiou | awesome-agentic-ai-zh 项目维护者 |
| 武见 | 「武见说」博主，知识管理实践者 |
| Browser-Harness | 592 行自愈式浏览器自动化项目，7.8k Star |
| 何三 | 「何三笔记」博主，独立开发者 |
| CDP | Chrome DevTools Protocol，浏览器底层调试协议 |

### Concepts Created

| 概念 | 说明 |
|---|---|
| Agent学习路线图 | 8 阶段 2 路径的系统化 Agent 学习路径 |
| Context-Engineering | 动态组合 system prompt + memory + 检索 + tool schema |
| 自愈式自动化 | AI 发现缺代码自己写补齐，继续执行 |
| CDP协议 | Chrome DevTools Protocol，WebSocket 直连浏览器 |
| Docs-As-Code | 把文档像代码管理——Git 版本控制、本地纯文本 |

---

## 2026-05-29 — Karpathy Hermes跑通文章摄入 (已覆盖)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/LLM Wiki/Karpathy 的 LLM Wiki 思路，我用 Hermes 跑通了.md
**Author:** Turing 实验室
**Time:** 2026-05-29
**Status:** 已通过 [[karpathy-llm-wiki-context-memory重构企业级的组织记忆]] 和相关实体覆盖

### Key Findings

**文章核心内容已整合到现有知识库：**

1. **核心命题**：两步接力跑通 Karpathy LLM Wiki——Claude Code 做基建部署 Hermes，Hermes 做长期知识维护
2. **工具分工哲学**：
   - Claude Code = 建筑队（一次性基建，能力强无状态，干完就撤）
   - Hermes = 物业（长期知识管理，理解偏好，自我纠错，归类体系）
3. **关键洞察**："把研究员当建筑工用，是浪费。把建筑队当研究员用，是灾难。"

### Entities Updated (本次)

| 实体 | 更新内容 |
|-----|---------|
| Hermes-Agent | 添加工具分工哲学、添加来源文章引用 |
| Claude-Code | 添加工具分工哲学、添加 Hermes 关联 |
| Karpathy | 添加来源文章引用 |

### Concepts Created

| 概念 | 说明 |
|-----|------|
| 工具分工哲学 | Claude Code = 建筑队，Hermes = 物业，工具放在正确位置 |

### Log Entries for Already-Covered Articles

**以下文章已在之前会话中处理，不再创建新 source 页面：**

| 文章 | 覆盖方式 | 备注 |
|-----|---------|------|
| LLM Wiki - 让LLM帮你构建进化中的知识库 | [[karpathy-llm-wiki-context-memory重构企业级的组织记忆]] | 企业级组织记忆主题已覆盖 |
| WorkBuddy 相关文章 | wiki/sources/WorkBuddy系列 | WorkBuddy 资料库、方法系列已覆盖 |
| OpenClaw 相关文章 | AGENTS.md section (19篇) | OpenClaw 小龙虾配置系列已覆盖 |
| Karpathy-autoresearch | [[Karpathy]] entity + [[LLM-Wiki]] concept | LLM Wiki 核心理念已整合 |

---

## 2026-05-29 — Karpathy LLM Wiki 被搬进代码仓库文章摄入 (874)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/LLM Wiki/Karpathy 的 LLM Wiki，被搬进代码仓库.md
**Author:** 硅基与token
**Time:** 2026-05-29
**New Sources:** 1
**New Entities:** [[GitNexus]]
**New Concepts:** [[代码仓库知识图谱]]
**Entities updated:** [[Karpathy]]
**Concepts updated:** [[LLM-Wiki]], [[MCP协议]]
**index.md updated:** Statistics (Sources 1139→1140, Entities 212→213, Concepts 215→216), LLM-Wiki (13→14)

### Key Findings

**Article 874 - Karpathy 的 LLM Wiki，被搬进代码仓库:**

1. **核心命题**：GitNexus 把代码仓库做成可查询、可追踪、可更新的结构化知识库，把 LLM Wiki 思路搬进代码仓库
2. **问题背景**：AI 编程助手应该临时 grep 代码，还是先拥有一张代码仓库地图？
3. **传统 RAG 缺陷**：每次查询都是"重新发现"，知识没有积累
4. **GitNexus 入口**：`npx gitnexus analyze` 索引仓库，`gitnexus mcp` 启动 MCP 服务
5. **六大工具**：query、context、impact、detect_changes、rename、cypher
6. **论文支撑**：
   - Codebase-Memory：Tree-sitter 持久知识图谱，token 消耗低一个数量级
   - Reliable Graph-RAG：AST 派生确定性图谱在覆盖率、成本和多跳 grounding 上更可靠
7. **呼应 Karpathy**：论文/笔记 → 函数/类/依赖，共同点是把"临时上下文"变成"持久结构"
8. **核心观点**：AI 编程下一步缺的不是更会聊天的助手，而是更少迷路的助手

### Entities Created

|| 实体 | 说明 |
|-----|------|
| GitNexus | 代码仓库知识图谱工具，CLI 索引仓库生成依赖图谱，通过 MCP 暴露给 AI 编程工具 |

### Concepts Created

|| 概念 | 说明 |
|-----|------|
| 代码仓库知识图谱 | 把代码仓库编译成结构化知识图谱，抽取依赖、调用链、cluster 和 execution flow |

### Entities Updated

|| 实体 | 更新内容 |
|-----|---------|
| Karpathy | 添加 GitNexus 代码仓库知识图谱章节、来源文章引用、相关概念链接 |

### Concepts Updated

|| 概念 | 更新内容 |
|-----|---------|
| LLM-Wiki | 添加 GitNexus 代码仓库知识图谱章节、来源文章引用、相关实体 GitNexus |
| MCP协议 | 添加代码仓库知识图谱应用场景、GitNexus/Windsurf 相关实体、karpathy 文章引用 |

---

## 2026-05-29 — HTML Slides实战教学文章摄入 (873)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/HTML Slides/全网最全！HTML Slides 实战教学：从趋势到工具，从美学规范到打造你的专属Skill.md
**Time:** 2026-05-29
**Author:** 巴赞的异托邦
**New Sources:** 1
**New Entities:** [[Slidev]]
**New Concepts:** [[HTML幻灯片范式转移]]
**index.md updated:** Statistics (Sources 1138→1139, Entities 211→212, Concepts 214→215)

### Key Findings

**Article 873 - 全网最全HTML Slides实战教学:**

1. **核心命题**：HTML Slides不是"另一种PPT"，而是演示文稿的**范式转移**
2. **四大变革**：
   - 体积与分发：几百KB vs 50MB，浏览器即可播放
   - 版本控制：纯文本格式，Git完美支持
   - 表现力：代码高亮（Shiki）、Vue/React组件嵌入、Canvas动画
   - 开放性：HTML/CSS/JS是Web标准，不依赖厂商
3. **主流工具对比**：
   - [[Slidev]]：开发者首选，Markdown驱动+Vue技术栈
   - [[reveal.js]]：功能天花板，3D旋转+Auto-Animate
   - [[Marp]]：极简派，纯Markdown一键导出
4. **美学规范六铁律**：
   - 整体风格定调：高级感、科技感，禁用白色背景/渐变色
   - 布局铁律：16:9比例，一页一观点，禁用滚动条
   - 配色：3-4色法则，高对比度
   - 字体层次：标题与正文不同字重/字号
   - 内容结构：首页→目录→过渡页→内容页→总结→结束页
   - 交互边界：所有元素必须在页面内完全可见
5. **AI Skill创建方法论**：
   - 提取视觉DNA（风格关键词+主色+字体+标志性元素）
   - 编写Skill提示词模板
   - 保存迭代循环
6. **GitHub成熟Skill推荐**：
   - Slidev生态：官方Skill + dev-slides
   - Reveal.js生态：revealjs-skill（⭐30K+）+ OpenSlides
   - 纯Markdown生态：Marp Template
   - 传统PPTX路线：PPT Master

### Entities Created

| 实体 | 说明 |
|-----|------|
| Slidev | HTML Slides工具生态中的开发者首选，Markdown驱动+Vue技术栈 |

### Concepts Created

| 概念 | 说明 |
|-----|------|
| HTML幻灯片范式转移 | 从PowerPoint/WPS二进制格式转向HTML/CSS/JS纯文本格式的范式革命 |

---

## 2026-05-29 — Karpathy LLM Wiki 企业级组织记忆文章摄入 (872)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/LLM Wiki/Karpathy LLM Wiki + Context + Memory 重构企业级的组织记忆.md
**Time:** 2026-05-29
**New Sources:** 1
**New Entities:** 0 (Karpathy 已存在)
**New Concepts:** [[企业级组织记忆]], [[四信号知识图谱]], [[RAG]], [[Louvain社区检测]]
**Entities updated:** [[Karpathy]]
**Concepts updated:** [[知识编译]], [[LLM-Wiki]]
**index.md updated:** Statistics (Sources 1137→1138, Concepts 211→214)

### Key Findings

**Article 872 - Karpathy LLM Wiki + Context + Memory 重构企业级组织记忆:**

1. **核心命题**：知识不是"存起来备查"，而是"编译进去活起来"
2. **三层架构**：Raw Sources（源文件层）→ Wiki（Wiki层）→ Schema（规范层）
3. **三项核心操作**：
   - Ingest：知识的编译——将源文件"编译"成 Wiki 页面
   - Query：知识的查询——综合分析与引用，沉淀有价值回答
   - Lint：知识的维护——定期健康检查，确保 Wiki 不会"腐烂"
4. **传统 RAG 缺陷**：每次查询都是一次"重新发现"（rediscovering knowledge from scratch）
5. **企业级扩展**：个人→小团队→部门→企业四级演进
6. **四层 Memory 处理**：Working/Episodic/Semantic/Procedural Memory
7. **关键经验**：Schema 是活的文档、Log 是最有价值的文件、交叉引用是关键

### Concepts Created

| 概念 | 说明 |
|-----|------|
| 企业级组织记忆 | 用 LLM Wiki + Context + Memory 构建的 AI 时代企业级知识体系 |
| 四信号知识图谱 | 知识图谱构建中的四个关键信号维度（结构/语义/时序/使用） |
| RAG | Retrieval-Augmented Generation，传统知识检索架构及其缺陷分析 |
| Louvain社区检测 | 用于发现知识图谱中主题聚类的社区检测算法 |

### Entities Updated

| 实体 | 更新内容 |
|-----|---------|
| Karpathy | 添加三项核心操作、企业级组织记忆、新增来源文章引用 |

### Concepts Updated

| 概念 | 更新内容 |
|-----|---------|
| 知识编译 | 添加企业级扩展、三项核心操作、Memory 处理架构 |
| LLM-Wiki | 添加三层架构、三项核心操作、RAG 缺陷分析、企业级扩展 |

---

## 2026-05-29 — patent-disclosure-skill 文章摄入 (871)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/AI Coding/AI帮我写专利交底书？这个716星技能做到了.md
**Time:** 2026-05-29
**New Sources:** 1
**New Entities:** [[patent-disclosure-skill]], [[CNIPA]]
**New Concepts:** [[技术交底书自动化]], [[专利查新]], [[AgentSkills规范]]
**index.md updated:** Statistics (Sources 1136→1137, Entities 210→211, Concepts 209→211), AI Coding (11→12)

### Key Findings

**Article 871 - patent-disclosure-skill:**

1. **项目数据**: GitHub 716 Star, 92 Fork, MIT 协议，遵循 AgentSkills 规范
2. **七大核心能力**: 项目智能扫描/专利点挖掘/国知局优先查新/标准化交底书生成/标准化交付命名/自动自检/多轮迭代支持
3. **查新优先级**: 优先爬取 CNIPA → 降级到网络搜索，专属爬虫 `cnipa_epub_search.py`
4. **交付格式**: `.docx` 输出 + mermaid 图渲染成 PNG + 脱敏模板
5. **支持平台**: Claude Code/Cursor/OpenClaw 等 AgentSkills 兼容平台
6. **核心价值**: 专利点挖掘 + 国知局查新 + 脱敏交底书 + 多轮迭代，全流程 AI 自动化

### Entities Created

| 实体 | 说明 |
|-----|------|
| patent-disclosure-skill | GitHub 716 Star，中国专利交底书自动化工具 |
| CNIPA | 中国国家知识产权局，专利查新数据源 |

### Concepts Created

| 概念 | 说明 |
|-----|------|
| 技术交底书自动化 | AI 自动生成专利技术交底书完整工作流 |
| 专利查新 | 检索对比专利文献判断新颖性的关键步骤 |
| AgentSkills规范 | AI Agent 技能标准化规范，跨平台兼容 |

---

## 2026-05-29 — GitHub 需求雷达文章摄入 (869→870)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/GitHub/我把Github做成需求雷达，开源了.md
**Time:** 2026-05-29 08:00
**New Sources:** 1
**New Entities:** none (Codex already exists)
**New Concepts:** [[需求挖掘]]
**Entities updated:** [[Codex]] (添加 Hermes-Agent、GitHub Demand Radar 链接，添加需求挖掘等概念)
**index.md updated:** Statistics (Sources 1135→1136, Concepts 208→209), GitHub (27→28)

### Key Findings

**Article 870 - GitHub Demand Radar 开源:**

1. **项目定位**：GitHub Demand Radar — 从 GitHub 热门项目 Issue/PR 中挖掘真实需求的 Skill
2. **核心洞察**：找项目最难的不是写代码，而是判断"这个东西值得做"
3. **实验案例**：扫描 Claude Code buddy 桌宠功能需求热度极高，后续多个定制桌宠项目涌现
4. **判断标准**：用户反复提起 + 补充场景 + 情绪强 + 边界清楚 = 真实需求
5. **工具化流程**：之前手动翻 Github Trending → 现交给 Codex 每天早上定时发简报
6. **配置方法**：下载 geekjourneyx/github-demand-radar，输入提示词设置自动化
7. **时效性**：buddy 功能热度高峰已过，产品化窗口需把握时机

### Concepts Created

| 概念 | 说明 |
|-----|------|
| 需求挖掘 | 从 GitHub Issue/PR 等渠道发现真实需求的方法论 |

---

## 2026-05-28 — PPT Master 教程文章摄入 (869)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/PPT Master/PPT Master 教程：PDF 一键转可编辑 PPT，手把手带你从安装到出片.md
**Time:** 2026-05-28 12:00
**New Sources:** 1
**New Entities:** [[hugohe3]]
**New Concepts:** [[PDF转PPTX]], [[SVG转PPTX]]
**Entities updated:** [[ppt-master]], [[PPT制作]]
**index.md updated:** Statistics (Sources 1128→1129, Entities 206→213, Concepts 195→198), AI办公 (17→18)

### Key Findings

**Article 869 - PPT Master 教程 PDF转PPTX:**

1. **实战案例**：94页扫描版PDF《2023信息技术宝典手册（Python版）》→ 14页可编辑PPT
2. **能力边界**：
   - 擅长：Word/Markdown→PPT、网页链接→PPT、可搜索文字PDF→PPT、多格式混输入
   - 不擅长：扫描版PDF→PPT（需OCR）、复杂数据图表、独立运行（需AI IDE）
3. **SVG编写要点**：XML转义（<→<）、中文字体指定、数字前缀排序
4. **AI校验流程**：逐页核查知识点、联网验证细节、Python实际运行验证
5. **适合人群**：教师（教案转课件）、职场人（方案转演示）、学生（论文转答辩）

### Entities Created

| 实体 | 说明 |
|-----|------|
| hugohe3 | PPT Master项目作者，GitHub开源开发者 |

### Concepts Created

| 概念 | 说明 |
|-----|------|
| PDF转PPTX | PDF到PPTX的转换工作流，区分可搜索文字PDF和扫描版PDF |
| SVG转PPTX | SVG作为中间格式转DrawingML，核心技术管线 |

---

## 2026-05-28 — Agent时代商业重构文章摄入 (868)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/Agent/1400亿Agent入场，"流量"这条护城河要塌了.md
**Time:** 2026-05-28 08:00
**New Sources:** 1
**New Entities:** [[蚂蚁集团]], [[韩歆毅]], [[Google]], [[OpenAI]], [[Stripe]], [[Visa]], [[Mastercard]], [[支付宝]]
**New Concepts:** [[Agent时代]], [[智能体生态]], [[A2A协议]], [[ACP协议]], [[AI支付]]
**index.md updated:** Statistics (Sources 1127→1128, Entities 205→213, Concepts 193→198), Agent (101→102)

### Key Findings

**Article 868 - 1400亿Agent入场：**

1. **核心判断**：蚂蚁集团CEO韩歆毅提出三大判断——流量逻辑失效/信任逻辑崛起/Agent重构商业决策权
2. **规模预测**：中国14亿人，但Agent可能会有1400亿个
3. **三重范式重构**：
   - "人找服务" → "服务找人"
   - "商品交易、服务交易" → "任务交易"
   - "双边市场" → "多边网络"
4. **全球共识**：Google A2A协议、OpenAI/Stripe ACP协议、Visa Intelligent Commerce、Mastercard Agent Pay、支付宝ACT协议均指向智能体生态需要信任机制
5. **AI支付两大变革**：执行载体从人变成Agent（可追溯可审计）、价值载体从法定货币扩展到Token

### Entities Created

| 实体 | 说明 |
|-----|------|
| 蚂蚁集团 | 金融科技公司，提出Agent时代三大判断 |
| 韩歆毅 | 蚂蚁集团CEO，演讲核心人物 |
| Google | 推出A2A协议，搭建跨系统智能体协作网络 |
| OpenAI | 与Stripe推出ACP协议，把ChatGPT升级为交易入口 |
| Stripe | 与OpenAI合作ACP协议，补齐商家侧交易闭环 |
| Visa | 推出Intelligent Commerce，让Agent安全交易 |
| Mastercard | 推出Agent Pay，提供可信支付基础设施 |
| 支付宝 | Agent时代三层定位：信任层/连接器/赋能器 |

### Concepts Created

| 概念 | 说明 |
|-----|------|
| Agent时代 | 1400亿Agent参与商业链路的时代 |
| 智能体生态 | Agent数量规模、协同能力、网络化协作效应构成的新护城河 |
| A2A协议 | Google推出的Agent-to-Agent协议 |
| ACP协议 | OpenAI/Stripe推出的智能体电商协议 |
| AI支付 | Agent时代支付从工具升级为智能体商业生态基础设施 |

---

## 2026-05-27 — 微信同步 + 3篇文章摄入 (865-867)

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. 办公效率/我是怎么用飞书AI助手把公司办公效率翻倍的 → wiki/sources/飞书AI助手-办公效率翻倍.md
2. Hermes/用 Hermes Agent 搭一个 AI 销售代表，每天自动找线索、写邮件、跟进客户 → wiki/sources/Hermes-AI-SDR销售代表.md
3. AI工作流/裁员后一人干掉15人团队：这个跨境卖家的AI工作流，我拆给你看 → wiki/sources/跨境卖家AI工作流-一人团队.md
**Time:** 2026-05-27 18:00
**New Sources:** 3
**New Entities:** [[店小秘]], [[Tidio]], [[Perpetua]], [[Helium-10]]
**New Concepts:** [[AI-SDR]], [[注意力残留]], [[自动化运营]], [[AI选品]]
**Entities updated:** [[飞书]], [[OpenClaw]], [[Hermes-Agent]], [[Notion]], [[Supabase]]
**index.md updated:** Statistics (Sources 1124→1127, Entities 200→205, Concepts 189→193), 办公效率 (1→2), Hermes (199→200), AI工作流 (新建), 飞书 (10→11)

### Key Findings

**Article 865 - 飞书AI助手:**
1. 痛点：七八个办公系统来回切换，每次损失15秒注意力恢复时间，10人团队每天浪费50分钟
2. 解法：用 OpenClaw 搭建飞书 AI 机器人，以"团队成员"身份接入，AI 作为中间人连接各系统
3. 六大场景：文档助手/日程管理/数据查询/任务追踪/消息推送/群聊值班
4. 门槛低：从零到跑通第一个功能，半天就够

**Article 866 - Hermes AI SDR:**
1. AI SDR 自动研究潜在客户、写个性化邮件、筛选入站线索、更新 CRM、安排跟进
2. 效率对比：人类 SDR 每天研究 20-30 个；AI SDR 可同时研究几百个
3. 四大坑：邮件进垃圾箱/忘记退订/过度承诺/成本失控
4. Smart Routing：Gemini Flash 做研究（便宜），Claude/GPT 写邮件（质量高）

**Article 867 - 跨境卖家 AI 工作流:**
1. 案例：15人团队裁到1人，月流水 300万→120万，但净利润率 8%→15%
2. 五环节 AI 化：选品(3→0人)/文案(2→0人)/客服(5→1人)/广告(2→0人)/分析(1→0人)
3. AI选品命中率 93% vs 人工 30%；AI卖家 vs 非AI月利润差距 7倍
4. 四大爆发赛道：家居智能/绿色储能/健康美妆/银发经济

---

## 2026-05-26 — 7篇文章摄入 (847-854)

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. 飞书/通过飞书妙搭构建LLMWiki应用的实战指南 → wiki/sources/通过飞书妙搭构建LLMWiki应用的实战指南.md
2. WorkBuddy/WorkBuddy方法17 项目进度跟踪与甘特图 → wiki/sources/WorkBuddy方法17-项目进度跟踪与甘特图.md
3. OpenClaw/如何基于 Openclaw、Hermes、Opencode、pi-agent 来搭建自己的 Deep Research Agent → wiki/sources/如何基于Openclaw-Hermes-Opencode-pi-agent搭建Deep-Research-Agent.md
4. Claude/科研Skills更新了，Claude Code，Codex和小龙虾都能用 → wiki/sources/科研Skills更新-Claude-Code-Codex-小龙虾都能用.md
5. Agent/别再问要不要上 AI Agent，先问哪一步最该被替代 → wiki/sources/别再问要不要上AI-Agent-先问哪一步最该被替代.md
6. Claude/Text-to-CAD：用 AI 生成 3D 零件的开源 CAD 技能集 → wiki/sources/Text-to-CAD-AI生成3D零件开源CAD技能集.md
7. Hermes/让你的Hermes Agent发挥更大的价值 → wiki/sources/让你的Hermes-Agent发挥更大的价值.md
**Time:** 2026-05-26 14:00
**New Sources:** 7
**New Entities:** [[Karpathy]], [[飞书妙搭]], [[text-to-cad]], [[earthtojake]]
**New Concepts:** [[LLM-Wiki]], [[传统RAG困境]], [[甘特图自动生成]], [[Deep-Research-Agent]], [[database-lookup]], [[替代动作非人]], [[元提示]], [[Text-to-CAD]]
**Entities updated:** [[scientific-agent-skills]], [[WorkBuddy]]
**index.md updated:** Statistics (Sources 1109→1116, Entities 186→190, Concepts 178→186), Hermes (198→199), WorkBuddy (35→36), 飞书 (9→10), Agent (100→101), Claude (36→37), OpenClaw (135→136)

### Key Findings

**Article 847 - LLM Wiki via 飞书妙搭:**
1. 传统 RAG 困境：每次回答从零理解，没有记忆积累
2. Karpathy LLM Wiki 三层架构：`Raw Sources → Wiki → Schema`
3. 飞书妙搭三大优势：文档天然在飞书、用户无学习成本、核心是界面和流程
4. 最小可行路径：高频问题→第一批页面→对话入口→log.md日志

**Article 848 - WorkBuddy 甘特图:**
1. Prompt驱动甘特图自动生成，标识延期（红）/即将到期（黄）
2. 周会准备时间从2小时降到10分钟
3. 进阶：多项目组合、资源冲突检测、风险预警

**Article 849 - Deep Research Agent搭建:**
1. 框架对比：Hermes（最推荐，learning loop）、OpenClaw（always-on）、Pi-agent（极简）、OpenCode（coding）
2. 六步法：基础部署→Multi-Agent→MCP工具→迭代反思→输出持久化→优化生产化
3. 五角色分工：Planner/Researcher/Critic/Synthesizer/Coder

**Article 850 - Scientific Agent Skills更新:**
1. 152→139技能，database-lookup统一接口覆盖78数据库
2. 四类任务实测：文献综述超预期、数据分析看你会不会用、分子计算需验证、文档处理最稳定
3. 按场景推荐：科研写作/数据分析/生物信息学/药物发现

**Article 851 - Agent落地方法论:**
1. 替代动作非人：高频+标准化+低风险+ROI易量化
2. 流程接不住：输入规则输出异常边界都没定义
3. 四类场景：客服分流、线索初筛、内容初稿、报表汇总

**Article 853 - Text-to-CAD:**
1. build123d+OpenCascade，WASM浏览器端渲染
2. 七大技能：CAD生成/标准件/模型浏览/URDF/SDF/SRDF/SendCutSend
3. 多Agent支持：Codex/Claude Code/Gemini/OpenClaw

**Article 854 - Hermes Agent五大用法:**
1. /goal+元提示：让AI生成详细提示词再执行
2. 看板工作流：晨间任务丢进去，回来已完成
3. 竞品拆解：自动打开浏览器分析技术栈
4. 记忆Wiki：本地网站记录每次对话
5. 每日主动学习：早9点询问，积累对用户理解

---

## 2026-05-26 — 微信同步 + 3篇文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. Obsidian/用 Claude Code + Obsidian，打造属于自己的智能信息中枢 → wiki/sources/用-Claude-Code-Obsidian打造属于自己的智能信息中枢.md
2. GitHub/GitHub 炸了：19 万星的 Agent 配置天花板，一天涨 2k+星 → wiki/sources/GitHub-炸了-19万星的Agent配置天花板一天涨2k星.md
3. WorkBuddy/WorkBuddy资料库： 把AI训练成你的专属助理 → wiki/sources/WorkBuddy资料库-把AI训练成你的专属助理.md
**Time:** 2026-05-26 06:00
**New Sources:** 3
**New Entities:** [[ECC]], [[Affaan-Mustafa]], [[AgentShield]]
**New Concepts:** [[信息处理流程]], [[每日收工流程]], [[AI专属助理]], [[Agent-Harness]]
**Entities updated:** [[Claude Code]], [[Obsidian]], [[WorkBuddy]], [[Claude]], [[Cursor]], [[Codex]]

## 2026-05-26 — 2篇文章摄入 (855 & 856)

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. Agent/连夜打包！黑客松夺冠神作开源：含38个Agent、156项技能、千级安全测试 → wiki/sources/连夜打包-黑客松夺冠神作开源-ECC配置天花板.md
2. GitHub/今天 GitHub 上涨疯了的这个开源项目，程序员都在收藏 → wiki/sources/今天GitHub上涨疯了的开源项目-程序员都在收藏.md
**Time:** 2026-05-26 12:30
**New Sources:** 2
**New Entities:** [[Understand-Anything]]
**New Concepts:** [[黑客松]], [[持续学习系统]], [[代码知识图谱]]
**Entities updated:** [[ECC]], [[Affaan-Mustafa]], [[AgentShield]] (mentions: 1→2)
**index.md updated:** Statistics (Sources 1109→1111, Entities 186→187, Concepts 178→181), Agent (99→100), GitHub (26→27)

### Key Findings

**Article 855 - ECC 黑客松故事：**
1. 黑客松夺冠：2025年9月纽约，Anthropic × Forum Ventures，$15,000 奖金，8小时手搓 zenith.chat
2. ECC 核心数据：18.2万 Stars，60 Agent，232 Skill，75 命令，1282 安全检查
3. 安装方式：`/plugin marketplace add` + `/plugin install ecc@ecc`，勿与手动安装混用
4. AgentShield：三 Agent 红蓝对抗（Attacker/Defender/Auditor），扫描 CLAUDE.md/MCP/Hooks/Agent定义
5. 持续学习系统 v2：置信度机制（0.3→0.6→0.9）自动应用编码习惯，可导出分享团队
6. AI编程趋势：核心战场从「模型能力」转向「系统集成」

**Article 856 - Understand-Anything：**
1. GitHub Trending 第一名，单日新增 5,604 Stars，总 31k+
2. 核心命令：`/understand`（5 Agent扫描）、`/understand-dashboard`（交互图谱）、`/understand-diff`（影响分析）、`/understand-chat`（问答）
3. 技术路线：Tree-sitter 静态解析 + LLM 语义理解，两步分开结果更可靠
4. 图谱可提交 Git：JSON 文件团队共享，新人入职直接看图谱
5. 支持 15+ 工具：Claude Code/Cursor/Codex/Gemini CLI 等

---

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/diagram-maker Skill/智能体、MCP、Skill到底是个啥？大白话讲透.md
**Time:** 2026-05-25 00:10

## 2026-05-25 — 5篇文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. Claude/让你的 Claude Code 满血复活，Anthropic 在 GitHub 上开源了个插件。 → wiki/sources/让你的-Claude-Code-满血复活-Anthropic-开源官方插件.md
2. Agent/PDF 处理 Skill：让 Agent 真正会读、会拆、会抽取 PDF.md → wiki/sources/PDF-处理-Skill-让-Agent-真正会读会拆会抽取.md
3. AI大神/打工人必装的12个Skill，我全装了... → wiki/sources/打工人必装的12个Skill全装实测-3个真神3个救命6个未知.md
4. SkillManager/中国专利.skill：从项目文档到技术交底书.md → wiki/sources/中国专利-skill-从项目文档到技术交底书.md
5. AI生成PPT方案/AI 做 PPT 不难，难的是生成后还能改得动.md → wiki/sources/AI-做-PPT-难的是生成后还能改得动.md
**Time:** 2026-05-25 18:02
**New Sources:** 5 | **Entities touched:** Anthropic, claude-plugins-official, pdf-processing-skill-zh, patent-disclosure-skill, SlideMind, find-skills, deep-research, humanizer-zh 等
**Concepts touched:** Claude-Code-Plugins, PDF-处理流程, Agent-Skill, 专利交底书, HTML-SVG-PPT路线, 设计系统约束

## 2026-05-26 — 微信同步 + 3篇文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. Obsidian/用 Claude Code + Obsidian，打造属于自己的智能信息中枢 → wiki/sources/用-Claude-Code-Obsidian打造属于自己的智能信息中枢.md
2. GitHub/GitHub 炸了：19 万星的 Agent 配置天花板，一天涨 2k+星 → wiki/sources/GitHub-炸了-19万星的Agent配置天花板一天涨2k星.md
3. WorkBuddy/WorkBuddy资料库： 把AI训练成你的专属助理 → wiki/sources/WorkBuddy资料库-把AI训练成你的专属助理.md
**Time:** 2026-05-26 06:00
**New Sources:** 3
**New Entities:** [[ECC]], [[Affaan-Mustafa]], [[AgentShield]]
**New Concepts:** [[信息处理流程]], [[每日收工流程]], [[AI专属助理]], [[Agent-Harness]]
**Entities updated:** [[Claude Code]], [[Obsidian]], [[WorkBuddy]], [[Claude]], [[Cursor]], [[Codex]]

### Results

- **Sources processed:** 1
- **Categories:** diagram-maker Skill (1)
- **Source pages created:** 1 (wiki/sources/智能体MCP-Skill到底是啥5句话大白话讲透.md)
- **index.md:** Article already listed under Skills section (60篇)

### New Articles

|| ID | 分类 | 标题 | Slug |
||---|---|---|---|
|| 1 | diagram-maker Skill | 智能体、MCP、Skill到底是啥？5句话大白话讲透 | 智能体MCP-Skill到底是啥5句话大白话讲透 |

### Key Findings

1. **五大概念类比**: Agent=实习生本人，MCP=开通公司系统账号，Skill=标准操作手册，Rules=规矩，Memory=笔记本
2. **智能体vs大模型**: 大模型是你问它答，智能体是你交代任务它交付成果；大模型只会聊天，智能体会做事
3. **订饭店案例**: Memory→Rules→MCP→Skill四步协作，用户只说一句话，智能体完成全部工作
4. **数字员工公式**: MCP(工具)+Skill(章法)+Rules(底线)+Memory(记性)=能干活、会学习、守规矩、长记性的数字员工

---

## 2026-05-25 — AI运维终端文章重新摄入验证

**Operator:** Hermes Agent (scheduled cron task)
**Source:** 微信公众号/AI 运维终端/告别传统SSH！一款桌面级 AI 运维终端，体验嘎嘎好.md
**Time:** 2026-05-25

### 验证结果

该文章已于 2026-05-24 摄入并处理完毕。本次为验证性摄入，确认以下内容：

### 已存在的文件

| 类型 | 文件 | 状态 |
|---|---|---|
| Source | wiki/sources/告别传统SSH一款桌面级AI运维终端体验嘎嘎好.md | ✓ 存在且完整 |
| Entity | wiki/entities/GMSSH.md | ✓ 存在且完整 |
| Concept | wiki/concepts/SSH隧道.md | ✓ 存在且完整 |
| Concept | wiki/concepts/运维终端.md | ✓ 存在且完整 |

### 本次更新

| 类型 | 文件 | 更新内容 |
|---|---|---|
| Concept | wiki/concepts/MCP协议.md | 添加 GMSSH 关联、增加定义和应用场景章节 |

### Key Findings

1. **GMSSH 架构亮点**: 零侵入设计——所有可视化逻辑在客户端，服务器无需安装任何软件
2. **进程隔离**: 核心引擎 ga_main 管理独立子进程，插件崩溃不影响其他服务
3. **MCP 协议集成**: AI 通过 MCP 感知服务器实时状态，预置 50+ 运维技能包
4. **插件生态**: 核心闭源 + 生态开放策略，支持多语言开发（Python/Go/Node.js/Rust）

---

## 2026-05-24 — AI运维终端 & Hermes多代理系统文章摄入（2篇）

**Operator:** Hermes Agent (subagent task)
**Sources:** 微信公众号/AI 运维终端/, 微信公众号/Hermes/
**Time:** 2026-05-24 18:12

### Results

- **Sources processed:** 2
- **Categories:** AI运维终端 (1), Hermes (1)
- **Source pages created:** 2
- **Entity pages created:** 1 (GMSSH.md)
- **Concept pages created:** 5 (SSH隧道.md, 运维终端.md, Gateway路由.md, Profile系统.md, 知识库体系.md)
- **index.md updated:** Statistics (Sources 1092→1093, Entities 179→180, Concepts 186→191), Hermes (197→198), AI运维终端 (新增1篇)

### New Articles

| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | AI运维终端 | 告别传统SSH！一款桌面级 AI 运维终端，体验嘎嘎好 | 告别传统SSH一款桌面级AI运维终端体验嘎嘎好 |
| 2 | Hermes | 团队 Hermes 多代理系统部署指南 | 团队Hermes多代理系统部署指南 |

### Entities Created

- **GMSSH** — 桌面级 AI 驱动运维终端，纯 SSH 隧道零侵入架构，预置50+运维技能包

### Concepts Created

- **SSH隧道** — 零侵入运维通信技术，基于SSH协议的加密通道
- **运维终端** — AI驱动运维终端，图形化界面+AI辅助诊断
- **Gateway路由** — Hermes多代理路由系统，四种路由方式（Pairing/Command/Mention/Keyword）
- **Profile系统** — Hermes多代理配置管理机制，12个专业角色独立配置
- **知识库体系** — Hermes三层知识库架构（共享/角色/外部知识源）

### Key Findings

1. **GMSSH架构创新**: 零侵入设计——所有可视化逻辑在客户端，服务器无需安装任何软件，通过纯SSH隧道通信
2. **进程隔离设计**: 核心引擎ga_main管理独立子进程，某插件崩溃不影响其他服务，JSON-RPC 2.0协议支持多语言插件
3. **AI运维深度集成**: 通过MCP协议感知服务器实时状态，预置50+运维技能包，提供有上下文的诊断建议
4. **Hermes团队方案**: 12个专业角色代理（PM/UI/后端/前端/AI工程师/DevOps/QA/安全/Tech Lead/数据分析师/算法工程师/原型设计师）
5. **Gateway路由优先级**: @特定代理 → /命令 → 关键词匹配(阈值0.7) → 用户已配对 → 默认Profile
6. **三层知识库**: 共享知识库（所有角色可读）→ 角色知识库（仅本角色）→ 外部知识源（MCP协议集成）
7. **成本优化**: 混合方案（核心角色用企业版，一般开发用Copilot Enterprise）年成本80-120万，性价比最优

---

## 2026-05-24 — Agent/diagram-maker Skill/WorkBuddy Wiki Articles Ingestion (3篇)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/ (3 articles)
**Time:** 2026-05-24 18:10

### Results

- **Sources processed:** 3
- **Categories:** Agent (1), Skills (1), WorkBuddy (1)
- **Source pages created:** 3 (wiki/sources/)
- **Entity pages created:** 4 (Honcho.md, Plastic-Labs.md, WorkBuddy.md, 用户画像.md)
- **Concept pages created:** 2 (信息流自动化.md, 用户画像.md)
- **Concept pages updated:** 3 (记忆系统.md, MCP协议.md, Agent Skills.md)
- **index.md updated:** Statistics (Sources 1089→1092, Entities 178→180, Concepts 177→178), Agent (97→98), Skills (57→60), WorkBuddy (34→35)

### New Articles

|| ID | 分类 | 标题 | Slug |
||---|---|---|---|
|| 1 | Agent | Honcho：AI Agent记忆库，3年打磨让Agent真正认识用户 | Honcho-AI-Agent记忆库3年打磨让Agent真正认识用户 |
|| 2 | Skills | 智能体、MCP、Skill到底是啥？5句话大白话讲透 | 智能体MCP-Skill到底是啥5句话大白话讲透 |
|| 3 | WorkBuddy | 我用 WorkBuddy 建了一个新闻编辑部，一人公司正式开张！ | 我用WorkBuddy建了一个新闻编辑部一人公司正式开张 |

### Entities Created

- **Honcho** — Plastic Labs 开发的 AI Agent 记忆库，3,333 Stars，为 Agent 提供持久记忆
- **Plastic Labs** — Honcho 开发团队，专注 Agent 记忆问题
- **WorkBuddy** — 腾讯云 CodeBuddy 团队推出的 AI Agent 办公工具，"腾讯版 OpenClaw"

### Concepts Created

- **用户画像** — Agent 对用户的理解和表征，包括行为模式、偏好、知识等信息，随时间演化
- **信息流自动化** — 利用 AI Agent 自动抓取、筛选、整理、推送信息的系统，实现全流程自动化

### Key Findings

1. **Honcho 记忆系统**: 不同于简单的对话存储或 RAG 检索，Honcho 提供持续学习、自然语言查询、多实体支持，做了3年打磨（v3.0.6）
2. **Agent/MCP/Skill 概念解析**: Agent=实习生本人，MCP=开通公司系统账号，Skill=标准操作手册，Rules=规矩，Memory=笔记本
3. **WorkBuddy 新闻编辑部**: 6人虚拟团队（情报/编辑/视觉/运营/数据/写作 Agent），7×24小时全自动运转
4. **一人公司公式**: 一个人 + AI 助手 = 一支专业团队
5. **WorkBuddy 特点**: 执行即交付、多 Agent 并行协作、完全兼容 OpenClaw、本地执行数据安全

---

## 2026-05-24 — Skills Wiki Articles Ingestion (2篇)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/Skills/ (2 articles)
**Time:** 2026-05-24 18:30

### Results

- **Sources processed:** 2
- **Categories:** Skills (2)
- **Source pages created:** 2 (wiki/sources/)
- **Entity pages created:** 1 (wiki/entities/Skills-Manager.md)
- **Concept pages created:** 9 (wiki/concepts/)
- **index.md updated:** Statistics (Sources 1089→1091, Entities 178→179, Concepts 177→186), Skills section (57→59篇)
- **concept-table.md updated:** +9 concepts

### New Articles

| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | Skills | 20 个 Agent Skills 盘点：先装这 5 个就够了 | 20个-Agent-Skills-盘点-先装这5个就够了 |
| 2 | Skills | Skills装太多怎么办？用Skills Manager桌面应用统一管理 | Skills装太多怎么办-用Skills-Manager桌面应用统一管理 |

### Entity Created

- **Skills-Manager** — 跨平台桌面应用（Tauri 2 + React + Rust），统一管理15+款AI编码工具的Skills

### Concepts Created

- **中央技能库** — ~/.skills-manager统一存放，再分发到各Agent目录
- **Preset** — 可复用Skill分组，一键给Agent挂上/卸下整组Skill
- **多工具同步** — 中央库→Agent目录的同步机制，软链接或复制
- **Git备份** — skills/子目录版本历史，支持远程push/pull与快照恢复
- **技能分发** — 中央库→Agent全局/项目目录的分发过程
- **Skill安装策略** — 分批安装、指标绑定、周度复盘方法论
- **工程场景分类** — Skills按4类分类：发现/前端/自动化/后端
- **落地SOP** — Agent Skills的3周落地方案

### Key Findings

1. **Skills-Manager**: 15+工具统一管理，Tauri 2 + React + Rust技术栈，支持Preset/全局工作区/项目工作区
2. **安装策略**: 先装前5个高收益组合，逐周扩展，绑定验收指标，周度复盘保留/替换/淘汰
3. **四类分类**: 发现与规划/前端与设计质量/自动化与内容生产/后端平台治理
4. **避坑**: 不要把skill当插件收藏夹，要当成规则资产；无验收指标的安装等于没落地

---

## 2026-05-24 — GitHub热门项目盘点文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/GitHub/不要错过这 10 个本周火火火的 GitHub 开源项目。.md
**Time:** 2026-05-24 14:30

### Results

- **Sources processed:** 1
- **Categories:** GitHub (1)
- **Source pages created:** 1 (wiki/sources/不要错过这10个本周火火火的-GitHub-开源项目.md)
- **Entity pages updated:** 9 (添加来源文章引用)
- **Concept pages updated:** 2 (Agent工程原则.md, 多智能体协作.md)
- **index.md updated:** Statistics (Sources 1088→1089), GitHub section (25→26篇)

### New Articles

| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | GitHub | 不要错过这10个本周火火火的 GitHub 开源项目 | 不要错过这10个本周火火火的-GitHub-开源项目 |

### Entities Updated (添加来源引用)

- **scientific-agent-skills** — AI科研全家桶，2.5万+Star，133技能覆盖6大领域
- **academic-research-skills** — 论文写作流水线，~2万Star，一周涨1万+
- **Understand-Anything** — 代码库知识图谱，~2万Star，可交互可视化
- **codegraph** — 本周黑马，~1.8万Star，一周涨1.4万+
- **oh-my-pi** — 终端AI编程助手，~6000Star，Hashline编辑减少61%token
- **12-factor-agents** — Agent工程十二条军规，2.1万Star
- **ai-engineering-from-scratch** — 从零学AI工程，1.2万+Star，428节课320小时
- **supertonic** — 端侧离线TTS，99M参数，31语言支持
- **ViMax** — HKUDS多Agent视频剧组，四角色协作

### Key Findings

1. **热度趋势**: 本周多个项目单周涨星1万+，Skill相关项目持续火爆
2. **核心主题**: Agent工程纪律、代码知识图谱、多Agent协作、端侧推理、Skill生态爆发
3. **差异化亮点**: oh-my-pi拿编辑精度当差异化武器，Hashline系统解决空白符不匹配问题
4. **工程化趋势**: 12-factor-agents把LLM当自然语言到工具调用的转换引擎，用确定性代码控制流程
5. **协作模式**: ViMax把视频制作拆成导演/编剧/制片/视频生成器四个AI角色

---

## 2026-05-24 — GitHub开源项目文章批量摄入（9篇）

**Operator:** Hermes Agent (subagent task)
**Source:** 微信公众号/ (9 new GitHub articles)
**Time:** 2026-05-24

### Results

- **Sources processed:** 9
- **Categories:** AI技术 (3), AI Coding (3), Agent Teams (1), AI入门 (1), 视频制作 (1)
- **Source pages created:** 9 (wiki/sources/)
- **Entity pages created:** 12 (wiki/entities/)
- **Concept pages created:** 16 (wiki/concepts/)
- **index.md updated:** Statistics (Sources 1088→1097, Entities 178→189, Concepts 177→193)
- **All sections updated:** AI技术 (15→18), AI Coding (7→10), Agent Teams (3→4), AI入门 (2→3), 视频制作 (3→4)

### New Articles

| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | AI技术 | AI科研全家桶133个技能包 | AI科研全家桶133个技能包 |
| 2 | AI技术 | 学术论文写作全流程管线 | 学术论文写作全流程管线 |
| 3 | AI技术 | 闪电般快速的端侧离线TTS | 闪电般快速的端侧离线TTS |
| 4 | AI Coding | 把代码库变成可交互知识图谱 | 把代码库变成可交互知识图谱 |
| 5 | AI Coding | 给AI提前做功课的代码知识图谱 | 给AI提前做功课的代码知识图谱 |
| 6 | AI Coding | 内置IDE能力的终端AI编程助手 | 内置IDE能力的终端AI编程助手 |
| 7 | Agent Teams | 构建可靠AI Agent的十二条军规 | 构建可靠AI Agent的十二条军规 |
| 8 | AI入门 | 从零开始AI工程428节课 | 从零开始AI工程428节课 |
| 9 | 视频制作 | 多智能体协作视频生成框架 | 多智能体协作视频生成框架 |

### Entities Created

- **scientific-agent-skills** — 133个科研技能，覆盖9大领域（25k Stars）
- **academic-research-skills** — 学术论文写作全流程管线（~20k Stars）
- **supertonic** — 端侧离线TTS系统，99M参数，31语言
- **Understand-Anything** — 代码知识图谱+Dashboard（~20k Stars）
- **codegraph** — MCP Server形式的代码知识图谱（~18k Stars）
- **oh-my-pi** — 终端AI编程助手，32工具40+Provider（~6k Stars）
- **12-factor-agents** — Agent工程12条原则（~21k Stars）
- **ai-engineering-from-scratch** — 428节课AI工程学习（~7.5k Stars）
- **ViMax** — 多智能体协作视频生成框架（港大HKUDS）
- **HKUDS** — 港大数据智能实验室
- **MiniMax** — AI大模型提供商（M2.7有1M上下文）

### Concepts Created

- **Agent Skills** — 标准化技能包封装
- **端侧推理** — 本地设备运行AI模型
- **MCP Server** — AI Agent标准化工具接口
- **代码知识图谱** — 结构化代码关系图谱
- **多智能体协作** — 多Agent角色分工协作
- **Agent工程原则** — 12-Factor Agent方法论
- **学术写作管线** — 论文全流程自动化
- **Hashline编辑** — 内容哈希锚点定位代码
- **tree-sitter** — 增量AST解析器
- **FTS5全文搜索** — SQLite全文搜索扩展
- **Idea2Video** — 灵感到视频自动化
- **Expression Tags** — TTS情感控制标签
- **引用审计** — 反幻觉引用验证机制
- **RAG长脚本生成** — RAG技术生成长脚本
- **六步教学模式** — AI工程教学方法

### Key Technical Findings

1. **scientific-agent-skills**: 133技能覆盖生物信息学、化学信息学、药物发现等9领域，100+科学数据库统一访问
2. **academic-research-skills**: 13+12+7代理协作，10阶段编排器，v3.8新增引用审计反幻觉机制
3. **supertonic**: 99M参数，ONNX Runtime完全离线，CPU媲美A100速度，11平台SDK
4. **Understand-Anything**: 多代理管道分析，业务逻辑域视图(domains/flows/steps)，15+平台兼容
5. **codegraph**: 7个代码库基准测试，平均节省35%成本、59% Token、49%时间、70%工具调用
6. **oh-my-pi**: 27k行Rust原生模块，Hashline编辑减少61% Token，双内核执行
7. **12-factor-agents**: 借鉴12-Factor Apps，核心理念是把LLM当转换引擎、用确定性代码控制流程
8. **ai-engineering-from-scratch**: 428节课320小时，六步教学(Motto→Problem→Concept→Build→Use→Ship)
9. **ViMax**: 四角色协作(Director/Screenwriter/Producer/Video Generator)，支持Idea2Video/Novel2Video/Script2Video

---

## 2026-05-24 — OPC Skills 一人企业方法论文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/SkillManager/把_一人企业方法论_装进 AI：9 个 Skill，帮你从盘点到闭环搭起自己的小生意.md
**Time:** 2026-05-24 12:20

### Results

- **Sources processed:** 1
- **Categories:** SkillManager (1)
- **Source pages created:** 1 (wiki/sources/把一人企业方法论装进AI-9个Skill.md)
- **Entity pages created:** 3 (一人企业方法论.md, OPC技能集.md, 易仁永澄.md)
- **Concept pages created:** 4 (利基定位.md, MVP设计.md, 资源盘点.md, 九步建盘.md)
- **index.md updated:** Statistics (Sources 1087→1088, Entities 175→178, Concepts 175→179), AI办公 section (+1 article)
- **concept-table.md updated:** +4 concepts (九步建盘, 利基定位, MVP设计, 资源盘点)

### New Articles

|| ID | 分类 | 标题 | Slug ||
||---|---|---|---||
|| 1 | SkillManager | 把一人企业方法论装进AI：9个Skill帮你从盘点到闭环搭起自己的小生意 | 把一人企业方法论装进AI-9个Skill |

### Entities Created

- **一人企业方法论** — 易仁永澄提出的一套系统化方法论，将一人企业搭建拆解为九步建盘体系
- **OPC技能集** — 方糖团队将方法论封装为9个可调用AI Agent Skill，总编排串联各步骤
- **易仁永澄** — 《一人企业方法论³》创始人

### Concepts Created

- **九步建盘** — 一人企业方法论核心流程框架：线性7步(01→07)严格顺序 + 触发2步(08、09)按需触发
- **利基定位** — 第02步："三环合一"找细分市场，6维评分筛选候选
- **MVP设计** — 第06步：决定验证哪个假设、最小形式、成功标准
- **资源盘点** — 第01步：按8类(经验/人群/能力/关系/渠道/资产/约束/硬性边界)盘点手上有什么

### Key Findings

1. **方法论AI化**: OPC技能集将易仁永澄的《一人企业方法论³》封装为9个可调用的Skill，传播损耗几乎为零
2. **核心价值**: 最值钱的是"拦着你别瞎做"——AI反复劝退、设边界、定成功标准
3. **真实案例**: 室内设计师林夏用3小时副业时间走完流程，锁定"报价防坑陪跑+平替设计"组合
4. **结构化输出**: 每步产出文档(inventory.md、lean-canvas.md、mvp-spec.md等)作为下一步输入和复盘底稿
5. **安装方式**: npx skills add github.com/easychen/opc-methodology/skills/opc-orchestrator 等命令

---

## 2026-05-24 — Obsidian Sync 方案对比文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/Obsidian/Obsidian 怎么同步？4 套方案深度对比，终于不用折腾了（2026 最新版）.md
**Time:** 2026-05-24 13:00

### Results

- **Sources processed:** 1
- **Categories:** Obsidian (1)
- **Source pages created:** 1 (wiki/sources/Obsidian怎么同步-4套方案深度对比-2026最新版.md)
- **Entity pages created:** 3 (Obsidian-Sync.md, Remotely-Save.md, WebDAV.md)
- **Concept pages created:** 2 (同步冲突处理.md, 云盘同步.md)
- **index.md updated:** Statistics (Sources 1087→1088, Entities 175→178, Concepts 175→177), Obsidian section (33→34篇)

### New Articles

|| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | Obsidian | Obsidian 怎么同步？4 套方案深度对比（2026 最新版） | Obsidian怎么同步-4套方案深度对比-2026最新版 |

### Entities Created

- **Obsidian-Sync** — Obsidian官方同步服务，约$48/年，冲突处理能力强，支持端到端加密
- **Remotely-Save** — Obsidian社区同步插件，通过WebDAV协议实现多端同步，国内用户免费首选
- **WebDAV** — 远程文件同步协议，"远程文件夹"，支持NAS/坚果云/私有服务器

### Concepts Created

- **同步冲突处理** — 多设备同时修改同一文件时的处理能力，Obsidian Sync/Git强，云盘方案弱
- **云盘同步** — 用云盘同步Obsidian文件夹的方案，iCloud/OneDrive/坚果云，冲突处理弱

### Key Technical Findings

1. **四种同步方案对比表**：Obsidian Sync(付费强冲突处理)、云盘方案(免费弱冲突)、Git(免费强版本控制)、Remotely Save+WebDAV(免费中冲突)
2. **云盘方案铁律**：不要同时在两台设备编辑同一个文件，会产生冲突副本需手动合并
3. **国内用户首选**：Remotely Save + 坚果云 WebDAV，速度快、免费、移动端体验好
4. **NAS终极方案**：数据完全自主，局域网同步速度快
5. **本地优先哲学**：Obsidian核心理念"数据首先属于你自己"，代价是同步需自己解决

---

## 2026-05-24 — Wechat-Cli + Graphify LLM Wiki 文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/LLM Wiki/Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki.md
**Time:** 2026-05-24 12:12

### Results

- **Sources processed:** 1
- **Categories:** LLM Wiki (1)
- **Source pages created:** 1 (wiki/sources/Wechat-Cli-将微信聊天记录导入-Karpathy的-LLM-Wiki.md)
- **Entity pages updated:** 2 (wechat-cli.md, Graphify.md)
- **Concept pages created:** 3 (暗知识.md, 微信数据导出.md, 增量同步.md)
- **index.md updated:** Statistics (Sources 1085→1086, Concepts 174→177), LLM-Wiki section (11→12篇)
- **concept-table.md updated:** +3 concepts (暗知识, 微信数据导出, 增量同步)

### New Articles

|| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | LLM Wiki | Wechat-Cli + Graphify — 从加密数据库到结构化知识图谱的完整链路 | Wechat-Cli-将微信聊天记录导入-Karpathy的-LLM-Wiki |

### Entities Updated

- **wechat-cli** — 提及文章数 1→3，新增核心技术原理（AES-256-CBC解密、task_for_pid）、11条命令详解、安全特性、安装要点
- **Graphify** — 提及文章数 2→3，新增与wechat-cli配合使用说明、输出产物表格

### Concepts Created

- **暗知识** — 有价值但从未被记录到正式文档中的隐含信息，如群聊中的决策和共识
- **微信数据导出** — 从微信加密数据库（SQLCipher）提取聊天记录的技术过程，需进程内存扫描提取密钥
- **增量同步** — 知识库定期自动追加最新内容的维护模式，通过new-messages接口实现零维护成本更新

### Key Technical Findings

1. **解密原理**: 微信Mac版使用SQLCipher加密SQLite数据库，密钥藏在进程内存，wechat-cli用320行C代码通过`task_for_pid`读取
2. **macOS签名要求**: 需给微信添加`get-task-allow`调试权限，绕开/Applications保护（复制到~/Applications）
3. **从源码安装必要性**: 需sudo权限扫描进程内存，不应信任预编译二进制
4. **完整链路**: wechat-cli export → Markdown → Graphify → 知识图谱（graph.html + graph.json + GRAPH_REPORT.md）
5. **自动化同步**: `new-messages`命令 + cron实现知识库每天自动更新

---

## 2026-05-24 — Obsidian Beginner Articles Ingestion

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/ (2 Obsidian beginner articles processed)
**Time:** 2026-05-24 12:00

### Results

- **Sources processed:** 2
- **Categories:** Obsidian (2)
- **Source pages created:** 2 (wiki/sources/)
- **Entity pages updated:** 1 (Obsidian.md)
- **Concept pages created:** 1 (第二大脑.md)
- **Concept pages updated:** 2 (本地优先.md, 双向链接.md)
- **index.md updated:** Statistics (Sources 1085→1087, Obsidian 31→33)
- **concept-table.md updated:** +1 concept (第二大脑)

### New Articles

|| ID | 分类 | 标题 | Slug |
||---|---|---|---|
|| 1 | Obsidian | 20分钟，让你的Obsidian从"能用"变成"想用" | 20分钟-让你的-Obsidian-从能用变成想用 |
|| 2 | Obsidian | Obsidian新手入门：安装、仓库、插件，一篇讲透 | Obsidian新手入门-安装仓库插件-从零开始搭建第二大脑 |

### Key Concepts Identified

- **Obsidian vs Notion/飞书/Logseq对比**：本地优先、数据归属、双向链接、插件生态差异
- **本地优先哲学**：数据安全、离线可用、无厂商锁定
- **双向链接**：`[[笔记名]]`语法，反向链接面板，知识网络而非散落纸片
- **第二大脑**：不是存储内容而是连接知识，训练思维网络
- **仓库（Vault）**：一个文件夹+配置数据，Obsidian核心概念
- **核心插件**：Templater、Dataview、Calendar、Kanban

### Entity/Concept Updates

- **Obsidian.md**：更新mentions数，增加"第二大脑"核心特性
- **本地优先.md**：增加Obsidian实践案例，与Notion/飞书对比
- **双向链接.md**：完整重写，增加Obsidian实践和工具对比表
- **第二大脑.md**：新建，系统阐述Obsidian知识管理理念

### Notes

- 两篇文章内容高度重叠，第二篇是第一篇的扩展版本
- Obsidian定位：个人知识操作系统，而非笔记软件
- 核心差异点：本地优先（数据自主）vs 云端工具（数据在厂商）
- 双向链接是Obsidian最强功能，让知识形成网络

---

## 2026-05-24 — Dify 数据可视化 MCP 工具摄入

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/Dify/dify打造数据可视化图表.md
**Time:** 2026-05-24

### Results

- **Sources processed:** 1
- **Categories:** Dify (1 new)
- **Source pages created:** 1 (wiki/sources/dify打造数据可视化图表.md)
- **Entity pages created:** 2 (mcp-server-chart.md, AntV.md)
- **Concept pages updated:** 3 (数据可视化, 自然语言转SQL, 图表生成, Dify工作流)
- **index.md updated:** Statistics (Sources 1085→1086, Entities 175→177), Dify section (1→2篇)
- **concept-table.md updated:** +3 concepts (图表生成, 自然语言转SQL, Dify工作流)

### New Articles

|| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | Dify | Dify打造数据可视化图表：mcp-server-chart MCP 工具实战 | dify打造数据可视化图表 |

### Entities Created

- **mcp-server-chart** — 蚂蚁集团 AntV 团队开源的 MCP Server，支持 15+ 种图表类型，图片链接返回
- **AntV** — 蚂蚁集团数据可视化团队，提供 mcp-server-chart 和 Dify 插件市场可视化工具

### Concepts Added/Updated

- **数据可视化** — 提及文章数 18→19
- **图表生成** — AI驱动的数据可视化图表自动生成，支持15+种图表类型
- **自然语言转SQL** — ROOKIE_TEXT2DATA 插件核心能力
- **Dify工作流** — 可视化工作流编排，节点式流程设计

### Key Findings

1. **DeepSeek-V3 必需**: Dify 工作流必须使用 DeepSeek-V3 模型才能成功生成图表，其他模型会失败
2. **SSE 协议限制**: Dify 插件 Agent 策略不支持 streamable_http，必须使用 SSE 协议连接 MCP
3. **三协议支持**: mcp-server-chart 支持 STDIO、SSE、streamable Http，但不同客户端支持度不同
4. **图片链接输出**: 所有图表通过支付宝 CDN 返回图片链接，公网可访问
5. **两种集成方式**: Cherry Studio（streamable Http）vs Dify 工作流（SSE）

---

## 2026-05-23 — WeChat Article Batch 6 Ingestion

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/ (11 articles processed)
**Time:** 2026-05-23 06:00

### Results

- **Sources processed:** 11
- **Categories:** Prompt (2), LLM Wiki (1), Skills (1), MarkItDown (1), SkillManager (2), AI生成PPT方案 (1), GitHub (1), RAG (1), Agent (1)
- **Source pages created:** 11 (wiki/sources/)
- **Concept pages created:** 4 (Design System, GraphRAG, MinerU, 数字员工)
- **index.md updated:** Statistics (Sources 1074→1085, Concepts 170→174)
- **concept-table.md updated:** +4 concepts

### New Articles

| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | Prompt | 开源\|一款AI Prompt和Skill管理系统，支持多平台安装、版本控制与多模型测试 | 开源-PromptHub |
| 2 | LLM Wiki | LLM Wiki知识管理上手更丝滑 | LLM-Wiki知识管理上手更丝滑 |
| 3 | Skills | hack-skills 助力 AI 智能体成长为实力顶尖的实战渗透高手！ | hack-skills-助力AI智能体成长为实战渗透高手 |
| 4 | Prompt | 从 Prompt 到 Skill：一套搭建数字员工体系的完整方法论 | 从-Prompt到Skill-数字员工体系方法论 |
| 5 | MarkItDown | 带图PDF 怎么转 Markdown？我终于找到了的最终方案 | 带图PDF转Markdown-工具对比 |
| 6 | SkillManager | 2026年最全创作SKILL：从热点到发布，Skill一套5分钟搞定 | 2026年最全创作SKILL-从热点到发布5分钟搞定 |
| 7 | SkillManager | 再也不用求前端了！这个开源免费的skill让你一秒拥有专业级UI设计能力 | UI-UX-Pro-Max-Skill专业级UI设计 |
| 8 | AI生成PPT方案 | skill自动生成宣传效果图片和可以编辑的ppt | PPT-Master自动生成宣传图片和可编辑PPT |
| 9 | GitHub | GitHub 每日推荐 \| 2026年05月22日 星期五 | GitHub-每日推荐-2026-05-22 |
| 10 | RAG | 基于知识图谱的多模态 GraphRAG 项目实战，系统架构详解 | GraphRAG项目实战-多模态知识图谱系统架构 |
| 11 | Agent | 别再堆 Agent 了，企业 AI 要先把流程做成 Skill | 别再堆Agent了-企业AI要把流程做成Skill |

### Notes

- Design System: AI编程工具的自动设计系统生成（67种UI风格、161套行业配色）
- GraphRAG: 向量检索+图遍历混合，多跳推理问答，Neo4j+Milvus双索引
- MinerU: 多模态PDF解析，109种语言OCR，表格/公式/图片完整保留
- 数字员工: 基于Skill封装的AI工作团队，使AI能稳定、专业地执行特定任务

## 2026-05-22 — WeChat Article Batch 5 Ingestion

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/ (7 articles processed)
**Time:** 2026-05-22 22:27

### Results

- **Sources processed:** 7
- **Categories:** Skills (1), Agent (1), 知识库 (1), Obsidian (1), LLM Wiki (2), SkillManager (1)
- **Source pages created:** 7 (wiki/sources/)
- **Entity pages created:** 1 (CLI-Anything)
- **Concept pages created:** 5 (text-to-cad, 参数化设计, CLI-Hub, 知识库自动化, Memex)
- **index.md updated:** Statistics (Sources 1074→1081, Entities 175→176, Concepts 170→175)
- **concept-table.md updated:** +5 concepts

### New Articles

| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | Skills | 3款AI生成CAD的开源Skills，AI生成BIM | 3款AI生成CAD的开源SKillsAI生成BIM |
| 2 | Agent | CLI-Anything：把任意软件变成AI能用的CLI工具 | CLI-Anything把任意软件变成AI能用的CLI工具好用爆了 |
| 3 | 知识库 | 企业自建内部知识库最容易死在8个问题上 | 企业自建内部知识库最容易死在这8个问题上管理技术双维度 |
| 4 | Obsidian | 别再把Obsidian只当笔记软件了高阶玩家都在这样用 | 别再把Obsidian只当笔记软件了高阶玩家都在这样用 |
| 5 | LLM Wiki | 给Karpathy的LLMWiki装上自动引擎 | 给Karpathy的LLMWiki装上自动引擎 |
| 6 | LLM Wiki | Karpathy的LLMWiki火了但他没解决一个问题 | Karpathy的LLMWiki火了但他没解决一个问题 |
| 7 | SkillManager | AISkill给数字员工配的操作册 | AISkill给数字员工配的操作册 |

### Notes

- text-to-cad: AI生成CAD开源工具，支持STEP/STL/3MF/DXF/URDF/SRDF/SDF格式导出
- CLI-Anything: HKUDS开发的CLI自动生成工具，7阶段流水线让Agent操作任意软件
- 企业知识库8大问题: 管理7问题+技术AI只搜索不分析
- Obsidian高阶用法: CSS/Templater/QuickAdd/Obsidian URI/插件开发
- LLM Wiki自动引擎: AutoCLI定时抓取+Agent编译+微信推送日报
- LLM Wiki问题: 被动容器需要人工喂料，三步解决方案让知识库自动运转
- AI Skill: Agent生态四要素，Skill=标准工作手册

---

## 2026-05-22 — WeChat Article Batch 4 Ingestion

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/ (2 articles processed)
**Time:** 2026-05-22 18:00

### Results

- **Sources processed:** 2
- **Categories:** Agent (1), LLM Wiki (1)
- **Source pages created:** 2 (wiki/sources/)
- **Entity pages created:** 1 (CLI-Anything)
- **Concept pages created:** 2 (Agent-Native, API-First)
- **index.md updated:** Statistics (Sources 1072→1074, Entities 174→175), Agent section (+1), LLM-Wiki section (+1)
- **concept-table.md updated:** +2 concepts

### New Articles

| ID | 分类 | 标题 | Slug |
|---|---|---|---|
| 1 | Agent | 35.6K Stars 的 CLI-Anything 揭示了什么？Agent-Native 时代来了 | 35-6K-Stars-CLI-Anything-Agent-Native |
| 2 | LLM Wiki | LLM Wiki 架构解析：Karpathy 的 Markdown 知识库模式 | LLM-Wiki-架构解析-Karpathy-Markdown-知识库模式 |

### Notes

- CLI-Anything (35.6K Stars): 让所有软件原生支持 AI Agent 调用的 CLI 工具，Agent-Native 架构趋势的代表项目
- LLM Wiki 架构解析: Karpathy 的 Markdown 知识库模式深度解析，四层架构（Raw Sources → Ingest → Wiki → Query Loop）
- 新增实体: CLI-Anything
- 新增概念: Agent-Native, API-First

---

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


## 2026-05-25 — 微信同步

## 2026-05-25 — 微信同步 (定时任务)

**Operator:** Hermes Agent (scheduled cron)
**Time:** 2026-05-25 12:02

### Run Summary

- **收集阶段:** 0 新增入队 | 队列状态: pending=2, success=818
- **处理阶段:** 成功处理 2 篇（Prompt x1, PPT skill x1）
- **摄入状态:** 已在 2026-05-25 上午批次完成，wiki 页面已存在

### Articles (已在上午批次摄入)

||| ID | 分类 | 标题 | 状态 ||
|||---|---|---|---|||
||| 1 | Prompt | [开源]本地优先的 Prompt、Skill 与 AI 编程资产工作台 | 已存在 ||
||| 2 | PPT skill | 10.6k Star！Claude御用PPT Skill实测 | 已存在 ||

### Git Status

- Wiki 页面无变更（上午批次已提交）
- 仅做拉取同步

## 2026-05-25 — 晚间批次：5篇文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. LLM Wiki/LLM Wiki 项目分享：知识管理的演变洞察.md → wiki/sources/llm-wiki-项目分享-知识管理的演变洞察.md
2. WorkBuddy/免费！AI视频生成实战：30分钟用WorkBuddy做出爆款书籍带货视频，0门槛上手！.md → wiki/sources/免费-AI视频生成实战-30分钟用WorkBuddy做出爆款书籍带货视频-0门槛上手.md
3. Claude/GitHub上最火的10个MCP服务器，让Claude Code连接万物（保姆级）.md → wiki/sources/github上最火的10个MCP服务器-让Claude-Code连接万物保姆级.md
4. AI生成PPT方案/一句话生成PPT，已经能用了：html-ppt-skill实测指南.md → wiki/sources/一句话生成PPT-已经能用了-html-ppt-skill实测指南.md
5. PPT Master/PPT Master：AI 造 PPT 的正确姿势.md → wiki/sources/ppt-master-AI-造-PPT的正确姿势.md
**Time:** 2026-05-25 22:58
**New Sources:** 5 | **Entities touched:** WorkBuddy (mentions: 36→36, updated), PPT Master (full rewrite), html-ppt-skill
**Concepts touched:** MCP Server (更新Top 10列表), LLM Wiki方法论, AIGC工作流, AI视频生成

### Results

- **Sources processed:** 5
- **Categories:** LLM Wiki (1), WorkBuddy (1), Claude (1), AI生成PPT方案 (1), PPT Master (1)
- **Source pages created:** 5
- **Entities updated:** WorkBuddy (add book-viral-script/edgetTS/ffmpeg capabilities), PPT Master (full rewrite with v2.8.0 details)
- **Concepts updated:** MCP Server (add Top 10 MCP servers table)
- **index.md:** Added 5 new source entries under AI办公/Claude/LLM-Wiki sections, Sources: 1098→1103

## 2026-05-26 12:00 — 微信同步：2篇文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. Agent/DeepSeek-Reasonix 爆火开源，DeepSeek 原生的终端 AI 编程Agent，前缀缓存命中率99.82%，Token成本再降80%.md → wiki/sources/deepseek-reasonix-爆火开源-deepseek-原生的终端-ai-编程agent.md
2. 微信全流程 Skill/5分钟，我要这个公众号的所有文章.md → wiki/sources/5分钟我要这个公众号的所有文章.md
**Time:** 2026-05-26 12:00
**New Sources:** 2 | **Entities touched:** DeepSeek (mentions: 54→55, updated)
**Concepts touched:** Token成本优化 (new), 内容筛选 (new), 信息获取 (new), AI编程 (updated)

### Results

- **Sources processed:** 2
- **Categories:** Agent (1), 微信全流程 Skill (1)
- **Source pages created:** 2
- **Entities created:** [[wechat-article-exporter]]
- **Entities updated:** [[DeepSeek]]
- **Concepts created:** [[Token成本优化]], [[内容筛选]], [[信息获取]]
- **Concepts updated:** [[AI编程]]
- **index.md:** Added 2 new source entries under Agent and 微信全流程 Skill sections, Sources: 1106→1108, Entities: 183→185, Concepts: 174→176


## 2026-05-26 — wechat-article-exporter 摄入

**Operator:** Hermes Agent (手动触发)
**Source:** GitHub/wechat-article-exporter.md
**Time:** 2026-05-26 14:15
**New Sources:** 1 | **Entities touched:** wechat-article-exporter
**Concepts touched:** 微信公众号文章抓取、文章格式还原
**Summary:** 处理 GitHub/wechat-article-exporter.md。新建 4 个页面（1 source + 1 entity + 2 concepts），更新 1 个页面（index.md）。
新实体：wechat-article-exporter。新概念：微信公众号文章抓取、文章格式还原。

## 2026-05-27 00:00 — 微信同步：4篇文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. AI工具/一个Skill，搞定12种AI工具的提示词.md → wiki/sources/一个Skill-搞定12种AI工具的提示词.md
2. WorkBuddy/装上这三个Skill：在WorkBuddy轻松做出有格调的PPT和配图！.md → wiki/sources/装上这三个Skill-在WorkBuddy轻松做出有格调的PPT和配图.md
3. WorkBuddy/WorkBuddy 100种用法 #56 | "做个西游记PPT" → 15页网页演示上线，全程零操作.md → wiki/sources/WorkBuddy-100种用法-56-西游记PPT.md
4. diagram-maker Skill/合同初审 Skill：把合同风险点标出来.md → wiki/sources/合同初审-Skill-把合同风险点标出来.md
**Time:** 2026-05-27 00:00
**New Sources:** 4 | **Entities touched:** prompt-master (+new), any2html (+new), info-card-designer (+new), CloudStudio (+new), contract-review-skill (+new); WorkBuddy (updated); guizang-ppt-skill (updated)
**Concepts touched:** Prompt工程, Skill工程, 推理模型, HTML-PPT, AI办公, 自动化部署, 合同审查, 风险管控

### Results

- **Sources processed:** 4
- **Categories:** AI工具 (1), WorkBuddy (2), diagram-maker Skill (1)
- **Source pages created:** 4
- **Entities created:** prompt-master, any2html, info-card-designer, CloudStudio, contract-review-skill
- **Entities updated:** WorkBuddy (add any2html/info-card-designer/contract-review-skill), guizang-ppt-skill (add CloudStudio/WorkBuddy sources)
- **index.md:** Added 4 new source entries under AI工具/WorkBuddy sections, Sources: 1116→1120, Entities: 190→195

## 2026-05-27 12:00 — 微信同步：2篇文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. WorkBuddy/WorkBuddy实战：3个自动化工作流，彻底改变办公方式.md → wiki/sources/WorkBuddy实战-3个自动化工作流-彻底改变办公方式.md
2. WorkBuddy/WorkBuddy方法20 _ 数据透视表自动生成：一句话搞定多维度汇总.md → wiki/sources/WorkBuddy方法20-数据透视表自动生成.md
**Time:** 2026-05-27 12:00
**New Sources:** 2 | **Entities touched:** Wayen (+new); WorkBuddy (updated)
**Concepts touched:** 工作流自动化, 多模态生成, 团队协作, 知识管理, 数据分析, Prompt工程

### Results

- **Sources processed:** 2
- **Categories:** WorkBuddy (2)
- **Source pages created:** 2
- **Entities created:** Wayen (AI职场提效专家)
- **Entities updated:** WorkBuddy (mentions: 1→3, 新增工作流自动化/多模态生成/数据分析能力)
- **Concepts used:** 工作流自动化, 多模态生成, 团队协作, 知识管理, 数据分析
- **index.md:** Added 2 new source entries under WorkBuddy section, Sources: 1122→1124, Entities: 199→200

## 2026-05-27 06:00 — 微信同步：2篇文章摄入

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. WorkBuddy/零基础老师手把手教程（一）：用 WorkBuddy + IMA，让 AI 真正帮你备课、出题、写材料.md → wiki/sources/零基础老师手把手教程-用-WorkBuddy-IMA-让-AI-帮你备课出题写材料.md
2. Impeccable/一天一个SKILL——还在用蓝湖/磨刀？不如用用这个前端UI设计大师级SKILL——Impeccable.md → wiki/sources/一天一个SKILL-前端UI设计大师级SKILL-Impeccable.md
**Time:** 2026-05-27 06:00
**New Sources:** 2 | **Entities touched:** WorkBuddy (+new), IMA (+new), Impeccable (+new), Paul Bakaus (+new)
**Concepts touched:** AI备课 (+new), AI前端生成 (+new), 设计系统 (+new)

### Results

- **Sources processed:** 2
- **Categories:** WorkBuddy (1), Impeccable (1)
- **Source pages created:** 2
- **Entities created:** WorkBuddy, IMA, Impeccable, Paul Bakaus
- **Concepts created:** AI备课, AI前端生成, 设计系统
- **index.md:** Added 2 new source entries under WorkBuddy and new Impeccable sections, Sources: 1120→1122, Entities: 195→199, Concepts: 186→189

## 2026-05-28 — 45个Hermes Agent案例 & synthesize-research Skill 摄入 (870-871)

**Operator:** Hermes Agent (scheduled cron)
**Source:** 微信公众号/OpenClaw/45个Hermes Agent _ OpenClaw自动化案例（上）.md; 微信公众号/SkillManager/`synthesize-research` Skill 全文中文版.md
**Time:** 2026-05-28 12:01
**New Sources:** 2
**New Entities:** (none — entities already exist)
**New Concepts:** [[工作流自动化]], [[定性研究]], [[定量研究]], [[用户分群]]
**Entities updated:** [[Hermes-Agent]], [[OpenClaw]], [[Skill]], [[定时任务]]
**index.md updated:** Statistics (Sources 1129→1130, Concepts 197→199), Hermes Agent section (+1 entry), OpenClaw section (+1 entry)

### Key Findings

**Article 870 - 45个Hermes Agent / OpenClaw自动化案例（上）:**

1. **核心定位**：Hermes/OpenClaw 的核心优势是"让 Agent 在机器上持续运行，自动完成任务"
2. **45个场景覆盖**：内容创作(01-10)、邮件沟通(11-20)、信息研究(21-30)、日程任务(31-40)、文件数据(41-45)
3. **自然语言驱动**：cron 设置、内容日历、跟进提醒均通过自然语言描述即可实现
4. **Skill 复用机制**：工作流通过 Skill 保存，一次配置多次触发
5. **工具链整合**：Tavily API + 飞书 Bot + MEMORY.md + Skills Hub 形成完整自动化生态

**Article 871 - synthesize-research Skill 全文中文版:**

1. **方法论完整**：Thematic Analysis（六步）、Affinity Mapping（五步）、Triangulation（三角验证）
2. **定性→定量闭环**：访谈产生假设 → 问卷验证规模 → 再次定性深挖
3. **5-8条强发现**：克制综合冲动，高频×高影响优先排序
4. **矛盾即信号**：不同来源讲不同故事时，差异揭示用户分群
5. **可执行建议**：「在设置流程中加入进度指示器」而非「改进 onboarding」

### Entities Created

(none — all entities already existed in wiki)

### Concepts Created

| 概念 | 来源文章 | 说明 |
|------|---------|------|
| [[工作流自动化]] | 870 | 45个场景的核心概念 |
| [[定性研究]] | 871 | 用户研究方法论基础 |
| [[定量研究]] | 871 | 与定性互补的验证方法 |
| [[用户分群]] | 871 | 基于行为的用户分类 |

### Source Pages Created

- `wiki/sources/45个Hermes-Agent-OpenClaw自动化案例（上）.md`
- `wiki/sources/synthesize-research-Skill全文中文版.md`

## 2026-05-28 — 微信公众号同步摄入 6 篇新文章

**Operator:** Hermes Agent (scheduled cron)
**Time:** 2026-05-28 18:00
**New Sources:** 5
**New Entities:** [[LM-Studio]], [[宝塔面板]], [[LongCat-Video-Avatar]], [[美团LongCat团队]]
**New Concepts:** [[AI操作系统]], [[Skill系统]], [[知识编译]], [[唇同步]], [[数字人]], [[多项目隔离]], [[离线AI工作流]], [[开源视频Avatar]]
**index.md updated:** +4 Sources (HeyGen数字人、Obsidian离线AI、Karpathy知识编译、Claude Code Harness), +4 Entities, +8 Concepts

### Key Findings

**Article A — Obsidian + LM Studio 离线AI工作流:**
- 技术栈：Obsidian + LM Studio + 本地LLM插件(Copilot/Text Generator/Smart Connections)
- 核心优势：隐私保护、断网可用、成本可控（无API按token计费）
- 支持模型：Qwen2.5-7B/Llama-3.1-8B日常对话，CodeQwen/DeepSeek-Coder代码辅助，Phi-3-mini轻量场景
- 本地API端口 localhost:1234 与 Obsidian 插件通信

**Article B — AI网站上线指南:**
- 问题根源：localhost 只能本机访问，无法公网访问
- 解决方案：域名 + 服务器 + 宝塔面板 + DNS + HTTPS
- 涉及技术：Nginx/Caddy反向代理、SSL证书、域名解析

**Article C — Karpathy LLM Wiki 知识编译:**
- 规模：100篇文章40万词个人知识库
- 五层架构：输入层(raw/)→编译层(Wiki生成)→存储层(.md)→查询层(Q/A)→输出层(多格式)
- 核心理念：LLM编译而非手动编辑、知识是活数据不是死文档

**Article D — LongCat-Video-Avatar 开源数字人:**
- 美团LongCat团队开源方案，MIT许可
- 核心升级：Whisper-Large音频编码(DMD2 8步蒸馏+INT8量化)
- 支持：中文英语日语、身份一致性不漂移、批量内容生产

**Article E — Claude Code + Harness 搭建AI公司:**
- Claude Code = AI操作系统，不是聊天框
- Skill = 员工技能手册（三层：知识层+流程层+工具调用层）
- MCP = 外部工具连接器
- Harness = 项目经理（决定谁干什么）
- 核心价值：Skill会积累，越用越懂用户

### Entities Created

| 实体 | 说明 |
|---|---|
| LM-Studio | 本地大模型运行平台，支持GGUF格式 |
| 宝塔面板 | Linux服务器Web管理面板 |
| LongCat-Video-Avatar | 美团开源数字人Avatar方案 |
| 美团LongCat团队 | LongCat-Video-Avatar开发团队 |

### Concepts Created

| 概念 | 说明 |
|---|---|
| AI操作系统 | Claude Code作为AI员工运行的操作系统 |
| Skill系统 | AI员工技能手册三层模型 |
| 知识编译 | Karpathy的LLM Wiki核心理念 |
| 唇同步 | 数字人视频关键技术 |
| 数字人 | AI视频Avatar，开源替代HeyGen |
| 多项目隔离 | Claude Code不同项目上下文不污染 |
| 离线AI工作流 | Obsidian + LM Studio本地AI系统 |
| 开源视频Avatar | LongCat等开源唇同步视频方案 |

---

## 2026-05-29 — Superpowers + WeChat Radar 文章摄入 (D & E)

**Operator:** Hermes Agent (scheduled cron)
**Sources:**
1. 微信公众号/GitHub/GitHub上159K颗星！你的AI编程代理不是能力不够，是不知道怎么干活.md → wiki/sources/GitHub-159K-Superpowers-AI编程方法论.md
2. 微信公众号/Wechatsync/微信群聊看板wechat radar 再也不用翻微信群聊记录了.md → wiki/sources/WeChat-Radar-群聊情报看板.md
**Time:** 2026-05-29
**New Sources:** 2
**New Entities:** [[Superpowers]], [[WeChat-Radar]]
**New Concepts:** [[AI编程方法论]], [[群聊情报聚合]]
**index.md updated:** Statistics (Sources 1144→1146, Entities 217→219, Concepts 216→218), GitHub (28→29), Wechatsync (新建)

### Key Findings

**Article D - GitHub 159K Superpowers:**

1. **核心命题**：AI编程代理真正缺的不是能力，而是"怎么干活的方法论"
2. **14个技能**：覆盖软件开发全流程——头脑风暴、写计划、子Agent开发、TDD、代码审查、系统化调试、完工验证等
3. **核心差异**：装了和没装的区别——一个上来就干，一个想清楚了再干
4. **支持工具**：原版支持 Claude Code/Codex/Gemini CLI/OpenCode/Cursor；中文增强版 superpowers-zh 支持 Hermes Agent/OpenClaw
5. **安装方式**：`/plugin install superpowers@claude-plugins-official` 或 `npx superpowers-zh`
6. **核心观点**：AI + 好方法论可以替代没有方法论的程序员；不是让AI更聪明，而是让它知道怎么干活

**Article E - WeChat Radar:**

1. **核心命题**：解决"群太多、真正有用的消息被淹没"问题
2. **四大能力**：
   - 话题雷达：跨群聚合同一天热门话题
   - 链接情报：去重整理文章/GitHub/工具链接
   - 群日报：一键摘要，可丢给AI二次处理
   - 本地存储：SQLite，不上传云端
3. **界面特点**：情报驾驶舱，活跃群数/总消息数/链接/@我/高信号人物一屏全收
4. **项目状态**：2025年5月24号开源，连续更新多版
5. **使用方式**：编辑 config.yaml，浏览器打开 localhost:7860

### Entities Created

| 实体 | 说明 |
|---|---|
| Superpowers | GitHub 159K星，AI编程代理技能系统，14个方法论技能 |
| WeChat-Radar | 群聊情报看板工具，话题雷达/链接情报/群日报/本地存储 |

### Concepts Created

| 概念 | 说明 |
|---|---|
| AI编程方法论 | 让AI编程代理知道怎么干活的系统性工作流程和规范 |
| 群聊情报聚合 | 从多个群聊中自动提取、去重、整理有价值信息的技术和方法 |

### index.md Updates

- Statistics: Sources 1144→1146, Entities 217→219, Concepts 216→218
- GitHub: 28→29篇（新增 Superpowers）
- Wechatsync: 新建分类（1篇）

---

