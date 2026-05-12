> 📎 来源: [知行缠壹](https://mp.weixin.qq.com/s?__biz=MzUzNDc5ODExNQ==&mid=2247483879&idx=1&sn=38cf6e6f71c387c594f95073d02be038&chksm=fb4e51444958920f908c5f7cd2b1a1e2cdf16e29d7385009064cc12234039b15d60d8a203b99&mpshare=1&scene=1&srcid=0420RXRwfToWGOEHwPMAzjdt&sharer_shareinfo=8fe4c9ed7bf6d75f9e355b4536116cb6&sharer_shareinfo_first=8fe4c9ed7bf6d75f9e355b4536116cb6) | 时间: 2026-04-20 21:35

---

|  |
| --- |
| 上一篇文章《给 AI 装上技能包》介绍了 Skill 的基本概念。但如果你只停留在"安装几个现成技能"的阶段，那就像买了辆法拉利却只在市区开 30 码——太浪费了。  今天，我们来聊聊 Skill 的**进阶玩法**：如何让 Skill 绑定特定 Agent，变成"专属能力"？如何用 RAG 让 Skill 带上你的业务文档？怎么用脚本让 Skill 自动执行复杂任务？ |

## 01为什么需要进阶 Skill？

**基础 Skill 的局限：**

| 场景 | 基础 Skill | 进阶 Skill |
| --- | --- | --- |
| 网页采集 | 只能抓取公开页面 | 能登录、能过反爬、能提取结构化数据 |
| 投资分析 | 只能给通用建议 | 能读你的持仓文档、结合你的策略、输出定制化报告 |
| 自动化 | 只能执行单步动作 | 能根据触发器自动决策、多步协同、异常处理 |

|  |
| --- |
| **💡 核心洞察：**问题不在 Skill 不够强，而在你没用好它。 |

**进阶 Skill 的三大武器：**

| 武器 | 作用 | 典型场景 |
| --- | --- | --- |
| **agentBindings** | 绑定特定 Agent，变成"专属能力" | 让"投资分析 Agent"永远带上你的投资策略文档 |
| **references** | 注入 RAG 知识，让 Skill 懂你的业务 | 让"客服技能"学会你的产品手册 |
| **scripts** | 嵌入脚本，自动执行复杂任务 | 让"周报技能"自动拉数据、生成图表、发送邮件 |

## 02武器一：agentBindings——让 Skill 绑定专属 Agent

默认情况下，Skill 是"通用能力"，谁都能用。但有时候，你希望某个 Skill**只被特定 Agent 使用**，或者**带上特定 Agent 的配置**。这时候就用 

```
agentBindings
```

。

|  |
| --- |
| **📍 实战案例：投资分析 Skill** 让"投资分析 Agent"自动带上持仓文档和投资策略，输出符合你风格的分析报告。 |

**SKILL.md 配置示例：**

```
---
```

```

```

**效果：**只有 

```
investment-agent
```

 能使用这个 Skill，使用时自动带上持仓文档和策略。

## 03武器二：references——用 RAG 让 Skill 懂你的业务

**RAG（检索增强生成）**= Skill 在回答前，先从你的文档里"检索"相关信息，再"生成"答案。

|  |
| --- |
| **📍 实战案例：客服 Skill** 用户问"如何导出数据" → Skill 从   ``` product-faq.md ```   检索 → 给出准确答案 |

**references 目录结构：**

```
references/
```

## 04武器三：scripts——用脚本自动执行复杂任务

有些任务，AI 不适合直接做：需要调用外部 API、处理大量数据、定时执行、精确控制流程。这时候，让 Skill 调用脚本，**AI 负责"指挥"，脚本负责"干活"**。

|  |
| --- |
| **📍 实战案例：周报生成 Skill** 自动拉取 GitHub 提交记录 + Jira 任务完成情况 + 时间追踪数据，生成周报草稿。 |

**脚本目录结构：**

```
scripts/
```

## 05实战案例：网页采集 Skill（多工具协同）

需要采集小红书笔记数据（需登录）、1688 商品价格（有反爬）、公众号文章（付费墙）？创建一个"网页采集 Skill"，**协同多个工具**：

- **agent-browser**

  ：处理需要登录的站点
- **scrapling**

  ：绕过反爬保护
- **jina-reader**

  ：绕过付费墙
- **tavily**

  ：初步搜索

|  |
| --- |
| **💡 关键点：**不是用一个工具硬扛，而是**根据站点特性选择工具**。 |

## 06Skill 最佳实践

**如何写好 SKILL.md？**

|  |
| --- |
| **1. 标题清晰** ``` name ```   和   ``` description ```   一句话说明 Skill 是干什么的 |

|  |
| --- |
| **2. 能力说明具体** 能做什么（具体场景）+ 不能做什么（边界） |

|  |
| --- |
| **3. 使用场景明确** 输入是什么，输出是什么 |

**推荐目录结构：**

```
my-skill/
```

## 07ClawHub 技能市场

ClawHub 是 OpenClaw 的技能市场，你可以**发现、安装、分享**Skill。

|  |
| --- |
| **📍 常用命令** npx skills add -g  # 安装 npx skills list --global # 列出 npx skills publish ./my-skill # 发布 |

## ✓总结

|  |
| --- |
| **Skill 进阶玩法核心：**  1️⃣**agentBindings**：让 Skill 绑定专属 Agent，变成"专属能力"  2️⃣**references**：用 RAG 让 Skill 带上你的业务文档  3️⃣**scripts**：用脚本自动执行复杂任务 |

|  |
| --- |
| **🎯 记住：**Skill 不只是"工具包"，更是你的**业务逻辑封装器**。不要只用现成技能，要学会**定制专属能力**。 |

🔗 相关资源：

ClawHub 技能市场：clawhub.ai

OpenClaw 文档：docs.openclaw.ai
