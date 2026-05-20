title: Infinite Canvas — 无限画布 AI 图像/视频生成工作台
source: https://github.com/hero8152/Infinite-Canvas
author: hero8152
date: 2026-05-20
tags: [AI绘图, 可视化工作流, ComfyUI, 图像生成, 视频生成, FastAPI, 无限画布]

# Infinite Canvas — 无限画布 AI 图像/视频生成工作台

## 项目简介

一个基于 FastAPI + Web 的可视化 AI 图像/视频生成工作台。在浏览器中提供"无限画布"（类似 Figma 的无限拖拽缩放画布），将各种 AI 模型以节点形式拖拽到画布上连线，像搭积木一样组合出图像/视频生成工作流。适合非技术人员使用，把 ComfyUI 的复杂度封装成浏览器里的拖拽画布体验。

GitHub: https://github.com/hero8152/Infinite-Canvas

## 核心功能

1. **多后端支持**：可接 ComfyUI 本地工作流、OpenAI 协议 API、ModelScope（魔搭）API、异步协议
2. **无限画布节点编辑**：拖拽节点、连线、参数配置，可视化编排 AI 生成流程
3. **图像生成+放大**：支持 Flux 等模型，支持 2K/4K 出图和图像增强（upscale）
4. **视频生成**：支持视频生成功能
5. **LLM 节点**：可用 GPT/Gemini 等大模型生成提示词，支持图片输入反推（图生文），可用 ModelScope 的 VL 模型
6. **循环并发**：循环节点可批量并发生成，如一次出 10 张不同卖点的产品图
7. **画笔编辑**：可在画布上直接绘制编辑
8. **自定义 ComfyUI 工作流**：可设置自定义输入和参数，在画布的 ComfyUI 节点中调用
9. **中英文切换**
10. **网页内 API 设置**：全程在网页中配置 API，可拉取模型一键添加

## 技术栈

- 后端：Python 3.10 + FastAPI + uvicorn
- 依赖：requests, pydantic, python-multipart, httpx, Pillow
- 前端：纯 HTML/JS（canvas.html ~8800 行，画布核心逻辑）
- 自带精简版 Python 3.10 运行环境（Windows）

## 安装运行（Windows）

1. 运行 `安装依赖.bat` 安装 Python 依赖
2. 运行 `run.bat` 启动服务
3. 浏览器打开本地服务地址

## 典型使用场景

- 电商批量出图：用 Gemini 生成卖点提示词 → 循环节点并发调用 API → 一次生成多张产品图
- AI 绘画创作：在无限画布上组合 LLM + 图像模型 + 放大节点
- 视频生成：通过节点连线一键生成视频

## 更新记录（摘要）

- 5/13：修复依赖报错、网页内 API 设置、LLM 图片反推、中英文切换、自定义 ComfyUI 工作流、视频生成、2K/4K 修复
- 5/14：Mac 修复、ModelScope LoRA 支持、OpenAI/异步协议
- 5/15：循环组件+计数、协议验证按键、精简版 Python
- 5/18：视频生成 bug 修复、画笔编辑、ComfyUI 并发修复
