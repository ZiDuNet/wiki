> 📎 来源: [大飞象的智能体2025](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247486498&idx=1&sn=60f258921cf4eaee0d52488f717daa72&chksm=c398fded45741d95620686364b9d93de479448df6ee505aa6519e9a82e24138ad4970df11931&mpshare=1&scene=1&srcid=0420jmw2mo6RypfZJWSv9wE8&sharer_shareinfo=63299185dc0c6a813d1aa5ab0db5b88b&sharer_shareinfo_first=63299185dc0c6a813d1aa5ab0db5b88b) | 时间: 2026-04-20 19:10

---

**导语**：OpenClaw之后，2026年最火的AI Agent是谁？答案是Hermes Agent——一个能自我进化、越用越聪明的"数字员工"。本文将从安装部署到进阶玩法，手把手教你打造专属AI助理。

## 一、Hermes Agent是什么？为什么它这么火？

### 核心定位

Hermes Agent是由Nous Research开源的自主AI智能体框架，采用MIT开源协议。它不是普通聊天机器人，而是具备**自进化、持久记忆、多工具调用、多平台接入**能力的"数字员工"。

**一句话概括**：OpenClaw是你配置它，Hermes是它学习你。 

### 核心能力

**自进化技能系统**：完成任务后自动提炼流程，生成可复用技能并持续优化

**四级持久记忆**：L1核心记忆、L2用户画像、L3历史搜索、L4技能记忆

**多工具并行调用**：终端执行、文件读写、浏览器自动化、定时任务

**多平台统一网关**：Telegram、飞书、钉钉、企业微信等15+平台

**灵活部署**：本地、云端、Docker容器化全支持

### 为什么它这么火？

 1. **踩中OpenClaw痛点**：记忆丢失率高、技能需手动维护、CVE漏洞频发
 2. **一键迁移**：hermes claw migrate 5分钟完成数据迁移
 3. **越用越聪明**：用得越久，能力越强，真正实现"成长型AI助理" 

## 二、环境准备：安装前必查

### 系统支持

• Linux (Ubuntu/Debian/CentOS)：✅ 完全支持（官方推荐）

• macOS (Intel/Apple Silicon)：✅ 完全支持

• Windows：⚠️ 需安装WSL2（不支持原生）

• Android：✅ Termux环境可运行

### 硬件要求

• **最低配置**：1核1GB内存（配合外部大模型API）

• **推荐配置**：4GB+内存，2核CPU

• **本地运行模型**：16GB+显存

## 三、安装部署：三种方式任选

### 方式一：官方脚本一键安装（推荐）

 # Linux/macOS/WSL2
 curl -fsSL https://hermes-agent.org/install.sh | bash

 # 安装完成后初始化
 hermes init 

### 方式二：Docker部署

 docker run -d \
   --name hermes-agent \
   --restart unless-stopped \
   -v ~/.hermes:/root/.hermes \
   -p 3000:3000 \
   -e HERMES\_MODEL\_PROVIDER=deepseek \
   -e HERMES\_API\_KEY=your-api-key \
   nousresearch/hermes-agent:latest 

### 方式三：阿里云一键部署

1. 登录阿里云控制台

2. 选择轻量应用服务器

3. 应用镜像选择"Hermes Agent"

4. 配置百炼API Key

5. 等待部署完成（约2分钟）

## 四、模型配置：对接大模型

### 支持的模型提供商

 • DeepSeek：¥1/百万tokens
 • MiniMax：¥0.3/百万tokens
 • 阿里云百炼：按量计费
 • OpenAI：$0.002/1K tokens
 • Claude：$0.003/1K tokens
 • 本地Ollama：免费 

### 密钥管理建议

**不要把API密钥写进config.yaml！**

 所有敏感配置放进环境变量文件：
 ~/.hermes/.env 

## 五、快速上手：从第一次对话开始

### 验证安装

 hermes doctor 

### 启动对话

 hermes 

### 常用斜杠命令

• /help：查看帮助

• /model：切换模型

• /clear：清空当前对话

• /memory：查看记忆状态

• /skills：查看已安装技能

• /exit：退出对话

## 六、记忆系统：让AI真正"记住"你

### 四级记忆架构

**L1：核心记忆（MEMORY.md）**
 位置：~/.hermes/memories/MEMORY.md
 容量：约800 tokens
 内容：环境事实、项目约定、经验教训 

**L2：用户画像（USER.md）**
 位置：~/.hermes/memories/USER.md
 容量：约500 tokens
 内容：用户偏好、沟通风格、工作习惯 

**L3：历史搜索（SQLite + FTS5）**
 存储：所有历史会话、工具执行日志
 功能：跨会话语义/关键词检索 

**L4：技能记忆（Skills）**
 位置：~/.hermes/skills/
 内容：自动生成的可复用工作流 

### 记忆自动写入机制

• 每10个turn自动触发反思

• 任务完成后自动提炼经验

• 调用5次+工具自动生成技能

## 七、多平台接入：一处部署，多端使用

### 支持的平台

Telegram、Discord、WhatsApp、Signal、飞书、钉钉、企业微信、QQ等15+平台。

### 配置飞书

 hermes platform add feishu
 hermes platform configure feishu \
   --app-id=your-app-id \
   --app-secret=your-app-secret 

### 启动网关

 hermes start --daemon 

## 八、从OpenClaw迁移：一行命令搞定

如果你之前使用OpenClaw，可以一键迁移所有数据：

 hermes claw migrate 

**迁移内容**：
 • 设置配置
 • 记忆文件
 • 技能库
 • API密钥

 整个过程约5分钟，数据无缝迁移。 

## 九、总结：从入门到精通的三个阶段

**阶段一：能运行**
 • 完成安装部署
 • 配置模型API
 • 完成第一次对话 

**阶段二：能工作**
 • 配置多平台接入
 • 学会记忆管理
 • 掌握常用命令 

**阶段三：能进化**
 • 技能自动生成
 • 工作流沉淀
 • 个性化定制 

**Hermes Agent的核心价值**：不是简单的对话工具，而是能从使用中学习、越用越聪明的"成长型AI助理"。

 装好只是第一步，真正用起来，你会发现它越来越懂你。 

---

![](assets/img_32c5d90b1849.jpg)

![](assets/img_fa8f8ce0f960.jpg)

更多阅读：

[越用越聪明的AI：Hermes四级记忆架构深度解析](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247486493&idx=1&sn=3584b2901d085c0a070f9378ce4a0273&scene=21#wechat_redirect)

[腾讯QClaw实测：微信直连AI，三分钟上手](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247485510&idx=1&sn=61ed4e993e5fea6c569e6ac0629bf1cd&scene=21#wechat_redirect)

[OpenClaw性能调优：让AI跑得更快](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247486004&idx=1&sn=0d5cf7bad04fb8b3a1e4f2f2ec60e814&scene=21#wechat_redirect)

[关于微信接入OpenClaw的10条冷思考](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247486348&idx=1&sn=c59d82970a81fcc1468191311bf341a3&scene=21#wechat_redirect)

[Token演变为智能经济的"新大宗商品"，中国正构建"Token+人民币"世界经济新体系](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247486475&idx=1&sn=5574dc3e980a18917821a2da03093c97&scene=21#wechat_redirect)

本文首发于公众号，作者：象哥
