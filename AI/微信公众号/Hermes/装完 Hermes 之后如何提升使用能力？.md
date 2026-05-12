> 📎 来源: [数智增长局](https://mp.weixin.qq.com/s?__biz=MzU2OTUyNTIzMw==&mid=2247486865&idx=1&sn=55d467f3e07e709856f6377327429225&chksm=fd2b1cebacc0212dcea20ca715356e73e2cdb770a4d34df689e97dc4e539203719ebb81f19d0&mpshare=1&scene=1&srcid=0425ipre1LLOXuSaMcLBWXqt&sharer_shareinfo=bc1a924fdff0ff98ab2af53cd4d2f8e1&sharer_shareinfo_first=bc1a924fdff0ff98ab2af53cd4d2f8e1) | 时间: 2026-04-25 19:41

---

很多人装完 Hermes Agent 后，会有一个共同的问题：
👉 能跑，但不知道怎么“用好”。

其实 Hermes 的强大之处不在于“对话”，而在于 **Agent + Skills + 自动化能力**。
这一篇整理了一套我自己常用的资源网站 + 命令清单，基本覆盖从入门到进阶的整个路径。

---

## 一、Hermes 常用网址工具（建议收藏）

先把工具链准备好，很多问题其实不用问人，自己查更快。

### 1、Hermes 官方文档

http://hermes-agent.nousresearch.com/docs
👉 用途：最权威的使用说明和配置指南

刚上手时一定要过一遍，尤其是：

- 配置文件结构
- 模型接入方式
- 基础命令逻辑

很多“不会用”的问题，其实文档里早就写清楚了。

---

### 2、Github 主仓库

http://github.com/NousResearch/hermes-agent

👉 用途：源码 + 部署教程 + 更新日志

这里重点看两块：

- README（部署步骤）
- Releases（版本更新）

想第一时间知道新功能、Bug 修复，这里是最准的。

---

### 3、中文文档

http://hermes.xaapi.ai

👉 用途：更适合中文用户的使用指南

如果你觉得官方文档偏技术，可以优先看这个版本，理解成本更低。

---

### 4、中文社区 FAQ

https://hermesagent.org.cn/docs/reference/faq

👉 用途：解决“80%常见问题”

比如：

- 为什么模型连不上？
- 为什么技能无法调用？
- 为什么执行报错？

遇到问题先查这里，效率很高。

---

### 5、Discord 社区

http://discord.gg/nousresearch

👉 用途：官方交流 + 实时反馈

适合：

- 提 Bug
- 看别人怎么用
- 获取第一手动态

如果你想“玩深一点”，这个一定要进。

---

### 6、Skills 市场

http://agentskills.io

👉 用途：扩展 Hermes 能力的核心入口

Hermes 的灵魂其实是 Skills。
在这里你可以：

- 找现成插件
- 看别人做了什么自动化
- 直接安装能力模块

一句话总结：
👉 不装 Skills 的 Hermes，只发挥了 30% 能力。

---

### 7、Hermes 橙皮书

https://huasheng.ai/orange-books/hermes-agent/

👉 用途：系统性学习，从入门到进阶

这个更像一本“教材”，适合想系统掌握的人，而不是只会用命令。

---

### 8、Hermes 进阶技巧合集

https://x.com/LufzzLiz/status/2042237123865297267?s=20

👉 用途：实战导向的技巧总结

特别推荐新手做一件事：
👉 按这份清单，把里面的操作都试一遍

你会快速跨过“不会用”的阶段。

---

## 二、Hermes Agent 常用命令（建议熟练掌握）

如果说网址是“资料库”，那命令就是你真正的“操作入口”。

---

### 1、基础交互

开始聊天

```
Hermes
```

继续上次对话

```
Hermes -c
```

单次问答（不进入会话）

```
hermes -q "问题"
```

👉 使用建议：
日常查问题用 `-q`，做连续任务用对话模式。

---

### 2、配置相关

初始化配置向导

```
hermes setup
```

切换模型

```
hermes model
```

查看当前配置

```
hermes config
```

修改配置项

```
hermes config set KEY VAL
```

👉 小技巧：
配置问题是新手最常见坑，多用 `config` + `doctor`。

---

### 3、状态 & 健康检查

健康检查

```
hermes doctor
```

查看运行状态

```
hermes status
```

👉 出问题第一步：先跑 doctor，而不是盲猜。

---

### 4、Skills（能力扩展核心）

搜索技能

```
hermes skills search 关键词
```

安装技能

```
hermes skills install ID
```

查看已安装技能

```
hermes skills list
```

👉 重点理解：
Hermes ≠ ChatGPT
Hermes = ChatGPT + 工具调用 + 自动执行

Skills 就是那个“工具箱”。

---

### 5、网关 / 消息接入

配置消息平台

```
hermes gateway setup
```

启动网关

```
hermes gateway start
```

查看网关状态

```
hermes gateway status
```

👉 用途：
把 Hermes 接入 Telegram / Discord / 其他平台，实现自动化 Bot。

---

### 6、更新与维护

更新到最新版

```
hermes update
```

👉 建议：
不要长期停留旧版本，新功能更新很快。

---

### 7、记忆系统

查看记忆统计

```
hermes memory stats
```

清理记忆

```
hermes memory prune
```

👉 如果你发现：

- 回答越来越慢
- 上下文混乱

可以适当清理记忆。

---

### 8、会话管理

查看历史会话

```
hermes sessions list
```

👉 适合做复盘、找历史记录。

---

### 9、帮助命令

```
hermes --help
```

👉 不确定怎么用的时候，最直接的方法。

---

## 三、最后说点实在的

很多人卡在一个误区：
👉 以为 Hermes 是“聊天工具”

其实更准确的理解是：

> **Hermes 是一个可编排的 AI 执行系统**

你真正应该练的是三件事：

1. 会找工具（Skills）
2. 会配环境（config / model）
3. 会设计任务（而不是只问问题）

当你从“问答”转向“让它帮你做事”，
Hermes 才算真正开始好用。

---

我有“龙虾俱乐部”社群，不收费，扫码进群。

![](assets/img_0c14b5a26b17.png)
