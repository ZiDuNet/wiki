> 📎 来源: [AI新工具实战派](https://mp.weixin.qq.com/s?__biz=MzkxNjM4NjQ1NQ==&mid=2247484464&idx=1&sn=17fb467c0836908b051241adbf21b1cf&chksm=c0fd0aa9947d14fd21a340a686d4a8f3fa29fe750c2948302f808419b28b15f26a7d23644fc6&mpshare=1&scene=1&srcid=0428sXC4rySLinkoNwplE8sp&sharer_shareinfo=35f31ef77e55e48387c783fb0de92f81&sharer_shareinfo_first=35f31ef77e55e48387c783fb0de92f81) | 时间: 2026-04-28 06:45

---

![](assets/img_658de8520c36.png)

01

全局选项｜前置通用参数

![](assets/img_801be45f4037.gif)

![](assets/img_03f15eb192fd.gif)

✅ 所有命令都能搭配使用，全局快速控制运行环境

- `hermes --version / -V`

👉 快速查看当前客户端完整版本号

- `hermes -p `

👉 切换指定 Profile 多环境配置，适配多项目隔离使用

- `hermes -r `

👉 精准恢复指定历史会话，接续之前的代理工作进度

- `hermes -c [name]`

👉 一键恢复最近一次会话，无需手动检索会话记录

- `hermes --yolo`

👉 跳过所有高危操作二次确认，适合脚本自动化批量执行场景

- `hermes --tui`

👉 拉起终端可视化交互界面，纯窗口化操作，直观好上手

- `hermes --worktree`

👉 为并行多代理工作流创建独立隔离空间，互不干扰运行

- `hermes --pass-session-id`

👉 将会话ID同步透传给下游代理链路，方便全链路日志溯源排查

02

核心高频命令｜日常90%场景都用这部分

![](assets/img_801be45f4037.gif)

![](assets/img_03f15eb192fd.gif)

🔹 聊天交互｜Agent 核心对话能力

- `hermes chat`

👉 默认交互式长对话，实时和AI代理连续沟通，适配复杂需求拆解

- `hermes chat -g "你的问题"`

👉 单次快速问答，无需进入交互会话，轻量化临时查需求

- `hermes chat --model `

👉 单次对话临时指定专属大模型，灵活切换适配不同任务场景

- `hermes chat --provider `

👉 手动切换模型服务供应商，适配多接口、多厂商混合部署环境

- `hermes chat --toolsets `

👉 按需启用批量工具集，多工具英文逗号分隔，一键批量挂载

- `hermes chat --skills `

👉 对话前置预加载专属技能，提前挂载能力，上手直接调用

- `hermes chat --image <本地路径>`

👉 本地图片直接上传联动对话，支持图文多模态交互分析

- `hermes chat --max-turns `

👉 限制本轮对话最大工具调用轮次，避免无限循环调用耗资源

- `hermes chat --checkpoints`

👉 开启文件系统快照检查点，中途断电也能无缝恢复对话进度

🔹 环境设置｜首次装机、换环境必用

- `hermes setup`

👉 一站式全流程初始化向导，新手装机无脑跟着回车即可完成配置

- `hermes setup model`

👉 单独重装、切换、对接大模型接口，不动其他全局配置

- `hermes setup terminal`

👉 适配当前终端编码、字体、交互样式，解决终端适配报错问题

- `hermes setup gateway`

👉 配置消息推送网关，对接第三方平台联动消息同步

- `hermes setup tts`

👉 配置语音合成播报能力，适配语音交互、播报类落地场景

- `hermes setup tools`

👉 批量配置全局工具权限、调用白名单，规范工具使用范围

- `hermes setup agent`

👉 自定义代理行为规则、响应策略，贴合业务场景定制代理逻辑

- `hermes setup --reset`

👉 一键清空所有自定义配置，彻底还原出厂初始纯净环境

🔹 登录认证｜账号凭据安全管理

- `hermes auth`

👉 统一凭据管理中心，新增、查看、轮换密钥、清理过期权限全覆盖

![](assets/img_c5858ec0abe4.png)

![](assets/img_260ac0e54387.png)

⚠️hermes login / logout 已全面弃用，统一只用 hermes auth 更安全合规

![](assets/img_d710edfc2924.png)

![](assets/img_fda6b1e8991f.png)

🔹 状态排障｜运维查问题专用

- `hermes status`

👉 全景速览：代理运行状态、认证有效性、网关在线状态一键全查

- `hermes doctor`

👉 智能体检，自动扫描配置冲突、端口占用、密钥过期、环境缺失依赖

- `hermes config`

👉 快速打印全部运行中生效配置，核对参数不用翻底层文件

- `hermes config edit`

👉 直接打开配置文件可视化编辑，无需找路径、不用敲路径命令

- `hermes debug`

👉 一键打包日志、系统环境、链路报错，快速上报排查疑难故障

🔹 网关服务｜后台常驻消息推送

- `hermes gateway start / stop / restart`

👉 标准后台启停重启三件套，运维值守高频刚需命令

- `hermes gateway run`

👉 前台直接运行网关，适合本地调试、实时看运行日志排错

- `hermes gateway status`

👉 查看网关在线、离线、异常、端口占用、联动链路状态

- `hermes gateway install`

👉 把网关直接注册成系统自启动服务，开机自动后台常驻运行

🔹 会话 & 日志 & 备份｜数据安全兜底

- `hermes sessions` 全量会话管理

✅ 列出全部历史会话 ✅ 导出关键工作会话 ✅ 清理无效冗余会话

- `hermes logs` 查看运行日志

- `hermes logs tail` 实时滚动监控日志，值守盯现场专用

- `hermes backup / import`

👉 整机配置+技能+会话一键备份，换服务器、迁移环境直接一键恢复

🔹 技能市场｜能力按需装卸载

- `hermes skills list / info / search`

👉 查全部技能、看技能详情、关键词检索所需功能技能包

- `hermes skills enable / disable`

👉 秒开秒关指定技能，不用卸载，灵活切换业务可用能力

- `hermes skills install / config`

👉 在线安装第三方技能，单独精细化配置专属技能参数

03

高级运维｜开发者专属能力

![](assets/img_801be45f4037.gif)

![](assets/img_03f15eb192fd.gif)

- `hermes honcho` 管理跨会话长期记忆，多轮长任务上下文不丢失

- `hermes memory` 对接外部向量库、记忆库，拓展长效存储能力

- `hermes mcp / plugins` 自定义插件扩展、私有协议服务对接

- `hermes dashboard` 一键拉起Web可视化后台面板，图形化管控全服务

- `hermes update / uninstall` 在线安全升级版本、干净卸载不留残留配置

04

迁移专用｜从 OpenClaw 无缝迁过来

![](assets/img_801be45f4037.gif)

![](assets/img_03f15eb192fd.gif)

- `hermes claw migrate` 一键全量迁移旧环境配置、会话、自定义技能

- `hermes claw migrate --dry-run` 先模拟预览迁移，不改动原数据，安全无风险

- `hermes claw cleanup` 迁移完成后，一键清理旧环境冗余垃圾文件

05

聊天框内直接用｜会话快捷指令

![](assets/img_801be45f4037.gif)

![](assets/img_03f15eb192fd.gif)

不用切终端，对话窗口直接输入，高效省时间：

- `/model` 查看当前会话正在使用的模型版本

- `/model 模型名` 临时切换本轮对话专属模型，即时生效

06

一键安装 + 快速上手三步

![](assets/img_801be45f4037.gif)

![](assets/img_03f15eb192fd.gif)

🔹 一键安装脚本（直接复制执行）

```
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

🔹 装机后必跑三步

1. `hermes setup` 初始化全环境
2. `hermes model` 绑定专属大模型接口
3. `hermes chat` 直接开工使用

07

常用路径 & 技能分类速查

![](assets/img_801be45f4037.gif)

![](assets/img_03f15eb192fd.gif)

📁 核心配置路径

- 主配置：`~/.hermes/config.yaml`

- 环境变量：`~/.hermes/.env`
