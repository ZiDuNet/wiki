> 📎 来源: [极客枫哥](https://mp.weixin.qq.com/s?__biz=Mzk0NDY4Mzk3Ng==&mid=2247485970&idx=1&sn=947dee2545c615eacde4e7eca50e3363&chksm=c297dd12dee8476127906c70d9e0f67ace35b0729aa8d1357afa0d855a201b74d151c2d9f4cb&mpshare=1&scene=1&srcid=04233yuDhZ2XVMMgm4kRGcjV&sharer_shareinfo=0e6ebd331b95d5b6f6aa347eaa0515ef&sharer_shareinfo_first=0e6ebd331b95d5b6f6aa347eaa0515ef) | 时间: 2026-04-23 04:30

---

![](assets/img_d144d87f85d6.png)

![](assets/img_07e20075ceac.png)

你好啊，我是枫哥～十年互联网程序员，懒癌患者，不定期分享效率工具，AI 编程，web 逆向等内容，期待与你进行交流

我装过 30+ 个 OpenClaw skill，最后每天真正在用的只有 10 个。其余那些，不是吃灰，就是添堵。

这篇不讲虚的，直接给你一份能落地的清单：**哪些必须装，哪些按需装，哪些先别碰。**

---

## 先说结论：如果你只装 3 个，就装这三个

- **wechat-article-export-skill**（公众号文章提取）
- **skill-feishu-docx-powerwrite**（飞书文档高质量写入）
- **material-inbox**（素材自动归档）

这三个组合起来，已经能覆盖大部分内容创作工作流。

## 第一梯队：必装（5 个）

### 1) wechat-article-export-skill

**一句话**：把公众号文章一键转 Markdown。**典型场景**：收藏、拆解、二次整理。**安装命令**：

```
skillhub install wechat-article-export-skill
```

**评分**：实用频率 9/10｜上手难度 2/10｜踩坑风险 3/10

**点评**：中国用户刚需。图片不下载，但文字提取很稳。

---

### 2) skill-feishu-docx-powerwrite

**一句话**：把内容写进飞书文档，而且格式不翻车。

**典型场景**：周报、方案、长文发布前整理。

**评分**：实用频率 9/10｜上手难度 4/10｜踩坑风险 4/10

**点评**：专治“Markdown 到飞书格式崩坏”。尤其是表格、长文分块写入这种坑。

---

### 3) material-inbox

**一句话**：你丢链接，它帮你提炼+分类+打标签+归档。

**典型场景**：素材库建设、知识管理。

**安装命令**：

```
skillhub install material-inbox
```

**评分**：实用频率 8/10｜上手难度 3/10｜踩坑风险 2/10

**点评**：省掉大量手工整理时间，长期收益很高。

---

### 4) thinking-archive

**一句话**：把你的想法和对话沉淀成可复用资产。

**典型场景**：复盘、长期知识积累、灵感库。

**安装命令**：

```
skillhub install thinking-archive
```

**评分**：实用频率 7/10｜上手难度 3/10｜踩坑风险 2/10

**点评**：适合认真做长期输出的人，短期不惊艳，长期很香。

---

### 5) multi-search-engine

**一句话**：一次查多个搜索源，减少信息偏差。

**典型场景**：研究、写作前调研、竞品资料。

**评分**：实用频率 8/10｜上手难度 2/10｜踩坑风险 2/10

**点评**：比单引擎靠谱，尤其在中英文混搜时。

---

## 第二梯队：推荐（3 个）

### 6) self-improvement

**一句话**：让 AI 记录错误、纠正和经验，避免重复踩坑。

**安装命令**：

```
skillhub install self-improving-agent
```

**评分**：实用频率 7/10｜上手难度 4/10｜踩坑风险 3/10

**点评**：这是“越用越聪明”的基础设施，不是花活。

---

### 7) humanizer

**一句话**：去 AI 味，把“模型腔”改成人话。

**安装命令**：

```
skillhub install humanizer
```

**评分**：实用频率 8/10｜上手难度 2/10｜踩坑风险 2/10

**点评**：做公众号/短内容创作时非常实用，能明显提升可读性。

---

### 8) wechat-mp-cn

**一句话**：公众号监控和追踪。

**评分**：实用频率 6/10｜上手难度 5/10｜踩坑风险 5/10

**点评**：有价值，但依赖链路多，容易被授权/API 问题影响。

---

## 第三梯队：按需（2 个）

### 9) summarize

**一句话**：长内容快速提要。

**评分**：实用频率 6/10｜上手难度 1/10｜踩坑风险 2/10

**点评**：适合先筛选再深读，省时间。

### 10) weather

**一句话**：天气查询工具。

**评分**：实用频率 3/10｜上手难度 1/10｜踩坑风险 1/10

**点评**：能用，但不是生产力核心。

---

## 三个高频工作流（可直接照抄）

### 工作流 A：公众号文章 → 飞书文档 → 素材库

- ```
  wechat-article-export-skill
  ```

   提取
- ```
  skill-feishu-docx-powerwrite
  ```

   写入飞书
- ```
  material-inbox
  ```

   归档打标签

### 工作流 B：搜索调研 → 摘要提炼 → 思考沉淀

- ```
  multi-search-engine
  ```

   搜集信息
- ```
  summarize
  ```

   快速提要
- ```
  thinking-archive
  ```

   沉淀观点

### 工作流 C：AI 初稿 → 去 AI 味 → 发布

- AI 生成初稿
- ```
  humanizer
  ```

   去模板腔
- 人工终审后发布

---

## 避坑清单（真的会踩）

- **别一开始装太多 skill**：先跑通 3 个核心再扩展。
- **别把关键流程绑死在单一 API**：今天可用，明天可能就配额归零。
- **别迷信“全自动”**：涉及发布内容，必须人工终审。

---

## 结尾

Skill 不在多，在于能不能进入你的日常工作流。你要是每天都在用，3 个 skill 也能打；你要是从来不打开，30 个也只是电子收藏夹。

---

## 附：一键安装（推荐清单）

```
# 必装skillhub install wechat-article-export-skillskillhub install material-inboxskillhub install thinking-archiveskillhub install self-improving-agentskillhub install humanizer
```

（

```
skill-feishu-docx-powerwrite
```

 和 

```
multi-search-engine
```

 通常已内置）

---

你把你现在的 skill 列表贴评论区，我帮你做一次“去冗余诊断”：哪些该删，哪些该装，顺便补一条最省事的工作流。

### 作者介绍

- 枫哥，90 后奶爸，十年互联网程序员。
- 一边带娃，一边研究效率工具、AI编程和逆向技术。
- 想聊技术、工具或AI应用，欢迎加我微信（备注：公众号）

![](assets/img_d5ad4917e612.webp)
