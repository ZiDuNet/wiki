> 📎 来源: [思考家](https://mp.weixin.qq.com/s?__biz=MzA4OTc4NDExOQ==&mid=2651294071&idx=1&sn=c6484b116846d0275172e3562331c0df&chksm=8a82f72ff1add69b189e67d417147865b2ab346cd5f966c4fef630092a2c5c3f6964cc0fc9a1&mpshare=1&scene=1&srcid=0511B1tpDLBh9llVKtaY9Ajf&sharer_shareinfo=bc92c33bef7d5821c6f12fda1511489e&sharer_shareinfo_first=bc92c33bef7d5821c6f12fda1511489e) | 时间: 2026-05-11 00:09

---

---

## 写在前面的话:"DeerFlow 企业版 是基于开源 DeerFlow2 的生产就绪分支，为企业团队使用补齐了身份认证、多租户隔离、安全加固和运营审计能力。企业开源版本使用Claude code 手搓。

如果 DeerFlow 2.0 是极客的玩具，那这个版本就是团队的生产级武器。

它保留了上游所有能力——Sub-Agent、Skills、沙箱执行、MCP、IM 集成——同时为企业团队补齐了自托管所必须的身份认证、多租户隔离、安全加固和运营审计能力。

上游适合本地单兵作战；这个分支，适合 2~50 人的团队在私有环境中安全共享。

---

## 企业级身份与访问控制：不再裸奔

![](assets/img_24bfcf8bf9f7.jpg)

DeerFlow 企业版支持 **OIDC + 密码登录并行**，可以对接 Okta、Azure AD、Keycloak 等主流 SSO 方案。密码登录作为备份通道，服务账号、紧急访问都能正常走通。

**自服务注册码**是一大亮点：管理员一键生成单次注册码，团队成员扫码即可入驻，完全不需要邮件服务器。

首次启动时，只需配置 

```
DEERFLOW_BOOTSTRAP_ADMIN_EMAIL
```

，平台管理员自动创建，开箱即用。JWT 认证采用 RS256 算法，

```
make identity-keys
```

 即可生成 2048 位密钥对，网关启动时自动检测缺失并生成。

---

## 多租户隔离：数据不会串门

![](assets/img_6deaa5599210.jpg)

这是企业版与上游最本质的区别。

每个租户拥有**物理隔离的文件系统**：沙箱挂载、线程数据、上传输出、Skill 目录严格分离。跨租户访问在网关、沙箱层、路径守卫三层同时拒绝，想越界？没门。

列表线程接口不再跨用户泄露，共享部署不再裸奔。

```
workspace_member
```

 角色为受邀用户量身定制了权限集，权限边界清晰。

---

## 安全加固：P0 漏洞已全部修复

DeerFlow 企业版修复了多个高危安全问题：

![](assets/img_252eeef8b2bf.jpg)

**网关认证基线**：14 个遗留 

```
/api/*
```

 路由默认开启认证，

```
PUBLIC_PREFIXES
```

 白名单显式管理豁免路径，彻底关闭了 

```
ENABLE_IDENTITY=true
```

 情况下仍留有后门的 P0 漏洞。

**会话弹性**：401 响应自动触发单飞刷新重试（Singleflight），不再出现「会话过期」弹窗打断长任务。身份层与 LangGraph SDK 层共享同一重试机制，体验流畅。

**Cookie TTL 解耦**：

```
deerflow_session
```

 的 Max-Age 现在跟踪 

```
refresh_ttl_sec
```

（7 天），而非 

```
access_ttl_sec
```

（15 分钟）。关笔记本过夜，不再被踢下线。

**审计流水线**：所有写操作、RBAC 拒绝、登录登出、工具拒绝均经 

```
AuditMiddleware
```

 → 

```
audit_logs
```

 表落地。Postgres 不可达时关键事件落盘为 JSONL，修复后自动回填，支持游标分页 CSV 导出。合规审计，不再是难题。

---

## Skill 与 Agent 治理：从 DIY 到有序

DeerFlow 企业版引入了 **Skill 审批工作流**：待发布 Skill 经 

```
GET /api/admin/skills/pending
```

 → 批准/拒绝，管理后台显示待审 / 已审（拒绝 + 归档）标签页。

Skill 可以绑定到线程：通过 

```
POST /api/threads/{tid}/skills
```

 绑定 Skill，聊天界面显示 

```
/skill-name
```

 徽章，「加载到聊天」深度链接端到端可用。

自定义 Agent 编辑页支持从 UI 编辑 

```
description / model / SOUL / tool_groups / skills / org_key_env
```

，

```
tool_groups
```

 下拉菜单调用 

```
GET /api/tool-groups
```

，管理后台也增强了模型管理、密码修改、i18n 标签等功能。

---

## 运行时稳定性：那些年踩过的坑，都修了

**Gateway 模式事件循环单例**：通过 lifespan 注册进程级事件循环，彻底消除了长会话及跨 Sub-Agent 边界场景下的「Event loop is closed」错误。

**摘要级联修复**：历史摘要标记现在正确存储在 

```
additional_kwargs
```

 中，下一轮作为 

```
prior_summary
```

 种子而非再次被摘要，历史摘要不再被压扁。

**工具调用恢复**：

```
LoopDetectionMiddleware
```

 硬停现在会为同轮漂移的 

```
ToolMessage
```

 发出 

```
RemoveMessage
```

，防止严格校验 

```
tool_call_id
```

 序列的模型供应商抛出 400。

---

## 快速上手：7 步跑起来

![](assets/img_b65ae0274048.jpg)

### 1. 克隆代码

```
git clone https://github.com/HE1780/deer-flow-by-cc.gitcd deer-flow-by-cc
```

### 2. 启动依赖服务

```
docker compose up -d postgres redis
```

### 3. 执行数据库迁移

```
cd backend && make db-upgrade
```

### 4. 生成 JWT 密钥

```
cd backend && make identity-keys
```

### 5. 配置环境变量

```
# .envENABLE_IDENTITY=trueDEERFLOW_DATABASE_URL=postgresql+asyncpg://deerflow:***@localhost:5432/deerflowDEERFLOW_REDIS_URL=redis://localhost:6379/0DEERFLOW_BOOTSTRAP_ADMIN_EMAIL=you@example.comREGISTRATION_CODE_EXPIRES_DAYS=7
```

### 6. （可选）配置 OIDC

```
cp config/identity.yaml.example config/identity.yaml# 编辑 $PROVIDER_VAR 引用从环境变量解析
```

### 7. 启动服务

```
make dev   # 或 make up 用于生产 Docker 部署
```

---

## 我该用哪个版本？

         

| 你的场景 | 用上游 | 用这个版本 |
| --- | --- | --- |
| 单开发者、本地使用 | ✅ | — |
| 笔记本评测 / Demo | ✅ | — |
| 团队自托管（2~50 人） | — | ✅ |
| 需要真实登录（OIDC 或密码） | — | ✅ |
| 需要租户数据隔离 | — | ✅ |
| 需要合规审计日志 | — | ✅ |
| 需要 Skill 上线审批流程 | — | ✅ |

       
> **升级路径**：这个分支是上游的严格超集，只需重定向 git remote 并运行 

> ```
> make db-upgrade
> ```

> ；

> ```
> ENABLE_IDENTITY=false
> ```

>  时现有部署行为与上游完全一致。

---

## 总结

DeerFlow 企业版不是上游的替代品，而是上游的**生产级扩展**。

如果你是个人开发者，上游依然是最优选择。但当你的场景升级到团队协作、私有部署、合规审计，DeerFlow 企业版就是你需要的那把武器。

GitHub：HE1780/deer-flow-by-cc

---

**推荐阅读**：

- DeerFlow 上游仓库
- DeerFlow 企业版完整设计文档（见项目 

  ```
  docs/superpowers/specs/archive/
  ```

  ）
