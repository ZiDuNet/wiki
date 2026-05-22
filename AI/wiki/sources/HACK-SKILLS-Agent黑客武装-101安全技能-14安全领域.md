---
tags: [安全, 渗透测试, Web安全, CTF, Skill, Agent, GitHub, 开源]
source: "GitHub"
created: 2026-05-22
updated: 2026-05-22
category: 安全工具
---

# HACK.SKILLS - Agent 的黑客武装

> 来源: [yaklang/hack-skills](https://github.com/yaklang/hack-skills) | Apache-2.0 | 101 Skills

## 摘要

由 Yaklang 团队出品的 Agent 安全技能知识库，覆盖 Web 安全、API 安全、认证授权、OS 提权、AD 攻击、移动安全、二进制漏洞利用（Pwn）、逆向工程、密码学攻击、区块链与智能合约安全、AI/ML 安全、网络协议与横向移动、数字取证等 **14 个安全领域**，共 **101 个深度专题 Skill**。

面向漏洞赏金、渗透测试、CTF 竞赛和授权安全研究。

## 架构设计

**三层加载模型：**

1. **总入口 (hack)** — 全局路由、测试排序、跨类别切换
2. **分类入口 (6个)** — 按攻击面路由到稳定主题族（recon-for-sec、api-sec、auth-sec、injection-checking、file-access-vuln、business-logic-vuln）
3. **深度专题 (101个)** — 完整攻击手册和执行细节，按需加载

每个 Skill 独立目录：`skills/{semantic-identifier}/SKILL.md`

## 14 大安全领域

| 领域 | 代表性 Skill | 亮点 |
|---|---|---|
| 侦察与方法论 | recon-and-methodology | Java中间件指纹矩阵、泄露检测清单 |
| API 安全 | api-recon-and-docs, graphql-and-hidden-parameters | OpenAPI/Swagger发现、JWT攻击 |
| 认证与授权 | authbypass-authentication-flaws, idor-broken-object-authorization | 密码重置22模式矩阵、验证码绕过20法 |
| 注入攻击 | xss-cross-site-scripting, sqli-sql-injection, ssti-server-side-template-injection | 15+模板引擎覆盖、WAF绕过矩阵 |
| 文件与路径 | path-traversal-lfi, upload-insecure-files | LFI-to-RCE 7路径、PHP wrapper矩阵 |
| 业务逻辑 | business-logic-vulnerabilities, race-condition | 支付篡改矩阵、HTTP/2单包攻击 |
| 高级Web安全 | waf-bypass-techniques, request-smuggling, csp-bypass-advanced | Cloudflare/Akamai绕过、HTTP走私 |
| 基础设施与网络 | unauthorized-access-common-services, insecure-source-code-management | .git恢复、反向代理误配 |
| OS 提权 | linux-privilege-escalation, windows-privilege-escalation, macos-privilege-escalation | SUID/Capabilities/GTFOBins |
| Active Directory | active-directory-kerberos-attacks, active-directory-acl-abuse | Kerberos攻击链、ADCS利用 |
| 移动安全 | android-pentesting-tricks | APK逆向、Frida hook |
| 二进制/Pwn | binary-exploitation-stack, binary-exploitation-heap, format-string-exploitation | 栈/堆利用、ROP链 |
| 密码学 | classical-cipher-analysis, cryptographic-attacks | RSA攻击、格攻击 |
| AI/ML 安全 | ai-ml-security, llm-security | LLM注入、模型窃取 |
| 区块链 | defi-attack-patterns, smart-contract-security | DeFi闪电贷攻击、合约审计 |
| 逆向工程 | reverse-engineering-methodology, anti-debugging-techniques | 反调试、代码混淆/去混淆 |
| 网络协议与横向移动 | network-pivoting, container-escape-techniques | 容器逃逸、隧道穿透 |
| 数字取证 | digital-forensics-methodology | 内存取证、磁盘分析 |

## 知识来源（蒸馏层）

不是简单搬运，而是从公开安全知识库中蒸馏提炼：

- PayloadsAllTheThings → 场景化索引、方法矩阵
- PentesterSpecialDict → 参数命名模式、中间件指纹矩阵
- Dictionary-Of-Pentesting → 绕过模式矩阵、WAF厂商绕过分节
- Hello-CTF / ctf-wiki → CTF特定技术、二进制利用技术
- hacktricks → OS级提权手册、AD攻击链
- 公开CVE公告 → 攻击模式矩阵、决策树

## 安装

```bash
npx skills add yaklang/hack-skills
```

## 在线浏览

- 网页版: https://skills.hackbenchmark.com（模糊搜索、分类侧栏、等级筛选）
- 离线加密 ZIP: AES-256，密码 `hack-skills`

## 相关实体

- [[yaklang]], [[Skill]], [[Agent]], [[GitHub]], [[Web安全]], [[渗透测试]], [[CTF]]

## 相关概念

- [[安全技能蒸馏]]
- [[三层加载模型]]
- [[Agent 安全能力]]
