> 📎 来源: [kali笔记](https://mp.weixin.qq.com/s?__biz=MzkxMzIwNTY1OA==&mid=2247518750&idx=1&sn=b3dc0c7e2b6094d153563f24434c419a&chksm=c0c481e63f7b4228eafcab0b3cb65438df486ae2096d92b39a9325c232a3964135f3bb108f4a&mpshare=1&scene=1&srcid=051144IDiYVdrz6Tsv8Rtg1c&sharer_shareinfo=b79373a8477318a7b510505d40fb7307&sharer_shareinfo_first=b79373a8477318a7b510505d40fb7307) | 时间: 2026-05-11 08:05

---

> 网络安全威胁层出不穷的今天，你是不是也有这些困惑：个人和企业到底该怎么筑牢自己的网络安全防线？怎么快速找到网络环境里的安全漏洞、及时补上？国家强制要求的网络安全等级保护，有没有更简单高效的落地方法？爆火的 AI 智能体，真的能帮我们给网络安全保驾护航吗？今天这篇文章，就给你一套可直接上手的完整答案。

长期以来，等保测评一直是企业网络安全工作中最令人头疼的环节之一。等保过程充满神秘感，大多数企业只能作为旁观者，面对复杂的测评流程和专业要求束手无策；同时网络安全本身又有着极高的技术门槛，让很多非专业人士难以建立清晰的认知。面对这样的困境，现在我们可以借助AI智能体，通过Skill完美解决！

# ![](assets/img_570eb9a792c0.gif) 部署 ![](assets/img_15d60a89e466.gif)

目前最新版，我们只需到官网https://www.openocta.com根据自己的系统类型下载安装即可。 无需多余的环境配置！下载安装包后，在Kali中可以执行下面命令进行安装。

```
dpkg -i openocta_linux_amd64.deb
```

![](assets/img_27825cc472b4.png)

部署完成后，访问

```
ip:18900
```

便可进入控制台。

![](assets/img_6328136d5a28.png)


点击模型选项，根据自己的需求添加模型。完成后我们便可以直接调用Kali Linux中的工具进行等保测评。

![](assets/img_c4bb6b4b8491.png)

# ![](assets/img_4fbf03b0d7c0.gif) 等保技能 ![](assets/img_62a2e55cefc2.gif)

利用Skill，Openocta可以借助Kail Linux中的工具直接进行等保测评。无需复杂的配置便可上手。

  

 

主要流程01020304信息收集进行域名信息收集、端口扫描、资产收集漏洞扫描常见漏洞扫描和审计漏洞复现验证是否存在漏洞、POC复现报告生成及修复为用户生成扫描报告，及修复建议。

 

  

Skill能做什么？

  

 

 这个Skill能做什么?

| 能力 | 介绍 |
| --- | --- |
| 全自动化 | 只需告诉目标信息，全程自动化无需人工干预。 |
| 直接调用工具 | 技能会自动解锁Kali中的安全工具，缺少工具相应工具时，会自动安装。 |
| 等级报告 | 完成后，会依据等保2.0要求生成全面的报告及修复建议。 |
| 完全开源 | 技能完全开源，可根据自身情况适当修改。 |

技能获取：在下方仓库中，下载技能到本地。点击技能库，将下载的技能导入即可。接下来让其学习并掌握此技能。

> 开源项目地址：https://github.com/openocta/openocta\_skills

 

![](assets/img_0bb29feaecf5.jpg)

扫描小助手进入交流群，获得更多SKILL; 如您有好的SKILL，也欢迎提交PR

 

![](assets/img_e577f0bdaaa2.png)

# ![](assets/img_b24ba82c6b55.gif) 等保测评 ![](assets/img_aff9fd890b3e.gif)

接下来，我们以信息收集-漏洞扫描-漏洞复现-报告评分及修复四个主流模块开展技能实战。相关提示语如下！

> 现在，我需要你对我公司的网络资产进行等保测评，完成后给我相关报告。以下是相关信息：公司官网网址：bbskali.cn  公司内网网段：192.168.50.1/24 当前，我将你部署在Kali Linux中。里面的工具可以直接调用！请为我完成等保测评

![](assets/img_316b0cf51017.png)

接下来，是整个等保测试流程。
**😎第一阶段：信息收集**

![](assets/img_8bd2e6116373.png)

![](assets/img_aea8b9d71b62.png)

![](assets/img_dd3b78d5c79c.png)

![](assets/img_6736c7fbd448.png)

![](assets/img_f89a171b60f6.png)

**🧲第二阶段深度渗透测试**

![](assets/img_1a31d8679146.png)

![](assets/img_f0b0b506e67f.png)

![](assets/img_9dd5f03752f8.png)

![](assets/img_eb37b9c37b3f.png)

![](assets/img_8ce69ce29abd.png)

**❤️第三阶段漏洞利用验证/提权测试**

![](assets/img_8a437bd2e925.png)

![](assets/img_9f16ced51b14.png)

![](assets/img_1e57148ca66c.png)

![](assets/img_39c13877d8b4.png)

![](assets/img_45af6ae26bf8.png)

![](assets/img_29b1dd2e0fb7.png)

**📧第四阶段：完整等保测评报告 + 合规差距分析 + 整改路线图**

![](assets/img_33798401c00f.png)

![](assets/img_6d932dbe3a6a.png)

![](assets/img_de605d619aae.png)

![](assets/img_1d47e64e17c4.png)

![](assets/img_d4c4e3c27a6d.png)

![](assets/img_b89280073a2c.png)

![](assets/img_0e71ba1f9383.png)

![](assets/img_1ce1d40d60f9.png)

![](assets/img_2f65d759ffb4.png)

# ![](assets/img_21b65f94dd21.gif) 总结 ![](assets/img_2ddf9e1e15e8.gif)

通过OpenOcta国产开源智能体，能够为个人和企业提供快速、高效地等保测评方案，实现网络环境的安全防护和合规性要求。极大地简化了安全管理流程，提高了工作效率。亮明了自身网络安全存在的不足，方便用户更新相关漏洞，从而提高自身网络安全。
