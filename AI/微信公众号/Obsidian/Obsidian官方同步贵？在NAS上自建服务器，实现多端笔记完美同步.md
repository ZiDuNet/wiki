> 📎 来源: [Stark324](https://mp.weixin.qq.com/s?__biz=MzkyNjU2MzIzNQ==&mid=2247507848&idx=1&sn=fa525363f0576d9d7f3074be24cc8f05&chksm=c3ebd7b4869b5190afe0f97a8225bb745cd7f65cc453c1ddeeaffd473573d40cc00c9ef10a4a&mpshare=1&scene=1&srcid=0521nxEeQicJMf4FyGKJKH2h&sharer_shareinfo=da700945969b5cb6a60300176196c724&sharer_shareinfo_first=da700945969b5cb6a60300176196c724) | 时间: 2026-05-21 15:10

---

# Obsidian官方同步贵？在NAS上自建服务器，实现多端笔记完美同步

哈喽小伙伴们好，我是Stark-C~

说到Obsidian很多小伙伴都相当熟悉了吧？作为当下最受欢迎的知识管理软件之一，它无论是写日记、做项目管理，还是搭建个人知识库，Obsidian 都能给你足够的自由度和可玩性。

它最大的亮点就是“本地优先”，也就是说它所有数据都保存在本地，隐私安全方面非常高，但同时也带来了多端同步困难的问题。

虽说Obsidian有官方同步服务，不过除了收费小贵，貌似对对内的网络环境也不太友好（服务器在国外）。

所以今天就为大家分享一个可以部署在NAS上的免费 Obsidian 同步解决方案：Fast Note Sync！

## 关于Fast Note Sync

![](assets/img_2166d97d7f63.png)

Snipaste\_2026-05-19\_09-48-40

🔺Fast Note Sync是一款免费开源、可私有化部署的 Obsidian 多端实时同步 & 备份插件，支持 Mac、Windows、Android、iOS，并提供多语言界面，并通过 WebSocket 实现毫秒级同步。

需要说明的是它需要搭配独立的服务端（Fast Note Sync Service）使用，插件负责本地监听与同步，服务端负责存储、版本管理、配置同步等功能，并且服务端可NAS私有化部署。

项目Github地址：https://github.com/haierkeys/obsidian-fast-note-sync

服务端Github地址：https://github.com/haierkeys/fast-note-sync-service

**项目特色亮点：**

1. 多端实时同步（毫秒级）：使用 WebSocket 协议，笔记在不同设备间几乎“秒更”，支持文本、图片、视频、音频等附件同步；
2. 完整的附件与配置同步：除笔记外，还能同步主题、插件、快捷键等 

   ```
   .obsidian
   ```

    配置，解决换设备后环境不一致的问题；
3. 私有化部署，数据完全自控：服务端基于 Golang + WebSocket + SQLite + React 构建，可部署在 NAS、软路由、云服务器等设备上；
4. 极简配置：插件端只需粘贴服务端生成的远端配置即可使用，桌面端支持“一键导入配置”；
5. Web 管理后台：可在网页端直接查看、编辑笔记、管理用户、生成配置；
6. 笔记历史版本 & 回收站：可查看任意笔记的完整修改记录，支持恢复误删内容。

# Fast Note Sync Service部署

前面说过，Fast Note Sync需要搭配独立的服务端（Fast Note Sync Service）使用，并且服务端可以私有化部署，所以接下来我以极空间NAS为例，为大家展示详细的操作过程。

![](assets/img_f93ad9eaeb33.png)

🔺打开极空间NAS文件管理器，在Docker目录下新建一个“Obsidian”的文件夹。

![](assets/img_85238e2d54dc.png)

🔺然后点击极空间NAS的“Docker”应用，点击【Compose】 > 【新增项目】。

![](assets/img_e574bdf7b626.png)

🔺在“创建项目”页面自定义项目名称，“存储位置”需要手动选择我们前面新建的Obsidian文件夹，勾选下方的“所有合规文件夹添加最大读写权限”，最后输入以下 Docker Compose 配置信息后点“创建”按钮：

```
services:  fast-note-sync-service:    image: haierkeys/fast-note-sync-service:latest    container_name: fast-note-sync-service    restart: always    ports:      - "9100:9000"  # 项目端口，冒号前面不要冲突    volumes:      - ./storage:/fast-note-sync/storage      - ./config:/fast-note-sync/config
```

以上代码需要修改的地方就看我给到的中文注释，其它的直接保持默认即可。镜像的拉取需要自行解决网络问题，粘贴到自己的NAS这边之前建议使用AI工具优化一下，以防止格式问题造成的部署失败。

![](assets/img_634ff0c1bf26.png)

🔺项目部署之后看到显示“运行中”，就说明可以使用了，我们也可以点击项目的“远程连接”测试一下。

![](assets/img_ff1069410244.png)

🔺如果能正常显示Fast Note Sync页面，就说明没有问题。这里建议大家可以直接注册一个用户名和密码，稍后直接使用即可。

![](assets/img_87333831d992.png)

🔺这里说明一个情况：因为同步必然会涉及到外网使用场景，所以我们需要提前做好外网访问的准备。

如果有公网IP，直接使用Lucky做一个反向代理就可以了（具体教程全网很多，自己搜便是），如果是使用NAS自己的反向代理，需要在配置反向代理的时候启用Websocket支持。（Lucky的反向代理是默认就支持WebSocket的）。

如果没有公网IP需要自行搞定内网穿透，极空间虽说自带“节点小宝”内网穿透服务，但节点小宝是P2P直连，不支持WebSocket，所以外网访问的时候会同步失败。至于其它的内网穿透方案请自测，据说Tailscale是没问题的。

## Fast Note Sync配置

![](assets/img_7b700ee1ce97.png)

🔺搞定外网访问之后，我们打开项目Github主页，点击"Releases"。

![](assets/img_be1d933b4d1c.png)

🔺选择最新的“alpha”版本展开，下载对应的zip压缩包文件。

![](assets/img_8696c96d8572.png)

🔺zip压缩包文件下载到本地之后我们需要将其解压，得到一个文件夹（稍后会用到）。

![](assets/img_eefc4e3cb554.png)

🔺这个时候我们就可以打开我们电脑上的Obsidian程序，点击“设置”按钮。

![](assets/img_6146eb43f40d.png)

🔺然后在“第三方插件”里“关闭安全模式”。

![](assets/img_3f5ef81822e9.png)

🔺继续点击“已安装插件”后面的文件夹图标。

![](assets/img_310795a7ff8b.png)

🔺点开以后会打开一个文件夹（其实就是Obsidian的插件库），这个时候我们把前面解压得到的文件夹直接拖过来。

![](assets/img_729f22d88de1.png)

🔺之后在点击“已安装插件”的刷新按钮，就能看到Fast Note Sync插件加载过来了，然后我们手动打开，在点击“设置”。

![](assets/img_539d16d4b56c.png)

🔺这个时候我们需要使用具备外网访问的链接打开Fast Note Sync服务端（比如说我这里直接使用的是前面准备好的反向代理链接），输入用户名和密码登录进来之后，点击右上角的用户图标，选择“授权客户端”。

![](assets/img_6246e5fcca5b.png)

🔺在打开的窗口选择“一键授权到Obsidian”。

![](assets/img_fa0b5a27e6a3.png)

🔺如果不出意外，在Obsidian插件设置这边就会自动显示”导入授权配置“，并开始自动同步。配置信息可以在”远端配置“这里查看，只要显示”服务已连接“就说明是正常的。

PS：如果说局域网服务地址连接正常，反向代理无法连接，很大可能就是我前面提到的，你使用的外网链接不支持Websocket导致的~

![](assets/img_841399bac0d6.png)

🔺配置好服务之后，我们刷新下Fast Note Sync服务端，就很看到已连接的在线客户端，我这里显示的是我本地电脑。

![](assets/img_1e797b43bcbd.png)

🔺然后在它笔记库中可以看到我Obsidian那边的内容已经全部同步过来了，速度极快。

![](assets/img_e4c318d23d7b.png)

🔺在这里也可以随意打开任意一篇内容，不管是文字还是图片，也都能正常显示。

![](assets/img_00987707067f.png)

🔺另外我们还可以在插件设置里开启配置自动同步，我个人没这个需求，所以这里只是为有需要的小伙伴提一嘴。

## Fast Note Sync手机端体验

其实搞定了前面外网同步问题，那后面我们不管是在手机，还是平板上的设置基本就没什么问题了。我这里以安卓手机为例：

![](assets/img_2e876cab9995.png)

🔺比如说我想要将我的知识库同步到手机，我们就直接将这个知识库的整个总文件夹直接上传到手机上。注意哈，这个总文件夹包含Obsidian的本地知识库文件夹，以及一个“.obsidian”的配置文件夹（如果你没看到是你没有开启查看隐藏文件功能），而这个配置文件夹就包含了插件文件。

![](assets/img_ce61e9043b22.png)

🔺和PC端一样，我们先要吧Obsidian设置中的第三方插件“关闭安全模式”。

![](assets/img_bb4f5b58633e.png)

🔺然后在Obsidian仓库中将我们上传到手机的知识库总文件添加进来。

![](assets/img_7cb15f710afb.png)

🔺添加的时候需要允许文件夹访问，然后信任仓库作者并启用插件，之后Fast Note Sync插件就会自动加载进来。我这边出现了一个小问题，它的远端服务令牌没有同步过来，不过我直接手动复制并粘贴过来就正常了。

![](assets/img_0e53b8693f76.png)

🔺实测手机端的展示效果也不错！

![](assets/img_ce349c329e3a.png)

🔺另外在Fast Note Sync Service服务端也能看到接入进来的安卓设备。

## 最后

总的来说，Fast Note Sync算是一个当前非常优秀的Obsidian同步方案了，它不仅能替代付费的官方同步，并且在速度和稳定性上也很有保障，强烈建议各位使用Obsidian的小伙伴体验！

目前极空间的各大NAS产品优惠继续，同时极空间部分产品还可享受白条3期或6期免息政策，180天内出现质量问题只换不修，2年官方质保。喜欢的小伙伴不要犹豫赶快入手吧，早买早享受~

好了，以上就是今天给大家分享的内容，我是爱分享的Stark-C，如果今天的内容对你有帮助请记得收藏，顺便点点关注，咱们下期再见！谢谢大家~
