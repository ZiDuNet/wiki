> 📎 来源: [虾哥AI](https://mp.weixin.qq.com/s?__biz=MzkwMTU5OTEwNQ==&mid=2247487054&idx=1&sn=fc4197147995fc4d64f85af7aea3f272&chksm=c1a0a90bb3151b40a7c07202e7676c646ddbaa5dd250416cf3d0ca435c67027cd090a57dc60b&mpshare=1&scene=1&srcid=042493czmPEztXgnwnNQQurJ&sharer_shareinfo=027015312f5a2e81ef3bf8d7b346408d&sharer_shareinfo_first=027015312f5a2e81ef3bf8d7b346408d) | 时间: 2026-04-24 00:00

---

# Hermes Agent命令大全：常用命令全覆盖，从安装到调优

【导读】 装完Hermes Agent，不知道从哪下手？hermes chat、hermes model、hermes gateway、hermes skills、hermes cron……每个命令干什么用，什么时候用，怎么组合用，这篇全给你讲清楚。直接上命令+场景，常用命令全覆盖。

---

## 一、核心命令：日常必用

### hermes chat — 启动对话

```
hermes                         # 启动交互式对话hermes chat -q "Summarize PRs"  # 单次查询，不进入交互模式hermes chat --model claude-sonnet-4  # 指定模型hermes chat --toolsets web,terminal  # 指定工具集hermes chat --resume abc123     # 恢复指定会话hermes chat --continue          # 恢复上一个会话
```

**什么时候用：** 日常对话、临时任务、问问题。

**典型场景：** 打开终端，直接敲 `hermes` 开始聊天；加了 `-q` 参数做单次自动化调用然后退出。

---

### hermes model — 配置模型

```
hermes model                   # 交互式选择模型和Provider/model claude-sonnet-4         # 切换模型（会话内）/model zai:glm-5              # 切换Provider和模型/model claude-sonnet-4 --global  # 切换并保存为默认
```

**什么时候用：** 添加新Provider（OpenRouter、Anthropic等）、首次配置API Key、切换默认模型。

**典型场景：** 切换到更便宜的速度提供商，或者临时用更强模型跑复杂任务。

支持的Provider一览：`auto`, `openrouter`, `nous`, `openai-codex`, `copilot-acp`, `copilot`, `anthropic`, `gemini`, `huggingface`, `zai`, `kimi-coding`, `minimax`, `minimax-cn`, `kilocode`, `xiaomi`, `arcee`。

---

### hermes gateway — 消息网关

```
hermes gateway setup           # 配置消息平台（飞书/Telegram/Discord等）hermes gateway run             # 前台运行（WSL用户用这个）hermes gateway start           # 后台服务启动hermes gateway stop            # 停止服务hermes gateway status          # 查看服务状态
```

**什么时候用：** 配置飞书接入、启动Bot服务、检查运行状态。

**典型场景：** 首次配置飞书Bot用 `setup`，WSL环境下用 `run` 前台运行便于看日志，服务端部署用 `start` 后台守护。

---

## 二、配置与调试：出了问题用这些

### hermes doctor — 自动诊断

```
hermes doctor                  # 诊断配置问题hermes doctor --fix            # 自动修复（能修的自动修）
```

**什么时候用：** 命令报错、连接失败、先跑这个。

**典型场景：** 跑任何命令报错了，第一反应就是 `hermes doctor --fix`，能修的自动修，修不了的告诉你哪里有问题。

---

### hermes status — 查看状态

```
hermes status                  # 快速状态总览hermes status --all           # 完整详细信息hermes status --deep          # 深度检查（耗时更长）
```

**什么时候用：** 快速了解当前配置情况。

**典型场景：** 接手别人的机器，先跑 `hermes status --all` 扫一眼当前配置。

---

### hermes dump — 一键导出诊断信息

```
hermes dump                    # 生成可分享的诊断报告hermes dump --show-keys       # 显示API Key状态（脱敏）
```

**什么时候用：** 提Bug、问社区、让高手帮你看配置。

**典型场景：** 在GitHub Issue或Discord求助前，先跑 `hermes dump` 生成报告链接贴上去，省得来回要日志。

---

### hermes logs — 查看日志

```
hermes logs                    # 查看最近50行hermes logs -f                 # 实时跟踪日志hermes logs gateway -n 100    # 查看gateway日志100行hermes logs --level WARNING --since 1h  # 最近1小时警告级别日志hermes logs --session abc123   # 只看指定会话的日志
```

**什么时候用：** 排查Bug、追踪Agent行为、看Webhook事件。

**典型场景：** 配合 `hermes logs -f` 实时盯日志，定位问题时加上 `--level WARNING` 只看警告。

---

### hermes debug share — 分享调试信息

```
hermes debug share             # 上传诊断报告，生成可分享链接hermes debug share --lines 500  # 包含更多日志行hermes debug share --expire 30  # 30天后过期
```

**什么时候用：** 在Discord/GitHub提问时贴链接。

**典型场景：** 群里有人问你问题，`hermes debug share --lines 500` 一键生成链接甩过去，比截图清晰一百倍。

---

## 三、定时任务与自动化

### hermes cron — 定时任务

```
hermes cron list               # 列出所有定时任务hermes cron create             # 创建新任务（交互式）hermes cron create --skill myskill  # 带Skill创建hermes cron run            # 立即触发执行一次hermes cron pause          # 暂停任务hermes cron resume         # 恢复任务hermes cron remove         # 删除任务hermes cron status             # 查看调度器状态
```

**什么时候用：** 每天自动生成日报、每周自动推送周报、监控任务等。

**典型场景：** 早上8点自动抓取GH Trending生成技术日报，配置一次每天自动跑，不用手动触发。

---

### hermes webhook — 事件触发

```
hermes webhook subscribe  \  --prompt "分析GitHub issue: {payload.title}" \  --events=issues,pull_request \  --deliver telegram \  --deliver-chat-id 你的ChatIDhermes webhook list            # 列出所有Webhook订阅hermes webhook test      # 发送测试事件hermes webhook remove    # 删除订阅
```

**什么时候用：** GitHub有PR自动触发Agent处理、第三方服务事件触发等。

**典型场景：** 给仓库配置一个webhook，收到GitHub Issue事件自动触发Agent分类和初步回复。支持 `--events=issues,pull_request,push` 等多个事件类型，`--deliver` 指定推送平台。

---

## 四、记忆与Skills系统

### hermes skills — 技能管理

```
hermes skills browse           # 浏览Skill市场hermes skills search <关键词>   # 搜索Skillshermes skills install    # 安装Skillhermes skills inspect    # 预览Skill内容（不安装）hermes skills list            # 列出已安装Skillshermes skills check            # 检查Skills更新hermes skills update          # 更新已有Skillshermes skills audit           # 扫描Skills健康状态hermes skills uninstall   # 卸载Skill
```

**什么时候用：** 扩展Agent能力、管理技能库。

**典型场景：** 想做图片生成？`hermes skills search image` 搜一下；装完不确定有没有问题？`hermes skills audit` 扫一遍。

---

### hermes memory — 外部记忆

> `hermes memory configure # 配置外部记忆Provider`

**什么时候用：** 连接Honcho、Mem0等外部记忆系统，实现跨会话记忆共享。

**典型场景：** 需要Agent记住你的偏好、项目背景，用这个配置外部记忆Provider。

---

### hermes honcho — Honcho集成

```
hermes honcho status           # 查看Honcho连接状态hermes honcho setup            # 配置Honcho
```

**什么时候用：** 跨会话记忆共享、用户画像持久化。

**典型场景：** Honcho是一个用户画像服务，配置后每次对话Agent都知道你是谁、关注什么。

---

## 五、数据与文件管理

### hermes backup — 备份

```
hermes backup                  # 全量备份hermes backup --quick         # 快速快照（只备份关键状态）hermes backup -o /path/backup.zip  # 指定备份路径
```

**什么时候用：** 升级前、大改配置前、定期自动备份。

**典型场景：** 升级大版本前跑一遍 `hermes backup`，出了问题一分钟回滚。

---

### hermes import — 恢复

```
hermes import backup.zip      # 从备份恢复hermes import backup.zip --force  # 覆盖恢复
```

**什么时候用：** 换服务器、迁移数据、回滚配置。

**典型场景：** 换了一台新机器，`hermes import backup.zip` 把所有配置和会话历史迁移过去。

---

### hermes sessions — 会话管理

```
hermes sessions list           # 列出所有会话hermes sessions rename    # 重命名会话hermes sessions delete     # 删除会话hermes sessions prune          # 清理旧会话
```

**什么时候用：** 整理会话历史、删除敏感对话、释放存储空间。

**典型场景：** 聊了很多轮之后 `hermes sessions list` 看看有哪些，`prune` 批量清理旧会话。

---

### hermes insights — 用量分析

```
hermes insights                # 查看Token/费用/活跃度统计hermes insights --days 30    # 最近30天统计
```

**什么时候用：** 了解使用成本、优化模型选择。

**典型场景：** 月底跑一下 `hermes insights --days 30`，看看Token消耗分布，考虑是否切换到更划算的Provider。

---

### hermes auth — 凭证管理

```
hermes auth list               # 列出所有凭证hermes auth add openrouter --api-key sk-or-v1-xxx  # 添加API Keyhermes auth remove openrouter 2  # 删除指定Keyhermes auth reset openrouter    # 重置限速
```

**什么时候用：** 管理多个API Key、Key轮换、处理限速。

**典型场景：** 同一个Provider注册了多个Key，某个Key被限速了，`hermes auth reset` 重置后切到另一个。

---

### hermes update — 更新与卸载

```
hermes update                  # 更新到最新版本hermes uninstall              # 卸载Hermes
```

**什么时候用：** 保持最新版本、彻底清理。

**典型场景：** 每次大版本更新后跑 `hermes update`，不想用了 `hermes uninstall` 干净卸载。

---

## 七、Global 全局选项

所有命令都支持以下全局选项：

```
--version, -V                  # 显示版本号--profile, -p            # 指定配置profile--resume, -r       # 恢复指定会话--continue, -c                # 恢复上一个会话--worktree, -w          # 指定工作目录--yolo                        # 跳过确认直接执行--pass-session-id             # 传递会话ID给子进程
```

**什么时候用：** 多实例同时跑不同任务时用 `--profile` 隔离；脚本里自动化跑加 `--yolo` 跳过交互确认。

---

## 八、多实例管理：hermes profile

```
hermes profile list             # 列出所有profilehermes profile create     # 创建新profilehermes profile create  --clone  # 从当前profile克隆配置hermes profile use        # 设为默认profilehermes profile delete     # 删除profilehermes profile alias  --name h-xxx  # 创建快捷命令别名hermes profile export  -o backup.tar.gz  # 导出profilehermes profile import backup.tar.gz --name restored  # 导入profile
```

```
# 用指定profile启动对话hermes -p work chat -q "处理今天的工作任务"
```

**什么时候用：** 工作和生活完全隔离？`hermes profile create work`，`hermes profile use work`，两套配置互不干扰。切换机器时 `export` 备份，`import` 恢复，5秒迁移完成。

**典型场景：** 多人共用一台服务器，每人一个profile；或者同一台机器上区分"日常对话"和"编程任务"两套配置。

---

## 九、OpenClaw迁移（完整参数）

```
hermes claw migrate --dry-run            # 预览迁移内容hermes claw migrate --preset full        # 全量迁移（含API keys）hermes claw migrate --preset user-data   # 只迁移用户数据，不含密钥hermes claw migrate --overwrite          # 覆盖已有文件（默认跳过冲突）hermes claw migrate --source ~/.openclaw  # 指定OpenClaw目录hermes claw migrate --workspace-target ~/.hermes/workspace  # 指定workspace迁移目标hermes claw migrate --skill-conflict overwrite  # 技能冲突处理：skip/overwrite/rename
```

**什么时候用：** 从OpenClaw完整迁移，包括SOUL.md、MEMORY.md、Skills、API keys、Telegram/Discord配置等30+项目。

**典型场景：** 试了几天Hermes决定正式切换，`--dry-run` 先看一遍迁移清单，确认没问题 `--preset full` 正式迁移。

---

## 十、速查表

| 场景 | 命令 |
| --- | --- |
| 启动对话 | `hermes chat` |
| 配置模型 | `hermes model` |
| 配置飞书Bot | `hermes gateway setup` |
| 启动Bot服务（WSL） | `hermes gateway run` |
| 启动Bot服务（后台） | `hermes gateway start` |
| 诊断问题 | `hermes doctor --fix` |
| 导诊断信息 | `hermes dump` |
| 查日志 | `hermes logs -f` |
| 创建定时任务 | `hermes cron create` |
| 安装Skill | `hermes skills install ` |
| 搜索Skill | `hermes skills search <关键词>` |
| 备份配置 | `hermes backup` |
| 恢复备份 | `hermes import backup.zip` |
| OpenClaw迁移 | `hermes claw migrate --dry-run` |
| 查看用量 | `hermes insights` |
| 管理凭证 | `hermes auth list` |
| 更新版本 | `hermes update` |

---

## 九、Provider速查

| Provider | 说明 |
| --- | --- |
| `anthropic` | Anthropic官方（Claude系列） |
| `openrouter` | 聚合多模型的网关 |
| `gemini` | Google Gemini |
| `minimax` / `minimax-cn` | MiniMax（国内可用） |
| `zai` | Nous Research |
| `kimi-coding` | 月之暗面Kimi |
| `openai-codex` | OpenAI Codex |
| `copilot` / `copilot-acp` | GitHub Copilot |

---

**附：版本信息**

- Hermes版本：v0.8.0（2026.4.8）
- 命令参考：https://hermes-agent.nousresearch.com/docs/reference/cli-commands

---

欢迎在评论区聊聊你的想法~

如果这篇文章让你有收获，别忘了点赞、分享、推荐～

也欢迎关注我的公众号，每天有AI最新资讯分享🦐

![](assets/img_b7f486f7e0b7.jpg)

![](assets/img_0c24058d72f3.jpg)
