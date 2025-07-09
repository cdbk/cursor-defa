# Cursor Rules - DEF-A統合最適化版

## 📊 最適化結果サマリー

### ファイルサイズ最適化（2025年1月版）
- **最適化前**: `core_rules.cursorrules` (467行) + `rule_selector.cursorrules` (716行) = 1,183行
- **最適化後**: 
  - `core_rules.cursorrules` (130行) - コンパクト版
  - `rule_selector.cursorrules` (387行) - コンパクト版
  - `defa_framework.cursorrules` (185行) - 詳細版（新規分離）
  - `prompt_templates.cursorrules` (447行) - 詳細版（新規分離）
- **総行数**: 1,149行（3%削減）
- **処理効率**: 階層的参照構造により応答速度向上

### 最適化戦略
1. **ファイル分割**: 詳細内容を専用ファイルに分離
2. **コンパクト化**: 冗長な説明・例の削減
3. **階層的参照**: 必要に応じた段階的読み込み
4. **効率性重視**: 応答速度と品質の最適バランス

## 🎯 概要

DEF-AモデルをCursorルールに統合し、効率的なAI協働を実現する最適化版ルールセットです。

### 戦略的価値
- **部分適用戦略**: 質問内容に応じた適切なDEF-A段階選択
- **認知負荷管理**: 緊急度・複雑性に応じた応答最適化
- **知的生産性最大化**: 効率性と品質の最適バランス
- **継続的改善**: 使用状況に応じた段階的適用拡大

## 📁 ファイル構成

### コアファイル（コンパクト版）
- **`core_rules.cursorrules`** (130行) - 基本品質基準・DEF-A統合フレームワーク
- **`rule_selector.cursorrules`** (387行) - 質問分析・ルール選択システム

### 詳細ファイル（必要時参照）
- **`defa_framework.cursorrules`** (185行) - DEF-Aモデル詳細・段階別ガイドライン
- **`prompt_templates.cursorrules`** (447行) - プロンプトテンプレート・状況別例

### 技術領域別ファイル
- **`frontend_rules.cursorrules`** - フロントエンド開発専用ルール
- **`backend_rules.cursorrules`** - バックエンド開発専用ルール
- **`testing_rules.cursorrules`** - テスト・品質保証専用ルール

## 🔄 DEF-A部分適用戦略

### 適用パターン
- **完全DEF-A適用**: 戦略的・複雑な課題（Define→Explore→Formulate→Act→Assess）
- **部分DEF-A適用**: 技術実装質問（Formulate→Act→Assess）
- **最小DEF-A適用**: 緊急対応（Actのみ）
- **学習支援適用**: 教育・理解（Explore→Act）

### 認知スタイル
- **🧠 Systems Mode**: 戦略的システム思考型（構造化・論理的・全体最適化）
- **🌸 Empathy Mode**: 感情統合コミュニケーション型（段階的・実用的・感情共鳴）

## 📋 使用方法

### 基本使用
1. **質問分析**: 質問内容からDEF-A段階・認知スタイルを判定
2. **ルール選択**: 技術領域に応じた適切なルールファイルを選択
3. **部分適用**: 質問特性に応じたDEF-A段階を適用
4. **品質基準**: 三方よし・丁度いい・持続可能性の原則を適用

### プロンプトテンプレート
```markdown
# Cursor プロンプト - DEF-A統合指示

## [CONTEXT] 開発状況
- **プロジェクト**: [プロジェクト名・特性]
- **開発段階**: [要件定義/設計/実装/テスト/運用]
- **緊急度**: [緊急/通常/学習]
- **チーム規模**: [個人/小規模/大規模]

## [REQUEST] 具体的要求
[具体的な質問・要求内容]

## [DEF-A] 思考フロー指定
- **適用段階**: [Define/Explore/Formulate/Act/Assess]
- **認知スタイル**: [Systems思考重視/Empathy共感重視]
- **複雑性レベル**: [簡潔/標準/詳細]

## [RULES] 適用ルール
- **主要ルール**: [frontend/backend/testing/core]
- **品質基準**: [三方よし/丁度いい/持続可能性]
- **出力形式**: [コード/設計書/説明/チュートリアル]
```

## 🛠 技術スタック

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

## 🚀 セットアップ手順

### 1. 基本セットアップ
```bash
# リポジトリクローン
git clone [repository-url]
cd cursor_user_rules

# ルールファイル配置
cp rules/*.cursorrules ~/.cursor/rules/
```

### 2. Cursor設定
```json
// .cursorrules
@core_rules.cursorrules
@rule_selector.cursorrules
@defa_framework.cursorrules
@prompt_templates.cursorrules
@frontend_rules.cursorrules
@backend_rules.cursorrules
@testing_rules.cursorrules
```

### 3. 環境確認
- **Cursor**: 最新版推奨
- **Node.js**: v18以上
- **TypeScript**: v5以上

## 📚 参考資料

### DEF-Aモデル
- **Define**: 問題設定・多次元定義
- **Explore**: 多視点分析・深層探求
- **Formulate**: 統合・構造化・最適化
- **Act/Apply**: 実行・適用
- **Assess/Adjust**: 評価・調整

### 品質原則
- **三方よし**: 開発者・ユーザー・システム全体の利益
- **丁度いい**: 過不足のない最適解
- **持続可能性**: 長期的な保守・拡張性

## 🤝 貢献

### 開発ガイドライン
- **コード品質**: 可読性・保守性を重視
- **ドキュメント**: 包括的な説明・例の提供
- **テスト**: 品質保証・動作確認

### 貢献プロセス
1. **Issue作成**: 改善提案・バグ報告
2. **ブランチ作成**: 機能開発・修正
3. **プルリクエスト**: コードレビュー・マージ

## 📄 ライセンス

MIT License - 詳細は[LICENSE](LICENSE)ファイルを参照

## 📞 サポート

### 問題報告
- **GitHub Issues**: バグ報告・機能要求
- **ドキュメント**: 使用方法・トラブルシューティング

### コミュニティ
- **ディスカッション**: 技術的な質問・議論
- **フィードバック**: 改善提案・使用体験

---

**Version**: 2.0.0 (DEF-A統合最適化版)  
**Last Updated**: 2025年1月  
**Author**: Kentaro Kitagawa

 