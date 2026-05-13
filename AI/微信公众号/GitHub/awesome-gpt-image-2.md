---
title: awesome-gpt-image-2 - GPT-Image2 工业级提示词引擎与模板库
source: https://github.com/freestylefly/awesome-gpt-image-2
author: freestylefly
date: 2026-05-13
tags:
  - GPT-Image-2
  - AI绘画
  - Prompt模板
  - 图像生成
  - OpenAI
  - 提示词工程
---

# awesome-gpt-image-2

## 项目简介

**Prompt as Code | GPT-Image2 工业级提示词引擎与模板库**

这是一个专门为 GPT-Image-2 打造的开源提示词模板库，收录了 **400+ 逆向工程案例** 和 **20+ 工业级模板**，将社区散落的案例转化为可复用的 Prompt-as-Code 资产，方便 AI Agent 和开发者直接调用。

GPT-Image-2 是 OpenAI 的新一代图像生成模型，具有极强的指令理解能力和高达 99%+ 的文字渲染准确率，支持 4K 分辨率、3 秒出图。这个项目解决了"模型变强了但不知道怎么描述"的问题。

### 核心价值

- **案例丰富**：400+ 高质量案例，涵盖 UI 设计、海报、电商图、品牌 Logo、写实摄影、插画等多个领域
- **结构化描述**：将主体、背景、光影、排版拆开，不是散文式的"氛围感"
- **开箱即用**：每个案例都带完整 prompt 和效果图，一比一对照
- **MIT 协议开源**：可以克隆后替换成自己行业的关键词复用

---

## 模板库概览

### 21 套工业级模板分类

| 模板类型 | 说明 |
|---------|------|
| **UI Screenshot** | 应用界面截图生成 |
| **Poster Design** | 海报设计 |
| **Infographic** | 信息图/知识卡片 |
| **Product Visual** | 产品视觉包装 |
| **3D Scene** | 3D 场景渲染 |
| **Character Illustration** | 角色插画 |
| **Text Rendering** | 文字渲染 |
| **Portrait Photography** | 人像摄影 |
| **Social Media** | 社交媒体图片 |
| **E-commerce** | 电商产品图 |
| **Brand Logo** | 品牌 Logo 设计 |
| **Dark Style** | 暗黑风格 |
| **Chinese Calligraphy** | 中文书法作品 |
| **Movie Poster** | 电影海报 |
| **App Mockup** | 应用模型展示 |
| **Live Screenshot** | 直播间截图 |
| **Hot Search** | 微博热搜截图 |
| **Chinese Style** | 国风主题 |
| **Product Promo** | 产品宣传图 |
| **Technical Diagram** | 技术图解 |
| **Creative Poster** | 创意海报 |

---

## 精选案例示例

### 1. 生成宣传海报

**提示词：**
```
生成【星巴克】2026年春季新品上市的宣传海报，包含产品图片、促销信息和品牌元素
```

**适用场景：** 品牌宣传、活动推广、新品发布

---

### 2. 生成直播间截图

**提示词：**
```
生成一个抖音直播的截图，主播在直播卖水果，在线人数是66666，热度是200万+，有个叫Deepsider的大哥刷了火箭礼物
```

**适用场景：** 直播预热、社交媒体营销、案例展示

---

### 3. 生成热搜截图

**提示词：**
```
画一个微博热搜截图，第一条：GPT Image 2震撼发布，带爆字和热字
```

**适用场景：** 话题营销、热点借势、传播造势

---

### 4. 生成书法作品

**提示词：**
```
生成苏轼《水调歌头·明月几时有》全文中文书法作品，行书风格飘逸洒脱，墨色浓淡变化丰富，米黄色宣纸底，落款钤印，竖幅卷轴形式
```

**适用场景：** 文化创意、艺术设计、礼品定制

---

### 5. 国风主题海报

**提示词结构：**
```
时代背景 → 情绪基调 → 构图元素 → 文字排布 → 留白比例
```

**示例：**
```
《红楼梦》主题海报，清中期风格，暗色调，园林背景，留白40%
```

**适用场景：** 文化创意、古典主题、书籍封面

---

### 6. UI 界面截图

**JSON 格式模板：**
```json
{
  "type": "UI Screenshot",
  "platform": "iOS",
  "product": "Fitness App",
  "layout": "Card-based feed with bottom tab bar",
  "style": {
    "theme": "Dark Mode",
    "primary_color": "Neon Green",
    "typography": "Clean sans-serif"
  },
  "content": {
    "header": "Today's Activity",
    "cards": [
      {"title": "Running", "value": "5.2 km"},
      {"title": "Calories", "value": "320 kcal"}
    ]
  }
}
```

**适用场景：** App 设计、产品原型、展示文档

---

### 7. 信息图/知识卡片

**提示词：**
```
Create a detailed medical infographic of the human body showing major organs and how long a person can survive without each. Use a central transparent body, labeled organs, and a clean modern poster design.
```

**适用场景：** 科普教育、医疗健康、知识传播

---

### 8. 产品宣传图

**提示词：**
```
用 gpt-image-2 为这个开源仓库生成苹果风格的中文卡片宣传图
```

**适用场景：** 产品推广、品牌宣传、社交媒体

---

## 提示词工程技巧

### 文字渲染控制

GPT-Image-2 的文字渲染能力非常强，但需要正确引导：

- **强制文字锁定**：要求"文字绝对可读，必须显示指定的中文"，避免出现乱码
- **排版要求**：明确指定文字位置、大小、字体风格
- **避免火星文**：不要使用模糊的描述，要指定确切内容

### 结构化描述法

```
主体描述 → 背景环境 → 光影效果 → 构图方式 → 风格调性 → 文字排布
```

**示例：**
```
一个年轻女性（主体），站在咖啡店窗边（背景），柔和的侧光（光影），半身特写构图（构图），日系胶片风格（风格），底部添加品牌logo（文字）
```

---

## 项目结构

```
awesome-gpt-image-2/
├── data/                    # 案例数据
├── docs/                    # 文档
│   └── templates.md         # 模板详细说明
├── src/                     # 源代码
├── scripts/                 # 脚本工具
├── agents/                  # Agent 集成
│   └── skills/
│       └── gpt-image-2-style-library/
├── api/                     # API 使用示例
└── README.md
```

---

## 快速开始

### 1. 浏览案例库

访问项目页面，浏览不同类别的案例和模板。

### 2. 复制模板

找到适合你需求的模板，复制完整的 prompt 结构。

### 3. 替换关键词

将模板中的占位符替换为你自己的内容（品牌名、产品描述等）。

### 4. 调用 API

通过 OpenAI API 调用 GPT-Image-2：

```python
from openai import OpenAI

client = OpenAI()

response = client.images.generate(
    model="gpt-image-2",
    prompt="你的提示词",
    size="1024x1024",
    quality="hd"
)

image_url = response.data[0].url
```

---

## 相关资源

- **GitHub 仓库：** https://github.com/freestylefly/awesome-gpt-image-2
- **赞助商：** Ciyuan API（经济实惠的 GPT Image 2 访问平台）
- **更新频率：** 不定期更新，持续添加新工作流
- **开源协议：** MIT License

---

## 适用人群

- **设计师**：快速生成创意稿、概念图
- **产品经理**：制作产品原型、宣传物料
- **内容创作者**：社交媒体内容、博客配图
- **开发者**：集成到 AI 工作流中
- **营销人员**：品牌宣传、活动海报

---

## 总结

awesome-gpt-image-2 是一个实用的 GPT-Image-2 提示词模板库，通过 400+ 真实案例和 20+ 工业级模板，帮助用户快速掌握 AI 图像生成的提示词写法。项目采用 MIT 协议开源，可以直接克隆并定制成自己行业的版本，非常适合需要批量生成特定类型图片的用户。