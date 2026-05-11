---
tags: [Hermes, Agent, 飞书]
source: "斐哥讲AI"
created: 2026-04-22
updated: 2026-05-10
category: Hermes
---

# 创建文档lark-cli docs +create --title "标题" --markdown "# 标题\n\n内容"# 更新文档lark-cli docs +update --doc  --mode append --markdown "\n\n新内容"# 获取文档lark-cli docs +fetch --doc # 搜索文档lark-cli docs +search --query "关键词"# 查看群列表lark-cli im chat list# 发消息lark-cli im message create --receive-id-type chatid \  --data '{"receiveid":"<群ID>","msgtype":"text","content":"{\"text\":\"Hello\"}"}'

> 来源: [斐哥讲AI](https://mp.weixin.qq.com/s?__biz=MzYzNTg3NTM2NA==&mid=2247483674&idx=1&sn=70102af2d451e6475ce7599e66f401f8&chksm=f1648b5e55e8f3ab2b90ff4b2578ab6a82b4648dcd39c123d300f18c93e28c8a0ec844a8da3f&mpshare=1&scene=1&srcid=0422zIaTmHCAphLsexCWI8aY&sharer_shareinfo=ca77006550810806f69bbe7946b7855f&sharer_shareinfo_first=ca77006550810806f69bbe7946b7855f) | 2026-04-22

## 摘要

lark-cli 是飞书官方命令行工具，配置好后可以让 AI 帮你操作飞书。
- 云文档：创建、更新、搜索、分享文档
- 发送消息：发消息到群聊或用户
- 日历管理：创建日历事件、查看日程、添加提醒
- 联系人：搜索用户、获取用户信息
- 群组管理：查看群列表、管理群成员
- 任务管理：创建任务、设置截止日期
- 视频会议：创建会议、获取会议信息
- 通讯录：搜索部门、获取成员列表
- 更多：网络钩子、审批等企业功能
- 不用打开飞书网页，直接用命令行或 AI 操作
- 可以自动化重复性工作（如每天生成报告发到飞书）
- 与 AI Agent 结合，实现智能化工作流
告诉 AI：
AI 会自动帮你执行安装命令。
验证安装：
告诉 AI：
AI 会引导你完成整个配置流程。
运行以下命令：
运行后会显示一个链接，在浏览器打开。

## 相关实体

[[Hermes]], [[飞书]]

## 相关概念

[[AI-Agent]]
