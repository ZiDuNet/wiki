> 📎 来源: [奇思妙想味道](https://mp.weixin.qq.com/s?__biz=MzAxNDc4ODk0OQ==&mid=2247483768&idx=1&sn=81ea2bf87a6886d3de3e64ce9e99b519&chksm=9a643752b63749d949561053c2aa88b47934ec943d185e081be1d8ee1eb1a90ec1c83887ff70&mpshare=1&scene=1&srcid=04204O6bTD7b8XdAWDYrmSVr&sharer_shareinfo=b4a9b7ff59fc17372441f8e3c844c8d0&sharer_shareinfo_first=b4a9b7ff59fc17372441f8e3c844c8d0) | 时间: 2026-04-20 20:43

---

之前有人靠安装龙虾（OpenClaw）提车，现在更牛的来了——Hermes Agent，堪称“龙虾Pro Max”！

它比龙虾更稳定、更省钱，自带自动进化buff，不用手动折腾就能越用越好用。

话不多说，从新手入门到高手精通，全程实操无废话，跟着做就能上手，看完直接解锁AI Agent变现新姿势👇

## 第一阶段：新手入门（10分钟上手，完成首次对话）

核心目标：让Hermes成功跑起来，搞定基础配置，实现第一次AI对话。先搞懂3个核心概念，避免走弯路：

- **记忆**：跨会话记住你的偏好、项目上下文，不用每次都重复说明
- **技能（Skill）**：完成任务后自动总结经验，生成可复用技能，省token又高效
- **网关系统**：一个网关打通15+通讯平台，随时随地调用AI

### 实操步骤（超简单，复制命令就能装）

#### 1. 一键安装Hermes

✅ macOS/Linux/WSL2用户（直接复制命令，终端执行）：

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

✅ Windows用户：先安装WSL2，再在WSL2终端执行上面的命令（无WSL2的话，先搜“WSL2安装教程”，5分钟搞定）。

安装时会自动处理所有依赖（Python、Node.js、Git等），自动创建配置目录、设置环境变量，不用手动操作！

#### 2. 验证安装（必做）

安装完成后，执行以下命令，确保Hermes能正常运行：

```
source ~/.bashrc  # zsh用户执行：source ~/.zshrc
```

#### 3. 配置模型供应商（新手必看）

安装完成后，系统会自动进入配置向导，按以下步骤来：

1. 选择「Quick Setup」（新手推荐，省去复杂配置）
2. 选择模型供应商：优先选Deepseek、Kimi等国产大模型（免费额度高，适合新手试错）
3. 测试首次对话，验证配置成功：

```
hermes chat -q "Hello! What tools do you have available?"
```

有正常回复，就说明安装+配置全部搞定！

#### 新手常用命令（收藏，避免反复找）

- hermes → 开启交互式对话（核心命令）
- hermes model → 切换模型供应商/模型
- hermes tools → 配置启用的工具集
- hermes gateway → 启动消息网关
- hermes update → 更新Hermes到最新版本
- hermes doctor → 遇到问题，先执行这个诊断

## 第二阶段：中级进阶（让Hermes真正“有用”，接入多平台）

核心目标：打通常用通讯平台，激活Hermes核心功能，让它从“能运行”变成“能干活”。先深度理解2个核心机制：

### 核心机制拆解

#### 1. Skill系统（Hermes最牛特性）

完成复杂任务后，Hermes会自动总结经验，生成可复用的Skill，下次做同类任务直接调用，省时间、省token。

触发Skill创建的3个时机：

- 完成多步骤任务后（比如抓取网页+总结）
- 手动要求“创建技能”
- 跨会话重复某种工作模式时

查看已有技能：`
`

```
ls ~/.hermes/skills/
```

#### 2. 消息网关（随时随地调用Hermes）

一个网关就能接入Telegram、飞书、钉钉等15+平台，手机、电脑都能调用，不用一直开终端。

### 5个实操任务（必做，验收即达标）

#### 任务1：接入Telegram机器人（最常用）

1. 在Telegram搜索@BotFather，发送/newbot创建新机器人，获取Bot Token
2. 配置Hermes（二选一）：

```
# 方式1：命令配置hermes config set TELEGRAM_BOT_TOKEN your-bot-token# 方式2：手动编辑配置文件（~/.hermes/config.yaml）gateway:  adapters:    telegram:      enabled: true
```

3. 启动网关：`
`

```
hermes gateway
```

4. 在Telegram向机器人发送/start，能响应即成功。

#### 任务2：接入飞书/钉钉机器人

✅ 飞书：执行`
`

```
hermes gateway setup
```

`按指引选择飞书，一步步配置即可；`

✅ 钉钉：手动编辑

```
~/.hermes/config.yaml
```

添加以下内容：

```
gateway:
```

#### 任务3：配置常用工具集

执行`hermes tools`，启用至少3个常用工具（推荐）：

- filesystem（文件读写）
- web\_search（互联网搜索）
- firecrawl（网页抓取）

#### 任务4：测试记忆功能

1. 执行`hermes`，告诉它你的偏好（比如“我叫XX，喜欢用中文交流”）
2. 输入exit退出对话，重新执行`hermes chat`
3. 问它“你知道我是谁吗？”，能说出你的名字即正常。

#### 任务5：触发Skill创建

执行`hermes chat`，输入指令：“帮我抓取Hacker News首页的AI新闻，并总结成中文摘要发给我”，完成后会提示创建Skill，点击确认即可。

#### 中级验收标准（达标即进入高手阶段）

- Telegram/飞书机器人能正常响应消息
- 启用至少3个常用工具
- 跨会话记忆功能正常
- 成功触发1次Skill创建

## 第三阶段：高手精通（构建自进化闭环，实现自动化变现）

核心目标：让Hermes实现7×24小时自动化工作，搭建多Agent协同，真正解放双手，甚至用来接单变现。先搞懂3个高级机制：

### 高级机制拆解

- **MCP集成**：连接外部工具（数据库、GitHub、自定义API），扩展Hermes能力
- **多Agent编排**：创建多个子Agent，分工协作（比如调研、写作、校对）
- **Cron定时任务**：自动执行日报、备份、新闻推送等任务，无需手动操作

### 5个高手实操任务（解锁自动化能力）

#### 任务1：MCP扩展集成（必做）

1. 安装MCP扩展：

```
uv pip install -e ".[mcp]"
```

2. 配置MCP服务器（编辑~/.hermes/config.yaml）：

```
mcp:
```

3. 测试调用：在对话中输入“读取我GitHub上的最新Issue，并总结给我”，能正常返回即成功。

#### 任务2：搭建定时自动化任务

以“每天早上9点，发送AI新闻摘要到Telegram”为例：

1. 编辑~/.hermes/cron/tasks.yaml：

```
tasks:
```

2. 查看定时任务：`ls ~/.hermes/cron/`

#### 任务3：多Agent编排（高效协作）

执行`hermes chat`，输入指令：“创建一个调研Agent负责收集信息，一个写作Agent负责整理成文，一个校对Agent负责检查错误”，Hermes会自动创建子Agent协同工作。

也可以手动配置（编辑~/.hermes/config.yaml）：

```
agents:
```

#### 任务4：高级配置与安全

- 配置Docker隔离模式（更安全）：`hermes config set terminal.backend docker`
- 数据备份（防止配置丢失）：

```
tar -czvf hermes-backup.tar.gz ~/.hermes/
```

#### 任务5：性能优化

- 监控日志：`tail -f ~/.hermes/logs/hermes.log`
- 预热模型（提升启动速度）：`hermes model warmup`
- 限制资源（Docker运行）：

```
docker run -d \
```

#### 高手验收标准

- MCP扩展正常集成（至少连接1个外部服务）
- Cron定时任务能自动执行
- 多Agent协作正常
- 掌握数据备份与安全配置
- 能修改config.yaml进行高级配置

## 常见问题与解决方案（新手必看，避坑！）

- 问题1：hermes: command not found → 解决方案：执行`source ~/.bashrc`，或检查PATH配置
- 问题2：API密钥未设置 → 解决方案：执行`hermes model`重新配置
- 问题3：Windows无法安装 → 解决方案：必须先安装WSL2，再执行安装命令
- 问题4：机器人无响应 → 解决方案：检查网关是否运行（`hermes gateway`）
- 问题5：更新后配置丢失 → 解决方案：执行`hermes config check`，再执行`hermes config migrate`

💡 提示：遇到任何问题，先执行`hermes doctor`，会自动诊断并给出解决方案！

## 学习资源汇总（收藏，随时查阅）

### 官方资源

- GitHub仓库：https://github.com/nousresearch/hermes-agent
- 官网：https://hermes-agent.nousresearch.com/
- 官方文档：https://hermes-agent.nousresearch.com/docs/

### 社区资源

- 菜鸟教程：https://www.runoob.com/ai-agent/hermes-agent.html
- 橙皮书（花叔）：https://www.huasheng.ai/orange-books/hermes-agent/

最后说一句：Hermes不是简单的AI工具，而是能自动进化的“数字员工”。从新手入门到高手精通，跟着这篇教程一步步做，既能解放自己的双手，也能解锁变现新路径——毕竟，早一步掌握，就早一步抢占AI Agent的红利！

收藏这篇教程，跟着实操，下次别人问起Hermes，你就是那个“懂行的人”～
