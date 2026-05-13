---
title: 企业微信 CLI (wechat-cli)
source: https://github.com/fclwtt/wechat-cli
author: fclwtt
date: 2026-05-13
tags:
  - 企业微信
  - CLI
  - AI-Agent
  - 开源项目
  - 腾讯
---

# 企业微信 CLI (wechat-cli)

## 项目简介

企业微信 CLI（命令行界面）开源项目由腾讯企业微信团队发布，于2026年3月30日正式上架 GitHub 社区。该项目开放了企业微信消息、日程、文档、智能表格、会议、待办、通讯录等七大核心产品能力，支持主流 AI Agent（如 Claude Code、Codex、WorkBuddy、QClaw 等）调用。

开发者可基于这些能力，让 AI Agent 以更自然的方式理解和调用企业微信能力，快速开发更贴近日常办公场景的 AI 应用。

**GitHub 仓库**：https://github.com/fclwtt/wechat-cli

---

## 核心能力

CLI 开放了以下七大产品能力：

| 应用 | 可执行的命令 |
|------|-------------|
| 💬 消息 | 获取单聊、群聊消息，并可向指定用户和群聊发送消息 |
| 📄 文档 | 新建、写入、读取文档 |
| 📊 智能表格 | 新建、写入、读取智能表格 |
| 📅 日程 | 新建、查询、更新日程，查看其他人的闲忙状态，添加日程的参与人员 |
| 💻 会议 | 预定、查询、取消会议，添加参会人 |
| ✅ 待办 | 创建待办任务，查询你指定时间内的待办列表、添加待办参与人、更改待办状态 |
| 👥 通讯录 | 获取用户通讯录内的成员 userid、姓名、备注信息 |

---

## 安装与配置

### 环境要求

- Node.js（npm/npx）
- 企业微信机器人的 Bot ID 和 Secret

### 获取 Bot ID 和 Secret

1. 登录企业微信，进入工作台
2. 找到「智能机器人」，点击「手动创建」
3. 选择 **API 模式**创建
4. 连接方式选择「使用长连接」，即可获取并保存 Bot ID 及 Secret
5. 配置可见成员，并完成权限授权，保存即可完成机器人创建

### 安装 CLI

```bash
# 安装 CLI
npm install -g @wecom/cli

# 安装 CLI SKILL（必需）
npx skills add WeComTeam/wecom-cli -y -g
```

或使用：
```bash
npx skills add wecom/cli -y -g
```

---

## 快速开始

### 1. 配置机器人凭证（仅需一次）

```bash
wecom-cli init --botId "YOUR_BOT_ID" --secret "YOUR_BOT_SECRET"
```

### 2. 查看支持的品类和能力

```bash
wecom-cli --help
```

### 3. 列出某个品类下的所有工具

```bash
wecom-cli list contact
```

### 4. 调用工具

```bash
wecom-cli call contact get_userlist '{}'
```

---

## 包含的 Skills

| Skill | 所属应用 | 说明 |
|-------|---------|------|
| wecom-preflight | — | 前置条件检查，确保工具权限配置正确（所有其他 skill 自动依赖） |
| wecom-contact-lookup | 通讯录 | 通讯录成员查询，按姓名/别名搜索 |
| wecom-get-todo-list | 待办 | 待办列表查询，按时间过滤和分页 |
| wecom-get-todo-detail | 待办 | 待办详情查询 |

---

## 支持的 AI Agent

- Claude Code
- Codex
- WorkBuddy
- QClaw
- 其他兼容 MCP/Skill 协议的 AI Agent

---

## 技术特点

- **内部架构**：使用 MCP（Model Context Protocol）服务
- **开发语言**：基于 Rust 开发，性能优越
- **Node.js 支持**：提供 Node.js CLI 包，方便前端开发者使用

---

## 相关链接

- GitHub 仓库：https://github.com/fclwtt/wechat-cli
- 企业微信官网：https://work.weixin.qq.com/

---

## 参考资料

- [企业微信 CLI 开源项目发布 - CSDN](https://blog.csdn.net/m0_70959451/article/details/159637463)
- [企业微信 CLI 开源：开放核心能力，解锁办公新可能 - CSDN](https://blog.csdn.net/EveningTalk/article/details/159651812)
- [腾讯张军：企业微信 CLI 开源项目上架 GitHub 社区](https://so.html5.qq.com/page/real/search_news?docid=70000021_08169c9d81508352)