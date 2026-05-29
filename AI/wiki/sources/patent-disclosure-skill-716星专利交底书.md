---
tags: [专利, AI工具, 自动化, patent-disclosure-skill]
sources: [人才+1，有人把申请专利也做成了skill，知识产权的普及度再次增加.md]
created: 2026-05-30
updated: 2026-05-30
---

# patent-disclosure-skill：AI 全自动专利技术交底书

**来源：** 人才+1，有人把申请专利也做成了skill，知识产权的普及度再次增加.md
**摄入日期：** 2026-05-30
**类型：** 文章
**公众号：** 开源AI项目落地

## 摘要

介绍 patent-disclosure-skill 项目——一个专利技术交底书自动生成技能包。能把研发配合写专利的时间从 3 天缩短到 30 分钟。通过扫描本地代码仓库或设计文档，自动挖掘专利点，输出符合国知局标准、带高清图表的 Word 版技术交底书。适用于软件/硬件专利，专利代办未来也会白菜价。

## 核心观点

- **核心价值**：把专利技术交底书从 3 天压缩到 30 分钟
- **输入方式**：扫描本地代码仓库或设计文档（.docx / .pptx）
- **原材料自动清洗**：内置文件转换脚本，将 Office 二进制文件打散为 Markdown 纯文本再喂给 AI，避免解析混乱
- **硬核查新**：用 Playwright 爬国知局官方专利公布公告网站做查新对比，降级方案是 Google Patents
- **图示自动化渲染**：大模型输出 Mermaid 代码，调用本地 Node.js 渲染引擎生成 PNG，物理嵌入 Word
- **LaTeX 公式一致性闭环**：检查 Word 里 LaTeX 公式兼容性，扫描前后参数一致性
- **多轮修订和审计追踪**：增量合并，维护修订对话记录，追溯每轮修改来龙去脉
- **GitHub**：https://github.com/handsomestWei/patent-disclosure-skill

## 提及实体

- [[patent-disclosure-skill]] — 专利技术交底书自动生成 Skill，716 Star
- [[Playwright]] — 官方查新时用的浏览器自动化工具
- [[Mermaid]] — 流程图/架构图描述语言，用于自动生成专利附图
- [[handsomestWei]] — 项目作者

## 涉及概念

- [[专利技术交底书]] — 专利申请核心文件，描述技术方案、背景、缺陷、架构图、流程图
- [[AI文档自动化]] — 用 AI 自动处理文档转换、格式调整、内容生成
- [[Vibe Coding]] — 类似文章 919 的 AI 辅助开发模式