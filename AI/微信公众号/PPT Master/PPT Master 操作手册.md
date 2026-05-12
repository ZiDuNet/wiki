> 📎 来源: [一豪同学](https://mp.weixin.qq.com/s?__biz=MzkzOTI0NjYxOA==&mid=2247484107&idx=1&sn=5625ee33cb8cd23ed160c7dddcf83dd6&chksm=c3c7b1de4d815396bdfa31ab8ac9fb0ef52375cdf50f37236d080387ca0c9234186f0faa2231&mpshare=1&scene=1&srcid=0509kL5NK23MkkkGGY7WCQwh&sharer_shareinfo=80167b806b2f011ab2ca567e5912b3c4&sharer_shareinfo_first=80167b806b2f011ab2ca567e5912b3c4) | 时间: 2026-05-09 15:23

---

# PPT Master 操作手册

> AI 驱动的多格式 SVG 内容生成系统，将源文档（PDF/DOCX/URL/Markdown）通过多角色协作转换为高质量 PPTX 演示文稿。

---

## 目录

1. 快速开始
2. 环境准备
3. 完整工作流
4. 源文档转换
5. 项目初始化
6. 设计策划阶段
7. 图片获取阶段
8. SVG 生成阶段
9. 后处理与导出
10. 常用命令速查
11. 画布格式选择
12. 图片生成
13. 常见问题

---

## 1. 快速开始

### 1.1 最简路径（推荐新用户）

在 Claude Code 中直接输入需求即可触发全流程：

```
帮我做一个关于 XXX 的PPT
```

或提供源文件：

```
把这份文档转换成PPT：<路径到文件
```

Claude Code 会自动执行：源文档处理 → 项目创建 → 设计确认 → SVG 生成 → PPTX 导出。

### 1.2 完整路径（手动控制）

适合需要精细控制每个步骤的场景，按 第 3 节 逐步执行。

---

## 2. 环境准备

### 2.1 Python 依赖

```
pip install -r "C:/Users/matebook 14/.claude/skills/ppt-master/requirements.txt"
```

核心依赖包括：

- `python-pptx`

  — PPTX 文件生成
- `CairoSVG`

  或 `svglib` — SVG 转 PNG（Office 兼容）
- `PyMuPDF`

  — PDF 转 Markdown
- `mammoth`

  / `markdownify` / `ebooklib` — 文档转 Markdown
- `openpyxl`

  — Excel 转 Markdown
- `Pillow`

  + `numpy` — 图片处理
- `edge-tts`

  — 旁白语音生成
- `flask`

  — SVG 编辑器

### 2.2 图片生成后端（可选）

如需 AI 生成图片，配置环境变量 `IMAGE_BACKEND，`支持的 provider：

- Gemini（默认，推荐）
- OpenAI 兼容后端
- 及其他 14 种后端

在 `.env` 文件中设置：

```
IMAGE_BACKEND=geminiGOOGLE_API_KEY=your_key_here
```

---

## 3. 完整工作流

```
源文档 → 创建项目 → 模板选择(可选) → Strategist → [图片获取] → Executor → 后处理 → 导出
```

### 执行纪律（重要）

| 规则 | 说明 |
| --- | --- |
| **串行执行** | 步骤必须按顺序执行，不可跳步 |
| **⛔ BLOCKING 硬停** | 标记为 BLOCKING 的步骤必须等待用户确认 |
| **不跨阶段打包** | 禁止提前准备后续阶段内容 |
| **SVG 由主 Agent 生成** | 禁止委托给子 Agent |
| **逐页生成** | SVG 页面必须一页一页顺序生成 |

### 阶段总览

| 步骤 | 名称 | 阻塞点 | 产物 |
| --- | --- | --- | --- |
| 1 | 源内容处理 | 确认内容就绪 | Markdown 文件 |
| 2 | 项目初始化 | 确认结构创建成功 | 项目目录 + sources/ |
| 3 | 模板选择 | 默认无阻塞 | design\_spec.md |
| 4 | Strategist 设计 | ⛔ 八大确认 | design\_spec.md + spec\_lock.md |
| 5 | 图片获取（条件触发） | 无 | image\_prompts.md + image\_sources.json |
| 6 | Executor SVG 生成 | 质量检查门 | svg\_output/ + notes/total.md |
| 7 | 后处理与导出 | 无 | .pptx 文件 |

---

## 4. 源文档转换

根据源文件类型选择对应命令：

| 源文件类型 | 命令 |
| --- | --- |
| PDF | `python3 scripts/source_to_md/pdf_to_md.py ` |
| DOCX / Word | `python3 scripts/source_to_md/doc_to_md.py ` |
| XLSX / Excel | `python3 scripts/source_to_md/excel_to_md.py ` |
| PPTX / PowerPoint | `python3 scripts/source_to_md/ppt_to_md.py ` |
| EPUB / HTML / LaTeX | `python3 scripts/source_to_md/doc_to_md.py ` |
| 网页链接 | `python3 scripts/source_to_md/web_to_md.py ` |
| 微信公众号/安全站点 | `python3 scripts/source_to_md/web_to_md.py ` （需安装 `curl_cffi`） |
| Markdown | 直接读取，无需转换 |

转换完成后，确认内容可读且完整，进入下一步。

---

## 5. 项目初始化

### 5.1 创建项目

```
python3 scripts/project_manager.py init <项目名称> --format <格式
```

格式选项见 第 11 节，常用 `ppt169`（默认）。

### 5.2 导入源文件

```
python3 scripts/project_manager.py import-sources <项目路径> <源文件...> --move
```

> ⚠️ **必须使用 `--move：`**文件会被移入 `sources/` 目录，原位置不再保留。

### 5.3 验证项目结构

```
python3 scripts/project_manager.py validate <项目路径
```

---

## 6. 设计策划阶段（Strategist）

### 6.1 八大确认（⛔ BLOCKING）

Strategist 角色会提出以下建议，**必须等待用户确认**后才能继续：

1. **画布格式**

   — 如 `ppt169` (1280x720)
2. **页数范围**

   — 如 15-20 页
3. **目标受众**

   — 如"技术团队"
4. **风格目标**

   — 如"专业、简洁"
5. **配色方案**

   — 如深蓝+白色+金色
6. **图标使用**

   — 如"使用线性图标"
7. **排版方案**

   — 如"无衬线字体"
8. **图片使用**

   — 如"每页一张配图"

### 6.2 图片分析（如有用户提供的图片）

```
python3 scripts/analyze_images.py <项目路径>/images
```

> ⚠️ **禁止直接打开/查看图片文件，**所有图片信息必须通过 `analyze_images.py` 获取。

### 6.3 产物

- `<项目路径>/design_spec.md`

  — 人类可读的设计文档
- `<项目路径>/spec_lock.md`

  — 机器可读的执行契约（每页生成前必须重新读取）

---

## 7. 图片获取阶段（Conditional）

### 7.1 触发条件

当设计文档中的资源列表包含 `Acquire Via: ai` 或 `Acquire Via: web` 时触发。

### 7.2 执行流程

| 获取方式 | 参考文档 | 执行命令 |
| --- | --- | --- |
| AI 生成 | `references/image-generator.md` | `python3 scripts/image_gen.py ...` |
| 网络搜索 | `references/image-searcher.md` | `python3 scripts/image_search.py ...` |

### 7.3 图片生成命令

```
# 生成单张图片python3 scripts/image_gen.py "A modern futuristic workspace"# 查看所有可用的图片生成后端python3 scripts/image_gen.py --list-backends
```

### 7.4 完成检查

每行资源状态必须为以下之一：

- `Generated`

  — AI 生成成功
- `Sourced`

  — 网络搜索成功
- `Needs-Manual`

  — 需要手动提供

不允许残留 `Pending` 状态。

---

## 8. SVG 生成阶段（Executor）

### 8.1 前置准备

1. 读取角色定义（自动）
2. 输出关键设计参数（画布尺寸、配色、字体、字号）
3. **批量预读：**

   一次性读取所有用到的布局模板 SVG 和图表模板 SVG

### 8.2 逐页生成

SVG 页面必须**一页一页顺序生成，**保存到 `<项目路径>/svg_output/。`

每页生成前必须重新读取 `spec_lock.md。`

### 8.3 质量检查（⛔ 必须通过）

```
python3 scripts/svg_quality_checker.py <项目路径
```

| 结果 | 处理 |
| --- | --- |
| `error` | **必须修复，** 重新生成该页 |
| `warning` | 方便则修复，否则跳过 |

> ⚠️ 质量检查必须在 `svg_output/` 目录上运行（不是 `svg_final/`）。

### 8.4 讲者备注生成

自动生成 `<项目路径>/notes/total.md。`

### 8.5 图表校准（可选）

如果 PPT 包含数据图表（柱状图/折线图/饼图等），在步骤 7 之前运行：

```
阅读 workflows/verify-charts.md 并执行
```

---

## 9. 后处理与导出

### 三个命令必须**逐个执行，**不可合并：

### 9.1 分割讲者备注

```
python3 scripts/total_md_split.py <项目路径
```

### 9.2 SVG 后处理

图标嵌入、图片裁剪与嵌入、文本扁平化、圆角矩形转路径：

```
python3 scripts/finalize_svg.py <项目路径
```

### 9.3 导出 PPTX

```
python3 scripts/svg_to_pptx.py <项目路径
```

产物：

- `exports/<项目名>_<时间戳>.pptx`

  — 主 PPTX（原生高保真）
- `backup/<时间戳>/<项目名>_svg.pptx`

  — SVG 预览版本
- `backup/<时间戳>/svg_output/`

  — SVG 源文件备份

### 9.4 动画选项（可选）

```
python3 scripts/svg_to_pptx.py <项目路径> -t fade -a mixed --animation-trigger after-previous
```

| 参数 | 默认值 | 可选值 |
| --- | --- | --- |
| `-t` 页过渡 | `fade` | fade/push/wipe/split/strips/cover/random/none |
| `-a` 入场动画 | `mixed` | 具体效果或 none |
| `--animation-trigger` | `after-previous` | on-click/with-previous/after-previous |
| `--auto-advance` | 无 | 秒数（自动播放） |

### 9.5 录制旁白（可选）

仅当用户明确要求语音旁白时执行：

```
阅读 workflows/generate-audio.md 并执行
```

默认使用 Edge TTS，也支持 ElevenLabs / MiniMax / Qwen / CosyVoice。

### 9.6 本地预览

```
python3 -m http.server -d <项目路径>/svg_final 8000
```

浏览器打开 `http://localhost:8000` 查看 SVG 页面。

---

## 10. 常用命令速查

### 10.1 文档转换

```
python3 scripts/source_to_md/pdf_to_md.py python3 scripts/source_to_md/ppt_to_md.py python3 scripts/source_to_md/doc_to_md.py python3 scripts/source_to_md/excel_to_md.py python3 scripts/source_to_md/web_to_md.py
```

### 10.2 项目管理

```
python3 scripts/project_manager.py init  --format ppt169python3 scripts/project_manager.py import-sources   --movepython3 scripts/project_manager.py validate
```

### 10.3 SVG 处理

```
python3 scripts/svg_quality_checker.py python3 scripts/finalize_svg.py python3 scripts/total_md_split.py
```

### 10.4 导出

```
python3 scripts/svg_to_pptx.py
```

### 10.5 图片

```
python3 scripts/image_gen.py "prompt"python3 scripts/image_gen.py --list-backendspython3 scripts/analyze_images.py /images
```

### 10.6 模板导入

```
python3 scripts/pptx_template_import.py
```

### 10.7 仓库更新

```
python3 scripts/update_repo.py
```

---

## 11. 画布格式选择

### 格式速查表

| 格式 | 尺寸 | 比例 | 适用场景 |
| --- | --- | --- | --- |
| **PPT 16:9** | 1280×720 | 16:9 | 商务演示、会议（默认推荐） |
| **PPT 4:3** | 1024×768 | 4:3 | 传统投影仪、学术答辩 |
| **小红书** | 1242×1660 | 3:4 | 图文分享、知识帖子 |
| **微信朋友圈/IG** | 1080×1080 | 1:1 | 方形海报、品牌展示 |
| **故事/抖音** | 1080×1920 | 9:16 | 竖版故事、短视频封面 |
| **微信文章头图** | 900×383 | 2.35:1 | 微信公众号封面 |
| **宽幅 Banner** | 1920×1080 | 16:9 | 网页横幅、数字屏幕 |
| **竖版海报** | 1080×1920 | 9:16 | 手机屏幕、电梯广告 |
| **A4 打印** | 1240×1754 | 1:√2 | 打印海报、传单 |

### 选择决策树

```
内容用途？├── 演示│   ├── 现代设备 → PPT 16:9 (1280x720)│   └── 传统设备 → PPT 4:3 (1024x768)├── 社交分享│   ├── 小红书 → 1242x1660│   ├── 微信朋友圈/IG → 1080x1080│   └── 故事/抖音 → 1080x1920└── 营销物料    ├── 微信文章头图 → 900x383    ├── Banner → 1920x1080    └── 打印 → 1240x1754
```

---

## 12. 图片生成

### 12.1 支持的 AI 图片后端

| 后端 | 环境变量 | 说明 |
| --- | --- | --- |
| Gemini（推荐） | `IMAGE_BACKEND=gemini` | Google Gemini，默认 |
| OpenAI 兼容 | `IMAGE_BACKEND=openai` | 兼容 OpenAI API |
| SiliconFlow | `IMAGE_BACKEND=siliconflow` | 硅基流动 |
| VolcEngine | `IMAGE_BACKEND=volcengine` | 火山引擎 |
| Zhipu | `IMAGE_BACKEND=zhipu` | 智谱 AI |
| Qwen | `IMAGE_BACKEND=qwen` | 通义千问 |
| 其他 10+ 种 | `--list-backends` | 查看所有可用后端 |

### 12.2 图片水印去除

如果使用 Gemini 生成的图片带有水印：

```
python3 scripts/gemini_watermark_remover.py
```

---

## 13. 常见问题

### 13.1 安装相关

**Q: Python 依赖安装失败？**

确保已安装 Python 3.8+，然后：

```
pip install --upgrade pippip install -r "C:/Users/matebook 14/.claude/skills/ppt-master/requirements.txt"
```

**Q: CairoSVG 安装失败（macOS/Linux）？**

```
# macOSbrew install cairo# Ubuntu/Debiansudo apt install libcairo2-dev
```

### 13.2 使用相关

**Q: 如何修改已生成页面的内容？**

- 如果能明确描述修改需求（如"第 3 页副标题字号改 32"），直接编辑 SVG 文件
- 如果描述不够精确（如"这里看着不对"），使用 `workflows/visual-edit.md` 可视化编辑

**Q: 如何更新技能文件？**

```
python3 scripts/update_repo.py
```

**Q: 故障排查？**

查看 `scripts/docs/troubleshooting.md` 获取已知问题的解决方案。

### 13.3 技能位置

| 内容 | 路径 |
| --- | --- |
| 技能定义 | `C:/Users/matebook 14/.claude/skills/ppt-master/SKILL.md` |
| Python 依赖 | `C:/Users/matebook 14/.claude/skills/ppt-master/requirements.txt` |
| 环境变量模板 | `C:/Users/matebook 14/.claude/skills/ppt-master/.env.example` |
| 参考文档 | `C:/Users/matebook 14/.claude/skills/ppt-master/references/` |
| 脚本工具 | `C:/Users/matebook 14/.claude/skills/ppt-master/scripts/` |
| 图标库 | `C:/Users/matebook 14/.claude/skills/ppt-master/templates/icons/` |
| 布局模板 | `C:/Users/matebook 14/.claude/skills/ppt-master/templates/layouts/` |
| 图表模板 | `C:/Users/matebook 14/.claude/skills/ppt-master/templates/charts/` |
