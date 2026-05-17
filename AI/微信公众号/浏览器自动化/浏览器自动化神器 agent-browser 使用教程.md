> 📎 来源: [iLvc](https://mp.weixin.qq.com/s?__biz=MzI5NDczNjA4OA==&mid=2247491309&idx=1&sn=2d874f82095f3d3f522c17a306971897&chksm=ed293cbbb891b4336f5b8c0563b9e8bd2e8c1325fc5772f52f8670f5adc4c933840d8822daf4&mpshare=1&scene=1&srcid=0517Yoip0R2jMaphoGLTFqb4&sharer_shareinfo=1cb7b06b38d8aaa0c89b713a53963469&sharer_shareinfo_first=1cb7b06b38d8aaa0c89b713a53963469) | 时间: 2026-05-17 16:24

---

![](assets/img_abd348e76b86.png)

这是一篇 agent-browser 浏览器自动化教程，引入案例“微信公众号自动化添加贴图工作流”。简直就是浏览器自动化的“神器”。

早在上个月，[学习 agent](https://mp.weixin.qq.com/s?__biz=MzI5NDczNjA4OA==&mid=2247490943&idx=1&sn=2def9ca3af8df31bf73486b471ec66a9&scene=21#wechat_redirect) 时，用 anygen 生成了一个`mini-opencalw-mvp`，在实践的过程中，想着能不能用 agent 来代替我现在繁琐的操作呢？还能做一个适合自己用的 agent。

我有一件每天都要做的事情，给穗穗记录她的日常，记录她的长大，从 day 52 一直到今天。

大致流程如下： 

- 1.公众号助手添加一个 Day XX 的文章草稿；

- 2.语音记录发生的事情； 

- 3.在电脑上登录微信公众号找到 Day XX 的文章，复制到 obsdian 做备份； 

- 4.打开 [anygen.io](https://mp.weixin.qq.com/s?__biz=MzI5NDczNjA4OA==&mid=2247490505&idx=1&sn=3087dff176b8a25fafb60bf569bd9bc1&scene=21#wechat_redirect),复制内容 使用 suisui-comic-chapter skill 生成漫画； 

- 5.手动下载所有的图片； 

- 6.给图片批量改文件名称；

- 7.在电脑上登录微信公众号，发表贴图，上传文件，填写信息等一系列操作，然后扫码发表；

给穗穗发表的内容，有贴图也有文章，如果是文章的话，还有一步时把录音的内容，让 AI 修改成可读性的内容。

上面的流程单个看起来也没有什么，但我一般都是隔一段时间去操作一次，所有就变成巨无聊的事情，我TM就成复制粘贴点点点的机器人了。

为什么不能用 agent 来实现自动化呢？说干就干。

经过AI调研，发现 agent-browser 是一个专门给 agent 用的浏览器自动化工具，agent 优先；

之前做的`mini-opencalw-mvp` agent 模型用的是，白山算力的免费模型`DeepSeek-R1-0528-Qwen3-8B`支持工具调用，刚好可以作为 agent 的基模；

安装 angent-browser（推荐） ：

> npm install -g agent-browser agent-browser install # Download Chrome from Chrome for Testing (first time)

如果你是用 openclaw 之类的 agent，可以安装 skill：

> npx skills add vercel-labs/agent-browser

安装完之后，让 AI 写个 agent-browser 的工具函数，我自己是这么干，为了叙述方便，后续不再解释 code 方面的内容，因为 代码都是 AI 写的，我用的 trae 国内版，对小白来说已经够用了。

在 AI 一顿试错之后，加之对 openai 调用不甚理解，导致后面压根没有办法进行到下一步，然后建议以脚本的方式去做固定化的操作步骤。

虽然代码都是 AI 写的，但是 也得把操作过程告诉 AI，我这才去详细看了 agent-browser 的文档，指令都很清晰，理解无障碍。如果不会就问 AI。

所谓的浏览器自动化，就是模拟人的操作，人工是怎么操作，那么 AI 就是怎么操作。

回到上面的步骤，把公众号里草稿复制到本地这个流程，详细每步如下：

- 1.打开浏览器，进入`https://mp.weixin.qq.com` ；
- 2.扫描登录，进入首页；
- 3.点击`全部草稿`，进入草稿箱；
- 4.搜索文章标题；
- 5.找到文章，移到文章上；
- 5.显示操作按钮，点击`编辑`按钮的图标，进入编辑页面；
- 6.复制内容；
- 7.打开 obsdian，新建一个Day xx 的文件；
- 8.粘贴内容；

对应的贴图流程操作如下：

- 1.打开浏览器，进入`https://mp.weixin.qq.com` ；
- 2.扫描登录，进入首页；
- 3.点击`贴图`，进入新建贴图页面；
- 4.点击上传，本地上传图片；
- 5.添加标题；
- 6.添加内容：标签和描述
- 7.添加连接，选中最新发表的内容，确定；
- 8.添加合集，输入合集名称，点击合集名称，确定；
- 9.保存为草稿；

看着操作内容也不多啊，就8、9步而已，如果是要添加 10个贴图呢？就是 80、90步，时间更是不是 1+1=2 ，而是 1+1=3，=5的倍增，人毕竟不是机器，不可能毫无情绪的执行任何重复的指令。

先来看看，现在来看下我使用 agent-browser 之后的流程有变成了什么样：

- 1.agent-browser 打开浏览器，进入`https://mp.weixin.qq.com` ；
- 2.🙂扫描登录，自动 进入首页；
- 3.agent-browser 点击`贴图`，进入新建贴图页面；
- 4.agent-browser 点击上传，本地上传图片；
- 5.AI生成标题 agent-browser 添加标题；
- 6.AI生成内容 agent-browser 添加内容：标签和描述
- 7.agent-browser 添加连接，选中最新发表的内容，确定；
- 8.agent-browser 添加合集，输入合集名称，点击合集名称，确定；
- 9.agent-browser 保存为草稿；

我唯一需要做的就是扫描登录，当然也可以用账号密码登录，我单纯是没有设置 账号、密码登录；当然图片肯定要准备好；

接下来我们来实操，并学习一些基础指令。

`agent-browser open  # 启动浏览器并跳转指定网址（别名：goto、navigate）`

`agent-browser click  # 点击元素（加 --new-tab 在新标签页打开）`

`agent-browser fill   # 清空输入框并填入文本`

`agent-browser type   # 向元素内逐字输入文本`

`agent-browser press  # 按下按键（回车、Tab、全选 Ctrl+a 等）（别名：key）`

`agent-browser hover  # 鼠标悬浮在元素上`

`agent-browser snapshot # 获取带元素引用的无障碍访问树结构`

`agent-browser snapshot -i # 仅提取可交互元素（推荐使用）`

`agent-browser upload   # 上传文件到指定上传控件`

`agent-browser close # 关闭浏览器（别名：quit、exit）`

上面的指令中，很多指令有``,这是什么意思呢？其实就是我们操作的 DOM 元素，agent-browser 提供可视化操作 Refs。

> 官方介绍 :引用标识 Refs（推荐用法）

> Refs 可以基于页面快照**稳定精准地定位元素**，非常适合 AI 智能体使用。

> 1. 获取带引用标识的页面快照

> ```
> agent-browser snapshot
> ```

> 输出示例：

> - 标题 "Example Domain" [ref=e1] [level=1]
> - 按钮 "Submit" [ref=e2]

> 2. 使用引用标识操作元素

> ```
> agent-browser click @e2                   # 点击该按钮
> ```

> 为什么要用 Refs？

> - **确定性强**：引用标识精准绑定快照里的唯一元素
> - **执行更快**：无需重新查询 DOM 节点
> - **适配 AI**：大模型可以轻松解析并可靠调用 Refs

在实操的过程经常发现想要的操作的内容，在 Refs 中没有，那么就需要用到其他方式去定位一个元素。如果之前做过爬虫，对这个肯定不陌生。

agent-browser 还支持：**CSS selectors** 、**Text & XPath**、**Semantic locators**。

怎么用呢？也是很简单的，在浏览器页面，右键-检查，找到对应的元素，右键-复制，如图所示。

插入图片

好了，学了那么多，总该到实操了吧。

嘿嘿(¬◡¬)✧，其实，实操就是一个实践和调试的过程，把人工操作转化为 agent-browser 提供的指令，这就需要一点时间来弄啦。

调试贴图的工作流，就废了我四五个小时，尤其是卡在上传文件这个步骤，找了 N 次方案。当我遇到很难处理，不知道用哪个时，可以把整个 HTML 发给 AI，让 AI 分析。

下面是我调试成功后的 agent-browser 的指令流，当然还是需要配合 pytho 脚本，去实现是工程化，并且我还引入了 AI 功能，自动生成标题和内容描述。

```
// 贴图工作流
```

参考链接：

- agent-browser：https://agent-browser.dev/

- 白山算力：https://ai.baishan.com/auth/login?referralCode=hL1ZmwiXnv
