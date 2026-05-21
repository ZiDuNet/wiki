---
title: "Hermes 发布 Computer Use：MCP 协议驱动 macOS 桌面控制"
type: source-summary
created: 2026-05-12
updated: 2026-05-12
sources: ["Hermes 发布 Computer Use，可以控制你的电脑了，而且不限模型.md"]
tags: [Hermes, Computer Use, MCP协议, macOS, Agent, 桌面自动化]
---

# Hermes Computer Use：不限模型的桌面 Agent 控制

## 摘要

Hermes 发布 Computer Use 功能，通过 MCP 协议和 cua-driver 驱动，实现模型无关的 macOS 桌面自动化控制。核心优势：不限模型（Claude/GPT-4/Gemini/本地 vLLM 均可用）、后台运行不抢焦点、安全防护多层保障、Token 效率优化（20 步操作仅 ~3 万 token）。

## 核心特性

### 1. 不限模型（MCP 协议驱动）

**技术架构**：
- 底层驱动：cua-driver（MCP 协议实现）
- 不绑定任何模型厂商，只要支持 vision（能看截图）即可
- 支持列表：Anthropic Claude、OpenRouter 任意 vision 模型、GPT-4/5、Gemini、本地 vLLM

**优势**：用最便宜的 vision 模型干杂活，用最强模型干精细活，自由搭配。

### 2. 后台运行，不抢焦点

**技术方案**：macOS SkyLight 私有 SPI，事件直接发给目标进程，不走 HID 事件注入。

**效果**：
- 不移动光标
- 不切换 Space
- 不抢焦点
- 用户的鼠标纹丝不动，Mail 窗口不会弹到前台

**案例**：让 agent 去 Mail 搜 Stripe 最新邮件并总结 — 全程后台完成。

### 3. 安全防护

多层保护机制：
- **破坏性操作默认审批**：CLI 弹确认框，消息平台有审批按钮
- **硬编码屏蔽危险操作**：清空废纸篓、强制删除、锁屏、登出
- **输入内容黑名单**：`curl | bash`、`sudo rm -rf /`、fork bomb 直接拦截
- **系统 prompt 约束**：不点权限弹窗、不输密码、不执行截图嵌入指令
- **手动模式**：`approvals.mode: manual` 每步确认

### 4. Token 效率优化（四层）

| 优化层 | 方式 |
| --- | --- |
| 截图淘汰 | 仅保留最近 3 张截图，更早的自动替换为占位符 |
| 客户端压缩 | 识别多模态工具结果，自动剥离旧截图图片部分 |
| 图片 token 估算 | 每张图按 ~1500 token 估算（Anthropic 统一费率） |
| 服务端上下文编辑 | 仅 Anthropic API：服务端旧工具结果清理 |

**实测**：1568×900 分辨率 20 步操作会话，截图上下文约 3 万 token（而非 60 万）。

## 安装方式

```bash
# 方式一：直接命令（推荐）
hermes update
hermes computer-use install

# 方式二：交互式
hermes tools
# 选 🖱️ Computer Use (macOS) → cua-driver (background)
```

**macOS 权限**：
- 系统设置 → 隐私与安全性 → 辅助功能（允许终端/Hermes 应用）
- 系统设置 → 隐私与安全性 → 屏幕录制（允许同样应用）

**启动会话**：
```bash
hermes -t computer_use chat
```

## 限制条件

- **macOS only**：cua-driver 依赖 Apple 私有 SPI，Linux/Windows 不可用
- **私有 SPI 风险**：Apple 可能随系统更新改符号表，可用 `HERMES_CUA_DRIVER_VERSION` 环境变量锁定版本
- **后台模式延迟**：SkyLight 路由事件延迟 5-20ms，比直接 HID 注入慢
- **不支持键盘输入密码**：type 命令对 shell 危险模式有硬拦截

## 兼容性

| Provider | 视觉支持 | 可用 | 备注 |
| --- | --- | --- | --- |
| Anthropic (Claude Sonnet/Opus 3+) | ✅ | ✅ | 最佳体验，支持 SOM + 原始坐标 |
| OpenRouter (任意 vision 模型) | ✅ | ✅ | 支持多部分 tool message |
| OpenAI (GPT-4+, GPT-5) | ✅ | ✅ | 同上 |
| 本地 vLLM / LM Studio | ✅ | ✅ | 模型需支持多部分 tool content |
| 纯文本模型 | ❌ | ⚠️ 降级 | 可用 mode="ax" 纯无障碍树模式 |

## 关键实体

- [[Hermes-Agent]] — Computer Use 功能的提供方
- [[MCP协议]] — Computer Use 的底层驱动协议
- [[Claude]] / [[GPT-4]] / [[Gemini]] — 可用于驱动的 vision 模型
- [[macOS]] — 唯一支持的操作系统平台

## 关键概念

- [[浏览器自动化]] — Computer Use 本质是桌面自动化
- [[多模态]] — vision 能力是 Computer Use 的"眼睛"
- [[Token优化]] — 四层截图压缩节省上下文
- [[安全机制]] — 审批流、黑名单、硬编码屏蔽
