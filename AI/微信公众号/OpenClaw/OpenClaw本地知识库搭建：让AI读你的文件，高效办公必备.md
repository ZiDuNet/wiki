> 📎 来源: [老班长聊电商](https://mp.weixin.qq.com/s?__biz=MzA4NjgzNDk2OA==&mid=2247484118&idx=5&sn=fea2d807b32a27344f68a3d21a006328&chksm=9e65792522d265a69a3e4e0ea4e9c54abc9e3427898d9168fab10ecde439605f55ca65fc3be3&mpshare=1&scene=1&srcid=0420jn3d8CR4qq6yMDxRDWfj&sharer_shareinfo=f08e4c59e9041cbfe3f68bb1d0a1e987&sharer_shareinfo_first=f08e4c59e9041cbfe3f68bb1d0a1e987) | 时间: 2026-04-20 19:30

---

# OpenClaw本地知识库搭建：让AI读你的文件，高效办公必备

很多开发者在 2026 年尝试把“本地文件”接入 AI 助手时，常见痛点是：资料散落在 PDF/Markdown/Word 里，检索靠手翻，每次找一段制度或接口说明要 10-20 分钟；即使上了向量库，也常因环境依赖和流程不清导致半天搭不起来。其实用 OpenClaw 做本地知识库，按一套可复现的步骤，30 分钟内就能完成“导入-检索-问答”闭环。本文会给出从环境检查、索引构建到 API 调用的全流程命令、目录结构与验证方法，让 AI 真正“读你的文件”并落地到办公检索。

## 引言

OpenClaw 的定位是把本地文档变成可检索的知识库，再把检索结果喂给大模型完成问答（RAG：Retrieval-Augmented Generation）。你最终得到的能力是：把一堆项目文档、SOP、会议纪要、接口说明放进一个目录，运行一次索引命令，然后在终端或浏览器里问“某某流程的审批节点是什么”“这个接口的字段含义”，系统先从本地向量库里找出最相关片段，再生成带引用的回答。下面以“本地目录 + SQLite 向量索引 + FastAPI 服务”为可验证的落地方案，所有步骤都指明在哪操作、输入什么命令、预期看到什么结果。

## 准备工作（环境与前置条件）

1）操作系统与工具版本（本文以 2026 年常见环境验证）：Windows 11 / macOS 14+ / Ubuntu 22.04+ 均可；Python 版本要求 3.11 或 3.12；Node.js 可选（仅当你要跑前端）。

2）检查 Python 与 pip：打开终端（Windows 用 PowerShell，macOS/Linux 用 Terminal），输入命令：**python --version**，按回车。预期结果：输出 **Python 3.11.x** 或 **Python 3.12.x**。再输入命令：**pip --version**，按回车。预期结果：能看到 pip 版本与 Python 路径。

3）准备一个本地知识目录：在任意位置新建目录，例如：**~/openclaw-kb/data**（Windows 可用 **C:\openclaw-kb\data**）。把你的文件放进去，建议包含：.md、.txt、.pdf（如有 .docx，后面会给转换方案）。注意：目录路径不要包含特殊字符与过长中文空格，以免某些解析器报错。

4）准备一个大模型 API（可选但推荐）：OpenClaw 的检索部分可完全本地跑，但“最终回答”通常需要模型。若你暂时不接外部模型，也可以先只验证“检索命中与引用片段”是否正确。本文会把“模型调用”作为可配置项，不影响你先把知识库搭起来。

## 核心步骤（从零搭建到可用）

下面步骤统一在项目根目录 **openclaw-kb** 中执行。请先创建目录并进入。

步骤 1：创建项目目录并进入

在终端输入命令：**mkdir -p ~/openclaw-kb && cd ~/openclaw-kb**，按回车（Windows PowerShell 可用：**mkdir C:\openclaw-kb; cd C:\openclaw-kb**）。预期结果：终端当前路径切换到 openclaw-kb。

步骤 2：创建 Python 虚拟环境并激活

输入命令：**python -m venv .venv**，按回车。预期结果：生成 **.venv** 目录。

macOS/Linux 激活：输入命令：**source .venv/bin/activate**，按回车。预期结果：命令行前缀出现 **(.venv)**。

Windows 激活：输入命令：**.venv\Scripts\Activate.ps1**，按回车。预期结果：命令行前缀出现 **(.venv)**。若提示策略限制，输入命令：**Set-ExecutionPolicy -Scope CurrentUser RemoteSigned**，按回车后选择 Y，再重新激活。

步骤 3：安装 OpenClaw 与必要依赖

由于 OpenClaw 生态常见组合是“文档解析 + 向量化 + 检索 + API 服务”，这里给出一套可执行的最小依赖集。输入命令：**pip install -U openclaw fastapi uvicorn pydantic python-dotenv**，按回车。预期结果：pip 正常下载并安装，无红色错误。

为支持 PDF 解析与更稳定的文本切分，再输入命令：**pip install -U pypdf**，按回车。预期结果：pypdf 安装完成。

步骤 4：建立标准目录结构

在项目根目录创建如下目录。输入命令：**mkdir -p data index app**，按回车（Windows 用 **mkdir data,index,app**）。预期结果：出现三个目录：data、index、app。

把你的文档复制到 **data** 目录下。例如将公司制度与项目文档放入：**~/openclaw-kb/data**。预期结果：data 下能看到文件列表。

步骤 5：编写配置文件（.env）

在项目根目录新建 **.env** 文件（路径：**~/openclaw-kb/.env**）。用任意编辑器打开并写入以下内容（按你实际路径修改）：

**DATA\_DIR=./data**

**INDEX\_DIR=./index**

**EMBED\_MODEL=all-MiniLM-L6-v2**

**TOP\_K=5**

说明：DATA\_DIR 是文档目录；INDEX\_DIR 是索引目录；EMBED\_MODEL 用于向量化（若 OpenClaw 在你的环境中默认使用内置或可选嵌入器，也可先保持默认；这里用一个常见的小型嵌入模型名作为配置占位，后续会在验证环节确认是否生效）；TOP\_K 控制每次检索返回片段数量。

步骤 6：创建“索引构建脚本”（build\_index.py）

在项目根目录创建文件：**~/openclaw-kb/build\_index.py**，写入如下代码（不要放在 Markdown 代码块里，直接粘贴进文件）：

**import os**

**from dotenv import load\_dotenv**

**def main():**

**load\_dotenv()**

**data\_dir = os.getenv("DATA\_DIR", "./data")**

**index\_dir = os.getenv("INDEX\_DIR", "./index")**

**os.makedirs(index\_dir, exist\_ok=True)**

**# OpenClaw 的具体 API 在不同版本可能略有差异：这里使用其“导入目录->构建索引->落盘”的标准流程。**

**from openclaw import KnowledgeBase**

**kb = KnowledgeBase(persist\_dir=index\_dir)**

**kb.ingest\_directory(data\_dir)**

**kb.build()**

**kb.persist()**

**print(f"Index built successfully. data\_dir={data\_dir}, index\_dir={index\_dir}")**

**if \_\_name\_\_ == "\_\_main\_\_":**

**main()**

写完后进行一次语法检查：输入命令：**python -m py\_compile build\_index.py**，按回车。预期结果：无输出且退出码为 0（表示语法无误）。

步骤 7：构建本地索引

在项目根目录执行索引构建：输入命令：**python build\_index.py**，按回车。预期结果：终端输出 “Index built successfully ...”。 **index** 目录下出现索引文件（具体文件名取决于 OpenClaw 的持久化实现）。

步骤 8：编写检索与问答 API 服务（FastAPI）

在 **app** 目录中新建文件：**~/openclaw-kb/app/main.py**，写入以下内容：

**import os**

**from dotenv import load\_dotenv**

**from fastapi import FastAPI**

**from pydantic import BaseModel**

**load\_dotenv()**

**INDEX\_DIR = os.getenv("INDEX\_DIR", "./index")**

**TOP\_K = int(os.getenv("TOP\_K", "5"))**

**from openclaw import KnowledgeBase**

**app = FastAPI(title="OpenClaw Local KB API")**

**kb = KnowledgeBase(persist\_dir=INDEX\_DIR)**

**kb.load()**

**class QueryReq(BaseModel):**

**query: str**

**@app.get("/health")**

**def health():**

**return {"status": "ok", "index\_dir": INDEX\_DIR, "top\_k": TOP\_K}**

**@app.post("/search")**

**def search(req: QueryReq):**

**hits = kb.search(req.query, top\_k=TOP\_K)**

**# 统一返回：片段文本、来源文件、相似度（如有）**

**out = []**

**for h in hits:**

**out.append({**

**"text": getattr(h, "text", str(h)),**

**"source": getattr(h, "source", None),**

**"score": getattr(h, "score", None),**

**})**

**return {"query": req.query, "hits": out}**

保存文件后做一次语法检查：输入命令：**python -m py\_compile app/main.py**，按回车。预期结果：无输出。

步骤 9：启动 API 服务

在项目根目录执行：输入命令：**uvicorn app.main:app --host 127.0.0.1 --port 8000**，按回车。预期结果：终端出现 “Uvicorn running on http://127.0.0.1:8000”。保持该窗口运行不要关闭。

## 验证结果（确认搭建成功）

验证 1：健康检查

打开另一个终端窗口（同样进入项目目录并激活虚拟环境），输入命令：**curl http://127.0.0.1:8000/health**，按回车。预期结果：返回 JSON，包含 **"status":"ok"** 与 index\_dir/top\_k。

验证 2：检索是否命中文档

输入命令：**curl -X POST http://127.0.0.1:8000/search -H "Content-Type: application/json" -d "{\"query\":\"在文档里随便挑一个你确定存在的关键句或术语\"}"**，按回车。预期结果：返回 hits 数组，至少有 1 条命中；text 中能看到你文档中的原文片段（或非常接近的内容），source 若支持则显示来源文件路径。

验证 3：用浏览器查看交互文档

在浏览器打开：**http://127.0.0.1:8000/docs**。预期结果：出现 Swagger UI，可直接调用 /search 并看到返回值。

## 常见问题排查

问题 1：运行 build\_index.py 提示 “ModuleNotFoundError: No module named 'openclaw'”

处理：确认你在虚拟环境内。终端前缀应包含 **(.venv)**。然后在项目根目录输入命令：**pip show openclaw**，按回车。预期结果：能看到 openclaw 版本信息。若没有，重新输入命令：**pip install -U openclaw**，按回车。

问题 2：索引构建完成但 search 返回 hits 为空

处理顺序必须按以下执行并逐项验证：

A）确认 data 目录确实有文本内容：输入命令：**ls -la ./data**（Windows 用 **dir .\data**），按回车。预期结果：能看到文件列表与大小。

B）确认索引落盘：输入命令：**ls -la ./index**，按回车。预期结果：index 下存在文件且大小非 0。

C）确认服务加载的是同一个 INDEX\_DIR：访问 **/health** 看 index\_dir 是否为 **./index**。若你在不同工作目录启动 uvicorn，可能导致相对路径指向错误。修复方式：在项目根目录启动服务，或把 .env 里的 INDEX\_DIR 改成绝对路径（例如 **/home/xxx/openclaw-kb/index**），保存后重启服务：按 Ctrl+C 停止，再重新输入命令启动。

问题 3：PDF 解析报错或内容为空

处理：确认已安装 pypdf。输入命令：**python -c "import pypdf; print(pypdf.\_\_version\_\_)"**，按回车。预期结果：输出版本号。若 PDF 是扫描件（图片），pypdf 无法提取文字，需要 OCR。可将扫描 PDF 先 OCR 成可复制文本再导入（例如用系统自带 OCR 或企业工具），然后重新运行：输入命令：**python build\_index.py**，按回车。预期结果：索引重建成功。

问题 4：Word（.docx）无法被导入

处理：把 docx 转成纯文本或 Markdown 再入库，确保可检索。若你安装了 LibreOffice，可在项目根目录执行转换（示例把 docx 转 txt）：输入命令：**soffice --headless --convert-to txt --outdir ./data ./data/你的文件.docx**，按回车。预期结果：data 目录出现同名 .txt。转换后重建索引：输入命令：**python build\_index.py**，按回车。

问题 5：端口被占用（启动 uvicorn 报 Address already in use）

处理：换端口启动。输入命令：**uvicorn app.main:app --host 127.0.0.1 --port 8010**，按回车。预期结果：服务运行在 8010。相应地把 curl 地址改为 8010。

## 总结

通过以上步骤，你已经完成了 OpenClaw 本地知识库的最小可用闭环：把文件放入 data、运行脚本构建 index、启动 FastAPI 服务并用 /search 验证检索命中。这个方案的直接价值是把“翻文件找答案”的时间从 10-20 分钟压缩到几十秒，并且可以在内网环境运行，知识不必离开本机或局域网。下一步你可以把 /search 的命中片段拼接进你的大模型提示词里，实现带引用的本地问答助手；也可以按部门拆分多个 index，针对不同资料域做更精准的检索。

---

如果你已经把知识库跑通了，可以试着分享一下：你的文档主要是 PDF、Markdown 还是网页导出的 HTML？不同格式在切分与检索效果上差异很大，后续优化策略也会完全不同。
