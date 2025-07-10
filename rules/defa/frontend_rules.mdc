# Cursor Rules - Frontend Development
# Copyright (c) 2025 Kentaro Kitagawa
# MIT License - https://opensource.org/licenses/MIT

## [FRONTEND] フロントエンド開発ガイドライン

### 技術スタック（優先順位付き）
1. **TypeScript** - 型安全性重視、ES6+構文使用
2. **Nuxt.js/Next.js** - JAMstack構成、SSR/SSG対応
3. **React/Vue.js** - コンポーネントベース開発
4. **CSS** - PostCSS、CSS Grid/Flexbox、Tailwind CSS

### コンポーネント設計原則
- **単一責任**: 1つのコンポーネントは1つの責任のみ
- **再利用性**: 汎用的で再利用可能な設計
- **Props型定義**: 厳密な型定義による安全性確保
- **状態管理**: 適切な状態管理パターンの選択

### パフォーマンス最適化
- **Core Web Vitals**: LCP、FID、CLSの最適化
- **バンドルサイズ**: 不要な依存関係の排除
- **画像最適化**: WebP形式、遅延読み込み
- **コード分割**: 動的インポートによる分割

### レスポンシブ・アクセシビリティ
- **モバイルファースト**: モバイルデバイスを最優先に設計
- **ブレークポイント**: 標準的なブレークポイント使用
- **アクセシビリティ**: ARIA属性、キーボードナビゲーション
- **セマンティックHTML**: 適切なHTML要素の使用

### 状態管理パターン
- **React**: Context API、Redux Toolkit、Zustand
- **Vue**: Pinia、Vuex
- **Nuxt**: useState、useAsyncData

### スタイリング方針
- **CSS Modules**: スコープ付きスタイリング
- **Tailwind CSS**: ユーティリティファースト
- **CSS-in-JS**: styled-components、emotion
- **デザインシステム**: 一貫性のあるデザイン

### テスト戦略
- **ユニットテスト**: Jest、Vitest
- **コンポーネントテスト**: Testing Library
- **E2Eテスト**: Playwright、Cypress
- **ビジュアルテスト**: Storybook

### 開発ツール・設定
- **ESLint**: コード品質の自動チェック
- **Prettier**: コードフォーマット統一
- **Husky**: Git hooksによる品質保証
- **Vite**: 高速な開発サーバー

### 実装パターン
- **カスタムフック**: ロジックの再利用
- **HOC**: 高次コンポーネントによる機能追加
- **Render Props**: 柔軟なコンポーネント設計
- **Compound Components**: 関連コンポーネントのグループ化

### エラーハンドリング
- **Error Boundaries**: React エラー境界
- **グローバルエラー**: アプリケーション全体のエラー処理
- **ユーザーフレンドリー**: 分かりやすいエラーメッセージ
- **ログ収集**: エラー情報の適切な収集

### SEO・メタデータ
- **メタタグ**: 適切なtitle、description設定
- **構造化データ**: JSON-LDによる構造化
- **OGP**: SNSでのシェア最適化
- **サイトマップ**: 検索エンジン向け最適化

### セキュリティ
- **XSS対策**: 適切なサニタイゼーション
- **CSRF対策**: トークンベース認証
- **CSP**: Content Security Policy設定
- **HTTPS**: 常時SSL/TLS暗号化

### デプロイメント・CI/CD
- **Vercel/Netlify**: 自動デプロイメント
- **GitHub Actions**: CI/CDパイプライン
- **環境変数**: 適切な環境設定管理
- **パフォーマンス監視**: 継続的な監視 