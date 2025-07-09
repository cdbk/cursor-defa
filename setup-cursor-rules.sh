#!/bin/bash

# Cursor Rules Setup Script - DEF-A統合最適化版
# Copyright (c) 2025 Kentaro Kitagawa
# MIT License - https://opensource.org/licenses/MIT

echo "🚀 Cursor Rules Setup - DEF-A統合最適化版"
echo "=========================================="

# ルールディレクトリの作成
CURSOR_RULES_DIR="$HOME/.cursor/rules"
if [ ! -d "$CURSOR_RULES_DIR" ]; then
    echo "📁 Creating Cursor rules directory: $CURSOR_RULES_DIR"
    mkdir -p "$CURSOR_RULES_DIR"
else
    echo "✅ Cursor rules directory already exists: $CURSOR_RULES_DIR"
fi

# ルールファイルのコピー
echo "📋 Copying rule files..."

# コアファイル（コンパクト版）
cp rules/core_rules.cursorrules "$CURSOR_RULES_DIR/"
cp rules/rule_selector.cursorrules "$CURSOR_RULES_DIR/"

# 詳細ファイル（必要時参照）
cp rules/defa_framework.cursorrules "$CURSOR_RULES_DIR/"
cp rules/prompt_templates.cursorrules "$CURSOR_RULES_DIR/"

# 技術領域別ファイル
cp rules/frontend_rules.cursorrules "$CURSOR_RULES_DIR/"
cp rules/backend_rules.cursorrules "$CURSOR_RULES_DIR/"
cp rules/testing_rules.cursorrules "$CURSOR_RULES_DIR/"

echo "✅ All rule files copied successfully!"

# ファイル一覧の表示
echo "📁 Installed rule files:"
ls -la "$CURSOR_RULES_DIR"/*.cursorrules

echo ""
echo "🎯 Setup completed! Please restart Cursor to apply the new rules."
echo "📚 For usage instructions, see README.md and DEF-A_INTEGRATION_GUIDE.md" 