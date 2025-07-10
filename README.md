# Cursor Rules - DEF-A統合最適化版

## 🎯 概要

シンプル版とDEF-A統合版の2つのバージョンを提供するCursorルールセットです。DEF-Aモデルを統合し、効率的なAI協働を実現します。

### DEF-Aモデルとは
**DEF-Aモデル**は、AI時代における人間の思考を構造化し、複雑な課題を体系的に解決するための実践的フレームワークです。Define（定義）→Explore（探求）→Formulate（統合）→Act（実行）→Assess（評価）の5段階で、効率的な問題解決と価値創造を目指します。

### 🚀 段階的導入の推奨
1. **シンプル版**: `rules/simple/` フォルダ内のルールセット
2. **基本セット**: 基本ルールのみ（`core_rules.cursorrules`）
3. **拡張セット**: + 技術領域別ルール（フロントエンド/バックエンド/テスト）
4. **DEF-A統合版**: `rules/defa/` フォルダ内の完全なルールセット（チーム開発向け）

## 🚀 クイックスタート

### 自動セットアップ（推奨）
```bash
# リポジトリをクローン
git clone [repository-url]
cd cursor_user_rules

# セットアップスクリプトを実行
./setup-cursor-rules.sh
```

### 手動セットアップ

#### シンプル版セットアップ（初心者・個人開発向け）
```bash
# シンプル版ルールを配置
cp rules/simple/*.cursorrules ~/.cursor/rules/
```

```json
// .cursorrules
@core_rules.cursorrules
@rule_selector.cursorrules
@knowledge_management_rules.cursorrules
```

#### DEF-A統合版セットアップ（上級者・チーム開発向け）
```bash
# DEF-A統合版ルールファイル配置
cp rules/defa/*.cursorrules ~/.cursor/rules/
```

```json
// .cursorrules
@core_rules.cursorrules
@rule_selector.cursorrules
@defa_framework.cursorrules
@prompt_templates.cursorrules
@frontend_rules.cursorrules
@backend_rules.cursorrules
@testing_rules.cursorrules
@error_handling_rules.cursorrules
@team_collaboration_rules.cursorrules
@knowledge_management_rules.cursorrules
```

**詳細なセットアップ手順**: [DEF-A_INTEGRATION_GUIDE.md](DEF-A_INTEGRATION_GUIDE.md) を参照

## 📁 ファイル構成

### シンプル版
**`rules/simple/`** フォルダ内のルールセット
- **`core_rules.cursorrules`** (71行) - 基本品質基準・シンプル版
- **`rule_selector.cursorrules`** (259行) - 質問分析・ルール選択（シンプル版）
- **`frontend_rules.cursorrules`** (82行) - フロントエンド開発専用ルール
- **`backend_rules.cursorrules`** (98行) - バックエンド開発専用ルール
- **`testing_rules.cursorrules`** (191行) - テスト・品質保証専用ルール
- **`knowledge_management_rules.cursorrules`** (新規) - 知識管理・学習支援・暗黙知ルール化

**特徴**: DEF-Aモデル適用前の直感的で分かりやすい構成

### DEF-A統合版（上級者・チーム向け）
**`rules/defa/`** フォルダ内のルールセット

#### コアファイル（必須）
- **`core_rules.cursorrules`** (156行) - 基本品質基準・DEF-A統合フレームワーク
- **`rule_selector.cursorrules`** (190行) - 質問分析・ルール選択システム

#### 詳細ファイル（必要時参照）
- **`defa_framework.cursorrules`** (185行) - DEF-Aモデル詳細・段階別ガイドライン
- **`prompt_templates.cursorrules`** (145行) - プロンプトテンプレート・基本構造

#### 技術領域別ファイル
- **`frontend_rules.cursorrules`** (82行) - フロントエンド開発専用ルール
- **`backend_rules.cursorrules`** (98行) - バックエンド開発専用ルール
- **`testing_rules.cursorrules`** (191行) - テスト・品質保証専用ルール

#### 統合機能ファイル（新規追加）
- **`error_handling_rules.cursorrules`** (335行) - エラー処理統合・多層防御戦略
- **`team_collaboration_rules.cursorrules`** (372行) - チーム協働・知識共有・学習促進
- **`knowledge_management_rules.cursorrules`** (新規) - SECIモデル統合・暗黙知自動ルール化システム

## 💡 使用例

### シンプル版使用例（初心者・個人開発向け）
```markdown
# Cursor プロンプト - シンプル指示

## [REQUEST] 具体的要求
TypeScriptで型安全なAPIクライアントを実装したい

## [RULES] 適用ルール
- **品質基準**: 可読性・保守性重視
- **出力形式**: 実装コード + 簡単な説明
```

### DEF-A統合版使用例（上級者・チーム開発向け）
```markdown
# Cursor プロンプト - DEF-A統合指示

## [CONTEXT] 開発状況
- **プロジェクト**: 中規模Webアプリケーション
- **開発段階**: 機能実装
- **緊急度**: 通常
- **チーム規模**: 小規模

## [REQUEST] 具体的要求
TypeScriptで型安全なAPIクライアントを実装したい

## [DEF-A] 思考フロー指定
- **適用段階**: Formulate → Act → Assess
- **認知スタイル**: Systems思考重視
- **複雑性レベル**: 標準

## [RULES] 適用ルール
- **主要ルール**: frontend_rules.cursorrules
- **品質基準**: 三方よし
- **出力形式**: 実装コード + 使用例
```

**詳細な使用例・プロンプトテンプレート**: [DEF-A_INTEGRATION_GUIDE.md](DEF-A_INTEGRATION_GUIDE.md) を参照

## ⚠️ 重要: 複雑性について

このルールセットは**包括的で高度な機能**を提供しますが、**初心者には複雑すぎる可能性**があります。

**推奨使用シーン**:
- ✅ **初心者・個人開発**: シンプル版から開始
- ✅ **中級者以上**: 開発経験があり、体系的なアプローチを求める方
- ✅ **チーム開発**: 統一された品質基準とプロセスが必要な場合
- ✅ **大規模プロジェクト**: 包括的な開発ガイドラインが必要な場合

**注意が必要なシーン**:
- ⚠️ **緊急対応**: 複雑な分類よりも迅速な解決が必要な場合
- ⚠️ **学習初期**: まずは基本的なCursorの使い方に慣れることを推奨

## 🔄 DEF-A部分適用戦略

### 適用パターン
- **完全DEF-A適用**: 戦略的・複雑な課題（Define→Explore→Formulate→Act→Assess）
- **部分DEF-A適用**: 技術実装質問（Formulate→Act→Assess）
- **最小DEF-A適用**: 緊急対応（Actのみ）
- **学習支援適用**: 教育・理解（Explore→Act）

### プロジェクト特性別対応
- **スタートアップ**: 速度重視・MVP開発・最小適用中心
- **エンタープライズ**: 安定性重視・完全適用・包括的品質保証
- **保守・改善**: 既存システム安定性・Assess→Formulate→Act
- **学習・教育**: スキル向上・学習支援適用・段階的習得

### 認知スタイル
- **🧠 Systems Mode**: 戦略的システム思考型（構造化・論理的・全体最適化）
- **🌸 Empathy Mode**: 感情統合コミュニケーション型（段階的・実用的・感情共鳴）

## 📋 使用方法

### シンプル版使用フロー
1. **質問分析**: 技術領域・質問タイプの判定
2. **ルール選択**: 適切なルールファイルの選択
3. **実装**: 品質基準に基づく実装
4. **学習**: 知識管理・継続的改善

### DEF-A統合版使用フロー
1. **質問分析**: DEF-A段階・認知スタイルの判定
2. **ルール選択**: 技術領域に応じた適切なルールファイル選択
3. **部分適用**: 質問特性に応じたDEF-A段階の適用
4. **品質基準**: 三方よし・丁度いい・持続可能性の原則適用

**詳細な使用方法・プロンプトテンプレート**: [DEF-A_INTEGRATION_GUIDE.md](DEF-A_INTEGRATION_GUIDE.md) を参照

## 🛠 対応技術スタック

### フロントエンド
- **React/Vue/Angular**: モダンUIフレームワーク
- **TypeScript**: 型安全性・開発効率
- **レスポンシブデザイン**: モバイルファースト
- **アクセシビリティ**: WCAG 2.1準拠

### バックエンド
- **Node.js/Python/Java**: サーバーサイド技術
- **RESTful API**: 標準的なAPI設計
- **データベース**: PostgreSQL/MySQL/MongoDB
- **セキュリティ**: JWT認証・入力検証

### テスト・品質
- **TDD/BDD**: テスト駆動開発
- **Jest/Vitest**: テストフレームワーク
- **CI/CD**: 継続的インテグレーション
- **コードレビュー**: 品質保証プロセス

### 知識管理・学習
- **SECIモデル**: 暗黙知の形式知化・知識共有
- **自動ルール化**: プロジェクト固有知識の自動記録
- **継続的改善**: 学習効果・スキル向上の測定
- **チーム学習**: 知識共有・メンタリング・協働学習
- **日付管理**: システム日付の自動取得・検証による正確性確保

## 📈 効果測定指標

### 効率性指標
- **応答速度**: 質問分析から回答生成までの時間
- **認知負荷**: 使用するDEF-A段階数・複雑性レベル
- **部分適用率**: 完全適用 vs 部分適用の使用比率

### 品質指標
- **コード品質**: 可読性・保守性・セキュリティ
- **ユーザー満足度**: 回答の実用性・理解しやすさ
- **継続的使用**: ルールセットの継続的活用

### 学習効果指標
- **技術習得**: 段階的理解・実践能力向上
- **問題解決**: 複雑な課題への対応能力
- **チーム協働**: 知識共有・コミュニケーション改善

## 📊 最適化結果サマリー

### ファイルサイズ最適化
- **最適化前**: `core_rules.cursorrules` (467行) + `rule_selector.cursorrules` (716行) = 1,183行
- **最適化後**: 
  - `core_rules.cursorrules` (130行) - コンパクト版
  - `rule_selector.cursorrules` (180行) - 最適化版
  - `defa_framework.cursorrules` (185行) - 詳細版（新規分離）
  - `prompt_templates.cursorrules` (145行) - 最適化版（新規分離）
  - `error_handling_rules.cursorrules` (新規追加) - エラー処理統合
  - `team_collaboration_rules.cursorrules` (新規追加) - チーム協働統合
  - `knowledge_management_rules.cursorrules` (新規追加) - SECIモデル統合・暗黙知自動ルール化・日付管理システム
- **総行数**: 約900行（統合機能強化）
- **処理効率**: 階層的参照構造により応答速度向上
- **完成度**: 85% → 95%（新機能追加による大幅改善）

### 新機能追加（v0.7.0以降）
- **日付管理システム**: システム日付の自動取得・検証機能
  - 自動取得コマンド: `date +%Y-%m-%d`
  - 統一形式: YYYY-MM-DD
  - 使用場面: CHANGELOG、ファイル作成日、バージョン管理
  - 検証プロセス: 取得日付の確認・修正

### 最適化戦略
1. **ファイル分割**: 詳細内容を専用ファイルに分離
2. **コンパクト化**: 冗長な説明・例の削減
3. **階層的参照**: 必要に応じた段階的読み込み
4. **効率性重視**: 応答速度と品質の最適バランス
5. **詳細例分離**: 実用的な基本テンプレートと詳細例の分離

## 📚 参考資料

### DEF-Aモデル
- **Define**: 問題設定・多次元定義
- **Explore**: 多視点分析・深層探求
- **Formulate**: 統合・構造化・最適化
- **Act/Apply**: 実行・適用
- **Assess/Adjust**: 評価・調整

**参考仕様**: [DEF-Aモデル公式サイト](https://cdbk.tokyo/def) - 構造化思考フレームワークの詳細解説

### 品質原則
- **三方よし**: 開発者・ユーザー・システム全体の利益
- **丁度いい**: 過不足のない最適解
- **持続可能性**: 長期的な保守・拡張性

### 詳細例・参考資料
- **`examples/prompt_examples.md`** - 詳細プロンプト例集
- **`examples/rule_selector_examples.md`** - ルール選択詳細例集

## 🤝 貢献

### 開発ガイドライン
- **コード品質**: 可読性・保守性を重視
- **ドキュメント**: 包括的な説明・例の提供
- **テスト**: 品質保証・動作確認

### 貢献プロセス
1. **Issue作成**: 改善提案・バグ報告
2. **ブランチ作成**: 機能開発・修正
3. **プルリクエスト**: コードレビュー・マージ

## 📚 参考資料

### 詳細ガイド
- **[DEF-A_INTEGRATION_GUIDE.md](DEF-A_INTEGRATION_GUIDE.md)**: DEF-A統合の詳細説明・実践的活用戦略
- **[CONTRIBUTING.md](CONTRIBUTING.md)**: 開発・貢献ガイドライン
- **[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)**: コミュニティ行動規範

### 使用例・サンプル
- **`examples/prompt_examples.md`**: 詳細プロンプト例集
- **`examples/rule_selector_examples.md`**: ルール選択詳細例集

## 📄 ライセンス

MIT License - 詳細は[LICENSE](LICENSE)ファイルを参照


 