> 📎 来源: [开启新人生](https://mp.weixin.qq.com/s?__biz=MzYzOTA3NjAyOQ==&mid=2247483725&idx=1&sn=3969ba54bcda8700470728e1981802fe&chksm=f1eba6145f769fd029ab66b3074ad3731757a66d75fe0ae61e8b1fab54fcb6b45743c6cb7302&mpshare=1&scene=1&srcid=0513QljPmjjSZBIE7nJ7Sq6t&sharer_shareinfo=4d49ba49652753cab4f7106d788fb33e&sharer_shareinfo_first=4d49ba49652753cab4f7106d788fb33e) | 时间: 2026-05-13 15:40

---

Skills 是 Anthropic 推出但许多人尚未理解的一个功能。

它既不是外挂，也不是MCP，而是一份“说明书”——你告诉Claude遇到某类任务时该怎么做，它会在适当时机自行调用。

先说结论：没安装Skills的Claude，就像刚入职的清北员工——聪明，但什么都不懂你。

以下这15个是我每天都在用的。分为四类，看完你大概知道要先装哪几个。后续每日会分享3个X上新出的Skills,自学以及不想错过的朋友们可以关注下！

![](assets/img_2e4108f07d29.png)

—
▎第一类：内容生产的底层大脑

1｜frontend-design
官方出品，累计安装量超过27万次。
没装这个，你让 Claude 做任何网页、海报、落地页，出来的全是一个味儿：Inter 字体、紫色渐变、白底、方块卡片。
这被称为“分布收敛”——模型会回归到训练数据的平均值。
装了这个技能后，Claude会先掌握一套设计哲学再动手，输出的美感直接提升一个档次。

2｜canvas-design
专注于海报、单页设计及视觉艺术品的制作。
我用它做过产品宣传单、活动海报、朋友圈配图，比Canva那种模板套图有灵魂得多。

3｜theme-factory
10套预设的配色与字体主题，也能现场生成新主题。
制作演示文稿、报告或落地页时，一句话就能切换整套风格，省去无数次"再调整一下颜色"的反复修改。
—

![](assets/img_dfbf3f95b8d8.png)

▎第二类：牛马四件套

4｜docx
处理Word文档。合同、报告、信件、公文，所需的目录、标题、页码、表格均可制作。

5｜xlsx
处理Excel。清理杂乱表格、计算公式、生成图表、格式化，是我处理业务资料最常用的工具。

6｜pptx
制作简报。我会先用它撰写大纲，再用theme-factory套用主题，一份30页的提案简报半小时内就能生成。

7｜pdf
合并、拆分、旋转、添加浮水印、填表、OCR扫描件，所有PDF杂事它都能搞定。
这四个是一组的。只要涉及文件处理的工作，就全部安装，无一例外。

—

![](assets/img_39b4b20a6319.png)

▎第三类：

8｜file-reading

当你上传一个档案但内容还没进入对话时，这个Skill会告诉Claude该用什么方式去读——PDF怎么读、压缩档怎么解、图片怎么分析。

避免Claude对着binary档盲cat一通。

9｜pdf-reading

专门做PDF的深度阅读，包含文字抽取、表格提取、扫描件OCR、表单字段识别。

跟上面那个pdf是互补的——一个负责做，一个负责看懂。

10｜NotebookLM（Google出的，不是Claude的Skill，但我必须提）

把公司的SOP、合约、产品数据全部丢进去，它就变成一个只懂你公司的问答机器人。

免费。新人第一天报到丢给他用，省三个月带人时间。

—

![](assets/img_0f95f50c43ef.png)

▎第四类：

11｜systematic-debugging

这是我最想推荐给所有用Claude写code的人的一个。

AI抓bug的预设行为是乱试——改个变数、加行log、注释掉一块、复原、再试。

这个Skill强制Claude走一个四步骤协议：用最小测试重现bug、提出一个明确假设、只测那个假设、观察后迭代。

装了之后，Claude写code的debug能力会从「碰运气」变成「有方法论」。

12｜skill-creator

用来做Skills的Skill。

当你发现自己一直在重复对Claude讲同样的话，就表示你该把它做成一个Skill了。这个工具会带你一步步把经验封装起来。

13｜mcp-builder

教Claude怎么帮你做MCP Server。

现在是2026年，不懂MCP的人在AI这波会慢慢被甩开。这个Skill让你不懂也能做。

14｜brand-guidelines

把你公司的品牌色、字体、视觉规范存成一个Skill。

之后不管是谁用Claude出稿，出来的东西永远符合品牌规范。这对有固定VI的公司来说是刚需。

15｜internal-comms

专门写内部沟通——周报、月报、领导层更新、事故报告、FAQ、公司内刊。

我自己有多个任务同时跑，这个Skill帮我把「该同步给团队的东西」格式化，省下巨量的context switching成本。

![](assets/img_f2c7ccb0e37f.png)

—

▎最后，讲三个比「装什么」更重要的事

第一，装完你会忘记它存在。

Skill最大的敌人不是不好用，是你忘记在对的时候叫它。

我自己的做法是：在我的CLAUDE.md里写一句「遇到X类任务，自动调用Y skill」，让它变成预设行为，而不是靠我记得。

第二，Skill越少越好。

我看过有人装了50个Skill，结果Claude的context window被吃光，反应变慢，还会互相打架。

官方建议单个Skill控制在2000 token以内性能最好。宁缺勿滥。

第三，最强的Skill是你自己写的那个。

这15个是通用起点，但真正能让你跟别人拉开差距的，是你把自己这几年踩过的坑、总结的SOP、独门的方法论，写成一个只属于你的Skill。
