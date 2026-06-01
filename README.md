# 🌍 语言切换 | Language Switcher

[![简体中文](https://img.shields.io/badge/简体中文-✓-green?style=for-the-badge)](README.md)
[![English](https://img.shields.io/badge/English-✓-blue?style=for-the-badge)](README_en.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-✓-orange?style=for-the-badge)](README_zh_TW.md)
[![日本語](https://img.shields.io/badge/日本語-✓-pink?style=for-the-badge)](README_ja.md)

---

# 🎛️ TermMux-CLI

> **轻量级终端多路复用与AI Agent感知管理器**
> **Lightweight Terminal Multiplexer with AI Agent Awareness**

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-yellow.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-cyan.svg)](https://github.com/gitstq/TermMux-CLI)
[![Stars](https://img.shields.io/github/stars/gitstq/TermMux-CLI?style=social)](https://github.com/gitstq/TermMux-CLI)

---

## 🎉 项目介绍

**TermMux-CLI** 是一款专为开发者设计的**轻量级终端多路复用器**，灵感来源于 [herdr](https://github.com/ogulcancelik/herdr)，但使用 **Python** 实现，更易于安装和扩展。

### ✨ 核心价值

- 🔧 **工作区管理** - 轻松创建、切换、重命名、关闭工作区
- 🪟 **窗格分屏** - 水平/垂直分屏，灵活布局
- 🤖 **AI Agent感知** - 实时检测并显示Claude Code、Cursor等Agent的状态
- 💾 **会话持久化** - 保存和恢复工作区布局，永不丢失
- 🎨 **现代化TUI** - 基于Rich库构建的精美终端界面
- ⚡ **零核心依赖** - 仅依赖 Rich 和 psutil，开箱即用

### 💡 灵感来源

本项目灵感来源于 [herdr](https://github.com/ogulcancelik/herdr)，一款用 Rust 编写的优秀终端多路复用器。TermMux-CLI 采用 Python 实现，目标是：
- 降低安装门槛 (`pip install termmux-cli`)
- 更易于定制和扩展
- 为 Python 开发者提供熟悉的开发体验

---

## ✨ 核心特性

### 🏠 工作区管理
- 📁 多工作区支持，每个工作区独立管理
- 🔄 工作区切换、重命名、删除
- 📊 工作区状态一目了然

### 🪟 窗格管理
- ➕ 创建新窗格
- ⏹️ 水平/垂直分屏
- ❌ 关闭窗格
- 🔲 窗格聚焦切换

### 🤖 AI Agent感知
支持自动检测以下AI Agent的运行状态：

| Agent | 状态检测 | 状态指示 |
|-------|---------|---------|
| Claude Code | ✅ | 🟢🟡🔴🔵 |
| Cursor Agent | ✅ | 🟢🟡🔴🔵 |
| GitHub Copilot | ✅ | 🟢🟡🔴🔵 |
| OpenAI Codex | ✅ | 🟢🟡🔴🔵 |
| Gemini CLI | ✅ | 🟢🟡🔴🔵 |
| Kiro CLI | ✅ | 🟢🟡🔴🔵 |

**Agent状态说明：**
- 🟢 **空闲 (Idle)** - Agent已就绪，等待输入
- 🟡 **工作中 (Working)** - Agent正在执行任务
- 🔴 **阻塞 (Blocked)** - Agent等待用户确认或输入
- 🔵 **完成 (Done)** - 任务已完成

### 💾 会话管理
- 💾 一键保存当前工作区布局
- 📂 加载历史会话
- 🗑️ 删除不再需要的会话
- 📋 会话列表管理

---

## 🚀 快速开始

### 📋 环境要求

- Python 3.8 或更高版本
- Linux / macOS / Windows

### 🔧 安装

#### 方式一：pip 安装 (推荐)

```bash
pip install termmux-cli
```

#### 方式二：从源码安装

```bash
# 克隆仓库
git clone https://github.com/gitstq/TermMux-CLI.git
cd TermMux-CLI

# 安装依赖
pip install -r requirements.txt

# 运行
python termmux-cli.py
```

### 🎮 使用方法

```bash
# 启动交互模式
termmux

# 或者
python termmux-cli.py
```

### ⌨️ 快捷键

| 按键 | 功能 |
|-----|------|
| `n` | 新建工作区 |
| `s` | 保存当前会话 |
| `l` | 加载历史会话 |
| `r` | 刷新AI Agent检测 |
| `q` | 退出程序 |

---

## 📖 详细使用指南

### 🏠 工作区操作

```python
from src.workspace import Workspace, WorkspaceManager

# 创建工作区管理器
manager = WorkspaceManager()

# 创建新工作区
ws = manager.create_workspace("我的项目")

# 切换工作区
manager.switch_workspace(0)

# 重命名工作区
manager.rename_workspace(ws.id, "新名称")

# 删除工作区
manager.delete_workspace(ws.id)
```

### 🪟 窗格操作

```python
from src.pane import Pane, PaneManager, SplitDirection

# 创建窗格管理器
manager = PaneManager()

# 创建窗格
pane = manager.create_pane(
    title="终端",
    command="bash",
    working_directory="/home/user"
)

# 分割窗格
new_pane = manager.split_pane(pane.id, SplitDirection.HORIZONTAL)

# 关闭窗格
manager.close_pane(pane.id)
```

### 🤖 Agent检测

```python
from src.agent import AgentDetector, AgentStatus

# 创建检测器
detector = AgentDetector()

# 扫描运行中的Agent
detector.scan()

# 获取检测结果
agents = detector.get_detected_agents()

# 按状态筛选
working_agents = detector.get_agents_by_status(AgentStatus.WORKING)

# 获取状态摘要
summary = detector.get_agent_summary()
print(f"空闲: {summary['idle']}, 工作: {summary['working']}")
```

### 💾 会话管理

```python
from src.config import Config
from src.session import SessionManager
from src.workspace import WorkspaceManager

# 初始化
config = Config()
session_mgr = SessionManager(config)
ws_mgr = WorkspaceManager()

# 保存会话
session_mgr.save_session("我的会话", ws_mgr)

# 加载会话
session_mgr.load_session("我的会话", ws_mgr)

# 列出所有会话
sessions = session_mgr.list_sessions()
for name in sessions:
    info = session_mgr.get_session_info(name)
    print(f"{name}: {info['workspace_count']} 个工作区")
```

---

## 🏗️ 项目架构

```
TermMux-CLI/
├── src/
│   ├── __init__.py      # 包初始化
│   ├── core.py          # 核心模块 (TermMux主控制器)
│   ├── workspace.py     # 工作区管理
│   ├── pane.py          # 窗格管理
│   ├── agent.py         # AI Agent检测
│   ├── config.py        # 配置管理
│   └── session.py       # 会话管理
├── tests/
│   ├── __init__.py
│   └── test_termmux.py  # 单元测试
├── docs/                # 文档目录
├── termmux-cli.py       # CLI入口
├── termmux.py           # 备用入口
├── setup.py             # 安装配置
├── requirements.txt     # 依赖清单
├── pytest.ini           # 测试配置
└── README.md            # 本文档
```

---

## 💡 设计思路与迭代规划

### 🎯 设计理念

1. **简洁至上** - 专注于核心功能，避免过度设计
2. **零依赖** - 核心功能零外部依赖，降低使用门槛
3. **模块化** - 各模块独立，便于维护和扩展
4. **用户友好** - 清晰的API设计，完善的错误提示

### 📋 技术选型

| 组件 | 选型 | 原因 |
|-----|-----|------|
| 语言 | Python 3.8+ | 生态丰富，易于扩展 |
| TUI | Rich | 现代化终端界面 |
| 进程 | psutil | 跨平台进程管理 |
| 测试 | pytest | 简洁高效的测试框架 |

### 🛣️ 迭代计划

- [ ] v1.1.0 - 支持更多AI Agent检测
- [ ] v1.2.0 - 添加窗格内命令执行
- [ ] v1.3.0 - 支持tmux后端
- [ ] v2.0.0 - 添加远程SSH会话支持
- [ ] v2.1.0 - 多用户/团队协作功能

### 🤝 贡献方向

欢迎提交PR或Issue！贡献方向包括：
- 🐛 Bug修复
- ✨ 新功能开发
- 📚 文档完善
- 🌍 多语言翻译
- 🎨 界面优化

---

## 📦 打包与部署

### 🐍 Python打包

```bash
# 构建wheel包
python -m build

# 安装本地包
pip install dist/termmux_cli-*.whl
```

### 🐳 Docker部署

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "termmux-cli.py"]
```

---

## 🤝 贡献指南

### 🔀 分支管理

- `main` - 主分支，稳定版本
- `develop` - 开发分支
- `feature/*` - 功能分支
- `fix/*` - 修复分支

### 📝 提交规范

使用 Angular 提交规范：

```
feat: 新增功能
fix: 修复问题
docs: 文档更新
refactor: 代码重构
test: 测试相关
chore: 构建/工具相关
```

### 🧪 测试要求

```bash
# 运行所有测试
pytest tests/ -v

# 带覆盖率报告
pytest tests/ --cov=src --cov-report=html
```

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 开源协议。

---

## 🙏 致谢

- 灵感来源：[herdr](https://github.com/ogulcancelik/herdr) - Rust实现的终端多路复用器
- TUI框架：[Rich](https://github.com/Textualize/rich) - 优秀的Python终端UI库
- 进程管理：[psutil](https://github.com/giampaolo/psutil) - 跨平台进程和系统监控库

---

## 📞 联系方式

- 🐛 Issue: [GitHub Issues](https://github.com/gitstq/TermMux-CLI/issues)
- 📧 Email: gitstq@example.com
- 🌐 GitHub: [https://github.com/gitstq](https://github.com/gitstq)

---

<div align="center">

**如果这个项目对您有帮助，请 ⭐ Star 支持！**

Made with ❤️ by [gitstq](https://github.com/gitstq)

</div>
