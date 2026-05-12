> 📎 来源: [非碳基观察](https://mp.weixin.qq.com/s?__biz=MzU5Mjc3NjEwMg==&mid=2247483915&idx=1&sn=a382dca18dbc499df0d6388b781d1c33&chksm=ff9c5d0d07fac5caff81caa0fe4e4ce2a39882bc1972a93f3cf680a769177867cb7076508072&mpshare=1&scene=1&srcid=04248P04RLcyPoCAOWybPd9e&sharer_shareinfo=00c4dfb70ad6afaffe86b5add8df522f&sharer_shareinfo_first=00c4dfb70ad6afaffe86b5add8df522f) | 时间: 2026-04-24 00:14

---

> 让 AI 记住你的独门秘籍，一次封装，反复使用

---

## 一、什么是 Skills？

**Skills 是 AI 的"能力扩展包"** —— 把你熟悉的工作流程、工具用法、专业知识打包成一个可复用的模块，让 AI 每次遇到类似任务时都能按你的方式执行。

### 类比理解

| 传统方式 | Skills 方式 |
| --- | --- |
| 每次告诉 AI 怎么做 | 教一次，永远记住 |
| 重复写同样的提示词 | 触发技能自动加载 |
| AI 容易忘记细节 | 固化到上下文里 |
| 无法团队协作 | 可分享、可安装 |

### 实际例子

**没有 Skills 时**：

```
你：帮我爬取这个网页的产品数据，要用 Python，   先 requests 获取 HTML，然后 BeautifulSoup 解析，   提取标题、价格、图片链接，存成 JSON...（每次都要说一遍）
```

**有 Skills 后**：

```
你：爬取 https://shop.com/products（AI 自动调用 scrapling skill，按你预设的方式执行）
```

---

## 二、Skills 的核心结构

一个 Skill 就是一个文件夹，最少只需要一个文件：

```
my-skill/└── SKILL.md
```

### SKILL.md 的组成

```
---name: skill-名称description: 一句话描述这个技能做什么，什么时候触发---# 技能说明正文这里是详细的使用指南...
```

---

## 三、实战：封装你的第一个 Skills

### 场景：把"两会政策分析"工作流封装成 Skill

假设你经常需要：

1. 抓取政府网站政策文件
2. 提取关键信息
3. 分析对个人的机会
4. 输出结构化报告

#### 步骤 1：创建 Skill 目录

```
# 在 workspace 下创建 skills 目录（如果不存在）mkdir -p C:\Users\Administrator\.openclaw\workspace\skills\two-sessions-analyzer
```

#### 步骤 2：编写 SKILL.md

```
---name: two-sessions-analyzerdescription: 分析全国两会政策文件，提取个人创业机会。  使用场景：(1) 两会期间抓取政策信息，(2) 分析政策对个人/小企业的影响，  (3) 识别商机和痛点，(4) 生成结构化报告。triggers:  - pattern: "两会 | 政策分析 | 创业机会 | 政策解读"    description: "检测政策分析需求"examples:  - "分析今年两会政策，找出适合个人的赚钱机会"  - "解读十五五规划里的商机"  - "两会提到了哪些民生痛点可以创业"---# 两会政策分析技能## 工作流程### 1. 信息收集使用 scrapling 或 web_fetch 抓取以下来源：- 新华网两会专题：https://www.xinhuanet.com/politics/2026lh/- 人民网两会频道：https://www.people.com.cn/n1/2026/0305/c1001-*.html- 政府工作报告全文```python# 示例：抓取政策标题列表urls = [    "https://www.xinhuanet.com/politics/2026lh/",    "https://www.news.cn/politics/20260303/23274f88a82e45379ddb9c50f62a6bb6/c.html"]
```

### 2. 信息提取

对每篇文章提取：

- **政策方向**：如"智能经济"、"养老服务"、"乡村振兴"
- **具体举措**：如"建立生育补贴制度"、"数字经济核心产业占 GDP 12.5%"
- **量化指标**：如"人均预期寿命 80 岁"、"研发投入增长 7%"

### 3. 机会分析框架

按以下维度分析：

| 维度 | 分析问题 |
| --- | --- |
| 痛点 | 政策要解决什么民生问题？ |
| 需求 | 哪些人群有未被满足的需求？ |
| 门槛 | 个人/小团队能进入吗？ |
| 规模 | 市场有多大？ |
| 竞争 | 已有玩家是谁？ |

### 4. 输出格式

```
## 政策方向：XXX### 政策要点- 要点 1- 要点 2### 个人机会| 方向 | 痛点 | 赚钱方式 ||------|------|----------|| XXX | XXX | XXX |### 行动建议1. 短期（1-3 月）：...2. 中期（3-6 月）：...3. 长期（6-12 月）：...
```

## 注意事项

- 优先分析"投资于人"、"智能经济"、"银发经济"相关条款
- 区分国家大战略和个人小机会
- 标注政策落地时间窗口

```
#### 步骤 3：测试 Skill```bash# 重启 OpenClaw 或等待自动刷新# 然后测试："分析今年两会政策，找出适合个人的赚钱机会"
```

---

## 四、进阶：添加脚本和资源

当工作流包含固定代码时，可以把脚本打包进 Skill。

### 完整 Skill 结构

```
two-sessions-analyzer/├── SKILL.md              # 必需：技能说明├── scripts/              # 可选：可执行脚本│   ├── fetch_policy.py   # 抓取政策│   └── analyze.py        # 分析机会├── references/           # 可选：参考资料│   └── policy_framework.md  # 分析框架文档└── assets/               # 可选：输出模板    └── report_template.md   # 报告模板
```

### 示例脚本：fetch\_policy.py

```
#!/usr/bin/env python3"""抓取两会政策文章"""import requestsfrom bs4 import BeautifulSoupdef fetch_policy_urls(base_url):    """提取政策文章链接"""    resp = requests.get(base_url)    soup = BeautifulSoup(resp.text, 'html.parser')        urls = []    for link in soup.select('a[href*="/politics/"]'):        href = link.get('href')        if href and'2026'in href:            urls.append(href)        return urls[:20]  # 限制数量def extract_content(url):    """提取文章正文"""    resp = requests.get(url)    soup = BeautifulSoup(resp.text, 'html.parser')        # 提取标题和正文    title = soup.find('h1').text.strip()    content = soup.find('div', class_='content').text.strip()        return {'title': title, 'content': content, 'url': url}if __name__ == '__main__':    urls = fetch_policy_urls('https://www.xinhuanet.com/politics/2026lh/')    for url in urls:        article = extract_content(url)        print(f"抓取：{article['title']}")
```

### 在 SKILL.md 中引用脚本

```
## 使用方法### 自动抓取```bashpython {baseDir}/scripts/fetch_policy.py
```

### 分析机会

```
python {baseDir}/scripts/analyze.py --input policy_data.json
```

> ```
> {baseDir}
> ```

>  会自动替换为 Skill 目录路径

```
---## 五、Skill 元数据详解### 完整 Frontmatter 示例```yaml---name: weatherdescription: 查询天气和预报。使用场景：用户询问天气、温度、降水、出行天气准备homepage: https://wttr.in/:helptriggers:  - pattern: "天气 | 下雨 | 温度 | 预报"    description: "检测天气查询需求"  - pattern: "weather|rain|temperature|forecast"    description: "English weather queries"auto_invoke: trueexamples:  - "北京今天天气怎么样"  - "明天会下雨吗"  - "周末上海天气"metadata:  {    "openclaw": {      "emoji": "🌤️",      "requires": { "bins": ["curl"] },      "primaryEnv": "WEATHER_API_KEY",    }  }---
```

### 字段说明

| 字段 | 作用 | 必填 |
| --- | --- | --- |
| `name` | 技能名称（唯一标识） | ✅ |
| `description` | 触发条件和使用场景 | ✅ |
| `homepage` | 技能主页/文档链接 | ❌ |
| `triggers` | 触发关键词模式 | ❌ |
| `auto_invoke` | 是否自动触发 | ❌ |
| `examples` | 使用示例 | ❌ |
| `metadata.openclaw.emoji` | 显示图标 | ❌ |
| `metadata.openclaw.requires.bins` | 依赖的命令行工具 | ❌ |
| `metadata.openclaw.requires.env` | 依赖的环境变量 | ❌ |

### 条件加载示例

```
# 只在 macOS 上加载metadata:{"openclaw":{"os":["darwin"]}}# 需要 Python 和 API Keymetadata:{    "openclaw":{      "requires":{        "bins":["python3"],        "env":["OPENAI_API_KEY"]      }    }}# 需要安装依赖metadata:{    "openclaw":{      "requires":{"anyBins":["uv","pip"]},      "install":[        {          "kind":"pip",          "package":"scrapling",          "label":"安装 Scrapling"        }      ]    }}
```

---

## 六、Skills 加载机制

### 三个来源（优先级从高到低）

```
1. workspace/skills/     ← 你的工作区技能（最高优先级）2. ~/.openclaw/skills/   ← 本地管理技能3.  bundled skills       ← 内置技能（最低优先级）
```

### 同名覆盖规则

如果三个地方都有 

```
weather
```

 skill：

- 只有 

  ```
  workspace/skills/weather
  ```

   会生效
- 其他两个被覆盖

### 配置文件覆盖

在 

```
~/.openclaw/openclaw.json
```

 中：

```
{  skills: {    entries: {      "two-sessions-analyzer": {        enabled: true,        env: {          "QVERIS_API_KEY": "sk-xxx"        }      },      "weather": { enabled: false }  // 禁用某个技能    }  }}
```

---

## 七、更多实战案例

### 案例 1：竞品监控 Skill

```
---name: competitor-monitordescription: 监控竞品网站价格/产品更新。使用场景：  (1) 定期抓取竞品价格，(2) 发现新品上架，(3) 价格变动提醒triggers:  - pattern: "竞品 | 监控 | 价格变动 | 新品"---# 竞品监控## 配置目标网站```pythonCOMPETITORS = [    {"name": "竞品 A", "url": "https://a.com/products"},    {"name": "竞品 B", "url": "https://b.com/shop"}]
```

## 输出格式

```
## 竞品监控报告 - 2026-03-06### 价格变动| 产品 | 原价 | 现价 | 变化 ||------|------|------|------|| XXX | ¥999 | ¥899 | -10% |### 新品上架- 产品 A（¥1299）- 产品 B（¥599）
```

```
### 案例 2：日报生成 Skill```markdown---name: daily-reportdescription: 自动生成工作日报。使用场景：  (1) 汇总当日完成的任务，(2) 整理明日计划，(3) 标注风险和问题triggers:  - pattern: "日报 | 工作日志 | 今日完成"---# 日报生成## 输入告诉 AI：- 今天做了什么- 遇到什么问题- 明天计划## 输出模板```markdown# 工作日报 - {{date}}## ✅ 今日完成1. ...2. ...## ⚠️ 问题/风险- ...## 📋 明日计划1. ...2. ...## 💡 思考/建议...
```

```
### 案例 3：数据分析 Skill```markdown---name: data-analyzerdescription: 数据分析 + 可视化。使用场景：  (1) CSV/Excel 数据分析，(2) 生成统计图表，(3) 输出洞察报告metadata:  {    "openclaw": {      "requires": { "bins": ["python3"] },      "install": [        {"kind": "pip", "package": "pandas matplotlib openpyxl"}      ]    }  }---# 数据分析## 脚本```python# scripts/analyze.pyimport pandas as pdimport matplotlib.pyplot as pltdef analyze_csv(file_path):    df = pd.read_csv(file_path)    # 生成统计和图表    return df.describe()
```

## 输出

- 统计摘要
- 趋势图（PNG）
- 关键洞察

```
---## 八、最佳实践### ✅ 应该做的1. **描述要具体**   ```yaml   # ❌ 太模糊   description: 帮助分析数据      # ✅ 具体   description: 分析 CSV/Excel 数据，生成统计图表和洞察报告。     使用场景：销售数据分析、用户行为分析、A/B 测试结果
```

2. **示例要真实**

   ```
   examples:  - "分析上月销售数据，找出 top10 产品"  - "对比 A/B 测试两组的转化率"
   ```
3. **脚本要测试**

- 实际运行脚本确保无 bug
- 验证输出符合预期

4. **文档要精简**

- SKILL.md 正文控制在 500 行内
- 详细内容放 

  ```
  references/
  ```

   目录

### ❌ 不应该做的

1. **不要包含无关文件**

   ```
   ❌ README.md❌ CHANGELOG.md❌ INSTALLATION_GUIDE.md
   ```
2. **不要重复信息**

- SKILL.md 和 references 文件不要重复
- 核心流程在 SKILL.md，细节在 references

3. **不要过度设计**

- 先解决具体问题，再考虑通用性
- 一个技能做好一件事

---

## 九、调试技巧

### 检查 Skill 是否加载

```
openclaw skills list
```

输出中查找你的 skill 名称，状态应为 

```
✓ ready
```

### 查看触发条件

在对话中测试触发词：

```
"帮我分析一下两会政策"  # 应该触发 two-sessions-analyzer
```

### 查看加载日志

```
# 查看 OpenClaw 日志cat ~/.openclaw/logs/openclaw.log | grep skills
```

### 热重载

修改 SKILL.md 后：

1. 默认会自动检测变化
2. 或重启 OpenClaw 会话

---

## 十、分享你的 Skills

### 发布到 ClawHub

```
# 进入 skill 目录cd workspace/skills/two-sessions-analyzer# 发布clawhub publish
```

### 安装别人的 Skills

```
# 从 ClawHub 安装clawhub install # 从本地安装clawhub install ./path/to/skill
```

### 团队协作

把 skill 目录放入团队共享目录：

```
{  skills: {    load: {      extraDirs: ["D:\\team-skills"]    }  }}
```

---

## 总结

### Skills 的价值

| 维度 | 收益 |
| --- | --- |
| 效率 | 一次封装，反复使用 |
| 质量 | 固化最佳实践 |
| 协作 | 团队共享能力 |
| 积累 | 形成知识资产 |

### 下一步行动

1. **选一个你常做的任务**（如数据分析、报告生成、信息收集）
2. **按本文步骤创建 Skill**
3. **测试并迭代优化**
4. **分享给团队**
