---
tags: [GitHub, API, Python]
source: "BUG与灵光"
created: 2026-04-21
updated: 2026-05-10
category: GitHub
---

# 获取最新文章 ID 列表url = 'https://hacker-news.firebaseio.com/v0/topstories.json'r = requests.get(url)storyids = r.json()    # 返回 [35580378, 35579582, ...]# 按 ID 逐条获取详情storyurl = f'https://hacker-news.firebaseio.com/v0/item/{storyids[0]}.json'r = requests.get(storyurl)story = r.json()print(story['title'])print(story.get('url', 'No URL'))

> 来源: [BUG与灵光](https://mp.weixin.qq.com/s?__biz=MzYzNTIzOTc4OQ==&mid=2247483877&idx=1&sn=aa0b251846fe7c235d5663b59de5c43b&chksm=f1c9b603de84f8937df08c233ab47438f72df76309725d2dd7db1591306eeef94d2607ee5347&mpshare=1&scene=1&srcid=0421fNNYCyW3Moa7xvb0equA&sharer_shareinfo=37f96d5b502e74a86e0513a1058a5810&sharer_shareinfo_first=37f96d5b502e74a86e0513a1058a5810) | 2026-04-21

## 摘要

上一章是"下载现成数据"，这一章升级了——**程序自己上网请求数据**。
API（Application Programming Interface）说白了就是网站提供给程序用的"数据窗口"。你不看网页，只拿数据。GitHub 的仓库信息、Hacker News 的文章列表，都可以通过 API 一行代码拿到。
核心工具就一个库：**requests**。
安装完就能用了，调 API 比想象中简单：
`requests.get(url)` 就像用浏览器访问这个地址，但返回的不是 HTML 页面，而是纯数据（通常是 JSON）。`r.json()` 自动把 JSON 解析成 Python 字典，方便直接操作。
| 状态码 | 含义 |
| --- | --- |
| 200 | 请求成功，数据到手 |
| 403 | 被拒绝（通常是请求太频繁） |
| 404 | 资源不存在（URL 写错了） |
GitHub API 对未认证请求有限制：每小时最多 60 次。可以查看剩余次数：
如果频率不够用，就加认证（Personal Access Token），能提到 5000 次/小时。
API ...

## 相关实体

[[GitHub]], [[Python]]

## 相关概念

[[数据可视化]]
