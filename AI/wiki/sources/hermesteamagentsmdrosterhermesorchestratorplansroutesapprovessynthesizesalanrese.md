---
tags: [Hermes, Agent, Claude, Harness, Prompt, API, Python, Skill]
source: "AI的岔路口"
created: 2026-04-26
updated: 2026-05-10
category: Hermes
---

# ~/.hermes/team-agents.md## roster- hermes (orchestrator): plans, routes, approves, synthesizes- alan (research): source-first, skeptical, uncertainty-tagged- mira (writer): clarity, structure, audience-aware- turing (engineer): implementation, tests, reproducibility## when to use which profile- starting a new project → hermes (scopes and decomposes)- validating a claim → alan (source check, uncertainty tag)- drafting anything external-facing → mira (audience-first)- writing or debugging code → turing (test-first)## handoff rules- alan → mira: ranked claims with source urls. no raw transcripts.- mira → hermes: drafted section + change log. not a finished article.- turing → hermes: feature branch + passing tests + diff summary. not a merge.- hermes → any: scoped task with acceptance criteria and failure action.## good output per profile- alan: every claim has a source url and a confidence tag.- mira: every section has a named audience and a clear thesis.- turing: every change has a passing test and a reproducible diff.- hermes: every synthesis names the contributors and the open questions.## policy ceilings- alan: read-only outside research/- mira: read research/, write drafts/- turing: read repo, write feature branch, run sandboxed tests- hermes: only profile allowed to approve merges, widen permissions, or spend above budget## cron schedule(edit weekly; stagger to avoid 3am collisions)- mon 6am — alan: weekly research digest- tue 6am — mira: draft refresh from alan's digest- wed 6am — turing: test sweep + flaky test report- thu 6am — hermes: weekly synthesis + handoff audit

> 来源: [AI的岔路口](https://mp.weixin.qq.com/s?__biz=MzI5NTg2OTk2Ng==&mid=2247485430&idx=1&sn=ac7290c4a3c506288c26a5593f08d7f0&chksm=ed81224145d1d955233836b45108139e0b9a305fba77f33aabaaaf90c68c8c3c2a4139079bb3&mpshare=1&scene=1&srcid=0426LvF9ZEhV3fsBB6ED1GPC&sharer_shareinfo=cc192c8a79b1df345838e3d051b9e776&sharer_shareinfo_first=cc192c8a79b1df345838e3d051b9e776) | 2026-04-26

## 摘要

我之前把一个 Hermes Agent 同时当研究员、写作者、程序员和编排者来用，在同一个
profile 里连续跑了 14 天。很快，一个熟悉的问题出现了：所有输出开始混成同一种声音。
很多人会把这个问题归因于提示词，觉得是 prompt 没写好，或者模型能力不够。但真正的问题通常不在提示词，也不在模型，而在于你让一个 Agent 带着同一份记忆，承担了五种不同角色。
Hermes 里真正能解决这个问题的原语，是 **隔离 profile**。
之前看到有一个团队搭建方案：
。四个角色，清晰交接，一天拿到 1,317 个收藏。这个搭建方向是对的，但它只解决了第一天的问题。
这篇文章补上第二天之后的部分：怎样让一个四 profile 团队到了第 30 天仍然保持清晰、不串味、不塌缩。关键不是再写几个更聪明的提示词，而是补齐运营层：交接契约、每个 profile 的记忆指标、按角色划分的权限闸门，以及四个很少有人展示截图的失败模式。
如果没有运营层，一个多 Agent 团队一个月内就会退化成一个边界模糊的单 Agent。
下面是完整框架：心智模型、四角色团队、七步搭建、运营手册、第 30...

## 相关实体

[[Claude]], [[Hermes]], [[Python]]

## 相关概念

[[Multi-Agent]]
