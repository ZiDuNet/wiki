# CrewAI — 多智能体协作框架

> GitHub: https://github.com/crewAIInc/crewAI
> Stars: 47.8k+ (2026年4月) | Forks: 6.5k+ | PyPI 月下载: 500万+
> 协议: MIT | 语言: Python (>=3.10 <3.14) | 独立于 LangChain

## 一句话简介

**纯 Python 多 Agent 编排框架** — 把复杂任务拆解成多个专业 AI 角色，让它们像真实团队一样协作。被称为"一人公司"的开源实现。

## 核心概念

| 概念 | 说明 |
|------|------|
| **Agent** | 具有角色(Role)、目标(Goal)、背景故事(Backstory)的 AI 智能体 |
| **Task** | 分配给 Agent 的具体任务，支持依赖链和结构化输出 |
| **Crew** | Agent 团队，管理任务分配和协作流程 |
| **Flow** | 事件驱动的生产级工作流，精细控制执行路径和状态管理 |

## 两种协作模式

### Crews（团队模式）
- Agent 自主决策、动态委派任务
- 角色分工协作，灵活解决问题
- 适合需要"智能协作"的场景

### Flows（流程模式）
- 事件驱动，精确控制执行路径
- 安全的状态管理，支持条件分支
- AI Agent + 生产 Python 代码混合编排
- 适合需要"精确控制"的生产环境

**最佳实践**: Crews + Flows 结合使用，兼顾自主性和可控性。

## 快速开始

```bash
# 安装
uv pip install crewai

# 创建项目
crewai create crew my_project

# 运行
cd my_project && crewai run
```

核心代码示例：
```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role='高级研究员',
    goal='深入研究目标领域并产出分析报告',
    backstory='你是一位经验丰富的研究分析师...',
    tools=[search_tool, scrape_tool]
)

writer = Agent(
    role='技术写作专家',
    goal='将研究成果转化为高质量技术文档',
    backstory='你擅长将复杂概念转化为清晰易懂的文字...'
)

research_task = Task(
    description='研究 {topic} 的最新进展',
    expected_output='详细的研究分析报告',
    agent=researcher
)

write_task = Task(
    description='基于研究报告撰写技术文档',
    expected_output='Markdown 格式的技术文档',
    agent=writer,
    dependencies=[research_task]
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task]
)
result = crew.kickoff()
```

## CrewAI AMP Suite（企业版）

- **Control Plane**: 统一管理、监控、扩展 Agent 和工作流
- **Tracing & Observability**: 实时追踪 Agent 执行，含指标、日志、调用链
- **企业安全**: 内置安全合规措施
- **部署选项**: 本地 / 云端

## AI Coding Agent 集成

Claude Code 一键安装 Skill：
```shell
/plugin marketplace add crewAIInc/skills
/plugin install crewai-skills@crewai-plugins
/reload-plugins
```

Cursor/Codex/Windsurf：
```shell
npx skills add crewaiinc/skills
```

## vs LangGraph

- CrewAI 完全独立构建，不依赖 LangChain
- 更轻量、高性能、低资源占用
- 同时支持 Crews（自主协作）和 Flows（精确控制）两种范式
- 社区认证开发者超 10 万

## 适用场景

- 内容创作流水线（Researcher → Writer → Reviewer）
- 市场分析与报告生成
- 代码审查与自动化开发
- 数据分析与洞察提取
- 任何需要多角色协作的复杂任务
