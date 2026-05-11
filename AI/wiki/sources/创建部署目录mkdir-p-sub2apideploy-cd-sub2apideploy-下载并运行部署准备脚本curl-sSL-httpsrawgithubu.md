---
tags: [API中转, Agent, GitHub, Dify, API, OpenAI]
source: "牛study"
created: 2026-05-01
updated: 2026-05-10
category: API中转
---

# 创建部署目录mkdir -p sub2api-deploy && cd sub2api-deploy# 下载并运行部署准备脚本curl -sSL https://raw.githubusercontent.com/Wei-Shaw/sub2api/main/deploy/docker-deploy.sh | bash

> 来源: [牛study](https://mp.weixin.qq.com/s?__biz=MzkzMDI3NDUyNQ==&mid=2247484367&idx=1&sn=942b858c9f8c60296e4e01ade3e2d405&chksm=c3c2d65733a9d25a6154a9a860b107a61562d9007be8c5db2c3e38e4e844f6f6965b9ea1b718&mpshare=1&scene=1&srcid=05014DgJgRFL4Mq8XxGg9kOx&sharer_shareinfo=d41d0325735ab690a3a8fba7b0d30b4f&sharer_shareinfo_first=d41d0325735ab690a3a8fba7b0d30b4f) | 2026-05-01

## 摘要

服务器的选择有很多，腾讯云，阿里云，华为云，京东云等，各家的服务器对新人都有优惠，阿里云的新人优惠的话，2核2G好像是**68一年**，但是对老用户的话，阿里云不清楚，腾讯云是**99一年**，当然了这里的服务器节点，不能选大陆服务器和香港服务器的，必须选国外节点，比如新加坡，首尔之类的吗，不然国外ai使用上受限很多。
阿里云服务器截图
腾讯云服务器截图
购买了服务器后，就可以进行第二步了
使用mkdir新建一个目录,使用cd命令进入目录
之后直接使用官方的安装脚本进行安装，再次之前的先安装
安装完成后，就直接使用官方的sub2api脚本进行安装
到这一步先别等一等，修改一下配置文件，比如开放的端口号和默认管理员账号和密码
里面的模板大概是这样的
这里我修改了一下默认端口号和管理员账号和密码
端口号我改成了6780
管理员账号和密码根据自己常用的账号和密码，不用系统自带的，设置完成后启动
查看一下日志，没有什么问题，就可以进行访问了
如果没有购买域名，就是公网ip:6780，如果购买了域名，公网链接就替换成域名
登录界面
输入开始设置的账号和密码，进入界面
主界面
到这里sub2api...

## 相关实体

[[Dify]], [[Docker]], [[Gemini]], [[GitHub]], [[OpenAI]], [[VS-Code]]

## 相关概念


