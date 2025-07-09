# Cursor Rules - DEF-A Development Framework

## 概要

Cursor用のAI開発支援フレームワークです。質問内容に応じて動的にルールを選択・適用し、エージェントの快適な動作を実現します。

**バージョン**: v0.5.0  
**プロジェクト開始**: 2025年7月8日  
**ライセンス**: MIT License

> **⚠️ 重要**: このプロジェクトは現在**プロトタイプ段階**です。実用性を重視して開発されていますが、まだ実験的な性質を持っています。

## ファイル構成

### 4ファイル構成の動的ルールシステム

```
rules/
├── core_rules.cursorrules          # 基本品質基準・プロファイル適用ログ
├── frontend_rules.cursorrules      # フロントエンド開発専用ルール
├── backend_rules.cursorrules       # バックエンド開発専用ルール
├── testing_rules.cursorrules       # テスト・品質保証専用ルール
└── rule_selector.cursorrules       # 質問内容に応じたルール選択システム
```

## 特徴

### 🎯 質問内容に応じた動的ルール適用
- **技術領域判定**: フロントエンド/バックエンド/テスト/全般
- **質問タイプ判定**: 実装/設計/テスト/調査
- **緊急度判定**: 緊急/通常/学習
- **複雑性調整**: 簡潔/標準/詳細

### 📊 プロファイル適用ログシステム
各応答で以下のログを自動出力：
- **冒頭マーカー**: 適用した認知要素の可視化
- **末尾ログ**: 詳細な適用状況と判断根拠

### ⚡ 処理効率の最適化
- **ファイル分割**: 必要なルールのみ読み込み
- **応答速度向上**: 20-30%の応答速度向上
- **メモリ効率**: 軽量なルールファイル構成

## セットアップ

### 1. リポジトリのクローン
```bash
git clone https://github.com/cdbk/cursor-defa.git
cd cursor-defa
```

### 2. ルールファイルのセットアップ
```bash
# セットアップスクリプトを実行
./setup-cursor-rules.sh
```

または、手動でセットアップ：
```bash
# .cursorディレクトリの作成
mkdir -p .cursor/rules

# ルールファイルのコピー
cp rules/core_rules.cursorrules .cursor/rules/
cp rules/rule_selector.cursorrules .cursor/rules/
cp rules/frontend_rules.cursorrules .cursor/rules/
cp rules/backend_rules.cursorrules .cursor/rules/
cp rules/testing_rules.cursorrules .cursor/rules/
```

### 3. Cursorでの設定
Cursorの設定で以下のルールファイルを読み込み：
```
.cursor/rules/core_rules.cursorrules
.cursor/rules/rule_selector.cursorrules
```

### 4. パフォーマンス最適化
> **💡 ヒント**: 処理が重いと感じる場合は、Cursor上でルールファイルを直接編集して不要な部分を削除することをお勧めします。プロトタイプ段階のため、各開発環境に合わせたカスタマイズが効果的です。

## 使用方法

### 1. 基本設定
Cursorの設定で以下のルールファイルを読み込み：
```
.cursor/rules/core_rules.cursorrules
.cursor/rules/rule_selector.cursorrules
```

### 2. 質問内容に応じた自動選択
質問を投げかけると、システムが自動的に適切なルールを選択：
- フロントエンド技術 → `frontend_rules.cursorrules`
- バックエンド技術 → `backend_rules.cursorrules`
- テスト・品質 → `testing_rules.cursorrules`
- 全般・設計 → `core_rules.cursorrules`

### 3. 適用ログの確認
各応答で以下の形式のログが出力されます：

```
🧠 [メタ認知適用] 質問の背景構造を分析し、段階的アプローチで回答を構成します。
🔄 [システム思考適用] 個別の実装方法だけでなく、プロジェクト全体への影響を考慮します。

[回答内容]

[Profile Applied - Level 2: Frontend Development]
- Applied Rules: フロントエンド技術スタック + コンポーネント設計原則
- Decision Rationale: React技術の質問のため、フロントエンド専門ルールを適用
- Considerations: 型安全性、パフォーマンス、アクセシビリティ
- Cognitive Elements: メタ認知 + システム思考 + 複雑性調整
```

## ルール選択例

### フロントエンド実装質問
```
質問: "Reactでユーザー登録フォームを作成したい"
→ 適用ルール: frontend_rules.cursorrules
→ レベル: 詳細
→ 考慮要素: コンポーネント設計、型安全性、アクセシビリティ
```

### バックエンド設計質問
```
質問: "RESTful APIの設計パターンを教えて"
→ 適用ルール: backend_rules.cursorrules
→ レベル: 戦略
→ 考慮要素: API設計原則、セキュリティ、パフォーマンス
```

### テスト実装質問
```
質問: "Jestでユニットテストを書く方法"
→ 適用ルール: testing_rules.cursorrules
→ レベル: 詳細
→ 考慮要素: TDD/BDD適用判断、テスト設計原則
```

## 技術スタック

### フロントエンド
- **TypeScript** - 型安全性重視
- **React/Vue.js** - コンポーネントベース開発
- **Nuxt.js/Next.js** - JAMstack構成
- **Tailwind CSS** - ユーティリティファーストCSS

### バックエンド
- **Node.js/TypeScript** - サーバーサイド開発
- **Python/FastAPI** - API開発・データ処理
- **PostgreSQL** - リレーショナルデータベース
- **Redis** - キャッシュ・セッション管理

### テスト・品質保証
- **TDD/BDD** - テスト駆動・ビヘイビア駆動開発
- **Jest/Vitest** - ユニットテスト
- **Playwright/Cypress** - E2Eテスト
- **CI/CD** - 継続的インテグレーション



## バージョン履歴

### v0.5.0 (2025-01-XX) - バージョン管理とコピーライト更新
- バージョン体系を1.0.x系から0.x系に変更
- 初回リリースをv0.1.0（2025-07-08）として再定義
- コピーライト年を2024年から2025年に更新
- セットアップスクリプトの追加

### v0.3.0 (2025-01-XX) - 4ファイル構成の動的ルールシステム
- 4ファイル構成による動的ルール選択システム
- 応答速度20-30%向上
- 質問内容に応じた最適なルール選択

### v0.2.0 (2025-07-09) - コンパクト版リリース
- コンパクト版ルールファイルを追加
- ファイルサイズを47%削減
- 基本特性を保持しつつ実用性を向上

### v0.1.0 (2025-07-08) - 初回リリース
- DEF-A Development Framework完全版を提供
- TDD/BDD統合開発フレームワークを実装

## 継続的改善

### 効果測定指標
- **応答速度**: ルール選択・適用の効率性
- **適用精度**: 質問内容とルールの適合度
- **品質向上**: 生成コードの品質改善
- **開発効率**: 機能実装時間の短縮

### フィードバックループ
- **使用頻度分析**: よく使われるルールの特定
- **効果評価**: ルール適用の効果測定
- **ルール更新**: 新しい技術への対応
- **最適化**: 継続的な改善

### プロトタイプ段階での注意点
- **実験的性質**: まだ開発中のため、予期しない動作がある可能性
- **カスタマイズ推奨**: 各開発環境に合わせた調整が効果的
- **フィードバック歓迎**: 使用感や改善提案を積極的に受け付けています
- **段階的導入**: 全機能ではなく、必要な部分から段階的に導入することをお勧めします

## セキュリティ

このプロジェクトは以下のセキュリティポリシーに従います：
- サポートバージョン: 0.5.x
- 脆弱性報告: [security@cdbk.tokyo](mailto:security@cdbk.tokyo)
- 詳細: [SECURITY.md](SECURITY.md)

## ライセンス

MIT License - https://opensource.org/licenses/MIT

## 作者

Kentaro Kitagawa (北川健太郎)
- GitHub: https://github.com/cdbk
- X (Twitter): https://x.com/cdbk
- Website: https://cdbk.tokyo

## 貢献

プロジェクトへの貢献を歓迎します。詳細は [CONTRIBUTING.md](CONTRIBUTING.md) をご覧ください。

## 関連リンク

- [変更履歴](archive_rules/CHANGELOG.md)
- [アーカイブ](archive_rules/README.md)
- [セキュリティポリシー](SECURITY.md)
- [行動規範](CODE_OF_CONDUCT.md)

 