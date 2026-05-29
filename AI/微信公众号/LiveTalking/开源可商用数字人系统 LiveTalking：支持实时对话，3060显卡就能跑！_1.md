> 📎 来源: [肥极喵](https://mp.weixin.qq.com/s?__biz=MzkzMjcwOTY3OQ==&mid=2247484509&idx=1&sn=1ce217f14686b2405864afb4025f0470&chksm=c3faa1480fe3aadcccab2eba302eed4d4ffd636f9fa02c5ea430c35ac44d33ff227ef4ec6395&mpshare=1&scene=1&srcid=0529AFRlVvgaZNYhakYAQBse&sharer_shareinfo=f137827dd02c376f1e40e1420710a6ca&sharer_shareinfo_first=f137827dd02c376f1e40e1420710a6ca) | 时间: 2026-05-29 12:15

---

![](assets/img_ca2d33f4b5e3.webp)

## 一、简介

LiveTalking 是一个开源的实时流式数字人系统，支持**音视频同步对话**，能够实现接近商用级别的交互体验。

项目由原 **metahuman-stream** 重命名而来，避免与 3D 数字人混淆，专注于**2D实时驱动数字人技术路线**。

其核心能力在于：
👉 输入文本 / 音频 → 实时生成语音 → 驱动嘴型 → 输出视频流（低延迟）

适用于：

- AI客服 / 虚拟主播
- 数字人直播
- 智能讲解 / 导购系统
- AI Agent 可视化交互

---

![](assets/img_06b3f7da04aa.png)

## 二、功能

LiveTalking 的功能非常全面，基本覆盖“数字人产品化”的核心能力：

### 🎯 核心能力

- 支持多模型驱动：Wav2Lip / MuseTalk / ER-NeRF
- 支持声音克隆（TTS）
- 支持实时打断（对话可中断）
- 支持多并发会话

### 📡 输出能力

- WebRTC（低延迟）
- RTMP 推流（直播平台）
- 虚拟摄像头输出（OBS / Zoom）

### 🎬 增强能力

- 自定义数字人形象
- 动作编排（空闲播放视频）
- 多数字人扩展能力
- 插件化架构（可扩展TTS / Avatar / Output）

---

## 三、技术栈

整体架构是一个标准的 AI 实时流系统：

### 🧠 AI层

- LLM：通义千问（Qwen）等
- TTS：EdgeTTS / GPT-SoVITS
- 视觉模型：

- Wav2Lip（轻量实时）
- MuseTalk（高质量）
- ER-NeRF（高拟真）

### ⚙️ 后端

- Python 3.10
- PyTorch 2.5 + CUDA 12.4
- WebRTC / RTMP 流媒体

### 🧩 架构设计

- API层：会话 + 请求处理
- 逻辑层：LLM + TTS + 特征提取
- 渲染层：唇形生成 + 视频融合
- 流媒体层：实时推流
- 插件系统：模块解耦扩展

👉 本质就是一个：
**LLM + TTS + CV + Streaming 的融合系统**

---

## 四、部署方式（重点）

这一部分我帮你整理成**最稳不翻车版本**👇

---

### ✅ 方式一：Docker（强烈推荐）

适合：快速体验 / 不想折腾环境

```
docker run --gpus all -it --network=host --rm \registry.cn-beijing.aliyuncs.com/codewithgpu2/lipku-metahuman-stream:2K9qaMBu8v
```

进入容器后：

```
cd /root/metahuman-streamgit pull
```

然后运行：

```
python app.py --transport webrtc --model wav2lip --avatar_id wav2lip256_avatar1
```

---

### ⚠️ 关键端口（必须放行）

```
TCP: 8010UDP: 1-65536（WebRTC 必须）
```

👉 如果你在云服务器：

- 必须开 UDP（很多人卡这里）
- 没 UDP → 看不到视频

---

### ✅ 方式二：源码部署（可控性强）

#### 1️⃣ 创建环境

```
conda create -n nerfstream python=3.10conda activate nerfstream
```

#### 2️⃣ 安装 PyTorch（注意 CUDA 版本）

```
conda install pytorch==2.5.0 torchvision==0.20.0 \torchaudio==2.5.0 pytorch-cuda=12.4 \-c pytorch -c nvidia
```

👉 ⚠️ 如果 CUDA 不是 12.4
去官网匹配版本：https://pytorch.org/get-started/previous-versions/

---

#### 3️⃣ 安装依赖

```
pip install -r requirements.txt
```

---

#### 4️⃣ 下载模型

必须准备：

- wav2lip 模型
- avatar 数据

```
模型下载：https://pan.quark.cn/s/83a750323ef0或 Google Drive
```

放置方式：

```
models/wav2lip.pthdata/avatars/wav2lip256_avatar1/
```

---

#### 5️⃣ 启动服务

```
python app.py \--transport webrtc \--model wav2lip \--avatar_id wav2lip256_avatar1
```

---

#### 6️⃣ 访问方式

浏览器打开：

```
http://你的IP:8010/webrtcapi.html
```

操作：

1. 1. 点击 start
2. 2. 输入文本
3. 3. 数字人开始说话

---

## 五、性能说明（重点选型）

| 模型 | GPU | FPS |
| --- | --- | --- |
| wav2lip | 3060 | 60 |
| wav2lip | 3080Ti | 120 |
| musetalk | 3080Ti | 42 |
| musetalk | 4090 | 72 |

👉 结论很直接：

- **3060以上 → 可跑实时**
- **想要更真实 → 上 3080Ti / 4090**

---

## 六、开源地址

- Gitee：
  👉 https://gitee.com/lipku/LiveTalking
- 文档：
  👉 https://livetalking-doc.readthedocs.io/

 

![](assets/img_13743a822cf9.gif)

![](assets/img_18d567c81b58.gif)

[DouYin\_Spider：！高手逆向了抖音Api并开源了](https://mp.weixin.qq.com/s?__biz=MzkzMjcwOTY3OQ==&mid=2247484504&idx=1&sn=4f85d01c79974488e2656322929035d4&scene=21#wechat_redirect)

[开源：Jellyfish一个全流程AI短剧工厂，轻松搞定角色一致性！](https://mp.weixin.qq.com/s?__biz=MzkzMjcwOTY3OQ==&mid=2247484499&idx=1&sn=6641dfe09259a7fc14264f7088ed9a45&scene=21#wechat_redirect)

[杜绝污染工作电脑！开箱即用！Win11虚拟机中运行 OpenClaw ！](https://mp.weixin.qq.com/s?__biz=MzkzMjcwOTY3OQ==&mid=2247484487&idx=1&sn=184605fe2c1dd417bba77526a29b27fe&scene=21#wechat_redirect)

[开源的闲鱼助手JAVA版本来了](https://mp.weixin.qq.com/s?__biz=MzkzMjcwOTY3OQ==&mid=2247484478&idx=1&sn=d6763b1326cee6a55ce50e784645d757&scene=21#wechat_redirect)
