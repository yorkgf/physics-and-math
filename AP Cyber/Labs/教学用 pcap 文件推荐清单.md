# 教学用 pcap 文件推荐清单

> 为 Unit 3 Wireshark 实验准备。所有文件均可免费下载，来源可靠。
> 建议提前下载好，重命名为对应任务名后分发给学生。

---

## 一、从哪里下载（按优先级）

### 1. Wireshark 官方样本库（最推荐，来源最可靠）

**地址**：[wiki.wireshark.org/SampleCaptures](https://wiki.wireshark.org/SampleCaptures)

Wireshark 官方维护的 pcap 样本集合，按协议分类。**免费、合法、放心用**。

| 协议/主题 | 直接找的关键词 | 用途 |
| --- | --- | --- |
| ARP | SampleCaptures 页面搜 "ARP" | 基础 ARP 流量 |
| DNS | 搜 "DNS" | 正常 DNS 查询/响应 |
| HTTP | 搜 "HTTP" | 普通 web 流量 |
| IEEE 802.11 (无线) | 搜 "802.11" | 演示 evil twin / 无线攻击概念 |

### 2. malware-traffic-analysis.net（真实恶意流量样本）

**地址**：[malware-traffic-analysis.net](https://www.malware-traffic-analysis.net/)

一位安全分析师维护的博客，每月更新真实恶意流量样本，带详细的答案和解析。**适合综合分析任务**。

- 优点：非常真实，每个样本有答案可对照
- 缺点：有些文件需要密码解压（密码在页面上写着）
- 注意：提醒学生不要点击样本里的恶意链接/IP

**推荐入门级样本（选 1–2 个）**：

- 博客首页找 **"2019" 或 "2020"** 年份的题目，难度较低
- 找标签里带 **"basic"** 或 **"beginner"** 的
- 每个样本包含：pcap 文件 + 配套的问题 + 答案页

### 3. Netresec 公共 pcap 库

**地址**：[netresec.com/?page=PcapFiles](https://www.netresec.com/?page=PcapFiles)

另一个知名的 pcap 资源站，有很多真实网络安全事件的抓包。

### 4. 用 Wireshark 自己生成（最可控）

如果你有两台电脑或一台虚拟机，可以**自己造 pcap**：

1. 打开 Wireshark → 选择一个接口 → 开始抓包
2. 在另一台设备执行特定操作（比如 ping 一下、访问一个网站）
3. 停止抓包 → 保存为 `.pcapng`
4. 可以用 `arpspoof` 等工具（Kali Linux 自带）模拟 ARP 欺骗再抓

优点：场景完全由你控制；缺点：花时间。

---

## 二、按实验任务推荐的具体文件

> 下表是根据 Unit 3 Lab 的四个任务，给出的「到哪找、找什么」指引。具体文件名会随站点更新而变化，所以用**搜索关键词**而不是固定文件名。

| 任务 | 推荐来源 | 搜索关键词 | 难度 | 说明 |
| --- | --- | --- | --- | --- |
| **任务 1：ARP 欺骗** | Wireshark SampleCaptures | "ARP" + 找包含 `gratuitous ARP` 或 `ARP poisoning` 字样的链接 | ⭐ 入门 | 如果官方样本不够典型，去 malware-traffic-analysis.net 找带 ARP 攻击的样本 |
| **任务 2：端口扫描** | Wireshark SampleCaptures | "TCP" 里找包含大量 SYN 的样本，或直接搜 "port scan" | ⭐ 入门 | 也可以用 nmap 自己扫一台虚拟机然后抓包生成（最可控） |
| **任务 3：DNS 投毒** | Netresec 或 Wireshark SampleCaptures | "DNS" + 找异常响应的样本 | ⭐⭐ 中等 | 真实 DNS 投毒样本较难找，可以用正常 DNS 样本 + 手工伪造一个异常响应包做对比教学 |
| **任务 4：综合分析** | malware-traffic-analysis.net | 选 2019–2020 年题目，找标有 "basic" 的 | ⭐⭐ 中等 | 选一个包含侦察 → 初始访问 → 数据传输完整链条的样本 |

---

## 三、我的建议：最省事的备课方案

如果你想花最少的时间准备，按下面这条路走：

1. **从 Wireshark 官方 SampleCaptures 下 3–4 个基础协议样本**（ARP、DNS、HTTP 各一个）
   - 用来做任务 1、2、3 的「入门版」，学生先学会看包和用过滤器

2. **从 malware-traffic-analysis.net 选 1 个 basic 级别的综合样本**
   - 用来做任务 4（综合分析），这个网站每个题目都有问题和答案页，你直接用它的问题当作业就行

3. **不需要自己造攻击流量**
   - 真实样本 + 配套答案，教学效果比自己构造的好得多
   - 省时间

---

## 四、下载后要做的事

1. **重命名**：把下载的文件改名为 `任务1-arp.pcap`、`任务2-portscan.pcap` 等，学生一目了然
2. **提前验证**：自己用 Wireshark 打开一遍，确保文件没坏、能看到预期的内容
3. **写答案**：把每个任务的参考答案先自己做出来，这样学生提问时你心里有数
4. **打包分发**：把 4 个 pcap + 实验指导 PDF/Markdown 打成一个压缩包，课上发给学生

---

## 五、法律与安全提醒

- 所有从上述网站下载的 pcap 文件**仅供教学使用**
- pcap 文件里可能包含真实的恶意 IP、域名、URL —— 告诉学生**不要复制出来去真实网络上访问**
- **不要在学校生产网络上启动 Wireshark 的实时抓包**——只做离线分析
- 不要把 pcap 文件上传到公网或分享给校外人员

---

*适用课程：AP Cybersecurity Unit 3*
*版本：v1.0 | 2026 年 8 月*
