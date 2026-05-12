> 📎 来源: [Draco正在VibeCoding](https://mp.weixin.qq.com/s?__biz=MzI2NzM4MTQwMg==&mid=2247496046&idx=1&sn=4d36164231789fa1641ad8b40b761df9&chksm=ebb0bdb16967fbb1c4be76992ddf7d5b93c4c30f8d983251a6a95b03f87631b4585a55b096ba&mpshare=1&scene=1&srcid=05136a8pOQP6b3xUkqw60I2Q&sharer_shareinfo=e1fa82217a059479ed5c191acff2349f&sharer_shareinfo_first=e1fa82217a059479ed5c191acff2349f) | 时间: 2026-05-13 01:53

---

这个项目叫9Router，你可以把它看成是OpenRouter的本地版，或者CC Switch的超级版。

看看这阵仗，基本上把最重要的大模型提供商和Agent都给集成进来了！

![](assets/img_e7901ad9eeec.png)

![](assets/img_ba6e0bab1983.png)

使用方法很简单：

1.

把9Router的Github仓库（https://github.com/decolua/9router）喂给你的一个已经在正常工作的Agent（我用的KIMI Code）

> 记得提前建个空的9Router文件夹，然后用Agent打开这个空文件夹

![](assets/img_040c32211587.png)

2.

十来分钟之后，Agent就给你搞定了，会返回一个localhost的地址，比如“http://localhost:20128/login”，用浏览器打开这个地址

> 密码在.env 文件中，可以自己改

![](assets/img_25154be277f8.png)

3.

登录进去之后是这个样子：

![](assets/img_ae0f68a9f05f.png)

4.

先不用管首页这个Endpoint，一般不需要改，直接点击左侧第二个Tab “Providers”：

![](assets/img_60b5199a8d18.png)

5.

如果想用免费的token，你能看到OpenCode Free那里有个“Ready”的绿色标志，点进去看一眼：

![](assets/img_147cb1e4292a.png)

6.

把上图中的“oc/deepseek-v4-flash-free”的加号点一下，让它变成可用的大模型，变成下图这样：

![](assets/img_2f9ed384c33e.png)

7.

然后，点击左侧Tab中的“CLI Tools”，然后选一个你平常使用比较多的Agent，比如我选择Hermes Agent，点击它：

![](assets/img_98f762df028e.png)

8.

然后在展开的面板中，点击Default Model最右侧的Select按钮：

![](assets/img_fe0e13b0a873.png)

9.

点击选择OpenCode Free下面的“deepseek-v4-flash-free”

![](assets/img_48ffe349e829.png)

10.

然后点击“Apply”

![](assets/img_654bf63185e8.png)

11.

如果配置成功，就会出现下面这个绿条

![](assets/img_1d1f611357be.png)

12.

然后回到你刚才选择的Agent，问它一嘴目前它知不知道自己背后用的啥模型：

![](assets/img_df68cbfe3eb7.png)

> 恭喜你！免费token获取成功！

13.

除了免费的token，你也可以添加其他的大模型Providers，比如进入KIMI，点击“Add Connection”

![](assets/img_84859ddd3779.png)

14.

把API KEY填进去，Name那里随便写个kimi，然后点击“Save”：

![](assets/img_42d66fda933c.png)

16.

然后应该能看到Connections那里是绿色的“Active”：

![](assets/img_ee386dc4785e.png)

17.

然后这次我选择在OpenCode里启用KIMI的模型：回到CLI Tools中选择OpenCode，然后点击Add Model

![](assets/img_abd9d299ac7a.png)

18.

然后选择Kimi K2.6

![](assets/img_fa58bc1461fd.png)

19.

Subagent Model那里也选择Kimi K2.6，然后点击Apply按钮：

![](assets/img_e81c420e8c48.png)

20.

OpenCode+Kimi K2.6也搞定了：

![](assets/img_15277874de56.png)

21.

然后打开OpenCode验证一下，没毛病9Router提供的kimi/kimi-k2.6：

![](assets/img_ce197fa96882.png)

22.

还有个有趣的功能叫Combo，你可以添加多个模型，前面的失败了9Router会自动fallback到后面的模型上去，使用起来和其他模型一样直接在Agent那里添加Model就行：

![](assets/img_2508851bf29b.png)

![](assets/img_6479e1fe19e4.png)

23.

最后，让Agent将9Router的服务最好持久化：

> 当然，也可以走docker容器的模式，看自己喜好吧

![](assets/img_41cbeeb670d3.png)

24.

模型用量可以到Usage里随时查看

![](assets/img_4af6511cc0cb.png)

OK，走到这里，9Router就算稳定跑起来了。

除了大模型，9Router也把图片、语音、Embedding、Web/Search的Providers列出来了（就差视频生成）：

![](assets/img_eff5e2ac4dec.png)

![](assets/img_3100b97dc3f5.png)

![](assets/img_fd4b232d869b.png)

![](assets/img_7b83fa6d792e.png)

![](assets/img_b78bc1ea04dc.png)

此外，对于Github Copilot、Antigravity、Kiro，你还可以使用MITM路由劫持的方式来强迫这几个Agent走9Router，具体怎么用，可以直接问帮你安装9Router的那个Agent，由于我用不到，就不在这里展开了...

![](assets/img_2f6cf7879620.png)

![](assets/img_0f7231a48803.png)

9Router还有一些其他能力，就留给大家自己探索吧~

Have fun！
