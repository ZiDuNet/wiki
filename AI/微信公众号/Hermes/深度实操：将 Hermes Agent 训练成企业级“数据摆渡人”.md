> 📎 来源: [李朝兴](https://mp.weixin.qq.com/s?__biz=MjM5Mzk4MjUzNQ==&mid=2449526043&idx=1&sn=2052807944ca1a3a8c8561d69eeb7725&chksm=b0f4d1b5f2f1121093090661bf22f76d3c89d715532d79c0ee73d3093166f4611c9e96be9298&mpshare=1&scene=1&srcid=0429JFdufTyoEJo8VZr3WVhR&sharer_shareinfo=7ea221d006a7d8b3f7425c55c0894e4f&sharer_shareinfo_first=7ea221d006a7d8b3f7425c55c0894e4f) | 时间: 2026-04-29 14:08

---

![](assets/img_b54d457bb154.jpg)

在前一篇文章中，我们确立了“工具化封装”的思路。但要让 Hermes Agent 真正上生产环境，光有思路远远不够。你必须解决三个工程化难题：非结构化数据的吞噬、长链路事务的最终一致性、以及老系统的“反人类”认证。

下面，我们以最复杂的ERP里抓数据，同步到 SaaS 版 CRM，并在 OA 里踢一脚审批。 我将带你一步步写出能跑、能抗、能恢复的代码。

第一章：工具级封装——不仅要通，还要“抗打”

老旧 ERP 没有 REST API，只有数据库。但直接让 Agent 写 SQL？那是灾难。我们必须构建一层 Data Access Object (DAO) 工具。

1.1 深度的数据脱敏与清洗工具

不要只做简单的字段映射。老系统的数据库里往往有坑：逻辑删除的脏数据、全角半角字符混用、一对多关系用逗号拼接。

进阶实操代码：构建坚固的 ERP 工具

python

# hermes\_tools/deep\_erp\_tool.py

import pymysql

import re

from hermes import tool

from hermes.exceptions import ToolExecutionError

import unicodedata

class ERPSanitizer:

    """数据清洗器：专门对付老系统的脏数据"""

    

    @staticmethod

    def normalize\_customer\_name(raw\_name):

        """去掉全角空格，统一大小写，清洗特殊符号"""

        if not raw\_name:

            return "未知客户"

        # 全角转半角

name = unicodedata.normalize('NFKC', raw\_name)

        # 去掉数据库里常有的前后制表符

        name = name.strip().replace('\t', '')

        # 去掉连续空格

        name = re.sub(r'\s+', ' ', name)

        return name

    @staticmethod

    def mask\_sensitive(data\_dict):

        """对返回体做彻底的脱敏"""

        # 1. 手机号脱敏

        if 'phone' in data\_dict and data\_dict['phone']:

           data\_dict['phone'] = re.sub(r'(\d{3})\d{4}

           (\d{4})', r'\1\*\*\*\*\2', str(data\_dict['phone']))

        

        # 2. 身份证脱敏

        if 'id\_card' in data\_dict and data\_dict['id\_card']:

            data\_dict['id\_card'] = re.sub(r'(\d{4})\d{10}(\d{4})', r'\1\*\*\*\*\*\*\*\*\*\*\2', str(data\_dict['id\_card']))

            

        # 3. 地址模糊化（只留省市）

        if 'address' in data\_dict and data\_dict['address']:

            data\_dict['address'] = data\_dict['address'][:6] + '...'

            

        return data\_dict

@tool(

    name="fetch\_erp\_order\_full\_detail",

    description="获取ERP订单全量详情，包括客户信息、商品明细、物流状态。当用户询问订单详情时必须调用此工具。"

)

def fetch\_erp\_order\_full\_detail(order\_id: str) -> dict:

    """

    增强版ERP查询：支持连表查询、数据清洗、自动脱敏

    """

    conn = None

    try:

        # 1. 连接池获取（不要每次都新建连接，生产环境用 DBUtils 或 SQLAlchemy 池）

        conn = pymysql.connect(

            host='10.0.0.12', 

            user='readonly\_user',  # 必须只读账户

            password='Str0ngP@ss', 

            database='legacy\_erp',

            connect\_timeout=3,  # 超时熔断

            charset='utf8mb4'

        )

        

        with conn.cursor(pymysql.cursors.DictCursor) as cursor:

            # 2. 复杂业务逻辑写在这里，不让 LLM 碰 SQL

            sql = """

                SELECT 

    o.order\_id, o.total\_amount,   o.status, o.create\_time,

    c.customer\_name, c.phone as customer\_phone, 

    c.id\_card, oi.product\_name, oi.quantity, 

    oi.unit\_price

                FROM orders o

                JOIN customers c ON o.customer\_id = c.id

                JOIN order\_items oi ON o.id = oi.order\_id

                WHERE o.order\_id = %s AND o.is\_deleted = 0  # 过滤逻辑删除

            """

            cursor.execute(sql, (order\_id,))

            rows = cursor.fetchall()

            

            if not rows:

                return {"status": "not\_found", "message": f"订单 {order\_id} 不存在或已删除"}

            

            # 3. 数据结构重构：将扁平化的一对多数据转为层级 JSON

            order\_data = {

                "order\_id": rows[0]['order\_id'],

                "total\_amount": float(rows[0]

                          ['total\_amount']),

                "status": rows[0]['status'],

                "create\_time": rows[0]

['create\_time'].strftime("%Y-%m-%d %H:%M"),

                "customer": {

                    "name": 

ERPSanitizer.normalize\_customer\_name(rows[0]['customer\_name']),

                    "phone": rows[0]['customer\_phone'],

                    "id\_card": rows[0]['id\_card']

                },

                "items": []

            }

            

            for row in rows:

                order\_data["items"].append({

                    "product": row['product\_name'],

                    "quantity": row['quantity'],

                    "unit\_price": float(row['unit\_price'])

                })

            

            # 4. 执行脱敏

            order\_data = 

           ERPSanitizer.mask\_sensitive(order\_data)

            

            return order\_data

            

    except pymysql.Error as e:

        # 5. 优雅降级：不要直接把数据库报错抛给 LLM，要封装成自然语言

        raise ToolExecutionError(f"ERP数据库暂时无法连接，错误代码: {e.args[0]}")

    finally:

        if conn:

            conn.close()

关键点解析：

· SQL 硬编码：永远不要让 LLM 拼接 SQL 语句。工具函数内部写死了 SQL 模板，外部只能传参数。

· 数据重构：老系统关联查询出的扁平数据，在工具层就转成了易于 LLM 理解的嵌套 JSON。

· 降级处理：抛出 ToolExecutionError 会让 Hermes Agent 意识到这不是它的错，并告诉用户“ERP系统繁忙，请稍后再试”，而不是胡乱猜测。

第二章：多步协同——引入“工作记忆”与“状态回查”

跨系统协同最怕的不是失败，而是卡在中间。比如：ERP查到了，CRM创建任务失败了，用户不知道发生了什么。

我们需要利用 Hermes 的 Conversation Memory（对话记忆） 和 Context Object（上下文对象） 来保证全链路的可观测性。

2.1 构建带“工作记忆”的长链路协同

场景设定： 用户指令“把今天所有未付款的大额订单找出来，在CRM给对应的销售创建催款任务。”

这个指令需要多个步骤，步骤二依赖于步骤一的结果。我们要让 Agent 学会像实习生一样，记下第一步的结果，再做第二步。

Hermes 配置与系统提示词（完整版）

yaml

# hermes\_agent\_config.yaml

llm:

  model: "qwen-max"  # 或 gpt-4-turbo

  temperature: 0.1  # 严谨任务用低温，降低幻觉

tools:

  module\_paths:

    - hermes\_tools.deep\_erp\_tool   # ERP工具

    - hermes\_tools.crm\_tool        # CRM工具

    - hermes\_tools.oa\_tool         # OA工具

session:

  memory\_type: "conversation\_buffer"  # 保留最近10轮对话作为“工作记忆”

  max\_token\_limit: 4000

agent\_profile: |

  【身份】：你是企业数据运转中枢，直接操作 ERP、CRM、OA 系统。

  

  【核心调度逻辑】—— 状态机思维：

  1. \*\*数据提取阶段\*\*：

     - 一旦涉及查询，必须调用 

        fetch\_erp\_order\_full\_detail 

        或 search\_erp\_orders\_by\_criteria。

     - 查询成功后，将关键信息（订单ID列表、金额、对应销售）记在心中（工作记忆）。

2. \*\*条件决策阶段\*\*：

     - 检查步骤1返回的订单金额。若单笔金额 > 10万且状态为“未付款”，标记为高风险。

     - 过滤出所有高风险订单，提取其订单ID和销售姓名。

  

  3. \*\*跨系统执行阶段\*\*：

     - \*\*CRM操作\*\*：对每个高风险订单，调用 crm\_create\_follow\_up\_task。

       参数：owner = 销售姓名, subject = "紧急催款：订单{order\_id}金额{amount}元"

       \*\*注意\*\*：此步骤必须循环调用，不能只调一次。提交流程后等待返回的任务ID。

     - \*\*OA操作\*\*：如果累计高风险金额超过50万，调用 oa\_create\_finance\_alert，向财务总监发起特别预警。

  

  4. \*\*结果汇报阶段\*\*：

     - 汇总所有 CRM 创建的任务ID，生成表格返回用户。

     - 若任一步骤失败，停止执行并详细告知用户已成功和失败的操作，严禁继续执行逻辑。

2.2 工具：CRM 回调验证与幂等性

CRM 那边的接口可能不靠谱，我们必须写一个带重试机制和幂等校验的工具。

python

# hermes\_tools/crm\_tool.py

import requests

import hashlib

from hermes import tool

from hermes.exceptions import ToolExecutionError

import time

@tool(name="crm\_create\_follow\_up\_task")

def crm\_create\_follow\_up\_task(owner: str, subject: str, order\_id: str) -> dict:

    """

    在CRM创建跟进任务。

    idempotency\_key 防止网络超时导致的重复创建。

    """

1. 生成幂等键：相同订单ID+操作类型，绝对不会重复创建任务

    idempotency\_key = hashlib.md5(f"

   {order\_id}\_follow\_up".encode()).hexdigest()

    

    headers = {

        "Authorization": "Bearer xxxxx",

        "Content-Type": "application/json",

        "Idempotency-Key": idempotency\_key

    }

    

    payload = {

        "task\_owner": owner,

        "subject": subject,

        "due\_date": "today",

        "related\_order": order\_id

    }

    

    # 2. 指数退让重试（Retry with Backoff）

    max\_retries = 3

    for attempt in range(max\_retries):

        try:

            resp = requests.post(

                "https://api.crm.com/v3/tasks", 

                json=payload, 

                headers=headers, 

                timeout=5

            )

            

            if resp.status\_code == 200:

                task\_data = resp.json()

                return {

                    "task\_id": task\_data['id'], 

                    "url": task\_data['url'],

                    "creation\_status": "success"

                }

            elif resp.status\_code == 409:  # 幂等冲突，说明已创建

                return {

                    "task\_id": "已存在(幂等)", 

                    "creation\_status": "skipped"

                }

            elif resp.status\_code >= 500:  # 服务端错重试

    if attempt < max\_retries - 1:

                    time.sleep(2 \*\* attempt)

                    continue

                else:

                    raise ToolExecutionError(f"CRM服务异常，状态码: {resp.status\_code}")

            else:  # 4xx 客户端错不重试

                raise ToolExecutionError(f"CRM请求参数错误: {resp.text}")

                

        except requests.exceptions.Timeout:

            if attempt < max\_retries - 1:

                time.sleep(2 \*\* attempt)

                continue

            else:

                raise ToolExecutionError("CRM接口超时，请检查网络")

为什么这样做？

· 幂等性：即使 Agent 因为 LLM 响应超时而重试了这个操作，CRM 端也不会创建两个重复任务。

· 详细异常分类：LLM 读到 ToolExecutionError("CRM接口超时") 后，会生成人性化的回复，而不是把一堆 ConnectionError 堆栈拍到用户脸上。

第三章：突破认证壁垒——SSO 与凭据动态注入

你的 OA 系统可能需要动态 Token，ERP 数据库密码不能写死在代码里。怎么让 Hermes Agent 自动、安全地获得权限？

3.1 基于 OAuth2 的 Client Credentials 流

在工具函数内部集成 oauthlib，让每次调用系统时，Agent 自动去认证中心换取 Token。

python

# hermes\_tools/auth\_manager.py

from oauthlib.oauth2 import 

BackendApplicationClient

from requests\_oauthlib import OAuth2Session

import time

class TokenManager:

    """全局Token管家，自动刷新"""

    def \_\_init\_\_(self):

        self.client\_id = "hermes\_agent"

        self.client\_secret = "safe\_secret\_from\_vault"  

# 建议从环境变量或 Vault 读取

        self.token\_url = 

"https://sso.company.com/oauth/token"

        self.\_token = None

        self.\_expires\_at = 0

    def get\_valid\_token(self):

        """获取有效Token，过期自动续期"""

        if time.time() > self.\_expires\_at - 60:  # 提前60秒刷新

            client = BackendApplicationClient(client\_id=self.client\_id)

            oauth = OAuth2Session(client=client)

            self.\_token = oauth.fetch\_token(

                token\_url=self.token\_url,

                client\_id=self.client\_id,

                client\_secret=self.client\_secret

            )

            self.\_expires\_at = time.time() + self.\_token.get('expires\_in', 3600)

        return self.\_token['access\_token']

# 全局实例

token\_manager = TokenManager()

# 在 OA 工具中使用

@tool(name="oa\_start\_approval")

def oa\_start\_approval(approver\_id: str, form\_data: dict):

    token = token\_manager.get\_valid\_token()

    headers = {"Authorization": f"Bearer {token}"}

    resp = requests.post("https://oa.company.com/api/workflow/start", 

                         json=form\_data, headers=headers)

第四章：完整的协同脚本——“一键同步”指令落地

当以上所有工具都就绪，你可以在 Hermes 的 UI 或 API 中发出这样的指令：

用户指令：

“扫描 ERP 中昨天到今天所有客户为‘宇宙大公司’的新订单，只要金额超过5万，就在 CRM 里给销售总监李总创建一个‘重点跟进’任务，然后把订单详情截图发给我。如果总金额超过100万，帮我发一个 OA 审批，标题叫‘大客户超额交易报备’，审批人设置为 CFO 王总。”

Agent 的完整思考与动作链（日志回放）：

1. Task Planning: "用户要三件事：查订单、建CRM任务、可能发起OA。我按顺序执行。"

2. Action 1 - 调ERP工具：search\_erp\_orders\_by\_criteria(customer\_name="宇宙大公司", start\_date="2024-05-20", end\_date="2024-05-21")

   · Result：返回3个订单，总金额 120万。

3. Working Memory Update: "记忆：订单A(45万), B(55万), C(20万)，总额120万 > 100万阈值，待会儿需要OA。"

4. Action 2 - 调CRM工具 (循环)：

   · crm\_create\_follow\_up\_task(owner="lizong", subject="重点跟进：订单A", order\_id="A001")

   · crm\_create\_follow\_up\_task(owner="lizong", subject="重点跟进：订单B", order\_id="A002")

   · crm\_create\_follow\_up\_task(owner="lizong", subject="重点跟进：订单C", order\_id="A003")

   · Result：三个任务全部创建成功，ID为 T101, T102, T103。

5. Action 3 - 逻辑判断：总额120万 > 100万，触发 OA 分支。

6. Action 4 - 调OA工具：oa\_start\_approval(approver\_id="wang\_CFO", form\_title="大客户超额交易报备", content="...")

   · Result：OA 审批流创建成功，流水号 OA-998。

7. Final Response:

   “已为您完成以下操作：

   1. 在 ERP 中找到 3 笔宇宙大公司的订单，总额 120 万元。

   2. 已为李总在 CRM 创建 3 条重点跟进任务：T101、T102、T103。

   3. 由于总额超 100 万，已自动向王总发起 OA 审批，流水号 OA-998，请关注审批进度。”

结语

到了这一步，你已经不再是简单地调用 LLM API 了。你是在用工程化手段，把 Hermes Agent 打造成了一个 懂业务、守规矩、有记忆、抗故障 的数字员工。

这套方案的精髓不是 Hermes 框架本身有多逆天，而是它给了你一个骨架，让你能把系统权限、业务规则、异常处理机制有机地填充进去。当老旧的 ERP 和现代 SaaS 在 Hermes 这座桥梁上自如流转数据时，你就会发现，打通系统壁垒这件事，代码其实是最后一步，前面的工具设计哲学，才是真正的分水岭。

![](assets/img_7602c12c7fc6.jpg)
