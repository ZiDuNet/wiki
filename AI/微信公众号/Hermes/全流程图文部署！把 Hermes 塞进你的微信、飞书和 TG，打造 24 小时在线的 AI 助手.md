> 📎 来源: [大刘AI编程](https://mp.weixin.qq.com/s?__biz=MzE5ODA5MjY4NA==&mid=2247487542&idx=1&sn=c86b8c3256fb739ade5cd31ed2ce7ac0&chksm=97105fcadd03c3de2eda18ff2716a23a28631689c655453aac0f7d007db12bc0d1b7a99e0cb2&mpshare=1&scene=1&srcid=0418xRJDZU9J71HbNlGa1ry0&sharer_shareinfo=9cec06b8889a92e2aec0ef526f14f1b4&sharer_shareinfo_first=9cec06b8889a92e2aec0ef526f14f1b4) | 时间: 2026-04-18 19:00

---

大家好，我是大刘。

经过前两篇Hermes-Agent的理论学习，我们Hermes为什么会越用越聪明，三层记忆法、Skill 是如何长成，还有他的工具与 MCP 这套“手脚”。

今天带大家三步走：一键安装脚本、多平台授权绑定、最后教你如何调教它的‘记忆’，让Hermes助手成功跑在微信、飞书、Telegram。

正篇开始！

# 一键部署，开启云端大脑

这次我们不用docker方式部署，我直接在云服务器上部署，它的安装方法和本机安装步骤和流程是一样的。

访问官网：https://hermes-agent.nousresearch.com

![](assets/img_5a9a4837e307.png)

我们可以看到安装命令，直接执行

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

开启我们的安装之旅！

![](assets/img_47f857708148.png)

如果你是在一台新机上第一次安装，安装程序会安装一些依赖，差不多10分钟后，到了下面这个界面。

![](assets/img_ca8f3db3edec.png)

## OpenClaw迁移

同一台机器同时安装OpenClaw，Hermes是不会有冲突的。

之前我这台机器安装过OpenClaw，有个助理叫“Open”，安装程序发现了这点，它问我是否要在正式导入数据前先“预览”一下哪些内容会被迁移。

这是选Y，导入所有配置。

![](assets/img_814d5e63f40c.png)

## 配置大模型

接着配置Hermes底层用的大模型，虽然多这台服务器是美国的，但可以选国内版的minimax。

**高能预警**

注意下，在 Linux 终端粘贴 API Key 时，为了安全，屏幕上是**完全不显示字符**的（连星号都没有）。别以为没粘上，点一下右键或按 Ctrl+V 后，大胆按回车就行！

![](assets/img_4992f9c3ce49.png)

![](assets/img_57fc91c64e7e.png)

## 配置传声桶

选择通讯工具，我这里配置三项：

![](assets/img_9e5b8a4f8338.png)

### Telegram

### 第一步：创建机器人，获取token

1. **找到 BotFather** 在 Telegram 的搜索栏输入 

   ```
   @BotFather
   ```

   ，选择带有蓝色认证复选框的官方账号，进去后点击 **Start**。

   ![](assets/img_2c7bed33980a.png)
2. **创建新机器人**

   ![](assets/img_f65da733738e.png)

- 在对话框发送命令：

  ```
  /newbot
  ```
- 设置名称 (Name)：这是显示在对话列表顶部的名称（例如：

  ```
  My Hermes Agent
  ```

  ）。你可以随时修改。
- 设置用户名 (Username)：这是机器人的唯一 ID，必须以 

  ```
  bot
  ```

   结尾（例如：

  ```
  hermes_my_agent_bot
  ```

  ）。这个名称一旦设定不可更改。

3. **获取 Token** 完成上述操作后，BotFather 会发送一条包含 **API Token** 的消息。

- Token 格式通常类似于：

  ```
  123456789:ABCDefhIJKlmNoPQRstUVwxyZ
  ```

  。
- **直接点击** 该字符串即可自动复制。

**小黑板：**

- **不要泄露 Token**：这个 Token 是控制你机器人的唯一凭证。如果别人拿到了它，就可以**完全控制**你的机器人。
- **如果不慎泄露**：可以再次私聊 BotFather，发送 

  ```
  /revoke
  ```

   来作废旧 Token 并生成新的。

### 第二步 配置userId

![](assets/img_488314001e15.png)

在 Telegram 搜索栏搜索 **```
@userinfobot
```** 并点击 **Start**。

![](assets/img_bd08bf36e914.png)

这步有可能因为网络问题，没有响应，重新搜索，进入。

![](assets/img_63d8d8f08dc8.png)

## 飞书

接着配置飞书，按下图一路绿灯，回车。

![](assets/img_0044ff1e5c0b.png)

打开图中的飞书链接，显示如下，不得不说飞书跟进就是快，操作门槛也越来越低。 可以选择新建，也可以选择已有机器人。

给飞书点个赞！

![](assets/img_c6142d5fd261.png)

## 微信

Hermes现在已经支持接入个人微信，打开链接，手机扫码。

方便倒是方便，但我发现一个微信只能接入一个Hermes，多了不能接，有点遗憾。

个人微信接入 Agent 有违规风险，建议小白先用小号测试，或者主推 Telegram/飞书，保护账号安全。

![](assets/img_35c3c782b044.png)

选推荐模式，这个选项是说当有人第一次私聊机器人时，系统会生成一个配对请求，需要你手动确认后才能开始对话。这就像是“加好友验证”，安全性最高且灵活。

![](assets/img_00b53410d835.png)

特定的工作群或技术交流群需要机器人提供服务，或者拒绝所有群聊天。如果没有想好，后面再单独配置。

![](assets/img_c52973e8e6af.png)

## 网关运行模式

仔细看我下图的解释，因为这次安装是在云服务器上的，所以我选System service模式。

![](assets/img_100217b7dbdd.png)

![](assets/img_6500064bc03c.png)

![](assets/img_0e4f95d98e3f.png)

## 安装完成

![](assets/img_a6bd46659b6e.png)

![](assets/img_07a259c233a0.png)

到了这一步，我们可以和从OpenClaw迁移过来

```
Open
```

聊天对话了。

退出后提示安装成功，并给了一些帮助命令，到这一步，是走完了安装流程。

![](assets/img_b7347829333f.png)

## 测试下通讯是否正常

### Telegram

找到机器人，沟通是否顺畅。

![](assets/img_39ef409353f4.png)

![](assets/img_5c266183952c.png)

## 微信

![](assets/img_98df6463ac2f.png)

复制好友申请，到服务器上执行。

![](assets/img_bfacaf378b53.png)

![](assets/img_d8deac22932b.png)

## 飞书

![](assets/img_006f2d54085a.png)

在飞书这，遇到问题，一直没有响应。

用本地Cursor连接云端服务器，查看下hermes有关飞书的配置，提示没有配置成功。

如果你跟我一样在飞书配置上卡住了，别慌，我用 Cursor 连上服务器后台瞄了一眼才发现问题。怎么连服务器？看我这篇保姆级教程： https://mp.weixin.qq.com/s/mcqVQ9dAZRwpSvUYxt-leQ

![](assets/img_4b82e31c0f5a.png)

看配置文件的核心就是看 

```
config.yaml
```

 里的 

```
feishu
```

 段落有没有被正确填充。

我们执行hermes gateway setup，重新配置下，可能当时配置飞书时，少操作了？

![](assets/img_bb781936bf79.png)

![](assets/img_163b988d481c.png)

# 配置讲解

安装完是“肉体”成了，后面的配置是注入“灵魂”。

Hermes的设计思路是能省则省，一个config.yaml搞定所有事，不搞分散的环境变量和多层配置文件，核心配置都在一个文件里： ~/.hermes/config.yaml 。

主要文件或目录的作用，可以看下图：

![](assets/img_5fa818d802c1.png)

## skill && mcp

相信我们在使用过程中会发现skill和mcp的功能会发生重叠，此时该优先选哪个呢？

![](assets/img_89ef35ac17e0.png)

Hermes自带40多个工具，MCP又能接入几千个。怎么选？

![](assets/img_1acdb15a8fa7.png)

一个简单的判断标准：

如果Hermes已经内置了这个能力，用内置的；

如果需要和外部服务交互，用MCP。

逻辑（怎么干）写 Skill，触手（连哪里）找 MCP。

![](assets/img_23932a40922a.png)

**重要经验**：刚开始别一次性接入太多MCP Server。

先接一两个最常用的（GitHub、数据库），用熟了再加。每多一个 Server，工具选择空间大一圈，决策路径也变长。

MCP解决“能连什么”，Skill解决“怎么用”。两者配合效果更好。

---

# 最后多说两句

Claude Code，OpenClaw，Hermes 他们并不互斥。

一个典型的重度用户完全可以用 Claude Code 写代码，OpenClaw 处理跨平台的自动化流，Hermes 在后台跑那些不需要人盯着的长任务。

它们代表的是三种不同的人机关系，而不是同一个市场里的竞争者。

- **Claude Code**：你的“首席程序员”（盯着屏幕敲代码）。
- **OpenClaw**：你的“全能管家”（处理复杂的跨应用审批流）。
- **Hermes**：你的“数字分身”（在后台、在群里，随时待命响应）。

未来三者的底层设计，有很大概率会趋同一致，鹿死谁手，不得而知！

![](assets/img_3ee4b9c27712.png)

将Hermes装起来只是第一步，怎么让它帮你干活才是真本事。

下一期讲从零开始，手把手教你给 Hermes 完成一个任务。

想让它帮你查资料、调代码、自动回消息的，密切关注。

觉得有用，点个”在看“，转发一下，咱们下期见。

![](assets/img_1f2ccb13be6f.png)
