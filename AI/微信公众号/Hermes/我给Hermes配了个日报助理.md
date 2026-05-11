> 📎 来源: [智行问道](https://mp.weixin.qq.com/s?__biz=MzY4NDE5MDg2OA==&mid=2247486350&idx=1&sn=74278cc3afb406f6ceff0ae658f688ea&chksm=f29040d7f363e904da2a1fba65b085b1df9b2037e595681b725c9db00a9b3c5f63baf601a4a0&mpshare=1&scene=1&srcid=05062kEZMtauxjU2lVKz0CuR&sharer_shareinfo=bd2325176f70f6568dc1a1ac30365800&sharer_shareinfo_first=bd2325176f70f6568dc1a1ac30365800) | 时间: 2026-05-06 04:46

---

智行问道 · 五一特辑 Day3

我给 Hermes 配了个
日报助理

每天早上8点，AI热点准时推送到微信

by 深海 | 智行问道 | AI实战

|  |  |  |
| --- | --- | --- |
| 2000字 | 3步操作 | 3分钟阅读 |

---

**🤔 先问个问题**

每天早上醒来，你做的第一件事是什么？我的是打开微信，看看AI圈有什么热点。但为了那两三条有效信息，每天花5-10分钟翻公众号，一个月就是2.5-5小时。这不是阅读，是信息焦虑。

**💡 所以我想让 Hermes 帮我做这件事**

每天早上8点，搜一遍全网AI热点 → 提炼5条摘要 → 推送到我的微信。我睁眼打开微信，消息列表里已经躺好了。3步搞定，不需要写代码。

**⚡ 第1步：创建日报Agent**

Hermes 里有预设的 OPC 模板：

hermes agent create --template one-person-company --name daily-report

**⚡ 第2步：配 Cron 定时任务**

hermes cron add \
--schedule "0 8 \* \* \*" \
--name morning-report \
--agent daily-report \
--input "搜索今天AI行业的头条新闻，整理成5条以内摘要，每条50字左右，中文，按重要性排序。"

**⚡ 第3步：验证效果**

等不到明早8点，先手动跑一次：

hermes run daily-report --input "搜索今天AI头条新闻，5条中文摘要"

几秒钟后，输出这样一份结果：

1. 谷歌发布Gemini 3.0，多模态推理提升300%

2. 欧盟通过《AI责任法案》最终草案

3. 英伟达GH400芯片量产，推理成本降80%

4. 中国发布全球首个AI医疗大模型标准

5. Anthropic推出Claude本地版

5条，每条一行，花了不到30秒，成本¥0.02。这要是自己翻公众号搜，至少10分钟。

**🤖 推送到微信**

定时任务的输出会自动通过微信网关推送到你微信。前提是网关在跑：

tmux attach -t hermes

看到 weixin connected 就正常了。以后每天早上8点，微信自动收到一条AI早报。

---

**💡 还能怎么玩**

🔹 行业日报：把"AI行业"改成"光伏行业"
🔹 竞品监控：定点搜几个竞品公司的动态
🔹 晚间复盘：再配一个Cron，晚上10点推送总结

**🎯 小结**

✅ 3条命令，搭好日报助理
✅ 每天8点自动推送到微信
✅ 一天成本¥0.02

---

📌 回复「日报」获取 Cron 配置模板

📖 推荐阅读

▶[别人挤在景区看人头，我让Hermes用数据扒出了5条冷门路线](https://mp.weixin.qq.com/s?__biz=MzY4NDE5MDg2OA==&mid=2247486245&idx=1&sn=d817fc7aa030b057fada0d4a106f2433&scene=21#wechat_redirect)

▶OPC一人公司成本差237倍

![](assets/img_254ca646ea4d.jpg)

关注「智行问道」

AI提升办公效率 · 赋能千行百业

---

智行问道 · 用AI重新定义工作效率
