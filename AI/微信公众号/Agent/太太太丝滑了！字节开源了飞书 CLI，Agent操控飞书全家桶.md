> 📎 来源: [海涛AI智能体](https://mp.weixin.qq.com/s?__biz=Mzk0MDc1OTU5Mw==&mid=2247491040&idx=1&sn=e50ac8c049fbe44deab5aa0d47dfb358&chksm=c39c0a94ba66814bee63ffe6103641581817dee4575276789dcf84d9b8969a94ef9c1b057806&mpshare=1&scene=1&srcid=0415aofvrqbXdyE7OvqdOlyo&sharer_shareinfo=2a432c4284116cb317d799797adb80ae&sharer_shareinfo_first=2a432c4284116cb317d799797adb80ae) | 时间: 2026-04-15 22:22

---

💡

字节跳动开源了 lark-cli（飞书命令行工具），配合 AI Agent（如 OpenClaw / Claude Code），可以用自然语言直接操作飞书消息、云文档、多维表格、日历等全套能力，真正实现自然语言驱动的智能办公。

![](assets/img_8cef0f8dd0e5.png)

lark-cli 的价值

- 降低门槛：无需写代码，自然语言即可操作飞书
- 效率提升：批量操作、自动化流程大幅节省时间
- 生态打通：AI Agent + 飞书 = 智能办公新范式
- 开源可控：MIT 协议，可自由定制和扩展

✅

开始体验：npm install -g @anthropic-ai/lark-cli 即可安装，配合 Claude Code 或 OpenClaw 等 AI Agent 使用效果更佳。

直达地址：https://github.com/larksuite/cli

先看下具体功能，再实操测试

![](assets/img_4b1ebf81df1b.png)

## 一、快速上手：应用配置

```
# 安装 CLInpm install -g @larksuite/cli# 安装 CLI SKILL（必需）npx skills add larksuite/cli -y -g
```

安装 lark-cli 后，运行 lark-cli config init --new，按提示在浏览器中完成应用配置和授权：

![](assets/img_4be8a4c64dda.png)

扫描二维码完成创建飞书应用，同时自动完成授权配置

![](assets/img_893e1faa167b.png)

![](assets/img_f80d446796db.png)

应用配置完成后可以在控制台看到消息提醒，接下来就可以在Claude code或OpenClaw中使用了~

![](assets/img_d7196c666a73.png)

## 二、实战案例

如下案例在Claude code中进行测试，其它模型还没有实测效果

### 案例 1：AI 热点整理 + 消息推送

让其帮我整理近期的AI热点信息，发送飞书消息给我

![](assets/img_d11dc8f8dd74.png)

### 案例 2：一键撰写文章并保存到飞书文档

围绕第一条撰写公众号文章，保存到飞书云文档

![](assets/img_0208f34be71e.png)

![](assets/img_f4cabc1da8e8.png)

### 案例 3：多维表格 —— 美股科技股监控

这是一个更复杂的场景：让 AI 创建飞书多维表格，实现美股科技股票的自动监控。

第一步：让Claude Code收集美股科技股票数据，并创建多维表格

![](assets/img_29a001ebcba7.png)

第二步：多维表格内容规划

![](assets/img_eca6929340ee.png)

第三步：自动写入数据

![](assets/img_e1d4de7a1921.png)

可以看到，自动创建多维表格并写入数据，字段类型也非常正确，在之前是非常难控制到这么细的粒度。

![](assets/img_df4a07165721.png)

第四步：配置表格视图

支持创建多维表格视图

![](assets/img_8c41056fd43b.png)

以板块、投资评级维度分别创建了两个视图

![](assets/img_32aea9819db6.png)

第五步：创建数据仪表盘

多维表格还有个强大功能，数据仪表盘，我们看下支持情况

![](assets/img_cb7775ee46ce.png)

完全自动化创建多维表格仪表盘

![](assets/img_31dda1e3ff50.png)

### 案例4：飞书CLI同时支持了 白板Skills，我测试了下面几个开发经常用到的架构图、时序图，体会下直出的乐趣。

例如这种架构图，可以搭配Claude Code直接绘制并保存到云文档，（不是图片、不是图片）支持二次编辑修改。

![](assets/img_d6f4a947b9e4.png)

#### 绘制思维导图

![](assets/img_e6f1a07b19b2.png)

#### 时间线

![](assets/img_e37c3ecec582.png)

#### 消息时序图

![](assets/img_2fe864876a5e.png)

#### 泳道图

![](assets/img_fd495c55eafd.png)

以上就是飞书CLI的初步实操案例，受篇幅限制，部分截图不太清晰，如果有伙伴对于其中演示案例感兴趣，可以留言，我把飞书文档和多维表格分享出来。

最后，分享下最近的观察

软件的演化路径，正在极速转变。

过去十几年，我们从命令行走向图形界面，目的是让普通人也能用上电脑。

而现在，界面正在从图形走回命令行，因为出现了一类新用户：AI Agent。

Agent 不需要按钮，不需要页面，它需要的是可编程的接口。

命令行CLI，恰好就是最轻、最直接的那种。

飞书在这方面动作很快，值得点赞。
