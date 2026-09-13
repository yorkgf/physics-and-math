# DVWA × AP Cybersecurity CED 实验映射表

> 校验日期：2026-09-02
> 校验方式：SSH 进入靶机逐份阅读 `/var/www/html/dvwa/vulnerabilities/*/source/*.php` 源码
> 靶场版本：DVWA master（digininja/DVWA），Apache 2.4.52 + PHP 8.1 + MariaDB 10.6
> 用途：确定哪些 CED 学习目标可在本靶场落地实操，哪些需外部工具

---

## 零、结论修正（重要）

本表推翻了早期"DVWA 只能覆盖约 40% CED"的估计。**实际安装版含 19 个漏洞模块**（不是旧版教材里的 12 个），多出 `cryptography`、`open_redirect`、`bac`、`authbypass`、`csp`、`javascript`、`weak_id`、`api` 八个模块，使 **Unit 5 接近全覆盖、Unit 1.1 与 4.2 获得原本以为缺失的支撑**。

修正后的可落地范围：**Unit 1 的 1.2 / Unit 2 的 2.1 / Unit 4 的 4.1–4.4 / Unit 5 的 5.1–5.3、5.5–5.6**。

---

## 一、主表：19 个模块 → CED 精确映射

强度标记：🟢 直接对应必备知识 | 🟡 概念性对应（无精确 EK 编号）| ⭐ 本模块独有教学价值

| # | 模块（菜单名） | 源码实际特征（已验证） | 演示的漏洞 | CED 映射 | 强度 |
|---|---|---|---|---|---|
| 1 | Brute Force | `$_GET` 传参、`md5()`、SQL 拼接、无 token、无锁定 | 在线口令爆破 / 默认凭据 | 1.2.A.1, 1.2.A.2, 1.2.B.2, 1.2.C.1-C.2, 4.2.B.5, 4.2.B.6, 4.2.D.5, 4.4.A.6, 4.4.D.1 | 🟢⭐ |
| 2 | SQL Injection | `user_id = '$id'` 直接拼接 | SQL 注入（联合/联合读出全表） | 5.1.B.2, 5.1.B.3, 5.1.B.4, 5.5.B.1, 5.5.B.2, 5.6.E.1, 2.1.F.1 | 🟢 |
| 3 | SQL Injection (Blind) | 只回"存在/不存在"，无数据回显 | 布尔盲注、时间盲注 | 5.1.B.4 深化；5.6.E.1（日志侧信道） | 🟢 |
| 4 | Command Injection | `shell_exec('ping ' . $target)`，无过滤 | 命令拼接（`;`、`&&`） | 5.1.B.2, **5.5.B.1（分号被明确列为 control character）**, 4.1.C.1, 5.6.E.1 | 🟢⭐ |
| 5 | XSS (Reflected) | `echo '<pre>Hello ' . $_GET['name']`，且 `X-XSS-Protection: 0` | Type I 反射型 | 5.1.B.5, 5.1.B.6, 5.6.E.2, 1.1.C.3 | 🟢 |
| 6 | XSS (Stored) | 留言板入库，仅 escape 未 HTML 编码 | Type II 存储型 | 5.1.B.6（明列 comment field / forum post / visitor log）, 5.6.E.2 | 🟢 |
| 7 | XSS (DOM) | 纯前端 `# No protections, anything goes` | DOM 型（服务端日志看不到！） | 5.1.B.5 延伸；**与 5.6.E.2 形成"日志检测失效"讨论** | 🟢⭐ |
| 8 | CSRF | `if(isset($_GET['Change']))` 改密码，无 token | 跨站请求伪造 | 1.1.C.3（点链接的后果）, 2.1.F.3（token=预防控制）, 5.1.B.2 | 🟡 |
| 9 | File Inclusion | `$file = $_GET['page']` 无白名单 | LFI / RFI / 目录遍历 | 5.1.B.9, 5.1.B.10, 5.5.B.2, 5.6.E.4（`../` 检测） | 🟢 |
| 10 | File Upload | `basename($_FILES[...]['name'])` 后直接 `move_uploaded_file`，**零类型校验** | webshell 上传 | 5.1.A.3, 4.1.B.2（RAT/恶意软件）, 4.3.A.3（软件安装策略）, 5.5.B | 🟢 |
| 11 | Insecure CAPTCHA | 校验 `step` 参数，可跳过步骤 2 | 业务流程绕过 / 重放 | 5.1.B.2（逻辑未验证）, 4.2.C（认证因素讨论） | 🟡 |
| 12 | Weak Session IDs | `$_SESSION['last_session_id']++` 可预测递增 | 可预测会话标识 | 5.1.B.2, 4.4.A.4（IoC）, 2.1.F.3 | 🟡⭐ |
| 13 | Authorisation Bypass | 逻辑在 `dvwaPage.inc.php`：按级别设 `httponly` / `SameSite` | Cookie 属性与认证会话操控 | 2.1.F.2（技术控制）, 4.2.A.5, 4.2.C.1 | 🟡 |
| 14 | Broken Access Control (BAC) | low 级 `$role = $_COOKIE['user_role']` → **角色来自客户端 cookie** | 越权提权（改 cookie 即成 admin） | 5.1.A.2, 5.1.A.3, **5.2.C（选择访问控制模型）**, 2.1.F.1 | 🟢⭐ |
| 15 | Cryptography | low=`base64`+`xor_this()`；medium=`openssl aes`；high/impossible=ECB / oracle attack | 编码≠加密、小 keyspace、ECB 模式缺陷 | 5.3.A.2, 5.3.A.3（keyspace）, 5.3.A.4（对称）, 5.3.B.1-B.3, 4.2.A.1 | 🟢⭐ |
| 16 | CSP Bypass | 头里白名单放行 `pastebin.com / unpkg.com / cdn.jsdelivr.net` | 信任列表内的脚本注入 | 2.1.F.2, 5.5.B（校验思路）, 5.1.B.5 延伸 | 🟡⭐ |
| 17 | JavaScript Attacks | 前端内嵌 MD5 库，密码在浏览器侧哈希 | 客户端校验可绕过；JS 可接触敏感数据 | **5.1.B.5（原文即"Javascript…can access sensitive data…like usernames, passwords"）** | 🟢⭐ |
| 18 | Open HTTP Redirect | `header("location: " . $_GET['redirect'])` 零校验 | 可信域名伪装跳转 | **1.1.A.1, 1.1.B.1（社交工程落地页）**, 3.1.A.3（credential harvesting）, 1.1.C.3 | 🟢⭐ |
| 19 | API | 读 `REQUEST_URI`，服务端可控参数 | 接口层信任问题 | 5.1.B.2, 5.2.C | 🟡 |

---

## 二、反向索引：按 CED 单元找可用模块

### Unit 1 · Introduction to Security

| 主题 | 可用模块 | 说明 |
|---|---|---|
| 1.1 社交工程 | **Open HTTP Redirect**、XSS (Stored) 挂假表单 | 🔧 **修正**：不需要 GoPhish 也能演示"可信链接把人送到假页面" |
| 1.2 可疑网站登录 | Brute Force（全套） | 最完整的模块级支撑 |
| 1.3 公共 Wi-Fi | ⚠️ 需外部：Wireshark/tshark（已装）+ USB 无线网卡 | DVWA 只作被抓包的目标；1.3.B 无线攻击仍需硬件 |
| 1.4 AI 攻击 | 无直接对应 | 配合 LLM 课程 |
| 1.5 AI 防御 | **Brute/SQLi/XSS 产生的真实 access.log 作为 AI 分析素材** | 🔧 修正：不必造假 CSV |

### Unit 2 · Securing Spaces

| 主题 | 可用模块 | 说明 |
|---|---|---|
| 2.1.A 社交工程基础 | Open Redirect、XSS | |
| 2.1.B 对手类型 | Brute（script kiddy 用现成工具）vs 盲注（高技术门槛）→ 对应 2.1.B.1 | ⭐ 用难度差讲"攻击者画像" |
| 2.1.F 控制类型分类 | **四级 security level 对照 = 活教材**（见第三节） | |
| 2.1.G 纵深防御 | Brute 的 high 级（加了 token 却仍无锁定） | ⭐ 证明"有控制≠防住该类威胁" |
| 2.2–2.4 物理安全 | ❌ 无 | 讲授 + 实物 |

### Unit 3 · Securing Networks

| 主题 | 可用模块 | 说明 |
|---|---|---|
| 3.1.A.3 DNS 投毒 / credential harvesting | Open Redirect 演示同类后果 | 🟡 类比映射 |
| 3.1.C.2 漏洞扫描器 | 用 nmap（已装）扫靶机 | ✅ |
| 3.4 防火墙 | 给靶机配 ufw 白名单 | ✅ 防御实验 |
| 3.5.NIDS/NIPS/SIEM | ❌ 需 Suricata/Security Onion | 可用 access.log 做入门分析 |
| 3.2/3.3 无线、分段 | ❌ | |

### Unit 4 · Securing Devices

| 主题 | 可用模块 | 说明 |
|---|---|---|
| 4.1.B 恶意软件 | File Upload（传 webshell ≈ RAT） | ✅ |
| 4.1.C 设备漏洞利用 | Command Injection（`shell_exec` 执行任意命令） | ✅ |
| 4.2.A 为何用哈希存口令 | `users` 表现成 MD5；`admin` 与 `smithy` 哈希相同 | ⭐ 铁证"无盐" |
| 4.2.B 在线/离线攻击、字典、彩虹表、口令喷洒、默认凭据 | Brute（在线）+ 导出哈希用 john（已装）离线破 | 🟢 全套 |
| 4.2.C 认证因素 | Insecure CAPTCHA、Authorisation Bypass | 🟡 |
| 4.2.D 配置登录设置 | **Impossible 级源码内含 `total_failed_login=3` / `lockout_time=15`** | ⭐ 可直接改参数做实验 |
| 4.4 检测设备攻击 / IoC | Apache `access.log` + DVWA `security_log` 表 | 🟢 |

### Unit 5 · Securing Applications and Data（最强区）

| 主题 | 可用模块 |
|---|---|
| 5.1.B.2 注入 | SQLi、Blind SQLi、Command Injection |
| 5.1.B.4 SQL 注入 | SQLi、Blind SQLi |
| 5.1.B.6 XSS 两种类型 | XSS Reflected / Stored / DOM |
| 5.1.B.7-B.8 缓冲区溢出 | ❌ 需专门靶场（Protostar）；只能靠超长参数演示"检测侧"（5.6.E.3） |
| 5.1.B.10 目录遍历 | File Inclusion |
| 5.2.C 访问控制模型 | **BAC** |
| 5.3.A/B 对称加密 | **Cryptography**（XOR→AES→ECB 攻击三级递进） |
| 5.4 非对称加密 | ❌ 需 GPG/OpenSSL CLI 实验 |
| 5.5.B 输入净化 | **任意模块的 low/medium/high/impossible 源码对比** |
| 5.6.E 日志检测攻击 | SQLi（`'`/`OR 1=1`/`--`）、XSS（`<script>`）、遍历（`../`）、溢出（超长 URL） |

---

## 三、⭐ 最高价值的跨模块素材：Security Level 四级阶梯

这是本靶场**独有且 CED 难以用其他方式讲清**的教学资产。以 Brute 模块为例（源码实测）：

| 防护项 | low | medium | high | impossible |
|---|---|---|---|---|
| HTTP 方法 | GET | GET | GET | **POST** |
| 口令出现在 URL | ✅ | ✅ | ✅ | ❌ |
| Anti-CSRF token | ❌ | ❌ | ✅ | ✅ |
| SQL escape | ❌ | ✅ | ✅ | PDO 参数化 |
| 失败延迟 | 无 | `sleep(2)` | `sleep(rand(0,3))` | `sleep(rand(2,4))` |
| 失败计数 | ❌ | ❌ | ❌ | ✅ `failed_login+1` |
| **账号锁定** | ❌ | ❌ | ❌ | ✅ **3 次 / 15 分钟** |
| 成功后安全告警 | ❌ | ❌ | ❌ | ✅ |
| cookie `httponly`+`SameSite=Strict` | ❌ | ❌ | ❌ | ✅ |

**核心教学点（务必进教案）**
> **high 级别依然能被爆破。** 因为它加的是 CSRF token 和 SQL escape —— 这两项对"反复猜口令"贡献为零。
> 对应 2.1.F.3（控制按功能分类）+ 2.1.G（纵深防御）：一个控制只覆盖它设计针对的那类威胁。

**彩蛋 1｜防护自身引入新漏洞**（源码原注释）
```php
// User locked out.  Note, using this method would allow for user enumeration!
```
→ 若告知"该账号已锁定"，等于确认该用户名存在（用户枚举）。讨论：如何既防爆破又不泄露账号存在性。

**彩蛋 2｜锁定即 DoS 面**（对应 3.1.A.4 + CIA 的 A）
→ 攻击者可用错密码故意锁死他人账号 15 分钟。讨论：锁账号 / 锁 IP / 只告警 的取舍。

---

## 四、⚠️ 本靶场实施注意事项（源码级，已验证）

1. **新版默认安全级别是 `impossible`**（cookie 缺失时回落）→ 学生首次进入"破不了"，必须先 `DVWA Security` 设 low。
2. **所有漏洞模块要求已认证**：`dvwaPageStartup(array('authenticated'))` → 未登录访问 `/vulnerabilities/brute/` 会 **302 → login.php**。**所以不能把 brute 页 URL 直接发给学生当爆破入口**。
   → 教学口径：把 `admin/password` 定位成"靶场出厂默认账号 = 已入站身份"（正好对应 4.2.B.5 默认凭据），爆破目标改为 `gordonb`/`1337`/`pablo`/`smithy`。
3. **5 个账号都能登录且登录后权限完全相同**（`login.php` 不检查 `role`）→ 可做"五组守己攻人"红蓝对抗，各组会话独立（级别存 cookie，不互串）。
4. **`account_enabled` 列建了但全仓无任何代码引用** → 设为 0 仍能登录。极佳讨论题：**控制存在于代码中，不存在于字段、配置或文档中。**
5. **impossible 的锁定是账号级、全局生效** → 学生爆破 admin 会把共享账号锁死 15 分钟，全班登不进。→ 该轮改用非 admin 目标，或由教师演示。
6. 本版本**无改口令 GUI**（旧版有 DVWA Users）→ 防守回合需直接 `UPDATE users SET password=MD5(...)`.
7. Brute 模块在 high 级别仍是 GET + 每轮需重取 token，脚本需相应改造。

---

## 五、DVWA 无法覆盖的 CED 内容（需外部工具）

| CED | 需要 |
|---|---|
| 1.3.B 无线攻击（evil twin / deauth / WPA 破解） | USB 无线网卡（AR9271）+ aircrack-ng |
| 2.2–2.4 物理安全与检测 | 讲授 + 实物 |
| 3.1.A.1/A.2 ARP 投毒、MAC flooding | 双 VM + bettercap/scapy |
| 3.2/3.3 无线安全、网络分段与 DMZ | Packet Tracer / GNS3 |
| 3.5.A.2-A.4 NIDS/NIPS/SIEM | Suricata 或 Security Onion |
| 4.3.B 反恶意软件、4.3.C 补丁管理 | 独立 VM 对比实验 |
| 5.1.B.7/B.8 缓冲区溢出 | Protostar / 专门靶场 |
| 5.4 非对称加密（RSA/ECC、密钥长度） | GPG / OpenSSL CLI |
| 5.2.D Linux 访问控制配置 | 直接在靶机命令行练 |

---

## 六、建议实施顺序（复用度优先）

```
① 1.2  Brute Force 四级阶梯         ← 实验包已完成
② 4.2  users 表哈希 + 在线/离线破解  ← 复用①的靶场与账号，改动最小 ★下一步
③ 4.4/5.6  攻击后 access.log 找 IoC  ← 复用①②产生的真实日志
④ 1.5  把③的日志喂给 LLM 做对比      ← 复用同一份日志
⑤ 5.1  SQLi / XSS / LFI / Upload 四连
⑥ 5.5  任意模块四级源码对比（防守视角）
⑦ 5.3  Cryptography（Base64→XOR→AES→ECB）
⑧ 1.1  Open HTTP Redirect 钓鱼跳转
```

②③④ 三步共享同一批数据，一次准备连上四节课 —— 这是本靶场性价比最高的路径。

---

*相关：[[Unit 1-2 实操场景与教学计划]] · [[AP Cybersecurity - Syllabus 2026-2027]] · 实验包见 `~/tmp/dvwa_teaching/`*
