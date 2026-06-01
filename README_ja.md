# 🌍 言語切り替え | Language Switcher

[![简体中文](https://img.shields.io/badge/简体中文-✓-green?style=for-the-badge)](README.md)
[![English](https://img.shields.io/badge/English-✓-blue?style=for-the-badge)](README_en.md)
[![繁體中文](https://img.shields.io/badge/繁體中文-✓-orange?style=for-the-badge)](README_zh_TW.md)
[![日本語](https://img.shields.io/badge/日本語-✓-pink?style=for-the-badge)](README_ja.md)

---

# 🎛️ TermMux-CLI

> **軽量級ターミナルマルチプレクサとAI Agent感知マネージャー**
> **Lightweight Terminal Multiplexer with AI Agent Awareness**

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-yellow.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20macOS%20%7C%20Windows-cyan.svg)](https://github.com/gitstq/TermMux-CLI)
[![Stars](https://img.shields.io/github/stars/gitstq/TermMux-CLI?style=social)](https://github.com/gitstq/TermMux-CLI)

---

## 🎉 プロジェクト紹介

**TermMux-CLI** は開発者向けの**軽量級ターミナルマルチプレクサ**です。[herdr](https://github.com/ogulcancelik/herdr) からインスピレーションを受け、**Python** で実装されているため、インストールと拡張が容易です。

### ✨ コアバリュー

- 🔧 **ワークスペース管理** - ワークスペースの作成、切替、名前変更、削除が簡単
- 🪟 **ペイン管理** - 水平/垂直分割、柔軟なレイアウト
- 🤖 **AI Agent感知** - Claude Code、CursorなどのAgentの状態をリアルタイム検出・表示
- 💾 **セッション永続化** - ワークスペースレイアウトの保存と復元
- 🎨 **モダンTUI** - Richライブラリで構築された美しいターミナルインターフェース
- ⚡ **ゼロコア依存** - Rich と psutil のみ依赖、開封即用

### 💡 インスピレーション

本プロジェクトは [herdr](https://github.com/ogulcancelik/herdr) からインスピレーションを受けています。Rustで書かれた優れたターミナルマルチプレクサです。TermMux-CLI は Python で実装し、以下を目的としています：
- インストール门槛の低下 (`pip install termmux-cli`)
- カスタマイズと拡張がより簡単に
- Python 開発者に馴染みのある開発体験を提供

---

## ✨ コア機能

### 🏠 ワークスペース管理
- 📁 マルチワークスペース対応、各ワークスペース独立管理
- 🔄 ワークスペース切替、名前変更、削除
- 📊 ワークスペース状態が一覧できる

### 🪟 ペイン管理
- ➕ 新規ペイン作成
- ⏹️ 水平/垂直分割
- ❌ ペイン閉じる
- 🔲 ペインフォーカス切替

### 🤖 AI Agent感知
以下のAI Agentの実行状態を自動検出：

| Agent | 状態検出 | 状態表示 |
|-------|---------|---------|
| Claude Code | ✅ | 🟢🟡🔴🔵 |
| Cursor Agent | ✅ | 🟢🟡🔴🔵 |
| GitHub Copilot | ✅ | 🟢🟡🔴🔵 |
| OpenAI Codex | ✅ | 🟢🟡🔴🔵 |
| Gemini CLI | ✅ | 🟢🟡🔴🔵 |
| Kiro CLI | ✅ | 🟢🟡🔴🔵 |

**Agent状態の説明：**
- 🟢 **アイドル (Idle)** - Agent準備完了、入力待ち
- 🟡 **作業中 (Working)** - Agentタスク実行中
- 🔴 **ブロック (Blocked)** - Agentユーザー確認・入力待ち
- 🔵 **完了 (Done)** - タスク完了

### 💾 セッション管理
- 💾 ワンクリックで現在のワークスペースレイアウト保存
- 📂 履歴セッション読込
- 🗑️ 不要なセッション削除
- 📋 セッションリスト管理

---

## 🚀 クイックスタート

### 📋 動作環境

- Python 3.8 以上
- Linux / macOS / Windows

### 🔧 インストール

#### 方法一：pip インストール (推奨)

```bash
pip install termmux-cli
```

#### 方法二：ソースからインストール

```bash
# リポジトリをクローン
git clone https://github.com/gitstq/TermMux-CLI.git
cd TermMux-CLI

# 依存関係をインストール
pip install -r requirements.txt

# 実行
python termmux-cli.py
```

### 🎮 使い方

```bash
# インタラクティブモードを開始
termmux

# または
python termmux-cli.py
```

### ⌨️ ショートカットキー

| キー | 機能 |
|-----|------|
| `n` | 新規ワークスペース |
| `s` | 現在のセッション保存 |
| `l` | 履歴セッション読込 |
| `r` | AI Agent検出を更新 |
| `q` | プログラム終了 |

---

## 📖 詳細使い方ガイド

### 🏠 ワークスペース操作

```python
from src.workspace import Workspace, WorkspaceManager

# ワークスペースマネージャーを作成
manager = WorkspaceManager()

# 新規ワークスペース作成
ws = manager.create_workspace("マイプロジェクト")

# ワークスペース切替
manager.switch_workspace(0)

# ワークスペース名前変更
manager.rename_workspace(ws.id, "新しい名前")

# ワークスペース削除
manager.delete_workspace(ws.id)
```

### 🪟 ペイン操作

```python
from src.pane import Pane, PaneManager, SplitDirection

# ペインマネージャーを作成
manager = PaneManager()

# ペイン作成
pane = manager.create_pane(
    title="ターミナル",
    command="bash",
    working_directory="/home/user"
)

# ペイン分割
new_pane = manager.split_pane(pane.id, SplitDirection.HORIZONTAL)

# ペイン閉じる
manager.close_pane(pane.id)
```

### 🤖 Agent検出

```python
from src.agent import AgentDetector, AgentStatus

# 検出器を作成
detector = AgentDetector()

# 実行中のAgentをスキャン
detector.scan()

# 検出結果を取得
agents = detector.get_detected_agents()

# 状態でフィルタ
working_agents = detector.get_agents_by_status(AgentStatus.WORKING)

# 状態サマリーを取得
summary = detector.get_agent_summary()
print(f"アイドル: {summary['idle']}, 作業中: {summary['working']}")
```

### 💾 セッション管理

```python
from src.config import Config
from src.session import SessionManager
from src.workspace import WorkspaceManager

# 初期化
config = Config()
session_mgr = SessionManager(config)
ws_mgr = WorkspaceManager()

# セッション保存
session_mgr.save_session("マイセッション", ws_mgr)

# セッション読込
session_mgr.load_session("マイセッション", ws_mgr)

# 全セッションをリスト
sessions = session_mgr.list_sessions()
for name in sessions:
    info = session_mgr.get_session_info(name)
    print(f"{name}: {info['workspace_count']} ワークスペース")
```

---

## 🏗️ プロジェクト構成

```
TermMux-CLI/
├── src/
│   ├── __init__.py      # パッケージ初期化
│   ├── core.py          # コアモジュール (TermMuxメインコントローラー)
│   ├── workspace.py     # ワークスペース管理
│   ├── pane.py          # ペイン管理
│   ├── agent.py         # AI Agent検出
│   ├── config.py        # 設定管理
│   └── session.py       # セッション管理
├── tests/
│   ├── __init__.py
│   └── test_termmux.py  # ユニットテスト
├── docs/                # ドキュメントディレクトリ
├── termmux-cli.py       # CLIエントリポイント
├── termmux.py           # 代替エントリ
├── setup.py             # インストール設定
├── requirements.txt     # 依存関係リスト
├── pytest.ini           # テスト設定
└── README_ja.md         # 日本語ドキュメント
```

---

## 💡 設計思路とロードマップ

### 🎯 設計理念

1. **シンプル至上** - コア機能に专注、過度な設計を避ける
2. **ゼロ依存** - コア機能は外部依存なし、使用门槛を低下
3. **モジュール化** - 各モジュール独立、メンテンスと拡張が容易
4. **ユーザーコットンリー** - 明確なAPI設計、完全なエラーメッセージ

### 📋 技術選定

| コンポーネント | 選定 | 理由 |
|-----------|--------|--------|
| 言語 | Python 3.8+ | エコシステム豊富、拡張容易 |
| TUI | Rich | モダンなターミナルUIライブラリ |
| プロセス | psutil | クロスプラットフォームプロセス管理 |
| テスト | pytest | シンプルで効率的なテストフレームワーク |

### 🛣️ ロードマップ

- [ ] v1.1.0 - より多くのAI Agent検出をサポート
- [ ] v1.2.0 - ペイン内コマンド実行を追加
- [ ] v1.3.0 - tmuxバックエンドをサポート
- [ ] v2.0.0 - リモートSSHセッションサポートを追加
- [ ] v2.1.0 - マルチユーザー/チームコラボレーション機能

### 🤝 コントリビューションの方向性

PRやIssueの提出を歓迎します！コントリビューションの方向性：
- 🐛 バグ修正
- ✨ 新機能開発
- 📚 ドキュメンテーション改善
- 🌍 多言語翻訳
- 🎨 UI最適化

---

## 📦 パッケージングとデプロイ

### 🐍 Pythonパッケージング

```bash
# wheelパッケージをビルド
python -m build

# ローカルパッケージをインストール
pip install dist/termmux_cli-*.whl
```

### 🐳 Dockerデプロイ

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "termmux-cli.py"]
```

---

## 🤝 コントリビューションガイド

### 🔀 ブランチ管理

- `main` - メインブランチ、安定バージョン
- `develop` - 開発ブランチ
- `feature/*` - フィーチャーブランチ
- `fix/*` - フィックスブランチ

### 📝 コミット規約

Angular コミット規約を使用：

```
feat: 新機能追加
fix: バグ修正
docs: ドキュメント更新
refactor: リファクタリング
test: テスト関連
chore: ビルド/ツール関連
```

### 🧪 テスト要件

```bash
# 全テストを実行
pytest tests/ -v

# カバレッジレポート付き
pytest tests/ --cov=src --cov-report=html
```

---

## 📄 オープンソースライセンス

本プロジェクトは [MIT License](LICENSE) でライセンスされています。

---

## 🙏 謝辞

- インスピレーション：[herdr](https://github.com/ogulcancelik/herdr) - Rustで書かれたターミナルマルチプレクサ
- TUIフレームワーク：[Rich](https://github.com/Textualize/rich) - 優れたPythonターミナルUIライブラリ
- プロセス管理：[psutil](https://github.com/giampaolo/psutil) - クロスプラットフォームプロセス＆システム監視ライブラリ

---

## 📞 連絡先

- 🐛 Issue: [GitHub Issues](https://github.com/gitstq/TermMux-CLI/issues)
- 📧 Email: gitstq@example.com
- 🌐 GitHub: [https://github.com/gitstq](https://github.com/gitstq)

---

<div align="center">

**このプロジェクトが役立った場合は、⭐ Star でサポートしてください！**

Made with ❤️ by [gitstq](https://github.com/gitstq)

</div>
