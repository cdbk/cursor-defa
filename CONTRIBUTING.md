# Contributing to Cursor Rules - DEF-A統合最適化版

## 🎯 はじめに

Cursor Rules - DEF-A統合最適化版への貢献をありがとうございます。このプロジェクトは、DEF-AモデルをCursorルールに統合し、効率性と品質の最適バランスを実現することを目指しています。

## 📁 プロジェクト構成

### ファイル構成
```
cursor_user_rules/
├── rules/
│   ├── simple/                     # シンプル版（初心者・個人開発向け）
│   │   ├── core_rules.cursorrules      # 基本品質基準・シンプル版 (71行)
│   │   ├── rule_selector.cursorrules   # 質問分析・ルール選択 (259行)
│   │   ├── frontend_rules.cursorrules  # フロントエンド開発専用ルール (82行)
│   │   ├── backend_rules.cursorrules   # バックエンド開発専用ルール (98行)
│   │   ├── testing_rules.cursorrules   # テスト・品質保証専用ルール (191行)
│   │   └── knowledge_management_rules.cursorrules # 知識管理・学習支援 (新規)
│   └── defa/                       # DEF-A統合版（上級者・チーム開発向け）
│       ├── core_rules.cursorrules      # 基本品質基準・DEF-A統合フレームワーク (156行)
│       ├── rule_selector.cursorrules   # 質問分析・ルール選択システム (190行)
│       ├── defa_framework.cursorrules  # DEF-Aモデル詳細・段階別ガイドライン (185行)
│       ├── prompt_templates.cursorrules # プロンプトテンプレート・基本構造 (145行)
│       ├── frontend_rules.cursorrules  # フロントエンド開発専用ルール (82行)
│       ├── backend_rules.cursorrules   # バックエンド開発専用ルール (98行)
│       ├── testing_rules.cursorrules   # テスト・品質保証専用ルール (191行)
│       ├── error_handling_rules.cursorrules # エラー処理統合・多層防御戦略 (335行)
│       ├── team_collaboration_rules.cursorrules # チーム協働・知識共有・学習促進 (372行)
│       └── knowledge_management_rules.cursorrules # SECIモデル統合・暗黙知自動ルール化 (新規)
├── archive_rules/                  # アーカイブされたルール
├── examples/                       # 使用例・サンプル
├── README.md                       # プロジェクト概要・クイックスタート
├── DEF-A_INTEGRATION_GUIDE.md      # DEF-A統合詳細ガイド・実践的活用
├── CONTRIBUTING.md                 # このファイル
├── CODE_OF_CONDUCT.md             # 行動規範
├── LICENSE                         # MITライセンス
└── setup-cursor-rules.sh          # セットアップスクリプト
```

## 🔄 開発フロー

### 1. Issue作成
- **バグ報告**: 具体的な問題と再現手順を記載
- **機能要求**: 新機能の必要性と期待する動作を説明
- **改善提案**: 既存機能の改善案を提案

### 2. ブランチ作成
```bash
# メインブランチから新しいブランチを作成
git checkout -b feature/your-feature-name
# または
git checkout -b fix/your-bug-fix
```

### 3. 開発・テスト
- ルールファイルの変更は必ずテスト
- 既存の機能に影響がないことを確認
- ドキュメントの更新も忘れずに

### 4. プルリクエスト作成
- 変更内容の詳細な説明
- テスト結果の報告
- 関連するIssueへのリンク

## 📋 開発ガイドライン

### ルールファイル作成・編集

#### 基本原則
- **可読性**: 明確な変数名、適切なコメント
- **保守性**: 将来の変更に耐える設計
- **効率性**: 応答速度と品質の最適バランス

#### DEF-A統合原則（DEF-A統合版のみ）
- **部分適用戦略**: 質問内容に応じた適切なDEF-A段階選択
- **認知負荷管理**: 緊急度・複雑性に応じた応答最適化
- **品質基準**: 三方よし・丁度いい・持続可能性の原則

#### シンプル版原則
- **直感的理解**: 複雑な概念を排除した分かりやすい構成
- **実用性重視**: 即座に活用できる実践的な内容
- **段階的学習**: 基礎から応用への自然な移行

#### ファイル構造
```markdown
# Cursor Rules - [ファイル名] (DEF-A統合最適化版)
# Copyright (c) 2025 Kentaro Kitagawa
# MIT License - https://opensource.org/licenses/MIT

## [SECTION] セクション名

### サブセクション
- **重要項目**: 説明
- **適用場面**: 使用場面の説明

### コード例
```typescript
// 実装例
```

## [REFERENCE] 詳細参照
- **関連ファイル**: 参照先ファイル名
```

### ドキュメント作成・編集

#### README.md
- プロジェクト概要
- セットアップ手順
- 使用方法
- 技術スタック
- 効果測定指標

#### DEF-A_INTEGRATION_GUIDE.md
- DEF-Aモデルの詳細説明・実践的活用戦略
- 適用戦略の具体例・プロンプトテンプレート
- 高度な使用方法・最適化テクニック
- シンプル版からDEF-A統合版への移行ガイド

## 🧪 テスト

### ルールファイルテスト
1. **構文チェック**: ルールファイルの構文エラーがないことを確認
2. **機能テスト**: 実際のCursorで動作確認
3. **統合テスト**: 他のルールファイルとの連携確認

### ドキュメントテスト
1. **リンクチェック**: 内部リンク・外部リンクの動作確認
2. **内容確認**: 技術的精度・説明の分かりやすさ
3. **一貫性確認**: 他のドキュメントとの整合性

## 📝 コミットメッセージ

### 形式
```
[type] 簡潔な説明

詳細な説明（必要に応じて）

関連Issue: #123
```

### タイプ
- `feat`: 新機能
- `fix`: バグ修正
- `docs`: ドキュメント更新
- `style`: コードスタイル修正
- `refactor`: リファクタリング
- `test`: テスト追加・修正
- `chore`: その他の変更

### 例
```
[feat] DEF-A部分適用戦略の追加

- 完全適用・部分適用・最小適用の3パターンを実装
- 認知負荷管理による効率性最適化
- 質問分析による自動段階選択

関連Issue: #45
```

## 🤝 レビュープロセス

### プルリクエストレビュー
1. **コードレビュー**: 技術的精度・品質の確認
2. **ドキュメントレビュー**: 説明の分かりやすさ・正確性
3. **統合テスト**: 全体への影響確認

### レビュー基準
- **機能性**: 要求仕様の満足
- **品質**: コード・ドキュメントの品質
- **保守性**: 将来の変更への対応
- **一貫性**: プロジェクト全体との整合性

## 📄 ライセンス

このプロジェクトはMITライセンスの下で公開されています。貢献するコードもMITライセンスの下で公開されることに同意してください。

---

**Thank you for contributing to Cursor Rules - DEF-A統合最適化版!** 🚀 