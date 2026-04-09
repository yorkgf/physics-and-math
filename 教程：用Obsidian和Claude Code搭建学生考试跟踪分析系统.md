# 用 Obsidian 和 Claude Code 搭建学生考试跟踪分析系统

> 手把手教你从零搭建一个自动化的学生考试分析系统。只需 6 步，你就能在 Obsidian 里用 AI 自动分析试卷、追踪学生薄弱点、生成教学建议。
>
> **你不需要任何编程基础，跟着做就行。**

---

## 目录

1. [安装 Obsidian 并开启社区插件](#第一步安装-obsidian-并开启社区插件)
2. [安装 CC-Switch（API 切换工具）](#第二步安装-cc-switchapi-切换工具)
3. [安装 Claude Code](#第三步安装-claude-code)
4. [通过 CC-Switch 配置 Claude Code 的 API](#第四步通过-cc-switch-配置-claude-code-的-api)
5. [验证 Claude Code 可用](#第五步验证-claude-code-可用)
6. [在 Obsidian 中安装 Agent Client 插件](#第六步在-obsidian-中安装-agent-client-插件)

---

## 第一步：安装 Obsidian 并开启社区插件

### 1.1 下载安装 Obsidian

1. 打开浏览器，访问 [obsidian.md](https://obsidian.md)
2. 页面会自动识别你的操作系统，点击下载按钮
3. 下载完成后，双击安装包，按提示完成安装

> Obsidian 是完全免费的，不需要注册账号。

### 1.2 创建你的第一个 Vault（知识库）

Vault 就是 Obsidian 中的一个文件夹，你所有的笔记都存在里面。

1. 打开 Obsidian，看到欢迎界面
2. 点击 **"Create new vault"**
3. 填写：
   - **Vault name**：比如 `Teaching Notes`
   - **Location**：选择一个你喜欢的位置，比如 `文档/Teaching Notes`
4. 点击 **"Create"**

完成后你会进入 Obsidian 主界面：左边是文件列表，右边是编辑区。

### 1.3 开启社区插件

Obsidian 默认禁用了社区插件，我们需要手动开启：

1. 点击左下角的 **齿轮图标**（Settings）
2. 左侧菜单点击 **"Community plugins"**
3. 点击 **"Turn on community plugins"**
4. 弹出确认框，点击 **"I accept the risk"**

> 后面要安装的 BRAT 和 Agent Client 插件都需要这个开关打开。

---

## 第二步：安装 CC-Switch（API 切换工具）

CC-Switch 是一个桌面应用，让你可以用国产大模型 API（智谱 GLM、DeepSeek、Kimi 等）来驱动 Claude Code，不需要购买 Anthropic 的海外订阅。

项目地址：[https://github.com/farion1231/cc-switch](https://github.com/farion1231/cc-switch)

### 2.1 下载安装

根据你的操作系统选择安装方式：

**macOS：**

打开终端（Terminal），运行：

```bash
brew tap farion1231/ccswitch && brew install --cask cc-switch
```

> 如果没有 Homebrew，先去 [brew.sh](https://brew.sh) 按提示安装。

**Windows：**

1. 打开 [CC-Switch Releases 页面](https://github.com/farion1231/cc-switch/releases)
2. 下载最新的 `.msi` 安装包
3. 双击安装，按提示完成

**Linux：**

1. 打开 [CC-Switch Releases 页面](https://github.com/farion1231/cc-switch/releases)
2. 下载 `.deb`（Ubuntu/Debian）或 `.AppImage`（通用）
3. `.deb` 文件双击安装，`.AppImage` 文件添加执行权限后直接运行

### 2.2 验证安装

安装完成后打开 CC-Switch，如果能看到主界面，说明安装成功。

> CC-Switch 内置了 50 多个服务商预设，包括智谱 GLM、DeepSeek、Kimi、通义千问等。

---

## 第三步：安装 Claude Code

Claude Code 是 Anthropic 的 AI 编程助手。我们用它来自动分析试卷、生成分析报告。

### 3.1 前置条件：安装 Node.js

Claude Code 需要 Node.js（版本 18 或更高）。

检查是否已安装——打开终端，运行：

```bash
node --version
```

如果显示 `v18.x.x` 或更高的版本号，说明已安装，跳过这步。

如果没有安装：

**macOS（用 Homebrew）：**

```bash
brew install node
```

**Ubuntu / Debian / Linux：**

```bash
sudo apt update && sudo apt install nodejs npm
```

**Windows：**

去 [nodejs.org](https://nodejs.org) 下载安装包，选择 LTS 版本。

### 3.2 安装 Claude Code

在终端中运行：

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

> 如果下载慢，可能需要科学上网。

### 3.3 验证安装

```bash
claude --version
```

显示版本号就说明成功了。

> 这时直接运行 `claude` 会提示需要 API key，没关系，下一步解决。

---

## 第四步：通过 CC-Switch 配置 Claude Code 的 API

这一步让 Claude Code 使用你选择的模型 API 来运行。

### 4.1 获取 API Key

选择一个模型服务商，注册并获取 API Key：

| 服务商 | 获取地址 | 说明 |
|--------|---------|------|
| **智谱 GLM** | [open.bigmodel.cn](https://open.bigmodel.cn) | 新用户有免费额度 |
| **DeepSeek** | [platform.deepseek.com](https://platform.deepseek.com) | 价格很低 |
| **Kimi（月之暗面）** | [platform.moonshot.cn](https://platform.moonshot.cn) | 支持超长文本 |
| **通义千问** | [dashscope.console.aliyun.com](https://dashscope.console.aliyun.com) | 阿里云旗下 |

点击对应链接，注册账号，在控制台创建 API Key。

### 4.2 在 CC-Switch 中添加服务商

1. 打开 CC-Switch 应用
2. 点击 **"Add Provider"**（添加服务商）
3. 你可以：
   - 从**预设列表**中选择（已包含主流服务商）
   - 或手动填写 API Base URL 和模型名称
4. 粘贴你的 API Key
5. 点击 **"Save"**（保存）

### 4.3 启用服务商

在 CC-Switch 中，点击你想使用的服务商旁边的开关，将其启用。

CC-Switch 支持**热切换**——切换后 Claude Code 会自动使用新的 API，不需要重启。

---

## 第五步：验证 Claude Code 可用

正式使用前，先测试一下。

### 5.1 进入你的 Vault 目录

```bash
cd ~/文档/Teaching\ Notes
```

> 把路径替换成你第一步创建 Vault 时选的位置。路径中有空格要用 `\` 转义或用引号包裹。

### 5.2 启动 Claude Code

```bash
claude
```

### 5.3 测试

在 Claude Code 中输入：

```
你好，请创建一个测试文件 test.md，内容为 "Hello from Claude Code!"
```

如果它成功创建了文件，你可以在 Obsidian 的文件列表中看到 `test.md`。说明一切正常！

测试完删掉它：

```
请删除 test.md 文件
```

---

## 第六步：在 Obsidian 中安装 Agent Client 插件

这一步让 Claude Code 直接嵌入到 Obsidian 中，你不用切换到终端，直接在 Obsidian 里就能用。

### 6.1 安装 BRAT 插件

BRAT 是一个 Obsidian 社区插件，用来安装还没上架官方商店的第三方插件。

1. 在 Obsidian 中打开 **Settings**（设置）
2. 进入 **Community plugins**（第三方插件）
3. 点击 **"Browse"**（浏览），搜索 **"BRAT"**
4. 找到 **"Obsidian42 - BRAT"**，点击 **"Install"**（安装）
5. 安装完点击 **"Enable"**（启用）

### 6.2 通过 BRAT 安装 Agent Client

Agent Client 是把 Claude Code 嵌入 Obsidian 的插件，通过 ACP 协议通信。

1. 按 `Ctrl+P`（macOS 按 `Cmd+P`）打开命令面板
2. 输入 **"BRAT"**，选择 **"BRAT: Add a Beta plugin with a frozen version"** 或 **"BRAT: Add Beta plugin"**
3. 在输入框中粘贴仓库地址：
   ```
   https://github.com/RAIT-09/obsidian-agent-client
   ```
4. 点击确认，等待下载
5. 下载完成后，回到 **Settings → Community plugins**
6. 在已安装列表中找到 **"Agent Client"**，打开开关启用

### 6.3 安装 ACP Adapter

ACP Adapter 是一个命令行工具，把 Claude Code 的能力桥接到 Obsidian 插件中。

在终端中运行：

```bash
npm install -g @agentclientprotocol/claude-agent-acp
```

验证安装并获取路径：

```bash
which claude-agent-acp
```

记下输出的路径（比如 `/usr/local/bin/claude-agent-acp`），下一步要用。

同时记下 Node.js 的路径：

```bash
which node
```

### 6.4 在 Obsidian 中配置 Agent Client

1. 打开 Obsidian **Settings**
2. 左侧找到 **"Agent Client"**（在 Community plugins 下面）
3. 填写以下配置：

| 配置项 | 填什么 | 怎么获取 |
|--------|--------|---------|
| **Node.js Path** | Node.js 的完整路径 | 终端运行 `which node`，如 `/usr/local/bin/node` |
| **Agent Command** | ACP adapter 的完整路径 | 上一步 `which claude-agent-acp` 的输出 |
| **Working Directory** | 你的 Vault 文件夹路径 | 如 `/Users/你的用户名/Documents/Teaching Notes` |

4. 点击 **Save** 保存

### 6.5 开始使用

配置完成后：

1. Obsidian 右侧或底部会出现一个 **Agent Client 面板**
2. 点击面板中的聊天输入框
3. 输入你的指令，比如：

```
请分析这份考试试卷和学生答题情况：

PDF 试卷路径：~/下载/QuarterQuiz.pdf
学生答题CSV：~/下载/Student_Matrix_Report.csv

要求：
1. 在 题库/ 文件夹下为每道题创建分析文件
2. 每个题目文件包含：正确答案、学生答题表格、正确率、知识点分析
3. 创建 Student Analysis.md，包含每位学生的知识点错误表格
4. 创建考试概览文件，包含班级成绩、薄弱点排名、教学建议
```

Claude Code 会自动分析并生成所有文件，你直接在 Obsidian 中就能看到结果！
效果如下（蓝色字体的例题都是可点击的链接）：
![[Pasted image 20260402121533.png]]
![[Pasted image 20260402121636.png]]
![[Pasted image 20260402121751.png]]