---
title: 朕不想做PPT，于是创造了大明PPT Agent Team
type: source-summary
tags: [PPT制作, Multi-Agent, 大明PPT, MiniMax, guizang-ppt-skill, TED演讲]
sources: [../微信公众号/Agent/朕不想做PPT，于是创造了大明PPT Agent Team.md]
created: 2026-05-19
updated: 2026-05-19
---

# 朕不想做PPT，于是创造了大明PPT Agent Team

> 来源：[[沃垠AI]] | 时间：2026-05-18

## 一句话摘要

作者冷逸借鉴明朝官僚体系，设计了一套「大明PPT Agent Team」Multi-Agent架构，在MiniMax Agent上实现高质量PPT自动生成，采用「内阁→锦衣卫→东厂→翰林院→工部→织造局」的角色分工流水线。

## 核心内容

### 架构灵感：大明官僚体系

作者从明史中获得灵感，用「大明官制」类比Multi-Agent协作：
- **皇帝（用户）**：最高统帅，对结果拥有一票否决权
- **内阁**：任务分配、进度监督、结果汇总（不执行）
- **锦衣卫**：深度研究（国之利器，"侦、捕、审、关"全链条）
- **东厂**：事实核查，制衡锦衣卫
- **翰林院**：PPT大纲设计（TED 3S原则：钩子→推进→高潮→落点）
- **工部**：配图生成
- **织造局**：HTML PPT输出

### 工作流程

```
下旨 → 深度研究 → 事实核查 → 大纲生成 → 配图生成 → HTML PPT输出
```

### 关键设计原则

1. **信源质量**：锦衣卫全网深度研究，4000字报告
2. **事实核查**：东厂打回锦衣卫重修多版才放过
3. **TED叙事**：翰林院按TED 3S原则设计故事线
4. **流程自动化**：皇帝只需确认，最终产出HTML PPT

### 技术栈

- **MiniMax Agent桌面版**：Agent Teams功能
- **guizang-ppt-skill**：PPT生成技能
- **GitHub开源**：https://github.com/woyin2024/lengyi-ppt-agent-team

### 使用方式

1. 下载MiniMax Agent桌面版（Windows/MacOS）
2. 订阅Token Plan（M2.7、音乐、视频、语音全包含）
3. 安装guizang-ppt-skill
4. 让MiniMax读取「[大明PPT御制流程.md](https://github.com/woyin2024/lengyi-ppt-agent-team/blob/main大明PPT御制流程.md)」组建Agent Team
5. 开始创作：「朕要做PPT，六部听旨」

## 关键实体

- [[MiniMax]] — Agent平台，提供桌面版和Token Plan
- [[guizang-ppt-skill]] — PPT生成开源Skill
- [[冷逸]] — 作者，明史爱好者
- [[沃垠AI]] — 内容发布公众号

## 关联概念

- [[Multi-Agent]] — 多智能体协作架构
- [[PPT制作]] — AI驱动的PPT生成
- [[TED演讲]] — 故事化演讲风格
- [[分阶段流程]] — 多步骤工作流编排
- [[事实核查]] — AI输出质量保障机制

## 标签

#PPT制作 #Multi-Agent #大明PPT #MiniMax #guizang-ppt-skill #TED演讲
