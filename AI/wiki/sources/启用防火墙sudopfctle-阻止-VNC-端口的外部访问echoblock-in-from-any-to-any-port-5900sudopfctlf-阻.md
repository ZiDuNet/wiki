---
tags: [OpenClaw, Agent, API]
source: "技术小丑"
created: 2026-04-18
updated: 2026-05-10
category: OpenClaw
---

# 启用防火墙sudo pfctl -e# 阻止 VNC 端口的外部访问echo "block in from any to any port 5900" | sudo pfctl -f -# 阻止 OpenClaw 端口的外部访问echo "block in from any to any port 18789" | sudo pfctl -f -# 验证规则sudo pfctl -sr

> 来源: [技术小丑](https://mp.weixin.qq.com/s?__biz=MjM5OTU0NTc5Mw==&mid=2257498869&idx=1&sn=30ea6f07418f176c3ce2c1ad35affd13&chksm=a5c054edb5a31b96a9113165fc8fe2bdcfe81be89ff42a4cde04475c42bd52de5732f6ba9291&mpshare=1&scene=1&srcid=0418rQbPFwCIyWMLYFcg9ORm&sharer_shareinfo=88bf2c8df7567efa2d4f972df66ae6ac&sharer_shareinfo_first=88bf2c8df7567efa2d4f972df66ae6ac) | 2026-04-18

## 摘要

**macOS 多账号 + VNC 隧道，让 AI 智能体在沙箱中运行**
OpenClaw（俗称"小龙虾"）火了。
用自然语言控制电脑，自动点击、录屏、跑脚本，简直是开发者和办公人士的神器。但它有个致命问题：**权限太大**。
一旦授权，OpenClaw 拿到的是整台电脑的"万能钥匙"——它能读写你的桌面、文档、SSH 密钥，甚至能执行
这种毁灭性命令。AI 幻觉、恶意插件、端口暴露……任何一点问题，都可能让你的主账户彻底失控。
**解决方案很简单**：用 macOS 的多用户隔离机制，给 OpenClaw 一个"沙箱账户"。
主账户继续正常工作，OpenClaw 在另一个账户里折腾。即使它发疯，也删不掉你的主账户文件；即使它被黑，黑客进来的只是一个普通用户，无法控制系统。
macOS 基于 Unix，文件系统采用 POSIX 权限模型。每个用户都有自己的
目录，权限隔离由内核强制执行。
即使 OpenClaw 试图执行高危操作，也会被内核拒绝：
配合 VNC 远程桌面协议，我们可以实现"一台电脑，两个桌面"：
•
主账户：日常使用
•
claw 账户：OpenClaw 独占
两者互...

## 相关实体

[[macOS]]
[[Docker]]

## 相关概念

[[数据安全]]
