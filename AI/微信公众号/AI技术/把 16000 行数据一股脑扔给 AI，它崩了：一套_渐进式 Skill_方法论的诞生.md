> 📎 来源: [前端C罗](https://mp.weixin.qq.com/s?__biz=MzkxNDMwMzUzNQ==&mid=2247483842&idx=1&sn=548b0780d13fc684708e19cdeae29d8a&chksm=c049ff19b2c254d3ed048dc9c392428165967e7c8670a768214816238d14898b5831d5371d69&mpshare=1&scene=1&srcid=0429t1xMa3VQ8lTY1mGc2KX5&sharer_shareinfo=11b17925245bc4bfe73c3a4e66b17b0a&sharer_shareinfo_first=11b17925245bc4bfe73c3a4e66b17b0a) | 时间: 2026-04-29 11:28

---

> **项目背景**：将 Figma 设计系统中的 54 个组件，逐一与 React 组件库的 Props 进行双向属性映射，生成结构化的 JSON 映射文件，为 Design↔Code 自动化流水线提供机器可消费的桥接数据。

> **核心叙事**：这篇文章不仅记录"做了什么"，更要回答"为什么这样做"。当我们首次尝试让 AI 一次性处理 54 个组件、2632 个节点、16000 行 JSON 数据时，遭遇了一系列深层问题。正是对这些问题的反思，催生了**基于 Skill 的渐进式处理方法论**——一种将大规模 AI 任务拆解为可控、可恢复、可累积的工程方法。

---

## 一、项目概述

### 1.1 解决什么问题

在设计与开发协作中，Figma 组件与 React 组件之间存在天然的"语义鸿沟"：

- **属性命名不同**：Figma 使用 

  ```
  theme 主题
  ```

  ，React 可能使用 

  ```
  type
  ```

   或 

  ```
  theme
  ```
- **属性类型不同**：Figma 用 VARIANT 枚举表达选中状态 

  ```
  "true"/"false"
  ```

  ，React 用布尔 

  ```
  value={true}
  ```
- **交互表达不同**：Figma 用 

  ```
  state
  ```

   VARIANT 统一表示 default/hover/active/disabled，React 将 

  ```
  disabled
  ```

   拆为独立 prop，hover/active 则交给 CSS 伪类
- **功能覆盖范围不对称**：React 有 

  ```
  onClick
  ```

  、

  ```
  onChange
  ```

   等回调 prop，Figma 没有交互行为概念；Figma 有嵌套实例开关，React 通过 

  ```
  children
  ```

   组合

本项目的目标是：**为每个组件生成一份结构化的 JSON 映射表**，精确记录 Figma 属性与 React Props 之间的对应关系、值映射规则和无法映射的属性清单，从而让 AI 或工具链能自动完成"设计稿 → 代码"和"代码 → 设计稿"的双向转换。

### 1.2 数据来源

| 来源 | 说明 |
| --- | --- |
| **Figma 端** | `docs/uikit-data.json` — 通过 Figma 插件导出的 TEA UI KIT 2.8 版完整数据，包含 29 个 COMPONENT + 73 个 COMPONENT\_SET，共计 2632 个组件节点、2248 个变体 |
| **React 端** | `tea2/tea-component/src/` — tea-component React 组件库源码，涵盖所有组件的 Props 接口定义（TypeScript） |
| **解析脚本** | `parse-uikit.js` — 预处理脚本，从 uikit-data.json 中提取组件名称和属性列表 |

### 1.3 产出规模

- **映射文件**：54 个 JSON 文件，存放于 

  ```
  .codebuddy/mappings/
  ```

   目录
- **进度追踪**：

  ```
  .codebuddy/mapping-progress.json
  ```

   记录全部 54 个组件的完成状态
- **覆盖组件**：从基础控件（Button、Input、Checkbox）到复合组件（Modal、Drawer、Table），再到业务组件（TagSearchBox、Transfer、NavMenu）

---

## 二、从"暴力投喂"到渐进式处理：问题的发现与方法论的演进

在介绍最终的映射方法论之前，有必要先回溯这套方法是如何"被逼出来的"。这段经历揭示了一个更深层的命题：**当 AI 面对大规模结构化数据处理任务时，传统的"一次性喂入全量数据"思路为何会失败，以及如何设计更优的人机协作范式。**

### 2.1 天真的起点："把数据全扔给 AI"

项目启动时，最直觉的做法是：

```
ounter(lineounter(lineounter(line
```

这种"暴力投喂"方式看似高效，实际上立即暴露了一系列根本性问题：

#### 问题一：上下文窗口溢出

```
uikit-data.json
```

 单文件就有 16000 行、约 50 万 token。加上 54 个组件的 React 源码，总数据量远超任何 AI 模型的上下文窗口。即使模型声称支持 128K 或 200K token 的上下文，**全量灌入也会导致：**

- **关键信息被稀释**：模型的注意力在海量数据中被分散，前面读到的组件属性在处理后面组件时已经"遗忘"
- **回答质量断崖式下降**：头几个组件映射质量尚可，越往后越出现属性遗漏、映射错乱、张冠李戴
- **无法验证正确性**：输出体量太大，人工审查 54 个 JSON 的成本反而高于手工编写

#### 问题二：错误无法隔离与回溯

一次性处理时，如果第 17 个组件的映射出错了：

- **无法定位问题来源**——是 Figma 数据解析错误，还是 React Props 理解偏差？
- **无法局部修正**——修改一个组件的逻辑可能需要重新生成全部 54 个文件
- **无法增量恢复**——如果中途因网络/token 限制中断，之前所有工作全部丢失

#### 问题三：认知负荷的不可控

54 个组件并非同质的：

- Button 有 13 个 Figma 属性 + 嵌套实例
- Badge 只有 3 个属性
- Alert 包含三层嵌套实例（

  ```
  after → close/carousel/do not notify/actions
  ```

  ）
- Table 需要跨越两个 Figma COMPONENT\_SET 合并映射

一次性处理时，模型必须同时记住所有这些差异化的映射规则，认知负荷远超单次推理的合理范围。结果就是**简单组件被过度处理，复杂组件被草率带过**。

#### 问题四：输出格式的漂移

这是最隐蔽但也最致命的问题。当模型一次性生成大量 JSON 时：

- 前 5 个文件严格遵循 schema（有 

  ```
  figmaRole
  ```

  、

  ```
  associatedToggleProp
  ```

  、

  ```
  behaviorMapping
  ```

  ）
- 第 10 个开始，字段命名出现不一致（

  ```
  reactMapping
  ```

   有时变成 

  ```
  mapping
  ```

  ）
- 第 20 个以后，

  ```
  figmaDesignPatterns
  ```

   部分开始被省略
- 到最后几个，连 

  ```
  unmappedReactProps
  ```

   都不再列出

**Schema 漂移**意味着下游的代码生成工具无法统一消费这些 JSON，整个流水线的可靠性被瓦解。

### 2.2 反思：AI 任务工程的三个认知

上述失败迫使我们重新思考"AI 处理大规模数据"这件事本身：

> **认知一：AI 的上下文窗口不是"无限内存"，而是"工作台"。**

> 工作台面积有限，同时摊开 54 份图纸必然导致每份图纸只能看到一角。正确的做法是：每次只摊开一份，专注完成后收起来，再摊开下一份。

> **认知二：AI 任务的可靠性与批处理粒度成反比。**

> 批量越大，单次输出中包含的决策越多，出错概率指数级增长。而错误的定位和修复成本也随之指数级增长。"小批量、高频次"才是可控的工程节奏。

> **认知三：AI 需要"外部脚手架"来维持长链任务的一致性。**

> 人类程序员在处理重复性任务时，依赖 IDE 模板、代码片段、linter 规则来保持一致性。AI 同样需要等价的外部机制——这就是 **Skill** 的角色。

### 2.3 解决方案的诞生：Skill 驱动的渐进式处理

基于上述反思，我们设计了 

```
uikit-tea-mapper
```

 Skill——一个结构化的"AI 工作指南"，将原本混沌的"一次性大任务"重构为**可控、可恢复、可验证的渐进式流水线**。

Skill 的核心设计理念可以用一句话概括：

> **"把人类工程师的经验编码为 AI 可执行的标准作业程序（SOP），每次只处理最小有意义的单元，通过外部状态文件维持跨次调用的连续性。"**

具体而言，Skill 解决了前述四个问题：

| 问题 | Skill 的解决方案 |
| --- | --- |
| 上下文溢出 | **信息裁剪原则** ：永远不读取 `uikit-data.json` 全文，只用 `search_content` 按组件名定向抽取 ~120 行相关数据；React 侧只读主 `.tsx` 文件 |
| 错误不可隔离 | **逐组件处理** ：每次只处理一个组件的完整流水线（采集 → 比对 → 写 JSON→ 更新进度），错误被限制在单个组件的作用域内 |
| 认知负荷不可控 | **三种设计模式的预编码** ：在 Skill 中预先定义了"独立属性"、"开关-内容配对"、"嵌套实例开关"三种模式的标准处理模板，AI 不需要每次重新"发现"这些模式 |
| 输出格式漂移 | **强制 Schema 约束** ：Skill 中内嵌了完整的输出 JSON 结构定义 + 每种设计模式的参考示例（`references/example-mapping-alert.json`），每个组件的输出都被同一个模板约束 |

### 2.4 Skill 的三层架构

最终实现的 

```
uikit-tea-mapper
```

 Skill 由三层组成：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line
```

**第一层 SOP** 是核心——它不是笼统的"请映射这些组件"，而是精确到操作粒度的步骤指令：

- Step 1：读进度文件 → 找到第一个 

  ```
  mapped: false
  ```

   的组件
- Step 2：用 

  ```
  search_content
  ```

   在 uikit-data.json 中搜索该组件（限 120 行上下文）
- Step 3：在 

  ```
  tea2/tea-component/src//
  ```

   读取 Props 接口
- Step 4：按三种模式建立映射
- Step 5：写入 JSON + 更新进度
- Step 6：**自动继续**处理下一个，无需人工干预

**第二层参考样本** 是"活模板"——AI 在生成每个组件映射时，可以参照 

```
example-mapping-alert.json
```

 的实际格式，确保输出结构严格一致。这相当于为 AI 提供了一份"标准答案的样子"。

**第三层可执行工具** 为后续扩展预留了空间——例如可以加入自动化的 JSON schema 验证脚本、映射覆盖率检测脚本等。

### 2.5 渐进式处理的"飞轮效应"

Skill 驱动的渐进式处理不仅仅是"分批做"那么简单。它产生了一种**飞轮效应**：

```
┌─────────────────────┐
```

具体例子：

1. **批次 1** 处理 Button 时，发现了 

   ```
   ↪
   ```

    前缀的"开关-内容配对"模式 → 编码进 Skill 的 Step 4 模式 B
2. **批次 2** 处理 Alert 时，发现了"嵌套实例开关"模式（after 后缀含 4 个子开关）→ 编码进 Skill 的 Step 4 模式 C + 创建 

   ```
   references/example-mapping-alert.json
   ```
3. **批次 3** 处理 Modal 时，这两种模式已经被 Skill "内化"，AI 无需重新推理即可正确处理

这种"在做中学、在学中编码、编码后复用"的循环，是"暴力投喂"方式无法实现的——因为一次性处理时没有"中间修正"的机会。

### 2.6 进度持久化：让中断不再意味着从零开始

Skill 设计中另一个关键机制是 **```
.codebuddy/mapping-progress.json
```**——一个简单但至关重要的状态文件：

```
[
```

这个文件的价值在于：

- **抗中断**：会话断开后，下次加载 Skill 会自动读取进度，从上次停下的地方继续
- **可审计**：随时可以看到哪些组件已完成、哪些待处理
- **可回滚**：如果某个组件映射质量不佳，只需将其 

  ```
  mapped
  ```

   改回 

  ```
  false
  ```

  ，Skill 会自动重新处理

在实际执行中，由于网络波动和 token 限额，整个任务经历了多次中断。如果没有这个进度文件，每次中断都意味着要重新检查哪些组件已完成——在 54 个组件的规模下，这本身就是一项繁琐且易出错的工作。

### 2.7 对比：两种范式的效果差异

| 维度 | 暴力投喂（一次性处理） | Skill 渐进式处理 |
| --- | --- | --- |
| **上下文占用** | ~50 万 token（全量数据） | ~2000 token/组件（定向抽取） |
| **单组件映射质量** | 前 5 个尚可，后面迅速退化 | 54 个组件质量均匀一致 |
| **Schema 一致性** | 严重漂移 | 100% 一致（由参考样本约束） |
| **错误可追溯性** | 无法定位（"大泥球"输出） | 精确到单个组件（隔离的 JSON 文件） |
| **中断恢复** | 从零开始 | 从断点精确恢复 |
| **处理时间** | 理论快但实际因重做更慢 | 7 个批次、稳步推进 |
| **知识积累** | 无（一次性消耗） | 持续积累（Skill 迭代增强） |

---

## 三、映射方法论（Skill 最终形态）

### 3.1 整体工作流

Skill 定义的标准作业程序（SOP）包含 6 个步骤，每个组件严格按序执行：

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
```

**关键设计决策**：

1. **信息裁剪**：永远不读取 

   ```
   uikit-data.json
   ```

    全文（16000 行），只通过 

   ```
   search_content
   ```

    按组件名搜索，提取 ~120 行上下文。这将单组件的 Figma 数据输入从 ~50 万 token 降至 ~500 token
2. **最小读取原则**：React 侧只读主组件的 

   ```
   .tsx
   ```

    文件中的 Props 接口定义，不读 demo/test/example 文件
3. **模式匹配优先**：先识别属性所属的设计模式（独立/配对/嵌套），再按模式模板填充映射
4. **自动继续机制**：一个组件完成后立即开始下一个，无需人工干预——这使得 Skill 启动后可以"无人值守"地连续处理

### 3.2 映射 JSON 的标准结构

每个映射文件遵循统一 schema：

```
{
```

---

## 四、映射中的深层挑战：源数据不够用，领域知识必须按需注入

前面三章讲了"怎么做"（方法论），这一章要回答一个更本质的问题：**为什么仅凭 

```
uikit-data.json
```

 + React 源码这两份"源数据"，AI 依然无法独立完成高质量映射？**

答案是：**源数据只描述了"有什么"，但没有告诉 AI "这意味着什么"。** Figma 属性系统有自己的设计范式和隐含约定，React 有自己的前端工程惯例，两者之间的"翻译规则"既不在 Figma 数据里，也不在 React 源码里——它们存在于设计师和前端工程师的**领域知识**中。

这一认识直接影响了 Skill 的设计：除了 SOP（告诉 AI 怎么做）和 Progress（记住做到哪了），还需要 **References（按需注入源数据之外的领域知识）**。

下面按"知识缺口"的类型逐一展开。

### 4.1 知识缺口一：Figma 设计模式的隐含约定

Figma 组件属性体系存在三种反复出现的设计模式，它们是正确映射的前提——但这些模式**在数据中没有任何显式标注**，必须由"懂 Figma 设计系统的人"告诉 AI。

#### 模式 A：独立属性（Independent）

最简单的模式——Figma 属性与 React Prop 存在直接的一对一对应关系：

```
Figma: variant 变体 (VARIANT) = solid | outlined | plain | link
```

看似简单，但即便是这种模式也暗藏需要额外知识才能处理的细微差异：

- **默认值不一致**：Button 的 

  ```
  theme
  ```

  ，Figma 默认 

  ```
  brand
  ```

  ，React 默认 

  ```
  neutral
  ```

  ——数据只告诉你各自的默认值是什么，但"这两个默认值对应同一个视觉效果吗"需要设计知识来判断
- **值命名不一致**：Tag 的 

  ```
  theme
  ```

  ，Figma 用 

  ```
  brand
  ```

  ，React 用 

  ```
  primary
  ```

  ——数据无法告诉你它们是"同一概念的不同名字"还是"完全不同的概念"
- **Figma 值带人类可读注释**：Drawer 的 

  ```
  size
  ```

  ，Figma 值为 

  ```
  m (default)
  ```

   对应 React 的 

  ```
  m
  ```

  ——需要知道 

  ```
  (default)
  ```

   是注释而非值的一部分

**注入方式**：在 Skill 的 SOP Step 4 中预先描述"模式 A"的处理规则，AI 遇到每个 VARIANT 属性时按规则走，不需要自己猜测。

#### 模式 B：开关-内容配对（Toggle-Content Pair）

这是 Figma 设计系统中**最具特色但也最容易被 AI 误解**的模式。一个 **BOOLEAN 属性**控制某区域是否显示，一个**关联的 TEXT 或 INSTANCE\_SWAP 属性**提供该区域的内容。关联属性以 

```
↪
```

 前缀命名。

```
Figma:
```

**这里的知识缺口极其明显**：

- ```
  ↪
  ```

   是什么意思？——这是 Figma 对"关联文本属性"的**命名约定**，uikit-data.json 中没有任何字段解释这个符号的语义
- ```
  label 文本
  ```

  （BOOLEAN）和 

  ```
  ↪label 文本
  ```

  （TEXT）之间是什么关系？——数据中它们只是两个平级的属性，没有任何 

  ```
  parent/child
  ```

   或 

  ```
  controls
  ```

   字段将它们关联起来
- 开关关闭时内容属性是否还生效？——数据中不会告诉你"当 

  ```
  label 文本
  ```

   = false 时，

  ```
  ↪label 文本
  ```

   的值会被忽略"

如果不预先注入这些知识，AI 会把 

```
label 文本
```

 和 

```
↪label 文本
```

 当作两个独立的属性分别映射——这在 54 个组件中会产生大量错误，因为这种模式**高频出现**：

- ```
  title 标题
  ```

   + 

  ```
  ↪title 标题
  ```

  （Alert、Drawer 等）
- ```
  subtitle 副标题
  ```

   + 

  ```
  ↪subtitle 副标题
  ```

  （Drawer）
- ```
  text 文本
  ```

   + 

  ```
  ↪text 文本
  ```

  （Input）
- ```
  beforeIcon 前缀
  ```

   + 

  ```
  ↪before icon 前缀图标
  ```

  （Tag，INSTANCE\_SWAP 变体）

**注入方式**：在 Skill 的 

```
references/figma-property-types.md
```

 中显式解释了 

```
↪
```

 前缀的语义约定；在 SOP Step 4 模式 B 中定义了**识别规则**（"当看到 

```
↪
```

 前缀的 TEXT 属性时，查找同名的 BOOLEAN 属性作为其开关"）和**输出格式**（

```
figmaRole: "toggle"/"content"
```

 + 

```
associatedToggleProp/associatedTextProp
```

 双向引用）。

#### 模式 C：嵌套实例开关（Nested Instance Toggle）

一个 **BOOLEAN 属性**控制是否渲染某个**嵌套的子组件实例**，该嵌套实例拥有自己独立的属性面板：

```
Figma:
```

**知识缺口**：数据中虽然有 

```
controlsNestedInstance: true
```

 和 

```
nestedInstanceInfo
```

 字段，但 AI 需要知道：

- 嵌套实例的子属性**仅在父开关为 true 时才生效**（这个语义不在数据中）
- 嵌套实例可能对应 React 的**完全不同的组件**（如 Button 中的 Tag 嵌套实例对应独立的 

  ```

  ```

   组件），而非同一组件的某个 prop

更复杂的案例如 Alert 的 

```
after 后缀
```

，其嵌套实例内含四个独立子开关，分别映射到 React 的**不同 Props**：

| 嵌套子属性 | React 映射 | 所需领域知识 |
| --- | --- | --- |
| `close 关闭按钮` | `visible/defaultVisible + onClose` | 需知道 React Alert 用 `visible` 控制关闭按钮显隐 |
| `carousel 翻页` | `carouselMode` | 需知道 React Alert 支持轮播模式 |
| `do not notify 不再提示` | ❌ React 无内置支持 | 需知道这是 Figma 独有的设计概念 |
| `actions 后缀按钮` | `extra` | 需知道 React Alert 用 `extra` 承载后缀自定义内容 |

这张映射表中的每一行都依赖**对 React Alert API 的了解**——而这不在 Figma 数据中。

**注入方式**：在 Skill 的 

```
references/example-mapping-alert.json
```

 中提供了 Alert 组件的完整映射示例（218 行），覆盖了全部三种模式。AI 处理其他组件时可以参照这个"标杆样本"的深度和格式。

### 4.2 知识缺口二：跨域概念的"翻译规则"

Figma 和 React 虽然描述同一套 UI，但它们的**概念模型完全不同**。很多映射困难不是因为"找不到对应属性"，而是因为**同一个概念在两端的表达方式根本不同**，需要知道"翻译规则"。

#### `state` VARIANT：一个 Figma 属性 → 拆分到四个 React 层面

几乎所有交互组件在 Figma 中都用单一的 

```
state
```

 VARIANT 统一表达所有交互状态：

```
Figma state: default | hover | focus | active | disabled | readonly | error
```

但在 React 中，这些状态分散在完全不同的技术层面：

| Figma 的 state 值 | React 的实现层面 | 需要注入的知识 |
| --- | --- | --- |
| `disabled` | `disabled={true}` prop | React 用独立 boolean prop 控制 |
| `readonly` | `readonly={true}` prop | 同上 |
| `hover` / `active` / `focus` | CSS 伪类 `:hover``:active``:focus` | **这些状态在 React Props 中不存在** ，是浏览器原生行为 |
| `error` | 外层 `Form.Item` 的 `status="error"` | 不是组件自身的 prop，是**父组件的状态传递** |

这里的关键洞察是：**如果 AI 不知道"hover/active/focus 在 React 中是 CSS 伪类而非 Props"，它会尝试寻找一个不存在的 

```
hover
```

 prop，要么报告"映射缺失"，要么胡乱关联到某个无关的 prop。** 这是典型的"源数据没有告诉你该找什么不该找什么"的问题。

**注入方式**：在 Skill 的 

```
references/figma-property-types.md
```

 末尾专门说明了 

```
state 状态
```

 的拆分规则——"In React these are usually handled via: 

```
disabled
```

 boolean prop for the disabled state; CSS pseudo-classes for hover/active/focus (not props)"。

#### INSTANCE\_SWAP：Figma 实例 ID → React 图标名称

Figma 的图标选择使用 

```
INSTANCE_SWAP
```

 属性，值是 Figma 内部的组件实例 ID（如 

```
70703:3084
```

）。React 组件通常接受字符串图标名称或 

```
React.ReactNode
```

。

```
Figma: ↪icon 图标 (INSTANCE_SWAP) = "70703:3084"
```

**知识缺口**：

- ```
  70703:3084
  ```

   是 Figma 的节点 ID，在 React 世界中无任何意义
- 将其转换为图标名称需要查阅 

  ```
  uikit-data.json
  ```

   中的 icon 组件集（包含 306 个图标定义），这是一个**二次查表**过程
- 更根本的是，AI 需要知道"INSTANCE\_SWAP 的值不能直接使用，必须经过转换"

**注入方式**：在 

```
references/figma-property-types.md
```

 的 INSTANCE\_SWAP 节中说明了这种属性的语义——"Map to a React prop that accepts 

```
ReactNode
```

 or a specific icon/component name string"。

### 4.3 知识缺口三：不在数据中的"不存在"

最隐蔽的知识缺口是关于\*\*"什么不存在"\*\*——数据只告诉你"有什么"，不会告诉你"没什么"。

#### React 独有属性：为什么找不到对应？

每个组件都有一批 React Props 在 Figma 中找不到对应。AI 如果不了解原因，会浪费大量推理资源去"强行匹配"：

| 类别 | 代表属性 | 为什么在 Figma 中不存在（需要注入的知识） |
| --- | --- | --- |
| **事件回调** | `onClick` , `onChange`, `onClose` | Figma 是**静态设计工具**，没有交互行为的概念 |
| **受控/非受控** | `value` , `defaultValue` | Figma 不区分 React 的**受控组件模式** |
| **可见性控制** | `visible` , `defaultVisible` | Figma 通过**放置/删除**组件实例控制显隐，不需要 prop |
| **通用样式** | `className` , `style` | 是 `StyledProps` 基类继承的**编程接口**，设计层面无此概念 |
| **原生 HTML 属性** | `htmlType` , `name`, `type` | 是**浏览器原生**概念，设计工具不涉及 |
| **运行时行为** | `loading` , `scrollable`, `disableEscape` | 涉及**时间和动态行为**，静态设计无法体现 |
| **动画/过渡** | `onExited` , `interval` | 是**时间维度**的属性 |

这些属性必须被系统性地归入 

```
unmappedReactProps
```

 并标注原因——而"原因"本身就是领域知识。

**注入方式**：在 Skill SOP 的"通用规则"中预先指定——"If a React prop has no Figma counterpart, add it to the 

```
unmappedReactProps
```

 array"。更重要的是，通过参考样本 

```
example-mapping-alert.json
```

 展示了 

```
unmappedReactProps
```

 的标准写法（包括 

```
reason
```

 字段），AI 可以照此格式输出。

#### 组件粒度不对齐：两端的"单位"不一样

部分组件在 Figma 和 React 中的粒度划分不一致——这种"不一致"在任何一端的数据中都看不出来，只有**同时了解两端**的人才能发现：

| 组件 | Figma 的拆分方式 | React 的组织方式 | 需要注入的知识 |
| --- | --- | --- | --- |
| **Table** | `Table header cell` + `Table body cell`（两个独立 COMPONENT\_SET） | 统一的 `    ` + `columns` 配置 | 两个 Figma 组件要合并映射到一个 React 组件 |
| **ButtonGroup** | 「强关联按钮组」+「弱关联按钮组」 | `ButtonGroup` （from `button`）+ `ButtonBar`（from `buttonbar`） | 两个 Figma 组件分别映射到两个**不同目录**下的 React 组件 |
| **Form** | `Form label` + `Form item` | 统一的 `` | 两个 Figma 组件合并映射到一个 React 子组件 |
| **Menu** | `Menu item` + `Menu title` | `` + `` | 对应关系非显然（`title` ≠ `Group`） |

**注入方式**：在 Skill SOP 的末尾提供了"组件名称规范化表"（Component Name Normalization），将 Figma 组件名与 React 的 

```
src/
```

 目录名建立显式对应关系——这张表正是"源数据之外"的手动编写的领域知识。

### 4.4 Skill 的 References 层：领域知识的"按需加载"

回顾上述四类知识缺口，可以发现一个共同特征：**它们都是"人类专家脑子里的隐性知识"，既不在 Figma 数据中，也不在 React 源码中。**

Skill 的 

```
references/
```

 层正是为解决这个问题而设计的：

```
references/
```

这个设计体现了一个重要原则：

> **领域知识不应该"一股脑"全部灌给 AI，而应该被结构化地组织，在 AI 执行到相应步骤时"按需加载"。**

- AI 在 Step 2（采集 Figma 属性）时，遇到不认识的属性类型 → 查阅 

  ```
  figma-property-types.md
  ```
- AI 在 Step 4（建立映射）时，不确定输出格式 → 参照 

  ```
  example-mapping-alert.json
  ```
- AI 在处理 

  ```
  state
  ```

   VARIANT 时，不知道 hover 是否对应 React prop → 查阅 

  ```
  figma-property-types.md
  ```

   末尾的说明

这种"按需注入"比"全量灌入"高效得多——前者精准提供当前步骤所需的知识（~100 行），后者把所有可能用到的知识堆在一起（数千行），反而增加了 AI 的认知负荷。

### 4.5 小结：三层知识模型

将本章的分析汇总，一个完整的 AI 映射任务需要三层知识：

```
┌─────────────────────────────────────────────────────────┐
```

只有三层齐备，AI 才能在 54 个组件上输出均匀一致的高质量映射。缺少任何一层都会导致质量退化——而"暴力投喂"方式的根本缺陷正是**试图用第二层（更多数据）来弥补第一层（无 SOP）和第三层（无领域知识注入）的缺失**。

---

## 五、处理过程全记录

### 5.1 批次推进时间线

整个映射工作分为 **7 个批次**完成，从简单的独立属性组件逐步推进到复杂的嵌套实例组件：

| 批次 | 组件（编号） | 数量 | 特点 |
| --- | --- | --- | --- |
| **Batch 1** | Alert, Badge, BadgeContainer, Bubble, Button, ButtonGroup(强), ButtonGroup(弱), Checkbox, DateSelect, Drawer, Dropdown, InputAdornment, Password, TextArea, Input, InputNumber（1-16） | 16 | 基础控件，覆盖所有三种设计模式 |
| **Batch 2** | List item, Form label, Form item（17-19） | 3 | 列表与表单控件 |
| **Batch 3** | Menu item, Menu title, Message, Modal, Notification（20-24） | 5 | 菜单与反馈类组件 |
| **Batch 4** | Segement Button, Progress, Popconform, Radio（25-28） | 4 | 表单控件与状态展示 |
| **Batch 5** | Searchbox, Select button, Slider, Status, Switch（29-33） | 5 | 输入与选择类组件 |
| **Batch 6** | Table header cell, Table body cell, Tabs Example, Tag, TagSearchBox（34-38） | 5 | 数据展示与导航 |
| **Batch 7** | Pagination, Stepper, TimePicker, Upload, Rate, Avatar, Card, Calendar, Collapse, Autocomplete, MediaObject, Timeline, Tree, Cascader, Transfer, NavMenu（39-54） | 16 | 剩余全部组件，含多个 Example 级别组件 |

### 5.2 并行化策略

每批组件的处理采用最大化并行策略：

```
同时进行:
```

这种并行化策略使得单批 5 个组件的处理只需要 3-4 轮工具调用，而非串行的 15-20 轮。

---

## 六、映射结果统计

### 6.1 全量组件清单

点击展开完整的 54 个组件映射清单

| # | Figma 组件名 | React 组件 | 映射文件 |
| --- | --- | --- | --- |
| 1 | Alert 提示条 | Alert | alert.json |
| 2 | Badge 徽章 | Badge | badge.json |
| 3 | BadgeContainer 徽章容器 | Badge (wrapper) | badgecontainer.json |
| 4 | Bubble 气泡 | Bubble | bubble.json |
| 5 | Button 按钮 | Button | button.json |
| 6 | ButtonGroup 强关联按钮组 | ButtonGroup | buttongroup-strong.json |
| 7 | ButtonGroup 弱关联按钮组 | ButtonBar | buttongroup-weak.json |
| 8 | Checkbox 多选 | Checkbox | checkbox.json |
| 9 | DateSelect 日期选择 | DatePicker | dateselect.json |
| 10 | Drawer 抽屉 | Drawer | drawer.json |
| 11 | Dropdown button | Dropdown | dropdown.json |
| 12 | InputAdornment 输入装饰 | InputAdornment | inputadornment.json |
| 13 | Password 密码 | Input (password) | password.json |
| 14 | TextArea 文本区域 | Input.TextArea | textarea.json |
| 15 | Input 输入 | Input | input.json |
| 16 | InputNumber 数字输入 | InputNumber | inputnumber.json |
| 17 | List item | ListItem | listitem.json |
| 18 | Form label 表单标签栏 | Form.Item (label) | formlabel.json |
| 19 | Form item 表单项 | Form.Item | formitem.json |
| 20 | Menu item | Menu.Item | menuitem.json |
| 21 | Menu title | Menu.Group | menutitle.json |
| 22 | Message 提示 | Message | message.json |
| 23 | Modal 对话框 | Modal | modal.json |
| 24 | Notification 通知 | Notification | notification.json |
| 25 | Segement Button | Segment | segmentbutton.json |
| 26 | Progress 进度 | Progress | progress.json |
| 27 | Popconform 就地确认 | PopConfirm | popconfirm.json |
| 28 | Radio 单选 | Radio | radio.json |
| 29 | Searchbox 搜索 | SearchBox | searchbox.json |
| 30 | Select button | Select | selectbutton.json |
| 31 | Slider 滑块 | Slider | slider.json |
| 32 | Status 状态 | Status | status.json |
| 33 | Switch 开关 | Switch | switch.json |
| 34 | Table header cell | Table (column) | tableheadercell.json |
| 35 | Table body cell | Table (cell) | tablebodycell.json |
| 36 | Tabs Example | Tabs | tabs.json |
| 37 | Tag 标签 | Tag | tag.json |
| 38 | TagSearchBox | TagSearchBox | tagsearchbox.json |
| 39 | Pagination | Pagination | pagination.json |
| 40 | Stepper | Stepper | stepper.json |
| 41 | 时间选择 TimePicker | TimePicker | timepicker.json |
| 42 | 上传 Upload | Upload | upload.json |
| 43 | 评分 Rate | Rate | rate.json |
| 44 | Avatar | Avatar | avatar.json |
| 45 | 卡片 Card | Card | card.json |
| 46 | 日历 Calendar | Calendar | calendar.json |
| 47 | 折叠面板 Collapse | Collapse | collapse.json |
| 48 | 自动补全 autocomplete | AutoComplete | autocomplete.json |
| 49 | 媒体对象 MediaObject | MediaObject | mediaobject.json |
| 50 | 时间轴 Timeline | Timeline | timeline.json |
| 51 | 树形控件 Tree | Tree | tree.json |
| 52 | 级联选择 cascader | Cascader | cascader.json |
| 53 | 穿梭框 Transfer | Transfer | transfer.json |
| 54 | 导航菜单 NavMenu | NavMenu | navmenu.json |

### 6.2 设计模式分布

通过对 54 个映射文件的分析，三种设计模式的出现频率如下：

| 设计模式 | 出现组件数 | 代表组件 |
| --- | --- | --- |
| 独立属性映射 | 54 (全部) | Button.variant, Tag.theme, Modal.size |
| 开关-内容配对 (Toggle-Content Pair) | ~20 | Alert(title), Input(text), Checkbox(label), Drawer(subtitle), Tag(icons) |
| 嵌套实例开关 (Nested Instance Toggle) | ~8 | Alert(footer, after), Button(tag), Form item(嵌套控件) |

### 6.3 映射覆盖率

| 维度 | 说明 |
| --- | --- |
| **Figma 属性覆盖率** | 绝大多数 Figma 属性均找到 React 对应映射。少量无法映射的属性已在 `unmappedFigmaProps` 中记录（如 Alert 的「不再提示」功能） |
| **React Props 覆盖率** | 每个组件的核心视觉 Props 均有 Figma 对应。事件回调（onClick/onChange/onClose 等）、通用样式（className/style）、运行时控制（visible/loading）系统性地归入 `unmappedReactProps` |

---

## 七、产出应用场景

### 7.1 Design → Code（设计稿生成代码）

AI 拿到 Figma 组件实例的属性值后，通过查询映射 JSON：

1. 找到对应的 React 组件名和导入路径
2. 将 Figma 属性值通过 

   ```
   valueMapping
   ```

    转换为 React prop 值
3. 处理开关-内容配对（toggle=false 时跳过关联属性）
4. 生成 JSX 代码

**示例**：Figma Button 

```
{ variant: "solid", theme: "brand", size: "lg", state: "disabled", leftIcon: true }
```

 →

```
import { Button } from "tea-component";
```

### 7.2 Code → Design（代码反向生成设计稿属性）

给定一段 React JSX，反向查找映射表，输出 Figma 组件应设置的属性值，用于设计稿的自动同步或审查。

### 7.3 设计-开发一致性审查

比对 Figma 组件实例的实际属性值与 React 代码中的 prop 值，自动检测不一致之处（如 Figma 用了 

```
brand
```

 主题但代码写了 

```
primary
```

）。

---

## 八、经验总结与方法论反思

### 8.1 关于 AI 能力边界的认识

这个项目最深刻的教训不是关于 Figma 或 React 的——它关于**如何正确使用 AI 处理大规模结构化任务**。

**AI 不是"更快的打字员"。** 让 AI 一次性处理 54 个组件的映射，本质上是把它当作一个"能读更多数据的人工"来使用。但 AI 的推理质量与输入规模之间存在一个**非线性的衰减曲线**：

```
ounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(lineounter(line
```

前 5 个组件的质量接近人工水平，之后急剧下降。这不是模型"不够聪明"——而是**上下文注意力的物理限制**。理解了这一点，才能设计出与 AI 能力模型匹配的工作流。

### 8.2 Skill 模式的可推广性

```
uikit-tea-mapper
```

 Skill 的设计模式可以推广到一类通用问题：**大规模、重复性、需要一致输出的 AI 数据处理任务**。

其核心公式是：

```
Skill = SOP（步骤定义）
```

可预见的应用场景：

- **API 文档生成**：逐个 endpoint 处理，参照样本约束输出格式
- **代码迁移**：逐个文件处理，维护进度文件追踪已迁移/未迁移
- **测试用例生成**：逐个函数处理，参照已有测试约束风格
- **国际化翻译**：逐个 key 处理，参照术语表约束一致性

### 8.3 渐进式思维的本质

回顾整个项目，"渐进式"不仅是一种技术策略，更是一种**与 AI 协作的思维方式**：

1. **不要试图一步到位**——把大任务拆成可验证的小单元
2. **让 AI "边做边学"**——通过 Skill 迭代，前面组件的经验被编码进后面组件的处理逻辑
3. **用外部状态弥补 AI 的"无状态"天性**——进度文件、参考样本、强制 Schema 都是"外部记忆"
4. **错误是正常的，但必须可隔离**——单组件粒度的处理使错误定位和修复成本从 O(n) 降到 O(1)

> **最终结论**：这个项目表面上是 Figma↔React 的属性映射，但它真正解决的问题是："**当 AI 面对超出单次推理能力的任务时，如何通过工程化手段将任务分解为 AI 能力范围内的子问题，并通过外部脚手架保持全局一致性？**"

> 答案是 Skill——一种将人类工程经验编码为 AI 可执行 SOP 的结构化方法。

---

## 写在最后

如果你也在用 AI 处理"量大、重复、要求一致"的工程任务——不管是批量生成文档、迁移代码、还是处理结构化数据——希望这篇文章能帮你少踩一个坑：

**别急着把所有数据一股脑塞进去。**

先花 10 分钟想清楚三件事：

1. **最小处理单元是什么？** —— 能独立完成、独立验证、独立回滚的那个粒度
2. **输出格式怎么锁死？** —— 给 AI 一份"标准答案长什么样"的参考样本，比写 10 段提示词管用
3. **中断了怎么恢复？** —— 一个记录进度的 JSON 文件，能省掉无数次从头再来的痛苦

这三个问题的答案，就是一个最小可用的 Skill。

技术会迭代，模型会升级，但\*\*"把大任务拆成小单元、用外部脚手架保持一致性"\*\*这个思路，大概率会一直有效——因为它解决的不是 AI 的能力问题，而是所有"有限工作记忆"系统的共同瓶颈。
