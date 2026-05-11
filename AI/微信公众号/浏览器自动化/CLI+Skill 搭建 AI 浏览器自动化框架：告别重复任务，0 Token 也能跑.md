> 📎 来源: [AI炼金社](https://mp.weixin.qq.com/s?__biz=MzIwMzY3Njc2MA==&mid=2247484511&idx=1&sn=53ff47b9795e56f43389e7c2fc9b97eb&chksm=97cf633e8b585f052f7b59d49eb8cd34e3892ba070e00cc5c412f24fd199ecddf2178babc87b&mpshare=1&scene=1&srcid=05101dALJthfpsz1rScS4c6t&sharer_shareinfo=d1021028882983f5f7feabda1fc2102d&sharer_shareinfo_first=d1021028882983f5f7feabda1fc2102d) | 时间: 2026-05-10 15:56

---

每天早上打开浏览器，登录10个网站，点击签到按钮，关掉浏览器。重复一年，300次机械操作，浪费多少时间？

想自动化，但写脚本要学 Puppeteer/Playwright，调试 selector 更是噩梦——网站改个布局，脚本就报废。

有没有更简单的方案？

有。**OpenClaw Browser Automation Skill + agent-browser CLI，不用写代码，自然语言控制浏览器，很多工作流甚至 0 Token 就能跑起来。**

## 一、为什么用 Skill 而不是写脚本

传统浏览器自动化三宗罪：

1. **门槛高**

   ：Puppeteer/Playwright/Selenium 都要写代码，selector、event、promise 一套下来，新手直接放弃
2. **维护累**

   ：网站改 layout，selector 就失效；改了按钮位置，脚本就报错
3. **成本高**

   ：云浏览器 $0.05/分钟，LLM 每次截图/点击都要消耗 Token，8000字 context 直接塞爆

OpenClaw 的 Skill 体系换了个思路：

- **Skill = Markdown 文件**

  ，不是代码
- **agent-browser CLI**

  ：命令行浏览器，不用写 selector
- **语义定位**

  ：用 

  ```
  @ref
  ```

  （e1, e2, e3）操作元素，不是 CSS selector
- **0 Token 模式**

  ：很多自动化流程不需要 AI 参与，CLI 直接跑

结果：门槛降低 90%，维护成本降低 80%，Token 消耗降低到 0。

## 二、核心工作流：OPEN → SNAPSHOT → INTERACT → VERIFY

browser-automation-skill 的核心流程是 6 步循环：

```
1. OPEN    → 打开目标 URL2. SNAPSHOT → 获取页面结构 + 元素 @refs3. INTERACT → 用 @refs 点击/填写/选择4. VERIFY   → 再次 snapshot 确认变化5. REPEAT   → 循环直到任务完成6. CLOSE    → 关闭浏览器 session
```

关键点：**SNAPSHOT 生成 @refs，INTERACT 用 @refs 操作**。

不需要写 CSS selector（

```
#main > div.content > button.submit
```

），只要说"点击 @e5"，Agent 就知道点哪个按钮。

## 三、安装 agent-browser CLI

### 3.1 快速安装

```
npm install -g agent-browseragent-browser install --with-deps
```

验证：

```
agent-browser --version
```

### 3.2 安装 browser-automation-skill

```
clawhub install openclaw-skills-browserautomation-skill
```

或者用 npx：

```
npx clawhub install openclaw-skills-browserautomation-skill
```

## 四、实战：自动签到 0 Token 模式

### 4.1 传统方式（高 Token 消耗）

每次操作都要 AI 参与：

```
User: 打开 example.com 登录页AI: [调用 browser_navigate，消耗 context]User: 点击登录按钮AI: [调用 browser_snapshot + browser_click，消耗 context]...
```

签到 10 个网站，AI 每次都要 snapshot + click，Token 消耗几百。

### 4.2 Skill 方式（0 Token）

把签到流程写成 Skill，CLI 直接跑：

```
agent-browser open https://example.com/loginagent-browser snapshotagent-browser fill @e3 "username"agent-browser fill @e4 "password"agent-browser click @e5  # 登录按钮agent-browser snapshotagent-browser click @e21 # 签到按钮agent-browser close
```

全程不需要 AI 参与，**0 Token**。

更高级：把签到流程固化成 Skill Markdown 文件：

```
---name: auto-signin-exampledescription: 自动签到 example.com---## 步骤1. 打开 https://example.com/login2. 填写用户名到 @e33. 填写密码到 @e44. 点击 @e5 登录5. 点击 @e21 签到6. 关闭浏览器
```

下次直接调用：

```
clawhub run auto-signin-example
```

0 Token，0 代码，0 维护。

## 五、命令速查表

| 命令 | 作用 |
| --- | --- |
| ``` agent-browser open  ``` | 打开页面 |
| ``` agent-browser snapshot ``` | 获取 element @refs |
| ``` agent-browser click @e ``` | 点击元素 |
| ``` agent-browser fill @e  ``` | 填写输入框 |
| ``` agent-browser type  ``` | 输入文本 |
| ``` agent-browser screenshot ``` | 截图 |
| ``` agent-browser state-save ``` | 保存登录状态 |
| ``` agent-browser state-load ``` | 加载登录状态 |
| ``` agent-browser close ``` | 关闭浏览器 |

保存登录状态后，下次签到不用重新登录——这是自动签发的关键。

## 六、ClawHub Skills 生态：2857+ 可复用能力

browser-automation-skill 只是 ClawHub 生态的一个。

当前 ClawHub 有 **2857+ Skills**，覆盖：

- **Browser Automation**

  ：agent-browser、playwright-cli、CDP 集成
- **Coding**

  ：cron-backup、security-check、agentmail-integration
- **Smart Home**

  ：Home Assistant、Home Assistant CLI
- **Health**

  ：Longevity Assistant、Apple Health Skill
- **Finance**

  ：Personal Finance Tracker
- **Search**

  ：Exa、Tavily、Firecrawl 集成

安装方式统一：

```
clawhub install
```

每个 Skill 都是 Markdown 文件，不是代码。**可读、可审计、可复用。**

## 七、小结

- **OpenClaw Browser Automation Skill**

  ：CLI-driven 浏览器自动化
- **agent-browser CLI**

  ：命令行浏览器，语义 refs 操作
- **核心流程**

  ：OPEN → SNAPSHOT → INTERACT → VERIFY → REPEAT → CLOSE
- **0 Token 模式**

  ：Skill 固化流程，CLI 直接跑，AI 不参与
- **ClawHub 生态**

  ：2857+ Skills，统一安装、可复用、可审计

告别重复枯燥任务，不是「理论上可行」，是现在就能跑起来——而且 **0 Token**。

## 相关链接

- browser-automation-skill（LobeHub）：https://lobehub.com/skills/openclaw-skills-browserautomation-skill
- ClawHub Skills Registry：https://clawhub.ai/
- OpenClaw Browser Automation Guide：https://medium.com/gitconnected/openclaw-browser-automation-the-complete-guide-for-2026-58826734fc98
- agent-browser GitHub：https://github.com/vercel-labs/agent-browser
- awesome-openclaw-skills：https://github.com/VoltAgent/awesome-openclaw-skills
