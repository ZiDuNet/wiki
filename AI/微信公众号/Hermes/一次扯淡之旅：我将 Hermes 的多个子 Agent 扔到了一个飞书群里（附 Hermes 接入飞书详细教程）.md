> 📎 来源: [云起泊言](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868771&idx=2&sn=43299f187b68194303aeee033470ee0c&chksm=86c60a21a2a1494dc30799e4a42ee764e01b82da86895eb1ffae9d46be201fc2a9fafc6af25f&mpshare=1&scene=1&srcid=04258JwUK3y6WGWOAoJGoOAJ&sharer_shareinfo=23e675f1179b7bf031e609ba0791e30b&sharer_shareinfo_first=23e675f1179b7bf031e609ba0791e30b) | 时间: 2026-04-25 20:11

---

我的工作中一直都没怎么接触过飞书，只是在偶尔参与某些产品内测的时候才会把它重新下载回来，在OpenClaw大火的时候看到人人都用飞书接入玩的飞起，那时也没有让我有接入的动力

上次发了一篇关于**Hermes开启多个子Agent**的教程，让我的Hermes分为了三个不同分工的Agent，一个负责写作，一个负责出PRD，一个负责编码，如果要想跟着这篇文章一起实现群组里面接入多个子Agent的话还是建议先看完我之前写的这篇文章：[Hermes 多 Agent 团队协作的正确打开方式](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868631&idx=1&sn=9b4210e367d4e69335bdb29839fe901d&scene=21#wechat_redirect)

---

当时看到有大佬将Hermes跟OpenClaw两个Agent扔到了某国外软件的群组里面，互相调用，互相督促，感觉还挺好玩的，于是我想尝试将Hermes的多个子Agent扔到同一个群组里面对话，但是死活不行，只有主Hermes能够回复我消息，子Agent就是不回消息，玩了玩没啥意思，于是就暂时搁置下来。

今天突然想到，既然某国外软件不行，那飞书是不可以，于是我又将飞书 APP 下载了回来

我想很多同学不管在玩OpenClaw还是在玩Hermes时，已经将飞书的接入流程玩的炉火纯青了，根本不用我的这篇教程来学习配置，所以我这篇文章也就当做我的一个记录吧~

---

## 接入教程

打开终端，执行命令：

```
hermes gateway setup
```

选择 

```
Feishu / Lark
```

 选项：

![](assets/img_dd476b0077c3.png)

选择第一个扫码登录：

![](assets/img_467fadbe0254.png)

**注意⚠️：扫码登录只有主Agent可以调起，子Agent不可以**

![](assets/img_aae46e6ce193.png)

扫码登录成功后继续后面的配置：

![](assets/img_ab662411bd4a.png)

![](assets/img_0d4f445a415a.png)

以上全部选择推荐配置即可

**Home chat ID**这里可以先不配置，直接回车，后续在机器人对话中发送 

```
/setHome
```

 就好了 

![](assets/img_ce0b3aa69a47.png)

按照流程操作完之后，这时候我们在飞牛APP中可以看到机器人了，进入对话随便发个消息，就可以收到配对命令：

![](assets/img_3d4042a39679.png)

将该命令粘贴到终端执行就可以了，当看到如图返回表示配对成功，就可以正常对话了：

![](assets/img_f3218817cd53.png)

---

以上为主Agent配置教程，虽然子Agent配置大相径庭，但是有部分细节不同，大家要仔细看以下内容：

现在假设你跟我一样也有了多个子Agent，比如写作助手叫writer，产品助手叫planner，编码助手叫coder，那么我以planner举例

在终端执行命令：

```
planner gateway setup
```

使用下面的命令也可以，跟上面的效果一样：

```
hermes -p planner gateway setup
```

你可以理解为

```
planner
```

 等于 

```
hermes -p planner
```

。

然后跟配主 Agent 一样的步骤，选择 **Feishu**，在选择扫码跟填写 APP ID 这一步，你不管选哪一个都一样，因为子 Agent 无法调起二维码，最终都会让你手动输入 APP ID（如下图）：

![](assets/img_be86611f3bdb.png)

到这一步，先按下不表，跟我来创建 APP ID：

访问飞牛开发者平台：

```
https://open.feishu.cn/
```

登录后点击右上角 **「开发者后台」**：

![](assets/img_ca10e1c27587.png)

进来后我们可以看到**创建飞牛智能体应用**的入口，点击 **「立即创建」**：

![](assets/img_2831944d45e0.png)

选择头像，输入名称：

![](assets/img_25318f3296f5.png)

创建成功后会获得 APP ID与 APP Secret：

![](assets/img_83a8ed0c7da0.png)

将App ID跟 App Secret 粘贴到终端后剩下的操作继续按照推荐的来就行了。

创建完毕后我们通过飞书打开planner机器人的对话，随便发个消息，收到配对命令：

![](assets/img_a67bfffc9e85.png)

**这里要注意一下，先别执行！！！**

由于收到的命令是主Agent的，执行会失败，根据我下方的命令进行修改一下再执行：

你收到的：

```
hermes pairing approve feishu ZH7CVU7F
```

你真正需要执行的：

```
hermes -p planner pairing approve feishu ZH7CVU7F
```

相信你按照我的步骤来，到这里肯定已经成功了：

![](assets/img_417227f86bfd.png)

其他子Agent继续按照上面的流程创建即可。

---

然后在飞书创建一个群组（这里不用我教了吧~），然后将机器人们拉进来就可以了

点击群组右上角三个点 -> 设置 -> 群机器人，添加机器人，完成！

![](assets/img_c60162fdea37.png)

然后就可以同时跟多个Hermes Agent机器人对话了~

![](assets/img_332dc0e2314e.png)

---

其实我想要的还不够，我想要的效果是我只负责跟Hermes主Agent对话，然后由主Agent去通知另外的子Agent去工作，达到真正的团队协作，只是~

无论我怎样让主Agent去@子Agent进行任务的下发，都无法实现：

![](assets/img_a72bfac09954.png)

由于飞书的@功能与直接输入@+名字不一样，经过多次尝试最终的效果依旧不尽人意，所以就只能换个思路了

**让群组机器人获取群组中的所有消息**

首先在开发者平台应用 -「事件与回调」中确保已经开通获取群组中所有消息：

![](assets/img_7e0bcb9c5ac2.png)

不过好像Hermes 的飞书组件是没有这个功能的，就算开通了权限不@机器人的情况下它也没法接收/发送消息，于是，我让Hermes自己改代码：

![](assets/img_89da25896488.png)

![](assets/img_5bba8529b91a.png)

在 

```
config.yaml
```

中增加了如下配置：

```
feishu:  require_mention: true  free_response_channels:    - oc_xxxx
```

于是我将 

```
require_mention
```

 改为了 

```
false
```

，开启了魔幻之旅：

![](assets/img_bee898f4535c.png)

当我感觉一切美好的时候。。。。

![](assets/img_781965290764.png)

![](assets/img_122b86924d2b.png)

![](assets/img_9fd09d0a1569.png)

![](assets/img_1a7c717b1628.png)

彻底乱套了。。。

然后就让主 Agent 接着改代码，并且在配置中增加关键词识别：

```
feishu:  require_mention: true  free_response_channels:    - oc_xxxx  channel_required_keywords:    oc_xxxx:      - Hermes Planner
```

然后，越来越扯淡了~

![](assets/img_3ed8cc69ba8b.png)

**告辞，不玩了**👋👋

想问问大家对于这种多Agent放在同一个群聊里面是怎么玩的，是我的玩法不对吗？

- 往期推荐 -

[Hermes 配置 NVIDIA 免费使用 MiniMax-m2.7 模型](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868729&idx=1&sn=1e6d37dc86b6e7de8c9c897d76843ed6&scene=21#wechat_redirect)

[Codex 悄悄发布了 MacOS（Intel）版本](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868729&idx=2&sn=51a5c33caadb65e76a1f2721e6c7bcba&scene=21#wechat_redirect)

[GPT-Image-2 发布，我试完之后只想说：有点离谱](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868711&idx=1&sn=edcbf35e4cc07bfacca33a2994c66424&scene=21#wechat_redirect)

[Hermes 更新：终于支持Ollama，Web UI也可以更换主题了](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868684&idx=1&sn=102cf3048450b2e88f5cd371795be4f9&scene=21#wechat_redirect)

[这才是我想要的Hermes Web UI（强烈推荐）](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868645&idx=1&sn=857b458123fe6bc2945862a0f61fe146&scene=21#wechat_redirect)
