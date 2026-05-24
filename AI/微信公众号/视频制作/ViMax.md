# ViMax — 多智能体协作视频生成框架

> GitHub: https://github.com/HKUDS/ViMax
> Stars: 热门项目 (2026-05) | 协议: MIT | 语言: Python 3.12
> 技术栈: 多Agent协作、RAG、MiniMax M2.7、并行镜头生成

## 一句话简介

**港大数据智能实验室（HKUDS）出品的多智能体视频生成框架，把视频制作拆成 Director、Screenwriter、Producer、Video Generator 四个 AI 角色组成"剧组"，从剧本到成片一条龙。支持 Idea2Video、Script2Video、Novel2Video 三种模式。**

## 核心特点

- **Idea2Video**: 给个灵感就开搞，自动生成完整视频故事
- **Novel2Video**: 小说改编引擎，将完整小说转换为分集视频
- **Script2Video**: 从剧本生成无限长度视频
- **AutoCameo**: 上传照片即可将自己作为角色嵌入视频
- **多智能体协作**: 导演、编剧、制片人、视频生成器分工协作

## 快速安装

```bash
git clone https://github.com/HKUDS/ViMax.git
cd ViMax
uv sync
# 配置 configs/idea2video.yaml 中的 API 密钥
```

## 技术架构

```
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│ Director  │  │Screenwriter│  │ Producer │  │  Video   │
│  导演     │→│  编剧      │→│  制片    │→│ Generator│
└──────────┘  └──────────┘  └──────────┘  └──────────┘
      RAG长脚本生成 → 分镜设计 → 多机位模拟 → 并行镜头生成
```

- 智能长脚本生成（RAG-based）
- 表达性分镜设计
- 多摄像头拍摄模拟
- 智能参考图像选择
- 自动化一致性检查
- 支持 MiniMax 作为聊天模型（M2.7 有 1M 上下文）

## 适用场景

- AI 视频内容批量制作
- 小说/文章转视频
- 多 Agent 协作架构研究
- 教育和演示视频自动化生成

---
*来源: 逛逛GitHub - 不要错过这10个本周火火火的GitHub开源项目 (2026-05-24)*
