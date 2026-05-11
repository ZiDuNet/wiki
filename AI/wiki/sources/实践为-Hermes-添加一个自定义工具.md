---
tags: [Hermes, Agent, GitHub, API, Python, Skill]
source: "Preface Lab"
created: 2026-04-25
updated: 2026-05-10
category: Hermes
---

# 实践：为 Hermes 添加一个自定义工具

> 来源: [Preface Lab](https://mp.weixin.qq.com/s?__biz=MzE5MTM0NTQ1MA==&mid=2247483928&idx=1&sn=15bf8c6aed1372b88c57ed14f0ec147b&chksm=97ed80580f6403029251f784709f1bdb3cec0bd81c8fe1ed1a2c99f330b1259e59fff8c8b500&mpshare=1&scene=1&srcid=0425o2vFvklQ4COxQZPd8u9S&sharer_shareinfo=03e0cbffbfba3a327d5c4daa92844105&sharer_shareinfo_first=03e0cbffbfba3a327d5c4daa92844105) | 2026-04-25

## 摘要

- 1. 本章目标与前置准备
- 2. 工具设计：从需求到 Schema
- 3. 步骤一：创建工具文件
- 4. 步骤二：实现 Handler
- 5. 步骤三：注册到工具系统
- 6. 步骤四：添加到发现列表
- 7. 步骤五：验证工具可用
- 8. 完整代码
- 9. 常见问题与调试
- 10. 举一反三：更多工具示例
通过为一个真实需求创建完整工具，掌握：
**```
currency_convert
输入：amount（金额）、from_currency（源货币）、to_currency（目标货币）输出：转换后的金额、汇率、转换时间示例：  用户：100 美元换成人民币是多少？  工具调用：currency_convert(amount=100, from_currency="USD", to_currency="CNY")  返回：{"success": true, "amount": 725.50, "rate": 7.255, "from": "USD", "to": "CNY"}  Hermes 回复："100 美元 = 725.50 人民币（汇率 1:7.255）"...

## 相关实体

[[GitHub]], [[Hermes]], [[Python]]

## 相关概念


