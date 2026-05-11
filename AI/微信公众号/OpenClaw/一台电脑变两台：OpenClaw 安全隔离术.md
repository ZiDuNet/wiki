> 📎 来源: [技术小丑](https://mp.weixin.qq.com/s?__biz=MjM5OTU0NTc5Mw==&mid=2257498869&idx=1&sn=30ea6f07418f176c3ce2c1ad35affd13&chksm=a5c054edb5a31b96a9113165fc8fe2bdcfe81be89ff42a4cde04475c42bd52de5732f6ba9291&mpshare=1&scene=1&srcid=0418rQbPFwCIyWMLYFcg9ORm&sharer_shareinfo=88bf2c8df7567efa2d4f972df66ae6ac&sharer_shareinfo_first=88bf2c8df7567efa2d4f972df66ae6ac) | 时间: 2026-04-18 18:50

---

**macOS 多账号 + VNC 隧道，让 AI 智能体在沙箱中运行**

---

OpenClaw（俗称"小龙虾"）火了。

用自然语言控制电脑，自动点击、录屏、跑脚本，简直是开发者和办公人士的神器。但它有个致命问题：**权限太大**。

一旦授权，OpenClaw 拿到的是整台电脑的"万能钥匙"——它能读写你的桌面、文档、SSH 密钥，甚至能执行 

```
rm -rf /
```

 这种毁灭性命令。AI 幻觉、恶意插件、端口暴露……任何一点问题，都可能让你的主账户彻底失控。

**解决方案很简单**：用 macOS 的多用户隔离机制，给 OpenClaw 一个"沙箱账户"。

主账户继续正常工作，OpenClaw 在另一个账户里折腾。即使它发疯，也删不掉你的主账户文件；即使它被黑，黑客进来的只是一个普通用户，无法控制系统。

---

## 核心原理：POSIX 权限模型 + VNC 隔离

macOS 基于 Unix，文件系统采用 POSIX 权限模型。每个用户都有自己的 

```
/Users/{username}/
```

 目录，权限隔离由内核强制执行。

```
普通用户 claw：- 只能访问 /Users/claw/- 无法读取 /Users/becrafter/- 无法修改系统目录 /System、/Library- 无法执行 sudo 命令
```

即使 OpenClaw 试图执行高危操作，也会被内核拒绝：

```
$ sudo rm -rf /Password:  # 普通用户没有 sudo 权限claw is not in the sudoers file.  This incident will be reported.
```

配合 VNC 远程桌面协议，我们可以实现"一台电脑，两个桌面"：

•

主账户：日常使用

•

claw 账户：OpenClaw 独占

两者互不干扰，完全隔离。

---

## 步骤一：创建 claw 专用账户

这是整个方案的基石。打开「系统设置」→「用户与群组」，添加一个新账户：

•

账户名称：claw

•

账户类型：普通（关键！）

•

密码：设置强密码

**为什么必须是普通账户？**

管理员账户可以修改系统配置、访问其他用户数据。如果 claw 是管理员，隔离就形同虚设。普通账户的权限被严格限制在 

```
/Users/claw/
```

 目录内。

---

## 步骤二：开启菜单栏快速切换

为了方便在两个账户间切换，打开「系统设置」→「控制中心」，勾选「快速用户切换」→「在菜单栏显示」。

顶部菜单栏会出现账户图标，点击即可切换账户。

---

## 步骤三：首次登录 claw 账户

点击菜单栏账户图标，选择 claw，输入密码登录。

登录后，系统会要求你配置 Apple ID、Safari、iCloud 等。你可以：

•

登录同一个 Apple ID（方便同步配置）

•

或者创建新的 Apple ID（更彻底的隔离）

**保持登录状态，不要注销。**

---

## 步骤四：切回 becrafter，开启共享功能

切换回主账户（假设是 becrafter），打开「系统设置」→「通用」→「共享」。

依次开启：

•

屏幕共享

•

文件共享

•

内容缓存

这些服务会在后台运行，为 VNC 连接提供基础。

---

## 步骤五：SSH 隧道加密 VNC 连接

这是安全的关键。直接暴露 VNC 端口到公网是极其危险的——黑客可以扫描到 5900 端口，暴力破解密码，直接控制你的电脑。

**正确做法**：VNC 只监听 localhost，通过 SSH 隧道加密传输。

在主账户的终端中执行：

```
ssh -f -N -L 5901:localhost:5900 claw@localhost
```

**命令解析**：

•

```
-f
```

：SSH 在后台运行

•

```
-N
```

：不执行远程命令，仅用于端口转发

•

```
-L 5901:localhost:5900
```

：将本地 5901 端口转发到远程的 5900 端口

•

```
claw@localhost
```

：登录到 claw 账户

输入 claw 账户的密码后，SSH 隧道建立完成。**终端窗口必须保持打开**。

---

## 步骤六：VNC 连接进入 claw 桌面

打开 Finder，按 

```
Command + K
```

，输入：

```
vnc://localhost:5901
```

点击「连接」，选择「Log in as Yourself」，输入 claw 的用户名和密码。

进入的桌面是 claw 账户的独立环境，与主账户完全隔离。

---

## 步骤七：在 claw 账户中安装 OpenClaw

在 VNC 桌面中，打开 Safari 访问 OpenClaw 官网，下载 macOS 版本的安装包，正常安装即可。

安装完成后，配置 OpenClaw 权限：

•

辅助功能权限（用于屏幕控制）

•

屏幕录制权限（用于录屏）

•

完全磁盘访问权限（**仅在 claw 账户范围内**）

这些权限只会影响 claw 账户，主账户不受影响。

---

## 步骤八：配置防火墙规则

为了进一步加固安全，配置防火墙规则，阻止外部访问 VNC 和 OpenClaw 端口：

```
# 启用防火墙sudo pfctl -e# 阻止 VNC 端口的外部访问echo "block in from any to any port 5900" | sudo pfctl -f -# 阻止 OpenClaw 端口的外部访问echo "block in from any to any port 18789" | sudo pfctl -f -# 验证规则sudo pfctl -sr
```

即使 OpenClaw 被配置为监听所有网络接口，防火墙也会阻止外部访问。

---

## 验证隔离效果

配置完成后，验证隔离是否生效：

**1. 文件隔离测试**

在 claw 账户的终端中尝试访问主账户文件：

```
$ ls /Users/becrafter/ls: /Users/becrafter/: Permission denied
```

**2. 系统权限测试**

尝试执行需要管理员权限的命令：

```
$ sudo rm -rf /SystemPassword:claw is not in the sudoers file.  This incident will be reported.
```

**3. 桌面操作隔离测试**

在 claw 桌面创建一个文件夹，删除它；切换到主账户，确认主账户的桌面文件完好无损。

---

## 扩展：多实例并行部署

如果需要同时运行多个 OpenClaw 实例（比如处理不同任务），可以创建多个专用账户：

```
# 创建 claw1、claw2、claw3 等账户sudo sysbecrafterctl -addUser claw1 -password "Password1!"sudo sysbecrafterctl -addUser claw2 -password "Password2!"sudo sysbecrafterctl -addUser claw3 -password "Password3!"# 为每个账户配置独立的 SSH 隧道ssh -f -N -L 5901:localhost:5900 claw1@localhostssh -f -N -L 5902:localhost:5900 claw2@localhostssh -f -N -L 5903:localhost:5900 claw3@localhost
```

通过 VNC 连接不同端口（5901、5902、5903），即可控制不同的账户，实现真正的并行处理。

---

## 高级技巧：SSH 隧道自动重连

SSH 隧道可能会因为网络不稳定、系统休眠等原因断开。为了避免频繁手动重连，可以创建一个自动重连脚本：

```
#!/bin/bash# ~/scripts/auto_ssh_tunnel.shwhile true; do    if ! pgrep -f "ssh.*5901" > /dev/null; then        echo "$(date '+%Y-%m-%d %H:%M:%S') - SSH tunnel not found, recreating..."        ssh -f -N -L 5901:localhost:5900 claw@localhost    fi    sleep 5done
```

设置执行权限：

```
chmod +x ~/scripts/auto_ssh_tunnel.sh
```

后台运行：

```
nohup ~/scripts/auto_ssh_tunnel.sh > ~/scripts/tunnel.log 2>&1 &
```

脚本会每 5 秒检查一次 SSH 隧道状态，断开后自动重建。

---

## 总结

通过 macOS 多用户隔离机制和 VNC 远程桌面协议，我们实现了"一台电脑变两台"的安全隔离方案：

**核心价值**：

•

**权限隔离**：OpenClaw 被锁死在普通账户内，无法越权访问主账户

•

**桌面隔离**：主账户和 OpenClaw 账户并行运行，互不干扰

•

**连接安全**：SSH 隧道加密传输，防火墙阻止外部访问

•

**风险可控**：即使 OpenClaw 失控，主账户和系统安全不受影响

**适用场景**：

•

开发者：在隔离环境中安全使用 AI 自动化工具

•

企业团队：为团队成员提供隔离的工作空间

•

极客玩家：探索多实例并行部署

这套方案利用 macOS 原生功能，无需额外安装第三方工具，配置简单，维护方便。更重要的是，它不仅适用于 OpenClaw，也适用于任何需要桌面自动化和系统控制的 AI 工具。

**安全第一，但不必牺牲效率。** 在隔离环境中享受 AI 的强大能力，才是正确的打开方式。
