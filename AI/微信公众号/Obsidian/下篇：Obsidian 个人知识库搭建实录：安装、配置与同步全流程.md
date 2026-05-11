> 📎 来源: [徒手开榴莲](https://mp.weixin.qq.com/s?__biz=MzIxNzU0NjU0NA==&mid=2247485501&idx=1&sn=9deeac318ae91282a33d1b6cc3f8822c&chksm=96c21ae497103e03d7b43698b4105a88b2d158f9b9e9a10858f650c0df992428096f1fb43099&mpshare=1&scene=1&srcid=05102yrW7WTsi6dw1nLF0hAP&sharer_shareinfo=9f93d6d7312219dddeea06bdcf8c3b28&sharer_shareinfo_first=9f93d6d7312219dddeea06bdcf8c3b28) | 时间: 2026-05-10 15:14

---

上一篇讲了[为什么选用Obsidian搭建个人知识库](https://mp.weixin.qq.com/s?__biz=MzIxNzU0NjU0NA==&mid=2247485476&idx=1&sn=c03cafff71350b32045fb57fb1ca7aa2&scene=21#wechat_redirect)，这一篇直接讲怎么搭。

---

## 一、整体思路

这套方案不是单纯装一个 Obsidian。

而是把几个工具组合起来，搭成一条完整流程。

```
Obsidian：负责本地写作和知识管理GitHub：负责云端备份Claudian + Claude Code + MiniMax M2.7：负责 AI 辅助整理和生成Working Copy：负责手机端查看、编辑和同步
```

整体流程是：

```
本地写作  ↓云端备份  ↓AI 辅助整理和生成  ↓手机查看、编辑和同步
```

先把基础流程跑通。

再慢慢接入 AI。

不要一上来就追求全自动。

![](assets/img_d3e6086f0bc4.jpg)

---

## 二、工具清单

这套方案主要用到下面这些工具。

| 工具 | 作用 | 地址 |
| --- | --- | --- |
| Obsidian | 本地知识库主体，用来写笔记、放素材、管理内容 | https://obsidian.md/download |
| GitHub | 云端仓库，用来备份和同步知识库 | https://github.com/ |
| Git | 本地版本管理工具，用来把 Vault 推送到 GitHub | https://git-scm.com/downloads |
| Obsidian Git | Obsidian 插件，用来在电脑端自动同步 GitHub | Obsidian 插件市场搜索：Git |
| Claudian | Obsidian 插件，用来在 Obsidian 中接入 Claude Code 类能力 | https://github.com/YishenTu/claudian (如果插件市场搜不到, 通过此地址下载) |
| Working Copy | iPhone / iPad 上的 Git 客户端，用来同步手机端文件 | https://workingcopy.app/ |
| MiniMax M2.7 | AI 模型，用来辅助整理素材、生成草稿、优化文章 | 使用 MiniMax 控制台获取 API Key |
| Obsidian Web Clipper | Chrome 插件，用来把网页内容剪藏到 Obsidian | Chrome 应用商店搜索(如果可以)：Obsidian Web Clipper |

对应关系可以这样理解：

| 环节 | 对应工具 |
| --- | --- |
| 写作和管理 | Obsidian |
| 网页剪藏 | Clipping for web |
| 云端备份 | GitHub |
| 电脑端同步 | Git + Obsidian Git |
| AI 辅助 | Obsidian + Claudian + Claude Code + MiniMax M2.7 |
| 手机端同步 | Working Copy |

这里要注意顺序。

先搭 Obsidian。

再接 GitHub 同步。

然后接 AI 辅助。

最后处理手机端同步。

---

## 三、Obsidian 本地搭建

这一部分做三件事：

```
1、安装 Obsidian2、创建 Vault3、建立基础目录
```

---

### 1、下载安装 Obsidian

1、打开官网：https://obsidian.md/download

2、选择对应系统版本。

3、下载并安装。

4、打开 Obsidian。

![](assets/img_4944d26148a7.png)

---

### 2、创建 Vault

Vault 可以理解成一个本地知识库文件夹。

1、打开 Obsidian。

2、点击 **Create new vault**。

3、填写 Vault 名称。

4、选择本地保存位置。

5、点击 **Create**。

创建完成后，本地知识库就搭好了。

后续笔记、素材、草稿，都会以 Markdown 文件的形式保存在这个文件夹里。

![](assets/img_d766acf831ed.png)

### 3、建立基础目录

刚开始目录不要复杂。

先建 5 个文件夹就够用。

```
01_收集箱02_笔记03_资料04_项目99_归档
```

目录用途如下：

| 目录 | 用途 |
| --- | --- |
| 01\_收集箱 | 临时想法、灵感、网页摘录、待整理内容 |
| 02\_笔记 | 长期笔记、知识卡片、方法总结 |
| 03\_资料 | PDF、图片、截图、参考资料 |
| 04\_项目 | 某个具体主题或任务相关内容 |
| 99\_归档 | 暂时不用，但不想删除的内容 |

创建方式：

1、在 Obsidian 左侧文件区点击新建文件夹。

2、依次创建上面 5 个目录。

3、临时内容先放进 

```
01_收集箱
```

。

4、整理后的内容再移动到对应目录。

日常使用流程：

```
临时记录 → 01_收集箱整理笔记 → 02_笔记外部资料 → 03_资料具体事项 → 04_项目过期内容 → 99_归档
```

刚开始不要追求完美分类。

先保证每个内容都有地方放。

![](assets/img_0e43ac451e18.png)

### 4、安装Obsidian插件

1、打开 Obsidian 设置。

2、进入 **Community plugins**。

3、关闭 **Restricted mode**。

4、点击 **Browse**。

5、搜索并安装插件。

抛砖引玉,其他社区插件安装方式同理, 可自行探索

| 插件 | 作用 |
| --- | --- |
| Obsidian Git | 电脑端自动同步 GitHub |

![](assets/img_e4af23da092c.png)

## 四、多端同步配置

多端同步主要分三步：

```
1、GitHub 创建私有仓库2、本地 Vault 推送到 GitHub3、电脑端和手机端分别接入同步
```

---

### 1、GitHub 创建私有仓库

1、打开 GitHub：https://github.com/

2、登录账号。

3、点击右上角 **New repository**。

4、填写仓库名。

5、仓库类型选择 **Private**。

6、不要勾选初始化 README。

7、点击 **Create repository**。

8、复制仓库地址。

仓库地址格式一般是：

```
https://github.com/你的用户名/仓库名.git
```

个人知识库里可能有草稿、资料、私人记录。

建议使用**私有仓库**。这样别人看不到你写了什么

![](assets/img_d4303087a2a6.png)

---

### 2、本地 Vault 推送到 GitHub

先确认电脑已经安装 Git。

Git 下载地址：

```
https://git-scm.com/downloads
```

安装完成后，打开终端。

1、进入 Vault 所在目录。

```
cd 你的Vault路径
```

2、初始化 Git。

```
git init
```

3、添加文件。

```
git add .
```

4、提交文件。

```
git commit -m "init vault"
```

5、设置主分支。

```
git branch -M main
```

6、关联 GitHub 仓库。

```
git remote add origin https://github.com/你的用户名/仓库名.git
```

7、推送到 GitHub。

```
git push -u origin main
```

8、刷新 GitHub 仓库页面。

如果页面上能看到 Vault 里的文件，说明推送成功。

---

### 3、电脑端配置 Obsidian Git

这一步的作用是让电脑端自动同步。

1、打开 Obsidian。

2、进入 **Settings**。

3、进入 **Community plugins**。

4、搜索并安装 **Git**。

5、启用插件。

6、进入 Obsidian Git 插件设置。

基础配置可以先这样设置：

![](assets/img_9cc76a8ba4ea.png)

```
Auto pull interval：1 // 间隔很短, 为了方便测试Auto commit-and-sync interval：1 // 间隔很短, 为了方便测试Pull updates on startup：开启Push on backup：开启
```

配置完成后，测试一次。

1、在 Obsidian 新建一个测试文件。

2、随便一个地方写入一行内容。

3、等到了你设置的同步时间, 打开 GitHub 仓库页面。

如果能看到测试文件，说明电脑端同步成功。(然后再根据需要自己改下push 和 pull 的自动同步时间, 我目前是15分钟)

![](assets/img_0b9457f233fb.png)

---

### 4、手机端配置 Working Copy

手机端建议使用 Working Copy。

不要在手机端安装 Obsidian Git 插件。

配置步骤：

1、打开 App Store。

2、搜索并安装 **Working Copy**。

3、打开 Working Copy。

4、登录 GitHub。

5、授权 Working Copy 访问仓库。

6、点击 **Clone repository**。

7、选择刚才创建的 Obsidian 仓库。

8、等待同步完成。

![](assets/img_3b85d396cf44.jpg)

---

### 5、手机 Obsidian 打开仓库

1、打开手机端 Obsidian。

2、选择 **Open folder as vault**。(这步的意思是把手机里的文件作为仓库来同步, 不同手机版本可能不一样)

3、找到 Working Copy 同步下来的仓库文件夹。

4、选择该文件夹。

5、确认打开。

到这里，手机端就能查看同一个知识库了。

手机端适合做这些事：

```
查看笔记临时记录补充灵感轻量修改
```

重度写作、批量整理、AI 处理，建议放在电脑端完成。

![](assets/img_3b3cc5dfdc01.jpg)

---

## 五、接入 AI 辅助

前面几步完成后，知识库已经可以正常使用。

接下来再接入 AI。

这里的目标不是让 AI 接管全部流程。

而是让它帮我们处理重复工作。

比如：

```
整理素材生成摘要提炼知识卡片生成文章草稿优化文章结构调整表达节奏
```

这一部分主要用到：

```
Claudian + Claude Code + MiniMax M2.7
```

---

### 1、先理解它们的关系

可以这样理解：

| 工具 | 作用 |
| --- | --- |
| Obsidian | 存放内容和管理知识库 |
| Claudian | 在 Obsidian 中接入 Claude Code 类能力 |
| Claude Code | 读取文件、修改文件、执行任务 |
| MiniMax M2.7 | 提供模型能力 |
| Obsidian Vault | AI 要处理的本地知识库 |

整体关系是：

```
Obsidian 负责存内容Claudian 负责接入 Claude CodeClaude Code 负责执行文件任务MiniMax M2.7 负责提供模型能力
```

最终希望实现的效果是：

```
把素材放进 01_收集箱        ↓让 AI 整理成笔记        ↓输出到 02_笔记        ↓再根据笔记生成草稿        ↓保存到 04_项目
```

---

### 2、安装 Claudian

Claudian 是 Obsidian 插件。

但它不是从 Obsidian 插件市场直接安装的。

下载地址是：

```
https://github.com/YishenTu/claudian
```

需要注意的是第三步,下载完要记得去 Obsidian的设置里开启一下

![](assets/img_7eb94989384f.png)

### 3、配置 MiniMax M2.7

只需要在Claudian的配置下命令的调用路径:

![](assets/img_41f8959570cf.png)

我自己是使用了 Claude Code CLI 已经接好了 MiniMax M2.7.

![](assets/img_039662357f1b.png)

所以在上面只配个path就可以, Claudian的作用就是让用户在Obsidian中使用大模型, 底层走的还是自己接入的大模型,可以是kimi、deepSeek或者其他模型

### 4、让 AI 处理 Obsidian 内容

接入成功后，先测试最小任务。

比如：

```
读取 01_收集箱 中的指定文件，整理成一篇结构清晰的 Markdown 笔记，保存到 02_笔记。
```

这个测试主要验证三件事：

```
能不能读取文件能不能理解要求能不能写回指定目录
```

这一步跑通后，再继续升级。

比如让它根据笔记生成草稿：

```
读取 02_笔记 中的指定文件，生成一篇适合公众号阅读的文章草稿，保存到 04_项目。
```

先小任务。

再复杂任务。

---

### 5、建议放一个规则文件

为了减少每次重复说明，可以在 Vault 根目录放一个规则文件。

比如：

```
CLAUDE.md
```

里面写清楚基础要求。

示例：

```
# 基础要求- 使用中文输出- 内容适合普通读者- 表达清楚，少废话- 输出 Markdown 文件- 不要随意修改原始资料- 需要新建内容时，写入指定目录# 目录规则- 01_收集箱：原始素材、临时灵感- 02_笔记：整理后的长期笔记- 03_资料：外部资料- 04_项目：具体主题或项目内容- 99_归档：暂时不用的旧内容
```

后续还可以继续增加工作流。

比如：

```
# 工作流：整理素材当我说“整理这个素材”时：1. 读取指定文件2. 提取核心信息3. 整理成结构化笔记4. 保存到 02_笔记# 工作流：生成草稿当我说“根据这篇笔记生成草稿”时：1. 读取指定笔记2. 生成文章初稿3. 保持结构清晰4. 保存到 04_项目
```

这样 AI 就不只是聊天工具。

它开始变成知识库里的执行助手。

---

## 六、实用tips

### 1、Claudian 是 Obsidian 插件，但插件市场搜不到

Claudian 是 Obsidian 插件。

但它不是从 Obsidian 插件市场直接安装的。

下载地址是：

```
https://github.com/YishenTu/claudian
```

安装完记得在设置里开启

![](assets/img_5f65d12d842e.png)

### 2、手机端出现空文件夹，需要手动处理

在 iPhone 上通过 Working Copy 获取内容时，
Git 只跟踪文件，不跟踪目录。

也就是说，
如果你在电脑上做了文件移动，
并提交到了 GitHub，
手机端同步后，
旧的空文件夹可能还会留着。

这种情况下，
就需要手动删除一下。

---

### 3、手机端不要装 Git 插件

手机端要通过Working Copy 手动提交输入内容.

也就是说同步过程是这样的:

PC端: Obsidian 通过git插件,自动提交到 github
手机端: Obsidian 通过 Working Copy 手动提交到 github

---

### 4、不要在电脑和手机同时修改同一个文件

这套方案不是实时协作文档。

不要同时在电脑和手机上修改同一个文件。

更稳的方式是：

```
电脑写完 → 先同步 → 手机再打开手机改完 → 先同步 → 电脑再继续
```

这样可以减少冲突。

### 5、解决 chrome 插件无法下载

推荐一个宝藏网站: https://crxdl.com/

![](assets/img_0685eae178e7.png)

### 6、关于 Working Copy

作为一个同步软件, 从github同步到手机是免费的
但手机端如果要同步本地Obsidian笔记到github, 是付费功能

我半个多月使用下来发现并没有强需求
手机端记得内容少, 打开电脑copy一下也不费事

目前只有自己的大模型是付费的, 其余全部免费

## 结尾

这套方案搭下来，核心其实就是四步：

```
1、用 Obsidian 管理本地知识库2、用 GitHub 做云端备份3、用 Claudian + MiniMax M2.7 接入 AI 辅助4、用 Working Copy 打通手机端同步
```

如果真的搭建起来了, 你会发现：

你不是多装了一个软件。

而是给自己的长期积累，搭了一个可以持续生长的底座。

![](assets/img_e88b04d82bf0.png)

感谢阅读 

如果内容有帮助 , 点赞、收藏+关注 🙏

如有不足, 欢迎评论区留言指正

![](assets/img_6f685dd33fdd.png)
