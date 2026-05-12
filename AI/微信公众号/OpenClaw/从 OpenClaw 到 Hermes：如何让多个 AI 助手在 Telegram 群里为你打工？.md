> 📎 来源: [大刘AI编程](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487634&idx=1&sn=e8d8bb0d57141082a3425d125f90a747&chksm=97cca56bbe0bf0bb254ef3f5d07acbe9b85bfdf581d168f360b2544cdaf31eb183bdba25d526&mpshare=1&scene=1&srcid=0427R7DqTbc6GweQFSAE5B7e&sharer_shareinfo=6720374a2c1b4c2b52192eb969cf6fe3&sharer_shareinfo_first=6720374a2c1b4c2b52192eb969cf6fe3) | 时间: 2026-04-27 18:50

---

大家好，我是大刘。

之前咱们玩 AI，大多是把它当个“加强版搜索聊天框”。但随着 Hermes 这种 Agent 框架的成熟，玩法变了——**我们不再是调教一个 AI，而是要像带团队一样，指挥一群 AI。**

想象一下：一个 Agent 埋头写代码，另一个 Agent 负责评审找 Bug，你只需要在群里发号施令。

今天，我就手把手把这个“一人团队”组建起来。

# OpenClaw配置迁移

前文[全流程图文部署！把 Hermes 塞进你的微信、飞书和 TG，打造 24 小时在线的 AI 助手](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487542&idx=1&sn=c86b8c3256fb739ade5cd31ed2ce7ac0&scene=21#wechat_redirect)已经详细讲解了具体的安装步骤了。

如果你之前在同一台机器跑过 OpenClaw，那么一条命令平迁：

```
hermes claw migrate --dry-run     # 先预览，看迁什么hermes claw migrate               # 确认后执行
```

![](assets/img_779efaad4fb2.png)

会把 

```
~/.openclaw/
```

 下的配置全部迁到 

```
~/.hermes/
```

，冲突默认 skip。

迁移完之后，习惯性动作是跑一下 

```
hermes doctor
```

 检查身体。

```
hermes doctor
```

![](assets/img_3192cc078b22.png)

按照提示执行：

```
hermes doctor --fix
```

![](assets/img_b6d156f20c99.png)

此时还报MiniMax不通？

![](assets/img_aabe19895344.png)

执行

```
hermes
```

，我看正常对话是没有问题的，这是怎么回事？

![](assets/img_d1dfc4ff55f6.png)

这里有个**大坑**：你可能会看到 MiniMax 报 404 错误。

别慌！我去翻了下源码，发现这只是 

```
doctor
```

 的检测逻辑太“死板”——它用 

```
v1/models
```

 接口去探测联网，而国内很多站点不提供这个路径。

**一句话：只要你能正常聊天，这个错就当它不存在。** 就像体检中心查视力用的是 E 字表，虽然医生说你“看不见”，但只要你能顺畅写代码，这双眼睛就是好使的。

我**提供一些常用命令**如下：

### 1. 直接配置模型

随时随地换“脑子”（切换模型）

```
hermes model
```

如果配置好模型，可以在hermes界面中通过

```
/model
```

切换模型，还能在对话里随时切，对话测试！

![](assets/img_d7350ca7643a.png)

## 2. gateway相关配置

### 1. 配置gateway

```
hermes gateway setup
```

![](assets/img_a0f9190bb88c.png)

### 2. 查看gateway状态

看看你的机器人“联网”没。

```
hermes gateway status
```

### 3. 看日志方法

查看它在后台偷摸干啥（日志）。

```
journalctl --user -u hermes-gateway -f       # Linuxtail -f ~/.hermes/logs/gateway.log           # macOS
```

# 接入Telegram

## 第一步：新建机器人

去 BotFather 开一个 bot，具体步骤可以参见我上篇文章 [不想带人？那就带AI！大刘教你用 OpenClaw 攒出第一支 AI 员工团队](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487599&idx=1&sn=b8f42d07255ad933ff080491f4c2c7be&scene=21#wechat_redirect)

## 第二步：机器人配置

### 1. **允许其他 Bot 向你的 Bot 发送消息**

Telegram 搜 **@BotFather**：后 执行

```
/setbot2bot
```

，开启通道开关。

**使用场景：**

- 构建 Bot 之间的联动（比如 Bot A 转发消息给 Bot B）
- 多 Bot 协作工作流
- API 服务间的 Bot 通信

![](assets/img_9893006ec962.png)

### 2. 关掉 Privacy Mode（群聊必做）

在群聊场景下，**关闭 Privacy Mode（隐私模式）是必做动作。** 否则你的机器人就是个“小聋人”。

BotFather → 

```
/mybots
```

 → 选你的 bot → **Bot Settings → Group Privacy → Turn off**。

![](assets/img_b7a64832f0d1.png)

**注意**：

如果你是拉了群才想起去改设置，**一定要记得把 bot 先踢出去再重新拉回来！** Telegram 只有在进群的那一瞬间会读取状态，之后你改得再勤快，它也假装看不见。

替代方案：把 bot 设为群管理员，admin 自动无视 Privacy Mode。

### 3. 设置一个消息主频道

/sethome 是 Hermes Gateway 的一个 slash 命令，它是“指挥中心”，所有的通知都会汇总到这里，方便管理。

**它的核心作用：设置消息接收地址**

选择某个机器人，执行 /sethome 后，这个 Telegram 对话就成了你的"主频道"，用来接收：

1. **Cron 定时任务的结果** — 你设置的定时任务完成后，结果会发到这里
2. **跨平台消息** — 从其他平台（Discord、Slack 等）转发过来的消息

![](assets/img_0b40a03dff0b.png)

# 多 Agent 与 Bot-to-Bot 群聊跑通

之前以为Hermes就是一个单Agent体，不像OpenClaw支持多智能体，但最近发现也是支持的。

Hermes 最让我惊喜的是它的 

```
profile
```

 功能。简单理解，它就是“**平行宇宙**” 。

默认的 

```
~/.hermes/
```

 是你的主 Agent，而通过 

```
hermes profile create
```

，你可以克隆出无数个性格各异、技能不同的分身。

每个分身都有一个独立的 HERMES\_HOME 目录，包含：

```
~/.hermes/profiles//├── config.yaml      # 配置文件├── .env             # API 密钥├── SOUL.md          # AI 个性配置├── memories/        # 记忆├── sessions/        # 对话历史├── skills/          # 技能├── cron/            # 定时任务├── gateway/         # 网关配置├── logs/            # 日志├── workspace/       # 工作区└── ...
```

每个分身都有独立的“记忆、灵魂和钱包（API Key）”，互不干扰，这才是组建团队的基石。

看到这一堆文件夹别眼花，其实你平时只需要动 

```
SOUL.md
```

（改性格）和 

```
.env
```

（换 Key），其他的交给系统自动打理就行。

### 1. 创建profile

让我们通过命令 

```
hermes profile create
```

 可以创建一个全新的开发 Agent。

更多使用技巧，可以使用hermes帮助或者直接在Telegram的机器人会话中问。

![](assets/img_d80481147f93.png)

执行命令

```
hermes profile create dev --clone # 克隆默认 profile 的 config.yaml（只拷配置）
```

效果如下：

![](assets/img_4c01002e79e6.png)

更多有关profile命令如下：

```
hermes profile list                      # 列所有 profile + 状态hermes profile show dev                 # 单个详情（gateway 状态、路径、大小）hermes profile rename dev dev-writer   # 改名hermes profile export dev               # 打包成 mobi.tar.gz（搬家/备份）hermes profile import dev.tar.gz        # 从 tarball 还原hermes profile delete dev               # 删除（需再输一次名字确认，或加 --yes）hermes profile use dev                  # ⭐ 设粘性默认：此后光秃秃的 `hermes` 自动走
```

## 2. 创建机器人团队成员

重复按照上节接入一个Telegram机器人dev后，执行

```
hermes -p dev gateway setup
```

接下来按照提示完成连接Telegram，填入dev\_bot的token，安装重启gateway!

![](assets/img_bf17cb4f7d19.png)

看下效果，已经能正常对话。

![](assets/img_46aa23fe96dd.png)

到这一步，我们在云服务器的同一步

```
~/.hermes
```

目录下，生成了两个agent，并分别配对了两个机器人。

并能正常聊天。

接下来如法炮制，新增机器人cxt。

## 3. 建群测试

每个 agent 的 config.yaml：

> 主 agent 在 

> ```
> ~/.hermes/config.yaml
> ```

> 子 agent 在 

> ```
> ~/.hermes/profiles//config.yaml
> ```

加一行：

```
require_mention: true
```

当启用这个命令后，在群组里机器人只回复 @ 他人，不会响应群聊中的普通消息，避免 bot 在大群里"乱插嘴"。

这个属性是解决**我什么时候响应**（触发方式）！

![](assets/img_2c6d60141818.png)

让我们来测试下：

在master聊天窗口里私聊，要求master在群里发起聊天。

![](assets/img_fe7f035c3a73.png)

dev回应他了。

![](assets/img_6b45677f9e85.png)

## 千万别在白名单里乱加人！

之前我为了省事，把所有机器人的 ID 都塞进了 

```
.env
```

 里的 

```
TELEGRAM_ALLOWED_USERS
```

。

![](assets/img_79a03fe83ad4.png)

它是 Telegram 的**白名单配置**，是解决**谁能跟我说话**的问题（用户白名单）。

结果好家伙，三个机器人在群里自己聊上了，而且越聊越嗨，停都停不下来！

![](assets/img_11e1991ae664.png)

那场面，简直是“**数字生命在狂欢，我的余额在惨叫**”。

原理很简单：如果你把 Bot B 的 ID 塞进了 Bot A 的白名单，Bot A 就会把 Bot B 的发言当成‘主人的指令’去回复。结果就是 A 撩 B，B 撩 A，无穷匮也。

所以，白名单里记得只留你自己的 ID。

如果发现它们聊疯了，赶紧撤回修改，用 

```
hermes gateway restart
```

 物理降温。

```
hermes gateway restarthermes -p cxt  gateway restarthermes -p dev gateway restart
```

# 结语：从“写代码”到“带团队”

写了近 20 年代码，有一个最大的感触是：**个人的体力总有上限，但系统的杠杆没有。**

以前我们靠编程提升效率，那是“技术杠杆”；现在做独立开发，我思考的是如何把自己的逻辑“分身”给不同的 Agent，这就是 Hermes 给我们提供的 **“AI 杠杆”**。

组建这个 AI 团队，最终目的是为了把我们从那些繁琐的配置、重复的初稿、基础的代码中解放出来。

省下的时间干嘛？去盯着更有价值的事：**市场在哪里？需求在哪里？**

毕竟，技术只是路径，拿到结果才是终点。

如果你在配置过程中遇到了搞不定的坑，或者也想聊聊“如何用 AI 挖出金矿需求”，欢迎来我的个人群。

这里没什么高大上的理论，只聊怎么用最土、最有效的工具，帮普通人真正跨过编程这道门槛。

下一篇 我来展示 多个Agent是如何协作实现一个复杂任务的，有兴趣的可以关注我。

![](assets/img_d1551956d760.png)

更多文章：

[全流程图文部署！把 Hermes 塞进你的微信、飞书和 TG，打造 24 小时在线的 AI 助手](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487542&idx=1&sn=c86b8c3256fb739ade5cd31ed2ce7ac0&scene=21#wechat_redirect)

[8.7万星神作！Hermes Agent 深度拆解（下）：从“金鱼脑”到“神助攻”，他的手脚和大脑是怎么长的？](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487384&idx=1&sn=2bd2eb1ee7a2675dc02acd654efd9b20&scene=21#wechat_redirect)

[8.7万星神作！Hermes Agent 深度拆解（上）：像职场精英一样自动进化](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487371&idx=1&sn=b4e9c4f48e4d502cd80ddcfa09b57d05&scene=21#wechat_redirect)

[别再死磕 OpenClaw 了！我为什么劝你转战 Hermes？](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487366&idx=1&sn=1f90bb86d959ce1a169c2070b908418c&scene=21#wechat_redirect)
