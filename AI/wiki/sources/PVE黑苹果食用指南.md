# PVE黑苹果食用指南

> 来源：[ShouChen's Blog](https://shouchen.blog/post/202509091010/) | 作者：守晨 | 2025-09-09

因某些需求需要云Mac，记录一下折腾过程。

---

## 一、准备工作

### 1. OpenCore引导器

OpenCore 是一个开源的引导加载器，广泛用于黑苹果（在非苹果硬件上运行 macOS）项目。与常用的 Clover 引导器相比，OpenCore 支持更现代的 UEFI 启动方式，具有更高的可定制性和兼容性。

**OpenCore 优势：**
- 更强的硬件兼容性，适配新旧平台
- 更完善的安全性和原生功能支持（如 FileVault、iMessage 等）
- 配置灵活，易于维护和升级
- 社区活跃，文档丰富

**项目地址：** https://github.com/thenickdude/KVM-Opencore

在 Release 页面下载 `.iso.gz` 结尾的镜像文件，解压出 ISO 文件。当前最新支持 **Ventura**。

### 2. OSX镜像

使用 `OSX-KVM` 项目的镜像下载脚本（需 python3）：

**脚本地址：** https://github.com/kholia/OSX-KVM/blob/master/fetch-macOS-v2.py

```bash
python fetch-macOS-v2.py
```

选择 `Ventura`，下载得到 `BaseSystem.dmg`，用 `dmg2img` 转换：

```bash
# 安装 dmg2img（archlinux）
paru -S dmg2img

# 转换
dmg2img -i BaseSystem.dmg BaseSystem.img
```

最后将 **OpenCore** 和 **BaseSystem.img** 上传到 PVE 中。

---

## 二、创建虚拟机

### 阶段1：PVE界面配置

| 配置项 | 设置 |
|--------|------|
| 操作系统 | 类别 `Other`，ISO选 `OpenCore` |
| 系统 | 显卡 `VMware兼容`，机型 `q35`，勾选 `QEMU代理`，BIOS `OVMF(UEFI)`，不勾选 `预注册密钥` |
| 磁盘 | 总线 `VirtIO Block`，最低 32G |
| CPU | 类别 `Haswell`，核心数需为2的幂（2/4/8/16） |
| 网络 | 模型 `VirtIO (半虚拟化)` |

创建后**不要启动**，进入硬件配置，添加 CD/DVD 驱动器，把 `BaseSystem.img` 加进去。

### 阶段2：Shell配置

**避免循环引导：**

```bash
echo "options kvm ignore_msrs=Y" >> /etc/modprobe.d/kvm.conf && update-initramfs -k all -u
```

**编辑配置文件** `/etc/pve/qemu-server/<VMID>.conf`：

**Intel处理器：**
```
args: -device isa-applesmc,osk="ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc" -smbios type=2 -device usb-kbd,bus=ehci.0,port=2 -cpu host,kvm=on,vendor=GenuineIntel,+kvm_pv_unhalt,+kvm_pv_eoi,+hypervisor,+invtsc
```

**AMD处理器：**
```
args: -device isa-applesmc,osk="ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc" -smbios type=2 -device usb-kbd,bus=ehci.0,port=2 -global nec-usb-xhci.msi=off -cpu Penryn,kvm=on,vendor=GenuineIntel,+kvm_pv_unhalt,+kvm_pv_eoi,+hypervisor,+invtsc,+pcid,+ssse3,+sse4.2,+popcnt,+avx,+avx2,+aes,+fma,+fma4,+bmi1,+bmi2,+xsave,+xsaveopt,check
```

> AMD安装时若重启或无加载栏，将 `-cpu host` 替换为 `-cpu Haswell-noTSX`

将 ide 两行的 `media=cdrom` 改为 `media=disk`，确认引导顺序 OpenCore 排第一。

---

## 三、安装系统

1. 启动虚拟机 → OpenCore 引导界面 → 选择 **Base System**
2. 磁盘工具 → 选中目标磁盘 → 抹掉（APFS，GUID分区）
3. 退出磁盘工具 → 选择 **Reinstall macOS** → 选格式化好的磁盘
4. 安装需重启 **4次**：前2次选 Install，后2次直接进系统

---

## 四、使用体验

当前 PVE 上的 OSX 体验仅算**可用水平**，不够流畅。后续可尝试添加 AMD 显卡增强图形性能。

---

## 五、参考链接

- https://github.com/kholia/OSX-KVM
- https://imacos.top/2023/07/29/pve-macos/
- https://www.cnblogs.com/mokou/p/17085923.html
