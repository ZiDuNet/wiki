---
tags: [抖音, MCP, 视频下载, 文案提取, 开源项目]
sources: ["开源！抖音无水印视频 + AI 文案提取，这个 MCP 服务太香了.md"]
created: 2026-05-29
updated: 2026-05-29
---

# douyin-mcp-server

**类型:** 实体 — 开源项目
**GitHub:** https://github.com/yzfly/douyin-mcp-server
**维护者:** yzfly
**技术栈:** Python (uv)
**依赖:** uv + Python 3.10+ + FFmpeg

## 简介

抖音无水印视频下载 + AI语音文案提取的MCP Server。支持三种使用方式：WebUI浏览器操作、Claude Desktop MCP集成、命令行工具。

## 核心功能

- 无水印视频下载：从分享链接获取高质量无水印视频
- AI语音文案提取：硅基流动 SenseVoice API 语音转文字
- 大文件自动分段：超1小时/50MB自动用FFmpeg分割9分钟片段
- 输出格式：Markdown（视频元数据+AI文案）

## 使用方式

1. **WebUI**: `uv run python web/app.py` → http://localhost:8080
2. **MCP集成**: Claude Desktop 配置 mcpServers
3. **命令行**: `uv run python douyin-video/scripts/douyin_downloader.py -l "链接" -a extract`

## 相关概念

[[MCP协议]], [[MCP Server]], [[抖音]]

## 相关文章

- [[开源！抖音无水印视频 + AI 文案提取，这个 MCP 服务太香了]]
