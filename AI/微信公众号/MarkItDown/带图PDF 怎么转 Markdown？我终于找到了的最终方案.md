> 📎 来源: [胡萝卜很芒](https://mp.weixin.qq.com/s?__biz=MzA3MzU1MjU3NA==&mid=2247483859&idx=1&sn=3e82d13efe0d33ea588a2d0d3487754c&chksm=9e1df7d338811717f5d46c65baf655d690554137eb9891a4f4e9ffc10171668445cda9b4ad98&mpshare=1&scene=1&srcid=0522TTo3ewEjBQLIIQ6oQVGd&sharer_shareinfo=8a0d141de75708c9934f58c3259e91d2&sharer_shareinfo_first=8a0d141de75708c9934f58c3259e91d2) | 时间: 2026-05-22 22:35

---

本以为是个简单的任务。把几篇带图片的 PDF 文章转成 Markdown 格式，放到 Obsidian 知识库里。结果没想到，这竟成了一场反复折腾的修行。

一markitdown

第一个尝试的工具是 markitdown，微软开源的 PDF 转 Markdown 工具。

这个工具之前各个公众号自媒体都在吹，我以为很好用，用完后发现对于有图的 DOC、PDF 不太行，转化后的内容没有图片。

⚠️ 原文里有大量表格、数据截图，这些内容全都没了。只剩下一堆文字，信息完整性大打折扣。

这个工具适合纯文字的 PDF，但遇到图文混排的文档，就不够用了。

二PyMuPDF（fitz）

第二个尝试的是 PyMuPDF，Python 里叫 fitz 库。

这个库功能很强大，能把 PDF 的每一页转成图片，也能提取文本。

⚠️ 但真正动手的时候，才发现**中文路径是个大坑**。直接传入中文路径打开 PDF，报错：FileNotFoundError。路径显示成乱码。

折腾了一番才发现：Python 的 glob.glob() 能正确处理中文路径。用它先找到文件，再打开，问题解决。

fitz 提取文本的效果还行，但表格依然有问题。复杂的表格结构会被打乱，对齐关系丢失，读起来很费劲。

三用 marker-pdf 转换

第三个工具是 marker-pdf，专门为 PDF 转 Markdown 设计的。

✅ 最大优势：能自动识别 PDF 中的文字、表格和图片，输出结构化的 Markdown 文件。图片也会自动提取出来，放在单独的文件夹里。

转换效果明显好很多。表格保留得比较完整，图片也能正确引用。

⚠️ 但有两个问题：
· 转换速度很慢，一篇几十页的 PDF 要等近 20 分钟
· 图片太多时解析不到位，甚至把图片拆解过细，还会导致图片位置解析错位

四MinerU

第四个工具是 MinerU，开源社区的 PDF 提取工具，专门针对学术论文和复杂文档设计，对中文内容比较友好。

✅ 最大卖点：完整保留 PDF 的结构，包括公式、表格、图片，输出干净的 Markdown 格式。

看到介绍后很心动，准备安装。但问题来了：**完整版需要 GPU。**

⚠️ MinerU 完整功能依赖 detectron2，需要 NVIDIA GPU。我的电脑是 MacBook，没有 NVIDIA 显卡，编译 detectron2 直接失败。

试了 Docker 方案，官方 Dockerfile 基础镜像同样依赖 NVIDIA GPU（Compute Capability 7.0 以上）。Windows 电脑也不行。

折腾半天，最终结论：**用不了 MinerU 完整版。只能用轻量版（lite 版本），功能有限，OCR 和表格识别都不完整。**

后来换了思路：**把 PDF 上传到 MinerU 的在线服务处理。**

🔗 **在线地址：**https://mineru.net/OpenSourceTools/Extractor

这次转换效果确实好。有大量数据表格、指数估值截图、均线图表，MinerU 都正确提取了。存在图片拆解过细的情况，不过只有一张，手动添上去就行。

整理到 Obsidian 时，外部 URL 离线会失效，于是又做了一步处理：下载图片到本地附件文件夹，把 Markdown 里的外部链接全部换成 Obsidian 的 wiki-link 格式。这样图片就永久保存在知识库里了。

✅ MinerU 的转换质量确实比 marker-pdf 更好，表格结构更完整，并且直接把图片里的表格转化为了文字版，图片引用更清晰。

五工具对比

四种工具各有优劣，汇总如下：

| 工具 | 优点 | 缺点 |
| --- | --- | --- |
| markitdown | 速度快，几秒出结果；适合纯文字 PDF | 无法提取图片；图文混排文档不适用 |
| PyMuPDF (fitz) | 功能强大；可提取文本和页面截图 | 表格解析效果一般；中文路径需要特殊处理 |
| marker-pdf | 自动识别文字、表格、图片；输出结构化 Markdown；图片自动提取 | 转换速度慢；复杂表格可能简化；需人工核对完整性 |
| MinerU | 转换质量最高；表格、公式、图片完整保留；输出干净 Markdown | 需在线服务；完整版需 NVIDIA GPU，并且需要占 10G 以上的内存。 |

六最终方案

**✦ 批量转换方案**

如果是带图表的 PDF，想用程序**批量转换**：
先用 marker-pdf 做整体转换，拿到结构化的 Markdown 和提取出来的图片。之后人工核对内容完整性，遇到复杂表格用 MinerU 在线解析作为补充。

**✦ 少量高质量方案**

如果数量不多，直接用 MinerU 在线服务转换，效果更好，表格、图片都能完整保留。

🔗 **MinerU 在线地址：**https://mineru.net/OpenSourceTools/Extractor

**🙌 MinerU 也有 API**如果点赞超过 20，后面就写一篇用 MinerU API 进行批量转换的文章
欢迎 **关注** 我，持续分享 AI、Obsidian 相关内容
觉得文章有用？顺手 **点赞** 支持一下，让更多人看到 ✨
