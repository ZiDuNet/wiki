> 📎 来源: [AI李子](https://mp.weixin.qq.com/s?__biz=Mzk3NTgzNjk4Ng==&mid=2247484003&idx=1&sn=5f6bed903a62f838cf854ce0d715cec5&chksm=c575639590716968151fb4145d7bf21f8466023d1e6f5bcb4a78c74a5b55630d6ed5959f975b&mpshare=1&scene=1&srcid=0422J6OU0sbgx8YUHllmDB5Y&sharer_shareinfo=1bccbcb3103774be14f1631cfaccc01f&sharer_shareinfo_first=1bccbcb3103774be14f1631cfaccc01f) | 时间: 2026-04-22 17:35

---

![](assets/img_5b7b83bfc6cb.jpg)

# 1.背景信息

最近一段时间，新出了一个爆火Agent，叫hermes。他的名字很有意思，取自古希腊神话众神的信使，宙斯的儿子赫尔墨斯。由于他的架构，尤其是他的长效记忆架构，并自动根据你和他对话的过程生成skills等，号称自进化的agent。目前他在github上已经有快9.4万star了，还在高速增长中。今天咱们就来从部署到实践全方位体验一下。

![](assets/img_48529f4d43b3.png)

# 2.部署方式和配置

## 2.1基础环境准备

目前hermes三个平台（mac、linux、win）都支持，其实就是一行命令

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

今天主要说云端liunx和本地window平台的部署方式

## 2.1.1云端liunx

这个是目前最简单的一种方式，我用的是腾讯云，先到腾讯云买个最便宜的服务器，一个月大概几十块钱，我的配置是这样的。

![](assets/img_bc8347c597ea.png)

云端安装系统时直接用他们的模板建站，省去再安装hermes的过程（国内的网真的是太慢了）

![](assets/img_c2cabb880285.png)

安装好后，免密登录，他默认是root,需要切换账户到aentuser，因为腾讯把hermes装在这个账户下

![](assets/img_1db72863a981.png)

这就OK了

![](assets/img_57d07f733dfb.png)

先更新 hermes update

![](assets/img_7d452d0f9f95.png)

配置 hermes setup,因为是全新安装，不需要导入数据，选n就行。

![](assets/img_3a2515641960.png)

然后选择他推荐的quick setup就可以，接下来是选择模型商，把你自己的api和key填入就可以，他目前国内主流的都都支持，也可以自定义，最后一个就是。

![](assets/img_6c15c2943ded.png)

配置完，就到了设置IM连接。

![](assets/img_b6a5e9b57192.png)

这里我选择飞书，其它平台大同小异

![](assets/img_f937fff0160b.png)

然后选择，创建机器人，现在很简单了

![](assets/img_98b37856f0f9.png)

直接ctrl+点击这个链接

![](assets/img_5d950cbe3b5b.png)

然后他就会跳到飞书的后台，如果你有bot就选择你自己的，没有新创建一个

![](assets/img_76ad08a57666.png)

![](assets/img_3098515b3982.png)

选第一个，通过配对方式，和openclaw差不多

![](assets/img_ef5731a5a739.png)

全部按推荐的走，然后重启网关和启动

![](assets/img_869585c2f963.png)

然后就ok了

![](assets/img_740353e742da.png)

![](assets/img_06bf9f3e6d47.png)

还有最后一个，就是和飞书连接。

输入 /quit 并按回车退出 TUI 界面，回到命令行

启动网关，这个网关是和你的IM随时通信呢，将他安装为系统服务

hermes gateway install

![](assets/img_9a6ec374c274.png)

然后是启动服务：hermes gateway start

![](assets/img_b9dceb8db81d.png)

回到飞书，随意发个信息取得配对码

![](assets/img_3e5bdec06bf0.png)

然后直接把这个发给服务端

![](assets/img_03bd9b0d6c14.png)

这就完全好了，可以和飞书对话了。

![](assets/img_51f6250f8073.png)

可以给他设置风格，改一下soul.md文件

![](assets/img_38d63d70dbd6.png)

## 2.1.2本地win平台部署

其实win平台也是要在他自己wsl虚拟机中运行

随便找个文件夹右键点击在终端打开，启动Powershell。

![](assets/img_f216457adc44.png)

其实就是在win下把系统自带的虚拟机linux环境准备好。

执行以下命令安装ubuntu版本的linux，很简单，就一条命令

wsl -setup

![](assets/img_37fad861ed55.png)

安装完成后，会自动启动，用户名已经用的是你window的用户名，设置两次密码就行，这里一定注意，linux下输入密码是不会显示的，输入完成后回车就行，这也是为了安全。

![](assets/img_6ccea97c8b73.png)

如果不想安装到C盘，执行以下命令，我这里选择安装到D盘，第一步是创建一个文件夹，第2部是安装ubuntu

New-Item -Path D:\WSL\Ubuntu -ItemType Directory -Force

wsl --install -d Ubuntu --location D:\WSL\Ubuntu

如果觉得命令行麻烦，还有一个简单的办法就是到微软应用商店找ubuntu,效果是一样的

![](assets/img_d8bdcb7e7a59.png)

安装完成后，会自动启动，用户名已经用的是你window的用户名，设置两次密码就行，这里一定注意，linux下输入密码是不会显示的，输入完成后回车就行，这也是为了安全。

安装hermes

安装就更简单了，前面说的，在终端执行一行命令

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

如果网络不太好，用这个镜像加速命令

```
curl -fsSL https://ghproxy.net/https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

![](assets/img_c35a82ef942c.png)

安装完成后启动hermes就可以了，其它部分和linux的完全一样，就不截图了。

# 3.写在最后

这一篇是完全部署教程，让我想起了今年1月的时候，龙虾刚火，各种BUG，部署也是相当麻烦，但随着开源社区的持续开发，后边越来越容易，越来越可视化。hermes也一样，看起来麻烦，后边会越来越简单。

后边再继续探索他的使用，期待和大家进行深入的交流，有什么问题，随时给我留言。

最后老规矩，一图总结全文。

![](assets/img_d380a0f4ec50.png)
