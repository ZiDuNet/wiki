> 📎 来源: [田园往事](https://mp.weixin.qq.com/s?__biz=MzUyMzQ3MTMwNA==&mid=2247483733&idx=1&sn=fd29704b1d0b20fac2329c4267510ffa&chksm=fbfe8be8cda26bf9856b69b74f711407b9861997e12c24d0cf7f2b545ef3bdcd6b56db239912&mpshare=1&scene=1&srcid=0420xnpaH3UBmkbfnfbUJFFS&sharer_shareinfo=f634053d6f7813831ae13f553c650d0a&sharer_shareinfo_first=f634053d6f7813831ae13f553c650d0a) | 时间: 2026-04-20 21:29

---

一台服务器，一个飞书机器人，172 个 AI 专家为你打工。这不是科幻，这是我今天实际搭建的私人 AI 工作站。

---

📌 前言

你是否想过拥有一个 24 小时在线的 AI 助手团队？前端开发、后端架构、市场营销、游戏开发……每个领域都有专属专家随时待命。

今天我用 Hermes Agent 搭建了这样一套系统，接入飞书，配置多模型，并导入了 172 个专业 AI Agent。以下是完整的安装步骤和实战记录。

---

一、环境信息

系统：Ubuntu（WSL2）Hermes 版本：v0.9.0 (2026.4.13)安装路径：/home/liuzhe/.hermes/Python：3.11.15接入平台：飞书（Feishu）

---

二、Hermes Agent 安装

1. 克隆项目git clone GitHub - NousResearch/hermes-agent: The agent that grows with you ~/.hermes/hermes-agentcd ~/.hermes/hermes-agent
2. 创建虚拟环境 & 安装依赖python3 -m venv venvsource venv/bin/activatepipinstall -e .
3. 验证安装hermes --version

# 输出: Hermes Agent v0.9.0 (2026.4.13)

4. 启动 Gatewayhermes gateway run --replace

💡 Gateway 是 Hermes 的核心服务，负责连接各个平台，必须保持后台运行。

---

三、多模型配置

模型分工：• 日常对话 & 任务执行 → Claude (claude-sonnet-4-6)• 图片识别 & 视觉分析 → Gemini (gemini-3-pro-preview)• 本地备用模型 → Gemma4 (via Ollama)

多模型协同的优势：• 各司其职：Claude 负责推理和对话，Gemini 负责识图• 降低成本：简单任务用便宜模型，复杂任务用强模型• 高可用性：主模型挂了自动切换备用模型

---

四、飞书接入配置

Hermes 原生支持飞书平台接入，通过 WebSocket 长连接实现实时通信。

✓ feishu connected[Feishu] Connected in websocket mode

使用方式：

1. 在飞书中找到已配置的机器人
2. 直接发送消息即可对话
3. 支持文字、图片（Gemini 识图）、文件等多种消息类型

---

五、导入 172 个专业 AI Agent

这是重头戏！导入了开源项目 Agency Agents（⭐ 82,718 Stars），将一个完整的"虚拟 AI 公司"搬进了 Hermes。

Agent 部门一览：💻 Engineering（29个）：前端开发、后端架构、AI工程师、DevOps🎮 Game Development（20个）：Unity架构师、Unreal世界构建、Godot脚本📊 Finance：会计师、财务分析师🎨 Design：UI/UX 设计师📈 Marketing：SEO专家、内容策略师📋 Project Management：工作流架构师🧪 Testing（7个）：API测试、性能基准🏗️ Specialized（40+）：留学顾问、合规审计、供应链策略💰 Sales：销售外联、客户管理📱 Spatial Computing：visionOS/Metal 开发

导入效果：Hermes 根据问题自动匹配专家 Agent• "帮我写个 React组件" → 加载 Frontend Developer• "分析一下这个市场" → 加载 Strategy Consultant• "帮我规划留学" → 加载 Study Abroad Advisor

---

六、测试验证

随机验证 3 个 Agent + Game Development 5 个 Agent，全部 ✅ 通过。

---

七、稳定性保障

• 24 小时运行配置，30分钟超时，凌晨4点重置• systemd 管理，崩溃自动重启• 定期同步配置到 Windows D盘

---

八、实用的中国特化 Agent

🇨🇳 China Market Localization Strategist — 中国市场本地化策略📺 Bilibili Content Strategist — B站内容运营🔍 Baidu SEO Specialist — 百度SEO优化🛒 China E-Commerce Operator — 中国电商运营🎓 Study Abroad Advisor — 留学规划🐦 X (Twitter) URL 处理专家 — 社交媒体管理

---

九、实用 Skills 推荐

开发：TDD测试驱动开发、系统调试、代码审查创意：ASCII 艺术、Excalidraw 图表、P5.js 可视化研究：arXiv 论文检索、YouTube 转录、博客监控生产力：Google Workspace、Notion、飞书文档、PDF 编辑AI/ML：GGUF 量化、vLLM 部署、Axolotl 微调

---

十、总结

今日成果：✅ Hermes Agent 安装部署完成✅ 飞书平台接入成功✅ 多模型协同配置（Claude + Gemini + Ollama）✅ 172 个专业 AI Agent 导入并验证通过✅ 24 小时稳定运行配置

核心价值：Hermes Agent 不只是一个聊天机器人，它是一个 AI 团队管理平台。一个入口（飞书），背后是 172 个专业 AI 专家，7×24 小时不间断服务，完全开源，数据自主可控。

参考链接：• Hermes Agent：GitHub - NousResearch/hermes-agent: The agent that grows with you• Agency Agents：GitHub - msitarzewski/agency-agents: A complete AI agency at your fingertips - From frontend wizards

本文基于 Hermes Agent v0.9.0 实际配置编写，所有步骤均经过实测验证。如果你觉得有用，欢迎点赞、收藏、转发！👇
