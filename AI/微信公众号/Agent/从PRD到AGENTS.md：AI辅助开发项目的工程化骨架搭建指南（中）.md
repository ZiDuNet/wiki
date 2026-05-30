> 📎 来源: [AI系统架构](https://mp.weixin.qq.com/s?__biz=MzYzMTkxMDk5OA==&mid=2247483659&idx=1&sn=6adc98ad1b6b7cfbfca6d569e6529053&chksm=f1c21b25385cf5e54ec96c75122a5e68b5efe238f8f2ffaef0b918df9cda1cc3b64774ecadda&mpshare=1&scene=1&srcid=0530OzQUzOvgJRM16FQ8PfKz&sharer_shareinfo=bba32f898f191b66fc6aa124bbaff31c&sharer_shareinfo_first=bba32f898f191b66fc6aa124bbaff31c) | 时间: 2026-05-30 13:34

---

> 上篇已经完成方法论、跨工具策略、RBAC 示例技术栈和七步骨架搭建流程。本篇进入可落地的核心资产：AGENTS.md、CLAUDE.md、Skills、子代理、Rules、MCP、Hooks 与权限门禁。

**版本漂移声明**：本文涉及的 Claude Code、Codex CLI、Cursor 等工具仍在快速演进，Skills frontmatter 字段、subagents 机制、MCP 配置位置、Hooks 能力、sandbox/approval 策略等均可能随版本变化。本篇所有工具专属配置以 2026 年初主流版本为准；真正落地时请以各工具当前官方文档为权威来源，本文不再对每一处单独声明。

**本篇目录**

- AGENTS.md：跨工具规则源
- CLAUDE.md：工具专属薄壳
- Skills：把高频任务固化成 SOP
- 子代理与 Rules：审查和约束分层
- MCP、Hooks 与权限门禁

## 六、AGENTS.md：跨工具的唯一真实来源

```
AGENTS.md
```

 是标准 Markdown，没有必需字段，但有几类内容几乎所有项目都该写 [1]：项目概述、构建和测试命令、代码风格、测试要求、安全注意事项、PR 规则。

```
# RBAC Service — Agent Instructions## 项目概述通用 RBAC 权限中台。后端 Java 17 + Spring Boot 3，前端 Vue 3，存储 PostgreSQL 16 + Redis 7。所有受保护接口必须经JwtAuthenticationFilter 和方法级 @PreAuthorize 双层校验。## 仓库布局- backend/  Spring Boot 后端（Maven）- frontend/ Vue 3 前端（pnpm）- 其余见根目录 README## 环境准备- JDK 17（推荐 Temurin），Maven Wrapper 已内置- Node.js 20.x，pnpm 9.x- Docker 24+（本地 PG + Redis）- 启动依赖：`docker compose up -d`- 环境变量：复制 .env.example 到 .env，填写 DB_PASSWORD、  JWT_SECRET、REDIS_PASSWORD## 常用命令（Agent 请逐字使用）### 后端（在 backend/ 目录）- 启动开发：`./mvnw spring-boot:run`- 单元测试：`./mvnw test`- 集成测试：`./mvnw verify -P integration`- 代码检查：`./mvnw spotless:check`- 自动格式化：`./mvnw spotless:apply`- DB 迁移：本项目默认走 Spring Boot 启动时自动 migrate（由 `spring-boot-starter-flyway` 读取 `spring.datasource.*`）；如需单独执行，启用 flyway-maven-plugin 并配置其专属连接信息后再用 `./mvnw flyway:migrate`，两套配置互相独立- 打包：    `./mvnw clean package -DskipTests`### 前端（在 frontend/ 目录）- 启动开发：`pnpm dev`- 单元测试：`pnpm test`- e2e 测试：`pnpm test:e2e`- 类型检查：`pnpm typecheck`- 代码检查：`pnpm lint`- 构建：    `pnpm build`## 代码规范### 后端- 本项目使用 Java 17 作为编译基线，可使用 record、sealed、text block、instanceof pattern matching 等 Java 17 之前已转正的特性；需要更高版本能力（如 switch pattern matching）时先讨论- 包结构：按领域分（auth/user/role/permission/common），禁按分层分- 每个领域内分 `controller / service / mapper / entity / dto`- Controller 只做 HTTP 编排，业务逻辑在 Service，持久化在 Mapper- 所有请求 DTO 必须带 Jakarta Validation 注解- DTO 与 Entity 之间用 MapStruct 转换- 详见 @rules/backend/spring-patterns.md### 前端- Vue 3 一律用 `<script setup lang="ts">` + Composition API- 状态放 Pinia store，API 调用集中在 `src/api/`- 组件 PascalCase，组合式函数 `useXxx` 形式- 详见 @rules/frontend/vue-patterns.md### 注释统一使用中文前后端所有代码注释、JSDoc、Javadoc 一律使用中文，便于团队成员与 AI 协作时语义对齐。变量、函数、类型名等标识符保持英文。## RBAC 核心约束（Always）- 任何新 HTTP 接口必须挂 `@PreAuthorize("hasAuthority('<res>:<act>')")`  或在 SecurityConfig 明确放行- 权限码一律 `<resource>:<action>` 形式- 推荐由 Controller 通过 `@AuthenticationPrincipal` 获取当前用户，  再以显式参数传给 Service，便于测试与依赖追踪；审计、事件监听、  定时任务等横切关注点可例外使用 `SecurityContextHolder`- 新增/修改 Flyway 脚本必须带时间戳版本号- 任何涉及权限校验的改动必须有对应 `@SpringBootTest` e2e 用例- 权限数据变更后必须清理 Redis key `rbac:perms:{userId}`## 测试要求- 后端覆盖率阈值 80%（Jacoco）— 示例阈值，团队可据实调整- 前端 Vitest 覆盖率阈值 70%— 示例阈值，团队可据实调整- 新增 Filter / Guard / 拦截器必须配套单测 + 集成测试- 失败测试不得 @Disabled 或 .skip 跳过## 安全要求- 禁止硬编码密钥，通过 `@ConfigurationProperties` 读取- SQL 一律走 MyBatis-Plus；手写 SQL（XML Mapper / `@Select`）时用户输入值必须用 `#{}` 绑定，条件构造器优先使用 `eq/like/in` 等方法，避免 `apply()` 拼接字符串；确需动态排序字段、表名等标识符时只能来自枚举白名单- 鉴权失败统一走 `AuthEntryPointJwt`，只返回 401/403 + traceId- 前端禁止使用 `v-html` 渲染用户输入- 详见 @rules/common/security.md## PR 规则- 标题：`[rbac] <type>: <subject>`（type ∈ feat/fix/refactor/perf/chore）- 必须通过：后端 `./mvnw verify`、前端 `pnpm lint && pnpm typecheck && pnpm test`- 敏感改动（权限/认证/迁移）打标签 `needs-security-review`
```

**要点**：命令写**可执行的精确字符串**，Agent 会逐字复用 [3]；详细规则拆到 

```
rules/
```

 小文件，用 

```
@path/to/file
```

 引用，Claude Code 支持递归 5 层嵌套 [3]。

---

## 七、CLAUDE.md：Claude 专属薄壳

多工具并存时，

```
CLAUDE.md
```

 退化成轻量壳，只加 Claude 特性 [3]：

```
# CLAUDE.md — Claude Code 专属配置所有通用规则见 @AGENTS.md，本文件只补充 Claude 的行为约定。## Skills 优先级（匹配即用，禁止临场发挥）- 新增 Controller 接口 → @skills/rbac-permission-check/SKILL.md- 修改 schema / 加表加字段 → @skills/flyway-migration/SKILL.md- 读写 Redis → @skills/redis-cache-pattern/SKILL.md- 前端新增页面/模块 → @skills/vue3-feature-module/SKILL.md- 写测试 → @skills/tdd-workflow/SKILL.md## 子代理调度- 架构级决策 → 委托 planner- 修改 backend/**/security/** 或 auth/** → 必须经 security-reviewer- 修改 src/main/resources/db/migration/** → 必须经 db-migration-reviewer## 会话纪律- 每个微任务完成后 git commit- 切换任务前 /clear，长对话用 /compact- 超过 30 分钟的任务先 Plan Mode（Shift+Tab）## 语言中文对话；前后端代码注释统一中文；标识符保持英文
```

Cursor 直接在 

```
.cursor/rules/
```

 下放 

```
.mdc
```

 文件，YAML frontmatter 控制激活 [2]；Codex 用 

```
.codex/config.toml
```

 控制 sandbox/approvals。实践中可以让这些工具专属文件尽量只做薄壳，显式引用或同步根目录 

```
AGENTS.md
```

，避免多份规则长期漂移。

---

## 八、Skills：跨工具可复用的工作流

下面的代码和配置模板用于约束 AI 输出结构，帮助模型稳定执行项目约定。生产落地时仍需结合实际框架版本、安全要求和团队规范调整，不能把示例直接等同于最终生产代码。

Skills 是 Claude Code、Codex 等工具正在采用的主要工作流载体。以 Claude Code 官方规范为例，

```
SKILL.md
```

 的 YAML frontmatter 只有两个字段：

```
name
```

 和 

```
description
```

，两者都必填；发现机制完全依赖 

```
description
```

 中的关键词匹配，没有 

```
triggers
```

 / 

```
tools
```

 这类额外字段 [2]。其他工具（Codex、Cursor）虽然借用了 Skills 概念，但安装位置、触发机制和扩展字段会因实现而异。更稳妥的做法是：把 SOP 写成符合 Claude Code 规范的 

```
SKILL.md
```

，再按各工具要求放置、安装或引用。本质上，Skill 是被触发时替代临场发挥的标准作业程序（SOP）。

### 示例 1： ``` skills/rbac-permission-check/SKILL.md ```

```
---name: rbac-permission-checkdescription: 为新增或修改的 Spring MVC 接口挂载正确的 RBAC 权限注解，  并补齐 401/403/200 测试路径。适用于修改  backend/**/*Controller.java、新增 @GetMapping/@PostMapping/  @PutMapping/@DeleteMapping 或讨论接口权限校验时。---# RBAC 权限校验工作流## 触发场景用户要求在 Controller 中新增或修改 HTTP 接口时执行本 Skill。## 执行步骤### 1. 识别资源与动作- 路径推资源：`/api/users/**` → `user`；`/api/roles/{id}/permissions` → `role`- 方法推动作：GET→read, POST→create, PUT/PATCH→update, DELETE→delete- 语义动作使用显式动词：`assign`、`revoke`、`reset`、`lock`### 2. 决定校验方式- 首选方法级 `@PreAuthorize("hasAuthority('<res>:<act>')")`- 多权限任一：`hasAnyAuthority('a:x','a:y')`- 粗粒度角色入口：`hasRole('ADMIN')`- 禁止出现无 @PreAuthorize 也未在 SecurityConfig 显式放行的受保护接口### 3. 实现模板（注释全中文）\`\`\`java/** * 用户管理控制器 * 提供用户的增删改查接口，受 RBAC 权限约束 */@RestController@RequestMapping("/api/users")@RequiredArgsConstructorpublic class UserController {    private final UserService userService;    /**     * 创建用户     * @param dto       创建用户入参（需通过 Jakarta Validation 校验）     * @param operator  当前登录用户，由 Spring Security 自动注入     * @return 新创建的用户视图对象     */    @PostMapping    @PreAuthorize("hasAuthority('user:create')")    public ApiResponse<UserVO> create(            @Valid @RequestBody CreateUserDTO dto,            @AuthenticationPrincipal LoginUser operator) {        return ApiResponse.ok(userService.create(dto, operator.getId()));    }}\`\`\`### 4. 补齐测试（TDD 顺序）在 `backend/src/test/java/**/controller/` 新增 `*ControllerIT.java`，使用 `@SpringBootTest` + `MockMvc`，至少覆盖：- 无 token → 401- 有 token 但缺权限 → 403- 有 token 且权限正确 → 200 + 响应体断言- 可选：幂等/边界### 5. 验证- `./mvnw test -Dtest=<NewControllerIT>` 通过- `./mvnw spotless:check` 无报错- 新增权限码必须同步到 `src/main/resources/db/migration/` 的种子脚本## 禁止事项- 不在 Service 层的业务主流程中用 SecurityContextHolder 读当前用户  应由 Controller 使用 `@AuthenticationPrincipal LoginUser` 获取当前用户，再以显式参数传给 Service；  审计、事件监听、定时任务等横切关注点可例外- 不为了绕权限把接口迁到 `/public/**`- 不在 Controller 直接访问 Mapper，必须走 Service## 完成后更新 memory-bank/architecture.md 中的权限码表。
```

### 示例 2： ``` skills/flyway-migration/SKILL.md ```

```
---name: flyway-migrationdescription: 安全创建和执行 Flyway 数据库迁移。适用于新增或修改  backend/src/main/resources/db/migration/ 下的 SQL 脚本、  讨论加字段/改表结构、数据回填或迁移回滚方案时。---# Flyway 迁移工作流## 步骤1. 读 `backend/src/main/resources/db/migration/` 最新文件确认当前版本2. 新建 `V{yyyyMMddHHmm}__.sql`，如   `V202601151030__add_user_locked_column.sql`3. SQL 规则   - 新增字段优先 NULLable；如需 DEFAULT / NOT NULL，大表生产环境按“加字段 → 回填 → 加约束”分步执行   - 索引语句使用 `CREATE INDEX CONCURRENTLY`（PG 支持）   - 禁止 `DROP COLUMN` / `DROP TABLE` 不经人工确认   - UPDATE 必须带 WHERE   - SQL 内注释统一中文 `-- 中文说明`4. 本地验证：默认通过 `./mvnw spring-boot:run` 让 Spring Boot 自动 migrate；若项目启用了 flyway-maven-plugin，可用 `./mvnw flyway:migrate` 单独执行（两者配置独立，确认使用哪一条）5. 回滚预案：写明手工回滚 SQL 或恢复步骤，仅作为预案记录；不要假设默认 Flyway Community 能执行 undo 脚本6. 若影响实体，同步修改 `*Entity.java` 与 MyBatis-Plus 注解7. 提交包含：SQL 脚本 + Entity + 相关 Mapper + 测试## 风险点- 重命名字段走三步：加新字段 → 双写迁移 → 删旧字段- 加 UNIQUE 约束前必须先数据清洗- 生产环境 `ALTER TABLE` 加字段 + 默认值 + NOT NULL 需分三步
```

### 示例 3： ``` skills/redis-cache-pattern/SKILL.md ```

```
---name: redis-cache-patterndescription: Spring Data Redis 读写的标准模式，避免击穿、穿透、雪崩。  适用于新增或修改缓存逻辑、设计 Redis key/TTL、处理权限缓存失效、  出现大 key 或 KEYS 命令讨论时。---# Redis 缓存工作流## Key 命名约定- 业务前缀 + 对象 + 主键：`rbac:perms:{userId}`、`rbac:refresh:{userId}:{jti}`、`rbac:jwt:blk:{jti}`- TTL 必须显式设置，禁止无 TTL 长期驻留- 权限集 TTL 1800s，刷新 token TTL 7d，黑名单 TTL = token 剩余寿命## 读缓存模板（Cache-Aside，注释全中文）\`\`\`java/** * 加载指定用户的权限码集合 * 先查 Redis，未命中再回源 DB 并回写缓存 * 空结果使用短 TTL 占位，防止缓存穿透 * * @param userId 用户主键 * @return 权限码集合，形如 ["user:read", "role:assign"] */public Set<String> loadPermissions(Long userId) {    String key = "rbac:perms:" + userId;    // 单独的 nullKey 是一种实现选择：权限集存储为 Set 类型，与空值哨兵的标量类型冲突，    // 所以拆成两个 key。另一种等价方案是权限集改用 JSON 字符串存储，用同一个 key 存哨兵值    String nullKey = key + ":null";    // 命中空值占位，说明短时间内已确认该用户无权限    if (Boolean.TRUE.equals(redisTemplate.hasKey(nullKey))) return Set.of();    // 先尝试从缓存读取（key 不存在时返回空 Set，不会为 null）    Set<String> cached = redisTemplate.opsForSet().members(key);    if (!cached.isEmpty()) return cached;    // 缓存未命中，回源数据库    Set<String> db = permissionMapper.selectCodesByUserId(userId);    if (db.isEmpty()) {        // 防穿透：空值也缓存 60 秒，避免恶意刷库        redisTemplate.opsForValue().set(nullKey, "1", Duration.ofSeconds(60));        return db;    }    // 回写缓存并显式设置 TTL；SADD + EXPIRE 在同一 SessionCallback 中执行，    // 避免 EXPIRE 失败后留下无 TTL 的长驻 key    String[] codes = db.toArray(String[]::new);    redisTemplate.executePipelined((RedisCallback<Object>) conn -> {        byte[] rawKey = key.getBytes(StandardCharsets.UTF_8);        byte[][] rawVals = Arrays.stream(codes)                .map(s -> s.getBytes(StandardCharsets.UTF_8))                .toArray(byte[][]::new);        conn.setCommands().sAdd(rawKey, rawVals);        conn.keyCommands().expire(rawKey, Duration.ofMinutes(30).getSeconds());        return null;    });    return db;}\`\`\`## 失效策略- 角色权限变更 → 扫描受影响用户 ID，批量 DEL `rbac:perms:{id}` 与 `rbac:perms:{id}:null`- 用户角色变更 → 仅 DEL 该用户的权限 key 与空值占位 key- 删除操作使用 UNLINK（异步）避免大 key 阻塞## 禁止事项- 不使用 KEYS 命令扫描（O(N) 阻塞），用 SCAN- 不把大对象（>10KB）整块塞进单 key- 不在数据库事务中直接写 Redis；应在事务提交后失效缓存，必要时用事务后事件或消息补偿，避免 DB 回滚但缓存已变更
```

### 示例 4： ``` skills/vue3-feature-module/SKILL.md ```

```
---name: vue3-feature-moduledescription: 按约定新增 Vue 3 功能模块，同步产出页面、Pinia store、  API 层和路由配置。适用于新增 views/<feature>/、创建  stores/<feature>.ts、接入后端新接口或讨论前端权限指令时。---# Vue 3 功能模块工作流## 目录约定新增模块 ``（如 user、role）需在以下位置同时产出文件：\`\`\`frontend/src/├── api/<feature>.ts         # axios 调用，返回 Promise<T>>├── stores/<feature>.ts      # Pinia store，仅存必要状态├── views/<feature>/│   ├── List.vue             # 列表页│   ├── Form.vue             # 新建/编辑│   └── components/└── router/modules/<feature>.ts  # 路由定义（带 meta.permission）\`\`\`## 路由权限元数据（注释全中文）\`\`\`ts// 用户管理模块路由// meta.permission 用于路由守卫校验登录用户是否具备该权限码{  path: '/users',  component: () => import('@/views/user/List.vue'),  meta: { title: '用户管理', permission: 'user:read', icon: 'User' }}\`\`\``router.beforeEach` 中根据 meta.permission 匹配 Pinia 中的权限集，无权限跳 403 页。## API 层模板（注释全中文）本模板假设 `@/utils/request` 中已配置 axios 响应拦截器：自动拆包后端 `ApiResponse` 的 `data` 字段，错误码统一抛异常。调用方拿到的是 `Promise`，而非 `Promise>>`。\`\`\`tsimport request from '@/utils/request'import type { PageQuery, PageResult, UserVO, CreateUserDTO } from '@/types'/** * 分页查询用户列表 * @param q 分页与筛选参数 * @returns 拦截器拆包后的分页结果（非完整 AxiosResponse） */export const listUsers = (q: PageQuery) =>  request.get<UserVO>>('/users', { params: q })/** * 创建用户 * @param dto 新建用户表单数据 * @returns 拦截器拆包后的新建用户 VO */export const createUser = (dto: CreateUserDTO) =>  request.post<UserVO>('/users', dto)\`\`\`## 组件要求- 列表页必须带：分页、搜索、按钮级权限控制指令 `v-perm="'user:create'"`- 表单页用 Element Plus 的 `<el-form>` + async-validator- 所有用户输入展示前 escape，禁止 v-html- 加载态使用 VueUse 的 `useAsyncState` 或自研 `useRequest`- `<template>` 中的关键逻辑块使用 `` 注释## 验证- `pnpm typecheck` 无错误- `pnpm test` 相关组件快照/交互用例通过- 手测：无权限账号访问路由跳 403，按钮隐藏
```

Skills 的价值：同一段 SOP 在三个工具里都能被识别复用，避免「Claude 写的接口带校验、Codex 写的漏掉注解」这种不一致 [2]。

---

## 九、子代理与多角色

Claude Code 子代理放 

```
.claude/agents/.md
```

[2]，Codex 多代理角色放 

```
.codex/agents/.toml
```

[2]。

**```
.claude/agents/security-reviewer.md
```**

```
---name: security-reviewerdescription: 审查 RBAC 权限、Spring Security 配置、SQL 注入、越权风险tools: [Read, Grep, Glob, Bash]model: opus---你是专注 Java Web 安全与 RBAC 的高级审查员。对指定 diff 执行：1. 权限注解覆盖审计   - 所有新增/修改 Controller 方法必须带 @PreAuthorize     或在 SecurityConfig 显式放行   - 权限码格式必须 :2. 认证链路审查   - JwtAuthenticationFilter 是否在 UsernamePasswordAuthenticationFilter 之前   - token 解析失败是否被 AuthEntryPointJwt 捕获而非 5003. 数据流审查   - Service 层业务主流程不直接使用 SecurityContextHolder，当前用户由 Controller 显式传入；     审计、事件监听、定时任务等横切关注点可例外   - 用户输入经 DTO + Jakarta Validation   - 用户输入值在手写 SQL（XML/@Select）中必须用 #{}；条件构造器避免 `apply()` 字符串拼接；动态标识符只能来自枚举白名单4. Redis 安全   - 缓存 key 不包含用户可控原始字符串（防缓存投毒）   - 权限变更路径必须触发 DEL rbac:perms:*5. 越权测试覆盖   - 每个新接口必须有「缺权限→403」的 MockMvc 测试输出：Critical/High/Medium/Low 分组，每条给文件+行号+修复建议。
```

**```
.codex/agents/reviewer.toml
```**

```
[agent]name = "reviewer"description = "Spring Security + RBAC 覆盖性与正确性审查"[agent.tools]read = truegrep = trueshell = { approval = "ask" }edit = false[agent.instructions]file = "./reviewer-instructions.md"
```

如果当前 Codex CLI 版本支持 subagents，可以在 

```
.codex/agents/
```

 或等效位置配置角色并用对应命令调用；不支持时用新会话交叉审查替代 [2]。

---

## 十、Rules：模块化规则

Rules 是「始终遵守」的约束，分层组织让不同语言/模块互不干扰 [2]。

**```
rules/common/security.md
```** 片段：

```
# 安全基线## 密钥与凭证- 禁止硬编码：API key、JWT secret、DB 密码、Redis 密码- 后端通过 @ConfigurationProperties + 环境变量；前端通过 import.meta.env- 提交前扫描：`git diff --cached | grep -iE '(secret|token|password|api.?key)'`## 注入防御- SQL：手写 SQL（XML Mapper / `@Select`）时用户输入值必须用 `#{}`；条件构造器优先使用 `eq/like/in` 等方法，避免 `apply()` 拼接字符串；动态排序字段、表名等标识符只能来自白名单枚举- Shell：ProcessBuilder 传数组，禁 Runtime.getRuntime().exec(String)- HTML/Vue：禁 v-html 渲染用户输入## 鉴权失败- 后端：401/403 + traceId，不返回堆栈或内部字段- 前端：401 跳登录，403 跳 403 页，不在 toast 泄露细节## 注释语言- 前后端代码注释、Javadoc、JSDoc、SQL 注释全部使用中文- 标识符（类/方法/变量/表字段）保持英文- Git commit message 使用中文或英文均可，但同一仓库保持一致
```

**```
.cursor/rules/30-rbac-security.mdc
```**

```
---description: RBAC 权限校验与安全规则globs: ["backend/**/*Controller.java", "backend/**/security/**",        "backend/src/main/resources/db/migration/**"]alwaysApply: true---Controller 方法必须挂 @PreAuthorize。SecurityFilterChain 中JwtAuthenticationFilter 必须在 UsernamePasswordAuthenticationFilter之前。所有注释使用中文。详见 @AGENTS.md 与 @rules/common/security.md。
```

---

## 十一、MCP、Hooks、权限门禁

**```
.mcp.json
```**（MCP 配置模板）：

```
{  "mcpServers": {    "postgres": {      "command": "npx",      "args": ["-y", "@modelcontextprotocol/server-postgres",               "postgresql://localhost:5432/rbac_dev"]    },    "context7": {      "command": "npx",      "args": ["-y", "@upstash/context7-mcp"]    }  }}
```

注意：每个 MCP 工具描述都会占用上下文预算。建议只启用当前任务真正需要的 MCP 与工具，具体上限取决于模型上下文、工具描述长度和任务复杂度 [2]。

**```
.claude/settings.json
```**：

```
{  "permissions": {    "allow": [      "Bash(./mvnw test:*)",      "Bash(./mvnw spotless:*)",      "Bash(./mvnw verify)",      "Bash(pnpm test:*)",      "Bash(pnpm lint:*)",      "Bash(pnpm typecheck)",      "Edit(backend/src/**/*.java)",      "Edit(frontend/src/**/*.{ts,vue})",      "Edit(**/*.test.ts)"    ],    "ask": [      "Bash(./mvnw flyway:*)",      "Bash(git commit:*)",      "Bash(git push:*)",      "Bash(pnpm install:*)",      "Edit(backend/pom.xml)",      "Edit(frontend/package.json)",      "Edit(backend/src/main/resources/db/migration/**)",      "Edit(.env*)"    ],    "deny": [      "Bash(rm -rf:*)",      "Bash(psql:*)",      "Bash(redis-cli FLUSHALL:*)",      "Bash(redis-cli FLUSHDB:*)",      "Edit(.git/**)",      "Read(.env)"    ]  }}
```

**Hooks**：Claude Code 可以通过 PostToolUse 自动触发 

```
./mvnw spotless:apply
```

 或 

```
pnpm lint --fix
```

；Cursor 可按支持的自动化能力挂同类逻辑；Codex 侧则优先依靠 

```
AGENTS.md
```

 指令、审批策略和 sandbox 兜底 [2]。

**安全警示**：代理配置、Rules、Skills、Hooks、MCP 都可能成为提示注入、越权命令或供应链攻击的入口；

```
.cursorrules
```

 等文本规则中也可能夹带不可见 Unicode 指令。**拉取任何第三方 skills/agents/MCP 之前必须人工审阅**，有条件时再配合静态扫描或安全审查工具检查配置文件 [2][4]。

**```
.claudeignore
```** 最小模板（与 

```
.claude/settings.json
```

 的 

```
Read(.env)
```

 拦截规则共同生效——前者在模型读取层过滤，后者在权限门禁层拦截，构成双保险）：

```
node_modules/target/dist/.next/coverage/*.log.env**.png*.jpg*.mp4
```

---
