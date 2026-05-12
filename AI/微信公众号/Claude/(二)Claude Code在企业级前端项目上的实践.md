> 📎 来源: [Super话AI](https://mp.weixin.qq.com/s?__biz=MzA3MjY0NjQ1Mg==&mid=2648026254&idx=1&sn=9477b9dbfaff52072947961966982191&chksm=8626ec42b992311447781cd3c0eb4883e41729026000080c960f600cdc60bb137a098f12724e&mpshare=1&scene=1&srcid=0429S9SS83cV04qBSzloJrw5&sharer_shareinfo=c7b16e44f736357272b340c0e826249b&sharer_shareinfo_first=c7b16e44f736357272b340c0e826249b) | 时间: 2026-04-29 03:38

---

# Part2-【需求开发】OpenSpec实践SDD范式编程&【Git Hooks】配置pre-commit/commit-msg hooks&【安全】审查

    上一篇[(一)ClaudeCode在企业级前端项目上的实践](https://mp.weixin.qq.com/s?__biz=MzA3MjY0NjQ1Mg==&mid=2648026223&idx=1&sn=167f191b35b85a6e77f64759a64f8966&scene=21#wechat_redirect)，主要介绍了Claude Code在前端项目的初始化操作，以及实现【代码审查、规范检查、架构设计、新功能开发、项目源码分析】的能力。

    第二篇文章主要回答3个问题：1、我们应该怎么开发一个需求？2、需求开发完了，要提交代码到git时如何触发检查机制？3、最后，提交的代码如何保证没有泄露敏感信息？

    我本地使用的是Claude Code（以下简称cc）+deepseek-v4-pro进行演示。

---

#

# 【需求开发】OpenSpec实践SDD范式编程

## 一、安装OpenSpec&完善config.yaml

    可以参考我之前写的文章[团队老项目落地OpenSpec实践指南](https://mp.weixin.qq.com/s?__biz=MzA3MjY0NjQ1Mg==&mid=2648026198&idx=1&sn=775ee9d9205962bd7f651ccdf3bcb2e0&scene=21#wechat_redirect)。唯一不同在于：这篇文章里面的工具用的是Trae，换成cc后就不需要手动在.trae/rules下创建project\_rules.md作为该项目的规则，写入指令映射。OpenSpec会自动在项目.claude/commands目录下创建opsx命令。

![](assets/img_0f3beaefaf5c.png)

后续使用命令就变成：/opsx:propose

![](assets/img_8ccf5c180ed2.png)

其余功能都没变。

## 二、开始验证

下面以一个简单需求进行场景验证：

/opsx:propose兑换记录列表页面 标题改成：兑换记录页

changes目录下会创建exchange-record-rename-title目录：

![](assets/img_0b43e2c15d34.png)

检查无误后，接着执行：

/opsx:apply

修改代码，并将task.md中的所有任务状态改成已完成。

![](assets/img_bfe36578ab3c.png)

![](assets/img_3c1e10b5c514.png)

确认代码修改无误后，执行：

/opsx:verify

然后再执行：

/opsx:syncexchange-record-rename-title 同步规格（这里specs目录下没有改动，只有一个README文件，所以其实是sync后也没有什么变化）

/opsx:archive 归档需求

![](assets/img_0ed6b34761ed.png)

    需求开发完成，需要把代码提交到git，就需要触发相关检查机制。第一反应是想到GitHooks。

---

# 【Git Hooks】配置pre-commit/commit-msg hooks

## 一、CLAUDE.md中的【GitHooks配置】

![](assets/img_3869a5d8071f.png)

说明：【安装 Git Hooks】的bash命令（下面会讲到）和【已配置的Hooks】。

![](assets/img_f30d7d135659.png)

明确指出可用的技能和命令。

## 二、定义一键安装脚本install.sh

![](assets/img_22f8781d16dc.png)

做3件事：

1、检查是否安装依赖：Git、Node.js、npm、OpenSpec。

2、安装GitHooks：执行bash .claude/hooks/install-git-hooks.sh命令

![](assets/img_4dcbc7e2c197.png)

会更新.git/hooks下面的pre-commit和commit-msg钩子。

![](assets/img_0770ec4dccb0.png)

3、检查mcp（可选）。

## 三、更新关键词检测脚本 - keyword-trigger.js

![](assets/img_580e26873013.png)

匹配关键词，执行相应的技能。

## 四、skills目录：新增code-commit技能

![](assets/img_15567f709ef2.png)

## 五、install-git-hooks.sh

做2件事：

1、先找到.git目录。

2、将.claude/hooks/pre-commit.sh复制到./git/hooks/pre-commit；将.claude/hooks/git-commit-msg.sh复制到./git/hooks/commit-msg

![](assets/img_6de9a51b777a.png)

## 六、.claude/hooks/pre-commit.sh

执行npmrunlint进行检查和npmrunlint----fix进行修复。

## 七、.claude/hooks/git-commit-msg.sh

验证Commit Message 格式，标准格式：():

![](assets/img_d7dc2083fa9e.png)

## 八、开始验证

## 场景1 - 自然语言或命令的方式提交代码

第一次输入“帮我总结变更并提交代码”，或者输入命令“/code-commit”

![](assets/img_a6ef177be1a9.png)

第一次输出：

![](assets/img_5f6485840fd4.png)

![](assets/img_83077365d2f2.png)

第二次输入“TAPD ID: 123”。

第二次输出：先执行git add <文件1> <文件2>...

![](assets/img_9178bf4a88ed.png)

第二次输出：然后执行git commit，触发.git/hooks目录下的pre-commit执行代码lint检查，触发 .git/hooks目录下的commit-msg钩子验证 Commit Message 格式。

![](assets/img_f67cc735feba.png)

代码commit完成，可以push了。

![](assets/img_bf37fe4d6ffb.png)

## 场景2 - 原生执行git commit命令

修改src/App.vue，增加报错代码：

![](assets/img_999e8020c716.png)

输入bash命令：git commit -m "123"，触发.git/hooks目录下的pre-commit执行代码lint检查，有报错，不允许提交。

![](assets/img_080a23acdeb8.png)

修改src/App.vue，去掉报错代码。

先输入bash命令：git add .，将变更代码添加到暂存区。

然后输入bash命令：git commit -m "123"，触发.git/hooks目录下的pre-commit执行代码lint检查，检查无误；接着触发 .git/hooks目录下的commit-msg钩子验证 Commit Message 格式，有误。

![](assets/img_a41da407b0e4.png)

修改bash命令：git commit -m "chore(123): 新增git hooks相关功能"，可以正常提交了。

![](assets/img_163948f8f0eb.png)

    提交git这里还需要触发CI/CD流程，这个放到下一篇文章再展开说。这里先定义/security-review命令，保证在提交代码时没有泄露敏感信息。

---

# 【安全】使用/security-review命令执行代码安全审查扫描

![](assets/img_c008090ee05d.png)

主要做3件事：

1、敏感信息检查

2、安全漏洞检查

3、最佳实践检查

最后生成审查报告。

使用比较简单，直接输入/security-review命令即可。

下一篇CI/CD会讲安全审查要怎么用。

---

# 最后的话

    这篇主要介绍了开发、提交代码过程中如何使用cc做得更好。后面的文章我会继续完善企业级项目的其他流程。

---

谢谢你看到这里~

如果对你有帮助，别忘了点赞+推荐，也欢迎关注我，我会持续分享更多AI工具实用技巧。
