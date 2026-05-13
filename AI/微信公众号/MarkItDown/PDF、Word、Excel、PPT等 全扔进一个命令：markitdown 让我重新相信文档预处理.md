> 📎 来源: [无梦想不青春AGI](https://mp.weixin.qq.com/s?__biz=MjM5NjI1NTUxMw==&mid=2454634651&idx=1&sn=35b11bd15fc6fa3c300f36ad089922fc&chksm=b04baf29c2966103fa5823fcfea8d1673464d2b4123ede201bf8a98f20fd9c0219f7867d4c6e&mpshare=1&scene=1&srcid=0513E7ehqHlVRJRfMe8bqi3D&sharer_shareinfo=9670c7c5b7573bcdfe6b96c7bb93bf05&sharer_shareinfo_first=9670c7c5b7573bcdfe6b96c7bb93bf05) | 时间: 2026-05-13 16:40

---

# PDF、Word、Excel、PPT等 全扔进一个命令：markitdown 让我重新相信文档预处理

![](assets/img_4f0a7cd80904.png)

故事是这样的。

上个月我在搭一个 RAG 知识库，想把公司过去五年的技术文档全部灌进去。大概有几百份文件，PDF、Word、Excel、PPT 什么格式都有。

我信心满满地开始了。第一份是 PDF，复制粘贴，格式全乱。第二份是 Excel，粘贴出来表格变成了一团文字，列和行全混在一起。第三份是 PPT，复制出来只有文字没有结构，哪页是哪页完全分不清。

折腾了两天，我写了五六个不同格式的解析脚本，每个脚本处理一种格式。PDF 用 PyPDF2，Word 用 python-docx，Excel 用 openpyxl，PPT 用 python-pptx。每个库用法都不一样，每个都有各自的坑。PyPDF2 遇到扫描版 PDF 直接崩溃，python-docx 遇到复杂表格就丢数据，openpyxl 处理合并单元格时头都大了。

更痛苦的是，即使提取出了文本，格式也全丢了。标题变成普通段落，表格变成乱序文字，列表变成一行行没有层次的文字。把这些东西喂给大模型，模型的理解效果大打折扣。

一份排版整齐的表格，到了模型眼里变成一堆乱序文字。你让它分析「第二列第三行的数据」，它根本找不到。

那一刻我突然意识到，用大模型处理文档，最头疼的不是模型能力，而是喂给它什么。

然后我找到了 markitdown。

---

markitdown 是微软 AutoGen 团队开源的一个 Python 工具。专门干一件事——把各种文件转成 Markdown。

12 万 Star，8000 多个 Fork，MIT 协议。

听起来很普通对吧？转 Markdown 的工具多了去了。但 markitdown 不一样的地方在于，它不是「提取纯文本」，而是「保留文档结构」。

标题转成 Markdown 的 # 标题。列表转成 - 项目。表格转成 | 列 | 列 | 的 Markdown 表格。链接保留成 文字。图片支持 OCR 文字提取加 EXIF 元数据。音频支持语音转文字。

换句话说，它不是把一本书拆成散页，而是把书重新排版成大模型最舒服的阅读格式。

---

为什么选 Markdown，不是纯文本？

这是一个很关键的问题。

主流大模型本身就很好地理解 Markdown。你问 ChatGPT 或 Claude 问题，它们回答时不用你提示，也会自动用 Markdown 排版。说明它们在大量 Markdown 语料上训练过，理解得最好。

而且 Markdown 的标记符号极少，Token 消耗更省。一个 HTML 表格可能用几百个 token，同样的内容用 Markdown 表格只需要几十个 token。

跟老牌工具 textract 比，差异更明显。textract 只提取纯文本，把标题、列表、表格、链接这些结构信息全丢了。markitdown 把这些统统保留下来，转成对应的 Markdown 语法。

打个比方，textract 是把一本书拆成散页，你还得自己整理。markitdown 是把书重新装订，还配上了目录和索引。

---

支持的格式覆盖面很广。

Office 全家桶——Word、PowerPoint、Excel，全部支持。PDF，表格、文字、布局尽量保留。图片，JPG、PNG，支持 OCR 文字提取加 EXIF 元数据。音频，MP3、WAV，支持语音转文字。网页和数据文件，HTML、CSV、JSON、XML。还有 EPUB 电子书、Jupyter Notebook，甚至 ZIP 压缩包——它会递归把里面支持的文件全转一遍。

还有一个挺有意思的功能，直接扔 YouTube 链接也能转。自动抓字幕加转录。

我试了一个场景。把公司的一份产品需求文档 PDF 丢进去，100 多页，有表格、有列表、有层级标题。markitdown 几秒钟就转完了。输出的 Markdown 里，标题层级清清楚楚，表格列对齐，列表缩进正确。我直接把这个 Markdown 喂给 Claude，让它总结一下需求要点。Claude 的回复质量明显比用纯文本提取时要好得多。

---

安装和使用简单到离谱。

命令行一键装全依赖：

```
pip install 'markitdown[all]'
```

如果你只需要部分格式，可以按需装：

```
pip install 'markitdown[pdf,docx,pptx]'
```

Python 3.10 以上即可。装好后命令行直接用：

```
markitdown report.pdf > report.md
```

就这么简单。打开终端，敲一行命令，Markdown 文件就出来了。

程序员也可以用 Python API：

```
from markitdown import MarkItDownmd = MarkItDown()result = md.convert("report.xlsx")print(result.text_content)
```

还提供了 Docker 镜像，不想装 Python 环境也能用。

---

说个实际场景。

我之前搭 RAG 知识库的时候，公司内部各种格式的文档，手动处理各种数据实在太繁琐了。用 markitdown 一键全转 Markdown，灌进向量数据库，省去逐个格式写解析器的麻烦。

以前我的流程是——写 PDF 解析器、写 Word 解析器、写 Excel 解析器、写 PPT 解析器，每个都要调试，每个都有 bug。现在我的流程是——一行命令，全部转 Markdown，然后统一处理。

而且这个工具还有插件机制，社区可以开发第三方转换器扩展新格式。用 --use-plugins 开关启用。这意味着它的格式覆盖会越来越全。

---

还有一个点我觉得很多人没注意到。

markitdown 是微软 AutoGen 团队做的。AutoGen 是微软做多 Agent 对话框架的项目。他们做 markitdown 不是偶然，是因为在构建 Agent 工作流的时候，他们发现文档预处理是一个普遍的瓶颈。

Agent 要处理各种格式的文档，但每种格式都有自己的解析规则。如果每个 Agent 都要自己处理格式转换，代码会爆炸。markitdown 提供了一个统一的标准——不管什么格式，先转成 Markdown，然后 Agent 只处理 Markdown 就行。

这就像操作系统里的文件系统抽象。不管你用什么存储设备，操作系统都把它抽象成统一的文件接口。markitdown 做的就是文档领域的「文件系统抽象」——不管什么格式，最终都变成 Markdown。

---

说到这我想聊一个 deeper 的东西。

为什么文档预处理在 AI 时代变得如此重要？

因为大模型的输入是文本，但现实世界的文档是各种格式的。PDF、Word、Excel、PPT，这些格式设计出来是给人看的，不是给 AI 读的。它们的内部结构复杂，有字体、有样式、有布局、有嵌入对象，这些信息对 AI 来说大多是噪音。

文档预处理的核心任务，就是把这些「给人看的格式」转换成「给 AI 读的格式」。而且转换过程中要保留结构信息——标题层级、表格行列、列表嵌套、链接关系。因为 AI 理解文档不只是靠文字内容，还靠结构。

一个表格如果变成了乱序文字，AI 就理解不了行列之间的关系。一个标题如果变成了普通段落，AI 就分不清主次。markitdown 的价值就在于，它在转换过程中尽量保留了这些结构信息。

---

还有一个实用场景。

图片和音频的处理。

给它一张截图，markitdown 不光提取参数，还能用 GPT-4o 描述内容。给它一段会议录音，直接转出文字稿。这意味着你可以把非文本内容也纳入到 AI 工作流里。

我试了一个场景。把一次产品评审会议的录音丢进去，转出来的文字稿保留了说话人的切换，然后我把这个 Markdown 喂给 Claude，让它提取 action items 和决策点。整个过程自动化，不需要手动听录音做笔记。

---

好了，总结一下。

markitdown 是微软开源的文件转 Markdown 工具，12 万 Star。它解决的是 AI 时代一个底层问题——怎么让大模型真正「读懂」我们的文档。

它没做花哨的事，就是把格式转换做到足够广、足够好用。PDF、Word、Excel、PPT、图片、音频，扔进去基本都能出干净的 Markdown。而且保留了文档结构，让大模型的理解效果更好、Token 消耗更省。

日常跟大模型交互越来越频繁，这类基础设施的价值只会越来越高。

GitHub 地址：https://github.com/microsoft/markitdown

---

你看完这篇，有什么想说的？

你平时是怎么把各种格式文档喂给 AI 的？复制粘贴？写解析脚本？还是已经用上 markitdown 了？你觉得文档预处理是 AI 应用的基础设施吗？

评论区聊聊。

---

以上，既然看到这里了，如果觉得不错，随手点个赞、在看、转发三连吧，如果想第一时间收到推送，也可以给我个星标⭐～

谢谢你看我的文章，我们，下次再见。

> / 作者：mojianpo
> / 投稿或爆料，请联系邮箱：406223802@qq.com
