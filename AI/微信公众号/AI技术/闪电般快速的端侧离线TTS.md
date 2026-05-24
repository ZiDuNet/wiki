# supertonic — 闪电般快速的端侧离线 TTS

> GitHub: https://github.com/supertone-inc/supertonic
> Stars: 热门项目 (2026-05) | 协议: OpenRAIL-M (模型) / MIT (代码) | 语言: Python
> 技术栈: ONNX Runtime、端侧推理、多语言TTS

## 一句话简介

**约 99M 参数的端侧文本转语音系统，基于 ONNX Runtime 完全离线运行，CPU 上即可快速推理。v3 版本支持 31 种语言，新增 Expression Tags 情感控制标签。提供 11 个平台 SDK。**

## 核心特点

- **31 种语言**: 英语、中文、日语、韩语、阿拉伯语及欧洲多语言
- **完全离线**: 基于 ONNX Runtime，无云端依赖，保护隐私
- **轻量高效**: 约 99M 参数，CPU 上可媲美 A100 GPU 速度
- **跨平台部署**: C++、Node.js、Python、Rust、Java、Go、Swift、C#、Flutter、iOS、Web(WebGPU/WASM)
- **Expression Tags**: `<laugh>`、`<breath>`、`<sigh>` 等情感表达控制

## 快速安装

```bash
pip install supertonic

# 或完整克隆（含模型）
git clone https://github.com/supertone-inc/supertonic.git
git lfs install
git clone https://huggingface.co/Supertone/supertonic-3 assets
cd py && uv sync && uv run example_onnx.py
```

## 自然文本处理能力

- 金融表达（股票代码、百分比）
- 电话号码格式化
- 技术单位（GHz、TB、Mbps）
- 多语言混读

## 适用场景

- 嵌入式设备和边缘计算语音合成
- 隐私敏感场景的离线 TTS
- 游戏/应用内的角色配音
- 多语言产品本地化语音

---
*来源: 逛逛GitHub - 不要错过这10个本周火火火的GitHub开源项目 (2026-05-24)*
