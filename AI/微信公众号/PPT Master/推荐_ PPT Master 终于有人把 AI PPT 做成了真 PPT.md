> 📎 来源: [AI 新纪元-分子模拟](https://mp.weixin.qq.com/s?__biz=MzkwMzQ1NjY2OA==&mid=2247483793&idx=1&sn=cf31510bd653c648b40186ea3d2a45f0&chksm=c1ac5967b061d22a7ff2fd018d7c115ce0152e214ad217ea88fd325e82fcb4260cee5319085f&mpshare=1&scene=1&srcid=0430b9dU8djHhdB9uabFuJYH&sharer_shareinfo=1bf068c97c51b63f3c15d551cf036246&sharer_shareinfo_first=1bf068c97c51b63f3c15d551cf036246) | 时间: 2026-04-30 19:41

---

# PPT Master：终于有人把 AI PPT 做成了真 PPT

很多 AI PPT 工具，第一次看很惊艳。

但打开文件后会发现：标题不能单独改，图表不能拆，元素不能挪。一整页其实就是一张图。

这不是 PPT，更像截图合集。

PPT Master 想解决的就是这个问题：把 PDF、DOCX、网页、Markdown 等资料，变成一份**原生可编辑的 PowerPoint**。

文本是文本框，图形是形状，图表和版式都能继续调整。

> 它交付的不是“看起来像 PPT 的图片”，而是一份真正可以继续工作的 `.pptx`。

## 真正有用的地方

PPT Master 适合三类人：

- 经常把报告、文章、论文、网页整理成汇报材料的人。
- 不想从空白页开始排版，但又不能接受图片式 PPT 的人。
- 已经在用 Claude Code、Cursor、VS Code Copilot、Codex CLI 等 agent 工具的人。

它不是要替你一次生成“最终完美稿”。

更现实的价值是：让 AI 先完成结构、版式、视觉初稿和文件导出，你再做最后判断和精修。

这比从零做 PPT 快很多，也比拿到一堆不可编辑图片更靠谱。

## 它为什么不一样

常见 AI PPT 大致有四种：

| 类型 | 结果 | 后续编辑 |
| --- | --- | --- |
| 模板填空 | 套模板 | 受限制 |
| 图片式 PPT | 一页一图 | 很难改 |
| HTML 演示 | 网页 | 不是 PPT |
| PPT Master | 原生 PPTX | 可以逐元素改 |

PPT Master 选择的是最难、但最有价值的一类：生成 PowerPoint 原生对象。

这意味着你可以继续改标题、换颜色、移动图形、拆分图表，而不是被 AI 的第一版结果锁死。

## 它是怎么工作的

PPT Master 不是传统网页产品，更像一套给 AI agent 使用的本地工作流。

核心过程很清晰：

1. 先把 PDF、DOCX、网页、表格等资料转成结构化 Markdown。
2. 再由 AI 分析内容，确定页数、结构、风格和设计规范。
3. 然后逐页生成 SVG 设计稿。
4. 最后把 SVG 转成 PowerPoint 原生 DrawingML，并导出 `.pptx`。

这条路线的关键是 SVG。

AI 比较擅长生成 SVG，人也可以直接预览；而 SVG 和 PowerPoint 都是画布式的绝对坐标系统，转换起来比 HTML 更自然。

所以它的逻辑不是“AI 直接硬写 PPT XML”，而是先生成可检查的设计稿，再工程化转成可编辑 PPT。

## 本地工作流的优势

PPT Master 的另一个重要特点是本地运行。

除了你选择调用的 AI 模型外，文件转换、项目目录、SVG、PPTX 导出都在你的电脑上完成。

对投融资材料、公司报告、客户方案、研究资料来说，这一点很实际：资料不必为了做一份 PPT 就交给陌生平台。

它也不锁定模型和工具。Claude、GPT、Gemini、Kimi 都可以尝试；Claude Code、Cursor、VS Code Copilot、Codex CLI 等 agent 都能作为入口。

## 适合什么场景

如果你只是偶尔做一页简单汇报，普通模板工具可能更省事。

但如果你经常处理复杂资料，并且需要一份还能继续编辑、交付、复用的 PPT，PPT Master 的方向就很对。

它尤其适合：

- 咨询方案
- 投融资材料
- 研究汇报
- 课程培训
- 产品说明
- 文档转演示稿

## 怎么开始

最简单的方式是克隆项目并安装依赖：

```
git clonehttps://github.com/hugohe3/ppt-master.gitcd ppt-masterpip install -r requirements.txt
```

然后把资料放进 `projects/`，在 AI agent 里说：

```
请用 projects/q3-report/sources/report.pdf 生成一份 10 页左右的 PPT。
```

AI 会先确认设计规范，再生成 SVG、检查质量、导出 PPTX。

最终重点看 `exports/` 里的原生形状版 `.pptx`。

## 最后一句

AI 做 PPT，不应该只给你一张漂亮截图。

更好的结果，是给你一份可以继续修改、继续交付、继续复用的 PowerPoint。

PPT Master 的价值就在这里。

项目地址：

https://github.com/hugohe3/ppt-master
