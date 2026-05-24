---
type: entity
name: wechat-cli
created: 2026-05-10
updated: 2026-05-24
tags: [微信, CLI, Hermes, 微信数据导出, 暗知识]
---

# wechat-cli

**Type:** Entity (工具)
**Mentioned in:** 3 articles
**GitHub:** ⭐425 Stars, Apache-2.0

## 简介

wechat-cli 是纯本地/只读/零网络的微信命令行工具，通过进程内存扫描提取密钥，AES-256-CBC解密微信加密数据库，专为 AI agent 和 LLM 工具调用设计。支持11条核心命令，JSON默认输出，天然适配 LLM function call。

## 核心技术原理

```
C程序扫描进程内存提取密钥 → AES-256-CBC逐页透明解密 → 结构化SQL查询输出JSON
```

微信 Mac 版使用 SQLCipher 加密的 SQLite 数据库（AES-256-CBC逐页加密），密钥藏在进程内存里。wechat-cli 用 320 行 C 代码 (`find_all_keys_macos.c`) 通过 `task_for_pid` 读取微信进程内存，提取密钥后实现透明解密。

## 11条核心命令

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `sessions` | 最近会话列表（未读数、消息预览） | 查看活跃群聊 |
| `history` | 指定聊天记录（时间范围、类型过滤） | 回溯讨论 |
| `search` | 全局关键词搜索 | 快速定位 |
| `export` | 导出Markdown/纯文本 | **知识库导入** |
| `contacts` | 联系人搜索与详情 | 人员查询 |
| `stats` | 群聊统计（发言排行、活跃度） | 社群分析 |
| `favorites` | 收藏夹查询 | 个人收藏 |
| `new-messages` | 增量新消息 | **自动化同步** |

## 安全特性

- **C源码可审计**：320行内存扫描逻辑 + 78行AES解密
- **纯只读**：不发送、不修改、不删除任何消息
- **零网络**：密钥只在init阶段提取，数据全程不离开本机
- **依赖透明**：click + pycryptodome + zstandard（共3个主流库）

## 安装要点

- **建议从源码安装**：需要sudo权限扫描进程内存，不应信任预编译二进制
- **macOS签名要求**：需给微信添加 `get-task-allow` 调试权限并重新签名
- **绕开/Applications保护**：复制微信到 `~/Applications` 下操作

## 应用场景

1. **Hermes群聊情报助手**：自动总结100+群聊消息
2. **LLM Wiki知识库**：将聊天记录编译成知识图谱
3. **团队暗知识挖掘**：释放群聊中未被文档化的隐含价值

## Related Sources

- [[Wechat-Cli-将微信聊天记录导入-Karpathy的-LLM-Wiki]]
- [[用-Hermes-+-wechat-cli-搭建微信群聊情报助手,自动总结100+群聊消息]]
- [[用-Hermes-wechatcli-搭建微信群聊情报助手自动总结100群聊消息]]

## Related Concepts

- [[暗知识]]
- [[微信数据导出]]
- [[本地优先]]
- [[增量同步]]
- [[Hermes-Agent生态]]
- [[工作流自动化]]
- [[定时任务]]