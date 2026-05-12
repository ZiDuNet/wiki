> 📎 来源: [强哥AI智能体](https://mp.weixin.qq.com/s?__biz=MzA3MzAzMjQwMw==&mid=2447506393&idx=1&sn=4fb833c3a41fbab5330d995f33935f8c&chksm=8ae27511fdb948a835343515222cbb811f996aa8caeed89afc9c7c781f25a159245967a2f2b3&mpshare=1&scene=1&srcid=0410DZXeN7beRgNBV3eUHuSr&sharer_shareinfo=6f9c2bd4e96fca19c4c83cb4e866e521&sharer_shareinfo_first=6f9c2bd4e96fca19c4c83cb4e866e521) | 时间: 2026-04-13 16:15

---

用过 OpenClaw 做浏览器自动化的朋友应该都遇到过一个问题：它打开的是一个全新的、干净的浏览器，什么网站都没登录。你让它帮你操作后台，它先卡在登录页；你让它帮你填个表单，它连页面都进不去。

最新版解决了这个问题。

OpenClaw 现在支持直接连接你正在使用的 Chrome 浏览器——带着你所有的登录状态、Cookie、已打开的标签页。你在 Chrome 里登录了什么，AI 就能操作什么。

这篇文章讲清楚三件事：怎么配、能干嘛、要注意什么。

## 配置流程

一共三步，两分钟搞定。

### 第一步：在 Chrome 里开启远程调试

地址栏输入：

chrome://inspect/#remote-debugging

你会看到一个开关，拨成开启就行。这个设置重启 Chrome 后依然有效，不需要每次重新开。

注意：这个功能需要 Chrome 144 或更高版本。目前 144 还在 Beta 渠道，如果你的 Chrome 版本不够，需要先升级到 Beta 版。

### 第二步：修改 OpenClaw 配置文件

编辑 

```
~/.openclaw/openclaw.json
```

，加入以下内容：

{

  "browser": {

    "defaultProfile": "user",

    "profiles": {

      "user": {

        "driver": "existing-session",

        "attachOnly": true,

        "color": "#00AA00"

      }

    }

  }

}

两个参数解释一下：

●

```
driver: "existing-session"
```

：用 Chrome DevTools MCP 方式连接，这是新版才有的连接方式

●

```
attachOnly: true
```

：只连接已经打开的 Chrome，不会自己偷偷启动新的

### 第三步：启动并验证

# 启动连接

openclaw browser --browser-profile user start

 

# 查看连接状态

openclaw browser --browser-profile user status

 

# 列出你 Chrome 里的标签页

openclaw browser --browser-profile user tabs

如果 

```
status
```

 显示 

```
running: true
```

，

```
tabs
```

 列出了你正在打开的标签页，说明连接成功了。

首次连接时 Chrome 会弹一个授权对话框，点允许就行。连接建立后 Chrome 顶部会有一行提示横幅，告诉你当前有外部程序在控制浏览器。

## 它能做什么

连接成功之后，AI 可以像真人一样操作你的浏览器。这里列几个实际能用的场景。

### 批量操作后台系统

你有一个管理后台，需要批量修改几十条数据。以前要么手动一条条改，要么写脚本调 API（前提是有 API）。现在让 AI 直接在网页上操作，点进去、改内容、保存、下一条，跟你自己干一样，只是快很多。

这对那些**没有 API 只有网页界面**的系统特别有用。很多内部工具、老系统，根本没有开放接口，只能通过页面操作。

### 自动化填表和提交

需要在某个平台重复填写表单？比如批量上传商品信息、批量提交申请、定期填报数据。AI 可以直接在你已登录的页面上完成这些操作，不需要你研究 API 文档、不需要你写爬虫。

### 网页内容抓取和整理

打开目标网页，读取页面内容，截图，整理成你需要的格式。因为用的是你的真实浏览器，那些需要登录才能看到的内容也能抓到。

### 辅助调试

你在 DevTools 里看到一个报错，直接让 AI 分析。它能读取 Network 面板的请求详情、Console 里的错误日志，帮你定位问题。

### 日常操作代劳

整理 Notion 笔记、更新项目管理工具里的任务状态、在协作平台上批量处理消息……这类重复性的登录态操作，现在都可以交给 AI。

## 三种浏览器模式怎么选

OpenClaw 现在有三种浏览器控制模式，适合不同场景：

| 模式 | 原理 | 优点 | 缺点 | 适合场景 |
| --- | --- | --- | --- | --- |
| ``` openclaw ``` | 启动独立隔离浏览器 | 最安全，与你的 Chrome 完全隔离 | 没有登录状态 | 抓取公开网页、自动化测试 |
| ``` user ``` | 连接你的真实 Chrome | 能力最强，带登录状态 | 风险最高，AI 能访问所有标签页 | 需要登录的后台操作 |
| ``` chrome-relay ``` | 通过扩展控制指定标签页 | 只控制你选定的页面 | 需要安装扩展，手动选择标签页 | 只想让 AI 操作某一个页面 |

**我的建议：** 大部分场景用 

```
openclaw
```

 隔离模式就够了，只有确实需要登录状态的任务才切到 

```
user
```

 模式。

## 安全注意事项

```
user
```

 模式功能强大，但风险也不小。开启之后，AI 能访问你整个 Chrome 会话——所有标签页的 Cookie 和登录状态。如果你某个标签页还登着银行、另一个开着公司内网，AI 理论上都能碰到。

几个建议：

**1. 用专门的 Chrome 配置文件**

不要在你日常浏览的那个 Profile 里开。新建一个 Chrome Profile，只登录需要 AI 操作的网站。

**2. 关掉内网访问**

在配置文件里加上：

{

  "browser": {

    "ssrfPolicy": {

      "dangerouslyAllowPrivateNetwork": false

    }

  }

}

这个默认是开启的，意味着 AI 可以访问你的内网地址。建议关掉。

**3. 用完关掉远程调试**

任务做完后，回到 

```
chrome://inspect/#remote-debugging
```

 把开关关掉。不要让它一直开着。

**4. 敏感操作用隔离模式**

涉及资金、账号安全的操作，切回 

```
openclaw
```

 隔离模式。

## 常见问题

**Q：Chrome 版本不够怎么办？**

user 模式需要 Chrome 144+，目前在 Beta 渠道。可以安装 Chrome Beta 版本，或者等正式版推送。在此之前可以用 

```
chrome-relay
```

 扩展模式作为替代。

**Q：连接不上怎么排查？**

# 查看详细状态

openclaw browser --browser-profile user status

检查 

```
status
```

 输出里 

```
driver
```

 是不是 

```
existing-session
```

，

```
running
```

 是不是 

```
true
```

。常见问题是 Chrome 没有开启远程调试，或者 Chrome 版本不满足要求。

**Q：AI 操作的时候我能同时用 Chrome 吗？**

可以。AI 操作和你手动操作不冲突，但建议不要同时操作同一个标签页，避免冲突。

**Q：关掉 OpenClaw 之后 Chrome 会受影响吗？**

不会。断开连接后 Chrome 恢复正常状态，不影响任何功能。

这个功能对需要做浏览器自动化的人来说确实很实用，尤其是那些只有网页界面没有 API 的系统。配置简单，上手快，但一定要注意安全，用完记得关。
