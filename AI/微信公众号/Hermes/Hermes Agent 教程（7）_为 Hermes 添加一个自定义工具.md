> 📎 来源: [Preface Lab](https://mp.weixin.qq.com/s?__biz=MzE5MTM0NTQ1MA==&mid=2247483928&idx=1&sn=15bf8c6aed1372b88c57ed14f0ec147b&chksm=97ed80580f6403029251f784709f1bdb3cec0bd81c8fe1ed1a2c99f330b1259e59fff8c8b500&mpshare=1&scene=1&srcid=0425o2vFvklQ4COxQZPd8u9S&sharer_shareinfo=03e0cbffbfba3a327d5c4daa92844105&sharer_shareinfo_first=03e0cbffbfba3a327d5c4daa92844105) | 时间: 2026-04-25 19:32

---

# 实践：为 Hermes 添加一个自定义工具

> 本章目标：通过完整实战，掌握为 Hermes 添加新工具的全部流程
> 前置知识：Hermes Agent 教程（3）：工具系统深度解析
> 文档链接：https://github.com/Eva-Dengyh/AI-Fullstack-Notes

---

## 目录

- 1. 本章目标与前置准备
- 2. 工具设计：从需求到 Schema
- 3. 步骤一：创建工具文件
- 4. 步骤二：实现 Handler
- 5. 步骤三：注册到工具系统
- 6. 步骤四：添加到发现列表
- 7. 步骤五：验证工具可用
- 8. 完整代码
- 9. 常见问题与调试
- 10. 举一反三：更多工具示例

---

## 1. 本章目标与前置准备

### 1.1 本章目标

通过为一个真实需求创建完整工具，掌握：

```
✅ 如何设计一个工具的 Schema✅ 如何实现 Handler 的标准模式✅ 如何注册工具到 Hermes✅ 如何验证工具正常工作
```

### 1.2 我们要做的工具

**```
currency_convert
```

 工具**：货币转换

```
输入：amount（金额）、from_currency（源货币）、to_currency（目标货币）输出：转换后的金额、汇率、转换时间示例：  用户：100 美元换成人民币是多少？  工具调用：currency_convert(amount=100, from_currency="USD", to_currency="CNY")  返回：{"success": true, "amount": 725.50, "rate": 7.255, "from": "USD", "to": "CNY"}  Hermes 回复："100 美元 = 725.50 人民币（汇率 1:7.255）"
```

### 1.3 前置准备

确保你的 Hermes 环境可以正常运行：

```
cd ~/code/hermes-agentsource .venv/bin/activatepython -c "from tools.registry import registry; print('Registry OK')"
```

---

## 2. 工具设计：从需求到 Schema

### 2.1 第一步：明确工具职责

**工具名称：**

```
currency_convert
```

**工具做什么：** 根据实时汇率，将一种货币转换为另一种货币

**工具不做什么（边界）：**

- ❌ 不做历史汇率查询
- ❌ 不做多货币同时转换（单次只支持两种货币）
- ❌ 不支持加密货币（因为免费 API 不支持）

### 2.2 第二步：设计 Schema

Schema 是给 AI 模型看的"使用说明书"：

```
CURRENCY_CONVERT_SCHEMA = {    "name": "currency_convert",    "description": (        "Convert an amount from one currency to another using real-time exchange rates.\n\n"        "Use when: user asks about currency conversion, exchange rates, "        "how much is X in Y currency, etc.\n\n"        "Source: ExchangeRate-API (free tier, no API key required for basic use).\n\n"        "Supported currencies: USD, EUR, GBP, CNY, JPY, KRW, AUD, CAD, CHF, INR, ..."    ),    "parameters": {        "type": "object",        "properties": {            "amount": {                "type": "number",                "description": (                    "The amount of money to convert. "                    "Example: 100, 50.5, 1000"                )            },            "from_currency": {                "type": "string",                "description": (                    "Source currency code (3-letter ISO 4217). "                    "Examples: USD, EUR, GBP, CNY, JPY, KRW, AUD, CAD"                )            },            "to_currency": {                "type": "string",                "description": (                    "Target currency code (3-letter ISO 4217). "                    "Examples: USD, EUR, GBP, CNY, JPY, KRW, AUD, CAD"                )            }        },        "required": ["amount", "from_currency", "to_currency"]    }}
```

### 2.3 设计注意事项

**Schema 描述要包含：**

- 工具在**什么场景**下使用（"当用户问货币转换时"）
- 工具**接受什么参数**（参数名、类型、含义）
- 工具**返回什么**（让 AI 模型知道怎么解释结果）
- **限制条件**（不支持什么，防止 AI 滥用）

**Schema 描述不要包含：**

- 内部实现细节（AI 不需要知道）
- 错误处理的具体逻辑（由 Handler 负责）

---

## 3. 步骤一：创建工具文件

### 3.1 文件命名规范

```
tools/├── currency_convert_tool.py  ← 工具文件名└── ...
```

**命名规范：**

- 用下划线连接小写字母
- 以 

  ```
  _tool.py
  ```

   结尾
- 与工具名对应（

  ```
  currency_convert
  ```

   → 

  ```
  currency_convert_tool.py
  ```

  ）

### 3.2 文件结构模板

每个工具文件遵循统一结构：

```
#!/usr/bin/env python3"""[工具名称] Tool Module[简短描述工具功能]Usage:    [如果用户想直接调用，怎么用]"""import jsonimport urllib.requestfrom typing import Dict, Any# ============================================================# Schema：给 AI 模型看的说明书# ============================================================CURRENCY_CONVERT_SCHEMA = {    # ...（见上一节）}# ============================================================# 可用性检查# ============================================================def check_currency_convert_requirements() -> bool:    """货币转换工具始终可用（使用免费公开 API）"""    return True# ============================================================# Handler：真正做事的函数# ============================================================def currency_convert_handler(args: dict, **kwargs) -> str:    """    将一种货币转换为另一种货币。        Args:        args: 包含 amount, from_currency, to_currency        **kwargs: task_id 等额外参数        Returns:        JSON 字符串    """    pass  # 下一节实现# ============================================================# 注册到全局注册表# ============================================================from tools.registry import registryregistry.register(    name="currency_convert",    toolset="web",  # 货币转换依赖网络，放在 web 工具集    schema=CURRENCY_CONVERT_SCHEMA,    handler=lambda args, **kw: currency_convert_handler(args, **kw),    check_fn=check_currency_convert_requirements,    emoji="💱",)
```

---

## 4. 步骤二：实现 Handler

### 4.1 Handler 标准签名

```
def my_handler(args: dict, **kwargs) -> str:    """    Args:        args: 工具调用时传递的参数（字典）            - 由 AI 模型根据 Schema 推断生成            - 类型已经在 Schema 中声明                    **kwargs: 框架注入的额外上下文            - task_id: str      # 用于工具内部的状态隔离            - session_id: str   # 会话 ID            - tool_call_id: str # 工具调用 ID（用于日志追踪）        Returns:        str: JSON 字符串（必须是字符串！）    """
```

### 4.2 完整的 currency\_convert\_handler

```
def currency_convert_handler(args: dict, **kwargs) -> str:    """    货币转换 Handler。    """        # ========== 第1步：解析参数 ==========    amount = args.get("amount")    from_currency = args.get("from_currency", "").upper().strip()    to_currency = args.get("to_currency", "").upper().strip()        # 参数验证    if amount is None or amount == "":        return json.dumps({"error": "Amount is required"})        try:        amount = float(amount)        if amount < 0:            return json.dumps({"error": "Amount must be positive"})    except (ValueError, TypeError):        return json.dumps({"error": f"Invalid amount: {amount}"})        if not from_currency:        return json.dumps({"error": "from_currency is required"})        if not to_currency:        return json.dumps({"error": "to_currency is required"})        # ========== 第2步：调用外部 API ==========    try:        # 使用 exchangerate-api.com 的免费 API        # 不需要 API key（免费额度足够日常使用）        url = f"https://open.er-api.com/v6/latest/{from_currency}"                req = urllib.request.Request(            url,            headers={"User-Agent": "Hermes-Agent/1.0"}        )                with urllib.request.urlopen(req, timeout=10) as response:            data = json.loads(response.read().decode("utf-8"))                # 检查 API 返回状态        if data.get("result") != "success":            return json.dumps({                "error": "Exchange rate API returned an error"            })                rates = data.get("rates", {})        rate = rates.get(to_currency)                if rate is None:            return json.dumps({                "error": f"Currency '{to_currency}' not supported"            })                # ========== 第3步：计算结果 ==========        converted_amount = round(amount * rate, 2)                # ========== 第4步：返回 JSON 字符串 ==========        return json.dumps({            "success": True,            "from": from_currency,            "to": to_currency,            "amount": amount,            "converted_amount": converted_amount,            "rate": rate,            "time": data.get("time", ""),        })        except urllib.error.URLError as e:        return json.dumps({            "error": f"Network error: could not fetch exchange rate. "                     f"Please check your internet connection."        })    except Exception as e:        return json.dumps({            "error": f"Failed to convert currency: {str(e)}"        })
```

### 4.3 Handler 的三个必须部分

```
def handler(args, **kwargs) -> str:        # 1. 参数解析和验证    #    - 检查必填参数    #    - 类型转换（字符串 → 数字等）    #    - 非法参数返回错误 JSON    params = parse_and_validate(args)        # 2. 实际业务逻辑    #    - 调用外部 API / 读写文件 / 执行命令    #    - 各种异常处理    result = do_the_work(params)        # 3. 返回 JSON 字符串    #    - 必须是字符串！    #    - 成功：包含结果数据    #    - 失败：包含错误信息    return json.dumps(result)
```

---

## 5. 步骤三：注册到工具系统

### 5.1 注册代码

在文件末尾（所有函数定义之后）添加：

```
# tools/currency_convert_tool.py 末尾from tools.registry import registryregistry.register(    name="currency_convert",    toolset="web",  # 货币转换放在 web 工具集（依赖网络）    schema=CURRENCY_CONVERT_SCHEMA,    handler=lambda args, **kw: currency_convert_handler(args, **kw),    check_fn=check_currency_convert_requirements,    emoji="💱",)
```

### 5.2 注册参数详解

| 参数 | 含义 | 填写方式 |
| --- | --- | --- |
| ``` name ``` | 工具名（AI 调用的名字） | 字符串，小写+下划线 |
| ``` toolset ``` | 属于哪个工具集 | "web" / "file" / "terminal" 等 |
| ``` schema ``` | AI 看到的说明书 | 之前设计的字典 |
| ``` handler ``` | 真正执行的函数 | lambda 包装 |
| ``` check_fn ``` | 可用性检查函数 | 无依赖则返回 True |
| ``` emoji ``` | UI 显示图标 | 可选，好看用的 |

---

## 6. 步骤四：添加到发现列表

### 6.1 找到发现列表

```
model_tools.py
```

 中的 

```
_discover_tools()
```

 函数维护着所有工具模块的列表：

```
# model_tools.pydef _discover_tools():    _modules = [        "tools.ansi_strip",        "tools.binary_extensions",        # ... 已有 60+ 个 ...        # 在这里添加新工具    ]
```

### 6.2 添加新工具

打开 

```
model_tools.py
```

，找到 

```
_modules
```

 列表，在任意位置添加新工具：

```
# model_tools.py 约第 138 行附近_modules = [    # ... 其他工具 ...    "tools.cronjob_tools",    "tools.currency_convert_tool",  # ← 添加这一行    "tools.debug_helpers",    # ... 其他工具 ...]
```

---

## 7. 步骤五：验证工具可用

### 7.1 快速验证（Python 交互式）

```
# 在终端中运行cd ~/code/hermes-agentsource .venv/bin/activatepython>>> from model_tools import handle_function_call>>> result = handle_function_call(...     "currency_convert",...     {"amount": 100, "from_currency": "USD", "to_currency": "CNY"}... )>>> print(result)
```

**预期输出：**

```
{"success": true, "from": "USD", "to": "CNY", "amount": 100.0, "converted_amount": 725.5, "rate": 7.255, "time": "2025-03-25 12:00:00 UTC"}
```

### 7.2 在 Hermes 中验证

```
重启 Hermes（新会话生效）用户：100美元换成人民币是多少？  │  ▼Hermes AI 调用 currency_convert  │  ▼返回结果给 AI  │  ▼Hermes 回复："根据最新汇率，100 美元 = 725.50 人民币（1 USD = 7.255 CNY）"
```

---

## 8. 完整代码

以下是 

```
tools/currency_convert_tool.py
```

 的完整代码：

```
#!/usr/bin/env python3"""Currency Convert Tool ModuleConvert an amount from one currency to another using real-time exchange rates.Uses the free exchangerate-api.com API (no API key required).Usage:    currency_convert(amount=100, from_currency="USD", to_currency="CNY")"""import jsonimport urllib.errorimport urllib.requestfrom datetime import datetimefrom typing import Dict, Any# ============================================================# Schema：给 AI 模型看的说明书# ============================================================CURRENCY_CONVERT_SCHEMA = {    "name": "currency_convert",    "description": (        "Convert an amount from one currency to another using real-time exchange rates.\n\n"        "Use when: user asks about currency conversion, exchange rates, "        "how much is X in Y currency, etc.\n\n"        "Source: ExchangeRate-API (free tier, no API key required).\n\n"        "Supported currencies: USD, EUR, GBP, CNY, JPY, KRW, AUD, CAD, CHF, INR, SGD, ..."    ),    "parameters": {        "type": "object",        "properties": {            "amount": {                "type": "number",                "description": (                    "The amount of money to convert. "                    "Example: 100, 50.5, 1000"                )            },            "from_currency": {                "type": "string",                "description": (                    "Source currency code (3-letter ISO 4217). "                    "Examples: USD, EUR, GBP, CNY, JPY, KRW, AUD, CAD"                )            },            "to_currency": {                "type": "string",                "description": (                    "Target currency code (3-letter ISO 4217). "                    "Examples: USD, EUR, GBP, CNY, JPY, KRW, AUD, CAD"                )            }        },        "required": ["amount", "from_currency", "to_currency"]    }}# ============================================================# 可用性检查# ============================================================def check_currency_convert_requirements() -> bool:    """货币转换工具始终可用（使用免费公开 API）"""    return True# ============================================================# Handler：真正做事的函数# ============================================================def currency_convert_handler(args: dict, **kwargs) -> str:    """    将一种货币转换为另一种货币。        Args:        args: 包含 amount, from_currency, to_currency        **kwargs: task_id 等额外参数        Returns:        JSON 字符串    """        # ========== 第1步：解析参数 ==========    amount = args.get("amount")    from_currency = args.get("from_currency", "").upper().strip()    to_currency = args.get("to_currency", "").upper().strip()        # 参数验证    if amount is None or amount == "":        return json.dumps({"error": "amount is required"})        try:        amount = float(amount)        if amount < 0:            return json.dumps({"error": "amount must be a positive number"})    except (ValueError, TypeError):        return json.dumps({"error": f"invalid amount: {amount}"})        if not from_currency:        return json.dumps({"error": "from_currency is required"})        if not to_currency:        return json.dumps({"error": "to_currency is required"})        # ========== 第2步：调用外部 API ==========    try:        # 使用 exchangerate-api.com 的免费 API        url = f"https://open.er-api.com/v6/latest/{from_currency}"                req = urllib.request.Request(            url,            headers={"User-Agent": "Hermes-Agent/1.0"}        )                with urllib.request.urlopen(req, timeout=10) as response:            data = json.loads(response.read().decode("utf-8"))                # 检查 API 返回状态        if data.get("result") != "success":            return json.dumps({                "error": "exchange rate API returned an error"            })                rates = data.get("rates", {})        rate = rates.get(to_currency)                if rate is None:            return json.dumps({                "error": f"currency '{to_currency}' is not supported"            })                # ========== 第3步：计算结果 ==========        converted_amount = round(amount * rate, 2)                # ========== 第4步：返回 JSON 字符串 ==========        return json.dumps({            "success": True,            "from": from_currency,            "to": to_currency,            "amount": amount,            "converted_amount": converted_amount,            "rate": rate,            "time": data.get("time", ""),        })        except urllib.error.URLError as e:        return json.dumps({            "error": f"network error: could not fetch exchange rate. "                     f"please check your internet connection."        })    except Exception as e:        return json.dumps({            "error": f"failed to convert currency: {str(e)}"        })# ============================================================# 注册到全局注册表# ============================================================from tools.registry import registryregistry.register(    name="currency_convert",    toolset="web",    schema=CURRENCY_CONVERT_SCHEMA,    handler=lambda args, **kw: currency_convert_handler(args, **kw),    check_fn=check_currency_convert_requirements,    emoji="💱",)
```

---

## 9. 常见问题与调试

### 9.1 工具注册了但 Hermes 说"找不到"

**原因：**

```
model_tools.py
```

 的 

```
_modules
```

 列表没有更新

**解决：** 确保在 

```
_discover_tools()
```

 的列表中添加了新模块

### 9.2 工具调用成功但返回"Unknown tool"

**原因：** Handler 抛出了异常，被 

```
registry.dispatch
```

 捕获并返回了错误

**解决：** 检查返回的 JSON 里是否有 

```
"error"
```

 字段

### 9.3 Schema 没问题但 AI 不调用工具

**原因：** Schema 的 

```
description
```

 没有说清楚在什么场景使用

**解决：** 在 description 开头加上 

```
"Use when: ..."
```

 说明触发场景

### 9.4 调试技巧

```
# 在 handler 里加日志import logginglogger = logging.getLogger(__name__)def currency_convert_handler(args, **kwargs):    logger.info(f"currency_convert called with: {args}")    try:        result = do_convert(args)        logger.info(f"Result: {result}")        return json.dumps(result)    except Exception as e:        logger.error(f"Error: {e}")        raise  # 重新抛出，让 registry.dispatch 处理
```

---

## 10. 举一反三：更多工具示例

### 10.1 工具：单位转换（长度/重量/温度）

```
UNIT_CONVERT_SCHEMA = {    "name": "unit_convert",    "description": "Convert between units of measurement...",    "parameters": {        "properties": {            "value": {"type": "number"},            "from_unit": {"type": "string", "enum": ["km", "miles", "kg", "lbs", ...]},            "to_unit": {"type": "string", "enum": ["km", "miles", "kg", "lbs", ...]},        }    }}
```

### 10.2 工具：计算器（支持表达式）

```
CALCULATE_SCHEMA = {    "name": "calculate",    "description": "Evaluate a mathematical expression...",    "parameters": {        "properties": {            "expression": {"type": "string", "description": "Math expression, e.g. '2+2*3'"}        }    }}def calculate_handler(args):    import math  # 可以用 math 库做复杂计算    expression = args["expression"]    # 安全评估（只用 ast.parse 检查语法，不执行）    result = safe_eval(expression)    return json.dumps({"result": result})
```

### 10.3 工具：Wikipedia 快速查询

```
WIKIPEDIA_SCHEMA = {    "name": "wikipedia_lookup",    "description": "Quickly look up a topic on Wikipedia...",    "parameters": {        "properties": {            "query": {"type": "string"}        }    }}
```

---

## 总结

本章你应该掌握：

- 如何从需求出发设计一个工具
- 如何写一个符合规范的 Schema
- 如何实现 Handler 的标准三步模式
- 如何注册工具到 Hermes
- 如何添加到发现列表
- 如何验证工具正常工作
- 常见问题的调试方法

---

## 教程系列总结

恭喜你完成整个系列！现在你应该对 Hermes Agent 有了完整的理解：

```
第一章：本地启动及项目结构第二章：系统架构全景图第三章：工具系统深度解析第四章：Gateway 消息流深度解析第五章：记忆与 Skills 系统深度解析第六章：子 Agent 与并行执行深度解析第七章：实践——添加自定义工具
```

**你已经掌握了 Hermes Agent 的核心设计哲学和主要模块的工作原理。**
