> 📎 来源: [沃垠AI](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653727060&idx=1&sn=2d97908ab6ab0006d63bc1267d6dd928&chksm=8cb743be53878596561c04d8f36309cb63daf8a85d12a2ec29d2e8f832af0272b5e5a3bd6386&mpshare=1&scene=1&srcid=05186xullx3bNhgKh5ggzsvb&sharer_shareinfo=985d559089ff26b9583a2219eff5036f&sharer_shareinfo_first=985d559089ff26b9583a2219eff5036f) | 时间: 2026-05-18 23:15

---

大家好，我是冷逸

跟人的精力一样，大模型的上下文一旦长了就容易乱。长任务经常跑着跑着就变笨了，或者直接给你罢工不运转。

我最近在读明史，发觉大明这套官僚体系非常适合做Multi-Agent架构，于是我鼓捣了一番，搭了一个「大明PPT Agent Team」，专为高质量PPT而生。

![](assets/img_7be70a9469eb.png)

在这套Multi-Agent架构里，你是皇帝（也就是用户），是Agent Team的最高统帅，对Agent任务和结果拥有一票否决权。你调用这支Agent Team，也就是「皇帝诏曰」。

它的逻辑是这样：

- 你下旨给内阁，内阁会进行任务分配、进度监督和结果汇总。但内阁只管过程，不执行。
- 内阁接旨后，会分别派发给锦衣卫、东厂、翰林院、工部、织造局等Agent，由他们负责干活，内阁负责管理这支Agent Team，确保政令畅通。

整个Multi-Agent的工作流程是：下旨 → 深度研究 → 事实核查 → 大纲生成 → 配图生成 → HTML PPT 输出。

![](assets/img_f87a2ac0fb3b.jpg)

期间，皇帝（你）只负责躺在床上办公，会用微信就行。

我把整套Multi-Agent架构开源放在Github上了，欢迎大家star。

开源地址：

https://github.com/woyin2024/lengyi-ppt-agent-team

上个周，我看到MiniMax Agent桌面端上线了Agent Teams，我把这套架构搬到了MiniMax Agent上，做PPT的质量和效率都提升了不少，尤其是质量方面。

给大家看几个示例。

![](assets/img_2c24a2e81192.png)

![](assets/img_5ba73329a59b.png)

这套架构重点解决了信源质量、演讲风格和流程自动化的问题，直接产出TED叙事水准的PPT。

![](assets/img_38776e00654c.jpg)

使用流程

下面，我们来详细介绍一下这套Multi-Agent架构是如何在MiniMax Agent里工作的。

0）前置工作

首先，我们前往MiniMax官网下载安装MiniMax Agent桌面版，Windows和MacOS都支持。

![](assets/img_c9cf862082c0.png)

下载网址：

https://agent.minimaxi.com/download

然后，订阅一个Token Plan。

![](assets/img_3f9b1ee65fe2.gif)

现在，MiniMax已经把TokenPlan和Agent Plan合并了。一份订阅，CLI、API、Agent全打通；M2.7、音乐、视频、语音所有模型都包含在内。

这点，是真的很赞。

桌面版安装好后，我们给它设定一下工作文件夹。建议你单独建一个文件夹，把你要的上下文素材（比如图片、视频、文档啥的），都统一放在这个文件夹。

![](assets/img_a3ac615c3b14.png)

这样，它后面的上下文引用和产出物，都在这个文件夹里。

然后，给它连一下IM，飞书和微信都支持。比较简单，直接扫码就行。

![](assets/img_8b05355ed32d.png)

这个连接方式不是企微那种，也不是客服消息那种，是直接个人微信就有一个AI好友，可以直连MiniMax Agent。

![](assets/img_c925b8a952e5.png)

这样，皇上（你）就可以随时随地移动办公了。躺在床上都行，保管你的旁边没有别人酣睡/狗头。

MiniMax Agent有一个技能中心，这里有很多skills，可以直接安装，也可以自己创建。

![](assets/img_e07137371120.png)

这次的大明PPT Agent Team，需要用到guizang-ppt-skill，我们需要提前安装一下。安装也很简单，直接跟Agent说：

> 帮我安装这个skill：https://github.com/op7418/guizang-ppt-skill

![](assets/img_012a7c47fa9b.png)

1）创建Agent Teams

MiniMax，把升级后的Agent起了个新名字，叫「Mavis」，来源于Jarvis，也就是MiniMax as a Jarvis。

接下来，我们把「大明PPT Agent Team」装到Mavis上。

安装也很简单，如果你想要一个轻便版，直接让Mavis读这份「大明PPT御制流程.md」就行。

> 根据这份md文件：https://github.com/woyin2024/lengyi-ppt-agent-team/blob/main/大明PPT御制流程.md

> 帮我组建一支「大明PPT Agent Team」，共6个Agent：内阁、锦衣卫、东厂、翰林院、工部、织造局，详细设定每个Agent的角色与分工。

![](assets/img_f929023fe5a6.png)

如果你想要完全版，那就把整个开源项目都丢给Agent，让它参考进行设定。

比如，我丢给Mavis后，它很快就把这支Agent Team给建起来了。

![](assets/img_867cd73782d5.png)

2）实测Agent Team

接下来，我们实测体验一下这支大明PPT Agent Team。

> 朕要做PPT，六部听旨。

锦衣卫先进行全网深度研究，输出4000字报告，毕竟它可是大明的国之利器，拥有完整的“侦、捕、审、关”链条。

![](assets/img_603024ebfd7a.png)

光有锦衣卫调查不行，得安排东厂去制衡一下，对内容信源进行事实核查。

果不其然，找到了几个问题，打回锦衣卫重新修订。

![](assets/img_a79a9959b386.png)

直到锦衣卫提交了3版，东厂这才放过。

![](assets/img_434c0b0460ea.png)

核查无误，东厂会提交给皇帝陛下亲审，毕竟它可是“皇帝耳目”。

![](assets/img_4fd7775a9fb7.png)

皇上确认「研究报告\_终版.md」没有问题后，翰林院接棒制作PPT大纲。

![](assets/img_d042b49c7caa.png)

翰林院会按照TED 3S原则来设计大纲，为PPT设计一条完整的故事线（钩子→推进→高潮→落点），并标注建议配图部分。

大家如果经常看TED视频，会发觉他们的演讲PPT有一个很不一样的地方：PPT不传递信息，只强化体验。观众是来听你说话的，不是来读屏幕的。

所以，TED演讲的PPT，极其讲究故事感。

我把这套技巧设计成了TED 3S原则，让翰林院务必严格遵守。

![](assets/img_b35898b52e2a.png)

翰林院大纲做好后，会转工部出图、织造局做PPT。

![](assets/img_cb7c19cffa92.png)

期间，如果有遇到各部门撂挑子的，内阁一直都盯着的，确保政令畅通。

![](assets/img_6724baa8ab97.png)

同样，如果皇上想看Agent们的实时工况，可以随时视察。

![](assets/img_0e0e5a6dec62.gif)

工部和织造局交付PPT后，内阁会进行最终的产物验收。只有通过后，才呈给陛下。

![](assets/img_9104380779c6.png)

3）更多case

来看下最终交付的产物。

有研究报告（初版&终版）、PPT大纲。

![](assets/img_93fe7f7b17ab.png)

有详细的配图清单。

![](assets/img_0d913f6950b0.png)

以及最终的HTML PPT成品。

![](assets/img_41ee25de8428.gif)

也可以替换一下风格。

![](assets/img_da50f03e9926.png)

我还跑了几个case，最喜欢的是给我这个开源项目做的PPT，比如这第一张PPT，我是真的喜欢。

![](assets/img_89f65ef495ad.gif)

这设计和动效，真的太带感了。

我挑几张给大家展示下。

![](assets/img_1a9a383c04d2.png)

![](assets/img_4139438d5c3f.png)

![](assets/img_37171b9e7a67.png)

![](assets/img_9bcc544b6d92.png)

![](assets/img_f55b2ddb77cd.png)

![](assets/img_32c5971f3999.jpg)

写在最后

以上，就是我搭建的大明PPT Multi-Agent架构，天然适合支持Agent Team的平台，比如MiniMax Agent。

它把PPT流水线拆成了1+5的Agent Team任务，深度研究、内容复核、大纲生成、配图生成、PPT生成以及全程任务的派发与监督，六个Agent各司其职，协作完成。

就像一台国家机器一样精密运行，而你（皇帝陛下）只需要在微信上下旨就行。

成本方面，我也核算了一下。

我订阅的是98的Plus极速版，每5小时有1500次的模型调用，跑这篇文章我用掉了405次，不到5小时额度的1/3。

![](assets/img_ebb5c4eb1047.png)

这个成本，我觉得完全ok。

深度体验下来，Agent Team这套玩法是真的很有意思，我已经迫不及待想要去探索更多的玩法和架构了。

当然，欢迎大家一道来玩，一起迭代，一起成长。

我是冷逸，爱死磕提示词、Skills和Agent，努力给大家分享有用、有趣的AI干货。希望今天这篇文章对你有所帮助，觉得有用的话给我们三连支持一下，感谢。

我们，下期见。
