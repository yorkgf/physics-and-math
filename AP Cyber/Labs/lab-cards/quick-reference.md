# DVWA实验快速参考卡片

## 🔑 登录信息

| 项目 | 值 |
|-----|---|
| 靶场地址 | `http://192.168.0.169` |
| 用户名 | `admin` |
| 密码 | `password` |
| 安全级别 | Low（实验用） |

---

## 🎯 实验快速索引

### 按攻击类型

| 攻击类型 | 实验编号 | 关键Payload |
|---------|---------|------------|
| 暴力破解 | Lab 02 | 常用密码字典 |
| SQL注入 | Lab 03 | `1' OR '1'='1` |
| XSS | Lab 04 | `<script>alert('XSS')</script>` |
| CSRF | Lab 05 | 伪造请求链接 |
| 文件上传 | Lab 06 | PHP WebShell |
| 命令注入 | Lab 07 | `127.0.0.1 && whoami` |
| 文件包含 | Lab 08 | `../../../../../etc/passwd` |

### 按CED单元

| 单元 | 相关实验 |
|-----|---------|
| Unit 1: Introduction to Security | Lab 02 |
| Unit 3: Securing Networks | Lab 09 |
| Unit 4: Securing Devices | Lab 01, 02, 06, 09 |
| Unit 5: Securing Applications | Lab 03, 04, 05, 06, 07, 08, 10 |

---

## 📊 实验时长与难度

```
难度：★☆☆ (简单)  ★★☆ (中等)  ★★★ (困难)

Lab 01 ★☆☆ 30min  环境配置
Lab 02 ★☆☆ 30min  暴力破解
Lab 03 ★★☆ 30min  SQL注入
Lab 04 ★★☆ 30min  XSS
Lab 05 ★★☆ 30min  CSRF
Lab 06 ★★☆ 30min  文件上传
Lab 07 ★★☆ 30min  命令注入
Lab 08 ★★★ 30min  文件包含
Lab 09 ★★☆ 30min  日志分析
Lab 10 ★★★ 30min  综合评估
```

---

## 🛡️ 防御措施速查

### SQL注入防御
- ✅ 参数化查询
- ✅ 输入验证
- ✅ 使用ORM框架
- ❌ 字符串拼接SQL

### XSS防御
- ✅ 输出编码（htmlspecialchars）
- ✅ 内容安全策略(CSP)
- ✅ HttpOnly Cookie
- ❌ 直接输出用户输入

### CSRF防御
- ✅ CSRF Token
- ✅ SameSite Cookie
- ✅ 验证Referer
- ❌ 仅依赖Cookie认证

### 文件上传防御
- ✅ 白名单验证
- ✅ 文件内容检查
- ✅ 重命名文件
- ❌ 仅检查扩展名

### 命令注入防御
- ✅ 使用语言内置API
- ✅ escapeshellarg()
- ✅ 输入验证
- ❌ 字符串拼接命令

### 文件包含防御
- ✅ 禁用远程包含
- ✅ 白名单限制
- ✅ open_basedir
- ❌ 直接使用用户输入

---

## 🔍 日志分析关键词

### 攻击特征关键词

| 攻击类型 | 关键词 |
|---------|--------|
| SQL注入 | `UNION`, `SELECT`, `OR '1'='1`, `--`, `DROP` |
| XSS | `<script>`, `onerror`, `onload`, `javascript:` |
| 命令注入 | `&&`, `\|\|`, `;`, `\|`, `whoami`, `cat` |
| 文件包含 | `../`, `..\\`, `/etc/passwd`, `php://` |
| 目录遍历 | `../`, `..\\`, `/etc/`, `/var/` |

### 常用日志命令

```bash
# 查看访问日志
tail -f /var/log/apache2/access.log

# 搜索攻击特征
grep "UNION" /var/log/apache2/access.log
grep "<script>" /var/log/apache2/access.log
grep "whoami" /var/log/apache2/access.log

# 统计攻击次数
grep -c "UNION" /var/log/apache2/access.log
```

---

## 📝 实验记录模板

### 攻击记录表

| 日期 | 实验 | Payload | 结果 | 备注 |
|-----|------|---------|------|------|
| | | | | |
| | | | | |
| | | | | |

### 漏洞评估表

| 漏洞 | 严重程度 | 利用难度 | 影响范围 | 防御措施 |
|-----|---------|---------|---------|---------|
| | | | | |
| | | | | |
| | | | | |

### 风险评估矩阵

| 可能性 \ 影响 | 低 | 中 | 高 |
|-------------|---|---|---|
| 高 | 中 | 高 | 严重 |
| 中 | 低 | 中 | 高 |
| 低 | 低 | 低 | 中 |

---

## 🎓 CED学习目标速查

### Skill Category 1: Analyze Risk
- 1.A 识别漏洞、威胁和攻击方法
- 1.B 确定攻击者如何利用漏洞
- 1.C 评估风险的可能性和影响
- 1.D 记录风险的可能性和影响

### Skill Category 2: Mitigate Risk
- 2.A 识别安全控制并解释如何缓解风险
- 2.B 确定分层安全控制
- 2.C 评估保护性风险管理策略的影响
- 2.D 实施并记录缓解措施

### Skill Category 3: Detect Attacks
- 3.A 识别监控系统的方法
- 3.B 确定检测攻击的策略和方法
- 3.C 评估威胁检测方法的影响
- 3.D 通过分析数字证据检测和分类攻击

---

## ⚠️ 安全提醒

### 合法使用原则

1. **只在授权环境中测试**
   - 使用提供的DVWA靶场
   - 不要对真实系统进行测试

2. **遵守道德规范**
   - 尊重他人系统和数据
   - 不进行非法活动

3. **保密意识**
   - 不分享访问凭据
   - 不泄露敏感信息

### 紧急情况

如发现真实系统存在漏洞：
1. 不要进行进一步测试
2. 立即报告给系统管理员
3. 记录发现的漏洞
4. 不要公开漏洞信息

---

## 📞 联系信息

| 项目 | 联系方式 |
|-----|---------|
| 技术支持 | ____________ |
| 教师邮箱 | ____________ |
| 紧急联系 | ____________ |

---

## 📖 参考资源

### 学习网站
- OWASP: https://owasp.org
- PortSwigger: https://portswigger.net/web-security
- HackTheBox: https://www.hackthebox.com

### 工具下载
- Burp Suite: https://portswigger.net/burp
- OWASP ZAP: https://www.zaproxy.org
- Nmap: https://nmap.org

### 文档参考
- DVWA Documentation: https://github.com/digininja/DVWA
- OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/

---

**快速参考卡片 v1.0 | 2026-08-26**
