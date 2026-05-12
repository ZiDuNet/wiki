> 📎 来源: [阳哥书房](https://mp.weixin.qq.com/s?__biz=MzI2NjY5NzI0NA==&mid=2247517062&idx=1&sn=b41a00fc90da0a9a616528368022532f&chksm=ebf51d14e888d61141d9c00a8423d3772bf7571b4715cfb3449a37ecc35d32048ca986abbce2&mpshare=1&scene=1&srcid=0423oSSIjpazqXK3t903aILi&sharer_shareinfo=6b27200dd57d8d1d60dc0a66567867aa&sharer_shareinfo_first=6b27200dd57d8d1d60dc0a66567867aa) | 时间: 2026-04-23 23:58

---

今年准备要论文了，整理了下论文写作相关的 Skills，希望能用得上。

以下都是来源于网络的信息，目前还没有一一验证，大家自行挖掘哈。

## 01📊 执行摘要

经过全面搜索，发现 **12 个高质量论文写作相关 Skills**，涵盖学术论文规划、写作、文献综述、LaTeX 排版等完整流程。

**关键发现**:

- ⭐ **最受欢迎**: K-Dense-AI/claude-scientific-skills (8,799 stars)
- 🎯 **最相关**: lishix520/academic-paper-skills (专为学术论文设计)
- 🔬 **最强功能**: luwill/research-skills (含研究提案生成)

---

## 02🏆 Top 推荐 Skills

### 🥇 第一梯队: 直接可用

#### 1. **academic-paper-skills** ⭐⭐⭐⭐⭐

- **作者**: lishix520
- **Stars**: 22
- **GitHub**: https://github.com/lishix520/academic-paper-skills
- **描述**: 系统化的学术论文规划和写作框架
- **特点**:

- ✅ 双技能工作流 (Strategist + Composer)
- ✅ 7维度审稿人模拟系统
- ✅ 质量检查点 (3 validation gates)
- ✅ 支持 PhilArchive、arXiv 等预印本平台
- ✅ 包含 Python 验证脚本

- **适用场景**: 哲学、跨学科、人文社科类学术论文
- **适配度**: ⭐⭐⭐⭐ (可适配商业伦理、管理哲学等方向)

**核心工作流**:

```
Strategist (规划):  Phase 1: 平台分析 → 目标期刊 + 风格指南  Phase 2: 理论框架 → 文献 + 研究缺口分析  Phase 3: 大纲优化 → 审稿人评估大纲Composer (写作):  Phase 1: 基础搭建 → 风格指南 + 章节规划  Phase 2: 系统写作 → 带质量检查的草稿  Phase 3: 润色 → 最终评估 + 投稿准备
```

---

#### 2. **research-skills** ⭐⭐⭐⭐⭐

- **作者**: luwill
- **Stars**: 209
- **GitHub**: https://github.com/luwill/research-skills
- **描述**: 学术研究工作流技能集合
- **特点**:

- ✅ 3 个核心技能
- ✅ 医学影像综述写作 (7 阶段工作流)
- ✅ **研究提案生成** (最相关 MBA!)
- ✅ 论文转幻灯片 (自动图表提取)
- ✅ Nature Reviews 风格写作
- ✅ 双语支持 (中英文)
- ✅ Zotero/arXiv/PubMed 集成

- **适配度**: ⭐⭐⭐⭐⭐ (research-proposal 直接适配!)

**核心技能详解**:

**① research-proposal** :

- **触发词**: 

  ```
  /research-proposal
  ```

  , "研究计划", "PhD proposal"
- **功能**: 生成 2,000-4,000 字高质量研究提案
- **工作流**:

1. 需求收集 (主题、领域、语言、字数)
2. 多源文献收集 (WebSearch、Zotero、arXiv、PubMed)
3. 大纲生成 (用户审核)
4. 完整写作 (基于批准的大纲)
5. Markdown 输出 + 质量检查清单

- **要求**: 最少 40 篇参考文献, 3-5 个图表建议

**② medical-imaging-review**:

- 7 阶段综述写作工作流
- 领域特定模板 (心脏、肺部、脑部、病理等)
- 标准化写作风格 (模糊语言 + 引文模式)
- Zotero 集成

**③ paper-slide-deck**:

- 论文转幻灯片 (自动检测图表)
- 17 种视觉风格
- AI 图片生成 (Gemini API)
- PPTX/PDF 导出

---

### 🥈 第二梯队: 科学研究全能

#### 3. **claude-scientific-skills** ⭐⭐⭐⭐⭐

- **作者**: K-Dense-AI
- **Stars**: 8,799
- **GitHub**: https://github.com/K-Dense-AI/claude-scientific-skills
- **描述**: **140+ 科学技能**的巨型集合
- **特点**:

- ✅ 140+ 即用型科学技能
- ✅ 覆盖生物信息、化学、医学、AI 等
- ✅ 28+ 科学数据库 (OpenAlex、PubMed、ChEMBL、UniProt)
- ✅ 55+ Python 包 (RDKit、Scanpy、PyTorch、scikit-learn)
- ✅ 20+ 科学沟通技能
- ✅ **包含 scientific-writing 技能**

- **安装**: 

  ```
  npx skills add https://github.com/K-Dense-AI/claude-scientific-skills --skill scientific-writing
  ```

**相关的技能**:

- **scientific-writing**: 深度研究 + 学术写作 (核心技能!)
- **literature-review**: 文献综述系统化流程
- **hypothesis-generation**: 假设生成
- **research-grants**: 基金/提案写作
- **statistical-analysis**: 统计分析 (数据分析必备)
- **presentation-skills**: 学术汇报

---

#### 4. **claude-scientific-writer** ⭐⭐⭐⭐

- **作者**: K-Dense-AI
- **Stars**: 794
- **GitHub**: https://github.com/K-Dense-AI/claude-scientific-writer
- **描述**: 通用科学写作工具
- **特点**:

- ✅ AI 驱动的深度研究
- ✅ 格式化输出 (LaTeX、Markdown)
- ✅ 每篇文档都有全面的引文支持
- ✅ K-Dense Web 版本有更强大的功能

- **适用**: 科学论文、报告、学位论文

---

### 🥉 第三梯队: 文献研究

#### 5. **research-superpower** ⭐⭐⭐⭐

- **作者**: kthorn
- **Stars**: 6
- **GitHub**: https://github.com/kthorn/research-superpower
- **描述**: 文献搜索和综述超级技能
- **特点**:

- ✅ PubMed + Semantic Scholar 集成
- ✅ 智能论文筛选 (摘要评分 + 深度挖掘)
- ✅ 引文遍历 (前向 + 后向)
- ✅ ChEMBL 数据库 (药物化学)
- ✅ Unpaywall 集成 (找免费全文)
- ✅ 大规模筛选 (50+ 论文并行处理)

- **适用场景**: **文献综述**

**工作流**:

1. 解析文献问题
2. 构建筛选标准
3. 搜索 PubMed
4. 筛选摘要 (0-10 分)
5. 深度挖掘相关论文
6. 遍历引文
7. 综合发现 (SUMMARY.md)

---

#### 6. **stats-paper-writing-agent-skills** ⭐⭐⭐

- **作者**: fuhaoda
- **Stars**: 4
- **GitHub**: https://github.com/fuhaoda/stats-paper-writing-agent-skills
- **描述**: LaTeX 统计论文写作
- **特点**:

- ✅ 前端部分草稿 (标题、作者、摘要)
- ✅ LaTeX 模板
- ✅ 统计分析支持

- **适用**: 统计学、计量经济学论文

---

#### 7. **AI-Research-SKILLs** ⭐⭐⭐⭐

- **作者**: Orchestra-Research
- **Stars**: 3,637
- **GitHub**: https://github.com/Orchestra-Research/AI-Research-SKILLs
- **描述**: AI 研究和工程综合技能库
- **特点**:

- ✅ LaTeX (59.1%)、BibTeX (21.3%)、JavaScript (11.1%)
- ✅ 20-ml-paper-writing 技能 (ML 论文写作)
- ✅ Top 会议论文起草
- ✅ 引文验证
- ✅ LaTeX 模板

- **安装**: 

  ```
  npx playbooks add skill orchestra-research/ai-research-skills --skill 20-ml-paper-writing
  ```

---

## 03🔧 其他辅助 Skills

### LaTeX 文档处理

#### 8. **latex-document-skill**

- **作者**: ndpvt-web
- **Stars**: 74
- **GitHub**: https://github.com/ndpvt-web/latex-document-skill
- **特点**:

- ✅ 27 个模板
- ✅ 22 个脚本
- ✅ 22 个参考指南
- ✅ 手写笔记 → LaTeX 自动转换

---

### 写作辅助

#### 9. **writing-plans**

- **作者**: obra/superpowers
- **描述**: 写作规划技能

#### 10. **copywriting**

- **作者**: coreyhaines31/marketingskills
- **Stars**: 17,000+
- **描述**: 营销文案写作

---

### 办公文档

#### 11. **claude-office-skills**

- **作者**: tfriedel
- **Stars**: 251
- **GitHub**: https://github.com/tfriedel/claude-office-skills
- **描述**: PPTX、DOCX、XLSX、PDF 工作流
- **适用**: 生成演示文稿、Word 文档

---

### 文档处理

#### 12. **pdf**, **docx**, **xlsx**, **pptx**

- **作者**: anthropics/skills
- **描述**: 官方文档处理技能
- **适用**: 论文格式转换、数据处理

## 04🎯 按论文阶段推荐

### 阶段 1: 开题报告

**最佳选择**: 

```
luwill/research-skills/research-proposal
```

- ✅ 专为研究提案设计
- ✅ Nature Reviews 风格
- ✅ 双语支持
- ✅ 40+ 参考文献
- **安装**:

  ```
  git clone https://github.com/luwill/research-skills.gitcp -r research-skills/research-proposal ~/.claude/skills/
  ```

---

### 阶段 2: 文献综述

**最佳选择**: 

```
kthorn/research-superpower
```

- ✅ PubMed/Semantic Scholar 集成
- ✅ 智能筛选 + 引文遍历
- ✅ 大规模处理 (50+ 论文)
- **安装**:

  ```
  /plugin marketplace add https://github.com/kthorn/research-superpower/plugin install research-superpowers@research-superpowers-marketplace
  ```

**备选**: 

```
K-Dense-AI/claude-scientific-skills/literature-review
```

---

### 阶段 3: 理论框架与研究设计

**最佳选择**: 

```
lishix520/academic-paper-skills/strategist
```

- ✅ 理论框架构建
- ✅ 文献缺口分析 (3-5 引文支持)
- ✅ 7 维度审稿人评估

---

### 阶段 4: 数据收集与分析

**推荐组合**:

1. ```
   xlsx
   ```

    - 数据处理
2. ```
   K-Dense-AI/claude-scientific-skills/statistical-analysis
   ```

    - 统计分析
3. 本地 

   ```
   deep-research
   ```

    - 验证数据来源

---

### 阶段 5: 论文写作

**最佳选择**: 

```
lishix520/academic-paper-skills/composer
```

- ✅ 系统化写作流程
- ✅ 质量检查点
- ✅ 章节指导

**备选**: 

```
K-Dense-AI/claude-scientific-writer
```

---

### 阶段 6: 格式化与排版

**最佳选择**: 

```
ndpvt-web/latex-document-skill
```

- ✅ 27 个 LaTeX 模板
- ✅ 自动格式化

**备选**: 

```
tfriedel/claude-office-skills
```

 (Word/PPT)

---

### 阶段 7: 答辩准备

**推荐**: 

```
luwill/research-skills/paper-slide-deck
```

- ✅ 论文转幻灯片
- ✅ 自动图表提取
- ✅ 17 种视觉风格

---

## 05📦 安装指南

### 全局安装 (推荐)

```
# 1. 创建技能目录mkdir -p ~/.claude/skills# 2. 安装核心技能cd ~/.claude/skills# luwill/research-skillsgit clone https://github.com/luwill/research-skills.gitcp -r research-skills/research-proposal .cp -r research-skills/paper-slide-deck .cp -r research-skills/medical-imaging-review .# lishix520/academic-paper-skillsgit clone https://github.com/lishix520/academic-paper-skills.gitcp -r academic-paper-skills/strategist .cp -r academic-paper-skills/composer .# K-Dense-AI/claude-scientific-skillsgit clone https://github.com/K-Dense-AI/claude-scientific-skills.gitcp -r claude-scientific-skills/scientific-skills/scientific-writing .# ndpvt-web/latex-document-skillgit clone https://github.com/ndpvt-web/latex-document-skill.gitcp -r latex-document-skill/skills/* .# 清理rm -rf research-skills academic-paper-skills claude-scientific-skills latex-document-skill
```

### 使用 npx skills (最简单)

```
# K-Dense Scientific Skillsnpx skills add https://github.com/K-Dense-AI/claude-scientific-skills --skill scientific-writing# Orchestra Research Skillsnpx skills add orchestra-research/ai-research-skills --skill 20-ml-paper-writing
```

### 从 Marketplace 安装

```
# kthorn/research-superpower/plugin marketplace add https://github.com/kthorn/research-superpower/plugin install research-superpowers@research-superpowers-marketplace
```

---

## 06💡 使用示例

### 示例 1: 生成开题报告

```
使用 research-proposal skill我想写一篇关于"数字化转型对企业绩效影响"的 MBA 论文开题报告。领域: 管理学语言: 中文字数: 3000字左右
```

**输出**:

- 3,000 字左右的研究提案
- 40+ 参考文献
- 3-5 个研究图表建议
- Markdown 格式 (可转 Word/PDF)

---

### 示例 2: 文献综述

```
使用 research-superpowers帮我找关于"数字化转型"和"企业绩效"相关的学术论文,重点关注:1. 实证研究 (有数据分析)2. 近5年发表3. 有明确的研究框架4. 提供 IC50、p-value 等统计数据
```

**输出**:

- research-sessions/YYYY-MM-DD-query/ ├── SUMMARY.md (按相关性组织) ├── papers-reviewed.json (去重追踪) ├── papers/ (PDF 全文) └── citations/ (引文关系图)

---

### 示例 3: 完整论文写作

```
使用 academic-paper-composer根据这个大纲写论文:[你的大纲]目标期刊: 《管理世界》风格: 学术规范、定量研究
```

---

## 07🔗 技能对比表

| 技能 | Stars | 主要功能 | MBA 适配 | 安装难度 |
| --- | --- | --- | --- | --- |
| **luwill/research-skills** | 209 | 开题报告、综述、幻灯片 | ⭐⭐⭐⭐⭐ | 简单 |
| **lishix520/academic-paper-skills** | 22 | 论文规划 + 写作 | ⭐⭐⭐⭐ | 简单 |
| **K-Dense-AI/claude-scientific-skills** | 8,799 | 140+ 科学技能 | ⭐⭐⭐⭐ | 简单 |
| **kthorn/research-superpower** | 6 | 文献搜索 + 综述 | ⭐⭐⭐⭐ | 中等 |
| **fuhaoda/stats-paper-writing** | 4 | 统计论文 LaTeX | ⭐⭐⭐ | 简单 |
| **Orchestra-Research/AI-Research-SKILLs** | 3,637 | ML 论文写作 | ⭐⭐⭐ | 中等 |
| **ndpvt-web/latex-document-skill** | 74 | LaTeX 文档 | ⭐⭐⭐⭐ | 简单 |

---

## 08🎓 针对不同 MBA 方向的推荐

### 管理学/工商管理

1. **luwill/research-skills** (research-proposal)
2. **lishix520/academic-paper-skills**
3. **kthorn/research-superpower** (文献综述)

### 金融/投资

1. 本地 **stock-analysis** skill
2. **K-Dense-AI/claude-scientific-skills** (statistical-analysis)
3. **xlsx** skill (数据建模)

### 市场营销

1. 本地 **write-common-article** skill (需调整风格)
2. **coreyhaines31/marketingskills** (copywriting, marketing-psychology)
3. **luwill/research-skills** (research-proposal)

### 数据分析/商业智能

1. **K-Dense-AI/claude-scientific-skills** (全套)
2. **xlsx** skill
3. 本地 **deep-research** skill

### 战略管理

1. **lishix520/academic-paper-skills** (框架构建)
2. **luwill/research-skills** (research-proposal)
3. 本地 **corporate-analysis-suite** skills

---

## 09🚀 快速上手指南

### 最简方案 (3 步搞定)

#### 步骤 1: 安装核心技能

```
mkdir -p ~/.claude/skillscd ~/.claude/skills# 开题报告git clone https://github.com/luwill/research-skills.git tempcp -r temp/research-proposal .rm -rf temp# 科学写作npx skills add https://github.com/K-Dense-AI/claude-scientific-skills --skill scientific-writing
```

#### 步骤 2: 重启 Claude Code

```
# 退出并重新打开 Claude Code
```

#### 步骤 3: 开始写作

```
使用 research-proposal skill我想写 MBA 论文开题报告,主题是...
```

---

## 010📚 学习资源

### GitHub 仓库

- **Awesome Claude Skills**: https://github.com/travisvn/awesome-claude-skills
- **Claude Official Skills**: https://github.com/anthropics/skills
- **Skills.sh 市场**: https://skills.sh/

### 官方文档

- **Agent Skills 标准**: https://agentskills.io/
- **Claude Code 文档**: https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills
- **32 页完整指南**: https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf

### 社区资源

- **Reddit r/ClaudeCode**: https://www.reddit.com/r/ClaudeCode/
- **LinkedIn 技能讨论**: 搜索 "Claude Skills"
