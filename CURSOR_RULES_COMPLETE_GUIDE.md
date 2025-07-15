# Cursor Rules - DEF-A統合最適化版 完全ガイド

**作成日**: 2025-07-13 
**バージョン**: v0.8.1  
**ライセンス**: MIT License  
**著作権**: (c) 2025 Kentaro Kitagawa

---

## 🎯 プロジェクト概要

このプロジェクトは、Cursor IDEで使用するための包括的なルールセットを提供します。DEF-Aモデル（Define→Explore→Formulate→Act→Assess）を統合し、効率的なAI協働を実現する2つのバージョンを提供します。

### 主要特徴
- **シンプル版**: 初心者・個人開発向けの直感的なルールセット
- **DEF-A統合版**: 上級者・チーム開発向けの包括的なルールセット
- **倫理的配慮システム**: 人間の尊厳・包摂性・相互学習を重視
- **段階的導入**: スキルレベルに応じた段階的な学習・適用

---

## 📁 ファイル構成

### シンプル版（`rules/simple/`）
初心者・個人開発者向けの軽量版ルールセット

| ファイル | 行数 | 説明 |
|---------|------|------|
| `core_rules.cursorrules` | 72行 | 基本品質基準・シンプル版 |
| `rule_selector.cursorrules` | 287行 | 質問分析・ルール選択 |
| `frontend_rules.cursorrules` | 82行 | フロントエンド開発専用ルール |
| `backend_rules.cursorrules` | 98行 | バックエンド開発専用ルール |
| `testing_rules.cursorrules` | 191行 | テスト・品質保証専用ルール |
| `knowledge_management_rules.cursorrules` | 108行 | 知識管理・学習支援・日付管理 |
| `ethics_core.cursorrules` | 126行 | 基本倫理原則の定義（軽量版） |
| `ethics_monitoring.cursorrules` | 165行 | 自己監視システム（軽量版） |
| `programming_ethics_rules.cursorrules` | 118行 | プログラミング倫理ルール |

### DEF-A統合版（`rules/defa/`）
上級者・チーム開発向けの包括的ルールセット

| ファイル | 行数 | 説明 |
|---------|------|------|
| `core_rules.cursorrules` | 157行 | 基本品質基準・DEF-A統合フレームワーク |
| `rule_selector.cursorrules` | 210行 | 質問分析・ルール選択システム |
| `defa_framework.cursorrules` | 185行 | DEF-Aモデル詳細・段階別ガイドライン |
| `prompt_templates.cursorrules` | 145行 | プロンプトテンプレート・基本構造 |
| `frontend_rules.cursorrules` | 82行 | フロントエンド開発専用ルール |
| `backend_rules.cursorrules` | 98行 | バックエンド開発専用ルール |
| `testing_rules.cursorrules` | 191行 | テスト・品質保証専用ルール |
| `error_handling_rules.cursorrules` | 335行 | エラー処理統合・多層防御戦略 |
| `team_collaboration_rules.cursorrules` | 372行 | チーム協働・知識共有・学習促進 |
| `knowledge_management_rules.cursorrules` | 336行 | SECIモデル統合・暗黙知自動ルール化 |
| `ethics_core.cursorrules` | 153行 | 基本倫理原則の定義 |
| `ethics_monitoring.cursorrules` | 247行 | 自己監視システム |
| `ethics_response.cursorrules` | 244行 | 応答調整システム |
| `ethics_integration.cursorrules` | 265行 | 統合システム |
| `programming_ethics_rules.cursorrules` | 236行 | プログラミング倫理ルール |

---

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

#### シンプル版セットアップ
```bash
# シンプル版ルールを配置
cp rules/simple/*.cursorrules ~/.cursor/rules/
```

```json
// .cursorrules
@core_rules.cursorrules
@rule_selector.cursorrules
@knowledge_management_rules.cursorrules
@ethics_core.cursorrules
@ethics_monitoring.cursorrules
@programming_ethics_rules.cursorrules
```

#### DEF-A統合版セットアップ
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
@ethics_core.cursorrules
@ethics_monitoring.cursorrules
@ethics_response.cursorrules
@ethics_integration.cursorrules
@programming_ethics_rules.cursorrules
```

---

## 🧠 DEF-Aモデル詳細

### DEF-Aモデルとは
**DEF-Aモデル**は、AI時代における人間の思考を構造化し、複雑な課題を体系的に解決するための実践的フレームワークです。

#### 5段階の思考プロセス
1. **🎯 Define（定義）**: 問題設定・多次元定義
2. **🔍 Explore（探求）**: 多視点分析・深層探求
3. **✨ Formulate（統合）**: 統合・構造化・最適化
4. **📝 Act（実行）**: 実行・適用
5. **📈 Assess（評価）**: 評価・調整

### 部分適用戦略

#### 完全DEF-A適用（戦略的質問）
- **適用場面**: システム設計・アーキテクチャ決定・複雑な技術選択
- **段階**: Define → Explore → Formulate → Act → Assess
- **認知負荷**: 高（詳細な分析・統合が必要）

#### 部分DEF-A適用（技術実装質問）
- **適用場面**: 具体的な実装・コーディング・機能追加
- **段階**: Formulate → Act → Assess（実装重視）
- **認知負荷**: 中（実装・品質重視）

#### 最小DEF-A適用（緊急対応）
- **適用場面**: バグ修正・緊急対応・即座の解決が必要
- **段階**: Act（緊急対応実装のみ）
- **認知負荷**: 低（効率性最優先）

#### 学習支援適用（教育・理解）
- **適用場面**: 学習・技術理解・段階的説明
- **段階**: Explore → Act（学習・実践）
- **認知負荷**: 中（段階的理解重視）

### 認知スタイル

#### 🧠 Systems Mode（戦略的システム思考型）
- **適用場面**: 戦略分析・システム設計・複雑性統合・技術文書
- **特徴**: システム思考による全体最適化・長期的価値重視・構造化された論理的説明

#### 🌸 Empathy Mode（感情統合コミュニケーション型）
- **適用場面**: コンテンツ制作・読者との関係構築・感情的価値重視
- **特徴**: 感情共鳴による理解促進・実用性・段階的説明の重視・温かみのある表現

---

## 💡 使用例

### シンプル版使用例
```markdown
# Cursor プロンプト - シンプル指示

## [REQUEST] 具体的要求
TypeScriptで型安全なAPIクライアントを実装したい

## [RULES] 適用ルール
- **品質基準**: 可読性・保守性重視
- **出力形式**: 実装コード + 簡単な説明
```

### DEF-A統合版使用例
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

---

## 🛡️ 倫理的配慮システム

### 基本倫理原則
1. **人間の尊厳の平等な尊重**: 認知レベルに関係ない個人の価値認識
2. **機会平等の確保**: 成長・学習機会の公平な提供
3. **包摂的コミュニケーション**: すべての人が理解・参加できる対話
4. **相互学習の促進**: 一方的教授ではなく双方向的成長

### 倫理システム構成

#### シンプル版
- `ethics_core.cursorrules`: 基本倫理原則の定義（軽量版）
- `ethics_monitoring.cursorrules`: 自己監視システム（軽量版）
- `programming_ethics_rules.cursorrules`: プログラミング倫理ルール

#### DEF-A統合版
- `ethics_core.cursorrules`: 基本倫理原則の定義
- `ethics_monitoring.cursorrules`: 自己監視システム
- `ethics_response.cursorrules`: 応答調整システム
- `ethics_integration.cursorrules`: 統合システム
- `programming_ethics_rules.cursorrules`: プログラミング倫理ルール

### プログラミング倫理ルール
- **命名の倫理的配慮**: 関数名・変数名の包摂性・明確性
- **コメントの倫理的配慮**: 理解しやすく・偏見のない説明
- **エラーメッセージの倫理的配慮**: ユーザーフレンドリーで建設的な表現
- **コードレビューの倫理的配慮**: 建設的・成長促進的なフィードバック

---

## 🛠️ 対応技術スタック

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

---

## 📊 品質基準

### 基本品質原則
- **可読性 > 巧妙さ**: 明確な変数名、適切なコメント
- **型安全性**: TypeScript使用、適切な型定義
- **エラーハンドリング**: 適切な例外処理、ユーザーフレンドリーなエラーメッセージ
- **セキュリティ**: 入力検証、XSS対策、SQLインジェクション対策

### DEF-A統合品質基準
- **三方よし**: 開発者・ユーザー・システム全体の利益を考慮
- **丁度いい**: 過不足のない最適な解を追求
- **持続可能性**: 長期的な保守・拡張を考慮した設計

### 実装方針
- **段階的実装**: 小さなステップで確実に進める
- **検証可能**: テスト可能な形で実装
- **保守性**: 将来の変更に耐える設計
- **日付管理**: システム日付の自動取得・検証による正確性確保

---

## 🔄 プロジェクト特性別対応

### [STARTUP] スタートアップ・新規プロジェクト
- **優先度**: 速度重視・MVP開発
- **DEF-A戦略**: 最小適用中心・迅速プロトタイピング
- **品質基準**: 基本品質保証・迅速な市場投入
- **チーム協働**: 柔軟な役割分担・直接コミュニケーション

### [ENTERPRISE] エンタープライズ・大規模プロジェクト
- **優先度**: 安定性・スケーラビリティ重視
- **DEF-A戦略**: 完全適用・包括的品質保証
- **品質基準**: 高品質・セキュリティ・保守性
- **チーム協働**: 標準化されたプロセス・明確な役割分担

### [MAINTENANCE] 保守・改善プロジェクト
- **優先度**: 既存システム安定性・段階的改善
- **DEF-A戦略**: Assess→Formulate→Act（改善重視）
- **品質基準**: 既存品質維持・段階的向上
- **チーム協働**: 知識継承・継続的改善

### [LEARNING] 学習・教育プロジェクト
- **優先度**: スキル向上・理解促進
- **DEF-A戦略**: 学習支援適用・段階的習得
- **品質基準**: 学習効果・理解度重視
- **チーム協働**: メンタリング・相互学習

---

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

### 倫理的配慮指標
- **倫理的配慮**: 無意識的バイアスの自動検出・修正機能
- **包摂性向上**: 多様性を認める表現への自動変換
- **人間性保持**: 効率性と温かみのバランス調整
- **成長促進**: 相互学習機会の自動創出

---

## ⚠️ 重要: 複雑性について

このルールセットは**包括的で高度な機能**を提供しますが、**初心者には複雑すぎる可能性**があります。

### 推奨使用シーン
- ✅ **初心者・個人開発**: シンプル版から開始
- ✅ **中級者以上**: 開発経験があり、体系的なアプローチを求める方
- ✅ **チーム開発**: 統一された品質基準とプロセスが必要な場合
- ✅ **大規模プロジェクト**: 包括的な開発ガイドラインが必要な場合

### 注意が必要なシーン
- ⚠️ **緊急対応**: 複雑な分類よりも迅速な解決が必要な場合
- ⚠️ **学習初期**: まずは基本的なCursorの使い方に慣れることを推奨

---

## 📚 詳細ドキュメント

### 主要ドキュメント
- **README.md**: プロジェクト概要・セットアップ手順
- **DEF-A_INTEGRATION_GUIDE.md**: DEF-A統合の詳細ガイド
- **CHANGELOG.md**: 変更履歴・バージョン情報
- **CONTRIBUTING.md**: 貢献ガイドライン
- **CODE_OF_CONDUCT.md**: 行動規範
- **SECURITY.md**: セキュリティポリシー

### ライセンス情報
- **ライセンス**: MIT License
- **著作権**: (c) 2025 Kentaro Kitagawa
- **利用条件**: 商用・非商用問わず自由に利用可能

---

## 🔗 関連リンク

- **GitHub**: [repository-url]
- **ライセンス**: https://opensource.org/licenses/MIT
- **Cursor IDE**: https://cursor.sh/

---

## 📞 サポート・フィードバック

このルールセットに関する質問・提案・バグ報告は、GitHubのIssuesページでお気軽にお知らせください。

**作成日**: 2025-01-27  
**最終更新**: 2025-01-27  
**バージョン**: v0.8.1 