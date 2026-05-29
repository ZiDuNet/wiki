---
tags: [抖音, MCP, 视频下载, 文案提取, AI语音识别]
sources: ["开源！抖音无水印视频 + AI 文案提取，这个 MCP 服务太香了.md"]
created: 2026-05-29
updated: 2026-05-29
---

# 开源！抖音无水印视频 + AI 文案提取，这个 MCP 服务太香了

**来源：** 开源！抖音无水印视频 + AI 文案提取，这个 MCP 服务太香了.md
**摄入日期：** 2026-05-29
**类型：** 工具介绍

## 摘要

介绍 [[douyin-mcp-server]] 项目，一个基于 MCP 协议的抖音视频无水印下载 + AI 语音文案提取工具。支持 WebUI、Claude Desktop MCP 集成、命令行三种使用方式。

## 核心内容

- 无水印视频下载：从抖音分享链接直接获取高质量无水印视频
- AI 语音文案提取：调用硅基流动 SenseVoice API 转文字，超1小时/50MB自动分段处理
- 三种使用方式：WebUI（浏览器操作）、MCP Server（Claude Desktop集成）、命令行工具
- 大文件自动分段：FFmpeg自动分割9分钟片段，逐段调用API转录
- 输出格式：Markdown文件，含视频元数据和AI识别文案
- 依赖简单：uv + Python 3.10+ + FFmpeg

## 提及实体

- [[douyin-mcp-server]] — 抖音无水印视频下载+AI文案提取MCP服务
- [[硅基流动]] — SenseVoice API 提供方

## 涉及概念

- [[MCP协议]] — Model Context Protocol，Claude Desktop集成方式
- [[抖音]] — 目标平台
