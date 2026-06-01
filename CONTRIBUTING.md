# 🤝 貢献ガイドライン

TermMux-CLI への貢献を歓迎します！

## 🔀 ブランチ戦略

- `main` - 安定版リリース
- `develop` - 開発ブランチ
- `feature/*` - 新機能ブランチ
- `fix/*` - バグ修正ブランチ

## 📝 コミット規約

Angular コミット規約に従ってください：

```
feat: 新機能追加
fix: バグ修正
docs: ドキュメント更新
refactor: リファクタリング
test: テスト関連
chore: ビルド/ツール関連
```

## 🧪 テスト

```bash
# 全テスト実行
pytest tests/ -v

# カバレッジ付き
pytest tests/ --cov=src --cov-report=html
```

## 🔍 コード品質

```bash
# フォーマット
black src/ tests/

# リント
flake8 src/ --max-line-length=120

# 型チェック
mypy src/
```

## 🚀 Pull Request 手順

1. フォークを作成
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'feat: add amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. Pull Request を開く

## 📋 Issue の提出

バグ報告や機能リクエストは [GitHub Issues](https://github.com/gitstq/TermMux-CLI/issues) からお気軽にどうぞ！
