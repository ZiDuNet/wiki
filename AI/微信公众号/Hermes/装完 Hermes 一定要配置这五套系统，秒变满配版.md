> 📎 来源: [墨与端](https://mp.weixin.qq.com/s?__biz=MzYyNDI3NTg1Nw==&mid=2247484108&idx=1&sn=16fd1db0239484a339bba930eb654729&chksm=f1c68cb37d98143f5d72cc8072db03e9632aceccb94ffbff64a847bba918defc62fee3ec7a23&mpshare=1&scene=1&srcid=0425XH3iWGIrTIBuYyXsM3h9&sharer_shareinfo=355d97572c32764e1c7f4b948d772acd&sharer_shareinfo_first=355d97572c32764e1c7f4b948d772acd) | 时间: 2026-04-25 18:05

---

作者：AI小2

你有没有这种感觉——装完 Hermes，兴冲冲地问了它一个问题，它回答得怎么说呢，就跟刚入职第一天的新人一样礼貌但空洞？

不怪它。**Hermes 装完只是裸机状态，真正的满配版需要自己折腾。**

今天这篇，就是让你把 Hermes 从"普通对话助手"直接升级成"真・AI Agent"的操作指南。

### 第一件事：给它一个人格，别让它当空白人

Hermes 默认是没有"性格"的，它对谁说话都是一个调调。

怎么破？给它写一个 SOUL.md。

GitHub 上有个项目叫 **agency-agents-zh**，里面藏着 211 个中文角色模板——从小红书写手到抖音运营，从 ToG 政务助手到医疗合规顾问，要什么人格直接调。告诉 Hermes"激活哪个角色"，它就能切换到对应的工作模式。

这个步骤本质上是在做一件事：**给它一个上下文，让它知道自己是来干什么的。** 没装 SOUL.md 的 Hermes，就像一个没有专业背景的实习生——聪明是聪明，但不知道该往哪个方向使劲。

### 第二件事：把记忆系统换掉，别用自带的"金鱼脑"

Hermes 自带一个 MEMORY.md，但说实话——它记东西的方式很像金鱼，只有它觉得重要的时候才写，而且写到两千多字就再也塞不进去了。

换成 **Hindsight** 就不一样了：

- 它从每轮对话里\*\*自动提取\*\*实体、事实、关系、时间戳
- 没有字符上限
- 知识不是堆在那儿的文本，而是\*\*一张网\*\*——问到某个概念，相关的人和事一起浮出来

切换方法一行命令：

```
hermes memory setup
```

然后选

```
hindsight
```

，注册一个 Hindsight 的 API Key（免费额度够用），验证一下：

```
hermes memory status
```

看到"bank\_id"和"auto-recall"就说明激活了。

换完之后最明显的感觉是——你第二天再跟它聊，它真的记得昨天说到哪儿了。

### 第三件事：让它能"读懂"互联网，不只是跟你聊天

裸装 Hermes 能读你粘贴给它的文字，但没法主动去网上抓内容。

补上这四件套：

**Jina Reader**——单页抓取，丢个链接它就能读

**Crawl4AI**——批量深度抓取，适合做研究

**Scrapling**——专门对付反爬虫的

**CamoFox**——隐身浏览器，能绕过一些高级防护

装完这四个，Hermes 就从"只能聊本地内容"进化到"随便在网上冲浪"了。我自己用下来感受最深的是 Crawl4AI，搞某个话题的研究时让它批量抓相关页面，比一个一个复制粘贴快了不止十倍。

### 第四件事：给它搜索能力，而且要有兜底

主力用 **Tavily**——AI 专用搜索，每月 1000 次免费额度，效果比普通搜索引擎更懂你要什么。

备用选 **DuckDuckGo**——零成本兜底，万一 Tavily 抽风还能用。

再加上两个文档处理神器：

**Pandoc**——万能格式转换器，PDF 转 Markdown、Word 转 HTML，随意互转

**Marker**——PDF 转 Markdown 增强版，表格、公式都能保留

这四个装完，Hermes 写文章、查资料、做分析的能力直接起飞。

### 第五件事：管好 Token，别让它烧钱如流水

AI Agent 用多了你会发现一个问题——Token 消耗速度惊人。跑几个任务下来，账单金额让人心跳加速。

这时候需要三个工具来精细管控：

**Tokscale**——实时看全局 Token 消耗，支持 TUI 可视化

```
npx tokscale@latest
tokscale --hermes       # 只看 Hermes 的消耗
tokscale --hermes --week  # 看一周趋势
```

**hermes-hudui**——按模型、按组件、按会话深度拆解成本

```
git clone https://github.com/joeynyc/hermes-hudui.git
cd hermes-hudui && ./install.sh
# 浏览器打开 http://localhost:3001
```

**RTK（Rust Token Killer）**——把终端命令的输出压缩，能省 60% 到 90% 的 Token。Linux、macOS、Windows WSL 都能装：

```
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
rtk init -g
```

装完这三个，你才能真正知道钱花哪儿去了。我第一次装完 Tokscale，看到某些会话的 Token 消耗直接震惊了——原来某个看似正常的对话烧掉了这么多。

### 额外加分项：让它自己优化自己

**Hermes-agent-self-evolution**——用遗传算法自动优化 Agent 的提示词和行为脚本。

相当于让 AI 自己研究怎么让自己更好用，属实是套娃了。

```
git clone https://github.com/NousResearch/hermes-agent-self-evolution.git
cd hermes-agent-self-evolution
pip install -e ".[dev]"
```

### 满配 Hermes 到底强在哪？

简单列一下：

- \*\*人格系统\*\*→它知道自己是什么角色
- \*\*Hindsight 记忆\*\*→跨会话记住你的上下文
- \*\*网页抓取\*\*→能主动去网上找信息
- \*\*搜索 + 文档处理\*\*→信息获取能力拉满
- \*\*Token 管控\*\*→成本透明，不花冤枉钱
- \*\*自我进化\*\*→持续自动优化

裸装 Hermes 和满配 Hermes，是两种完全不同的工具。前者是个礼貌但无知的新人，后者是一个真正能打的数字员工。

好了，按顺序折腾完，你就是满配版 Hermes 了。

有收获的话，转发一下，感谢各位。
