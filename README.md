# Cursor Development Rules Collection

## 概要

Cursor用の開発支援ルールファイル集です。フロントエンド、バックエンド、全般開発に対応したルールを含み、AI協働開発の効率化と品質向上を目的としています。

**開発手法**: このプロジェクトは[Cursor](https://cursor.sh/)によるVibe Coding（AI協働開発）で作成されています。AIとの対話を通じて、効率的かつ高品質なコード開発を実現しています。

## 特徴

- **全般開発ルール**: コード品質・パフォーマンス・セキュリティ・アクセシビリティ等を網羅
- **TDD/BDD統合**: テスト駆動開発・ビヘイビア駆動開発の適用判断フレームワーク
- **ログ機能**: プロファイル適用状況の可視化と継続的改善
- **段階的適用**: プロジェクト規模や緊急度に応じた使い分け
- **技術スタック対応**: フロントエンド（TypeScript、Nuxt.js、Next.js）・バックエンド（Node.js、Python、データベース）対応
- **AI協働開発**: Vibe Codingによる効率的な開発プロセスと品質保証

## ファイル構成

```
rules/
├── general_development_rules.cursorrules    # 全般開発ルール
├── LICENSE                                  # MIT License
└── README.md                               # このファイル
```

## 使用方法

1. `.cursorrules` ファイルをプロジェクトルートに配置
2. Cursorでプロジェクトを開く
3. AI支援機能が自動的に適用されます

### 主要機能

#### TDD/BDD統合開発
- **TDD（テスト駆動開発）**: Red-Green-Refactorサイクルによる品質保証
- **BDD（ビヘイビア駆動開発）**: Given-When-Then形式によるビジネス価値重視
- **適用判断フレームワーク**: 開発状況に応じた最適な手法選択

#### ログ機能
- **可視化マーカー**: 応答冒頭での適用状況表示
- **詳細ログ**: 応答末尾での判断根拠と考慮要素の明記
- **継続的改善**: プロファイル適用効果の測定と最適化

#### 段階的適用
- **緊急モード**: バグ修正・緊急対応時の簡潔解決策
- **設計モード**: 新機能開発時の多角的検討
- **アーキテクチャモード**: システム設計時の全体最適化

### Vibe Codingについて

Vibe Codingは、AIとの自然な対話を通じてコードを開発する手法です。このプロジェクトでは、CursorのAI機能を活用して、効率的かつ高品質な開発を実現しています。

- **対話的開発**: AIとの継続的な対話による段階的改善
- **品質保証**: 人間の判断とAIの提案の最適な組み合わせ
- **学習効果**: 開発プロセスを通じた技術的成長

### 設定例

```bash
# プロジェクトルートにルールファイルをコピー
cp rules/general_development_rules.cursorrules .cursorrules
```

### 使用例

#### 新機能開発時
```
🧠 [メタ認知適用] 要件→設計→実装の段階的思考プロセスを適用します。
📊 [多視点分析適用] 技術選択、ユーザー体験、保守性の観点から分析します。
🔍 [TDD/BDD判断] 複雑性: 高、チーム規模: 小規模、品質要求: 高 → TDD+BDD適用

[実装内容]
```

#### バグ修正時
```
⚖️ [複雑性調整適用] 緊急度高のため、簡潔で即効性のある解決策を優先提示します。

[修正内容]
```

#### アーキテクチャ設計時
```
🔄 [システム思考適用] システム全体の構造的整合性を重視し、全体最適化の観点から設計判断を行います。
💎 [品質・倫理配慮適用] 「丁度いい」原則に基づき、過剰・過少設計を回避した最適解を追求します。

[設計内容]
```

## ライセンス

MIT License - 詳細は [LICENSE](LICENSE) ファイルを参照してください。

## 作者

**Kentaro Kitagawa**  
GitHub: [https://github.com/cdbk](https://github.com/cdbk)

## 技術スタック

### フロントエンド
- **TypeScript/JavaScript**: 型安全性重視の開発
- **Nuxt.js/Next.js**: JAMstack構成による高速なWebアプリケーション
- **CSS**: PostCSS、CSS Grid/Flexboxによるモダンなレイアウト

### バックエンド
- **Node.js/TypeScript**: サーバーサイド開発
- **Python/FastAPI**: API開発・データ処理
- **データベース**: PostgreSQL、Redis、MongoDB
- **インフラ**: Docker、Kubernetes、AWS/GCP

## 貢献

プルリクエストやイシューの報告を歓迎します。

1. このリポジトリをフォーク
2. 機能ブランチを作成 (`git checkout -b feature/amazing-feature`)
3. 変更をコミット (`git commit -m 'Add some amazing feature'`)
4. ブランチにプッシュ (`git push origin feature/amazing-feature`)
5. プルリクエストを作成

## ライセンス

このプロジェクトはMIT Licenseの下で公開されています。詳細は [LICENSE](LICENSE) ファイルを参照してください。 