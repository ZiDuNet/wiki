> 📎 来源: [AIGClaw](https://mp.weixin.qq.com/s?__biz=MzI2NTU0NTI2Nw==&mid=2247483902&idx=1&sn=2ef3fbc6713666b7c94122989ccc8856&chksm=eb8671ca75ae78951b632b184c5fd5c0e89a6cc6c23b5a73b8b6455eba764a97a7f92e628fac&mpshare=1&scene=1&srcid=0510ZplUvn5dNGwuVoCfhvHH&sharer_shareinfo=ee263090df22b06f4e9b273c16a39b64&sharer_shareinfo_first=ee263090df22b06f4e9b273c16a39b64) | 时间: 2026-05-10 15:50

---

> (https://hermes-agent.nousresearch.com/docs/guides/tips)（官方文档）

# 【写在前面】

Hermes Agent 是 Nous Research 推出的 AI 助手框架，支持多平台接入（飞书、微信、Telegram、Discord 等），内置 Skills 技能系统、记忆系统、任务委托等进阶功能。本文提炼了官方最佳实践的 13 条核心技巧，分七类展开，适合收藏备用。

# 一、获取最佳结果

## 1. 需求要具体

模糊的提示词产出模糊的结果。与其说「修复代码」，不如说：

```
修复 api/handlers.py 第 47 行的 TypeError——process_request()
```

    给的背景越充分，迭代次数越少。

## 2. 上下文提前给

    把相关细节（文件路径、错误信息、期望行为）一次性说清楚。一条精心构造的消息，胜过三轮补充说明。直接把错误堆栈粘贴过来，Agent 能直接解析。

## 3. 重复指令交给上下文文件

如果经常重复同一类指令（如「用 tabs 不用 spaces」「我们用 pytest」），把它们写入 AGENTS.md 文件。Agent 每次新会话都会自动读取，零额外成本。如下配置：

```
FastAPI + SQLAlchemy ORM
```

## 4. 让 Agent 自己使用工具

    不要手把手指挥每一个步骤。说「找出来并修复那个失败的测试」，而不是「打开 tests/test\_foo.py，看第 42 行，然后……」。

    Agent 有文件搜索、终端访问和代码执行能力，让它们自主探索和迭代。

## 5. 复杂流程先查 Skills

    在写一大段提示词之前，先看看是否已有现成的 Skill。输入 /skills 浏览可用技能，或直接调用如 /axolotl、/github-pr-workflow。也可以在飞书等app中询问有哪些skill，以及各自的作用

# 二、CLI 进阶技巧

## 6. 多行输入：Alt+Enter（或 Ctrl+J）

    按 Alt+Enter（或 Ctrl+J）插入换行但不发送，方便在发送前构思多行提示词、粘贴代码块或组织复杂请求。

## 7. 自动检测粘贴

    CLI 会自动检测多行粘贴，直接粘贴代码块或错误日志不会逐行发送，完整内容作为一条消息发出。

## 8. 中断与重定向：Ctrl+C

    按一次 Ctrl+C 中断 Agent 当前回复，可输入新内容重定向； 2 秒内按两次 Ctrl+C强制退出 当 Agent 走上弯路时，这个组合键非常实用。

## 9. 用 -c 恢复上一会话

    忘记上次的进度？运行 hermes -c 从断点继续，对话历史完整恢复。也可以按标题恢复：hermes -r "我的研究项目"。

## 10. 剪贴板图片直接粘贴

    按 Ctrl+V 将剪贴板图片直接粘贴到对话，Agent 用视觉分析截图、图表、错误弹窗或 UI 稿，无需先保存文件。

## 11. 斜杠命令 Tab 自动补全

   输入 / 再按 Tab，显示所有可用命令（包括内置命令 /compress、/model、/title 和所有已装 Skills），无需记忆，Tab 搞定一切。

> 💡**/verbose 切换工具输出显示模式：off → new → all → verbose。简单问答用 off，CLI 中用 all 获得沉浸感。**

# 三、上下文文件

## 12. AGENTS.md + SOUL.md

| 文件 | 用途 | 位置 |
| --- | --- | --- |
| AGENTS.md | 项目的大脑——放架构决策、编码规范、项目特定规则 | 项目根目录 |
| SOUL.md | 个性化——定义 Agent 的默认说话风格 | ~/.hermes/SOUL.md |

⚠️保持上下文文件简洁——每个字符都会计入每次消息的 token 预算。

# 四、记忆与技能（Memory & Skills）

## 13. Memory 存「事实」，Skills 存「流程」

    Memory（记忆）用于：环境信息、个人偏好、项目路径、Agent 学会的关于你的事

    Skills（技能）用于：多步骤工作流、工具特定指令、可复用方案

    什么时候创建 Skill：如果一个任务需要 5 步以上且你会重复做，告诉 Agent「把刚才做的存成一个叫 deploy-staging 的 Skill」，下次直接 /deploy-staging。

    定期清理：Memory 有容量限制（约 2,200 字符），满了 Agent 会自动合并。可以主动说「清理一下你的 memory」或「把 Python 3.9 那条更新为 3.12」。

> ⚠️**Memory 是会话启动时的快照——本会话内的修改不会立刻影响当前会话的 system prompt，要到下个会话才生效。**

# 五、性能与成本

- 保持提示词稳定

    不频繁切换模型或 system prompt，可获得更多缓存命中，显著降低成本

- 用 /compress

    会话变长时运行，压缩历史记录保留关键上下文

- 用 /usage和/insights

    定期查看 token 消耗和使用模式

- 委托并行任务

    需要同时研究三个主题？让 Agent 用 delegate\_task 并行执行，主对话 token 消耗更低

- 选对模型

    复杂推理用 Sonnet/Opus，格式化/重命名等简单任务切换快速模型

# 六、消息平台使用技巧

- 设置 Home Channel

  用 /sethome 指定一个 Telegram 或 Discord 聊天室作为主频道，定时任务结果会发到这里

- 给会话命名

  用 /title 给会话起名，也可以在飞书中发送如下信息可以给飞书的session命名

  ```
  /title 飞书
  ```

   方便之后 hermes sessions list 查找和 hermes -r 恢复

- DM Pairing

    队友给机器人发消息会自动收到配对码，用 hermes pairing approve telegram XKGH5N7P 审批，替代手动收集用户 ID

- /verbose 按需切换

    消息平台建议 new，CLI 建议 all

> 💡 在消息平台上，sessions 会自动重置（空闲 24 小时或每天凌晨 4 点）。如有需要可在 ~/.hermes/config.yaml 中调整。

# 七、安全建议

- 处理不受信代码用 Docker

    设置 TERMINAL\_BACKEND=docker，容器内破坏性命令不会影响宿主机

- Windows 用户注意编码

    默认编码无法表示所有 Unicode 字符，文件写入时显式指定 UTF-8：

```
with open("results.txt", "w", encoding="utf-8") as f:
```

- 危险命令谨慎授权

    触发 rm -rf、DROP TABLE 等高危操作时，四个选项（once / session / always / deny）选 always 前三思

- 消息平台机器人用 Allowlist

    禁止 GATEWAY\_ALLOW\_ALL\_USERS=true，用TELEGRAM\_ALLOWED\_USERS 等白名单

> ⚠️ 在容器后端（Docker、Singularity、Modal、Daytona）环境下，危险命令检查会被跳过，因为容器本身就是安全边界。请确保容器镜像已正确锁定。

# 总结

Hermes Agent 最佳实践的三条核心原则：

> **1. 给足上下文，少走弯路**

> **2. 让工具干活，别手把手指挥**

> **3. 用 Memory 记住事实，用 Skills 复用流程**

掌握这 13 条技巧，你与 Hermes Agent 的协作效率将显著提升。
