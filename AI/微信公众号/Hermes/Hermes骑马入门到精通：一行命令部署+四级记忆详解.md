> 📎 来源: [大飞象的智能体2025](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247486617&idx=1&sn=b440575217fb45ffc220071a65b40c49&chksm=c3d898187dcb2fe039246a3be1624f4b64d4a7f68ed7e3ea5976a9beb53e9c2b035b9ed49260&mpshare=1&scene=1&srcid=0425xErKcrO2y7BWFE2zz4Ar&sharer_shareinfo=57b8e0ba704670e71a23f91201c9e822&sharer_shareinfo_first=57b8e0ba704670e71a23f91201c9e822) | 时间: 2026-04-25 18:03

---

# Hermes骑马入门到精通：一行命令部署+四级记忆详解



Hermes Agent很火，但很多人不知道怎么用。



这篇文章就从入门到精通，详细讲解Hermes的部署和使用。



重点讲四级记忆架构，这是Hermes的核心。

---



## 一、一行命令部署



### 1. 系统要求



| 系统 | 支持情况 |

|---|---|

| Linux | ✅ 完全支持（推荐） |

| macOS | ✅ 完全支持 |

| Windows | ❌ 需安装WSL2 |



### 2. 硬件要求



| 配置 | 说明 |

|---|---|

| 最低配置 | 1核1GB内存 |

| 推荐配置 | 4GB+内存，2核CPU |



### 3. 一行命令



curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash



安装完成后：



source ~/.bashrc && hermes



就这么简单。



---



## 二、四级记忆架构详解



这是Hermes的核心，也是它区别于其他AI Agent的关键。



### L1 核心记忆



\*\*作用\*\*：存储你的基本信息和偏好



\*\*内容\*\*：

• 你叫什么名字

• 你喜欢什么风格

• 你用什么语言



\*\*示例\*\*：

用户姓名：象哥

偏好语言：中文

工作风格：简洁高效



### L2 用户画像



\*\*作用\*\*：记录你的工作习惯和常用工具



\*\*内容\*\*：

• 你用什么编程语言

• 你用什么编辑器

• 你常用什么工具



\*\*示例\*\*：

编程语言：Python

编辑器：VS Code

版本控制：Git

常用工具：Docker、Kubernetes



### L3 历史搜索



\*\*作用\*\*：保存你的搜索记录和结果



\*\*内容\*\*：

• 你搜过什么

• 结果是什么

• 什么时候搜的



\*\*示例\*\*：

搜索：Hermes Agent部署教程

时间：2026-04-24

结果：找到5篇相关文章



### L4 技能记忆



\*\*作用\*\*：存储自动生成的技能和经验



\*\*内容\*\*：

• 技能名称

• 执行步骤

• 使用次数



\*\*示例\*\*：

技能：日报生成

步骤：

1. 读取Git提交记录

2. 分析任务完成情况

3. 生成日报格式

使用次数：15次



---



## 三、四级记忆怎么工作？



### 第一次使用



你让Hermes帮你整理桌面文件。



你说：把PDF放到文档文件夹，图片放到图片文件夹。



它照做了，同时记住了你的偏好（L1）。



### 第二次使用



你又说：整理桌面文件。



它直接按上次的方式整理，不用你再描述（L2）。



### 第三次使用



你只需要说：整理。



它就知道要整理桌面文件，按你喜欢的方式（L3）。



### 之后



它生成了一个"文件整理"技能（L4）。



以后遇到类似任务，直接调用这个技能。



---



## 四、配置大模型



### 支持的模型



| 类型 | 模型 |

|---|---|

| OpenAI | GPT-4、GPT-3.5 |

| Anthropic | Claude系列 |

| 国产 | DeepSeek、通义千问、豆包 |



### 配置方法



首次启动会提示配置：



请输入API Key: sk-xxx

请选择模型: deepseek-v4-pro



---



## 五、基本使用



### 命令行交互



hermes

> 你好，帮我整理桌面文件

> 帮我生成今天的日报

> 帮我搜索Hermes教程



### 多平台接入



配置企业微信：

1. 在设置中添加企业微信配置

2. 扫码绑定

3. 在微信中发消息控制



---



## 六、自进化能力



### 工作原理



完成任务 → 自动总结步骤 → 生成技能 → 下次直接调用



### 示例



你让它帮你分析一个开源项目。



第一次：需要详细描述怎么分析。



第二次：它已经生成了"项目分析"技能，直接调用。



第三次：你只需要说"分析这个项目"，它就知道怎么做。



---



## 七、进阶技巧



### 1. 查看记忆



hermes memory show



### 2. 查看技能



hermes skills list



### 3. 定时任务



hermes cron add "0 9 \* \* \*" "生成日报"



---



## 八、常见问题



### Q1：记忆会丢失吗？



不会。记忆存储在本地数据库，重启不丢失。



### Q2：如何清空记忆？



hermes memory clear



### Q3：如何备份记忆？



记忆文件在 `~/.hermes/memories/` 目录，直接复制即可。



---



## 九、总结



Hermes Agent的核心是四级记忆架构：



| 层级 | 作用 |

|---|---|

| L1 | 记住你是谁 |

| L2 | 记住你怎么工作 |

| L3 | 记住你搜过什么 |

| L4 | 记住你学会了什么 |



部署很简单：

1. 一行命令安装

2. 配置API Key

3. 开始使用



GitHub地址：https://github.com/NousResearch/hermes-agent



有问题欢迎留言交流。

![](assets/img_32c5d90b1849.jpg)

![](assets/img_fa8f8ce0f960.jpg)

更多精彩：

[终于等到你！DeepSeek V4开源，性能碾压GPT-4，免费商用无限制](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247486579&idx=1&sn=2d26d8f1a6a0260242c5e99a5508c12b&scene=21#wechat_redirect)

[谁懂啊，Hermes 42天4万星，龙虾瞬间不香了](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247486584&idx=1&sn=725520a342f82f644383f5446845b327&scene=21#wechat_redirect)

[DeepSeek V4来了！1M上下文+Apache 2.0开源，AI圈又要变天了](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247486580&idx=1&sn=d1b876b041b7817401bd4272ddca6de8&scene=21#wechat_redirect)

[DeepSeek V4今日开源！万亿参数+百万上下文，国产大模型彻底杀疯了](https://mp.weixin.qq.com/s?__biz=MzkzNzY4NzA3MA==&mid=2247486574&idx=1&sn=ad5dd4a958d057e8ad2006c2aedbed88&scene=21#wechat_redirect)
