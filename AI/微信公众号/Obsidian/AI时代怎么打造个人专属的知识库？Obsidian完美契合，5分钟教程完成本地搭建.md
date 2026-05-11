> 📎 来源: [微糖小二](https://mp.weixin.qq.com/s?__biz=MzE5ODA5OTY1MQ==&mid=2247483818&idx=1&sn=bf355dfd6074c0b7e031b5f64ba988fd&chksm=9784f191cab2d287a6259040551925ffaa5a2b8815e6497670c4142247e07b166e20d0f659bd&mpshare=1&scene=1&srcid=0510mDR44DSzQnoUe2YqSU6z&sharer_shareinfo=6fc22fd93a5e39b500d0f7272063b0a1&sharer_shareinfo_first=6fc22fd93a5e39b500d0f7272063b0a1) | 时间: 2026-05-10 15:13

---

小二准则【不为学习而学习，严格遵循**二八法则**】。

在信息爆炸的时代，对于知识管理有很多选择，语雀，飞书，notion，logseq等等。这么多工具，怎么选？

如果是在之前，可能每个工具都有自己的特点，可以根据自己的需求进行选择。但是，在AI爆发式增长的今天，在未来，AI将和每个人息息相关，所以，需要一款和AI关联性更强的知识管理软件，接下来说一下使用Obsidian的几个理由。

# 为什么要用Obsidian

🚀  本地存储 ，掌握管理权 用过笔记本的都知道，最痛苦的就是笔记迁移，因为软件的兼容性问题，在迁移过程中，原本的格式发生各种问题，不得不人工再次整理。而Obsidian产生的笔记文件都是标准的 markdown纯文本文件，存在本地文件夹，只要有笔记软件支持markdown语法，就能完美展现。 同时，因为是存储在本地，不用担心因为网络问题，无法打开或者查看笔记。

那么，问题来了，既然是本地存储，换电脑了，怎么办？

🚀 支持远端同步 Obsidian 支持同步远端，如 iCloud、Dropbox、OneDrive、Git 等任意第三方远程存储服务，不用担心本地数据丢失以及换电脑使用。

🍂 图谱视图（Graph View） 在笔记中，存在互相引用的情况，通过图谱视图，可以非常直观的查看笔记之间的联系。非常适合构建第二大脑、学术研究、深度思考。

🍂 丰富的插件生态 除此之外，Obsidian插件生态丰富，有官方的，也有社区的，可以满足各种定制化需求。

对Obsidian 有了一个基本了解后，接下来，开始安装步骤。

# 开始搭建本地知识库

- 官方下载连接进行下载安装 https://obsidian.md/download
- 创建知识库 在打开的页面可以看到有个Create new vault的按钮，vault就是知识库，直接创建就行。

![](assets/img_1064b9bbece2.png)

- 创建笔记 在左侧的导航栏，可以创建文件和笔记。

![](assets/img_2c36ea63d35e.png)

- 笔记编辑 Obsidian支持Markdown语法，有的朋友可能比较陌生，不用担心，上手难度一颗星。看一遍基本可以满足80%的编辑需求。

这里贴上一份markdown语法学习指南

https://www.runoob.com/markdown/md-tutorial.html

- 玩转obsidian知识图谱 假设当前笔记如果需要引用历史的笔记，可以通过下面这个语法进行引用

java

```
[[需要引用的笔记]]
```

如图

![](assets/img_61f3cfc5510b.png)

查看知识图谱，点击左侧导航栏的open graph view

![](assets/img_5a9564689dab.png)

 因为现在知识库的笔记比较少，这边再贴一张效果图 

![](assets/img_34c365e95c86.png)

 以上，基本完成本地知识库的搭建，接下来看看怎么把本地知识库同步到远程，方便随取随用。  

# 远程备份，随地可用

前面已经讲过，obsidian支持官方的远程同步，但是要付费，不差钱可考虑，这里讲一下怎么同步到第三方远程服务。

obsidian支持同步到云服务器和github，以因为购买云服务存储也需要付费，采用github作为远程同步。 注意：**github是国外网站，网络不是非常稳定，可以使用国内的gitee平替**

首先，下载git并安装。(git下载地址)[https://git-scm.com/install/windows]，按照提示一步步操作就好，没有特别配置。

开始配置SSH公钥，这个SSH公钥是本地安装的git同步到gitee的凭证，需要在本地创建，然后在github/gitee进行添加，这里以github为例。

通过下面这个命令，在本地的终端创建ssh key，执行命令一直按回车就行

js

```
ssh-keygen -t ed25519 -C "Github ssH Key"
```

执行完后，找到id\_ed25519.pub文件或者直接执行下面这个命令，并复制如下部分的内容

js

```
cat ~/.ssh/id_ed25519.pub
```

![](assets/img_38b9b3d15a7d.png)

 注意，\*\*不要全部复制\*\* 

然后，打开(github地址)[https://github.com/]/(gitee地址)[https://gitee.com]，如果没有账号，需要注册。

登陆github后，点击个人头像，找到Settings 

![](assets/img_03971852e79b.png)

找到SSH and GPG keys这一栏，并new 一个新的SSH密钥 

![](assets/img_4a371af284bb.png)

把在本地生成的ssh key复制到下面，title可以自定义 

![](assets/img_cad0bf06d6d8.png)

开始创建本地仓库，注意仓库权限选择私人，否则其他人是能够访问你的仓库，数据容易泄漏，创建的时候，**一定要add Readme**否则后面会报错 

![](assets/img_0c6567e64c09.png)

把远程仓库克隆到本地 

![](assets/img_6595a8e46305.png)

本地终端，找到本地知识库需要保存的目录，根据自己需要，执行克隆命令

js

```
git clone [[刚刚复制的远程仓库的地址]]
```

执行完成后，可以在本地目录下看到刚刚复制的仓库 

![](assets/img_f8cac637f5b6.png)

打开克隆的知识库目录 

![](assets/img_66b656df10d7.png)

打开后，可以看到知识库名称 

![](assets/img_30aa2138a208.png)

 安装obsidian 的git插件，点击左下角的设置，然后找到Community plugins，点击Browse 

![](assets/img_36673cce695e.png)

搜索git并安装 

![](assets/img_b795d0321161.png)

设置Git，在设置的左侧进行配置，分别设置了自动同步和拉取的时间间隔，如果不清楚，按照小编配置即可，1分钟自动同步到远端，每天从远端拉取一次 

![](assets/img_7909d11f8f18.png)

手动同步怎么操作，同样，在导航栏左侧 

![](assets/img_eafd5fe7a1e6.png)

如上，已经基本完成配置工作，开始测试远程同步的功能，新建一个测试笔记

![](assets/img_944bd3b2516a.png)

先commit，如下会提示Commited，表示提交成功 

![](assets/img_908318a2d9b3.png)

再push到远端服务 

![](assets/img_79447d9968b8.png)

查看远程github仓库 

![](assets/img_fc9943d41631.png)

发现已经成功同步，到此，完成知识库远程备份。

我是小二，一线互联网大厂架构师，AIGC路上不断摸索。

如果文章有帮助，帮忙点个赞，**关注**不迷路。

往期推荐

[阿里云部署OpenClaw使用百炼套餐太贵?15分钟接入智谱Coding Plan](https://mp.weixin.qq.com/s?__biz=MzE5ODA5OTY1MQ==&mid=2247483792&idx=1&sn=a8f8b26e7392ed192bc543be5bd4dd35&scene=21#wechat_redirect)

[网络安全看不懂？5分钟读懂Https基本原理](https://mp.weixin.qq.com/s?__biz=MzE5ODA5OTY1MQ==&mid=2247483771&idx=1&sn=a79866bb327c993ec639efe21a618199&scene=21#wechat_redirect)
