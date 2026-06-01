# 🌍 語言切換 | Language Switcher

[![簡體中文](https://img.shields.io/badge/簡體中文-✓-green?style=for-the-badge)](README.md)
[![English](https://img.shields.io/badge/English-✓-blue?style=for-the-badge)](README_en.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-✓-orange?style=for-the-badge)](README_zh_TW.md)
[![日本語](https://img.shields.io/badge/日本語-✓-pink?style=for-the-badge)](README_ja.md)

---

# 🎛️ TermMux-CLI

> **輕量級終端多路復用與AI Agent感知管理器**
> **Lightweight Terminal Multiplexer with AI Agent Awareness**

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-yellow.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-cyan.svg)](https://github.com/gitstq/TermMux-CLI)
[![Stars](https://img.shields.io/github/stars/gitstq/TermMux-CLI?style=social)](https://github.com/gitstq/TermMux-CLI)

---

## 🎉 專案介紹

**TermMux-CLI** 是一款專為開發者設計的**輕量級終端多路復用器**，靈感來源於 [herdr](https://github.com/ogulcancelik/herdr)，但使用 **Python** 實現，更易於安裝和擴展。

### ✨ 核心價值

- 🔧 **工作區管理** - 輕鬆建立、切換、重新命名、關閉工作區
- 🪟 **窗格管理** - 水平/垂直分屏，靈活佈局
- 🤖 **AI Agent感知** - 即時檢測並顯示Claude Code、Cursor等Agent的狀態
- 💾 **會話持久化** - 儲存和恢復工作區佈局，永不丟失
- 🎨 **現代化TUI** - 基於Rich庫構建的精美終端介面
- ⚡ **零核心依賴** - 僅依賴 Rich 和 psutil，開箱即用

### 💡 靈感來源

本專案靈感來源於 [herdr](https://github.com/ogulcancelik/herdr)，一款用 Rust 編寫的優秀終端多路復用器。TermMux-CLI 採用 Python 實現，目標是：
- 降低安裝門檻 (`pip install termmux-cli`)
- 更易於定制和擴展
- 為 Python 開發者提供熟悉的開發體驗

---

## ✨ 核心功能

### 🏠 工作區管理
- 📁 多工作區支援，每個工作區獨立管理
- 🔄 工作區切換、重新命名、刪除
- 📊 工作區狀態一目了然

### 🪟 窗格管理
- ➕ 建立新窗格
- ⏹️ 水平/垂直分屏
- ❌ 關閉窗格
- 🔲 窗格聚焦切換

### 🤖 AI Agent感知
支援自動檢測以下AI Agent的運行狀態：

| Agent | 狀態檢測 | 狀態指示 |
|-------|---------|---------|
| Claude Code | ✅ | 🟢🟡🔴🔵 |
| Cursor Agent | ✅ | 🟢🟡🔴🔵 |
| GitHub Copilot | ✅ | 🟢🟡🔴🔵 |
| OpenAI Codex | ✅ | 🟢🟡🔴🔵 |
| Gemini CLI | ✅ | 🟢🟡🔴🔵 |
| Kiro CLI | ✅ | 🟢🟡🔴🔵 |

**Agent狀態說明：**
- 🟢 **空閒 (Idle)** - Agent已就緒，等待輸入
- 🟡 **工作中 (Working)** - Agent正在執行任務
- 🔴 **阻塞 (Blocked)** - Agent等待用戶確認或輸入
- 🔵 **完成 (Done)** - 任務已完成

### 💾 會話管理
- 💾 一鍵儲存當前工作區佈局
- 📂 載入歷史會話
- 🗑️ 刪除不再需要的會話
- 📋 會話列表管理

---

## 🚀 快速開始

### 📋 環境要求

- Python 3.8 或更高版本
- Linux / macOS / Windows

### 🔧 安裝

#### 方式一：pip 安裝 (推薦)

```bash
pip install termmux-cli
```

#### 方式二：從原始碼安裝

```bash
# 複製倉庫
git clone https://github.com/gitstq/TermMux-CLI.git
cd TermMux-CLI

# 安裝依賴
pip install -r requirements.txt

# 運行
python termmux-cli.py
```

### 🎮 使用方法

```bash
# 啟動互動模式
termmux

# 或者
python termmux-cli.py
```

### ⌨️ 快捷鍵

| 按鍵 | 功能 |
|-----|------|
| `n` | 新建工作區 |
| `s` | 儲存當前會話 |
| `l` | 載入歷史會話 |
| `r` | 重新整理AI Agent檢測 |
| `q` | 退出程式 |

---

## 📖 詳細使用指南

### 🏠 工作區操作

```python
from src.workspace import Workspace, WorkspaceManager

# 建立工作區管理器
manager = WorkspaceManager()

# 建立新工作區
ws = manager.create_workspace("我的專案")

# 切換工作區
manager.switch_workspace(0)

# 重新命名工作區
manager.rename_workspace(ws.id, "新名稱")

# 刪除工作區
manager.delete_workspace(ws.id)
```

### 🪟 窗格操作

```python
from src.pane import Pane, PaneManager, SplitDirection

# 建立窗格管理器
manager = PaneManager()

# 建立窗格
pane = manager.create_pane(
    title="終端",
    command="bash",
    working_directory="/home/user"
)

# 分割窗格
new_pane = manager.split_pane(pane.id, SplitDirection.HORIZONTAL)

# 關閉窗格
manager.close_pane(pane.id)
```

### 🤖 Agent檢測

```python
from src.agent import AgentDetector, AgentStatus

# 建立檢測器
detector = AgentDetector()

# 掃描運行中的Agent
detector.scan()

# 取得檢測結果
agents = detector.get_detected_agents()

# 按狀態篩選
working_agents = detector.get_agents_by_status(AgentStatus.WORKING)

# 取得狀態摘要
summary = detector.get_agent_summary()
print(f"空閒: {summary['idle']}, 工作: {summary['working']}")
```

### 💾 會話管理

```python
from src.config import Config
from src.session import SessionManager
from src.workspace import WorkspaceManager

# 初始化
config = Config()
session_mgr = SessionManager(config)
ws_mgr = WorkspaceManager()

# 儲存會話
session_mgr.save_session("我的會話", ws_mgr)

# 載入會話
session_mgr.load_session("我的會話", ws_mgr)

# 列出所有會話
sessions = session_mgr.list_sessions()
for name in sessions:
    info = session_mgr.get_session_info(name)
    print(f"{name}: {info['workspace_count']} 個工作區")
```

---

## 🏗️ 專案架構

```
TermMux-CLI/
├── src/
│   ├── __init__.py      # 套件初始化
│   ├── core.py          # 核心模組 (TermMux主控制器)
│   ├── workspace.py     # 工作區管理
│   ├── pane.py          # 窗格管理
│   ├── agent.py         # AI Agent檢測
│   ├── config.py        # 設定管理
│   └── session.py       # 會話管理
├── tests/
│   ├── __init__.py
│   └── test_termmux.py  # 單元測試
├── docs/                # 文件目錄
├── termmux-cli.py       # CLI入口
├── termmux.py           # 備用入口
├── setup.py             # 安裝設定
├── requirements.txt     # 依賴清單
├── pytest.ini           # 測試設定
└── README_zh_TW.md      # 繁體中文文件
```

---

## 💡 設計思路與迭代規劃

### 🎯 設計理念

1. **簡潔至上** - 專注於核心功能，避免過度設計
2. **零依賴** - 核心功能零外部依賴，降低使用門檻
3. **模組化** - 各模組獨立，便於維護和擴展
4. **用戶友好** - 清晰的API設計，完善的錯誤提示

### 📋 技術選型

| 組件 | 選型 | 原因 |
|-----|-----|------|
| 語言 | Python 3.8+ | 生態豐富，易於擴展 |
| TUI | Rich | 現代化終端介面 |
| 進程 | psutil | 跨平台進程管理 |
| 測試 | pytest | 簡潔高效的測試框架 |

### 🛣️ 迭代計劃

- [ ] v1.1.0 - 支援更多AI Agent檢測
- [ ] v1.2.0 - 新增窗格內命令執行
- [ ] v1.3.0 - 支援tmux後端
- [ ] v2.0.0 - 新增遠程SSH會話支援
- [ ] v2.1.0 - 多用戶/團隊協作功能

### 🤝 貢獻方向

歡迎提交PR或Issue！貢獻方向包括：
- 🐛 錯誤修復
- ✨ 新功能開發
- 📚 文件完善
- 🌍 多語言翻譯
- 🎨 介面優化

---

## 📦 打包與部署

### 🐍 Python打包

```bash
# 建構wheel包
python -m build

# 安裝本地包
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

## 🤝 貢獻指南

### 🔀 分支管理

- `main` - 主分支，穩定版本
- `develop` - 開發分支
- `feature/*` - 功能分支
- `fix/*` - 修復分支

### 📝 提交規範

使用 Angular 提交規範：

```
feat: 新增功能
fix: 修復問題
docs: 文件更新
refactor: 程式碼重構
test: 測試相關
chore: 建構/工具相關
```

### 🧪 測試要求

```bash
# 執行所有測試
pytest tests/ -v

# 帶覆蓋率報告
pytest tests/ --cov=src --cov-report=html
```

---

## 📄 開源協議

本專案採用 [MIT License](LICENSE) 開源協議。

---

## 🙏 致謝

- 靈感來源：[herdr](https://github.com/ogulcancelik/herdr) - Rust實現的終端多路復用器
- TUI框架：[Rich](https://github.com/Textualize/rich) - 優秀的Python終端UI庫
- 進程管理：[psutil](https://github.com/giampaolo/psutil) - 跨平台進程和系統監控庫

---

## 📞 聯繫方式

- 🐛 Issue: [GitHub Issues](https://github.com/gitstq/TermMux-CLI/issues)
- 📧 Email: gitstq@example.com
- 🌐 GitHub: [https://github.com/gitstq](https://github.com/gitstq)

---

<div align="center">

**如果這個專案對您有幫助，請 ⭐ Star 支持！**

Made with ❤️ by [gitstq](https://github.com/gitstq)

</div>
