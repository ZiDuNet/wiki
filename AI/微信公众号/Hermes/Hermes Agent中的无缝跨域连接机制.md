> 📎 来源: [AI步步通](https://mp.weixin.qq.com/s?__biz=MzY4NTE4OTYzNg==&mid=2247483841&idx=1&sn=9b87bcfe8d60ad78116e080833aed800&chksm=f2419a0ce7f45ab3ddb05d656b517e0880a54e6bd4a5a9e423b70e1f6b3f8ff48b2fe7d99b2c&mpshare=1&scene=1&srcid=0429aLFxKVsd2GucEPPn1cdc&sharer_shareinfo=182ce2abac35062633f4f68db7d758bb&sharer_shareinfo_first=182ce2abac35062633f4f68db7d758bb) | 时间: 2026-04-29 03:49

---

很多 Agent 看起来接了很多入口，实际工程形态却很分裂。命令行是一套调用链，Discord Bot 是另一套回调逻辑，Telegram 又单独维护轮询、权限、会话和消息格式。平台一多，团队维护的往往不是一个 Agent，而是好几份不断漂移的半成品。

Hermes 的 Gateway 体系，就是为了解决这层分裂。多入口接入不再是零散脚本，而是一套单独维护的系统能力。团队维护的重点因此回到同一个 Agent 内核，平台差异留在接入层处理。

维护重心也随之集中到统一核心。一套核心代码可以同时面向命令行、聊天平台、后台服务和容器化部署；团队持续维护的，是同一套能力在不同入口上的复用，而不是多份各自漂移的 Bot 逻辑。

入口越多，系统越需要先解决“同一套 Agent 能不能稳定复用”。Gateway 的作用，就是把复用边界和平台边界分开。

Hermes 的通信与部署体系可以分成三层：外层是不同入口壳，中间是流式适配、统一控制面和统一核心，底部是状态与身份、执行后端、部署包装三块底座。

Hermes 统一通信与部署架构综合图CLI / TUI当前目录、终端交互直接进入 AIAgentMessaging GatewayTelegram / Discord / WeCom / Weixin / Slack / QQ会话路由、权限、cron、语音、结果投递HTTP 入口API Server / WebhookOpenAI 兼容 / HMAC流式适配层stdout token 流 / OpenAI SSE / progressive message editingedit\_interval、buffer\_threshold、长度溢出分段、平台能力自动降级统一控制面平台适配器、allowlist / pairing、session key、线程隔离、tool progress、interruptpending approval、notify\_on\_complete、cron delivery、webhook route通信协议与运行状态停在控制面，平台细节不渗进核心 AgentAIAgent 统一核心prompt builder / memory / skills / tools / approvals / context compressionCLI、Gateway、API Server 共用同一执行循环，只更换入口与包装方式状态与身份层SQLite / JSONL sessionsMEMORY.md / USER.md / skills / profiles执行后端local / docker / ssh / modal / daytona隔离文件系统、命令副作用与进程空间部署包装foreground / systemd / launchdDocker / profiles / webhook mode

从外到内，Hermes 的通信与部署体系依次是入口层、流式适配层、统一控制面、统一核心，以及底部的状态、执行和部署边界。

图里的六层结构

1. 入口层：CLI、Messaging Gateway、HTTP 入口分别承接终端、聊天平台和 API/Webhook 请求。

2. 流式适配层：把同一条回答包装成终端输出、SSE 流或消息编辑更新。

3. 统一控制面：处理平台适配、会话路由、审批、中断、定时任务和结果投递。

4. 统一核心：AIAgent 复用同一套 prompt、memory、skills、tools 和 approvals。

5. 状态与身份层：保存 sessions、profiles、skills 以及长期记忆相关文件。

6. 执行与部署边界：terminal backend 决定副作用隔离，deployment packaging 决定服务形态。

## 一、CLI、Messaging Gateway、HTTP 入口只是三种接入方式

Hermes 的三种入口分别承担不同接入职责。CLI / TUI 处理本地目录与终端交互；Messaging Gateway 对接 Telegram、Discord、企业通信平台和各类消息渠道；HTTP 入口则承接 API Server 与 Webhook。入口形态完全不同，但它们都只是 Agent 接触外部世界的壳。

系统不再按平台切业务逻辑。Telegram 需要处理 BotFather 发出的 token、群聊隐私和 webhook 或轮询；Discord 需要处理 mention 规则、线程隔离、权限整数和语音频道；Webhook 则要接 HMAC 校验（消息签名校验）、HTTP 路由和幂等去重。这些都属于平台协议差异，应该停留在边缘，不该一路渗进 Agent 核心。

HTTP 入口同样只是接入层。它已经支持 OpenAI 兼容的 

```
/v1/chat/completions
```

 与 

```
/v1/responses
```

，Webhook 则负责把外部事件送进系统。入口可以很多，但入口本身不该决定 Agent 内核怎么写。结果如何回到不同渠道，取决于下一层的输出适配。

## 二、流式适配层决定回答怎么回传

同一个核心能否稳定挂到多个入口上，取决于输出链路是否已经统一。回传协议天然就是分裂的：CLI 可以把 token 直接打到 stdout；OpenAI 兼容 API 要按 SSE（Server-Sent Events，服务器推送事件）逐块吐出数据；Discord、Telegram、Slack 这类聊天平台却不能每来一个 token 就发一次请求，必须靠消息编辑、缓冲阈值和节流间隔把连续 token 重新包装成平台能承受的更新频率。

这层适配已经有明确接口。API Server 在开启 

```
stream: true
```

 后会返回 OpenAI 兼容的 SSE 数据块，并把工具进度标记内嵌进流里；消息平台侧则提供了 

```
transport: edit
```

、编辑间隔和缓冲阈值这类流式控制项。Hermes 没有把平台差异继续推给业务逻辑，而是在传输层做了专门的流式重封装。

```
AIAgent
```

 产出统一文本流和工具进度事件，CLI 直接打印，API Server 重新编码为 SSE，聊天平台则走缓冲后编辑消息。统一输入之外，统一输出也在流式适配层完成。

同一条回答流在三种入口上的不同包装

1. CLI：直接输出 token 流和工具进度，追求最低延迟。

2. API Server：把同一条输出改写成严格的 SSE 数据块，供 OpenAI 兼容前端消费。

3. Discord / Telegram / Slack：先缓冲，再按编辑频率批量刷新，避免 API flood 与消息抖动。

4. 不支持消息编辑的平台会自动关闭流式更新，改走一次性结果投递。

## 三、统一控制面把会话、审批和结果投递收口

Gateway 是一个单独常驻的后台进程，负责连接所有已配置平台、维护会话、运行定时任务，并把结果送回对应渠道。它承担的是 Hermes 对外通信的统一控制面，不是某个平台的 SDK 包装层。

在这套分工里，平台适配器负责接收消息，再把消息送进每个聊天空间自己的 session store，随后统一派发给 

```
AIAgent
```

。系统因此按平台切接入协议，而不再按平台切业务逻辑。

Gateway 当前承担的四层职责

平台接入：Telegram、Discord、WeCom、Weixin、Webhook 等各自处理认证、回调和消息协议

会话路由：按私聊、群聊、线程、用户维度生成 session key，决定上下文边界

统一执行：把消息送进同一个 Agent 主循环，继续复用 memory、skills、toolsets 和审批机制

结果投递：把文本、语音、文件、后台任务结果和定时任务消息送回正确目标

审批、打断和恢复，比普通消息转发更容易暴露问题。危险命令一旦触发审批，系统就不能只弹出一个“yes/no”提示框了事；它必须在正确的会话里停下来，把审批请求发给正确的人，再在同一个上下文里继续往下跑。手动审批模式下，CLI 弹交互式确认框；Messaging 模式会创建 

```
pending approval request
```

（待审批请求），把危险命令详情发回聊天渠道，等待用户用 

```
yes / no
```

 或 

```
/approve / /deny
```

 继续。

审批流程示例

Bot：即将执行 

```
rm -rf /workspace/tmp
```

，需要审批。

Bot：回复 

```
yes
```

 或 

```
/approve
```

 继续，回复 

```
no
```

 或 

```
/deny
```

 取消。

用户：

```
yes
```

。系统随后回到原 session，继续执行后续步骤。

要让审批链路稳定，session key 就必须足够细。默认规则是：私聊按 chat id，群聊按 

```
chat_id + user_id
```

，线程再叠加 

```
thread_id
```

。在群聊里采用每用户隔离时，中断状态也会沿着这个隔离后的 running-agent key 走。审批、打断、继续，都靠这条确定性的 session 语义接起来。

对于后台长任务，Hermes 又补了一层 completion 通知。现在已经有 

```
notify_on_complete
```

，后台进程完成后会自动通知 Agent，而不是靠人工轮询。这让“挂起后等结果回来再继续”在工具层面更完整了。

当前稳定路径依赖 pending approval、确定性 session key、每用户中断隔离和 GatewayRunner 的中断处理。跨渠道转交管理员、竞争仲裁和更深一层的恢复控制，不在当前公开配置面内。

## 四、AIAgent 统一核心留在中间

CLI、Gateway、API Server 共用同一个 Agent 核心。这层复用关系在目录结构中直接可见：

```
run_agent.py
```

 里的 

```
AIAgent
```

 仍是核心执行循环，CLI 直接调用它，Gateway 通过 

```
GatewayRunner
```

 把平台消息转给它，API Server 也把 OpenAI 兼容请求转给同一套核心工具链。

命令行、聊天平台和 HTTP 接口不是三套业务逻辑，而是三种不同的输入壳。它们共享同样的 memory、skills、session persistence、tool dispatch 和 prompt builder。不同入口之间变化的，主要是输入协议、会话键生成方式、权限规则，以及每个平台默认开放哪些 toolset。

边界这样划开之后，团队增强工具审批、技能加载、记忆注入、上下文压缩时，不需要去 Telegram、Discord、CLI 分别补丁，而是在统一核心里改一次，再让所有入口共同受益。统一核心解决的是逻辑复用，运行时隔离还要继续往下看状态层和执行层。

## 五、session、memory、profile 各管一层隔离

状态与身份层承接的是 SQLite / JSONL sessions、

```
MEMORY.md
```

、

```
USER.md
```

、skills 和 profiles。它决定“谁是谁”“上下文存在哪”“长期记忆挂在哪”，但不负责真正的命令副作用隔离。

多实例网关里，最常见的误判是把“记忆隔离”写成“执行隔离”。Hermes 的 Profile 设计确实已经把 config、memory、sessions、skills 和 gateway service 拆开了，也通过 token-lock isolation 避免两个 profile 复用同一个 Bot 凭证。但这只能保证身份域和状态域分开，不能自动保证工具副作用互不污染。

## 六、执行后端隔离副作用，部署包装承接长任务形态

Profile 只能隔离身份域和状态域，副作用边界还要看 terminal backend。这里的规则很硬：

```
local
```

 后端没有隔离，命令直接跑在宿主机；

```
docker / singularity / modal / daytona
```

 才是正式的沙箱边界。Docker 还给出了更具体的安全参数：只读根文件系统、drop all capabilities、禁止提权、PID 限额、独立 

```
namespace
```

（进程、网络等隔离空间）。持久化模式下，它把工作区绑定到 

```
~/.hermes/sandboxes/docker//
```

；Modal 和 Daytona 也都按 task 或 sandbox 做独立工作区。

因此，即便 Alice 和 Bob 在 Discord 上拥有完全独立的 session key，只要整个生产 Gateway 仍挂在 

```
local
```

 backend 上，他们就仍然可能共享宿主机副作用域。Profile 隔离不了这个问题，session 也隔离不了这个问题。面向生产 Gateway 部署，更稳的做法是把 

```
docker
```

、

```
modal
```

 或 

```
daytona
```

 当作执行边界。

执行隔离与通信隔离要分开看

1. Profile 解决的是配置、记忆、技能、令牌与服务实例隔离。

2. Session key 解决的是上下文、打断状态和审批归属隔离。

3. Terminal backend 解决的才是文件系统、进程和命令副作用隔离。

4. 生产网关若仍跑在宿主机本地后端上，前两层再干净也挡不住副作用串扰。

执行边界落在 terminal backend，服务形态落在 deployment packaging。

```
foreground / systemd / launchd / Docker / profiles / webhook mode
```

 对应的是“这个 Agent 以什么服务方式存在”，而不是“它的业务逻辑是什么”。Webhook 适配器已经能接收外部事件，跑完 Agent，再把结果投到 GitHub comment、Telegram、Discord、Slack 等目标；Cron 也能在新 session 里执行任务，并把结果送回创建来源或指定平台。另有一个 

```
/api/jobs
```

 REST API 用于 cron job 管理。

API 长任务回传是另一条独立边界。当前公开主接口稳定提供的是 SSE 流、服务端会话续接（

```
previous_response_id
```

）和幂等去重（

```
Idempotency-Key
```

，幂等键）。通用的 

```
task_id + callback
```

 工作流，不在当前公开主接口里。

## 七、生产级网关依赖分层控制面

Hermes 把几种原本最容易缠在一起的复杂性拆到了不同层。传输复杂性放在 streaming adapter，会话复杂性放在 deterministic session key，审批与中断复杂性放在 pending approval 与 GatewayRunner，执行副作用复杂性放在 terminal backend 与 sandbox。每一层只处理自己那一层的事。

企业级 Agent 平台也需要把通信协议、审批状态、执行安全边界和异步回传链路分开处理。Hermes 的主路径已经明确：入口统一只是起点，生产级网关还要把流式回传、会话控制、执行隔离和结果投递分别落到稳定的控制面里。

你在多平台接入 Agent 时遇到过哪些问题，欢迎留言交流。
