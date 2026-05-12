# Browserbase Skills 项目文档

---

## 📋 中文摘要

### 项目概述
**Browserbase Skills** 是一套为 **Claude Code** 设计的技能插件，使其能够通过浏览器自动化和官方 `bb` CLI 工具与 Browserbase 平台协同工作。

### 主要技能（Skills）列表

| 技能名称 | 功能描述 |
|---------|---------|
| **browser** | 通过 CLI 命令自动化网页浏览器交互，支持远程 Browserbase 会话，具备反机器人检测、CAPTCHA 解决和住宅代理功能 |
| **browserbase-cli** | 使用官方 `bb` CLI 进行 Browserbase Functions 和平台 API 操作，包括会话、项目、上下文、扩展、fetch 和仪表板管理 |
| **functions** | 使用 `bb` CLI 将无服务器浏览器自动化部署到 Browserbase 云端 |
| **site-debugger** | 诊断和修复失败的浏览器自动化，分析机器人检测、选择器、时序、认证和验证码问题，生成测试过的站点剧本 |
| **browser-trace** | 捕获完整的 DevTools 协议追踪（CDP 数据流、截图、DOM 转储），并将流数据分割成每页可搜索的桶 |
| **safe-browser** | 构建本地 Claude Agent SDK 浏览器代理，仅通过 CDP 门控的 `safe_browser` 工具提供浏览器能力，并强制执行域名白名单 |
| **bb-usage** | 在终端仪表板中显示 Browserbase 使用统计、会话分析和成本预测 |
| **cookie-sync** | 将本地 Chrome 的 Cookie 同步到 Browserbase 持久上下文，使 browse CLI 能访问已认证的站点 |
| **fetch** | 无需浏览器会话即可从静态页面获取 HTML 或 JSON，检查状态码、头部、跟踪重定向 |
| **search** | 无需浏览器会话即可搜索网页并返回结构化结果（标题、URL、元数据） |
| **ui-test** | AI 驱动的对抗性 UI 测试，分析 git diff 来测试变更，或探索整个应用来发现 bug |

### 安装方法

```bash
$ npx skills add browserbase/skills
```

### Claude Code 安装步骤

```bash
# 添加市场
$ /plugin marketplace add browserbase/skills

# 安装插件
$ /plugin install browse@browserbase
```

或手动安装：
1. 输入 `/plugin`
2. 选择 `3. Add marketplace`
3. 输入 `browserbase/skills`
4. 选择 `browse` 插件
5. 按 Enter 安装
6. **重启 Claude Code**

### 使用示例

安装后可以向 Claude 发出如下指令：
- *"去 Hacker News，获取热门帖子评论并总结"*
- *"测试 http://localhost:3000 并修复遇到的任何 bug"*
- *"帮我订个披萨，你已经在 Doordash 上登录了"*
- *"使用 `bb` 列出我的 Browserbase 项目并以 JSON 格式显示"*
- *"用 `bb functions init` 初始化一个新的 Browserbase Function 并解释后续命令"*
- *"使用 safe-browser 构建一个只停留在主站的 Hacker News 爬虫"*

### 故障排除

**Chrome 未找到问题：**
- macOS/Windows: 从 https://www.google.com/chrome/ 安装
- Linux: `sudo apt install google-chrome-stable`

**刷新配置文件 Cookie：**
```bash
rm -rf .chrome-profile
```

### 相关资源
- [Stagehand 文档](https://github.com/browserbase/stagehand)
- [Claude Code Skills 文档](https://support.claude.com/en/articles/12512176-what-are-skills)

---

## 📄 英文原文

# Browserbase Skills

A set of skills for enabling **[Claude Code](https://docs.claude.com/en/docs/claude-code/overview)** to work with Browserbase through browser automation and the official `bb` CLI.

## Skills

This plugin includes the following skills (see `skills/` for details):

| Skill | Description |
|-------|-------------|
| [browser](skills/browser/SKILL.md) | Automate web browser interactions via CLI commands — supports remote Browserbase sessions with anti-bot stealth, CAPTCHA solving, and residential proxies |
| [browserbase-cli](skills/browserbase-cli/SKILL.md) | Use the official `bb` CLI for Browserbase Functions and platform API workflows including sessions, projects, contexts, extensions, fetch, and dashboard |
| [functions](skills/functions/SKILL.md) | Deploy serverless browser automation to Browserbase cloud using the `bb` CLI |
| [site-debugger](skills/site-debugger/SKILL.md) | Diagnose and fix failing browser automations — analyzes bot detection, selectors, timing, auth, and captchas, then generates a tested site playbook |
| [browser-trace](skills/browser-trace/SKILL.md) | Capture a full DevTools-protocol trace (CDP firehose, screenshots, DOM dumps) alongside any browser automation, then bisect the stream into per-page searchable buckets |
| [safe-browser](skills/safe-browser/SKILL.md) | Build local Claude Agent SDK browser agents whose only browser capability is a CDP-gated `safe_browser` tool with domain allowlist enforcement |
| [bb-usage](skills/bb-usage/SKILL.md) | Show Browserbase usage stats, session analytics, and cost forecasts in a terminal dashboard |
| [cookie-sync](skills/cookie-sync/SKILL.md) | Sync cookies from local Chrome to a Browserbase persistent context so the browse CLI can access authenticated sites |
| [fetch](skills/fetch/SKILL.md) | Fetch HTML or JSON from static pages without a browser session — inspect status codes, headers, follow redirects |
| [search](skills/search/SKILL.md) | Search the web and return structured results (titles, URLs, metadata) without a browser session |
| [ui-test](skills/ui-test/SKILL.md) | AI-powered adversarial UI testing — analyzes git diffs to test changes, or explores the full app to find bugs |

## Installation

To install the skill to popular coding agents:

```bash
$ npx skills add browserbase/skills
```

### Claude Code

On Claude Code, to add the marketplace, simply run:

```bash
$ /plugin marketplace add browserbase/skills
```

Then install the plugin:

```bash
$ /plugin install browse@browserbase
```

If you prefer the manual interface:
1. On Claude Code, type `/plugin`
2. Select option `3. Add marketplace`
3. Enter the marketplace source: `browserbase/skills`
4. Press enter to select the `browse` plugin
5. Hit enter again to `Install now`
6. **Restart Claude Code** for changes to take effect

## Usage

Once installed, you can ask Claude to browse or use the Browserbase CLI:
- *"Go to Hacker News, get the top post comments, and summarize them "*
- *"QA test http://localhost:3000 and fix any bugs you encounter"*
- *"Order me a pizza, you're already signed in on Doordash"*
- *"Use `bb` to list my Browserbase projects and show the output as JSON"*
- *"Initialize a new Browserbase Function with `bb functions init` and explain the next commands"*
- *"Use safe-browser to build a Hacker News scraper that only stays on the main site"*

Claude will handle the rest.

For local and localhost work, `browse env local` now starts a clean isolated browser by default. Use `browse env local --auto-connect` when the agent should reuse your existing local Chrome session, cookies, or login state.

## Troubleshooting

### Chrome not found

Install Chrome for your platform:
- **macOS** or **Windows**: https://www.google.com/chrome/
- **Linux**: `sudo apt install google-chrome-stable`

### Profile refresh

To refresh cookies from your main Chrome profile:
```bash
rm -rf .chrome-profile
```

## Resources

- [Stagehand Documentation](https://github.com/browserbase/stagehand)
- [Claude Code Skills](https://support.claude.com/en/articles/12512176-what-are-skills)
