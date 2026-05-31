# Recordly

> 开源屏幕录制与编辑器，无需后期编辑即可生成精美的演示、Demo和产品视频。
> GitHub: https://github.com/webadderallorg/Recordly
> 许可证: AGPL 3.0

## 简介

Recordly 是一个跨平台桌面应用（macOS / Windows / Linux），专注于屏幕录制和视频编辑。它的核心特色是内置了自动缩放、光标美化、动态摄像头气泡叠加、样式化边框等演示工具，让用户无需专业后期制作就能产出高质量的产品演示视频。

- 网站: https://www.recordly.dev
- 创建者: [@webadderall](https://x.com/webadderall)
- 扩展市场: https://marketplace.recordly.dev/extensions
- 最初 fork 自 [OpenScreen](https://github.com/siddharthvaddem/openscreen)，现已独立发展

## 平台支持

| 平台 | 最低版本 | 捕获方式 |
|---|---|---|
| macOS | 14.0 (Sonoma) | 原生 ScreenCaptureKit |
| Windows | 10 Build 19041+ | 原生 Windows Graphics Capture (WGC) + WASAPI |
| Linux | 现代发行版 | Electron 捕获 API（系统音频需 PipeWire） |

## 核心功能

### 录制
- 录制整个屏幕或单个应用窗口
- 麦克风 + 系统音频采集
- 录制后直接进入编辑器

### 光标控制
- 自动缩放建议（基于光标活动）
- 光标平滑、运动模糊、点击弹跳、光标摇摆
- macOS 风格光标资源渲染
- 循环模式（Loop Mode）用于干净循环导出

### 动态摄像头叠加
- 摄像头气泡预设位置 + 自定义坐标
- 镜像、圆角、阴影控制
- 可选缩放响应式摄像头缩放

### 时间线编辑
- 拖拽式时间线：裁剪、缩放区域、变速区域、标注、音频区域
- 画幅裁剪与宽高比预设
- `.recordly` 项目文件保存/恢复

### 样式化边框与背景
- 内置壁纸 / 自定义上传 / 纯色 / 渐变
- 内边距、圆角、背景模糊、阴影

### 导出
- MP4 / GIF 导出
- 质量选择、GIF 帧率、尺寸预设

### 扩展系统
- 社区驱动的扩展市场：光标点击音效、设备边框、浏览器模型、壁纸、渲染钩子等

## 技术栈

- **框架**: Electron + React + TypeScript + Vite
- **渲染**: PixiJS（场景合成与导出共用同一逻辑）
- **构建**: electron-builder，支持 macOS/Windows/Linux 打包
- **桌面端原生**: Swift (macOS ScreenCaptureKit)、C++ (Windows WGC)
- **样式**: Tailwind CSS

## 安装方式

**预构建版本**: [GitHub Releases](https://github.com/webadderallorg/Recordly/releases)

**Arch Linux (AUR)**:
```bash
yay -S recordly-bin
```

**从源码构建**:
```bash
git clone https://github.com/webadderallorg/Recordly.git
cd Recordly
npm install
npm run dev        # 开发模式
npm run build      # 打包
```

## 已知限制

- Linux 不支持光标隐藏（Electron 限制）
- 系统音频：Linux 需 PipeWire，macOS 需 14.0+
- Windows 旧版本（<19041）录制时真实光标可能可见

## 标签

`screen-recorder` `video-editor` `electron` `open-source` `demo-tool` `pixijs`
