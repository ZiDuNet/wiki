---
type: concept
name: Harness
created: 2026-05-28
updated: 2026-05-28
tags: [Harness, 工作流调度, Agent编排]
sources: [[Claude-code使用笔记怎样用MCPSkillHarness搭建一个AI公司]]
---

# Harness

**类型:** 概念

## 定义

AI 工作流调度器，类比项目经理。不亲自干活，但掌控全局：谁干什么、什么顺序、出了问题怎么处理。

## 四大能力

| 能力 | 说明 |
|-----|------|
| 条件判断 | 不达标自动重试，重试三次才问人 |
| 上下文传递 | Step 1 输出自动作为 Step 3 输入 |
| 并行调度 | 配音生成和素材筛选同时跑 |
| 错误恢复 | MCP 超时自动重试，不崩流程 |

## 视频制作 Harness 示例

```
Step 1 → script-writing-skill（写口播文案）
Step 2 → 判断：文案是否达标？不达标→重试
Step 3 → shot-breakdown-skill（拆镜头）
Step 4 → filesystem-mcp（读素材）
Step 5 → tts-mcp（合成配音）
Step 6 → remotion-mcp（渲染视频）
Step 7 → browser-mcp（上传后台）
Step 8 → 记录数据到飞书
```

## 配置位置

`.claude/harness/` 目录下，每个复杂流程一个配置文件。

## 相关文章

- [[Claude-code使用笔记怎样用MCPSkillHarness搭建一个AI公司]]

## 相关概念

- [[Skill系统]]
- [[MCP]]
- [[AI操作系统]]