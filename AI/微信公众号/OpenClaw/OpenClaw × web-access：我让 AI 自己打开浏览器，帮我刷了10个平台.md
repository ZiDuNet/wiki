> 📎 来源: [小龙开发者](https://mp.weixin.qq.com/s?__biz=MzY4OTE4MDg2Nw==&mid=2247483968&idx=1&sn=90902eca165cb90143fc0a69cf834ec4&chksm=f2f335a86925af506eac37b4e214a24a69332154e5c96958311a3548b33a42dd0735319e9866&mpshare=1&scene=1&srcid=04238yDoLetlUfhPJ3Mse6f1&sharer_shareinfo=76ff19705455661560d6630d3ea6f8df&sharer_shareinfo_first=76ff19705455661560d6630d3ea6f8df) | 时间: 2026-04-23 23:59

---

OpenClaw 是 AI 的「大脑和双手」，web-access 是它的「眼睛」——两者结合，你的 Agent 终于能像人一样浏览网页了

🔗 OpenClaw + web-access

先说结论：

"

****OpenClaw + web-access = 目前开源界最完整的 Agent 联网方案。****
**前者提供 35 万 Star 级的 AI 执行框架，后者补齐了联网能力的最后一块短板。**

这个组合解决的核心问题很简单——**AI 能干活，但它的"眼睛"不好使。**

**AI 的"眼睛"有什么毛病？**

如果你用过 OpenClaw，或者任何 AI Agent 工具（Claude Code、Codex、Cursor），你一定遇到过这种场景：

**😵 场景一：遇到需要登录的网站**

你想让 Agent 帮你看看微信公众号的某篇文章，或者去小红书搜一下用户讨论。结果 Agent 直接歇菜——它没有登录态，打开页面要么是空壳，要么被反爬机制挡在门外。

**😵 场景二：动态渲染的页面**

GitHub 的提交记录页、B 站的视频列表、各种 SPA 单页应用……Agent 用 HTTP 请求去抓，拿到的只有一堆 JS 混淆代码或空白的 ``。

**😵 场景三：多平台并发调研**

你想同时调研 Dify、Coze、FastGPT 三个竞品。Agent 只能一个一个串行地去查，查完第一个再去第二个，效率极低。而且每个平台的文档结构不同，Agent 还要反复试错。

这就是当前 AI Agent 联网的**三座大山**：登录墙、动态渲染、低效串行。

而问题的根源在于——***大多数 Agent 的"联网"，其实只是"搜索+抓取"，不是真正意义上的"浏览"。***

**认识今天的两个主角**

**OpenClaw**

🦞 AI 执行框架 · 354K Stars

**web-access**

🌐 联网增强 Skill · 4.8K Stars

**主角一：OpenClaw —— AI 的"大脑和双手"**

奥地利开发者 Peter Steinberger 在"退休实验"中创建的开源项目，4个月冲到 GitHub **354K+ Stars**。核心理念是***"让 AI 拥有双手"***——通过 WhatsApp、Telegram、飞书等 **20+** 平台跟你对话的同时，它能操作你的文件系统、执行命令、管理日历、调用模型……

但它有一个短板：**内置的联网能力偏弱。**

🔍

**OpenClaw 内置的 Web Tools：**提供 

```
web_search
```

（搜索）和 

```
web_fetch
```

（抓取网页转 Markdown）。支持 Brave、Perplexity、Gemini、Grok、Kimi 五种搜索源。但本质上还是 HTTP 层面的操作——不执行 JavaScript、不带登录态、不能交互点击。

**主角二：web-access —— AI 的"眼睛"**

由开发者一泽EZE (eze-is) 创建的开源 Skill，一周内冲到 **4.8K+ Stars**。它不是 MCP，而是 Skill——不仅给工具，还给"怎么用工具"的完整方法论。

核心能力就一件事：**让 Agent 从"搜索网页"升级为"像真人一样浏览网页"。**

"

**MCP 是给你一把螺丝刀，Skill 是给你一把螺丝刀外加一份说明书——**
**告诉你这颗螺丝从哪个方向拧、用多大力、拧不动的时候换什么姿势。**

**它们在一起是怎么工作的？**

先看一张全景图：

**👤 你**

↓ 通过微信 / Telegram / WhatsApp 发送指令 ↓

**🦞 OpenClaw**
**Gateway + Agent + 记忆**

↓ 匹配到联网任务，调用 web-access Skill ↓

**🌐 web-access**
**五层通道调度 + CDP Proxy**

→

**🔴 Chrome 浏览器**
**你日常使用的浏览器实例**

↑ 登录态天然携带，看到的内容和你自己打开一样 ↑

**🦞 OpenClaw**
**整合结果 → 回复给你**

关键点来了——**web-access 接管的是你自己正在用的 Chrome，不是另开一个无头浏览器。**

这意味着什么？你在 Chrome 里登录过的所有网站——小红书、微信公众号、公司内网、GitHub——***Agent 直接就能用***，不需要再走一遍登录流程。这是和其他方案最大的区别。

**web-access 的五层联网能力**

当 OpenClaw 遇到一个联网任务时，web-access 不是上来就开浏览器，而是按优先级从轻到重逐层尝试：

**① Layer 1：WebSearch — 关键词搜索**

最轻量的方式。调用搜索引擎 API，拿摘要和链接。
适用：简单事实查询、"XXX是什么"
⚡ 最快、最省 Token

**② Layer 2：WebFetch — HTTP 直接抓取**

对目标 URL 发起 GET 请求，提取正文转为 Markdown。
适用：静态博客、新闻文章、技术文档
⚡ 不执行 JS，但够用就不上重武器

**③ Layer 3：curl — 原始 HTML 获取**

直接 curl 目标 URL，拿到原始 HTML 源码。
适用：API 返回、简单页面、需要自定义 Header
⚡ WebFetch 失败时的降级方案

**④ Layer 4：Jina Reader — 第三方渲染服务**

通过 jina.ai 把目标页面渲染后返回干净 Markdown。
适用：JS 渲染但无需登录的中等复杂页面
⚡ 免费额度有限，适合过渡使用

**⑤ Layer 5：CDP 浏览器直连 ⭐ 核心杀手锏**

通过 Chrome DevTools Protocol 直连你的真实浏览器。
适用：**动态渲染页面 / 需要登录态 / 反爬网站 / 交互操作**
🔥 支持点击、输入、滚动、截图、多 Tab 并行

💡

**渐进式升级策略：**这不是"五种工具随便选"，而是严格的优先级队列——能用 Layer 1 解决的绝不用 Layer 5。只有在前面四层都搞不定的时候（比如遇到小红书这种动态渲染+登录墙+反爬三位一体的站点），才启动 CDP 浏览器直连。既省 Token 又省时间。

**装了 web-access 之后，OpenClaw 变强了多少？**

直接看对比表，差距一目了然：

| **对比维度** | **OpenClaw 原生联网** | **+ web-access 增强** |
| --- | --- | --- |
| **工具策略** | Search / Fetch 二选一，降级逻辑简单 | **五层渐进式调度 ✅** 自动选择最优路径 |
| **登录态处理** | **需单独维护 CDP Profile ❌** 每站独立配置 | **直连用户Chrome ✅** 天然携带全部登录态 |
| **动态渲染** | **不支持 JS 执行 ❌** SPA/SSR 页面抓空 | **真实浏览器渲染 ✅** 所见即所得 |
| **并发能力** | **并行支持弱 ❌** 可能抢占焦点 | **多Tab后台并行 ✅** 子Agent互不干扰 |
| **经验沉淀** | **跨会话经验差 ❌** 每次从头摸索 | **按域名自动沉淀 ✅** 越用越顺（效率+90%） |
| **交互操作** | **只读模式 ❌** 无法点击/填表/滚动 | **完整DOM交互 ✅** 点击/输入/上传/截图 |
| **反爬对抗** | **易被封禁 ❌** | **真实浏览器指纹 ✅** 识别率极低 |

用一句话总结：**OpenClaw 原生联网是"拿着望远镜看世界"，装了 web-access 之后变成了"亲自走进现场考察"。**

**实际效果有多猛？四个真实案例**

**案例一 · 三平台竞品调研 → 并行 3 倍提速**

**任务："调研 Dify、Coze、FastGPT，整理成对比表"**

Agent 自动拆分为 3 个子 Agent 并行，各自开浏览器标签翻官方文档、提取节点类型和定价信息。主 Agent 收到结果后整合输出完整对比表。**耗时 = 单个平台调研时间，效率提升约 3 倍。**作者据此给项目加了条件分支节点和 HTTP 请求节点两个 TODO。

**案例二 · 小红书用户讨论 → 从搜索到浏览**

**任务："去小红书搜索'沉默王二'，整理前10条帖子观点"**

Agent 判定小红书需要 CDP 模式，接管已登录的 Chrome 标签页 → 输入关键词 → 等渲染 → 提取列表 → 点进详情抓评论。**因为复用了自己的登录态，搜索结果跟手动搜完全一致。**从"搜索"到"浏览"的能力跃迁。

**案例三 · GitHub 技术周报 → 渐进式工具升级**

**任务："根据 PaiAgent 最近 commit 生成技术周报"**

Agent 先用 WebFetch 拉 GitHub 页面 → 发现部分内容需 JS 渲染 → 自动升级到 CDP 模式 → 用真实浏览器打开并提取。**体现了"先用轻量方式，不行再上重武器"的核心设计原则。**

**案例四 · 10 平台并发监控 → 百级 Tab 同时跑**

**任务："同时监控小红书、微博、B站、Boss直聘、虎嗅等 10 个平台"**

作者实测：**10 个子 Agent 同时操作 10 个不同平台，各开 10 个 Tab（共 100 个网页），并行执行站内搜索、内容抓取、趋势分析。**共享同一 Chrome 实例，无界面抢占，无人工干预登录/跳转/反爬。**耗时比单 Agent 串行减少约 90%。**

**技术底座：为什么是 CDP？**

整个 web-access 的核心底座是 **CDP（Chrome DevTools Protocol）**——Chrome 远程调试协议。就是你按 F12 打开开发者工具时，底层在用的那套协议。

通过 CDP，外部程序可以控制浏览器做这些事：

- **导航控制**：打开 URL、前进后退、刷新
- **脚本执行**：在页面里运行任意 JavaScript
- **DOM 操作**：读取内容、修改样式、触发事件
- **模拟输入**：键盘打字、鼠标点击、页面滚动
- **网络监听**：捕获所有 HTTP 请求和响应
- **生成截图**：任意时刻截取当前视口

但 CDP 原始协议是 WebSocket，调用门槛高。所以 web-access 加了一层 **CDP Proxy**——把 WebSocket 包装成简单的 HTTP API：

CDP Proxy — 常用接口一览

```
# 列出当前所有浏览器标签页curl http://localhost:3456/targets
```

```
# 在指定标签页执行 curl"http://localhost:3456/eval?target=xxx"-d'document.title'
```

```
# 点击页面某个元素curl"http://localhost:3456/click?target=xxx"-d'button.submit'
```

```
# 截图保存当前视口curl"http://localhost:3456/screenshot?target=xxx"
```

```
# 向指定元素输入文字curl"http://localhost:3456/type?target=xxx"-d'hello world'
```

🔑

**三种方案对比：**Puppeteer 和 Chrome DevTools MCP 都能操控浏览器，但都需要启动独立的浏览器实例，**没有你的登录态**。CDP Proxy 方案唯一能做到的是——接入你日常用的 Chrome，天然携带所有已登录状态。

**web-access 对 OpenClaw 的三大增强**

**杀手锏一 · 登录态天然携带**

**不用再为每个站点单独配置认证**

CDP Proxy 接入的是你日常用的 Chrome。你在浏览器里登录过的小红书、微信公众号、飞书、公司内网……Agent 直接继承全部登录状态。**这是其他方案（MCP chrome-devtools、Puppeteer）做不到的。**对于需要授权墙的场景，这是不可替代的优势。

**杀手锏二 · Sub-Agent 并行分治**

**10 个子 Agent 同时跑，互不干扰**

遇到多个目标调研任务，主 Agent 自动拆分子任务，分发给多个子 Agent 并行执行。每个子 Agent 操作自己的浏览器标签页（Tab 隔离），结果汇总给主 Agent 整合输出。**实际测试：10 平台并发监控耗时减少约 90%。**OpenClaw 本身的 Lane 队列机制 + web-access 的并行分治，形成完美互补。

**杀手锏三 · 站点经验自动沉淀**

**越用越聪明，同站点二次访问效率 +90%**

web-access 维护了一个 

```
references/site-patterns/
```

 目录，按域名存储每次成功操作的路径经验——小红书的搜索框 CSS 选择器在哪、B站的分页是懒加载还是按钮翻页、公众号内容的渲染特点是什么。**首次访问新站点会探索学习，后续同域名访问直接复用上次的经验路径。**这就是"越用越顺"的技术实现。

作者把这套设计提炼成了一个公式：

"

****Skill = Agent 策略哲学 + 最小完备工具集 + 必要的事实说明****

翻译成人话就是：不只告诉 Agent "有哪些工具可用"，还要教它**"什么时候用什么、怎么用好、踩过哪些坑"**。这正是 OpenClaw Skill 架构的设计哲学——***Skill 不只是工具箱，更是专家的操作手册。***

**怎么装？两步搞定**

前提条件：你已经装好了 OpenClaw（没装的参考文末链接）。

**第一步：安装 web-access Skill**

在 OpenClaw 中直接发送以下指令（通过任意已接入渠道：Telegram / Discord / CLI 等）：

OpenClaw Chat — 安装 web-access

```
帮我安装 web-access skill， 仓库地址是 https://github.com/eze-is/web-access 这个 skill 原为 Claude Code 设计，安装前请先理解其核心原理 和工作逻辑，再结合 OpenClaw 的 Agent 架构与电脑环境进行适配， 使其真正融入当前环境，而非生硬移植。
```

📌

**注意：**GitHub 上已有社区适配版 

```
openclaw/skills/skills/ysyyrps777/web-access-openclaw
```

，可以直接放到 OpenClaw 自定义技能目录中使用。两种方式都可以。

**第二步：开启 Chrome 远程调试**

这一步只需要做一次：

Terminal / Chrome 地址栏

```
# 方法一：地址栏输入（推荐）chrome://inspect/#remote-debugging  # 勾选「允许远程调试」，重启 Chrome
```

装完之后，Skill 会自动做环境检查：Node.js 版本 ≥ 22？CDP 端口通不通？Proxy 进程有没有跑起来？全部绿灯就可以用了。

⚠️

**安全提醒：**CDP 模式下 Agent 可以操控你的真实浏览器。建议：
① 明确告知 Agent 边界（如"不要关闭我原有的标签页"）；
② 只从官方仓库或 awesome-openclaw-skills 安装 Skill；
③ 用 secureclaw 定期扫描已安装 Skill；
④ 不用时可在 Chrome 设置中关闭远程调试。

**也要说说它的局限**

🔋

**Token 消耗增加：**CDP 浏览器模式比普通搜索消耗更多 Token（截图 + DOM 分析 + 多步交互）。建议日常查询走 Layer 1-4，只在必要时启用 Layer 5。Active Memory 的 message 模式（最轻量）可以先评估效果。

💻

**依赖 Chrome 运行：**必须保持 Chrome 开启且远程调试端口可用。如果 Chrome 意外关闭，CDP 功能会失效。另外目前仅支持基于 Chromium 的浏览器（Chrome / Edge / Brave）。

🎯

**首次访问新站点较慢：**因为没有积累过该站点的操作经验，Agent 需要探索式地尝试。好消息是第二次访问同域名站点时，经验沉淀机制会让效率大幅提升（实测 +90%）。

🤝

**与 OpenClaw 内置 Browser 工具的关系：**OpenClaw 自身也有浏览器控制能力（Extension Relay / Managed / Remote CDP 三种模式）。web-access 不替代它，而是在其之上增加了智能调度层、经验沉淀层和并行分治层。**两者是互补关系，不是替代关系。**

✦ ✦ ✦

"

**以前 Agent 联网是"搜索"：输关键词、拿摘要、给答案。**
**现在是"浏览"：打开页面、等渲染、点链接、读细节、整理内容。**
**这两个动词背后的能力差距，大概相当于你让人帮你查资料，****和你让他帮你实地走访一圈的差距。**

**工具的上限，决定了你能做事情的边界。**

OpenClaw 给了 AI "双手"（执行能力），web-access 给了 AI "眼睛"（真实的联网感知能力）。两者结合，才是完整的 Agent。
