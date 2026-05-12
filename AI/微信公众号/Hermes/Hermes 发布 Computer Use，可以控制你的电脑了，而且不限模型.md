> 📎 来源: [云起泊言](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868976&idx=1&sn=18668eb52d3922da51367475a0b55c09&chksm=86d3d60d731db963859bac2c288b2a6945bb4c20a40d0812569d5cdb02d41ac42aa900ed55ec&mpshare=1&scene=1&srcid=0512kOgkdSnyLKUpGKzW1N15&sharer_shareinfo=4ead91104afb97cc43eddadc379cd456&sharer_shareinfo_first=4ead91104afb97cc43eddadc379cd456) | 时间: 2026-05-12 12:11

---

说到 Computer Use，大多数人第一反应是之前 Codex 发布的 Computer Use —— Codex 可以直接看着你的屏幕，帮你点、帮你打字。用过的人应该都知道，好用是好用，但是只能 Codex 使用；

Hermes 刚更新的这个 Computer Use 功能，把这一痛点解决，而且**不限模型**。

> 注意⚠️：由于 Computer Use 依赖 **cua driver**，且该驱动只支持 **Apple 芯片**苹果电脑，所以其他设备不用尝试了

### #不限模型，这是最关键的一点

Hermes 的 Computer Use 走的是 MCP 协议，底层驱动叫 cua-driver。它不绑定任何一家模型厂商，只要你的模型支持 vision（能看截图），就能拿来驱动桌面。

Claude、GPT-4/5、Gemini、OpenRouter 上的任意 vision 模型，甚至本地跑的 vLLM——全部能用。没有 Anthropic-native schema 的限制，也没有"必须用某个特定模型"的门槛。

这意味着什么？你可以用最便宜的 vision 模型干杂活，用最强的模型干精细活，自由搭配。而不是被锁在一个 provider 上。

### #后台运行，不抢你的电脑

大多数 Computer Use 实现，操作的时候你的鼠标会自己动、窗口会跳到前台、macOS 会切 Space。你本来在写文档，它突然把 Mail 切到最前面去搜邮件，体验很割裂。

Hermes 这个不一样。它用的是 macOS 的 SkyLight 私有 SPI，事件直接发给目标进程，不走 HID 事件注入，不移动光标，不切换 Space，不抢焦点。你和 agent 各干各的，互不干扰。

官方文档里举了个例子：让 agent 去 Mail 里搜 Stripe 的最新邮件并总结。整个过程你的鼠标纹丝不动，Mail 窗口也不会弹到前台。agent 在后台截图、点击搜索框、输入关键词、读取结果，一气呵成。

这其实就是 OpenAI Codex 那个"background computer-use"的开源版本。技术路线一样，只是 Hermes 把它做成了通用能力。

### #安全防护，不是裸奔

后台操控桌面听起来有点吓人——万一它乱点呢？

Hermes 做了几层防护：

- 点击、输入、拖拽这些破坏性操作默认需要审批，CLI 里会弹确认框，消息平台里有审批按钮
- 硬编码屏蔽了一批危险操作：清空废纸篓、强制删除、锁屏、登出
- 输入内容有黑名单：`curl | bash`、`sudo rm -rf /`、fork bomb 这些会被直接拦截
- 系统 prompt 明确告诉 agent：不点权限弹窗、不输密码、不执行截图里嵌入的指令

如果你想要更严格，可以在配置文件里设 `approvals.mode: manual`，每一步操作都要你确认才执行。

### #Token 效率，官方做了四层优化

截图很烧 token，这个是 Computer Use 的通病。Hermes 做了四层优化：

1. **截图淘汰**：上下文里只保留最近 3 张截图，更早的自动替换成占位符
2. **客户端压缩**：上下文压缩器会识别多模态工具结果，自动剥离旧截图的图片部分
3. **图片 token 估算**：每张图按 ~1500 token 估算（Anthropic 的统一费率），而不是按 base64 长度算
4. **服务端上下文编辑**（仅 Anthropic）：启用 Anthropic API 的服务端旧工具结果清理

实际效果：一个 1568×900 分辨率下 20 步操作的会话，截图上下文大约消耗 3 万 token，而不是 60 万。

这个差距很大。意味着你可以跑更长的任务而不用担心上下文爆掉。

### #安装和使用

首先执行命令更新 Hermes：

- 1

```
hermes update
```

**方式一：直接命令安装（推荐）**

- 1

```
hermes computer-use install
```

一行搞定。它会自动拉取 cua-driver 的安装脚本并执行。装完用 `hermes computer-use status` 验证。

**方式二：交互式启用**

- 1

```
hermes tools
```

在工具列表里选 🖱️ Computer Use (macOS) → cua-driver (background)，跟着提示走就行。

装完之后需要授权两个 macOS 权限：

- **系统设置 → 隐私与安全性 → 辅助功能**：允许终端（或 Hermes 应用）
- **系统设置 → 隐私与安全性 → 屏幕录制**：允许同样的应用

然后启动会话：

- 1

```
hermes -t computer_use chat
```

或者把 `computer_use` 加到 `~/.hermes/config.yaml` 的 enabled toolsets 里，以后默认就带上了。

### # 限制条件

**macOS only。** cua-driver 依赖 Apple 的私有 SPI，Linux 和 Windows 上跑不了。跨平台的 GUI 自动化还是得用 Hermes 的 browser 工具集。

**私有 SPI 风险。** Apple 随时可能在系统更新里改 SkyLight 的符号表。如果你想在 macOS 升级后保持稳定，可以用环境变量 `HERMES_CUA_DRIVER_VERSION` 锁定驱动版本。

**后台模式比前台慢。** SkyLight 路由的事件延迟在 5-20ms，比直接 HID 注入慢。对 agent 速度的点击操作来说感知不明显，但别指望拿它跑速度测试。

**不支持键盘输入密码。**`type` 命令对 shell 危险模式有硬拦截，密码类输入请用系统自带的自动填充。

### #兼容性一览

| Provider | 视觉支持 | 可用 | 备注 |
| --- | --- | --- | --- |
| Anthropic (Claude Sonnet/Opus 3+) | ✅ | ✅ | 最佳体验，支持 SOM + 原始坐标 |
| OpenRouter (任意 vision 模型) | ✅ | ✅ | 支持多部分 tool message |
| OpenAI (GPT-4+, GPT-5) | ✅ | ✅ | 同上 |
| 本地 vLLM / LM Studio | ✅ | ✅ | 模型需支持多部分 tool content |
| 纯文本模型 | ❌ | ⚠️ 降级 | 可用 mode="ax" 纯无障碍树模式 |

###

---

### Computer Use 这个能力，从 Anthropic 第一次演示到现在，一直是"看起来很酷但用起来有门槛"的状态。门槛不只是技术上的，还有使用成本上的——被锁在一个模型、一个平台，token 消耗高，操作时抢焦点。

Hermes 这次做的这几个点，刚好打在这些痛点上：模型解绑、后台运行、token 优化、安全兜底。

尤其是模型解绑这一点。Computer Use 本质上是一个"眼睛+手"的组合，"眼睛"是截图和理解，"手"是点击和输入。"手"的部分是固定的，"眼睛"的部分应该允许你选最合适的模型。Hermes 把这个选择权交给了用户。

如果你已经在用 Hermes，而且是 macOS 用户，这个功能值得试一下。安装成本很低，一条命令的事，但打开的可能性不小——尤其是那些需要 agent 操作桌面应用但又不想被抢走电脑控制权的场景。

但是遗憾的是 Windows 用户暂时还无法体验，希望在未来的某一天，可以对 Windows 系统进行兼容吧～

---

> 文档来源：https://hermes-agent.nousresearch.com/docs/user-guide/features/computer-use

- 往期推荐 -

[快领！Kiro Pro 免费一个月，可以使用 Opus 4.7（国内信用卡亲测可用）](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868971&idx=1&sn=651d9641322162173ba26e423fe55b64&scene=21#wechat_redirect)

[Codex 发布 Chrome 插件，用过之后我直呼牛逼！（附详细配置教程）](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868957&idx=1&sn=fd00db8c89f52dcd414e8b29599d8f92&scene=21#wechat_redirect)

[Hermes 终于支持原生 Windows 了！](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868940&idx=1&sn=c10ecb117f07790648beca2d263f9c64&scene=21#wechat_redirect)

[Codex 新出的宠物功能，让我越玩越上头了](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868935&idx=1&sn=4e2889408b7014d7a0cd1963bf413b7f&scene=21#wechat_redirect)

[装了 Hermes 却只当聊天框用？这 15 个功能你大概率没碰过](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868914&idx=1&sn=f716475e83811c3d7b35a191c7587d6d&scene=21#wechat_redirect)

[感谢小米送的 2 亿 Credits，治好了我的 Token 焦虑（还没申请的快冲！）](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868906&idx=1&sn=24f4c42a47bb1d3eb84f6319eaa58ed8&scene=21#wechat_redirect)

[给你的 Hermes & OpenClaw 安装这个工具，能让 Token 消耗立省60%](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868887&idx=1&sn=e7186e3b129602043b723a3096674d30&scene=21#wechat_redirect)
