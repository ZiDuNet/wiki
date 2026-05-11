> 📎 来源: [大刘AI编程](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487599&idx=1&sn=b8f42d07255ad933ff080491f4c2c7be&chksm=9724922babf23aba2ec01be06795ad632d43b64e83a2c6287d0c363e28c70756c2a0d589089d&mpshare=1&scene=1&srcid=0424iV0OsJD193Qxf8Cj8AHo&sharer_shareinfo=ff7ade282b2dd0b905e6907f3e1b9052&sharer_shareinfo_first=ff7ade282b2dd0b905e6907f3e1b9052) | 时间: 2026-04-24 21:29

---

大家好，我是大刘。

这两年“一人公司”（OPC）的概念火得一塌糊涂。

其实说白了，这就是咱们老一代人说的“下海”或者“再就业”的 2.0 AI 增强版。

以前你是单枪匹马，现在你有了一群不拿工资、不交社保、24 小时待命的 AI 员工。

**既然是公司，得有个样子**

为了不让大家听晕，咱们先给技术名词“翻译翻译”：

- **OpenClaw 实例** = 你的办公大楼（硬件基础）。
- **Telegram 机器人** = 员工的办公电话（对外沟通窗口）。
- **独立 Agent** = 你的各个部门员工（SEO、代码、策划）。
- **独立工作区** = 每个人的工位（防止文件弄混，各干各的）。

AI OPC本质上是：**一个 OpenClaw 实例 + 多个 Telegram机器人+ 多个独立 Agent + 多套独立工作区**

今天，大刘手把手教大家用 **OpenClaw** 组建你的第一支 AI 团队。

# 招人：去“人才市场”领员工

想让 AI 给你干活，得先去 Telegram 那里领几个“工号”。

**找 BotFather 谈话**：登录 Telegram 账号，并搜索 

```
@BotFather
```

，它是 Telegram 的“户籍警”。

![](assets/img_09cab65c4366.png)

按提示输入 Bot 名称和用户名（注意：用户名必须以 ’bot‘ 结尾）。

**起个响亮的名字**：比如 

```
lq_SEO_Bot
```

。注意，**名称**是给客户看的，要专业，有辨识度；**用户名**是给程序看的，必须以 

```
bot
```

 结尾。

**拿走 Token**：输入完成后会收到 Token，请妥善保存好勿对外泄露，这就是员工的“入职通知书”，藏好了，一会儿配置要用。

# 装修：给员工安排独立工位

当前OpenClaw目录下只有一个workspace，这个工作区有以下几个文件。

![](assets/img_43f53befef34.png)

因为我们要新建多个agent角色，如果共用同一个目录，记忆、行为、文档必然会互相串扰。

不能让 SEO 专家和开发工程师共用一个文件夹，否则他们的记忆会“串台”，SEO 可能会跑去写代码，开发可能会去研究关键词。

**直接复制目录，一人一个座儿：** 别嫌麻烦，这是防止 AI 产生“人格分裂”的关键。

```
cp -rf workspace workspace_seocp -rf workspace workspace_cxtcp -rf workspace workspace_dev
```

![](assets/img_3da6f56b4d71.png)

# 配置公司的“内部通讯系统”

老规矩修改文件前，先备份

![](assets/img_cc5c64fb38e1.png)

用 vscode 或 Cursor都可以远程连上云服务器， 我们要修改 

```
openclaw.json
```

。

这一步是把电话线接入总机。

## 第一步： 定义员式Agent 名单列表

在 

```
agents.list
```

 里给员工编号（master/dev/seo）

id 是你自己定义的，用来引用不同的 agent，只要对应上就可以。

**大刘提示：** 这个 ID 建议直接跟机器人名称对齐（比如机器人叫 

```
lq_dev_bot
```

，ID 就写 

```
dev
```

）。

虽然你可以乱取名，但相信我，OpenClaw 会记仇的——它可能会在记忆文件里跟你玩捉迷藏，咱们还是别给自己增加“人工降噪”的工作量了。

![](assets/img_0321b13de9da.png)

## 第二步：配置 Telegram 多账户通道

把刚才领到的 Token 填进 

```
channels
```

 里的 

```
telegram
```

 账户 ： 定位如下：

![](assets/img_8c16c3449ba0.png)

修改后：

![](assets/img_510912d3afc3.png)

注意：

```
accounts
```

 里的 key 要和 

```
agents.list
```

 的 

```
id
```

 保持一致（master / dev / cxt / seo），后面 bindings 靠这个 accountId 做路由。

## 第三步：核心路由（Bindings）

这一步是多 Agent 的核心，它决定：**哪个 Telegram Bot 收到的消息，交给哪个 Agent 处理。**

在

```
openclaw.json
```

的根节点，填充以下内容：

```
"bindings": [    { "agentId": "master",    "match": { "channel": "telegram", "accountId": "master" } },    { "agentId": "dev",     "match": { "channel": "telegram", "accountId": "dev" } },    { "agentId": "cxt", "match": { "channel": "telegram", "accountId": "cxt" } },    { "agentId": "seo",     "match": { "channel": "telegram", "accountId": "seo" } }   ]
```

效果如图：

![](assets/img_4209e4daf44c.png)

## 第四步：开启Agent串门功能

定位关键词“tools”，填充如下内容。

```
"agentToAgent": {      "enabled": true,      "allow": ["master", "dev", "cxt", "seo"]    }
```

效果如图：

![](assets/img_0799848e2e9c.png)

**大刘吐槽：** 这一步必须点火！不开的话，你招的不是 6 个员工，而是 6 个老死不相往来的“办公室孤岛”。开了它，他们才会互相发消息、递话。

# 全员集结，准备开业！

## 检查配置是否正常

### 第一步：重启openclaw 网关

```
openclaw gateway restart
```

![](assets/img_af0459fbf234.png)

### 第二步：检查通道状态

```
openclaw channels status --probe
```

![](assets/img_539a50e25664.png)

我们设置的Telegram Agent配置都算正常。

## 私聊

聊天窗口中@用户名，找到我们创建的机器人。

![](assets/img_1e0ae2bd5113.png)

点“start”。

![](assets/img_e1acddca5e6d.png)

![](assets/img_56569a0878c0.png)

复制 openclaw pairing approve telegram xxxxx 到服务器执行。

![](assets/img_cdee5760872c.png)

点对点对话没有问题！

![](assets/img_076de9155dff.png)

## 拉群开会

### 建群拉人

#### 第一步：新建群组

先不要加人，我先起个名称是“大刘OPC”。

![](assets/img_2023d4aba7af.png)

#### 第二步：添加成员

双击左上角

![](assets/img_1f840fb9dc4d.png)

#### 第三步. add机器人

![](assets/img_065aeaf8a05b.png)

![](assets/img_49ab5402135d.png)

全部添加成功！

![](assets/img_01699c66868f.png)

### 群聊配置

**痛点：为什么我 @ 机器人，它装死？**

很多同学配置到这儿发现：机器人进群了，但像个木头人。这时候你需要给它开“天眼”：

#### 1. 关掉 Privacy Mode（群聊必做）

把多个 Bot 拉进同一个 Telegram 群之后，你会注意到每个 Bot 旁边有一行状态说明：

```
has no access to messages
```

意思是Bot 虽然已经在群里，但**无法读取群消息**——人在群里，眼睛是瞎的。

具体步骤如下：

![](assets/img_b0009035512f.png)

点开每个机器人的详情后，再打开“Bot Setting”。

![](assets/img_c789d5d6f0fc.png)

Telegram 的 bot 默认开 Privacy Mode，在群里只能看到 **```
/命令
```** 和 @自己的消息。

这是 Telegram 的“防骚扰保护”，但在咱公司，这就是“上班摸鱼”。

必须关掉，它才能读到群消息。

![](assets/img_242ed0990bdd.png)

##### 2. **打开 Bot to Bot Communication Mode**

这个开关的作用是：允许这个 Bot 与其他 Bot 在群组中通信，让它们在特定场景下能互相看到、响应彼此的消息。对"多 Agent 同群协作"来说，这一项非常关键。

依次将每个机器人的配置，都修改完成后。

**踢了重拉**：这是玄学，也是科学。Telegram 只在机器人进门那一刻读配置。改完不重拉，等于白改

![](assets/img_48036a07c1aa.png)

可以看到重新拉到群里的机器人的状态没有问题了，接下来，测试在群里@机器人情况。

![](assets/img_9ae1dea40e56.png)

##### 3. Telegram用户能@机器人

发现我@机器人还是没有响应，此时需要在 

```
channels.telegram.allowFrom
```

 里写上 Telegram 用户数字 ID。

如果你想让机器人也能@其它机器人，可以加上其它机器人的用户数字id，机器人的用户数字ID就是先前保存的tokent的前半截数字。

![](assets/img_c42057b29122.png)

原理是：当群里，只有你或少数管理员在群里和机器人说话时，只用配置allowFrom就够用了。

![](assets/img_5ef50a00a665.png)

用户数字 ID 怎么找？最简单的办法是搜一个叫 

```
@userinfobot
```

 的机器人，给它发条消息，它会像查户口一样告诉你你的数字身份证。

![](assets/img_02efd610d5c7.png)

检查下效果，OK，至少@机器人没有问题了。

![](assets/img_36061e3fa626.png)

##### 4. 会话可见性

现在我@机器人可以了，但现在依然不能让主Agent@其它机器人。

![](assets/img_dcc1bd0613b5.png)

我们要的是公开透明！所以要在 

```
openclaw.json
```

 里加一行 

```
visibility: "all"
```

。 这就相当于给办公室安了透明玻璃，大家互相能看见在干啥，协作效率直接起飞。

![](assets/img_ac5a0d88defb.png)

原理：在列出/选择会话、向指定会话发消息时，不局限于当前智能体自己那条线，能**看到**系统里其它 agent 的 session，

和 

```
agentToAgent
```

 一起用时，更容易从当前会话定位并写入其它 agent 的会话。

![](assets/img_528bb855a47c.png)

总算有回应了，但他回复了主agent，并没有直接回复我，原理是主agent通过sessions\_send 发消息给其它机器人，其它机器人推送给主agent，主agent再转发给我。

明显这不是我想要的！

##### 5. subagents.allowAgents **双向授权**

每个 agent 都声明了能跟谁通信，比如：

```
"subagents": {"allowAgents": ["dev","master","cxt"]}
```

![](assets/img_a8dec9675f67.png)

重启网关后，在Telegram群里，

![](assets/img_51b2c81eb508.png)

还是依然在采用sessions\_send的方式，回复我。

##### 6. 修改SOUL.md

修改主Agent的SOUL.md文件，追加下面的调度规则。

![](assets/img_a1739a136004.png)

再看看效果，基本满足要求，剩下的，继续微调每个agent的调性了。

![](assets/img_c0ee231e6a62.png)

## 结业致辞：你的 AI 商业帝国已起航

恭喜你，现在你也是有团队的人了。

这种玩法有两种爽法：

1. **私聊单练**：适合让他安安静静帮你改 Bug、审合同。
2. **群聊协作**：适合你当甩手掌柜。你在群里发个需求，看他们几个 AI 自己在那讨论、干活、出结果，那种感觉……真的比带 20 个真人还要爽！

赶紧动手试试吧，别让你的 AI 员工在后台吃灰了！

**如果你在配置过程中遇到了“报错红字”，别慌，评论区留言，大刘帮你远程“人工降噪”。**

![](assets/img_a843559b3821.png)

更多文章：

[如何用 OpenClaw + Obsidian 打造一个“过目不忘”的第二大脑](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487558&idx=1&sn=070435e352c1ebc24d8b8391b416ccc3&scene=21#wechat_redirect)

[拒绝 AI “金鱼脑”：我的 OpenClaw 昨晚做了个梦，醒来变聪明了](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487347&idx=1&sn=753030650d2f565eb87fb30a7c68dba1&scene=21#wechat_redirect)

[OpenClaw 进化论：有了“灵魂”之后，我们要给 AI 找个好工作](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487341&idx=1&sn=689d59dd3956d647c694ba1d433cc556&scene=21#wechat_redirect)

[OpenClaw系列： 小白玩 OpenClaw 动不动就不响应？那是你没给它装上这双“眼睛”](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487329&idx=1&sn=b129a90b6beb8d13cdeddbf1f9904560&scene=21#wechat_redirect)

[OpenClaw系列：大刘教你用 SOUL.md，把冰冷的代码养成“三有青年”](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487313&idx=1&sn=f4122b5ea1483769212f797b72c71e68&scene=21#wechat_redirect)

[保姆级教程，大刘带你从 0 领养 OpenClaw](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487297&idx=1&sn=d9bfa62ffd8793cdf514a6716e5d0d1b&scene=21#wechat_redirect)

[一句话上线：OpenClaw 让部署不再是难事](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487262&idx=1&sn=c41383c9bb62704e7d033574af5852b9&scene=21#wechat_redirect)

[OpenClaw系列：拒绝 FOMO，我是如何调教出有“灵魂”的 AI 写作伙伴](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487178&idx=1&sn=b12701937c24ea4f354d64756c22d0ed&scene=21#wechat_redirect)

[OpenClaw系列二：如何基于 OpenClaw 打造一个永不失忆的 AI 助手？](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487191&idx=1&sn=b398cfd87aaaf06a3eb6e45b0c7e7298&scene=21#wechat_redirect)
