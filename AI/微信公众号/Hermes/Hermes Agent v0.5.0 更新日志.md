> 📎 来源: [OhMyAgent](https://mp.weixin.qq.com/s?__biz=MzI3MTUyMzA3Mg==&mid=2247484456&idx=1&sn=c6a96e6564b459c9811d411608ed8b90&chksm=eb7c84550508f07a68ea129a018b07f239d2dfcffe8971bf5e9ce0062623f12ad21f4c35c2c6&mpshare=1&scene=1&srcid=0422KC0BsontGzG3BoLYOqeF&sharer_shareinfo=a257ae9261d7eee7b4ab0e98bb513ce0&sharer_shareinfo_first=a257ae9261d7eee7b4ab0e98bb513ce0) | 时间: 2026-04-22 00:54

---

## v0.5.0

---

### 📅 发布时间

2026 年 3 月 28 日

### 📋 摘要

加固版本。新增 Hugging Face provider、/model 命令重构、Telegram 私聊话题、原生 Modal SDK、插件生命周期钩子、GPT 模型工具调用引导、Nix flake、50+ 安全和可靠性修复及供应链审计。

### 🎨 新功能

- **Nous Portal 支持 400+ 模型** — 推理门户大幅扩展
- **Hugging Face 一等推理 provider** — 完整集成 HF Inference API，含智能 agent 模型选择器、实时 /models 端点探测、设置向导流程
- **Telegram 私聊话题** — 基于项目的对话，每个话题可绑定独立 skill，在单个 Telegram 聊天中实现隔离工作流
- **原生 Modal SDK 后端** — 用原生 Modal SDK 替代 swe-rex 依赖，消除隧道简化终端后端
- **插件生命周期钩子激活** — pre\_llm\_call、post\_llm\_call、on\_session\_start、on\_session\_end 钩子在 agent 循环和 CLI/网关中完整触发
- **GPT 模型工具调用引导** — GPT\_TOOL\_USE\_GUIDANCE 防止 GPT 模型描述意图而非调用工具，自动清理历史中的 budget 警告
- **Nix flake** — 完整 uv2nix 构建、NixOS 模块含持久化容器模式、从 Python 源码自动生成配置键
- **供应链加固** — 移除被入侵的 litellm 依赖、锁定所有依赖版本范围、重新生成带哈希的 uv.lock、新增 CI 供应链审计工作流
- **Anthropic 输出限制修复** — 用每模型原生输出限制替代硬编码 16K max\_tokens（Opus 4.6 支持 128K、Sonnet 4.6 支持 64K）
- **思考预算耗尽检测** — 跳过模型将所有输出 token 用于推理时的无意义续重试
- **API 服务器幂等性支持** — Idempotency-Key、body 大小限制、OpenAI 错误信封
- **可配置 /verbose 命令** — 消息平台可切换工具输出详细程度
- **会话搜索最近会话模式** — 不带查询浏览最近会话，含标题、预览和时间戳
- **会话配置显示** — /new、/reset 和自动重置时展示会话配置
- **第三方会话隔离** — --source 标志按来源隔离会话
- **Telegram 自动发现备用 IP** — DNS-over-HTTPS 在 api.telegram.org 不可达时自动切换
- **上下文压缩重构** — 基于比例的缩放替代死代码 summary\_target\_tokens
- **新增 Skills**: G0DM0D3 jailbreaking、Docker 管理、OpenClaw 迁移 v2

### ⚠️ 修复

- 修复 SQLite WAL 写锁争用导致 TUI 冻结 15-20 秒
- 修复 SQLite 并发安全 + 会话记录完整性
- 修复网关缓存 agent 的 token 双重计数
- 修复空闲会话 "Event loop is closed" / "Press ENTER to continue"
- 修复工具调用循环中推理框渲染 3 次
- 修复状态栏显示 26K 而非 260K token 计数
- 修复 /queue 无论配置如何都始终工作
- 修复 agent turn 完成后 Discord 幽灵输入指示器
- 修复 Slack 进度消息发送到错误线程
- 修复 WhatsApp 媒体下载（文档、音频、视频）
- 修复 Telegram "Message thread not found" 杀死进度消息
- 修复 OpenClaw 迁移覆盖默认配置
- 修复 hermes update PEP 668 externally-managed-environment 错误
- 修复子 agent 因共享预算过早耗尽 max\_iterations
- 修复网关挂起 agent — /stop 现在强制终止会话锁
- 修复 \_custom provider 静默重映射为 openrouter
- 修复 Matrix 缺失 PLATFORMS 字典条目
- 修复 Email adapter \_seen\_uids 无限增长
- 修复 config.get() 在 YAML null 值时 AttributeError 崩溃
- 修复 .strip() 在 YAML None 值时崩溃
- 修复 API 服务器流式传输在工具调用时中断
- 修复 AsyncOpenAI/httpx 跨循环死锁
- 修复子 agent toolsets 未限制为父级启用集
- 修复 zip-slip 路径遍历在 self-update 中
- 修复 /model 命令重构为共享 switch\_model() 管线

### 💥 破坏性变更

无

### 🗑️ 废弃

无
