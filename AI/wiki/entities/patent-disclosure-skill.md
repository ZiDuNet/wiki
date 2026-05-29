---
type: entity
name: patent-disclosure-skill
created: 2026-05-29
updated: 2026-05-29
mentions: 1
github: handsomestWei/patent-disclosure-skill
stars: 716
---

# patent-disclosure-skill

**类型:** GitHub 工具实体
**GitHub:** handsomestWei/patent-disclosure-skill
**Star数:** 716 Star, 92 Fork
**协议:** MIT 开源

## 简介

中国专利.skill —— 从项目文档到可交付的技术交底书：专利点挖掘、查新优先国知局公布公告站、脱敏成文与自检闭环。

遵循 [[AgentSkills]] 规范，可无缝接入 [[Claude Code]]、[[Cursor]]、[[OpenClaw]] 等主流 AI 编码助手。

## 七大核心能力

1. **项目智能扫描** — 自动读取文档和代码，转 Markdown 再扫描
2. **专利点挖掘** — 自动识别潜在专利申请点
3. **国知局优先查新** — 优先爬取 [[CNIPA]]，降级到网络搜索
4. **标准化交底书生成** — 脱敏模板 + mermaid 图 + .docx 输出
5. **标准化交付命名** — `{案例名称}_{YYYYMMDDHHmmss}.md/.docx`
6. **自动自检** — 逻辑闭环/公式参数一致性检查
7. **多轮迭代支持** — 自动合并修正，维护修订对话记录

## 技术架构

```
patent-disclosure-skill/
├── SKILL.md              # 入口
├── prompts/              # 分步模板
├── tools/                # 工具集（含 cnipa_epub_search.py）
├── examples/             # 示例
├── outputs/              # 交付目录
└── requirements.txt      # Python 依赖
```

## 依赖管理

| 类型 | 文件 | 说明 |
|-----|------|------|
| 基础 | `requirements.txt` | Office 转换、交底书生成 |
| 查新（可选） | `tools/requirements-cnipa.txt` | 国知局爬虫（需 Playwright） |

## 安装方式

- **Claude Code**: 克隆到 `.claude/skills/` 目录
- **Cursor**: 放到 skills 路径，Settings → Rules 确认
- **详细说明**: 见项目 `INSTALL.md`

## 使用方式

自然语言触发：
- "帮我挖掘这个项目的专利点"
- "生成技术交底书"
- "查新对比专利"

斜杠命令：`/patent-disclosure-skill /交底书`

## 相关概念

- [[技术交底书自动化]]
- [[专利查新]]
- [[AI写作]]
- [[AgentSkills规范]]

## 相关实体

- [[CNIPA]] — 中国国家知识产权局
- [[Claude Code]]
- [[Cursor]]
- [[OpenClaw]]
- [[AgentSkills]]

## 来源文章

- [[ai帮我写专利交底书这个716星技能做到了]]

## 外部链接

- GitHub: https://github.com/handsomestWei/patent-disclosure-skill
- SkillHub: https://skillhub.cn/skills/patent-disclosure-skill