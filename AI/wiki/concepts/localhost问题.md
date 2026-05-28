---
type: concept
name: localhost问题
created: 2026-05-28
updated: 2026-05-28
tags: [localhost, 本地预览, 上线]
sources: [[别让-AI-写出来的网站死在-localhost给小白的上线指南]]
---

# localhost问题

**类型:** 概念

## 定义

AI 编程工具生成的项目默认在 `localhost:3000` 运行，这个地址只有开发者自己能打开，无法分享给他人。

## 本质

`localhost` = 本机。当把这个地址发给别人时：
- 别人访问的是他自己的电脑
- 他的电脑上没有你的项目
- 所以打不开

## 解决方案

将本地 Demo 变成公网可访问网站：
1. 网站文件放到服务器
2. 项目在服务器上运行
3. 域名解析到服务器 IP
4. 配置反向代理（Nginx）
5. 申请 SSL 证书开启 HTTPS

## 相关文章

- [[别让-AI-写出来的网站死在-localhost给小白的上线指南]]

## 相关概念

- [[网站部署]]
- [[HTTPS配置]]