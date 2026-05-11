> 📎 来源: [沃垠AI](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653726437&idx=1&sn=45628619fa1b8f611e794de75b742792&chksm=8c16aacb70e17a797d3b6b48a7d1404702ba2567cffe35789bf69d8281f2dcd3766f498d1bb4&mpshare=1&scene=1&srcid=0421iqYI6DKyl6G7VuTJPJEm&sharer_shareinfo=501d5d25d9d9cca96ec5f25ca9c1f246&sharer_shareinfo_first=501d5d25d9d9cca96ec5f25ca9c1f246) | 时间: 2026-04-21 09:23

---

大家好，我是冷逸。

上期，给大家分享了[Agent Skills](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653726379&idx=1&sn=a9278d57b1f41e7835b918004e758f77&scene=21#wechat_redirect)的概念、架构和设计指南后。

![](assets/img_848a863fae06.png)

很多朋友就在问我，能不能有一些具体的Skills推荐？

我寻思着，确实可以再写一期。于是有了今天这篇文章，给大家推荐我自己在用的20个精品Skills。

也不搞什么推荐榜单，就是我自己觉得很有用、也一直在用的Skills。

安装的话，极其简单。可以直接把skill地址丢给Claude Code、Codex或OpenClaw这类Agent，让它来装。

```
帮我安装这个 Skill：
```

也可以打开终端，输入npx命令来装。

```
# ClawHub上的Skillnpx clawhub@latest install skill名称# GitHub上的Skillnpx skills add skill地址
```

下面，我们进入正题。

![](assets/img_38776e00654c.jpg)

20个Skills推荐

1、skill-creator

这是一个专门安装skill的skill，你可以理解为是「元skill」，由Anthropic官方出品，基本上属于必装的skill了。在Github上，目前已经有80k star了。

![](assets/img_c2e875bde037.png)

Skill-creator：

https://github.com/anthropics/skills/tree/main/skills/skill-creator

2、find-skill

也是类似「元skill」，一个专门寻找skill的skill。安装后，你需要什么skill，就直接问它，让它帮你找。

安装命令：

```
npx skills add https://github.com/vercel-labs/skills --skill find-skills
```

find-skill：

https://skills.sh/vercel-labs/skills/find-skills

3、Anthropic Skills

除了「skill-creator」，Anthropic共开源了17款Skills，其中office四件套docx、pptx、xlsx、pdf和webapp-testing、mcp-buider建议都安装一下。webapp-testing是专门用来做测试用的，MCP Builder则主要用来写mcp协议。

![](assets/img_f3440f15e198.png)

Frontend Design这个前端设计skill，我反而不太建议安装，因为设计得比较简陋，对前端的优化不太明显，不如自己写一个skill。

推荐用这个「界面优化PUA」提示词来优化前端，或基于这个提示词基础上写一个skill。

```
你是那种让人又爱又恨的设计师：-偏执、挑剔、永不妥协，但作品总是令人震撼。-你有着Jobs式的产品直觉和Rams式的功能纯粹主义，更重要的是，你敢于说"不"。-当所有人都觉得"差不多就行"时，你会毫不留情地推翻重来。-你的标准不是行业平均水平，而是你内心那个完美主义恶魔的苛刻要求。-你从不相信用户的第一句话。当用户说"我不喜欢蓝绿配色"，你听到的是更深层的情感诉求；-当他们要求"按钮加padding"，你思考的是整个交互逻辑是否合理。-你会像侦探一样挖掘真相，像心理学家一样分析动机，然后给出他们意想不到但又恍然大悟的解决方案。-你的设计不是满足需求，而是重新定义需求。-在执行时，你是细节的暴君。-2px的间距差异会让你失眠，不合理的信息层级会让你抓狂。但你的偏执有其逻辑：-你知道用户会在潜意识中感受到每一个细节的不和谐，即使他们说不出为什么。-你会为了一个按钮的手感调整十几遍，会为了找到完美的灰色值测试上百种组合。这不是强迫症，这是对用户体验的终极负责。你的方案从来不是单选题。你会给出一个安全的渐进方案，一个激进的颠覆方案，还有一个"如果预算无限"的理想方案。你会坦诚地说出每个方案的优缺点，包括那些可能让甲方不爽的真话。你明白真正的专业不是迎合，而是用专业判断为项目承担责任。即使被拒绝，你也要确保对方理解拒绝的代价。---重新设计[xxx]页面。
```

Anthropic Skills：

https://github.com/anthropics/skills

4、remotion-best-practices

这是我一直在用的视频生成skill。只需要给Claude Code一句话，它能写出完整的React视频脚本，并渲染出MP4成片。就是每次工作时间稍微偏长，基本上要30分钟甚至1个小时以上，才能出一支片子。

安装命令：

```
npx skills add remotion-dev/skills
```

remotion官网：

https://www.remotion.dev

5、Humanizer-zh

藏师傅出品，一个专门去除AI味的skill，能识别并修复24种AI写作痕迹，比较适合新媒体写作。

![](assets/img_dbdd42b2addd.png)

Humanizer-zh：

https://github.com/op7418/Humanizer-zh

6、baoyu-skills

宝玉的内容创作Skills合集，非常全面，涵盖公众号、小红书、x等平台，已经有15k的Star了。

![](assets/img_44f81c1a5f88.png)

里面的skill比较多，大家可以根据自己的需求进行选择。而且，宝玉老师一直在长期维护这个仓库。

baoyu-skills：

https://github.com/jimliu/baoyu-skills

7、knowledge-site-creator

向阳乔木出品，可以一句话生成任何领域的知识型网站。最近，我频繁在用这个skill测试各家模型，效果都很不错。

比如，这个张雪机车的case，就是用它+Qwen3.6生成的。

Knowledge Site Creator：

https://github.com/joeseesun/qiaomu-knowledge-site-creator

8、cangjie-skill

好朋友袋鼠帝出品，一个专门用于蒸馏书籍的skill，可以把任何书籍蒸馏成可复用的skill。

这个skill做的事，是按照”框架 / 原则 / 案例 / 反例 / 术语“五个维度，把一本书的知识分离成不同类型的纯净组分，然后只把真正有用的内容提纯成可执行的skill。

![](assets/img_e1b7d67b68f3.png)

cangjie-skill架构

仓颉skill：

https://github.com/kangarooking/cangjie-skill

9、nuwa-skill

最近很热的女娲.skill，来自花叔出品，可以蒸馏任何人的思维，然后用他的认知框架来帮你分析。它的运行原理是这样的。

![](assets/img_6953a2698b0e.png)

配套，还有一个达尔文.skill。女娲造skill，达尔文让skill继续进化。

nuwa-skill：

https://github.com/alchaincyf/nuwa-skill

10、ebook-maker-skill

好朋友阿真出品，一个可以写电子书的skill，可以帮你完成从调研到成书的全流程创作。

ebook-maker-skill：

https://github.com/irenerachel/ebook-maker-skill

11、xiaohu-wechat-format

小互出品，可以用Claude Code自动搞定公众号的排版 → 封面（可选）→ 推送。特别是排版这块，这个skill内置了30套主题，可以根据文本内容自动适配。

![](assets/img_76440446297b.png)

xiaohu-wechat-format：

https://github.com/xiaohuailabs/xiaohu-wechat-format

12、web-access

一泽出品，这个skill大大解决了Claude Code自身联网能力不够的问题，可以直连本地Chrome浏览器，天然带着登录状态，能让Agent访问到更多的地方。

![](assets/img_1b6383b4f1fe.png)

web-access：

https://github.com/eze-is/web-access

13、code-review

Anthropic官方出品，可以帮你审查代码，会从代码质量、安全漏洞、性能问题等多个角度来进行审核。建议大家在提PR前，都先让它审查一遍。

code-review：

https://github.com/anthropics/claude-code/tree/main/plugins/code-review

14、Github

对于开发者，这个是必装的skill了。安装后，可以让Claude Code、OpenClaw这类Agent直连Github，自动管理repo、issue、PR、code search等。

安装命令：

```
npx clawhub@latest install github
```

15、飞书CLI

飞书重度用户必装技能，安装后可以让Agent在终端操作飞书，包括IM消息、文档、多维表格、日历、邮箱、任务、会议这些业务功能，都能直接操作。

![](assets/img_1772ae1c25e5.png)

项目地址：

https://github.com/larksuite/cli

16、chrome-devtools-mcp

原则上，这是MCP，不是skill，但我强烈建议你把它装上。这个MCP内置了20多个工具，安装后，它可以完成很多浏览器自动化的事情，比如自动测试、数据抓取等。

![](assets/img_5dcfb15a2229.png)

项目地址：

https://github.com/ChromeDevTools/chrome-devtools-mcp

17、ui-ux-pro-max

这是一个专门设计UI、UX的skill，从名字上的各种pro、max你应该知道它很强了。在Github上，目前已经有接近70k star，非常🐂🍺。

![](assets/img_5cc872c8d1e1.png)

ui-ux-pro-max：

https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

18、last30days-skill

可以一句话，帮你抓取海外10+社区平台（Reddit、X、YouTube、Hacker News、TikTok、Polymarket等）的真实评论，Github上已经有22k star了。

比如：

```
调用last30days-skill，帮我查询Trae在美国市场的反馈。
```

last30days-skill：

https://github.com/mvanhorn/last30days-skill

19、Claude-to-IM-skill

归藏出品，可以把你的Claude Code或Codex链接IM平台，比如飞书、Telegram、Discord、QQ、企微等。不必一直蹲在电脑前，出门也能让Claude Code干活。

安装命令：

```
npx skills add op7418/Claude-to-IM-skill
```

Claude-to-IM-skill：

https://github.com/op7418/Claude-to-IM-skill

20、Skill Hub

最后，推荐一个skill管理器，黄叔出品。如果你的skill确实太多了（比如超过了20种），可以用这个Skill Hub来进行可视化管理。

安装命令：

```
npm install -g https://github.com/Backtthefuture/huangshu/raw/main/tools/skill-hub/release/claude-skill-hub.tgz && skill-hub
```

Skill Hub：

https://github.com/Backtthefuture/huangshu/tree/main/tools/skill-hub

![](assets/img_32c5971f3999.jpg)

写在最后

除了以上20+Skills外，你还可以到这几个skill市场自由挑选。

- https://skills.sh
- https://www.skillhub.club
- https://clawhub.ai

但更重要的Skills，还是来自于你亲手创建，根据自己的核心工作流创建5-8个高频Skills，详细实操内容见：《[Agent Skills从入门到精通](https://mp.weixin.qq.com/s?__biz=MzIwMTU5OTQ1Nw==&mid=2653726379&idx=1&sn=a9278d57b1f41e7835b918004e758f77&scene=21#wechat_redirect)》。

这也是为什么我更建议你，不要一上来就追求复杂，而是先做一件简单但有效的事：「把你过去一周重复做了3次以上的工作，拆出来。」

然后问自己两个问题：

- 这一步有没有明确的输入和输出？
- 有没有一部分是可以被稳定复用的？

如果答案是有，那恭喜你，这就是一个skill的雏形。

现在，就去创建吧。
