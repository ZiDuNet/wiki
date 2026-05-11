> 📎 来源: [Draco正在VibeCoding](https://mp.weixin.qq.com/s?__biz=MzI2NzM4MTQwMg==&mid=2247495900&idx=1&sn=9823cf82913f506a2b97f3cc350038a1&chksm=eb1e061773a728960308c3b705cfce87e45fb298aa5604597a4c0f5c712b66c45b7a612beeef&mpshare=1&scene=1&srcid=0428hKUpwhqyyG7nWGjnQWMp&sharer_shareinfo=c6a08dc7be543d4c23ce1c0806e8e5e6&sharer_shareinfo_first=c6a08dc7be543d4c23ce1c0806e8e5e6) | 时间: 2026-04-28 19:42

---

（又是一个长篇喂饭教程，哈哈哈）

玩Hermes🐴和OpenClaw🦞对新手最不友好的是啥？

命令行啊！

估计90%的同学都是被命令行劝退的！

> 看着下面的这一大坨，小白是不是有眩晕感？

![](assets/img_68e84983ed09.png)

是否存在这样的Agent协作平台，可以同时满足下面的三个诉求：

1.

你可以轻松创建多Agents（不需要像Hermes/OpenClaws那样需要各种复杂的命令行配置）以组建自己的Agents团队；

2.

每个Agent同样拥有OpenClaw/Hermes等具备的Skills、Memory、Cron Jobs、Heartbeat等强大能力（Harness）；

3.

人和Agent、Agent和Agent之间可以基于Workspace/文档等实现高效协作；

别说，还真让我遇到这么一个有趣的平台：Moxt

> https://moxt.ai/

Slogan是：“你的AI团队，就在Moxt” ~

![](assets/img_559ae762ddaa.png)

后来，我还和这个（国人）团队建立了联系。

我的第一个问题是问他们：Moxt啥意思。

答案是：More Context。

好吧... 就是不确定老外是否知道这个单词该咋读😂

---

接下来，让我们看一眼Moxt的工作界面：

![](assets/img_8d33a4d4482f.png)

### 1. momo：你的私人专属AI助理

最右侧是你的个人Agent，默认都叫momo；结合多Agents工作模式（详见后文），momo在大多数场景里既是你个人专属Agent，也适合作为主Agent（Orchestrator）来指挥一众其他Agents进行协作；当然，momo的单兵作战能力也很强。除了在Moxt的工作台和momo沟通，你也可以在IM上指挥它作战。


> 打通IM平台的操作跟着官方步骤引导即可，不难。

> 唯一需要注意的是：打通飞书时，需要在飞书开放平台创建2个飞书应用，一个是Moxt Organization应用，一个是你实际需要沟通和指挥的Moxt Agent。



最左侧从上到下分别是：

### 2. Agent能力区：

•

AI Teammates：可以创建/招募多Agents；

•

Automation：自动化工作流（cron jobs）；

•

Skills、Rules、Memory：Agent标配的技能、规则、记忆；

•

Inbox：消息箱，例如多Agent协作时在文档中的消息回复都可以在Inbox中查看。

### 3. 团队空间Team Space

•

你如果要创建多Agents（或“真人”），那么大家是可以在Team Space共享文件的：

•

默认包含：

•

System/Skills: 也就是整个组织沉淀下来的SOP/Know-how/whatever你叫它什么...反正就是组织的经验沉淀；

•

AGENTS.md：所有Agents在组织中工作需要符合的要求（员工手册既视感）；

•

非默认包含的文件是我新建的，也就是打算让组织内的多个Agents进行协作的内容。比如：

•

Articles：我和Agent一起协作撰写的文章；

•

Daily Report：我让Social Listener Agent创建的日报（后文提到）

![](assets/img_5341f9ce0c35.png)



### 4. 个人空间Personal Space

•

专属于个人的内容，你可以和momo进行协作的空间

•

可以看到Skills/Memory/Heartbeat/AGENTS等一应俱全，基本上就是你的momo的能力集了

```
personal/├── AGENTS.md                  # 个人规则文件 — 定义你的 AI 助手的个性化行为├── 快速开始.md                 # 快速入门指南├── 快速开始.html               # 快速入门指南（富文本版）├── 帮助文档/                   # 帮助文档目录└── System/                    # 个人系统目录    ├── Heartbeat/             # 心跳检查配置    │   └── heartbeat.md    ├── Memory/                # AI 长期记忆    │   └── MEMORY.md          # 记忆索引文件（自动加载）    └── Skills/                # 个人 Skills（技能）        ├── deep-research-pro/     # 深度研究        ├── humanizer/             # 文本人性化        ├── marketing-mode/        # 营销模式        ├── news-summary/          # 新闻摘要        ├── openclaw-youtube-transcript/  # YouTube 转录        ├── summarize/             # 内容总结        └── yahoo-finance/         # 雅虎财经
```



工作区挺简单易懂的，让我们看看在Moxt怎么实现AI原生的工作体验。

---

## Skills的安装和调用

在momo沟通区，可以把skills的仓库丢给momo，让它直接安装即可（需要明确安装到Personal Space还是Team Space）。

例如，我的工作流都封装到了：https://github.com/dracohu2025-cloud/draco-skills-collection

所以就直接把整个仓库丢给momo：

![](assets/img_6fde9a29ed44.png)

注意，Skills依赖的API KEY等参数可以在Agent的Settings->Integration中点击“+Add”按钮，通过添加Secret Key/Value的方式来添加：

![](assets/img_79dab5bac739.png)

![](assets/img_deab1b4482f6.png)

配置好Secret Key/Value后，可以让Agent跑一个测试任务，Agent应该会正常返回交付物：

![](assets/img_0ee82b542a6e.png)

当然，这篇文章也是在Moxt工作区撰写的，你看到的公众号文章也是在Moxt里通过我封装的skill推送到公众号后台的～ 

再来试试用Manim生成配好TTS讲解数学或物理概念视频的skill：

> momo给自己列了个todo list，从安装Manim/ffmpeg的依赖开始~

![](assets/img_89f6d585e13c.png)

5分钟后，一条使用Manim+Doubao TTS的视频搞定了：

![](assets/img_2fdf79c8d615.png)

> https://static.moxtcontent.com/public/resource/ai/gen/aee6d867-f215-4f42-82eb-0e7a92e72e06.mp4

> 所以，逻辑上我之前2周时间在飞书上封装的15个工作流全部都已经在几分钟内移植到了Moxt中~



哦对了，强力建议你把封装好的skill上传到一个仓库里，比如我就把封装好的skills 都推送到了：https://github.com/dracohu2025-cloud/draco-skills-collection

---

## Github集成

Moxt还支持Github集成，你可以让Agents帮你写代码，审代码、Commit/Push...等等。

在Personal Space下方的Github区域，点击旁边的这个齿轮ICON：

![](assets/img_0a9c75d5a0bf.png)

点击Integration中的Connect Github：

![](assets/img_c49b118afe83.png)

点击Install&Authorize

![](assets/img_0881a5a98fdc.png)

完成后续的Github鉴权后回到Moxt的Integration，可以看到已经连上了：

![](assets/img_ec111896f7e1.png)

点击”Add“可以将某特仓库添加到Github工作区：

![](assets/img_47b91e490409.png)

然后让momo确认一下它是否能看到这个仓库：

![](assets/img_1136063b06ef.png)

你现在可以基于Github仓库开始编排代码了~

我又新建了一个

```
moxt-demo
```

 仓库，然后让momo自己写了一个涵盖官方“帮助文档”全部内容的介绍moxt的网站：

> Github Pages版： https://dracohu2025-cloud.github.io/moxt-demo/

![](assets/img_d8b5667e7c31.png)

momo大概写了十几分钟，然后把所有代码都push到Github仓库远端，也部署了一份到Github Pages，大家看一下效果

![](assets/img_a5584061eda9.png)

![](assets/img_86681f4d83e0.png)

momo非常聪明的取了Moxt官方的所有素材和色调，看上去和官网没有啥差别了，哈哈哈😄

> 由于是host markdown文档为主，momo直接选择了VitePress框架~ 简洁舒服，消耗的点数Moxt也相对较少

---

只有momo一个Agent怎么过瘾！ 我们能否创建多Agents的AI原生团队？当然可以

## 多Agents

你可以在左上角

```
AI Teammates
```

 创建（招募）更多AI牛马们：

![](assets/img_ed6894a84594.png)

让我们先看看“人才市场”（Market）里有些啥Agents：

![](assets/img_b5ddd570bec9.png)

Well，一共十个大类，100多种Agent牛马整整齐齐等待接受你的招募。

我先挑选了一个Social Listener：

![](assets/img_38b61779bacb.png)

然后点击”Add“按钮，它就出现在了AI Teammates列表中，然后点击它的头像：

![](assets/img_13c9b8312eaa.png)

然后就出现这个Agent的专属界面，可以看到：

1.

它有自己的Personal Space

2.

同时，它又共享我们的Team Workspace

3.

点击”Settings“可以看到这个Agent的相关能力（Skills/Memory/Heartbeat/Automations等）：

![](assets/img_df3587092cbf.png)



我给它下的第一个指令是：

> 请创建一个日报机制，每天早晨8:00和晚上20:00，总结并向我我汇报以下相关topics：

> 1.

> Hermes Agent

> 2.

> OpenClaw

> 3.

> AIGC Image

> 4.

> AIGC Video

> 5.

> Product Hunt top products

> 6.

> Github top repos

> 日报以markdown文件格式保存到 @Social Listener  目录内

几分钟之后，Social Listener就创建了第一个Report，并按照指定位置放到了Team Space 的 

```
Daily Reports/Social Listener
```

  文件目录中：

![](assets/img_f20acc3d9eb8.png)

这时再打开Social Listener的Settings，可以看到Automation中出现了一天两次的Daily Reports的定时任务：

![](assets/img_1602fc7543f6.png)



Social Listener是官方封装好的，如果我们自己创建一个新的Agent呢？

比如，创建一个 

```
Design Expert
```

 ：

![](assets/img_b9b8c165fb58.png)

新建的Agent大概有1分钟左右的初始化过程，然后它会做个自我介绍，以及和我探讨它后续的工作职责和风格：

![](assets/img_7350d8457efb.png)

我先让它确认了一下自己拥有哪些生成图片的工具，它的回复如下：

![](assets/img_e61a9cd60203.png)

第三个能力即梦生图是我刚才安装的skill带来的，那么前两个 **```
generate-image-fast
```** 和 **```
generate-image-hq
```** 就都是Moxt自带的底层工具箱了。

我大概测试了一下，前者应该是Stable Diffusion系的模型，非常快，效果一般。

后者可能Nano Banana或者GPT-Image系列，质量很高。

下面两张图是相同prompt下的出图效果：

![](assets/img_e3782db59254.jpg)

![](assets/img_10e295bf6f5e.png)

> 上图是fast模式，下图是hq模式，我觉得还是直接用hq模式吧。



当你拥有了多个Agents后，你可以让momo当总指挥，来编排其他Agents一起协同工作。

![](assets/img_ce5ad03954d6.png)

例如，让momo带领三个Agents把刚才的moxt-demo网站进行重构。

momo会在Team Space创建协作文档：

![](assets/img_dcf59422951c.png)

并在文档中@对应的Agent，而该Agent收到@之后，会在文档中进行回复，并开始自己的工作。

![](assets/img_d9a1a8181e22.png)

![](assets/img_f3c113dc2587.png)

> Hermes中文社区的3000人大群众有不少同学在折腾用一个Agent指挥其他Agent干活儿，喏，Moxt采用了这种协作范式，我觉得比在群里互相@要科学合理的多，文档即即一切嘛！

大概二十分钟后，新版网页上线！

> https://dracohu2025-cloud.github.io/moxt-demo/

![](assets/img_a8742be8f994.png)

![](assets/img_5852cd308673.png)

![](assets/img_8d945f226d6e.png)

![](assets/img_f1d70c6485d9.png)

## 可视化一切

Moxt里面还有一个“可视化一切”的概念，这个和上周钉钉CEO”无招“提到的”日抛”型应用应该是一个理念。

具体讲，就是，协作过程中的交付物不一定必须是文档，也可以是HTML。



我的理解是：

•

文档主要用于人和Agent、Agent和Agent之间的协作；

•

HTML主要是为了弥补人类阅读文字较低的比特带宽（看过一些研究说人的大脑每秒钟只能处理几个到几十个比特---这里应该指的是《思考，快与慢》中所说的“系统2”，即“慢系统”），尽量用视觉的方式来提高人类的信息处理效率...

![](assets/img_bf34009acee3.png)

Moxt的文件目录中存放的HTML是可以直接打开进行交互的，例如点击

```
Evidence-Map.html
```

 这个文件，右侧工作区会直接出现一个图谱模式的HTML页面：

![](assets/img_52e490d7e38d.png)



再比如，之前让Social Listener Agent创建的markdown文档的日报，又何必必须是markdown格式呢？为什么不能是HTML呢？

![](assets/img_734a5787d866.png)

![](assets/img_2ad00fb596ed.png)



---

## Moxt功能小结：

•

轻松创建多Agents团队，无须繁琐的命令行配置；

•

多Agents之间可以通过基于文档@的协作模式，一般是momo为主控的一主多从模式；

•

Agents可以操作文档、HTML、Github代码；

•

Web内容可以通过Github Pages轻松部署；

•

Agents也可以通过HTML打造各种可视化内容协助人类工作；

•

Agents自带图片生成工具；

•

Agent还可以引入各种skills、MCP、API来增强自己的能力；

总之，Agents的能力被封装的很好，你只需要专注在有价值的工作上即可！



更多Moxt相关内容，可以看我搭的这个Moxt网站～

> https://dracohu2025-cloud.github.io/moxt-demo/

## 定价/成本

最后，总要谈到使用成本：

![](assets/img_8f06d26cf655.png)

> 免费试用赠送1000积分（折合$10≈￥70人民币）

上面案例中Social Listener的一次日报对应150积分左右。

![](assets/img_32f2b1ca95fe.png)

上面提到的第一版网站建设大概对应700-800积分左右：

![](assets/img_f60d394071de.png)



怎么判断这个价格贵还是不贵？

看Agent的工作是不是真的在帮你创造价值，或降低成本。

如果你的公司真的需要搭建一个网站，并且需要找团队（不论是in-house还是out-source），需要花费几千上万的费用，那对你来说肯定是值得的，但如果你只是“玩一玩”，那可能就是不值的。

其他同理：市场调研、数据分析、投研洞察、客服售后等等...... 不同的工作会在Moxt中消耗不同的积分点数，不同的工作也在真实世界中创造/不同的价值或降低不同成本，这个，只有你自己来衡量ROI了。

总之，如果你有明确的业务场景，希望通过AI Agent提效降本，而又对OpenClaw/Hermes的命令行和各种“折腾”望而却步，那轻量化的Moxt Agent协作平台，可能是个非常不错的选择。
