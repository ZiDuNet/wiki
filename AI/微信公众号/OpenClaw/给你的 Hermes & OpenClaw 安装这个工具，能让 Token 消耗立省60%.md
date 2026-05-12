> 📎 来源: [云起泊言](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868887&idx=1&sn=e7186e3b129602043b723a3096674d30&chksm=8630dc17f8aa8261d1e62221932e542dc137de502b57322e0cd389ea9774202093f4c9474cff&mpshare=1&scene=1&srcid=0427hVjbXyUCqHEiisoDozhv&sharer_shareinfo=ce25204eff1846276bebe8b64f493b28&sharer_shareinfo_first=ce25204eff1846276bebe8b64f493b28) | 时间: 2026-04-27 15:58

---

如果你正在使用 **OpenClaw**、**Hermes Agent** 或者 **Claude Code** 等Agent工具，是不是经常在用的很爽的时候，又在一直担心 Token 的消耗？

每次一条命令的输出动不动就几万 Token，你让它查个 `git status` 它能给你唠出一篇小作文。本来上下文窗口就宝贵，这些冗余信息一塞，模型推理能力变差不说，你的 API 费用也跟着蹭蹭往上涨。

> **本文所涉及的工具只对开发测试人员有效，如果你只是用 Hermes、OpenClaw 来对话聊天，那么 0 优势，可以略过了~**

---

今天给大家推荐一款工具——**RTK (Rust Token Killer)**：Rust 开发的一款**零依赖 CLI 代理**，能智能过滤/压缩 `ls`、`git status`、`cargo test` 等终端输出，直接减少 60-90% Token。

**这到底是个啥玩意？**

它可以理解成在 Hermes 和你的命令行之间加了一层 **"过滤器"**——过滤掉注释、空行、重复日志、模板代码这些噪音，只把真正有用的核心信息喂给大模型。

举个例子你就明白了。你让 Hermes 执行 `npm test`，假设跑了 100 个测试只挂了 2 个，原始输出可能有 25000 Token，Hermes 得把全部结果都吞进去。RTK 直接给你过滤成"哪 2 个挂了，挂的原因是什么，其余 98 个全过"，压缩到大概 2500 Token。**省 90%。**

而且 **RTK** 是纯 Rust 写的单一二进制文件，零外部依赖，命令执行的额外开销不到 10 毫秒，你完全感觉不到它的存在。

看一下官方给的一组 30 分钟编程会话的 Token 消耗对比数据，感受一下这省得有多狠：

| 操作 | 使用频次 | 原始 Token | RTK 处理后 | 节省比例 |
| --- | --- | --- | --- | --- |
| `cat` / `read` | 20x | 40,000 | 12,000 | **-70%** |
| `grep` / `rg` | 8x | 16,000 | 3,200 | **-80%** |
| `git diff` | 5x | 10,000 | 2,500 | **-75%** |
| `cargo test` / `npm test` | 5x | 25,000 | 2,500 | **-90%** |
| **总计** | — | **~118,000** | **~23,900** | **-80%** |

对，你没看错，一个 30 分钟会话从将近 12 万 Token 直接砍到不到 2.4 万。

讲了这么多，给大家直接上安装教程吧。

---

### #安装流程

MacOS 推荐使用 HomeBrew 安装：

- 1

```
brew install rtk
```

Linux 使用命令直接安装：

- 1

```
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/refs/heads/master/install.sh | sh
```

Cargo 安装命令：

- 1

```
cargo install --git https://github.com/rtk-ai/rtk
```

**Windows** 系统推荐通过 **WSL** 安装，安装命令与 Linux 命令一致。

除了以上各种终端命令安装放室外，RTK 也贴心的为大家准备了发行包，可以通过以下链接进行下载：

- 1

```
https://github.com/rtk-ai/rtk/releases
```

安装完成后执行命令验证：

- 1
- 2

```
rtk --version   # 显示 版本号
```

集成到 Hermes / OpenClaw /Claude Code等工具中：

- 1

```
rtk init -g       # 安装全局 Hook + RTK.md（推荐）
```

需要注意，rtk 官方目前还不支持 Hermes，所以借助第三方插件实现，执行以下命令：

- 1

```
pip install rtk-hermes
```

然后重启 Hermes 即可，不用再修改任何东西。

**工作原理：**

- 1
- 2
- 3
- 4
- 5
- 6

```
没有rtk：使用 rtk：
```

---

**支持的 AI 工具一览以及安装方式：**

| 工具 | 安装方式 | Method |
| --- | --- | --- |
| **Claude Code** | `rtk init -g` | PreToolUse hook (bash) |
| **GitHub Copilot (VS Code)** | `rtk init -g --copilot` | PreToolUse hook — transparent rewrite |
| **GitHub Copilot CLI** | `rtk init -g --copilot` | PreToolUse deny-with-suggestion (CLI limitation) |
| **Cursor** | `rtk init -g --agent cursor` | preToolUse hook (hooks.json) |
| **Gemini CLI** | `rtk init -g --gemini` | BeforeTool hook |
| **Codex** | `rtk init -g --codex` | AGENTS.md + RTK.md instructions |
| **Windsurf** | `rtk init --agent windsurf` | .windsurfrules (project-scoped) |
| **Cline / Roo Code** | `rtk init --agent cline` | .clinerules (project-scoped) |
| **OpenCode** | `rtk init -g --opencode` | Plugin TS (tool.execute.before) |
| **OpenClaw** | `openclaw plugins install ./openclaw` | Plugin TS (before\_tool\_call) |
| **Kilo Code** | `rtk init --agent kilocode` | .kilocode/rules/rtk-rules.md (project-scoped) |
| **Google Antigravity** | `rtk init --agent antigravity` | .agents/rules/antigravity-rtk-rules.md (project-scoped) |

**常用命令**：

- 1
- 2
- 3
- 4
- 5
- 6

```
rtk ls. # 精简目录树（省 80%）
```

---

### #卸载流程

- 1
- 2
- 3

```
rtk init -g --uninstall
```

- 往期推荐 - 

[你的 Hermes 为什么总是记不住？这篇教你如何给 Hermes 添加长期记忆！](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868882&idx=1&sn=5b5c0d470d31c10deeca597314b77526&scene=21#wechat_redirect)

[网易又一次走在了前面：给你的OpenClaw、Hermes 配一个专属工作邮箱](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868870&idx=1&sn=12e20f9da96bdeb8255de6d711216ad8&scene=21#wechat_redirect)

[DeepSeek V4 终于来了！](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868859&idx=1&sn=d487ce8b8ca8fba8511544ef55e95e8f&scene=21#wechat_redirect)

[Claude Desktop 支持接入第三方 API 了（附详细操作教程）](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868849&idx=1&sn=b8808b3a67ccbac193dc3b074000ff76&scene=21#wechat_redirect)

[GPT-5.5 正式发布，冲冲冲！](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868823&idx=1&sn=527a188d96337ca025754b446a5b7fa5&scene=21#wechat_redirect)

[CliProxyAPI (CPA) 更新，支持GPT Image 2模型，Hermes 跟小龙虾可以直接生图](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868815&idx=1&sn=2463e7d3a72402e75756f1ed58cfb23b&scene=21#wechat_redirect)

[为你的 Hermes 定义人格和角色](https://mp.weixin.qq.com/s?__biz=MzA5NjAxMTY1OA==&mid=2461868805&idx=1&sn=011f931ba9a855bb106b5803fbc1a128&scene=21#wechat_redirect)
