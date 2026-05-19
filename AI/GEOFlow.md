# GEOFlow - 开源 GEO 智能内容工程系统

> **一句话介绍**：面向 GEO（生成式引擎优化）的开源智能内容生产系统，覆盖数据沉淀、知识库、素材管理、AI 生成、审核发布、前台展示与多端分发的完整链路。

## 基本信息

| 项目 | 详情 |
|------|------|
| GitHub | https://github.com/yaojingang/GEOFlow |
| Stars | 1643 ⭐ |
| Forks | 366 |
| 语言 | PHP 8.2+ (Laravel) |
| 协议 | Apache-2.0 |
| 创建时间 | 2026-04-13 |
| 最近更新 | 2026-05-19 |
| Tags | ai, cms, content-automation, geo, openai-compatible, php, postgresql, seo |
| 同作者项目 | [yao-geo-skills](https://github.com/yaojingang/yao-geo-skills) (⭐173) - GEO 内容与工作流 Skill 合集 |

## 系统定位

GEOFlow 是全球最早围绕 GEO 场景系统化设计的数据、内容与分发基础设施之一。它把"从数据到内容、从内容到多端发布"串联为一条可持续迭代的工作链路。

**GEO ≠ SEO**：
- SEO 优化搜索排名，获取点击
- GEO 优化内容让 AI 搜索引擎（ChatGPT、Perplexity、Gemini、DeepSeek 等）理解、引用、推荐

## 核心功能

### 1. 多模型内容生成
- 兼容 OpenAI 风格接口
- 支持智谱、火山方舟等非 `/v1` 路径的国产模型
- 智能模型切换与失败重试
- 支持 chat / embedding 模型类型

### 2. 批量任务调度
- 任务创建、文章总数与发布节奏控制
- 队列执行、失败记录与任务文章筛选
- 可选 Laravel Horizon 监控

### 3. 素材统一管理
- 标题库、关键词库、图片库、作者库
- 知识库、提示词集中管理

### 4. 知识库 RAG
- 上传后自动切片
- 配置 embedding 模型后写入 pgvector 向量数据库
- 生成时召回相关片段增强内容质量

### 5. 审核与发布工作流
- 草稿 → 审核 → 发布全流程
- 可配置自动发布
- 文章管理支持状态、作者、任务等筛选

### 6. 搜索展示优化
- 文章 SEO 元信息
- Open Graph 标签
- 结构化数据（JSON-LD）
- 前台 Markdown 支持 GFM 渲染（标题、表格、列表、图片）

### 7. 前台与主题系统
- 默认主题、主题包
- 预览路径、后台主题切换
- 站点名称仅影响前台，后台品牌固定为 GEOFlow

### 8. 多语言后台
- 中文、英文、日语、西班牙语、俄语、葡萄牙语（巴西）

### 9. 其他
- 版本更新提醒（对接 GitHub release）
- 管理员登录失败锁定（5次）
- WebSocket 支持（Laravel Reverb）

## 系统架构

```
后台管理页面
    ↓
任务调度器 / 队列（Horizon 可选）
    ↓
Worker 执行 AI 生成
    ↓
草稿 / 审核 / 发布
    ↓
前台文章与 SEO 页面输出
```

| 层级 | 技术 |
|------|------|
| Web / Admin | Laravel 路由与控制器；Blade 模板 |
| API | routes/api.php 等 HTTP 接口 |
| Scheduler / Queue | Laravel Scheduler + queue:work / Horizon + Reverb |
| Domain & Jobs | app/Services、app/Jobs、app/Http/Controllers |
| 数据库 | PostgreSQL（推荐 pgvector）+ Redis |

## 技术栈

| 组件 | 版本/说明 |
|------|-----------|
| PHP | 8.2+（Docker 镜像可用 8.4） |
| 框架 | Laravel |
| 数据库 | PostgreSQL 16 + pgvector |
| 缓存/队列 | Redis 7 |
| 向量搜索 | pgvector（embedding 存储） |
| 容器化 | Docker Compose |
| 队列监控 | Laravel Horizon（可选） |
| WebSocket | Laravel Reverb（按需启用） |
| 前端 | Blade + TailwindCSS |

## 部署方式

### Docker 一键部署（推荐）
```bash
git clone https://github.com/yaojingang/GEOFlow.git
cd GEOFlow
cp .env.example .env
docker compose build
docker compose up -d
```

Docker Compose 包含 7 个服务：postgres、redis、init、app、queue、scheduler、reverb

- 前台：`http://localhost:18080`
- 后台：`http://localhost:18080/geo_admin/login`

### 生产部署
```bash
# 使用 docker-compose.prod.yml（Nginx + PHP-FPM）
docker compose --env-file .env.prod -f docker-compose.prod.yml build
docker compose --env-file .env.prod -f docker-compose.prod.yml up -d
```

### 一键部署脚本
```bash
curl -fsSL https://raw.githubusercontent.com/yaojingang/GEOFlow/main/deploy-scripts/geoflow-docker-deploy.sh -o geoflow-docker-deploy.sh
bash geoflow-docker-deploy.sh
```

## 核心工作流

1. 配置 API：添加 chat 模型 + embedding 模型
2. 配置素材库：知识库、标题库、关键词库、图片库、作者
3. 新建任务：选择标题库、素材、模型、生成数量和发布频率
4. Worker 生成文章，进入草稿/审核/发布链路
5. 前台输出文章与 SEO 页面

## 适用场景

| 场景 | 说明 |
|------|------|
| 独立 GEO 官网 | 官网做成 AI 搜索友好型内容资产 |
| 官网 GEO 子频道 | 独立资讯/知识/解决方案频道 |
| 独立 GEO 信源站 | 行业/主题内容站点 |
| 内部 GEO CMS | 统一管理模型、素材、审核和发布 |
| 多站点部署 | 多个品牌频道、主题站管理 |
| 自动化信源管理 | 知识库+内容工程化分发 |

## 目录结构（关键部分）

```
GEOFlow/
├── app/
│   ├── Http/Controllers/   # 控制器
│   ├── Services/           # 业务逻辑
│   └── Jobs/               # 队列任务
├── routes/
│   └── api.php             # API 路由
├── resources/
│   └── views/              # Blade 模板
├── docker/                 # Docker 配置
├── public/                 # 网站根目录
├── .agents/skills/         # Agent 技能（AI SDK、Horizon、Laravel 最佳实践等）
└── .claude/skills/         # Claude Code 技能
```

## 项目亮点

1. **完整的 GEO 内容工程链路**：从数据到内容到分发，不是简单的 CMS
2. **RAG 知识库**：基于 pgvector 的向量检索，内容生成质量高
3. **多模型兼容**：不绑定单一 LLM 提供商
4. **生产就绪**：Docker Compose 一键部署，Nginx+PHP-FPM 生产配置
5. **内置 Agent Skills**：项目自带 .agents/skills 和 .claude/skills，支持 AI 辅助开发
6. **Apache 2.0 协议**：可自由商用

## 同类项目对比

| 项目 | Stars | 定位 | 技术栈 |
|------|-------|------|--------|
| **GEOFlow** | 1643 | 完整 GEO 内容生产系统 | PHP/Laravel |
| AutoGEO | 148 | 学术论文，自动 GEO 策略学习 | Python |
| geo-optimizer-skill | 427 | 网站审计+优化评分 | Python |
| GetCito | 114 | 开源 AIO/AEO/GEO 工具 | TypeScript |
| gego | 61 | 跨 LLM 品牌可见度追踪 | Go |
| eGEOagents | 108 | AI Agent GEO 技能集 | Python |
| geo-optimizer | 118 | 可插拔 GEO 优化框架 | Go |
