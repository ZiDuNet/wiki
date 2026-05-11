> 📎 来源: [极空间私有云](https://mp.weixin.qq.com/s?__biz=MjM5OTM5NTEzNw==&mid=2247571020&idx=1&sn=2aed4a0997799546a84f746f026ea2cf&chksm=a677f59305cf19fe28626db449b84f9e99b534f1c5950aa8629b12831b0547e069d1fda57826&mpshare=1&scene=1&srcid=04085NyXKmf4HOKTWLbhy6wo&sharer_shareinfo=b15486b11c0478d869f8456426d0cf4b&sharer_shareinfo_first=b15486b11c0478d869f8456426d0cf4b) | 时间: 2026-04-13 16:15

---

各位极友，我是小极君～

你有没有想过，让AI帮你把一部小说自动变成短剧？

从剧本拆解、角色生成、分镜规划，到视频合成、配音对口型——全自动，一条龙。

今天@可爱的小cherry 带来的这个开源项目叫 **Waoo**，一个全流程AI影视制作平台。你只需要导入一段文字，它就能帮你生成一部完整的短剧。虽然目前还在0.3 beta版本，细节有待打磨，但“影视制作工厂”的雏形已经出来了。

当然，生图生视频是要成本的。一集短剧几十个镜头，大概100元左右。但换个角度想，这可能是你离“AI影视创作者”最近的一次。

部署在极空间上，7×24小时待命。教程和代码都备好了，感兴趣的可以自己试试。👇👇👇

**/****/ 风险****提示**

**///**

1. 极空间仅提供支持创建Docker镜像的环境，软件功能与注意事项详见该软件内具体使用规则。
2. 本文仅代表作者观点，使用第三方解决方案，均非官方正式方案，可能会产生相关风险，请自行斟酌。

有的小伙伴留言说，我还没有玩 OpenClaw。

有没有 NAS 里可以部署的，支持接入不同 API、大模型，灵活性更高的「AI 影视制作一条龙」工具。

别说还真有。一款是漫改一条龙项目（我们以后介绍），另外一款是今天的主角：全自动短剧制作系统 —— Waoo。

从小说到剧本，从剧本到分镜，人物、背景图片一键生成，自动旁白、对口型，全自动运镜以及一键成片。

![](assets/img_34ed5b3a2e6b.png)

****Waoo**** 是一款在 Github 开源的全流程 AI 影视制作平台。官方称致力于打造业界首创的专业可控影视制作 AI Agent 平台 —— “从短片到真人电影，采用好莱坞标准工作流程。”

- 🎬 ****AI 剧本分析**** — 自动解析小说，提取角色、场景、剧情
- 🎨 ****角色 & 场景生成**** — AI 生成一致性人物和场景图片
- 📽️ ****分镜视频制作**** — 自动生成分镜头并合成视频
- 🎙️ ****AI 配音**** — 多角色语音合成
- 🌐 ****多语言支持**** — 中文 / 英文界面，右上角一键切换

![](https://mmbiz.qpic.cn/sz_mmbiz_png/FA7Xn1J8zEvSMYAOXkYBl9bw3fmTQd6PYXkzfLavph9dTpTicnLyzFZUFxpWempiagBHJUNNjcnWwlct0a3SwLDyP9LIY4eGaVEiaoib2Bp4lpk/640?wx_fmt=png)

这是我一键生成的一个短剧视频。使用了全部免费的 api 接口，并且没有修改脚本。质量的话仁者见仁智者见智，想要好的效果，更强大的收费模型和更好的脚本才是核心关键。**工作流的作用，是将不同厂家的 api 进行聚合，解决了一家独占的问题，也将整个流程打通。**

---

# **一、全自动影视梦工厂**

## **1. API 详解**

这一切，要从**“雅各布井”**说起....

跑偏了。项目的一切，要从理解视觉大模型说起。

大家都知道，做视频，不可能像普通的 AI 对话一样白嫖，毕竟生图、生视频的算力是比较夸张的。

常规来说，****一张图的成本约在 0.2元****，而一个 1080p 的 5s 视频消耗约为 110 tokens，****一个视频需要 2-3 块钱不等****。

所以做短视频肯定是硬砸钱的，想要白嫖也只能临时。

目前国内在生图、生视频里集成最多的就是****火山、阿里百炼、海螺****三大平台，也是我最推荐的，waoo 都支持。

如果你同时需要使用 **openclaw** 的，最建议购买的就是 **minimax （海螺）**，**包括音乐、视频、图片的免费用量**。

另外国内平台还接入了 vidu 平台。国外平台支持 gemini、openrouter、fal。

![](assets/img_b382d9afb920.png)

开启自动短视频制作前，我们需要在设置中心里添加 9 个类型的 API 接口。分别是 LLMs、生视频、生图（角色、场景、镜头、图片edit）、语音（音色、tts、口型）。

****想要效果好，最推荐的还是 gemini 的 banana 来生图。效果最真实，质量最高。****

![](assets/img_77f7f965099a.png)

## **2. 开始创作**

首先我们需要对一个小说文本进行拆解。目前系统支持两种模式。

第一种是全自动的智能文本分集，支持 3万字以内的小说拆解。

另外一种是单集拆解，每一集都导入一节文章。

![](assets/img_a6282b8e9824.png)

文章我自己利用 kimi agent 写了一部单篇科幻小说，8000 多个字，这里挑出了第一节来做短剧，直接把文本复制进去，然后选择制作的目标。

![](assets/img_c7661fda57ab.png)

画面支持 10 种屏幕比例，短剧无脑选择 9：16。

![](assets/img_023f4c2ecfc3.png)

风格支持真人、国漫、漫画、日漫。gemini 推荐真人，其它 agent 推荐国漫、日漫风格。

![](assets/img_4c4399cabb2c.png)

第一步，剧本拆解。会从角色、场景、片段三个角度进行文字处理，并经过数次的剧本转换、合并，形成短剧拍摄脚本的专业提示词。

![](assets/img_90735bc81741.png)

第二步，资产生成。等待剧本拆解完成以后，系统会把单集中出现的人物、场景，自动生成提示词。

有了提示词，我们就可以一键调用 api 生图。如果不满意，可以手动修改提示词，或者进行 api 炼丹。

![](assets/img_0946c0997a60.png)

每一个人物、场景都会生成 3 个选项，选择我们看起来最舒服的确认为实际素材。声音、音色也是一样。

![](assets/img_1e4090fee8a0.png)

人物的话，包括一张脸部细节，正、侧、背三视图。

![](assets/img_a867ca4acdae.png)

实际剧本上来看。第一节分成了三个片段，每个片段又有多个场景，角色对话、旁白、场景描述都有。

![](assets/img_70a2e76663bf.png)

第三步就是分镜规划了，这一步同样也是全自动的。结合剧情需要，会设置每一个小视频的首图、提示词、灯光、镜头语言等等。

![](assets/img_12439c502113.png)

只是一节，就包含了 38 个镜头。我个人的感觉是分的太细了，有些场景其实有重复。

![](assets/img_71d606f5be2e.png)

比如旁白，会单独占用一个画面去介绍，而不是结合语言一起。另外视频也不是首尾帧生成的，转场的一致性上稍微差一点。

不过毕竟这个项目还是 0.3 beta 版本，很多细节的打磨还在进行中，目前这个样子已经相当自动化了。

![](assets/img_d457eebb227a.png)

每一个场景分镜，我们都可以配置单独的生视频模型，也支持一键批量生成。38 个视频，一集的制作成本在 100 元左右。

![](assets/img_93111138ee7a.png)

由于项目的一键剪片还在开发中，所以制作出来的视频，我们需要手动下载到本地进行二次剪辑。

![](assets/img_653171d9712e.png)

# **二、极空间部署 waoo**

waoo 项目本身还是有一定的复杂度的，使用了 

```
mysql/minio/redis
```

 三种数据库。

但是实际部署的话，我们只需要使用一个 

```
yaml
```

 文件就可以搞定了。

顺便提一下极空间 docker 应用内测里的升级内容，docker compose 功能几乎重做，路径问题得到了完美解决，现在支持在配置路径后使用相对路径来部署容器，复杂的手机号和虚拟路径不再需要了。

![](assets/img_6cd9aca79d9c.png)

下面的 

```
yaml
```

 代码完全不需要变动，直接复制进去就可以部署。

```
services:  # ==================== MySQL ====================  mysql:    image: mysql:8.0    container_name: waoowaoo-mysql    restart: unless-stopped    environment:      MYSQL_ROOT_PASSWORD: waoowaoo123      MYSQL_DATABASE: waoowaoo      MYSQL_ROOT_HOST: "%"    volumes:      - mysql_data:/var/lib/mysql    command:      - "--default-authentication-plugin=mysql_native_password"      - "--sql_mode=STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION"    healthcheck:      test: ["CMD-SHELL", "mysqladmin ping -h 127.0.0.1 -uroot -pwaoowaoo123"]      interval: 5s      timeout: 5s      retries: 30      start_period: 15s  # ==================== Redis ====================  redis:    image: redis:7-alpine    container_name: waoowaoo-redis    restart: unless-stopped    volumes:      - redis_data:/data    command: ["redis-server", "--appendonly", "yes"]    healthcheck:      test: ["CMD", "redis-cli", "ping"]      interval: 5s      timeout: 5s      retries: 30      start_period: 5s  # ==================== MinIO ====================  minio:    image: minio/minio:RELEASE.2025-02-28T09-55-16Z    container_name: waoowaoo-minio    restart: unless-stopped    environment:      MINIO_ROOT_USER: minioadmin      MINIO_ROOT_PASSWORD: minioadmin    command: server /data --console-address ":9001"    volumes:      - minio_data:/data    healthcheck:      test: ["CMD", "curl", "-f", "http://127.0.0.1:9000/minio/health/live"]      interval: 5s      timeout: 5s      retries: 30      start_period: 10s  # ==================== App (Next.js + Workers) ====================  app:    image: ghcr.io/saturndec/waoowaoo:latest    container_name: waoowaoo-app    restart: unless-stopped    environment:      # 数据库（指向容器内部 MySQL，用服务名 mysql 而非 localhost）      DATABASE_URL: "mysql://root:waoowaoo123@mysql:3306/waoowaoo"      # Redis（指向容器内部 Redis，用服务名 redis）      REDIS_HOST: redis      REDIS_PORT: "6379"      REDIS_USERNAME: ""      REDIS_PASSWORD: ""      REDIS_TLS: ""      # 存储：默认 MinIO（S3 兼容）      STORAGE_TYPE: minio      MINIO_ENDPOINT: "http://minio:9000"      MINIO_REGION: "us-east-1"      MINIO_BUCKET: "waoowaoo"      MINIO_ACCESS_KEY: "minioadmin"      MINIO_SECRET_KEY: "minioadmin"      MINIO_FORCE_PATH_STYLE: "true"      # 认证      NEXTAUTH_URL: "http://localhost:3000"      NEXTAUTH_SECRET: "waoowaoo-default-secret-2026"      # 内部密钥      CRON_SECRET: "waoowaoo-docker-cron-secret"      INTERNAL_TASK_TOKEN: "waoowaoo-docker-task-token"      API_ENCRYPTION_KEY: "waoowaoo-opensource-fixed-key-2026"      # Worker 配置      WATCHDOG_INTERVAL_MS: "30000"      TASK_HEARTBEAT_TIMEOUT_MS: "90000"      QUEUE_CONCURRENCY_IMAGE: "50"      QUEUE_CONCURRENCY_VIDEO: "50"      QUEUE_CONCURRENCY_VOICE: "20"      QUEUE_CONCURRENCY_TEXT: "50"      # Bull Board      BULL_BOARD_HOST: "0.0.0.0"      BULL_BOARD_PORT: "3010"      BULL_BOARD_BASE_PATH: "/admin/queues"      BULL_BOARD_USER: ""      BULL_BOARD_PASSWORD: ""      # 日志      LOG_UNIFIED_ENABLED: "true"      LOG_LEVEL: "INFO"      LOG_FORMAT: "json"      LOG_DEBUG_ENABLED: "false"      LOG_AUDIT_ENABLED: "true"      LOG_SERVICE: "waoowaoo"      LOG_REDACT_KEYS: "password,token,apiKey,apikey,authorization,cookie,secret,access_token,refresh_token"      # 计费      BILLING_MODE: "OFF"      # 流式      LLM_STREAM_EPHEMERAL_ENABLED: "true"    ports:      - "33330:3000"      - "33329:3010"    volumes:      - ./data:/app/data      - ./docker-logs:/app/logs    depends_on:      mysql:        condition: service_healthy      redis:        condition: service_healthy      minio:        condition: service_healthy    command: >      sh -c "        npx prisma db push --skip-generate && npm run start      "volumes:  mysql_data:  redis_data:  minio_data:
```

---

# **总结**

从小说到剧本，从剧本到分镜，从图片到视频，waoo 的一条龙影视工厂满足了用户的使用需求，让 AI 短剧制作流程门槛大幅度降低。

人人都可以通过 NAS 部署后，打造成自己的 7\*24小时不间断影片工厂。搭配自动发布短视频的功能，嘿嘿，画面多美我不敢想。

不过考虑到视频制作成本还是比较高的，每个脚本一般就做前 2、3 集来做钩子即可，有流量的再考虑继续投入。

最后是性能方面，这个项目跑了 3 个数据库，内存大概吃了 1G 左右。我使用极空间 Z4Pro N95 处理器部署的，从常态化使用上来说完全 hold 的住，现在旗舰款的极空间Z4Pro+/Z4Pro+ 性能版那就更没有问题了~

![](assets/img_ff7a35de5569.webp)

![](assets/img_784f7a0a8071.gif)

![](assets/img_121c8e073628.gif)
