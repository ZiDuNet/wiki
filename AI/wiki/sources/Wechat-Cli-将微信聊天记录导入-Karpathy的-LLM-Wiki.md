---
title: Wechat-Cli + Graphify — 从加密数据库到结构化知识图谱的完整链路
type: source-summary
tags: [wechat-cli, Graphify, LLM-Wiki, 微信数据导出, 知识图谱, 暗知识, macOS]
sources: [Wechat-Cli：将微信聊天记录导入 Karpathy 的 LLM Wiki.md]
created: 2026-05-24
updated: 2026-05-24
---

# Wechat-Cli + Graphify — 从加密数据库到结构化知识图谱的完整链路

> 📎 来源: [AI作弊码](https://mp.weixin.qq.com/s?__biz=MzI2MzA5NjA4MQ==&mid=2665365507&idx=1&sn=8efb2e3bb093dcbda21aed892627d696) | 时间: 2026-05-24

## 核心观点

Karpathy LLM Wiki 系列第三篇：将数据源扩展到**微信聊天记录**。群聊讨论、技术分享、项目决策等「暗知识」一直被锁在微信加密数据库中，wechat-cli 通过进程内存扫描提取密钥，结合 Graphify 将聊天记录编译成知识图谱。

## wechat-cli 简介

**wechat-cli** (⭐425 Stars, Apache-2.0) 是纯本地/只读/零网络的命令行工具，专为 AI agent 和 LLM 工具调用设计。

### 技术原理

```
C程序扫描进程内存提取密钥 → AES-256-CBC逐页透明解密 → 结构化SQL查询输出JSON
```

微信 Mac 版使用 SQLCipher 加密的 SQLite 数据库，密钥藏在进程内存里。wechat-cli 用 320 行 C 代码 (`find_all_keys_macos.c`) 扫描内存提取密钥，实现透明解密。

### 11条核心命令

| 命令 | 功能 |
|------|------|
| `sessions` | 最近会话列表（带未读数、最后消息预览） |
| `history` | 指定联系人/群的聊天记录（支持时间范围、类型过滤） |
| `search` | 全局/指定聊天内关键词搜索 |
| `export` | 导出为Markdown或纯文本（**知识库导入的关键命令**） |
| `contacts` | 联系人搜索与详情 |
| `stats` | 群聊统计（发言排行、消息类型分布、24小时活跃度） |
| `favorites` | 收藏夹查询 |
| `new-messages` | 增量新消息（自上次检查后，适合自动化） |

## 安装实战要点

### 为什么从源码安装

不建议 `npm install -g @canghe_ai/wechat-cli`，因为安装的是 10MB 预编译 Mach-O 二进制（PyInstaller打包），无法审计。对于需要 root 权限读取进程内存的工具，应从源码构建。

```bash
# 从源码安装
git clone https://github.com/huohuoer/wechat-cli.git
cd wechat-cli

# 审计核心文件
cat wechat_cli/bin/find_all_keys_macos.c    # 320行，内存扫描逻辑
cat wechat_cli/core/crypto.py               # 78行，AES解密逻辑

# 编译C二进制
cd wechat_cli/bin
cc -O2 -o find_all_keys_macos.arm64 find_all_keys_macos.c -framework Foundation
cd ../..

# Python安装
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
```

### macOS 签名微信

wechat-cli 需通过 `task_for_pid` 读取微信进程内存，需要给微信添加 `get-task-allow` 调试权限并重新签名。

**踩坑**：直接对 `/Applications` 签名会失败（macOS App Management 安全策略阻止）。解决方案：复制微信到用户目录下操作。

```bash
# 复制到用户目录
mkdir -p ~/Applications
cp -R /Applications/WeChat.app ~/Applications/WeChat.app

# 用Python提取并修改entitlements（移除sandbox相关权限）
python3 -c "
import subprocess, plistlib
r = subprocess.run(['codesign','-d','--entitlements',':-',
  '$HOME/Applications/WeChat.app'], capture_output=True)
data = r.stdout
try: ent = plistlib.loads(data)
except:
  idx = data.find(b'xml')
  ent = plistlib.loads(data[idx:]) if idx>=0 else {}
for k in ['com.apple.security.app-sandbox',
  'com.apple.application-identifier',
  'com.apple.developer.team-identifier',
  'com.apple.security.application-groups']:
  ent.pop(k, None)
ent['com.apple.security.get-task-allow'] = True
with open('wechat_ent.plist','wb') as f:
  plistlib.dump(ent, f, fmt=plistlib.FMT_XML)
"

# 重新签名
codesign --force --deep --sign - --entitlements wechat_ent.plist ~/Applications/WeChat.app

# 从用户目录启动
open ~/Applications/WeChat.app
```

## 完整链路：微信到知识图谱

### Step 1: 导出聊天记录为 Markdown

```bash
mkdir -p wiki/chats

# 导出技术讨论群最近3个月聊天记录
wechat-cli export "你的技术群" --format markdown \
  --start-time "2026-01-11" --output wiki/chats/tech-group.md

# 批量导出多个关键群聊
for g in "产品讨论" "架构评审" "技术交流"; do
  wechat-cli export "$g" --format markdown \
    --output "wiki/chats/${g}.md"
done
```

导出的 Markdown 格式示例：
```markdown
# 聊天记录: 技术交流群
- [2026-04-08 23:32] 某工程师: 周末用Codex，半天把毕业设计写完了
- [2026-04-09 10:38] 某架构师: 前端用Gemini，后端用Claude，运维用Codex
- [2026-04-10 09:18] 某PM: [图片] (local_id=234)
```

### Step 2: Graphify 编译成知识图谱

```bash
# 安装 Graphify
pip install graphifyy
graphify install    # 自动检测AI编码助手

# 在AI编码助手中执行
/graphify wiki/

# 输出目录
graphify-out/
  graph.html        # 可交互可视化图谱
  GRAPH_REPORT.md   # 关键节点、社区结构、推荐问题
  graph.json        # 可查询的持久化图谱
```

## 持续同步方案

`new-messages` 命令维护本地状态文件，每次只返回上次检查后的新消息：

```bash
# 增量追加新消息到知识库
wechat-cli new-messages --format text >> wiki/chats/daily.md

# 定时任务：每天晚上10点自动同步
crontab -e
0 22 * * * wechat-cli new-messages >> wiki/daily.md
```

## 安全边界

### C源码审计要点

- `find_all_keys_macos.c` (320行)：只用 `mach_vm_read` 扫描进程内存中的密钥模式，写入本地JSON文件
- 无网络调用，无数据外发
- Python代码：pycryptodome AES解密 + click CLI框架 + zstandard 压缩（3个依赖）
- 纯只读：不发送、不修改、不删除任何消息

### 合规提醒

- 只读取**自己设备上的数据**
- 不破解他人账户，不绕过微信服务端
- 群聊记录涉及他人发言，导入知识库前需符合隐私法规
- 使用云端 LLM 处理 Graphify 时，聊天文本片段会发送到 API

## 技术栈速查

| 项目 | 详情 |
|------|------|
| 语言 | Python 90% / C 8%（内存扫描） / JavaScript 2% |
| 依赖 | click + pycryptodome + zstandard（共3个） |
| 系统要求 | macOS（主要支持） / Python 3.10+ |
| 协议 | Apache License 2.0 |
| 搭配工具 | Graphify (⭐20.3k Stars) |

## 相关实体

- [[wechat-cli]]
- [[Graphify]]
- [[Karpathy]]

## 相关概念

- [[暗知识]]
- [[微信数据导出]]
- [[知识图谱构建]]
- [[LLM-Wiki方法论]]
- [[本地优先]]
- [[增量同步]]