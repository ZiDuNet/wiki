> 📎 来源: [如此才是](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247485394&idx=1&sn=7013eaf07ffbd27d085edd588620913a&chksm=f574376dbe0f897390c7575c631f6e7ad390b5f00335e2d6a0e3c6163af9fae9c28bed58a28c&mpshare=1&scene=1&srcid=0516S2DAoOgTM575sWtpwRHp&sharer_shareinfo=0f7168cac795372bd91a5332b1bdd5df&sharer_shareinfo_first=0f7168cac795372bd91a5332b1bdd5df) | 时间: 2026-05-16 17:28

---

还在为PPT排版、改版、配色、动画耗费大半天时间而头疼吗？市面上的AI PPT工具大多输出固定PPTX，微调难、隐私忧、云依赖强。#GitHub开源项目#——**arcsin1/oh-my-ppt**，一款**纯本地优先的AI幻灯片生成与编辑桌面应用**。一句话生成完整HTML幻灯片，支持拖拽可视化编辑、对话式精准修改、整元素Anime.js动画、KaTeX公式渲染、图片/视频插入、版本历史回退、多格式导出，全部跑在你电脑上，无需注册、无数据泄露、无云锁-in。这个项目是**真正的AI驱动的演示工作台**（Presentation Workbench）。

### 一、项目核心价值

传统AI PPT痛点：

●输出死板PPTX，样式/动画难改；

●云服务数据泄露风险高；

●无法精细可视化编辑或对话修改单页元素。

**Oh My PPT** 彻底解决：生成的是**纯HTML幻灯片**（16:9固定画布），浏览器即开即用、可直接嵌入网页分享，还能无限自定义CSS/JS。核心理念是**Local-first + AI Agent驱动**，结合Electron桌面端体验，让你从“提示词生成”到“专业路演级演示”一气呵成。内置30+风格Skill（极简白、赛博霓虹、包豪斯、日式简约、小红书风等），支持自定义风格提取。

最新v2.0.6（2026-05-14）已支持元素复制/偏移、图片视频插入、撤销重做、元素删除、演示模式等，编辑体验飞跃。

![](assets/img_a2c74e1f7b88.jpg)

### 二、全部功能点

1.**一句话/文档驱动生成**：输入主题+需求，AI自动规划大纲、配色、排版，逐页渲染完整Deck。支持上传txt/md/csv/docx，自动提取主题、页数、详细描述，并**在生成时持续参考原文档内容**（文档仅本地保存）。生成时按固定16:9画布+内容高度预算组织页面，极大减少溢出。

2.**PPTX导入编辑**：上传本地PPTX，转为应用内可编辑HTML页面，同时自动提取原风格（配色、字体、布局）保存为可复用Skill。新页面自动继承风格。独立于AI生成链路。

3.**图片识别生成风格与大纲**：上传设计稿/截图（支持多模态模型），AI自动识别视觉特征，生成独特风格Skill + 演示大纲，一键回填创建表单。

4.**内置30+风格Skill + 自定义**：极简白、赛博霓虹、包豪斯等。风格编辑页支持导入图片提取视觉规则（配色/字体/版式/组件）。生成或编辑时可指定或切换。

![](assets/img_be48bc9a61a0.png)

5.**对话式+可视化编辑**（核心杀手级功能）：

○**聊天修改**：选中页面，说“标题换颜色”“加数据图表”“调整段落顺序”，AI精准修改单页或全Deck。

○**可视化拖拽**：所有元素（文字、图片、视频、图表、卡片）均可拖拽、缩放、选中。支持@ dnd-kit实现精确排序与拖拽。

○**元素操作**：一键复制（自动偏移独立可编辑）、删除（支持快捷键）、撤销/重做、文字双击实时编辑样式/内容。

○**插入素材**：编辑模式下直接上传图片/视频（mp4/webm/ogg），存入本地资源目录，可从素材库引用插入指定位置。

6.**演示模式**：一键全屏播放，键盘左右键/点击切换，支持页面切换动画。

7.**动画支持**：集成**Anime.js v4**本地运行时。AI可在生成/编辑时为**整元素**添加基础演示动画（淡入、轻微位移入场、缩放强调、简单错峰），避免碎片化逐字动画，更稳更专业。页面切换也支持过渡动画。

8.**数学公式渲染**：内置KaTeX，支持常见LaTeX公式，完美适配教学/技术分享。

9.**会话管理 + 版本历史**：区分AI生成 vs PPTX导入会话。可重命名。每次生成/编辑自动记录历史版本（含操作日志），支持任意回退，改错不怕。

10.**多格式导出**：PDF、批量PNG、可编辑PPTX（基于pptxgenjs持续优化）。HTML源文件可直接分享。

11.**其他务实细节**：生成取消、进度阶段指示（准备→规划→生成→校验）、多模型切换（设置中管理默认模型）、错误智能重试、会话耗时统计、左侧边栏可折叠等。

### 三、使用方法

**典型工作流**（首页操作）：

1.打开App → 首页填写主题+详细描述（或上传文档/图片/PPTX）。

2.AI规划大纲 → 生成视觉风格 → 逐页渲染HTML。

3.进入会话详情：预览模式浏览、进入编辑模式拖拽/聊天修改。

4.演示模式全屏路演，或导出PDF/PNG/PPTX。

实际使用中，生成稳定性高（LangGraph agent + 校验重试），14B+本地模型或强云模型效果最佳。HTML输出干净、可直接浏览器打开或嵌入网站。

![](assets/img_cfb4472d1d29.jpg)

### 四、安装方法

**推荐方式（最简单）**：

1.前往 GitHub Releases 下载最新安装包（Windows/macOS/Linux支持）。

2.Windows/macOS直接安装，macOS若提示“已损坏”见下方unsigned-app解决。

3.首次打开→设置页填写AI配置（见下）→开始使用。

\*\*从源码安装：

1.克隆仓库：

```
git clone https://github.com/arcsin1/oh-my-ppt.git && cd oh-my-ppt
```

2.安装依赖：

```
pnpm install
```

（推荐pnpm）

3.数据库迁移：

```
pnpm db:migrate
```

4.开发运行：

```
pnpm dev
```

（Electron + Vite热重载）

5.构建安装包：

○Windows：

```
pnpm build:win
```

○macOS：

```
pnpm build:mac
```

○Linux：

```
pnpm build:linux
```

6.生成图标（可选）：

```
pnpm electron:generate-icons
```

构建后out/目录即完整可分发应用。electron-builder.yml 配置了自动更新（dev-app-update.yml）。

### 五、配置必填（支持本地Ollama）

设置页填写：

●Provider: 

```
openai
```

（Ollama兼容）

●Base URL: 

```
http://127.0.0.1:11434/v1
```

●Model: 如 

```
qwen2.5:14b
```

（推荐14B+）

●API Key: 任意非空字符串（如

```
ollama
```

）

云模型同理（OpenAI/Anthropic）。应用强制非空key检查，支持多模型列表切换。

**unsigned-app问题（mac）**：右键→显示包内容→Contents/MacOS/oh-my-ppt → Terminal执行 

```
sudo xattr -cr /path/to/app
```

 或使用

```
spctl --master-disable
```

临时放行。

### 六、技术原理、架构

**整体架构**（Electron + Vite）：

●**Main Process** (

```
src/main/
```

): Electron核心，负责窗口创建、IPC通信、文件系统 guarded 操作、数据库、Agent管理。

●**Preload** (

```
src/preload/
```

): 安全上下文桥接。

●**Renderer** (

```
src/renderer/
```

): React 19 + TypeScript + Tailwind CSS + Radix UI + Zustand状态管理 + dnd-kit拖拽。使用React Router管理路由（首页/会话/编辑）。

●**Shared** (

```
src/shared/
```

): 类型定义、常量。

●**构建**：electron-vite.config.ts 配置别名（@shared、@renderer），Renderer集成React插件，主进程外部化electron依赖。

**AI Agent核心实现**（LangGraph + deepagents）：

●使用

```
deepagents
```

库 + LangChain（@langchain/langgraph、openai、anthropic）构建**状态化、可取消、并发Agent**。

●

```
AgentManager
```

 类（Map管理session）：每个会话独立Main Agent + Per-Page Agents，支持并行生成页面。

●**Deck Agent**：全Deck生成；**Edit Agent**：受限工具集，用于聊天修改。

●**GuardedFilesystemBackend**：虚拟模式+安全拦截，禁止生成期危险

```
edit_file
```

操作。

●**Tools**：session-bound工具集，实现文档解析、风格提取、页面渲染、元素修改等。

●**Prompt工程**：动态构建system prompt（buildDeckAgentSystemPrompt等），支持retry模式（不持久化user message，中英双语）。

●**模型解析**：

```
resolveModel
```

动态创建ChatOpenAI/ChatAnthropic，支持temperature控制、Ollama兼容（禁用thinking mode避免reasoning\_content问题）。

●**并发与安全**：AbortController取消、beginRun/finalizeGenerationFailure状态保护。

**数据持久化**：

●Drizzle-ORM + LibSQL（SQLite本地DB）：drizzle.config.ts管理schema。

●会话、页面元数据、历史版本、风格Skill、资源路径全部本地存储。

●pageNumber一致性通过

```
derivePageNumber
```

函数严格保障（metadata解析）。

**PPT渲染与扩展**：

●生成HTML页面（内嵌Tailwind类 + Anime.js v4运行时 + KaTeX）。

●导入：pptxtojson + mammoth（docx）解析。

●导出：pdf-lib（PDF）、pptxgenjs（PPTX）、批量PNG。

●动画：整元素Anime.js API调用（fadeIn、slideIn、scale等），避免高频闪烁。

●素材：本地资源目录管理（图片/视频路径持久化）。

**代码约束与工程化**（Agent.md/CLAUDE.md）：

●严格类型安全（禁止

```
as any
```

）、Prettier单引号无分号、路径别名。

●运行态保护：startingSessionIds等关键状态不可删除。

●DB操作、IPC flows（src/main/ipc/generation/）模块化：resolveContext + executeGeneration。

**性能优化**（CHANGELOG体现）：生成速度提升20-40%、自动重试、进度日志精简、编辑稳定性增强。

![](assets/img_ee1d11d78037.jpg)

Oh-My-PPT 做到了**“提示词输入 → 专业Deck输出 → 无限迭代”**的闭环，是创业路演、产品汇报、课堂教学的效率神器。更重要的是，它\*100%本地、开源MIT、持续迭代\*\*。

**—— 如此才是**

**把复杂的技术，讲成你真正能用上的生产力**

**[零基础也能玩转卫星！开源Ground Station + SDR 打造个人地面站全攻略](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484408&idx=1&sn=fa96368ff3647cd53bad3ee9391103ee&scene=21#wechat_redirect)**

**[OpenClaw & Hermes刷屏后，GitHub  Mercury Agent如何打动用户？ 灵魂驱动+权限铁闸+24/7永动 vs 两大竞品](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484903&idx=1&sn=8ea193b342d5f61ed5ed30de9ebb32b9&scene=21#wechat_redirect)**

**[苹果M系列芯片的福音！无需H100、无需云GPU，本地MacBook就能微调Gemma 4多模态模型](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484529&idx=1&sn=63e2f7f4ac65540fd05ef9d05f0d28a8&scene=21#wechat_redirect)**

**[开源Minecraft终极杀手！12.7K星GitHub神器Luanti（原Minetest）完整中文攻略：零基础安装、2800+模组随便玩、服务器+源码编译](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484515&idx=1&sn=f7cac21fab871c06cee81d780a1e37af&scene=21#wechat_redirect)**

**[AI 直接操控 Unity/Godot/Unreal 编辑器！用 OpenClaw + TomLeeLive 插件，聊天就能把你的游戏梦想变成现实](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484263&idx=1&sn=49474c84d4c0c6a1dd7925d821680aca&scene=21#wechat_redirect)**

[开源项目Paseo，AI编码代理跨设备统一指挥中心：统管Claude Code、Codex、OpenCode（以及Copilot、Pi等）](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484927&idx=1&sn=b4d7d4aed5a5ad7263bff54b50c395a5&scene=21#wechat_redirect)

[老婆/女朋友每天早上纠结45分钟穿什么？GitHub 开源AI衣柜神器 Wardrowbe 彻底解放！完整自托管安装+使用教程](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484594&idx=1&sn=2a9832be4fd2b3d423f9c62fbae5b0a3&scene=21#wechat_redirect)

[Notebook LM平替，开源Open Notebook：隐私零泄露、18+AI模型随意切、1-4人定制播客秒生成](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247484913&idx=1&sn=a3307c1fb6b981881b22ca1c1ca407e2&scene=21#wechat_redirect)

[30MB Rust无头浏览器Obscura：击败Chrome、V8真实JS+CDP全兼容，AI Agent与爬虫的隐形核武器](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247485078&idx=1&sn=84152e9774e0eab3d16839db3a7657de&scene=21#wechat_redirect)

[Rust重写的jcode：性能碾压Cursor Claude Code 139倍的下一代Coding Agent Harness，人类级内存图谱+多会话Swarm](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247485066&idx=1&sn=2a563ec1e199af1807b6541f91d0842b&scene=21#wechat_redirect)

[Warp开源震撼发布！5年Rust GPU终端+Oz Agentic开发环境完整拆解：功能全览、源码编译教程、核心架构深度解析](https://mp.weixin.qq.com/s?__biz=MzY5MTAxODQ1MQ==&mid=2247485052&idx=1&sn=f612497afd348acd327221233af635c2&scene=21#wechat_redirect)
