> 📎 来源: [超级AI技术](https://mp.weixin.qq.com/s?__biz=MzUyNzA1NDY0MQ==&mid=2247485594&idx=1&sn=e72c8c0e123086b7651aefd2107c5d56&chksm=fb1e164e9020c714c8ffdb3822f6c004f1851a28729045b8fa2bc5a544a0005c87926ff2fdf0&mpshare=1&scene=1&srcid=04289HVajt1rbLQnNsVTf6wH&sharer_shareinfo=aafe8f719c39afc3870211ae9077e029&sharer_shareinfo_first=aafe8f719c39afc3870211ae9077e029) | 时间: 2026-04-28 19:44

---

> 从快速跑通，到把交互体验和成本结构一起调顺，这篇文章把 Hermes Agent 三条最实用的进阶路线讲清楚。

## 先看结论：你该先用哪一套

很多人第一次上手 Hermes Agent，会把精力放在“模型怎么选”上。但真用起来，通常先要回答的是另外一个问题：

**你现在最缺的是跑通、体验，还是成本控制？**

先看这张选择表：

| 方案 | 适合人群 | 解决的问题 | 难度 |
| --- | --- | --- | --- |
| **Ollama 快速接入** | 第一次上手 Hermes 的用户 | 先把本地或云端模型跑通 | ⭐ |
| **Open WebUI 前端** | 日常高频使用者 | 让 Hermes 变成更像 ChatGPT 的交互界面 | ⭐⭐ |
| **主模型 + 辅助模型分工** | 已经稳定使用、开始关心账单的人 | 把高质量和低成本拆开配置 | ⭐⭐⭐ |

如果你是第一次接触 Hermes，建议顺序是：

1. 先用 Ollama 跑通一条最短链路

2. 再接 Open WebUI，把日常使用体验做顺

3. 最后再动主模型与辅助模型分工，去压成本

这样比较稳。

---

## 方案一：先用 Ollama 把 Hermes 跑通

### 这套方案适合什么场景

• 想先用最短路径把 Hermes Agent 跑起来

• 想直接接本地模型或 Ollama Cloud

• 不想一开始就手动改太多配置

Hermes 和 Ollama 现在已经有官方集成页，最短路径比以前简单很多。

按 Ollama 当前官方文档，直接执行：

ollama launch hermes

Ollama 会处理下面这些步骤：

1. 如果本机还没装 Hermes，会提示安装

2. 让你选择模型（本地模型或 cloud 模型）

3. 自动把 Hermes 指到 Ollama 本地接口

4. 可选地继续接消息网关，最后进入 Hermes 对话

Ollama 官方目前给 Hermes 推荐的模型里，cloud 方向包括：

• 

```
kimi-k2.5:cloud
```

• 

```
glm-5.1:cloud
```

• 

```
qwen3.5:cloud
```

• 

```
minimax-m2.7:cloud
```

本地方向则更建议看：

• 

```
gemma4
```

• 

```
qwen3.6
```

如果你的目标只是“尽快上手”，最省事的路径就是直接走

```
ollama launch hermes
```

。

### 如果你要纯本地运行

有些场景不适合云端模型，比如：

• 数据不能离开内网

• 希望完全离线

• 不想引入额外 API 成本

• 只是想先在自己机器上试清楚

这时可以让 Hermes 直接接本地 Ollama。

Hermes 官方配置文档里，把 Ollama 归在“本地 OpenAI 兼容服务”这一类。实际写法建议保留标准接口形式：

model:

  provider: ollama

  base\_url: http://127.0.0.1:11434/v1

  default: qwen3.6

这里有两个细节值得注意：

• 

```
provider: ollama
```

 走的是本地服务别名

• 

```
base_url
```

 用 OpenAI 兼容地址时，建议写到

```
/v1
```

如果机器配置比较紧，可以先从小模型起步。更重要的是把链路跑通，而不是一开始就追求最大参数量。

### 纯本地模式的硬件判断

可以粗略这样看：

| 场景 | 建议配置 |
| --- | --- |
| 轻量试用 | 8GB 内存起步，先跑小模型 |
| 日常开发 | 16GB 以上更稳 |
| 更大模型 / 更长上下文 | 优先看显存和内存，而不是只看 CPU |

如果你是 Apple Silicon，Ollama 会自动利用本机 GPU；如果是 NVIDIA 环境，驱动和 CUDA 配好之后，也能明显改善本地推理体验。

这一套首先要解决的是：

**先把 Hermes 跑起来，并且保证你知道模型到底跑在本地还是云端。**

---

## 方案二：用 Open WebUI 把 Hermes 变成可长期使用的前端

### 为什么很多人跑通后还是不好用

Hermes 跑起来之后，第二个常见问题往往会变成交互体验。

如果你长期在终端里直接聊，或者把它塞进一个 Markdown 支持一般、历史管理也弱的聊天入口，几轮之后就会开始觉得：

• 对话太长，不好回看

• 代码块和 Markdown 展示不够舒服

• 历史检索麻烦

• 多轮任务很容易丢上下文

这时候，Open WebUI 的价值就出来了。

Open WebUI 官方文档已经单独写了 Hermes 的接入说明，核心思路很简单：

• Hermes 作为 Agent 后端

• Open WebUI 作为聊天前端

• 两边通过 OpenAI 兼容接口连接

### 官方推荐接法

Open WebUI 文档给出的做法是：

先在 Hermes 的环境文件里打开 API Server：

API\_SERVER\_ENABLED=true

API\_SERVER\_KEY=your-secret-key

然后启动网关：

hermes gateway

正常情况下你会看到类似输出：

[API Server] API server listening on http://127.0.0.1:8642

接下来在 Open WebUI 里新增一个 OpenAI 连接，填：

| 项目 | 值 |
| --- | --- |
| URL | ``` http://localhost:8642/v1 ``` |
| API Key | 上面设置的   ``` API_SERVER_KEY ``` |

如果 Open WebUI 本身跑在 Docker 里，官方文档建议把

```
localhost
```

 换成：

http://host.docker.internal:8642/v1

### 这套方式的核心价值

接好以后，Hermes 还是那个 Hermes，但你会多出几个对长期使用非常关键的能力：

• 会话侧边栏更清楚

• Markdown 和代码块展示更稳定

• 历史检索更自然

• 多轮任务更容易回看

• 更适合把 Hermes 当成一个持续使用的工作入口，而不是临时脚本

这套方案真正解决的是：

**让 Hermes 从能用，变成适合日常长期使用。**

### 一个容易踩的坑

Open WebUI 文档里专门提到一个高频问题：

如果连接测试能过，但模型列表加载不出来，最常见原因是 URL 少了

```
/v1
```

。

连接地址要这样写：

• 对：

```
http://localhost:8642/v1
```

• 错：

```
http://localhost:8642
```

这个细节看着小，但很容易卡住第一次接入。

---

## 方案三：主模型负责质量，辅助模型负责省钱

### 这套玩法到底在省什么

很多人开始算 Hermes 成本时，第一反应是换一个更便宜的主模型。

更有效的做法，是把不同类型的任务拆开：

• 主对话、复杂判断、关键执行，交给质量更稳的模型

• 压缩、网页提取、审批判断、标题生成这类辅助链路，交给更快更便宜的模型

Hermes 官方配置文档里，

```
auxiliary
```

 就是干这个的。

文档明确写了：Hermes 会把图像分析、网页总结、上下文压缩等任务交给辅助模型；默认情况下会自动选择 Gemini Flash 一类的轻量模型，不一定需要你手动改。

成本优化没必要一上来就全局重写模型策略。
更稳的方式是：

**先保住主模型质量，再把辅助链路拆去便宜模型。**

### 一个更稳的配置思路

如果你已经确定主模型要走 MiniMax，而辅助链路想走 Gemini Flash，可以按 Hermes 当前的统一配置模式来写。

主模型：

model:

  provider: minimax-cn

  default: minimax/minimax-m2.7

这里我更建议直接使用 Hermes 内置 provider 路由，而不是手动写

```
base_url
```

。
原因很简单：官方配置文档已经说明，当只设置

```
provider
```

 时，Hermes 会自动使用该 provider 的鉴权和 base URL；只有你明确要接一个自定义 OpenAI 兼容端点时，才需要手写

```
base_url
```

。

辅助模型：

auxiliary:

  approval:

    provider: gemini

    model: gemini-2.5-flash

    timeout: 30

  compression:

    provider: gemini

    model: gemini-2.5-flash

    timeout: 120

  flush\_memories:

    provider: gemini

    model: gemini-2.5-flash

    timeout: 30

  mcp:

    provider: gemini

    model: gemini-2.5-flash

    timeout: 30

  session\_search:

    provider: gemini

    model: gemini-2.5-flash

    timeout: 30

  skills\_hub:

    provider: gemini

    model: gemini-2.5-flash

    timeout: 30

  title\_generation:

    provider: gemini

    model: gemini-2.5-flash

    timeout: 30

  vision:

    provider: gemini

    model: gemini-2.5-flash

    timeout: 30

    download\_timeout: 30

  web\_extract:

    provider: gemini

    model: gemini-2.5-flash

    timeout: 360

### 这里有几个关键点

第一，Hermes 官方文档已经把

```
auxiliary
```

 说明成统一模式：

• 

```
provider
```

• 

```
model
```

• 

```
base_url
```

三个旋钮是一致的。
走官方 provider 时，通常只需要

```
provider + model
```

。

第二，

```
main
```

 这个 provider 只适用于 auxiliary / fallback 这类场景，不能拿去填顶层

```
model.provider
```

。这一点官方文档也专门提醒过。

第三，压缩模型选择要看

```
auxiliary.compression
```

，而不是把旧时代的

```
summary_*
```

 之类字段继续往

```
compression
```

 里塞。

### 环境变量和引用方式

如果你在

```
~/.hermes/.env
```

 里放 key，正文配置建议都用

```
env:
```

 方式引用，不直接写明文。

例如：

mcp\_servers:

  gbrain:

    command: gbrain

    args: [serve]

    env:

      OPENAI\_API\_KEY: env:OPENAI\_API\_KEY

    connect\_timeout: 15

    timeout: 30

这样后续迁移和多人协作会干净很多。

### 不要一次把所有辅助链路都改掉

这套玩法最容易踩的坑，是一口气把所有辅助任务都切到便宜模型，然后出了问题又不知道是哪一层先坏的。

更稳的顺序通常是：

1. 先保持主模型不动

2. 先改

```
auxiliary.compression
```

3. 再改

```
web_extract
```

4. 最后再考虑审批、标题、vision 这些支线

这样一旦哪条链路出问题，回滚会更容易。

---

## 推荐上手顺序

如果你现在要真正把这篇文章里的三套玩法用起来，建议按这个顺序落地：

### 第一步：先跑通

先用 Ollama 官方集成把 Hermes 跑起来，确认：

• 模型能正常响应

• Hermes 本体装好

• 你知道当前到底在用本地模型还是 cloud 模型

### 第二步：再把前端体验做顺

把 Open WebUI 接上，确认：

• 

```
http://localhost:8642/v1
```

 能被正常识别

• 会话侧边栏、Markdown、代码块都可用

• 多轮对话不会因为前端体验太差而中途放弃

### 第三步：最后再做成本优化

把主模型和辅助模型分开，重点观察：

• 压缩链路是否稳定

• 网页提取是否变慢或变差

• 总体成本是否真的下降

• 主对话质量有没有被牵连

这个顺序的好处是，出问题时你知道到底是哪一层的问题。

---

## 写在最后

Hermes Agent 的进阶玩法，表面上看是“换模型、加前端、调配置”，本质上其实是三件事：

1. 把系统先跑通

2. 把使用体验做顺

3. 把成本结构调合理

如果你现在还是第一次接触 Hermes，不建议三套方案一起上。
最稳的节奏永远是：

• 先用 Ollama 跑通

• 再接 Open WebUI

• 最后再拆主副模型

这不是最炫的路线，但通常是最省时间、也最不容易把自己绕进去的路线。

## Change Log

1. 把文章结构改成“先选路线，再讲三种玩法”，目录更适合公众号阅读。

2. 把 Ollama、本地配置、Open WebUI 连接和辅助模型配置统一成更接近当前官方文档的写法。

3. 删除了容易过期或缺乏验证支撑的细节，比如固定技能数量、过于武断的配置断言。

## Pre-submission Checklist

• [x] 关键配置项已按官方文档做过最小核验

• [x] Open WebUI 连接地址与 API Server 开法已明确

• [x] 本地 Ollama 配置示例已统一到 OpenAI 兼容接口写法

• [x] 主模型与辅助模型分工逻辑已拆清

• [x] 文内没有残留禁用脚手架表达
