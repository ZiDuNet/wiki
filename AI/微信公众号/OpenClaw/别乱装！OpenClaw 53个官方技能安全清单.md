> 📎 来源: [愚公AI](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247484199&idx=1&sn=324f75d2fff99d9701738414cdc0bea8&chksm=fb51e3ab40e820613365ca0f3919578993e50c021393547a7ece056f3975264ca5fb677cef55&mpshare=1&scene=1&srcid=0513Cxa6tAkeBUjD4gdsclx0&sharer_shareinfo=5aaba777800ee8a3aa2d7e72b2980054&sharer_shareinfo_first=5aaba777800ee8a3aa2d7e72b2980054) | 时间: 2026-05-13 15:29

---

# 别乱装！OpenClaw 53个官方技能安全清单

最近OpenClaw圈被**ClawHavoc事件**刷屏：安全团队在ClawHub检出**341个恶意技能**，占比近12%，不少人因为乱装第三方技能导致数据泄露、权限越权、隐私暴露。

很多朋友装完OpenClaw就一头雾水：几万技能看着香，全开怕翻车，全关又浪费。今天直接给你一份**官方53个内置技能完整手册**，按场景分类、风险分级、分阶段安装，避开重复检测，安全又好用。

---

## 先搞懂：Tool和Skill不是一回事

- **Tool（工具）= 器官**：决定AI能不能做某事，比如read/write/exec，没有工具就像没手，啥也干不了。
- **Skill（技能）= 教程**：教AI怎么组合工具完成任务，**不新增权限**，只是一份使用说明书。

⚠️ 重要建议： 官方技能默认全部加载，**强烈建议用白名单skills.allowBundled**，只开你真正要用的，最小权限最安全。

---

## 53个官方技能｜分类+风险+用法速查

### 一、笔记管理（4个）

| 技能 | 平台 | 风险 | 适用场景 |
| --- | --- | --- | --- |
| obsidian | Obsidian | 低 | 本地笔记库管理，VM环境受限 |
| notion | Notion | 中 | 云端无限制，VM首选，需API Token |
| apple-notes | 苹果备忘录 | 低 | 仅Mac本地 |
| bear-notes | Bear | 低 | 仅Mac本地 |

### 二、任务待办（3个）

| 技能 | 平台 | 风险 | 说明 |
| --- | --- | --- | --- |
| things-mac | Things 3 | 低 | 仅Mac |
| apple-reminders | 提醒事项 | 低 | 仅Mac |
| trello | Trello | 中 | 团队看板，需API密钥 |

### 三、办公邮件（2个｜必看）

- **gog（必装）**：Google全家桶，Gmail/日历/Tasks/Drive一体，权限可随时收回，自然语言控办公
- **himalaya**：通用IMAP/SMTP，需存邮箱密码，**风险偏高**

### 四、消息社交（7个｜慎装）

这类技能可**完整读取历史+代发消息**，AI发的内容无法撤回，务必谨慎：

- 极高风险：wacli(WhatsApp)、imsg(iMessage)、bird(X/Twitter)
- 高风险：bluebubbles(跨设备iMessage)
- 中风险：slack、discord

### 五、开发工具（4个｜开发者必装）

- **github**：gh CLI管理Issue/PR/仓库，OAuth可控权限
- coding-agent：AI调度AI编码
- tmux：终端会话管理
- session-logs：历史日志检索

### 六、音乐/家居/外卖/创意/语音/系统等

这里只放**安全结论**，完整清单文末可对照：

- 音乐、智能家居、图像生成、PDF处理、摘要、天气**几乎全低风险**
- 外卖、语音通话、macOS UI控制**属高风险**
- **1password 极高风险**：授权即全库访问，非要用请建AI专用库

---

## 风险等级总览（心里有数）

- 低风险：30个 → 放心用
- 中风险：12个 → 用API，管好密钥
- 高风险：6个 → 敏感数据/支付/实时通信
- 极高风险：5个 → 隐私/密码/社媒全权，三思后行

---

## 新手安全安装路线｜3步不踩坑

### 第一周：必装3件套（零风险起步）

1. 1. gog：Google办公全能
2. 2. summarize：长文/PDF/播客快速摘要，每周省5小时+
3. 3. weather：免费无API，即用即走

### 第二周：按角色加技能

- 开发者：github + tmux + session-logs + coding-agent
- 笔记党：notion(云端) / obsidian(本地)
- 自动化玩家：搭配cron+message做每日简报

### 永久红线：这些尽量别装

- 社媒全权技能（wacli/imsg/bird）
- 1password密码库
- 涉及支付的外卖类
- 存储明文密码的邮件客户端

---

## 三条安全铁律（记住就不会翻车）

1. 1. **不用就不开**：白名单模式，只保留刚需
2. 2. **高权严审**：exec加审批，message只发自己
3. 3. **不可逆操作手动确认**：支付、发消息、公开发布，必须亲手点

---

## 最小安全配置（直接复制）

```
"skills":{"allowBundled":["gog","github","tmux","session-logs","weather","summarize","clawhub","healthcheck","skill-creator"]}
```

---

最后提醒：ClawHub第三方技能**一定要审源码**，官方53个才是最稳底线。安全用AI，效率拉满还不翻车～

```
您好，我是愚公既然看到这里了，如果觉得不错，麻烦随手点个赞、在看、转发三连吧～如果想第一时间收到推送，也可以给我个星标⭐～谢谢你阅读我的文章，我们下次再见！
```

**📚 往期文章精选**

[OpenClaw+Hermes双Agent联动案例](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247484056&idx=1&sn=6ac9db5b51186cc7b54a41c5f9e745ae&scene=21#wechat_redirect)

[40个Openclaw龙虾中文实战玩法，任你选！](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247484040&idx=1&sn=d9926b306159d398b1017c47a5c89f40&scene=21#wechat_redirect)

[Openclaw龙虾的最强竞争对手来了](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247484033&idx=1&sn=51b8ad315b58d4ca46905d190b5313de&scene=21#wechat_redirect)

[重磅更新！OpenClaw 4.7正式发布](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247484029&idx=1&sn=15256ede4a2e0728c328346584f19c1a&scene=21#wechat_redirect)

[你的龙虾终于能“上网冲浪”了！](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247484007&idx=1&sn=1236906b951721543181d85f19a5476a&scene=21#wechat_redirect)

[Openclaw龙虾产品实测排行](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247484015&idx=1&sn=be4455e523d03cf0f58c6c7a79d04d25&scene=21#wechat_redirect)

[龙虾OpenClaw使用飞书CLI 应用案例](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247483991&idx=1&sn=0a9cc8f7e223b1f80dd2469116d2f4d3&scene=21#wechat_redirect)

[Anthropic封杀OpenClaw龙虾调用](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247484011&idx=1&sn=32f3bbd129cce50e2b017503cb4eaa8c&scene=21#wechat_redirect)

[一夜之间！Claude Code 完全解锁版来袭](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247484003&idx=1&sn=bfb08b7097bd225ebe63eccf3a69d587&scene=21#wechat_redirect)

[14亿人的聊天入口正式支持接入OpenClaw](https://mp.weixin.qq.com/s?__biz=MzUzMTg5MzQ2Ng==&mid=2247483963&idx=1&sn=459a88abe5880dc56c5dc569ff3b32da&scene=21#wechat_redirect)
