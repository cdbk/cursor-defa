#!/bin/bash

# Cursor Rules Setup Script
# 公開ルールファイルをローカル環境にセットアップ

echo "🚀 Cursor Rules Setup Script"
echo "================================"

# .cursorディレクトリの作成
mkdir -p .cursor/rules

# ルールファイルのコピー
echo "📁 Copying rule files..."
cp rules/core_rules.cursorrules .cursor/rules/
cp rules/rule_selector.cursorrules .cursor/rules/
cp rules/frontend_rules.cursorrules .cursor/rules/
cp rules/backend_rules.cursorrules .cursor/rules/
cp rules/testing_rules.cursorrules .cursor/rules/

echo "✅ Setup completed!"
echo "📝 Available rules:"
ls -la .cursor/rules/

echo ""
echo "💡 Usage:"
echo "   - Copy specific rules to .cursorrules for your project"
echo "   - Or use rule_selector.cursorrules for dynamic selection"
echo ""
echo "🔄 To update rules:"
echo "   - Run this script again after pulling latest changes" 