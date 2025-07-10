# アーカイブ - 旧DEF-A Development Framework

## 概要

このディレクトリには、DEF-A Development Frameworkの旧バージョンが保存されています。新しい4ファイル構成の動的ルールシステムに移行する前の、単一ファイル構成のルールファイルです。

## ファイル一覧

### defa_development_framework.mdc
- **バージョン**: v0.1.0（完全版）
- **行数**: 547行
- **特徴**: 包括的な理論的背景と実装例を含む詳細版
- **用途**: プロジェクト設計や長期的な技術戦略の検討時
- **リリース日**: 2025-07-08

### defa_development_framework_compact.mdc
- **バージョン**: v2.0.0（コンパクト版）
- **行数**: 292行
- **特徴**: 実用性重視の簡潔版（47%削減）
- **用途**: 日常的な開発作業での使用
- **リリース日**: 2025-07-09

## 新システムへの移行

### 移行理由
1. **処理効率向上**: 単一ファイルの長文による処理負荷の軽減
2. **適用精度向上**: 質問内容に応じた動的ルール選択
3. **保守性向上**: 特定領域の更新が他に影響しない
4. **拡張性向上**: 新しい技術領域の追加が容易

### 新システム構成
```
rules/
├── core_rules.mdc          # 基本品質基準・プロファイル適用ログ
├── frontend_rules.mdc      # フロントエンド開発専用ルール
├── backend_rules.mdc       # バックエンド開発専用ルール
├── testing_rules.mdc       # テスト・品質保証専用ルール
└── rule_selector.mdc       # 質問内容に応じたルール選択システム
```

### 移行マッピング
| 旧ファイル | 新ファイル | 内容 |
|-----------|-----------|------|
| 基本品質基準 | core_rules.mdc | コード品質、プロファイル適用ログ |
| フロントエンド技術 | frontend_rules.mdc | React/Vue/Nuxt等のフロントエンド技術 |
| バックエンド技術 | backend_rules.mdc | API設計、データベース、セキュリティ |
| TDD/BDD | testing_rules.mdc | テスト駆動開発、品質保証 |
| ルール選択 | rule_selector.mdc | 質問内容に応じた動的選択 |

## 使用方法

### 旧システムを使用する場合
```bash
# 完全版を使用
cp archive_rules/defa_development_framework.mdc .mdc

# コンパクト版を使用
cp archive_rules/defa_development_framework_compact.mdc .mdc
```

### 新システムを使用する場合（推奨）
```bash
# 基本設定
cp rules/core_rules.mdc .mdc
cp rules/rule_selector.mdc .mdc
```

## バージョン履歴

### v2.0.0 (2025-07-09)
- コンパクト版ルールファイルを追加
- ファイルサイズを47%削減（547行 → 292行）
- 基本特性を保持しつつ実用性を向上

### v0.1.0 (2025-07-08)
- 初回リリース
- DEF-A Development Framework完全版を提供
- TDD/BDD統合開発フレームワークを実装

## 注意事項

- 旧ファイルは参考用として保持されています
- 新機能開発には新システムの使用を推奨します
- 旧ファイルの内容は新システムに統合されています
- 互換性の問題がある場合は、このアーカイブを参照してください

## ライセンス

MIT License - https://opensource.org/licenses/MIT

## 作者

Kentaro Kitagawa (北川健太郎)
- GitHub: https://github.com/cdbk
- Website: https://cdbk.tokyo 