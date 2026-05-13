---
tags: [MarkItDown, 文档预处理, 微软, PDF转换, RAG]
source: "无梦想不青春AGI"
created: 2026-05-13
updated: 2026-05-13
category: MarkItDown
---

# PDF、Word、Excel、PPT等 全扔进一个命令：markitdown 让我重新相信文档预处理

> 来源: [无梦想不青春AGI](https://mp.weixin.qq.com/s?__biz=MjM5NjI1NTUxMw==&mid=2454634651&idx=1&sn=35b11bd15fc6fa3c300f36ad089922fc&chksm=b04baf29c2966103fa5823fcfea8d1673464d2b4123ede201bf8a98f20fd9c0219f7867d4c6e) | 2026-05-13

## 摘要

MarkItDown是微软AutoGen团队开源的Python工具（12万Star），专门将各种文件转换成Markdown格式。不同于传统工具只提取纯文本，MarkItDown保留文档结构：标题转Markdown标题，列表转项目，表格转Markdown表格，图片支持OCR提取。

支持格式覆盖面广：Office全家桶、PDF、图片、音频、网页、数据文件、ZIP压缩包甚至YouTube链接。安装使用简单：`pip install 'markitdown[all]'`后命令行直接使用。MarkItDown的价值在于它提供了文档领域的"文件系统抽象"——不管什么格式，最终都变成Markdown，让大模型理解效果更好、Token消耗更省。适合RAG知识库搭建、批量文档处理等场景。