> 📎 来源: [编程老兵学AI](https://mp.weixin.qq.com/s?__biz=MzA5Njg3MDQzNQ==&mid=2456596671&idx=1&sn=1887f20ca626f157584fb989e0ecc5e8&chksm=86aea4c111a5fc58160b0758f712af11149c217da4a4cb55d9455dd8e8fb0307dce673cdaaf3&mpshare=1&scene=1&srcid=0421SQGs0Kw1hXYZSmsgtayC&sharer_shareinfo=83e47392126aa0e869afef72132126a6&sharer_shareinfo_first=83e47392126aa0e869afef72132126a6) | 时间: 2026-04-21 12:04

---

# 🎓 OpenClaw 多 Agent 团队协同案例分享

> 零基础搭建你的 AI 助教团队

---

## 📋 案例简介

本案例将展示如何使用 OpenClaw 快速搭建一个教学辅助 AI 团队，包含三个不同角色的 Agent，帮助老师减轻教学负担。

![](assets/img_b3a157ca803a.jpg)

### 适合谁看

- OpenClaw 新手
- 想用 AI 辅助教学的老师
- 对多 Agent 协作感兴趣的同学

### 你能学到什么

- 如何创建第一个 OpenClaw Agent
- 如何配置多 Agent 协同
- 如何将 Agent 接入实际场景

---

## 🛠️ 准备工作

### 1. 安装 OpenClaw

```
# 安装npm install -g openclaw@latest# 初始化openclaw onboard
```

![](assets/img_56417c66ec5c.jpg)

### 2. 配置飞书渠道（可选）

```
openclaw channels login
```

### 3. 启动 Gateway

```
openclaw gateway --port 18789
```

---

## 📝 快速开始

### 步骤 1：创建配置文件

在任意目录创建 `openclaw.json`：

```
{  "agents": {    "list": [      {        "id": "course-qa",        "name": "课程问答助手",        "instructions": "你是课程问答助手...",        "tools": { "alsoAllow": ["read"] }      }    ]  }}
```

![](assets/img_8e43fe965f1b.jpg)

### 步骤 2：测试

通过飞书发送消息给机器人，体验 Agent 回答。

---

## 🔧 进阶：创建多 Agent 团队

### 完整配置文件

```
{  "agents": {    "list": [      {        "id": "course-qa",        "name": "课程问答助手",        "instructions": "回答课程问题...",        "tools": { "alsoAllow": ["read", "web_fetch"] }      },      {        "id": "homework-helper",         "name": "作业助手",        "instructions": "引导完成作业...",        "tools": { "alsoAllow": ["read"] }      },      {        "id": "learning-coach",        "name": "学习教练",        "instructions": "鼓励学习...",        "tools": { "alsoAllow": ["read"] }      }    ]  }}
```

![](assets/img_9ff2432057f7.jpg)

---

## ❓ 常见问题

### Q1: Agent 为什么不回答？

A: 检查配置是否生效，运行 `openclaw gateway restart`

### Q2: 回答质量不好？

A: 调整 prompt，使用更具体的指令

### Q3: 如何接入更多渠道？

A: 参考 OpenClaw 文档配置 Telegram/Discord

---

## 📚 扩展学习

- OpenClaw 官方文档[1]
- Lobster 工作流[2]
- 多 Agent 路由[3]

---

## 🤝 参与讨论

有问题？来 OpenClaw Discord 或 GitHub 提 Issue！

![](assets/img_aa96ea7fa890.jpg)

---

## ⚠️ 注意事项

1. **配置路径**：将配置文件放到 `~/.openclaw/agents/main/agent/` 目录，或使用 `-c` 参数指定
2. **重启生效**：修改配置后记得 `openclaw gateway restart`
3. **工具权限**：根据需要给 Agent 添加工具权限
4. **敏感信息**：不要在 prompt 中包含敏感信息

---

## 📞 支持

- 文档：docs.openclaw.ai
- GitHub：github.com/openclaw/openclaw
- Discord：discord.gg/clawd

---

*本案例由 Monica 整理 | 2026-03-11 | 版本 1.2*

### 引用链接

[1]OpenClaw 官方文档: *https://docs.openclaw.ai*

[2]Lobster 工作流: *https://docs.openclaw.ai/tools/lobster*

[3]多 Agent 路由: *https://docs.openclaw.ai/concepts/multi-agent*
