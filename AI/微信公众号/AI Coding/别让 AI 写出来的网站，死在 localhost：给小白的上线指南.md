> 📎 来源: [宝塔面板](https://mp.weixin.qq.com/s?__biz=MzU2MjA3MDg5Mw==&mid=2247491484&idx=1&sn=a1711a35735a142308795bf78b5d8a8b&chksm=fd7b82f43d20dff0ab602783165e369d31d6997158cf5185dc090f07fda674fa81fac23c5531&mpshare=1&scene=1&srcid=0528zvcNqpqdafHFeJlqbZkO&sharer_shareinfo=46f062f9c04fe54c3eb953bfe4565271&sharer_shareinfo_first=46f062f9c04fe54c3eb953bfe4565271&hit_product=1) | 时间: 2026-05-28 15:04

---

前段时间看到一个很典的笑话：

“我用 AI 搭好了一个网站，你打开看看，地址是 `localhost:3000`。”

朋友沉默了几秒：

“哥，这个地址只有你自己能打开。”

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKQPQx9TxV3CdniaHWyIpQb9wfzWI5BoFIvCmR5iaxWUXylCP0U5R9dtI8764NcicEhZYeTZYYZpiaMDBkRibWJqzYsb3WdFSSZ1E9sg/640?wx_fmt=png&from=appmsg}}

这句话虽然是段子，但很多刚开始用 AI 写网站的人，可能真的遇到过类似情况。现在用 Trae、CodeBuddy、Qoder 这类 AI 编程工具，写一个网页项目已经不难。你只要告诉 AI 想做什么，它很快就能生成代码，并提示你运行：

```
npm installnpm run dev
```

然后访问：

```
http://localhost:3000
```

页面确实出来了。

但问题是，`localhost` 只代表你自己的电脑。你能打开，不代表别人也能打开。

如果想让朋友、客户、用户都能访问，就需要把这个网站部署到服务器上，绑定域名，配置 HTTPS，让它从一个本地 Demo，变成真正可以公网访问的网站。

这篇文章就用一个 AI 生成的网站项目做例子，看看如何通过宝塔面板，把它从：

```
http://localhost:3000
```

变成：

```
https://你的域名.com
```

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKQ8CCLukQDDCuMU4KeD9Ccq55icsUbFkibPsiaxUN1HU9F2dicHXcEicFTniaWw0CUKHzFwDjxdLKicKCoRMLj6FcSFPTYf6IQicBJXHjQ/640?wx_fmt=png&from=appmsg}}

**AI 写出网站，为什么别人打不开？**

很多 AI 编程工具在生成项目后，都会告诉你访问 `localhost:3000` 查看效果。这个3000可能是任意的端口。

这里的 `localhost`，可以简单理解成“本机”。也就是说，你访问的是自己电脑上正在运行的项目。当你把这个地址发给别人时，别人打开的也是他自己的电脑。可他的电脑上并没有你的项目，所以自然打不开。

所以，`localhost` 只是本地预览，不是网站上线。真正上线，需要满足几个条件：

- 网站文件要放到服务器上
- 项目要能在服务器上运行
- 域名要解析到服务器
- 用户访问域名时，要能找到你的项目
- 最好还要开启 HTTPS，避免浏览器提示不安全

这些事情，如果都用命令行处理，对小白来说会比较绕。

宝塔面板的价值，就是把服务器、网站、环境、域名、SSL、日志这些操作集中到一个可视化面板里，让上线过程更容易理解和操作。

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKTtkrMuxhJhfufpXfoicaTd4vib5eXKM6OPMBe8rjh9apzCsoNYrNGCEwovgjp5a0aiaorvicCQeVVpJHhHIEsHXog74EHIRtLeYia0/640?wx_fmt=png&from=appmsg}}

**这次我们要完成什么？**

这次的目标很简单：用 CodeBuddy 生成一个网页项目，然后通过宝塔面板把它部署到服务器上。最终效果是：本地访问：http://localhost:3000变成公网访问：https://你的域名.com

整个过程大致分为几步：

1. 用 AI 编程工具生成网站项目
2. 准备服务器并安装宝塔面板
3. 上传项目到服务器
4. 安装运行环境并启动项目
5. 通过宝塔配置网站入口
6. 绑定域名并开启 HTTPS
7. 检查访问效果和常见问题

下面开始实战。

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKTMcKhdZfZxJ7H3tyoOJOWceDSiatfABlJ1dh4IEdaORhgcfwMtb3LticY8dfUovJ4kt1wvquEaahTRwrjnAQTryDY5owj2BmAag/640?wx_fmt=png&from=appmsg}}

**实战：用宝塔把 AI 写出来的网站部署上线**

Step1：用 Trae / CodeBuddy 生成网站项目

首先我们打开AI编辑器，在编辑器中，可以给 AI 一个简单需求，例如：

```
帮我用 vue 生成一个简单的个人作品集页面，动效，互动效果
```

生成后，先在本地运行测试。

确认浏览器可以通过 `localhost` 正常打开。

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKRv9ySmLcEU7PL5icd2RFRAnicjtBzeBU5xsxX5maJTxklbH5ojhUMSS2JIO29bUDYgmo4qEStLYVzia3MSVnAuKcoWTJQc6Lcubs/640?wx_fmt=png&from=appmsg}}

Step2：准备服务器和宝塔面板

服务器各大云厂商都有便宜的服务器，至于宝塔面板，你甚至可以在购买的时候直接选择宝塔面板的镜像，比如腾讯，阿里（不要看我页面的价格，我是老用户了，新用户应该只需要几十块钱一年）

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKRVowdPd9XGeUibQBZ3aewvQnUsayUmZYQwAViafDIBdW51LlvuyBldnmIABYIZlqrRGTHWzicKQm6hGqqIOZgvbMAZwqT0P40Eyc/640?wx_fmt=png&from=appmsg}}

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKTBFNrr3q8W6XtT6gZdL5BDMkSNBAuic9ZMvN7CtTpJNfHVX8zrlPznez2B97ibHVv3hA4AaAJJGyUXJVNXcBP4hRskplwjM5Rps/640?wx_fmt=png&from=appmsg}}

你应该能在购买服务器的页面看到宝塔面板的镜像，购买后在服务器详情页面找到宝塔面板的登录信息登录即可，不同厂商的界面可能不一样，请以实际为准

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKR1W7pmgDXCGp1WsuMXr1FUhGxrYMsvmialS5RicgB0LicW1Gp0PeRTzD46ia8TpAcdmo94mS7xJ1yfzgtTprojxOjIKic258lblnjA/640?wx_fmt=png&from=appmsg}}

登录宝塔面板后按界面提示安装Nginx（因为AI写的都是Node或者纯HTML页面，所以不需要那么多）

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKRy2cf8icfkEULI2RIdpKibFKT1icuMx48jtA2QZJ4ezcYoiaOOaBxLerg8PqicicpZUgO4gUaCufZfDWILvnEwicCibB5OOjj43pAjXEk/640?wx_fmt=png&from=appmsg}}

安装成功后，点击侧边栏的网站-Node项目-安装Node项目管理器

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKSlxSjpMZORHMmyfzOGicHtsXgwZs73UlWJ3KFldic85nuOUzVlibs6nCCp0dxzuck2DHicU0YEoiagrpr7lKbp4lgwia4bIibwJWRKXM/640?wx_fmt=png&from=appmsg}}

安装完成之后，点击Node版本管理器-更新版本列表

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKQjCQgKnVwff62dmJwAky5cS0II2EOwjRdntQbnHCuLoSJjTc4YY0louVeZxWajU3Uf3yTodDFgCRGKnFpQp8wJzodB5p5alVk/640?wx_fmt=png&from=appmsg}}

更新后找到最新的稳定版安装

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKS7xzAXkwH9r4uNZDf0DdeLGXuQsTd1L3uVOWEOKOzySnhiaTyLQgiby5qhEibjJTdgObLHsNlOoQBqbqaxQFKXu9nqP0bTzNMrWg/640?wx_fmt=png&from=appmsg}}

安装成功之后我们需要把代码上传到服务器，如果你找不到代码在哪可以跟agent说：把当前项目代码打成压缩包放到桌面

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKT8xj9KcKyoPAPLOEPKm1wYEKtibdvVCZbnrsLzh626JjSwWPdyXTwVLsCic6tyib50FN1a6Wh8Cnpnmm6UOX5d1793yZHRRdNeT8/640?wx_fmt=png&from=appmsg}}

然后我们回到面板-点击文件，在默认的wwwroot下面点击上传

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKRaicDKOpCsXQWlPcCVWoEOxgaCSpDSa7ALGval1hUeqmaAK7Xic4cGOjNKhWO9Ib9ibNMePRA8qTbmry6yIKWNqNOibCT2GsDE7Jo/640?wx_fmt=png&from=appmsg}}

选择刚刚打包的文件，上传

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKQu0SfNS9SQTZugWWQ4DSOSYj3GA28moWNg2GUQtZhuMiaq6RI56psmVB2E0vnFef9WjxKAYB7Libh8H5I3BM5RwdpMaIEHeA0Ig/640?wx_fmt=png&from=appmsg}}

上传完之后解压

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKRSuSTTZH98jEQBg9ndR3Vx6WriaOF5YBnlBDhsT8LMj1qFib0n7B2wiauhL8sSoRfJahqpafX8Wp9qicrnLCnORcsjIAtzNhB41e8/640?wx_fmt=png&from=appmsg}}

路径这里记得填一下项目文件夹名称，或者你新建一个文件夹，要不然可能会把项目文件，解压到当前目录了（有的agent压缩的不是文件夹，而是项目里的具体文件，所以要创建个文件夹，不然解压出来乱掉了）

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKTLibMaFkJI88qACnBbYt7N6yHpCzAmxx4y8pm5nQItOP5XaC7uUEI2wicBfAYl3HD7xSCIiaRWyKNZjHxa2A20891nT3FiaF2AlNc/640?wx_fmt=png&from=appmsg}}

解压完成后回到网站-Node项目-添加项目，选择项目目录

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKStFcgcuWa4UiaSuXYL60sqpy7qYvbodXiao9NJ5yfmicya30wcMPCd1y8t9gCevY8jc9uMG6QEBibtcccLjS328VrI5ibia3oxcdibMI/640?wx_fmt=png&from=appmsg}}

启动选项会自动识别，选择版本，并选择包管理器为npm，点击确定

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKTdNczQKVqGZwWdCvKm0iakQ8MJMMic6tX6ia06Yp7m35MDibDXlY9Turvduqaia5bVl52zicQsFicfNTvl4xo2gFPicAVswnOoqUNcbhM/640?wx_fmt=png&from=appmsg}}

点击确定后，面板会自动安装项目依赖，耐心等待

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKQGj4iaiahL5QBGLqiczUD1dzf0wrDdaU4ic2bdcqABCibHvcsFpr1u4hCyr1gUhtoyKhiawUVRtCkRoeiaECjw78vic5LnUsqlZxm8B68/640?wx_fmt=png&from=appmsg}}

安装完成即可看到正在运行的项目

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKSECT4ptE4YNicGszeP3Rg1b4mWKAo8XB9kf3nG7rRm2an5Bkp5CazZJOkKXKNecHfI2Ntiaoh1ofB2JV7icT69weTh0rpyojiazQ0/640?wx_fmt=png&from=appmsg}}

点击项目名称进入项目管理页面，再点击域名管理

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKS5xShD1ZL09gv0ZDa7Eyun8PdnrPfU8tE5GWic7Je4YRBdXsWo4zHLnp4OghbIVW1UcZI0AaQdXtHr5kvfeo03TUs1xc916Iib8/640?wx_fmt=png&from=appmsg}}

如果你只是发给朋友临时看一下，域名这里你可以直接填写服务器的IP，也就是云厂商页面和面板页面上吗的地址栏，格式为xx.xxx.xxx.xxx这种，这个就是服务器IP

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKRKlAOePHVBU1qXyjm4g6o7yxSkgsbMvbGxHVIFLm2aJ56dHSXT2ibNNNOLG8Obgsyia6jVJScotSg6UTuWsSM6KYiab6GpicdcDKg/640?wx_fmt=png&from=appmsg}}

然后点击添加

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKRApofPVVdhEKwClEYSKmSROPbNQGErdCuIup6u7xpzkHGQ1nzmQkia4LsTwECf7wArWfwTIxqtuobUwfvdSYHWtPq3OVf19Y0o/640?wx_fmt=png&from=appmsg}}

PS：如果你是正式业务，建议绑定域名，你只需要将域名在域名解析商解析到你的服务器，在此处填写域名即可（注意：境内服务器可能需要完成ICP备案）

然后再点击外网映射，打开这个开关

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKT2NjibQVZ4KTjotZiaD8YQoMLCatCl4a3Mic6H9qEDLVM8whOHIZBm2DvwVY4dqG3sb1tgUe1zXQsb4Xic0esRupbjCicOLH49lOkw/640?wx_fmt=png&from=appmsg}}

打开之后，你可以在浏览器地址栏输入你刚刚填写的域名或者IP，访问你的项目

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKSko89g7dJUbnh8lBbqib8AByQyWOugwNFLDjJicZb2ex5EjvnibbOdmhndlbbEFs6dEgkI6ucPz2so5Pl1InTRM7pY5KXh82fCic0/640?wx_fmt=png&from=appmsg}}

你也可以把这个地址发给你的朋友访问，到此，一个完整的部署流程就结束了，后续你只需要更新代码，然后重启一下项目就好了

当然细心的小伙伴可能会发现，浏览器中显示着不安全这几个字，如何让他变得安全呢，这就需要SSL证书了，我们回到项目管理页面，点击SSL，选择图片这个，申请免费证书

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKTiaezoiaxfARHS0FRtz4aE2bWRobAXLjD9ybGEYNe9hMZYKMpp1hvibLgLtGXbcfvOBfAjAbh4C7S5yicC2ribPcCkwyd2fbsujXPU/640?wx_fmt=png&from=appmsg}}

选择刚刚绑定的域名，这里目前还不支持给IP申请免费的SSL证书

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKRicms9tTlxnRCupKNtSFzIoy9wp3XLBDB7MIG0tRbQq6FA8QWubgddaQ1iaY5oeJNiacZmbN30y1P4AcndXPywBmjGDu5UG8QwhM/640?wx_fmt=png&from=appmsg}}

点击申请证书等待程序自动执行

{{IMG:https://mmecoa.qpic.cn/mmecoa_png/gf6D0zv7SKR0sIh83MQA1iatqoW9sbwSeb7lnoM2UtjaUuKORK0lmSmUlWJmzgptmKxecraltwAxm971ISbKnS9ub565QQppsrYFkgKFEETU/640?wx_fmt=png&from=appmsg}}

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKQxNJicsoBCfrGaFyUHDWGHgCicoq8HteMCBCT9WSIN3jH5Tvxk3QgnIDlCCT3hodSicV7Rvwqx5eQicDXVEXHnahCGDbnTYt4QssU/640?wx_fmt=png&from=appmsg}}

完成后我们访问HTTPS://域名即可看到看到带锁的效果

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKQYp3eZvFTERBYt6ibcJkoiaqVHE1XdmTWwrYGnW874LLCjKibpTmdF8JZPZFpGqqYibG2lUYAo3WmCMykXibxYY5xMB3REibDophWf8/640?wx_fmt=png&from=appmsg}}

到这里，一个由 AI 写出来的网站，就完成了从本地到公网的上线过程。

一开始，它只是你电脑里的一个 `localhost:3000`，只有你自己能打开；现在，它已经可以通过域名访问，也可以开启 HTTPS，发给朋友、客户或者用户查看。

这其实也是很多 AI 编程新手最容易忽略的一步：
AI 能帮你把网站写出来，但网站真正有价值，不只是能在自己电脑上运行，而是能被别人访问、能稳定打开、能持续维护。

以后你再用 CodeBuddy、Trae、Qoder 这类工具写出一个网页项目时，不妨记住这个流程：

先让 AI 把项目写出来；
再用宝塔把项目部署到服务器；
最后绑定域名、开启 HTTPS，让它真正上线。

从 `localhost:3000` 到 `https://你的域名.com`，中间差的就是上线这一步。

AI 负责写网站，宝塔负责上线。
别让 AI 写出来的网站，死在 localhost。

{{IMG:https://mmecoa.qpic.cn/sz_mmecoa_png/gf6D0zv7SKTN9JxVKSN4nyHicvtvEYqrATz7U7KbDPR9F0CS2mN3WlUnffNG85WoibnFiazHiaTMicZJurjUPSSUTJQthmfdAROl3eNXKN7NqqTQ/640?wx_fmt=png&from=appmsg}}

**END**

如果你也刚好用 AI 写出了一个网页项目，不知道下一步怎么部署，可以试试用宝塔面板完成上线流程。服务器环境、项目运行、域名绑定、SSL 证书、日志查看，都可以在面板里集中管理，对第一次部署网站的小白会更友好一些。

当然，这里也悄悄的预告一下，后面你可以只用宝塔面板，加上你的域名和服务器，就能完成这些事情了，宝塔AI建站、宝塔......即将上线，敬请期待，后续我们也将结合AI将更多、更好用的运维和开发能力带给大家。

哦对了，好像好久都没抽过奖了，那么今天，我们⬇️⬇️⬇️
