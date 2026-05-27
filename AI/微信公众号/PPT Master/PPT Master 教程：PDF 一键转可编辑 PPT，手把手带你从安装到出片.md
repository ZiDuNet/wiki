> 📎 来源: [神经达尔加文](https://mp.weixin.qq.com/s?__biz=MzIwODM4ODA1MA==&mid=2247483865&idx=1&sn=946dd867764e608a3c1fd56de85c8292&chksm=96255a8ef48e3312735b024da4248794c3d65ae6e7d71af2283d11a95d2bda42041905518274&mpshare=1&scene=1&srcid=0527ENffUGPaZKkk8PeBHfLQ&sharer_shareinfo=c0b237d5837caa6d119663ec5754c298&sharer_shareinfo_first=c0b237d5837caa6d119663ec5754c298) | 时间: 2026-05-27 23:22

---

PDF扫描件 转 PPT 实战笔记

## 一起因：一个困扰我很久的痛点

日常工作中，我经常需要把各种 PDF 资料做成 PPT——给学生复习用、给教研组汇报用、给自己整理知识体系用。

但这些 PDF 的来源五花八门：

- **扫描件**

  ：教材、教辅的纸质版扫描成 PDF，没有文字层，全是图片
- **截图转 PDF**

  ：同事把截图粘贴到 Word 里再转成 PDF
- **Word 转 PDF**

  ：格式倒是保留了，但想改成 PPT 还是得从头排版

市面上的 AI PPT 工具我也试过不少，但普遍存在一个问题：**生成的 PPT 是"死"的**——要么整页是一张大图，改个字得重做；要么套个固定模板，AI 只能往框里填字，排版被限制得死死的。

## 二发现：群里的一条消息

2026年5月24日，我在一个科技社群里看到有人分享了一个 GitHub 项目：

> github.com/hugohe3/ppt-master

> AI从任何文档生成本地可编辑的PPTX——真正的PowerPoint形状与本地动画，而不是图像

我当时的第一反应是：又一个 AI PPT 工具？但点进去看了一下介绍，发现它说的"原生可编辑"跟别的工具不太一样——它生成的不是图片拼接，而是**真正的 PowerPoint 形状**，每个元素都能独立点击修改。

这个正好戳中我的痛点。于是我决定试一试。

## 三探索：用 AI 分析项目能力

我没有直接上手，而是先让 AI 帮我分析这个项目的能力边界。我给 AI 发了项目的 GitHub 链接，让它帮我梳理：

- 这个项目的核心原理是什么
- 它能处理哪些格式的输入
- 它的输出跟其他工具有什么本质区别
- 它的能力边界在哪里（什么场景强，什么场景弱）

AI 给我的分析让我确认了两件事：

1. **这个工具值得试**

   ——它的"原生 DrawingML 引擎"确实是独一份的技术路线
2. **扫描版 PDF 是它的软肋**

   ——任何 AI 工具都绕不过 OCR 这一步，PPT Master 也不例外

## 四动手：安装与环境搭建

### 4.1 克隆项目

```
cd ~/Her工作间git clone --depth 1 https://github.com/hugohe3/ppt-master.gitcd ppt-master
```

> 如果 GitHub 网速慢，可以用国内镜像：

> ```
> git clone --depth 1 https://atomgit.com/hugohe3/ppt-master.git
> ```

### 4.2 安装 Python 依赖

PPT Master 只需要 Python 3.10+，其余依赖一行命令搞定：

```
pip3 install python-pptx edge-tts svglib reportlab PyMuPDF \  mammoth markdownify ebooklib nbconvert openpyxl \  Pillow numpy requests beautifulsoup4 flask openai
```

**踩过的坑**：

```
svglib
```

 依赖系统级的 

```
cairo
```

 库，在 macOS 上需要先装：

```
brew install cairo
```

 然后再 

```
pip3 install svglib
```


如果 

```
cairo
```

 装不上也没关系——核心功能不受影响，

```
svg_to_pptx.py
```

 会自动用 PNG+SVG 双模式兼容。

### 4.3 验证安装

用项目自带的示例跑一遍，确认环境没问题：

```
python3 skills/ppt-master/scripts/svg_to_pptx.py \  examples/ppt169_general_dark_tech_claude_code_auto_mode \  -o ~/Her工作间/test_output.pptx
```

如果输出 

```
[Done] Saved: ...
```

 并且 PPTX 文件能正常打开，说明环境就绑了。

## 五实操：94页扫描版PDF → 14页可编辑PPT

### 5.1 选定测试素材

我选了一份"地狱难度"的素材来测试：《2023信息技术宝典手册（Python版）》

- 94 页
- 纯扫描版 PDF（没有文字层，每一页都是一张图片）
- 内容涵盖浙江省信息技术高考的全部九个专题

### 5.2 项目初始化

```
python3 skills/ppt-master/scripts/project_manager.py init projects/baodian
```

这会创建一个标准的项目目录结构：

```
projects/baodian_ppt169_YYYYMMDD/├── exports/          # 导出的 PPTX├── images/           # 图片资源├── notes/            # 演讲者备注├── sources/          # 源文件├── svg_output/       # 每页 SVG（核心！）└── templates/        # 模板
```

### 5.3 处理扫描版 PDF

扫描版 PDF 没有文字层，PPT Master 的 

```
pdf_to_md.py
```

 只能提取出图片：

```
python3 skills/ppt-master/scripts/source_to_md/pdf_to_md.py \  "/path/to/2023信息技术宝典手册（Python版）.pdf" -o /tmp/baodian.md
```

输出的 Markdown 里全是图片引用，没有文字。这一步**必须人工介入**——我逐页阅读图片，手动提取核心知识点。

这是整个流程中最耗时的环节。如果你的 PDF 是可搜索文字的版本（Word转PDF、带OCR的PDF），这一步可以省掉——PPT Master 会自动提取文字并生成大纲。

### 5.4 编写 SVG（核心步骤）

每个 SVG 文件就是 PPT 的一页。我为九个专题各写了一页，加上封面、Python速查表和结尾，共 14 页。

SVG 的基本结构：

```
#1a1a2e"/>            font-size="42" font-weight="bold" fill="#e94560">页面标题            fill="#16213e" stroke="#e94560" stroke-width="1"/>          font-size="15" fill="#cccccc">内容文字
```

**我踩过的坑（重要！）：**

**1. XML 转义**：SVG 是 XML 格式，

```
<
```

和

```

```

必须转义。我在写 Python 关系运算符时忘了这一步，导致导出报错。

```
<
```

→

```
<
```

，

```

```

→

```

```



**2. 中文字体**：SVG 中必须指定支持中文的字体，否则显示为方块。
使用：

```
font-family="Microsoft YaHei, SimHei, sans-serif"
```



**3. 文件命名**：用数字前缀排序，导出时会按文件名顺序生成幻灯片。

```
01_cover.svg
```

、

```
02_topic1.svg
```

、

```
03_topic2_1.svg
```

...

### 5.5 导出 PPTX

```
python3 skills/ppt-master/scripts/svg_to_pptx.py \  projects/baodian_ppt169_YYYYMMDD \  -o ~/Her工作间/信息技术宝典复习概览.pptx
```

成功输出：

```
[Done] Saved: /Users/xxx/Her工作间/信息技术宝典复习概览.pptx  Succeeded: 14, Failed: 0
```

用 PowerPoint 打开——每个元素都能独立点击、拖拽、改颜色、改字体。**这才是真正的"可编辑"。**

## 六校对：用 AI + 联网验证知识点

既然是高考复习资料，容不得半点马虎。我让 AI 做了三件事：

1. **逐页核查知识点**

   ：对照原 PDF 扫描件，检查每个知识点是否准确
2. **联网验证关键细节**

   ：比如 

   ```
   math.ceil(-2.3)
   ```

    到底是 

   ```
   -2
   ```

    还是 

   ```
   -3
   ```

   ，

   ```
   //
   ```

    对负数的行为到底是什么
3. **Python 实际运行验证**

   ：把有疑问的代码直接跑一遍，用结果说话

**核查发现的错误：**

| 位置 | 原文 | 正确 | 性质 |
| --- | --- | --- | --- |
| 第3页 字符串切片 | ``` S[5:-1]="022" ``` | ``` S[5:]="2" ``` | 事实错误 |

**核查确认正确的知识点（部分）：**

- ```
  ceil(-2.3) = -2
  ```

  、

  ```
  floor(-2.3) = -3
  ```

   ✓
- ```
  //
  ```

  对负数是向下取整（向负无穷），不是向零截断 ✓
- ```
  randint(a, b)
  ```

  包含两端 ✓
- 二叉树第 i 层最多 2^(i-1) 个节点 ✓
- 存储容量公式（音频、图像、视频）✓
- 大O复杂度排序 ✓

修正后重新导出，最终版本已确认无误。

## 七PPT Master 的能力边界总结

经过这次完整的实操，我对 PPT Master 的能力边界有了清晰的认识：

### 它擅长的

| 场景 | 说明 |
| --- | --- |
| Word/Markdown → PPT | 全自动，质量最高 |
| 网页链接 → PPT | 支持微信公众号文章 |
| PDF（可搜索文字）→ PPT | 自动提取文字和结构 |
| 多格式混输入 | PDF+Word+图片一起喂 |

### 它不擅长的

| 场景 | 说明 |
| --- | --- |
| 扫描版 PDF → PPT | 需要先 OCR 或人工提取文字 |
| 复杂数据图表 | 图表能力有限，有"伪图表"问题 |
| 独立运行 | 需要在 AI IDE（Claude Code/Cursor）中对话驱动 |

### 适合谁

- **教师**

  ：把教案、教辅转成课件 PPT
- **职场人**

  ：把方案、报告转成演示文稿
- **学生**

  ：把论文、笔记转成答辩 PPT

## 八快速上手清单

如果你想自己试一下，按这个顺序来：

```
1. 装 Python 3.10+                              ← 5分钟2. git clone 项目 + pip install 依赖              ← 5分钟3. 用示例跑通第一个 PPT（验证环境）               ← 2分钟4. 把你的 PDF 放进 projects/ 目录                 ← 1分钟5. 如果是可搜索文字的 PDF，直接让 AI 生成          ← 10分钟6. 如果是扫描版 PDF，先 OCR 或人工提取文字        ← 时间取决于页数7. 导出 PPTX，打开验证                            ← 2分钟
```

## 九还没解决的问题

前面的流程走下来，有一个问题始终没有解决：

**94页的扫描版PDF，最终只压缩成了14页PPT。**

这是"理解→重构"的工作方式——AI 读完全部内容后，按专题重新组织，浓缩出精华。适合做复习概览，但不是"原样转换"。

如果你需要的是"94页PDF → 94页PPT，每页内容尽量忠实于原文"，这就是进阶操作了。

> **下一篇：《PPT Master 进阶实操：扫描版PDF的逐页转换》**

> 将解决：如何让扫描版PDF的每一页都对应生成一帧PPT，保留原始内容的完整性。

## 十项目资源

- **GitHub 仓库**

  ：github.com/hugohe3/ppt-master
- **在线预览**

  ：hugohe3.github.io/ppt-master
- **文档**

  ：项目内 

  ```
  docs/zh/
  ```

   目录
- **示例**

  ：项目内 

  ```
  examples/
  ```

   目录（20+ 个完整示例）
- **常见问题**

  ：

  ```
  docs/zh/faq.md
  ```

---

写于 2026年5月24日
本教程基于 PPT Master v2.8.0 实操整理
