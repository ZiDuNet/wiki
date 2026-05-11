> 📎 来源: [Draco正在VibeCoding](https://mp.weixin.qq.com/s?__biz=MzI2NzM4MTQwMg==&mid=2247495822&idx=1&sn=d58fd93900538bf09db4b17a777f300b&chksm=ebd9c2c70c8cc3862d6d18876a2fd0024616b5a72d7752c2af0ec423737135b54fba1a1fc623&mpshare=1&scene=1&srcid=0421QUT1ckCxO5AAADrP60cd&sharer_shareinfo=1bd6d4c87de85a2818a506b10649634e&sharer_shareinfo_first=1bd6d4c87de85a2818a506b10649634e) | 时间: 2026-04-21 22:53

---

本来都不打算写Hermes保姆教程了，无奈我之前似乎无意间立了个“专写万字保姆教程”的人设，有N多同学在后台和微信里私信问保姆教程咋还没写😂，那...就今天补上！（结尾有彩蛋）

---

## 一、前置条件

### 本地Mac/Linux/Windows WSL2

或

### 腾讯云主机一台：

•

轻量应用服务器Lighthouse，自带流量和带宽，对绝大多数新手来说性价比友好；

•

2核4G或以上配置；

•

https://buy.cloud.tencent.com/lighthouse  新手推荐选择入门型2核4G配置：

![](assets/img_a1730f3688d5.png)

•

登录方式推荐SSH（密钥配对方式，需要创建并保存一个.pem密钥文件，请一定记住该文件的保存位置，后续会经常用到）

•

Ubuntu镜像（用户名默认ubuntu）；

•

海外节点（新加坡、曼谷、东京、首尔都可以）

![](assets/img_def2fda928a4.png)

•

备注： 

•

其他云厂商（阿里云、火山引擎甚至AWS）的云主机皆可，我只是自己用惯了腾讯云，所以本文中皆以腾讯云示例；

•

也可以是MacOS、Linux、Windows WSL2等本地电脑，这种情况会省去Remote-SSH相关的配置；

•

但我强烈推荐海外节点云主机的方式来部署Hermes Agent，理由如下： 

1.

下载各种依赖库、Github仓库、Docker Hub镜像等速度快很多（无须魔法）；

2.

在哪里都可以访问；

3.

大的云厂商机房的SLA肯定要比在家里摆一台Mac Mini要稳得多......

4.

使用DNS配置公网域名更简便，随时随地在手机上可以vibe一个你自己域名下的网站出来；

### 大模型推荐：KIMI K2.6

上周KIMI的Coding Plan全量推送了K2.6-code-preview，所以我已经使用K2.6一周多时间了。我有4个Hermes Agent，其中3个跑在K2.6上，一个跑在GPT-5.4上，在Hermes Agent上的体验KIMI K2.6和GPT-5.4可以打的有来有回！并且，由于GPT-5.4说话又臭又长还满嘴“黑话”，而KIMI K2.6说话比较简洁，我甚至更喜欢和K2.6搭伙干活儿。

刚好，KIMI昨晚正式发布了KIMI K2.6～

> https://mp.weixin.qq.com/s/6jfSSCcq7HMg-qXrsc4OVg

![](assets/img_07d611266d5d.png)

•

更强的长程编码能力

•

更强前端设计和编排能力

•

和Hermes/OpenClaw等更匹配的自主Agent协同能力

从KIMI官宣改进方向、benchmark以及Hermes官方（NOUS Research）的comments上看，的确和我的使用体感非常match！

![](assets/img_f9d1ad1236bd.png)

![](assets/img_b67373d31413.png)

此外，KIMI家的KIMI Code非常适合作为Hermes（或OpenClaw）的陪跑Agent，后文详述。

![](assets/img_77d98d62085f.png)

### 如果你选择云主机，请配置好VS Code的Remote-SSH

•

使用VS Code 在 ~/.ssh/config 文件中填入云主机的信息：

```
Host hermes-agent  / 备注：主机名称    HostName  / 备注：你的云主机的IP地址    User ubuntu    Port 22    IdentityFile / 备注：你的云主机的密钥文件（.pem）的存储位置，例如~/.ssh/xxxxxxx.pem    IdentitiesOnly yes    ControlMaster no    ServerAliveInterval 30    ServerAliveCountMax 3    TCPKeepAlive yes    Compression yes    ConnectTimeout 15    ConnectionAttempts 3    StrictHostKeyChecking accept-new    GSSAPIAuthentication no
```

> 如果你不会填写，也可以将主机IP信息和密钥文件告知你安装在本地的Agent（比如KIMI Code），由该Agent来帮你配置 ssh的config文件～ 配置完成之后，

•

配置好之后，可以在VS Code中通过快捷键 cmd+shift+P（windows是ctrl+shift+P）

![](assets/img_3659f595b96b.png)

•

搜索并点击Remote-SSH：连接到主机，然后选择刚才配置好的主机名称：

![](assets/img_86d62677359f.png)

•

首次连接大概需要一两分钟时间，连接成功后，可以在VS Code左下角看到“SSH-服务器名”

![](assets/img_621022d1a4b4.png)

•

连接成功之后，就可以在Panel（面板）中使用Terminal（终端）来完成后续的安装和配置了

![](assets/img_7a8660709262.png)

> 如果你实在不会配置Remote-SSH和使用VS Code进行Remote-SSH连接，那可以使用腾讯云提供的服务器登录可视化界面(Orca)：

![](assets/img_bc1e13be94a9.png)

> 注意要选择“终端连接（SSH）”；

> 验证方式取决于你购买服务器时选择的是密码还是密钥；

![](assets/img_6e57a858d68e.png)

> 登录成功之后，后续的安装方式都适用于此形式

![](assets/img_032c1707e3fc.png)

### 手边准备好Hermes Agent的文档随时翻阅：

> 我汉化的Hermes Doc中文站： https://hermes-doc.aigc.green/

---

**当准备好以上前置条件后，就可以开始安装Hermes Agent了，具体步骤如下：**

---

## 二、Hermes Agent的安装和配置

•

如果是直接在本地Mac/Linux/Windows WLS2中安装，在Terminal（终端）输入如下安装指令启动Hermes Agent的安装； 

•

如果使用云主机，则通过Remote-SSH方式连接，在Terminal（终端）里输入如下指令：

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

•

请注意：对于小白用户，为了后续使用方便，建议在ubuntu用户下安装，请注意输入命令前面的 ubuntu@VM-xxxxxx 表示当前使用ubuntu用户登录并在该用户下安装Hermes Agent；

![](assets/img_8105906d5bd6.png)

•

如果是一台全新的云主机，安装过程大概会持续10分钟左右；安装完成之后，会看到如下界面，选择“Quick setup”：

![](assets/img_f608ee9242ef.png)

•

在Select Provider（大模型提供商选择）界面，选择Kimi Coding Plan

![](assets/img_52f96f12400e.png)

•

在这个界面中将Kimi Code的API KEY粘贴进来（注意：屏幕上并不会显示出粘贴进去的API KEY，用键盘的粘贴快捷键完成粘贴之后，直接回车即可！）

![](assets/img_eb862e7205cd.png)

•

如果API KEY正确，那么会显示大模型选择界面，选择“kimi-for-coding”即可（这个endpoint背后就是最新的K2.6-code-preview）：

![](assets/img_d6a24cd1d8fe.png)

•

接下来是配置聊天软件的连接，选择“set up messaging now”

![](assets/img_93a4debd7ba2.png)

•

最新版本的Hermes Agent已经将飞书、企微、钉钉、微信、QQ等国内软件都放到了选项中，这里我们还是选择飞书（Feishu/Lark）：

![](assets/img_a529c7238c22.png)

•

注意，这里有个坑：一定要**按下空格键**来选中Feishu/Lark    !!!!!!!!!!!

•

如果你把光标移到Feishu/Lark的位置然后直接点击回车，程序会认为你什么Gateway都不选直接退出！

•

要看到Feishu/Lark前面有个对勾✅；然后，按下键盘上的“回车键”：

![](assets/img_0fd0c1ae6cd2.png)

•

进入配置方式选择，直接选择“Scan QR code to create a new bot automatically”

![](assets/img_46725700de10.png)

•

出现以下提示时，可以将红线中的链接发到自己的飞书里用手机打开，或者直接在浏览器中打开该连接：

![](assets/img_9cadb1c5c4ce.png)

•

如果你提前使用 

```
pip install qrcode
```

 命令安装过二维码依赖库，那么在这里可以看到一个二维码，用手机飞书直接扫描二维码即可

•

假设在浏览器中直接打开该连接，则可以在该页面内填写Hermes Agent对应的飞书机器人的名称，然后点击“创建”按钮：

![](assets/img_3c82ee2bc071.png)

•

飞书自动创建机器人（大概等待十几秒）：

![](assets/img_230367b864cc.png)

•

创建完成之后，会看到下面的界面，先不要点击任何按钮：

![](assets/img_4656652c690f.png)

•

让我们先切换回Terminal（终端）的安装界面，选择“Use DM pairing approval”（即配对码配对）：

![](assets/img_f17ac7d96de7.png)

•

选择“Respond only when @mentioned in groups”（群聊中仅被@时才回复消息）

![](assets/img_84500d1c54b7.png)

•

然后在这个界面下直接回车（不配置Home chat ID，后续再说）

![](assets/img_9f0055c95a06.png)

•

在这个界面输入大写“Y”，然后回车（安装Gateway作为守护进程服务）：

![](assets/img_9e0d6206fbc0.png)

•

在接下来的界面中选择“User Service”（无须sudo超管权限）

![](https://mmbiz.qpic.cn/mmbiz_png/0m9F5vC1OGg1XrGVQK6kauiaIY5ALWa9pdvDicG1LD9RO8Mia0G3sxqKXBTNtwibmMbfJh97ZiaLVibIelzzo5iaqdZJhBWXficgJnJQfBywAFx3zaU/640?from=appmsg)

•

输入”Y“，并回车（启动服务）：

![](assets/img_546b053e80b9.png)

•

显示配置成功：

![](assets/img_dc325725c270.png)

•

回到刚才创建飞书机器人的网页中，点击“打开机器人”，会通过deeplink唤起飞书客户端，并跳转到这个机器人的聊天界面：

![](assets/img_a9e997cab5fd.png)

![](assets/img_c81d657000fe.png)

•

给机器人发送消息，会收到一串配对码 

```
hermes pairing approve feishu xxxxxxxx
```

![](assets/img_cdc7f376d789.png)

•

在Terminal（终端）中输入这串配对码命令：

![](assets/img_2fc718bd163f.png)

•

然后重新回到飞书中和Hermes Agent机器人对话：

![](assets/img_4bf9ed4121d8.png)

•

OK，Hermes Agent机器人已经可以正确回复消息了！当然，你还可以按照上图的提示，在聊天界面中输入 

```
/sethome
```

 来将当前聊天窗口作为默认界面，后续如果有cron-job（定时任务）会默认发到这个聊天窗口中:

![](assets/img_f1d8a86dc01c.png)

![](assets/img_cb11c86904ca.png)

•

接下来，为了确保hermes指令可以在$PATH被正确识别，让我们先在命令行中输入：

```
source $HOME/.local/bin/env
```

•

然后，让我们在Terminal（终端）中输入 

```
hermes
```

  测试下Hermes Agent是否可以在Terminal里正常沟通了

•

应该会出现Hermes 的TUI（Terminal UI）界面：

![](assets/img_f8d119587d00.png)

•

可以先观察一下聊天框上面的一些元素： 

•

kimi-for-coding：你正在使用的大模型；

•

ctx：上下文窗口；

•

7s：当前session持续时间长度；

![](assets/img_d9d28d2cf5c4.png)

•

此外，你还可以在Terminal（终端）输入 

```
hermes dashboard
```

 来启动浏览器上的WebUI

![](assets/img_88bb8119afad.png)

•

绿油油的Hermes WebUI：

![](assets/img_20d7a2a54d85.png)

> OK，Hermes Agent的安装基本完成了。

---

## 三、安装飞书CLI，打造你的数字座舱

•

Hermes Agent官方给出的各平台能力列表中，国内平台中飞书覆盖最全面，这也是为什么我一直推荐飞书作为首选。

![](assets/img_3868cdd250ab.png)

•

除了机器人的基础能力外，我推荐安装飞书CLI来进一步增强对于飞书基建的利用能力。

•

飞书CLI： https://www.feishu.cn/feishu-cli

![](assets/img_afa816d94f53.png)

•

在安装Hermes Agent的主机Terminal（终端）输入：

```
npx @larksuite/cli@latest install
```

,并输入“y”，回车：

![](assets/img_eda187bb0401.png)

•

选择“中文”，回车：

![](assets/img_c1de51e5fc58.png)

•

用飞书app扫描弹出的二维码：

![](assets/img_c6c1dec79f53.png)

•

在手机上完成飞书CLI机器人的创建

•

选择“YES”

![](assets/img_1a94d275b703.png)

•

勾选要授权的业务（空格键=选中），然后回车：

![](assets/img_f7b52cd64916.png)

•

选择你认为合适的权限：

![](assets/img_235cddc16e28.png)

•

在浏览器中打开相应链接完成授权

![](assets/img_66099edfbb6a.png)

•

点击“开通并授权”按钮：

![](assets/img_dc61f1e80483.png)

•

还需要管理员进行审批：

![](assets/img_f74da177c447.png)

![](assets/img_a24c2d11ab1c.png)

•

管理员通过审批后回到Terminal终端；

•

为了方便后续在终端使用飞书CLI，将

```
lark-cli
```

加入$PATH:

```
export PATH="/home/ubuntu/.hermes/node/bin:$PATH"
```

•

可以输入

```
lark-cli --version
```

 查看其版本号，看到类似

```
lark-cli version 1.0.13
```

的信息则表明环境变量已添加成功：

![](assets/img_a62bbdaa2916.png)

•

输入 

```
lark-cli auth login
```

, 然后再次勾选全部权限后点击链接完成授权，应该看到密密麻麻的scope授权

![](assets/img_8cc9b40cea44.png)

•

这时回到飞书聊天界面，和Hermes Agent机器人输入以下内容：

```
我已经在你所在的服务器完成了飞书CLI的登录和授权，请你检查一下你是否已经可以调用飞书CLI了；如果可以，请创建一个飞书文档（随便写点内容）来证明你可以正常使用飞书CLI
```

![](assets/img_349c64991344.png)

•

记得让Hermes把它创建的飞书文档的链接发给你，以防它忽悠你：

![](assets/img_f843712fc83f.png)

---

## 四、如果遇到自己手动解决不了的问题怎么办 -- 安装陪跑Agent - KIMI Code

> 我推荐的大模型厂商是KIMI，而KIMI提供了KIMI Code这个相对轻量级的Coding Agent，你可以在安装Hermes对应的机器上安装KIMI Code来作为“陪跑”Agent帮你解决各种疑难杂症。

### 如果你使用的是VS Code

•

如果你是使用VS Code通过Remote-SSH连接云主机来安装Hermes，那么可以在VS Code的插件市场搜索并安装KIMI Code

![](assets/img_79f5781ea4bb.png)

•

安装成功后在侧边栏点击KIMI Code的图标

![](assets/img_775043e7e5db.png)

•

在界面中完成KIMI Code的登录

•

如果首次安装成功后打开KIMI插件是下图中这个状态，你需要点击“Open Folder”先打开一个文件目录；

![](assets/img_bcb4b465fe8f.png)

•

然后会出现引导打开官网以完成鉴权的过程；

•

登录成功之后会变成如下状态：

![](assets/img_85bd29ea32bb.png)

### 如果你使用的是Terminal（终端）

> 你可以在

> ```
> https://www.kimi.com/code?from=membership
> ```

>  找到安装KIMI Code CLI的命令

•

在Terminal（终端）中输入

```
curl -L code.kimi.com/install.sh | bash
```

![](assets/img_b7d8e8e82de8.png)

•

安装完成后在Terminal（终端）中继续输入

```
kimi
```

 以启动KIMI Code CLI版。

---

•

当遇到一些疑难杂症时，你就可以把问题扔给KIMI Code，让它帮你解决，比如下图这个使用

```
hermes update
```

报错的问题：

![](assets/img_63b346d4ce75.png)

> 当然，由于KIMI Code是个能力一点都不弱的Coding Agent，你完全可以让它在这台服务器上开发网站、App、skills等

•

另外，社群中有的同学说找不到KIMI的Coding Plan的API KEY和Token消耗量......可以直接通过以下网址进入：https://www.kimi.com/code/console

![](assets/img_c73f047e57f0.png)

•

也可以在网页版左下角点击

```
会员计划
```

：

![](assets/img_199b51614292.png)

•

然后点击会员计划中的

```
KIMI Code
```

超链接：

![](assets/img_ce27a11e13eb.png)

•

然后在这个页面点击

```
控制台
```

：

![](assets/img_b2cc5c11183e.png)

•

然后就能看到Token消耗量和创建API KEY的入口了～

![](assets/img_2150434c053c.png)

> 终极偷懒Tips：

> 如果你是先安装的KIMI Code，你完全可以让KIMI Code来帮你完成Hermes Agent的所有安装和配置！

> 你只需要将Hermes Agent的仓库"https://github.com/NousResearch/hermes-agent" 喂给KIMI Code，然后跟它说“请帮我完成Hermes Agent的安装和配置”即可！

---

## 五、关于Hermes你需要知道的冷（/热）知识

### 配置文件 config.yaml

•

让我们先熟悉一下Hermes Agent的目录结构：

![](assets/img_8347e4a0e547.png)

•

绝大多数的配置项都存储在config.yaml中，你可以使用VS Code等IDE来直接编辑这个文件，也可以直接在Terminal（终端）使用CLI命令行的方式直接配置，例如：

```
hermes config # 查看当前配置  hermes config edit # 在编辑器中打开 config.yaml  hermes config set KEY VAL # 设置特定值  hermes config check # 检查缺失的选项（更新后）  hermes config migrate # 交互式添加缺失的选项    # 示例：  hermes config set model anthropic/claude-opus-4  hermes config set terminal.backend docker  hermes config set OPENROUTER_API_KEY sk-or-... # 保存到 .env
```

> 更多配置文件相关内容，参见： https://hermes-doc.aigc.green/user-guide/configuration

此外：

1.

你的密钥都存储在 

```
.env
```

 文件中，如果某个大模型的密钥失效了，也可以直接用VS Code等IDE直接编辑修改 

```
.env
```

文件中对应密钥～

2.

对话相关记忆存储在 

```
sessions/
```

 和 

```
/memories/
```

 以及 

```
state.db
```

 中；

3.

技能存储在 

```
skills/
```

 中

### 如何在Hermes中创建多Agent

从上面的结构图可以看出来，Hermes的主Agent的workspace就是它的根目录，并不存在像OpenClaw的

```
workspace/
```

目录。

但是，当你使用profile命令在同一个Hermes实例中创建多Agent时，就会多出一个 

```
profiles/
```

 目录，这个目录相当于Hermes的workspace了。

例如，要创建一个名为

```
note-mananger
```

的Agent：

```
hermes profile create note-mananger       # 创建 profile 并生成 "note-mananger" 命令别名
```

注意：这时

```
note-mananger
```

已经是和主Agent（名为

```
hermes
```

）一样独立的Agent了，你在CLI命令行中对其进行操作时，要直接使用

```
note-mananger
```

，而不是

```
hermes
```

，例如：

```
note-mananger chat                        # 开始聊天note-mananger model                       # 配置模型note-mananger dashboard                   # 打开WebUI/Dashboard
```

也可以使用仅克隆配置 (--clone)命令：

```
hermes profile create note-mananger --clone
```

将当前 Profile 的 

```
config.yaml
```

、

```
.env
```

 和 

```
SOUL.md
```

 复制到新 Profile 中。使用相同的 API 密钥和模型，但拥有全新的会话和记忆。你可以编辑 

```
~/.hermes/profiles/note-mananger/.env
```

 来使用不同的 API 密钥，或者编辑 

```
~/.hermes/profiles/note-mananger/SOUL.md
```

 来设定不同的性格。

新的Agent创建完成后，你也需要为其连接新的聊天软件的入口（依然以

```
note-mananger
```

为例）：

```
note-mananger setup gateway
```

此外，当你使用特定的Agent启动TUI对话时，可以在对话框上方看到相应的Agent的名字：

![](assets/img_911c316101f2.png)

### 皮肤

•

Hermes Agent有一个很酷的TUI界面，但其实它内置了很多“皮肤”，你可以在TUI中输入 

```
/skin
```

 看看有哪些皮肤

![](assets/img_fd279b0b36d7.png)

•

你可以在TUI中输入 

```
/skin 皮肤名
```

来切换TUI皮肤，比如 

```
/skin poseidon
```

 可以切换成海皇波塞冬的皮肤

![](assets/img_9a9f7b17425c.png)

•

然后你再开启一个新的Hermes TUI时，皮肤就生效了：

![](assets/img_019e93d3fb78.png)

•

同理，你还可以得到下面这些皮肤：

![](assets/img_3ccd267b27ba.png)

![](assets/img_aaa6ee97f086.png)

![](assets/img_9dc04572b544.png)

•

你还可以从外部仓库安装更多的skins，比如： https://github.com/joeynyc/hermes-skins

![](assets/img_88e37b4e3efc.png)

![](assets/img_88ee3b45f579.png)

> 如果有兴趣，你完全可以通过在 

> ```
> ~/.hermes/skins/
> ```

>  下创建 YAML文件的方式自定义自己的皮肤：

> https://hermes-doc.aigc.green/user-guide/features/skins

### 无须审批的全自动YOLO模式

Hermes在工作过程中会经常让你输入 

```
/approve
```

 来显式批准，有时会很让人烦躁：

![](assets/img_debf90a42c3c.png)

或：

![](assets/img_da0c474e9bca.png)

如果你认为风险可控，可以在对话中输入 

```
/yolo
```

 来启动全自动运行模式：

![](assets/img_f82e0ef859de.png)

### 新建和恢复session

```
/reset
```

 或者 

```
/new
```

 可以新创建一个session，两个指令是等效的，上下文窗口会重置：

![](assets/img_736409fb071a.png)

注意：如果你希望精确恢复到某个session，你必须预先通过 /title {name} 方式给某个session命名，然后使用 /resume {name} 来进行恢复！极简示例如下

![](assets/img_e888861fd3f1.png)

### Personality预置聊天风格

你可以在~/.hermes/SOUL.md中修改Hermes Agent的个性，也可以在对话中临时切换它的聊天风格，一共有14种预置风格：

![](assets/img_0e449ee248c3.png)

你只需要在对话中输入 /personality {个姓名} 就能激活相应的个性，比如：

```
/personality kawaii
```

Hermes Agent就会切换成可爱的说话风格，句子中会多很多emoji...

![](assets/img_5b5df4021b61.png)

### 推理强度

对于某些大模型，有推理强度的设定，可以通过以下指令来调整推理强度：

```
/reasoning high
```

```
/reasoning medium
```

```
/reasoning low
```

![](assets/img_8f8c59b6f2bd.png)

![](assets/img_08d2a59c5133.png)

![](assets/img_ba0d48079ab3.png)

### 记忆文件 MEMORY.md 和 USER.md

注意，两个非常重要的记忆文件MEMORY.md（工作记忆）和USER.md（对用户的认知）是有明确的字符数上限的，你不能无限制的往里面塞内容！

•

MEMORY.md 限制 2,200 个字符；

•

USER.md 限制 1,375 个字符；

### 外接记忆系统

Hermes Agent提供了8家外接记忆系统provider：

![](assets/img_094d2b3bceff.png)

你可以（且仅可以）选择其中一家来配合Hermes Agent的内置记忆系统一起工作～

当你选择了特定的外接记忆系统时，你可以直接告知Hermes Agent你的选择，然后由它来指导和配合你完成后续的配置～

> BTW，我目前是选择了配置最简单的免费本地版Holographic；后续打算试试OpenViking、Mem0、Honcho的效果；

或者，也可以在Terminal（终端）中输入下面的指令来触发外接记忆方案的接入过程～

```
hermes memory setup
```

![](assets/img_8d43a64d9e3c.png)

记忆方案的接入过程及不在这里展开了～ 你的Hermes应该可以回答你的各种疑问。

### Hermes的Skills

Hermes的skills存放在

```
skills/
```

目录下，但和OpenClaw不同的是，它是按照分类来组织skills的，也就是说，第一层层并不是skills本身，而是分类目录（自己封装的skill有时Hermes找不到合适的分类也会先放在第一层级），具体的skills会放在第二层级目录下：

![](assets/img_0b02b9f377d1.png)

这和Hermes官方skills hub（ https://hermes-agent.nousresearch.com/docs/skills ）的分类是一致的：

![](assets/img_8f2cf2d35ef6.png)

> 注意：当你创建了多Agent之后，其他的Agent的skills的位置在：

> ```
> profiles//skills
> ```

>  目录下。

Skill进化机制可能是Hermes日常工作中最重要的能力（没有之一）。在和你一起工作时，Hermes Agent会频繁调用skill\_manage能力，来进行：

•

如果不存在skill，但Hermes判断这个工作流需要skill，它就会自动创建（create）一个新的skill；

•

当已经存在skill，但Hermes发现它无法满足最新的情况变化时，它会自动调用patch、edit、write\_file等能力对该skill进行升级；

•

当它认为某个skill的能力已经被其他skill的能力覆盖时，它会调用delete能力对无效的skill进行删除；

> 总之，skill即使对个人和组织know-how的沉淀，Hermes会在工作过程中不断创建新skill、升级已经存在的skill、删除无效的skill，这对于Hermes来说是个内禀的强制过程，这也就是为什么你会觉得Hermes越用越聪明。

![](assets/img_028172529c3f.png)

所以，如果你觉得初始状态的Hermes还不太聪明，那请尽快敞开了用Hermes吧！

### 浏览器自动化能力

Hermes Agent官方推荐了若干浏览器自动化解决方案来进一步提高你的网络浏览和操作效率。

如果你使用的是云主机，我推荐Browser Use和CamoFox。

![](assets/img_eb23fc7e5880.png)

•

并且，Browser Use宣布Hermes Agent用户可以免费使用它们提供的云端浏览器自动化方案（你需要去https://cloud.browser-use.com/ 官网申请一个API Key然后告知Hermes Agent帮你做个简单配置）

![](assets/img_f3625f4708b5.png)

•

CamoFox：可以提供基于Firefox的指纹伪装。

如果是你是用的本地电脑，那直接用CDP连接电脑上的浏览器就好了，可以直接复用网站的登录态。

---

## 实战（skills）

恭喜你，你现在拥有了这样一个极为强大的Agent环境：

•

脑子 = KIMi K2.6 （K2.6-code-preview）

•

Harness = Hermes（爱马仕/赫尔墨斯）

•

Chat & 文件管理 基建 = 飞书

这套环境让我在过去一周时间里，大幅度减少了对我那台Macbook Pro的依赖，70%以上工作完全在手机上完成；

并且，在这一周中，我高强度使用这套环境为自己搭建起了日常若干重要工作流，示例如下：

•

在飞书中撰写内容并推送到微信公众号草稿箱（上图为飞书文档，下图为微信公众号）：

![](assets/img_92e3f2645744.png)

![](assets/img_78f10c0491a6.png)

> skill地址：https://github.com/dracohu2025-cloud/draco-skills-collection/blob/main/feishu-doc-to-wechat-draft

•

使用即梦Seedream（或Nano Banana）生成图片并上传飞书云盘：

![](assets/img_5bcd7f6bd037.png)

> skill地址：https://github.com/dracohu2025-cloud/draco-skills-collection/blob/main/jimeng-image

•

使用Seedance2.0生成视频并回传飞书云盘（Seedance2.0比较贵😂，下方示例仅为480p）：

![](assets/img_313b4bfc7eda.png)

> skill地址：https://github.com/dracohu2025-cloud/draco-skills-collection/blob/main/seedance-video-local

•

将EPUB电子书转换为双人播客（+smart PPT）并回传飞书云盘：

> Skill地址：https://github.com/dracohu2025-cloud/draco-skills-collection/blob/main/epub2podcast

•

抓取某篇微信公众号内容并保存到飞书文档： 

•

CamoFox版： https://github.com/dracohu2025-cloud/draco-skills-collection/blob/main/wechat-article-camofox

•

BrowserUse版： https://github.com/dracohu2025-cloud/draco-skills-collection/blob/main/wechat-article-browseruse

•

使用Remotion生成单词解释短视频： 

•

https://github.com/dracohu2025-cloud/draco-skills-collection/blob/main/vocabulary-video-pipeline

前文提到过，skills即是个人和组织know-how或SOP的沉淀，除了Hermes Agent自己的内禀机制之外，自己也要注意养成将自己的工作流封装为skill的习惯，并且最好将这些skill放到Github仓库以未来跨Agent进行管理和安装～

## 彩蛋：

KIMI 2.6有极强的前端编排能力，刚好HeyGen又新发布了HyperFrames框架，这下，我们可以让KIMI K2.6来封装各种前端视频流

此外，我还让KIMI 2.6封装了100个HyperFrames原子化组件（部分示例如下）：

> 更多组件详见：https://hermes.aigc.green/hyperframes-registry/

![](assets/img_75ff977b81fc.png)

> Skill仓库地址：https://github.com/dracohu2025-cloud/draco-skills-collection/tree/main/hyperframes-explainer-video

逻辑上，从现在开始，你就可以用KIMI K2.6 + Hyperframe 生成视频来解释万物！

此外，我们还可以通过KIMI K2.6 + Manim的 方式来生成数学、物理方向的视频教程：

> Skill地址：https://github.com/dracohu2025-cloud/draco-skills-collection/tree/main/manim-video-with-tts

## 写在最后

在过去两周左右的时间里，我在尝试抛开GUI（也就是带各种可视化界面的）软件，而完全拥抱只通过自然文字进行交流了的Agent交互模式，只要有工作流上的卡点，就自己封装skill或者把目前能找到的优质skill给Agent装上；这有点像是互联网早期“能否仅靠互联网不出家门生存一周”的挑战～ 从这两周的体验来看，即便无法做到100%，但目前KIMI K2.6+Hermes+飞书这个组合也无限接近了！ 用到GUI的，也无非是类似申请注册API KEY这类事务性的工作，而这些工作被替代掉也并不存在技术门槛，只是软件设计的滞后性而已。

从CLI （Command Line Interface）到GUI（Graphical User Interface），再到AUI（Agent User Interface）；

交互方式从命令行，到可视化界面，再到自然语言。

每次范式变革，都会导致“所有应用都需要被重做一遍”的狂潮！

此外，视觉不是不重要；相反，视觉会变得更重要！

重要到，当给你看一幅画时，你需要马上说出这幅画的风格，用自然语言对这幅画进行精准的描述（人脑反推）；给你看一条视频时，你需要马上讲出这条视频的分镜设计！对，就是需要达到这个程度～

否则，你就几乎只能消费，而无法创作。而创作是价值的源泉！

而这，就是我下个阶段探索的方向！（正在搭建一个名为Graphics Academy的网站/应用，来帮助你（我自己）这些非科班出身的人来掌握上面👆描述的这种能力）～ 敬请期待！
