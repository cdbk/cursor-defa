# ドキュメント作成標準ルール

## 📋 概要

このドキュメントは、Cursor Rulesプロジェクトにおけるドキュメント作成時の標準ルールとガイドラインを定義します。

## 🎯 [D適用] - 基本原則

### ドキュメント作成の基本方針
1. **正確性**: 事実に基づく正確な情報の記載
2. **一貫性**: 統一された形式とスタイルの維持
3. **再利用性**: Cursorエージェントでの再利用を考慮した構造化
4. **保守性**: 継続的な更新と改善が可能な形式

## 🔍 [E適用] - 日付管理ルール

### 日付取得方法

#### 1. システム日付の自動取得
```bash
# 日本語形式（推奨）
date '+%Y年%m月%d日'

# 英語形式（国際的な用途）
date '+%Y-%m-%d'

# 詳細な日時（ログ用途）
date '+%Y年%m月%d日 %H時%M分'

# ISO形式（技術的用途）
date -u '+%Y-%m-%dT%H:%M:%SZ'
```

#### 2. 日付取得の実装例
```javascript
// Node.jsでの日付取得
const currentDate = new Date();
const japaneseDate = `${currentDate.getFullYear()}年${String(currentDate.getMonth() + 1).padStart(2, '0')}月${String(currentDate.getDate()).padStart(2, '0')}日`;

// または、child_processを使用してシステムコマンド実行
const { execSync } = require('child_process');
const systemDate = execSync('date \'+%Y年%m月%d日\'').toString().trim();
```

### 日付記載ルール

#### 1. 必須項目
- **作成日**: ドキュメント作成時の実際の日付
- **更新日**: 最終更新時の日付（作成時は作成日と同じ）
- **バージョン**: 作成日を含むバージョン管理

#### 2. 日付形式
```markdown
**作成日**: YYYY年MM月DD日
**更新日**: YYYY年MM月DD日
**バージョン**: X.Y.Z (YYYY-MM-DD)
```

#### 3. 日付記載例
```markdown
---
**作成日**: 2025年7月11日
**更新日**: 2025年7月11日
**作成者**: AI Assistant
**バージョン**: 1.0
**ステータス**: 作成完了
---
```

### 日付管理のベストプラクティス

#### 1. 作成時
- ドキュメント作成開始時に日付を取得
- 作成完了時に最終的な日付を確定
- システム日付の自動取得を優先

#### 2. 更新時
- 内容変更時に更新日を更新
- 変更履歴を記録
- バージョン番号の適切な管理

#### 3. 検証時
- 日付の論理的整合性を確認
- 作成日と更新日の関係を検証
- システム日付との整合性を確認

## ✨ [F適用] - ドキュメント構造標準

### ヘッダー構造
```markdown
# ドキュメントタイトル

## 📋 概要

## 🎯 [D適用] - Define段階

## 🔍 [E適用] - Explore段階

## ✨ [F適用] - Formulate段階

## 📝 [A1適用] - Act/Apply段階

## 📈 [A2適用] - Assess/Adjust段階

---

**作成日**: YYYY年MM月DD日
**更新日**: YYYY年MM月DD日
**作成者**: [作成者名]
**バージョン**: [バージョン番号]
**ステータス**: [ステータス]
```

### メタデータ標準
```yaml
---
title: "ドキュメントタイトル"
description: "ドキュメントの概要説明"
author: "作成者名"
created: "YYYY-MM-DD"
updated: "YYYY-MM-DD"
version: "X.Y.Z"
status: "draft|review|approved|archived"
tags: ["タグ1", "タグ2"]
category: "カテゴリ"
priority: "high|medium|low"
---
```

## 📝 [A1適用] - 実装ガイドライン

### 1. 新規ドキュメント作成時
```bash
# 1. 日付取得
CURRENT_DATE=$(date '+%Y年%m月%d日')

# 2. ドキュメント作成
cat > new_document.md << EOF
# 新規ドキュメント

## 📋 概要

## 🎯 [D適用] - Define段階

## 🔍 [E適用] - Explore段階

## ✨ [F適用] - Formulate段階

## 📝 [A1適用] - Act/Apply段階

## 📈 [A2適用] - Assess/Adjust段階

---

**作成日**: ${CURRENT_DATE}
**更新日**: ${CURRENT_DATE}
**作成者**: AI Assistant
**バージョン**: 1.0
**ステータス**: 作成中
EOF
```

### 2. ドキュメント更新時
```bash
# 更新日取得
UPDATE_DATE=$(date '+%Y年%m月%d日')

# 更新日の置換
sed -i "s/更新日.*/更新日: ${UPDATE_DATE}/" document.md
```

### 3. バージョン管理
```bash
# バージョン番号の自動更新
VERSION=$(grep "バージョン" document.md | cut -d' ' -f2)
NEW_VERSION=$(echo $VERSION | awk -F. '{print $1"."$2"."$3+1}')
sed -i "s/バージョン.*/バージョン: ${NEW_VERSION}/" document.md
```

## 📈 [A2適用] - 品質保証

### 日付検証チェックリスト
- [ ] 作成日がシステム日付と整合しているか
- [ ] 更新日が作成日以降になっているか
- [ ] 日付形式が統一されているか
- [ ] バージョン番号が適切に管理されているか
- [ ] メタデータが完全に記載されているか

### 自動化スクリプト例
```bash
#!/bin/bash
# document_validator.sh

validate_date_format() {
    local file=$1
    local date_pattern="[0-9]{4}年[0-9]{2}月[0-9]{2}日"
    
    if grep -q "作成日.*${date_pattern}" "$file"; then
        echo "✅ 作成日形式: OK"
    else
        echo "❌ 作成日形式: NG"
        return 1
    fi
    
    if grep -q "更新日.*${date_pattern}" "$file"; then
        echo "✅ 更新日形式: OK"
    else
        echo "❌ 更新日形式: NG"
        return 1
    fi
}

validate_date_logic() {
    local file=$1
    local created_date=$(grep "作成日" "$file" | grep -o "[0-9]{4}年[0-9]{2}月[0-9]{2}日")
    local updated_date=$(grep "更新日" "$file" | grep -o "[0-9]{4}年[0-9]{2}月[0-9]{2}日")
    
    if [ "$created_date" = "$updated_date" ]; then
        echo "✅ 日付論理: OK"
    else
        echo "⚠️  日付論理: 更新日が作成日と異なります"
    fi
}

# メイン処理
for file in *.md; do
    echo "=== $file ==="
    validate_date_format "$file"
    validate_date_logic "$file"
    echo
done
```

### 継続的改善

#### 1. 定期的な見直し
- **月次**: 日付管理ルールの効果測定
- **四半期**: ルールの改善と最適化
- **年次**: 全体的な見直しと更新

#### 2. フィードバック収集
- ドキュメント作成者の意見収集
- 日付管理の課題と改善点
- 自動化の要望と提案

#### 3. ツール改善
- 日付取得の自動化
- バリデーション機能の強化
- テンプレート機能の拡張

---

**作成日**: 2025年7月11日
**更新日**: 2025年7月11日
**作成者**: AI Assistant
**バージョン**: 1.0
**ステータス**: 標準確立完了 