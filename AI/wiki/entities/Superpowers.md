---
type: project
created: 2026-05-10
updated: 2026-05-10
---

# Superpowers

**Type:** project
**Description:** Jesse Vincent 的软件工程最佳实践 Skills 框架

## Related Entities

[[Claude-Code]] [[baoyu-skills]] [[Anthropic]] [[OpenAI]] [[GitHub]] [[OpenClaw]] [[MiniMax]] [[Remotion]]

## Related Concepts

[[Skill设计模式]] [[Harness-Engineering]] [[Skill编排]] [[Agent开发]] [[PPT制作]] [[AI编程]]

## Mentioned In

- [[Skills商店来了：5w+人在用的热门Skills，我试了一遍]] — 你有没有这种感觉。别人和AI聊几句就能搞定一件事，你折腾半天出来的结果却总是差点意思。不是AI不行，是你没给它配上“武器库”。
- [[Superpowers：把软件工程最佳实践封装成AI可执行的技能]] — Test-Driven Development**铁律：没有失败的测试，就不能写产品代码。**## 流程### RED 阶段写一个**失败的测试**，验证：- 测试失败原因正确- 测试的是正确的行为### GREEN 阶段写**最小代码**让测试通过，验证：- 所有测试通过- 没有为了通过测试而写的多余代码### REFACTOR 阶段在测试保护下重构清理，然后回到 RED 继续下一个行为。## 技术细节### 测试先行原则如果用户说"先写代码再加测试"：1. 告诉他们这是不允许的2. 如果代码已存在，删除它3. 从测试重新开始**你不能"保留参考"代码，不能"边写测试边调整"。**必须亲眼看到测试失败，才能确认测试的是正确的东西。### 验证失败必须正确RED 阶段不仅要"测试失败"，还要确认：- 失败原因是你期望的- 不是因为测试写错了如果测试错误地通过了，这不是好的 RED。
- [[最值得产品经理装的10个skills]] — 最值得产品经理装的10个skills
- [[论文写作-Skills-整理]] — 1. 创建技能目录mkdir -p ~/.claude/skills# 2. 安装核心技能cd ~/.claude/skills# luwill/research-skillsgit clone https://github.com/luwill/research-skills.gitcp -r research-skills/research-proposal .cp -r research-skills/paper-slide-deck .cp -r research-skills/medical-imaging-review .# lishix520/academic-paper-skillsgit clone https://github.com/lishix520/academic-paper-skills.gitcp -r academic-paper-skills/strategist .cp -r academic-paper-skills/composer .# K-Dense-AI/claude-scientific-skillsgit clone https://github.com/K-Dense-AI/claude-scientific-skills.gitcp -r claude-scientific-skills/scientific-skills/scientific-writing .# ndpvt-web/latex-document-skillgit clone https://github.com/ndpvt-web/latex-document-skill.gitcp -r latex-document-skill/skills/* .# 清理rm -rf research-skills academic-paper-skills claude-scientific-skills latex-document-skill
