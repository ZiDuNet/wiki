---
type: concept
created: 2026-05-26
updated: 2026-05-26
---

# Token成本优化

通过技术手段降低 AI 对话和任务执行中的 Token 消耗。

## 核心策略

- **前缀缓存优先**：围绕缓存稳定性设计对话循环，不是"碰巧命中缓存"而是"每一轮围绕缓存稳定性设计"
- **上下文压缩**：长会话中主动压缩无关上下文，保持核心信息密度
- **深度模型绑定**：专为一类模型做深度优化，而非追求跨模型通用性（"绑死一个后端是 feature"）
- **工具调用自动修复**：模型输出格式错误时自动修复，避免浪费一轮重试
- **成本透明**：明确量化每轮 Token 消耗和缓存命中率

## 典型案例

- **DeepSeek-Reasonix**：专门为 DeepSeek 前缀缓存做工程化优化，缓存命中率 99.82%，Token 成本再降 80%
- **Aider**：偶发缓存命中，非设计目标
- **Claude Code**：闭源 Anthropic 模型，不适用 DeepSeek 缓存机制

## 相关文章

- [[deepseek-reasonix-爆火开源-deepseek-原生的终端-ai-编程agent]] — 前缀缓存优先循环，Token 成本比 Claude Code 少约 60%

## 来源

- [[deepseek-reasonix-爆火开源-deepseek-原生的终端-ai-编程agent]]