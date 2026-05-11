> 📎 来源: [Java技术随笔](https://mp.weixin.qq.com/s?__biz=MzkzMzQyMjc5Ng==&mid=2247483985&idx=1&sn=10df35492fae14a275330e6407bc5c96&chksm=c31a3907dbeb5b6af85486c4f85e9d3750f69710faa9f3ba9ec611d5a5c7ecd50e9097fc94fb&mpshare=1&scene=1&srcid=05102ubsR2aaXdO9VTJzJFON&sharer_shareinfo=c0ebc39c284043cc81b2b2b88b9f5eb5&sharer_shareinfo_first=c0ebc39c284043cc81b2b2b88b9f5eb5) | 时间: 2026-05-10 13:25

---

前几天我盯着本地的 http://localhost:3000 看了半天，页面已经跑起来了，可问题还是很烦：要么我自己手动点一遍流程，再把哪里卡住、哪里错位、哪里样式怪怪的转述给 AI；要么就一张张截图，来回解释。说真的，这种沟通成本有点蠢。

我后来折腾 Browser Use⁠，就是想把这件事省掉。它最实用的地方，在我看来是它能自己进去看页面、自己点、自己读内容，然后把结果再回给 Claude 或 Codex⁠。你不用再当中间翻译。

官网： https://browser-use.com/

## ▎它到底适合拿来干什么

我现在对它的理解很简单：当你面对的是一个**真实网页**，而且下一步动作得看页面情况再决定，这时候它就比纯脚本顺手很多。

比如本地前端调试，你可以让它走一遍流程，看看中间有没有报错、按钮有没有反应、页面跳转对不对。再比如你懒得自己盯着页面看布局，它也能截图回来，顺手告诉你首屏有没有明显错位、信息层级乱不乱、配色和留白是不是别扭。

还有一类也很实用，就是后台页面。表格、筛选器、详情页、搜索框，这种我自己平时会直接让它点进去看一遍，再把关键内容提出来。省时。尤其页面路径长的时候，爽得很。

![](assets/img_e6b3e1a52e69.png)

图：让 AI 直接接到本地页面这件事，一旦跑通，很多“我来描述、你来猜”的沟通都会少掉。

## ▎先把 Cloud 和本地版分开

我一开始就栽在这。看到 https://api.browser-use.com/v3/mcp 以为万事大吉，后来才反应过来，那是 Cloud MCP⁠，浏览器跑在云端。你拿它看公网网站当然没问题，可你要看自己电脑上的 localhost⁠、内网系统、开发环境里的调试页，那就不对路了。

如果你的目标跟我一样，是让 Claude 或 Codex 看本地项目，直接走本地 stdio MCP 就行。官方把这两条线分得挺清楚，我建议先看这两页：

MCP 文档： https://docs.browser-use.com/guides/mcp-server

Open Source Quickstart： https://docs.browser-use.com/open-source/quickstart

## ▎装起来其实没那么玄乎

我自己先走的是最小跑通路线。Win11 下把 uv 装上，再把 browser-use 需要的浏览器依赖下好，基本就能往前走了：

pip install uv
uvx browser-use install

如果你想完全按官方安装流程来，那就再补 venv 和 uv pip install browser-use⁠。我这里先不把路写太长，目的很明确，先让本地 MCP 活过来再说。

然后就是最关键的配置。像 cc-switch 这种入口，我更建议直接用 stdio⁠：

{
  "type": "stdio",
  "command": "C:\\Users\\xx\\.local\\bin\\uvx.exe",
  "args": ["--from", "browser-use[cli]", "browser-use", "--headed", "--mcp"],
  "startup\_timeout\_sec": 60
}

如果你机器上的 uvx 已经进了 PATH⁠，command 直接写 uvx 也行。要是桌面客户端老是找不到命令，别猜了，老老实实写绝对路径，排错快很多。

模型这块也别想复杂了。官方本地方案支持 OPENAI\_API\_KEY⁠、ANTHROPIC\_API\_KEY⁠、GOOGLE\_API\_KEY 这些环境变量。你本来就在 Codex 或别的客户端里跑兼容模型的话，有时候它会直接继承当前环境；真连不上，再回头补环境变量就行。

模型支持： https://docs.browser-use.com/supported-models

## ▎接上以后，我会直接这么用

这部分反而最简单。MCP 起好以后，你平时怎么跟 Claude⁠、Codex 说话，就继续怎么说。网页操作能力已经挂成工具了，你直接用自然语言下任务就行。

比如：

使用 browser-use 打开 http://localhost:3000，截图并分析这个页面的布局和视觉风格有没有明显问题。

这就是它最对味的地方。你不用先把页面结构讲一遍，也不用自己总结“哪里可能有问题”，让它先进去看，回来再跟你说。

## ▎我最后留下来的判断

如果你要的是稳定到像 CI 一样的回归测试，那我还是会偏向 Playwright⁠。可如果你现在就想让 AI 帮你看一个真实网页、走一段真实流程、顺手给点界面反馈，Browser Use 这条路真的挺顺。

我自己现在最常拿它干的事，也就两类。第一类是走流程，看看哪一步炸了。第二类是看页面，看看布局和风格是不是已经开始跑偏。就这两件事，已经够它在本地开发里站住了。

· END ·

如果你愿意，欢迎关注。
后面继续分享更多实用内容~
