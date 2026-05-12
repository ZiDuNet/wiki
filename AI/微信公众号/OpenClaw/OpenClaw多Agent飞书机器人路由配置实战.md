> 📎 来源: [不灭的传说](https://mp.weixin.qq.com/s?__biz=MzA3ODk4OTU4Mg==&mid=2454625893&idx=1&sn=59c5e3a95f02600e7e1d75acbe077547&chksm=891ed41d337189fd0ffd149283636bec0fee7a78549659b09dba577735adc5e645cde04d2de0&mpshare=1&scene=1&srcid=0421XAV4lTLoblrPbBxk2NmJ&sharer_shareinfo=458e8019740036df5116a0ac71be361e&sharer_shareinfo_first=458e8019740036df5116a0ac71be361e) | 时间: 2026-04-21 20:23

---

# OpenClaw多Agent飞书机器人路由配置实战

> **摘要**：本文详细记录了OpenClaw多Agent系统中飞书机器人消息路由问题的诊断与解决过程。从所有消息错误路由到总指挥，到通过配置bindings实现正确分发，提供了完整的实战经验和避坑指南。

# 问题背景

最近在部署OpenClaw多Agent系统时，遇到了一个棘手的问题：我们配置了3个飞书机器人，分别对应3个不同的AI专家Agent（总指挥、编程大师、投资顾问）。但所有用户发送给这些机器人的消息，都被错误地路由到了总指挥Agent。

问题现象：

- 用户向编程大师机器人发送技术问题 → 总指挥回复
- 用户向投资顾问机器人发送财经咨询 → 总指挥回复

这完全打乱了我们的多Agent协作架构！

# 问题诊断过程

## 第一阶段：基础检查

检查飞书开放平台配置

✅-所有机器人APPID和APP Secret配置正确，事件订阅方式均为"使用长连接接收事件"（WebSocket模式）

检查OpenClaw配置文件~/.openclaw/openclaw.json✅

agent配置

```
{
```

渠道飞书机器人配置

```
{
```

检查Gateway日志✅

```
openclaw logs --follow
```

WebSocket连接都已建立,消息能被正确接收

```
0:43:07+00:00 info gateway/channels/feishu {"subsystem":"gateway/channels/feishu"} feishu[commander_bot]: Feishu[commander_bot] DM from ou_ec78524c64adc02cbbabf9ad8ed64956: 你现在有哪些技能？
```

但路由决策错误：所有消息都路由到agent:commander

## 第二阶段：深入学习官方文档

通过阅读OpenClaw官方文档《Multi-Agent Routing》，发现了关键信息：

核心要点：

1. 多Agent路由必须配置bindings
2. accountId是路由的关键标识
3. 路由规则按特异性匹配
4. 没有bindings时，所有消息路由到默认或第一个Agent

# 根本原因

缺少bindings配置！我们的配置虽然正确设置了agents.list和channels.feishu.accounts，但缺少了关键的bindings配置。OpenClaw Gateway收到飞书消息后，不知道应该将哪个accountId的消息路由到哪个agentId。

# 解决方案

## 添加bindings配置

```
{
```

##

# 实施步骤

## 手动编辑配置文件

备份原配置：

```
bash cp ~/.openclaw/openclaw.json ~/.openclaw/openclaw.json.backup
```

编辑配置文件，在根级别添加bindings数组

验证：

```
openclaw config validate 或者 openclaw doctor
```

重启Gateway

```
openclaw gateway restart
```

# 验证结果

配置更新后，进行了全面测试：

向编程大师机器人发送："你是?"

✅ 回复来自编程大师Agent

```
我是 CodeMaster 💻，你的编程专家
```

向投资顾问机器人发送："你是?"

✅ 回复来自投资顾问Agent

```
我是投资顾问，专注于为我的用户提供专业的投资分析和财经建议
```

所有消息路由恢复正常！

# 技术要点总结

## 1. OpenClaw多Agent路由架构

用户消息 → 飞书机器人 → OpenClaw Gateway → bindings匹配 → 对应Agent

## 2. bindings配置的核心作用

建立accountId到agentId的映射关系,决定消息路由的优先级和规则,支持复杂的路由策略（按频道、账户、群组等）

## 3. 路由匹配规则

按特异性从高到低匹配，accountId匹配 > 通道匹配，第一个匹配的binding生效

## 4. 常见配置错误

❌ 缺少bindings配置 → 所有消息路由到第一个Agent

❌ accountId不匹配 → 消息无法正确路由

❌ JSON格式错误 → 配置无法加载

# 避坑指南

## 1. 配置检查清单

agents.list中所有Agent已定义

channels.accounts中所有账户已配置

bindings中所有账户到Agent的映射已设置

JSON格式正确无误

Gateway已重启生效

## 2. 调试技巧

查看Gateway日志：tail -f /tmp/openclaw/openclaw-\*.log

检查路由决策：在日志中搜索dispatching to agent

验证配置：openclaw config get bindings

测试单个机器人：逐步测试每个机器人的路由

# 结语

OpenClaw的多Agent架构非常强大，但正确的配置是关键。bindings配置是多Agent路由的核心，缺少它会导致所有消息被错误路由。通过这次实战，我们不仅解决了具体问题，更深入理解了OpenClaw的路由机制。

关键收获：

1. 阅读官方文档是解决问题的捷径
2. bindings是多Agent路由的必备配置
3. 系统化的诊断方法比盲目尝试更有效
