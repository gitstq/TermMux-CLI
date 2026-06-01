# 🌍 Language Switcher | 语言切换

[![简体中文](https://img.shields.io/badge/简体中文-✓-green?style=for-the-badge)](README.md)
[![English](https://img.shields.io/badge/English-✓-blue?style=for-the-badge)](README_en.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-✓-orange?style=for-the-badge)](README_zh_TW.md)
[![日本語](https://img.shields.io/badge/日本語-✓-pink?style=for-the-badge)](README_ja.md)

---

# 🎛️ TermMux-CLI

> **Lightweight Terminal Multiplexer with AI Agent Awareness**
> **轻量级终端多路复用与AI Agent感知管理器**

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-yellow.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-cyan.svg)](https://github.com/gitstq/TermMux-CLI)
[![Stars](https://img.shields.io/github/stars/gitstq/TermMux-CLI?style=social)](https://github.com/gitstq/TermMux-CLI)

---

## 🎉 Introduction

**TermMux-CLI** is a lightweight terminal multiplexer designed for developers, inspired by [herdr](https://github.com/ogulcancelik/herdr), but implemented in **Python** for easier installation and extensibility.

### ✨ Core Values

- 🔧 **Workspace Management** - Create, switch, rename, and close workspaces easily
- 🪟 **Pane Management** - Horizontal/vertical splitting with flexible layouts
- 🤖 **AI Agent Awareness** - Real-time detection and status display for Claude Code, Cursor, etc.
- 💾 **Session Persistence** - Save and restore workspace layouts
- 🎨 **Modern TUI** - Beautiful terminal interface built with Rich library
- ⚡ **Zero Core Dependencies** - Only requires Rich and psutil, ready to use

### 💡 Inspiration

This project is inspired by [herdr](https://github.com/ogulcancelik/herdr), an excellent terminal multiplexer written in Rust. TermMux-CLI uses Python to:
- Lower installation barriers (`pip install termmux-cli`)
- Make customization and extension easier
- Provide familiar development experience for Python developers

---

## ✨ Key Features

### 🏠 Workspace Management
- 📁 Multi-workspace support with independent management
- 🔄 Workspace switching, renaming, deletion
- 📊 Clear workspace status overview

### 🪟 Pane Management
- ➕ Create new panes
- ⏹️ Horizontal/vertical splitting
- ❌ Close panes
- 🔲 Pane focus switching

### 🤖 AI Agent Awareness
Automatically detects and displays status for:

| Agent | Status Detection | Indicators |
|-------|-----------------|------------|
| Claude Code | ✅ | 🟢🟡🔴🔵 |
| Cursor Agent | ✅ | 🟢🟡🔴🔵 |
| GitHub Copilot | ✅ | 🟢🟡🔴🔵 |
| OpenAI Codex | ✅ | 🟢🟡🔴🔵 |
| Gemini CLI | ✅ | 🟢🟡🔴🔵 |
| Kiro CLI | ✅ | 🟢🟡🔴🔵 |

**Agent Status Legend:**
- 🟢 **Idle** - Agent ready, waiting for input
- 🟡 **Working** - Agent executing tasks
- 🔴 **Blocked** - Agent waiting for user confirmation or input
- 🔵 **Done** - Task completed

### 💾 Session Management
- 💾 One-click save of current workspace layout
- 📂 Load historical sessions
- 🗑️ Delete unused sessions
- 📋 Session list management

---

## 🚀 Quick Start

### 📋 Requirements

- Python 3.8 or higher
- Linux / macOS / Windows

### 🔧 Installation

#### Method 1: pip install (Recommended)

```bash
pip install termmux-cli
```

#### Method 2: From Source

```bash
# Clone repository
git clone https://github.com/gitstq/TermMux-CLI.git
cd TermMux-CLI

# Install dependencies
pip install -r requirements.txt

# Run
python termmux-cli.py
```

### 🎮 Usage

```bash
# Start interactive mode
termmux

# Or
python termmux-cli.py
```

### ⌨️ Keybindings

| Key | Action |
|-----|--------|
| `n` | New workspace |
| `s` | Save current session |
| `l` | Load historical session |
| `r` | Refresh AI Agent detection |
| `q` | Quit program |

---

## 📖 Detailed Usage Guide

### 🏠 Workspace Operations

```python
from src.workspace import Workspace, WorkspaceManager

# Create workspace manager
manager = WorkspaceManager()

# Create new workspace
ws = manager.create_workspace("My Project")

# Switch workspace
manager.switch_workspace(0)

# Rename workspace
manager.rename_workspace(ws.id, "New Name")

# Delete workspace
manager.delete_workspace(ws.id)
```

### 🪟 Pane Operations

```python
from src.pane import Pane, PaneManager, SplitDirection

# Create pane manager
manager = PaneManager()

# Create pane
pane = manager.create_pane(
    title="Terminal",
    command="bash",
    working_directory="/home/user"
)

# Split pane
new_pane = manager.split_pane(pane.id, SplitDirection.HORIZONTAL)

# Close pane
manager.close_pane(pane.id)
```

### 🤖 Agent Detection

```python
from src.agent import AgentDetector, AgentStatus

# Create detector
detector = AgentDetector()

# Scan running agents
detector.scan()

# Get detection results
agents = detector.get_detected_agents()

# Filter by status
working_agents = detector.get_agents_by_status(AgentStatus.WORKING)

# Get status summary
summary = detector.get_agent_summary()
print(f"Idle: {summary['idle']}, Working: {summary['working']}")
```

### 💾 Session Management

```python
from src.config import Config
from src.session import SessionManager
from src.workspace import WorkspaceManager

# Initialize
config = Config()
session_mgr = SessionManager(config)
ws_mgr = WorkspaceManager()

# Save session
session_mgr.save_session("My Session", ws_mgr)

# Load session
session_mgr.load_session("My Session", ws_mgr)

# List all sessions
sessions = session_mgr.list_sessions()
for name in sessions:
    info = session_mgr.get_session_info(name)
    print(f"{name}: {info['workspace_count']} workspaces")
```

---

## 🏗️ Project Architecture

```
TermMux-CLI/
├── src/
│   ├── __init__.py      # Package initialization
│   ├── core.py          # Core module (TermMux main controller)
│   ├── workspace.py     # Workspace management
│   ├── pane.py          # Pane management
│   ├── agent.py         # AI Agent detection
│   ├── config.py        # Configuration management
│   └── session.py       # Session management
├── tests/
│   ├── __init__.py
│   └── test_termmux.py  # Unit tests
├── docs/                # Documentation directory
├── termmux-cli.py       # CLI entry point
├── termmux.py           # Alternative entry
├── setup.py             # Installation configuration
├── requirements.txt     # Dependencies
├── pytest.ini           # Test configuration
└── README_en.md         # English documentation
```

---

## 💡 Design Philosophy & Roadmap

### 🎯 Design Philosophy

1. **Simplicity First** - Focus on core features, avoid overdesign
2. **Zero Dependencies** - Core functions have zero external dependencies
3. **Modularity** - Independent modules for easy maintenance and extension
4. **User-Friendly** - Clear API design with comprehensive error messages

### 📋 Tech Stack

| Component | Choice | Reason |
|-----------|--------|--------|
| Language | Python 3.8+ | Rich ecosystem, easy to extend |
| TUI | Rich | Modern terminal UI library |
| Process | psutil | Cross-platform process management |
| Testing | pytest | Simple and efficient testing framework |

### 🛣️ Roadmap

- [ ] v1.1.0 - Support more AI Agent detection
- [ ] v1.2.0 - Add in-pane command execution
- [ ] v1.3.0 - Support tmux backend
- [ ] v2.0.0 - Add remote SSH session support
- [ ] v2.1.0 - Multi-user/team collaboration features

### 🤝 Contribution Areas

PRs and Issues are welcome! Contribution areas include:
- 🐛 Bug fixes
- ✨ New feature development
- 📚 Documentation improvement
- 🌍 Multi-language translation
- 🎨 UI optimization

---

## 📦 Packaging & Deployment

### 🐍 Python Packaging

```bash
# Build wheel package
python -m build

# Install local package
pip install dist/termmux_cli-*.whl
```

### 🐳 Docker Deployment

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "termmux-cli.py"]
```

---

## 🤝 Contributing

### 🔀 Branch Management

- `main` - Main branch, stable version
- `develop` - Development branch
- `feature/*` - Feature branches
- `fix/*` - Fix branches

### 📝 Commit Convention

Using Angular commit convention:

```
feat: Add new feature
fix: Fix bug
docs: Documentation updates
refactor: Code refactoring
test: Test related
chore: Build/tool related
```

### 🧪 Testing Requirements

```bash
# Run all tests
pytest tests/ -v

# With coverage report
pytest tests/ --cov=src --cov-report=html
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Inspiration: [herdr](https://github.com/ogulcancelik/herdr) - Rust terminal multiplexer
- TUI Framework: [Rich](https://github.com/Textualize/rich) - Python terminal UI library
- Process Management: [psutil](https://github.com/giampaolo/psutil) - Cross-platform process monitoring

---

## 📞 Contact

- 🐛 Issue: [GitHub Issues](https://github.com/gitstq/TermMux-CLI/issues)
- 📧 Email: gitstq@example.com
- 🌐 GitHub: [https://github.com/gitstq](https://github.com/gitstq)

---

<div align="center">

**If this project helps you, please ⭐ Star to show your support!**

Made with ❤️ by [gitstq](https://github.com/gitstq)

</div>
