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

# バージョン選択
echo ""
echo "📋 ルールセットを選択してください:"
echo "1) シンプル版 - 初心者・個人開発向け"
echo "2) DEF-A統合版 - 上級者・チーム開発向け"
echo "3) 両方インストール"
echo ""
read -p "選択してください (1-3): " choice

case $choice in
    1)
        echo "📋 シンプル版をインストール中..."
        # シンプル版ファイルのコピー
        cp rules/simple/core_rules.mdc "$CURSOR_RULES_DIR/"
        cp rules/simple/rule_selector.mdc "$CURSOR_RULES_DIR/"
        cp rules/simple/frontend_rules.mdc "$CURSOR_RULES_DIR/"
        cp rules/simple/backend_rules.mdc "$CURSOR_RULES_DIR/"
        cp rules/simple/testing_rules.mdc "$CURSOR_RULES_DIR/"
        echo "✅ シンプル版のインストールが完了しました！"
        ;;
    2)
        echo "📋 DEF-A統合版をインストール中..."
        # DEF-A統合版ファイルのコピー
        cp rules/defa/core_rules.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/rule_selector.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/defa_framework.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/prompt_templates.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/frontend_rules.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/backend_rules.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/testing_rules.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/error_handling_rules.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/team_collaboration_rules.mdc "$CURSOR_RULES_DIR/"
        echo "✅ DEF-A統合版のインストールが完了しました！"
        ;;
    3)
        echo "📋 両方のバージョンをインストール中..."
        # シンプル版ファイルのコピー
        cp rules/simple/core_rules.mdc "$CURSOR_RULES_DIR/core_rules_simple.mdc"
        cp rules/simple/rule_selector.mdc "$CURSOR_RULES_DIR/rule_selector_simple.mdc"
        cp rules/simple/frontend_rules.mdc "$CURSOR_RULES_DIR/frontend_rules_simple.mdc"
        cp rules/simple/backend_rules.mdc "$CURSOR_RULES_DIR/backend_rules_simple.mdc"
        cp rules/simple/testing_rules.mdc "$CURSOR_RULES_DIR/testing_rules_simple.mdc"
        
        # DEF-A統合版ファイルのコピー
        cp rules/defa/core_rules.mdc "$CURSOR_RULES_DIR/core_rules_defa.mdc"
        cp rules/defa/rule_selector.mdc "$CURSOR_RULES_DIR/rule_selector_defa.mdc"
        cp rules/defa/defa_framework.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/prompt_templates.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/frontend_rules.mdc "$CURSOR_RULES_DIR/frontend_rules_defa.mdc"
        cp rules/defa/backend_rules.mdc "$CURSOR_RULES_DIR/backend_rules_defa.mdc"
        cp rules/defa/testing_rules.mdc "$CURSOR_RULES_DIR/testing_rules_defa.mdc"
        cp rules/defa/error_handling_rules.mdc "$CURSOR_RULES_DIR/"
        cp rules/defa/team_collaboration_rules.mdc "$CURSOR_RULES_DIR/"
        echo "✅ 両方のバージョンのインストールが完了しました！"
        ;;
    *)
        echo "❌ 無効な選択です。1-3のいずれかを選択してください。"
        exit 1
        ;;
esac

# ファイル一覧の表示
echo ""
echo "📁 Installed rule files:"
ls -la "$CURSOR_RULES_DIR"/*.mdc

echo ""
echo "🎯 Setup completed! Please restart Cursor to apply the new rules."
echo "📚 For usage instructions, see README.md and DEF-A_INTEGRATION_GUIDE.md"
echo ""
echo "💡 設定例:"
if [ "$choice" = "1" ]; then
    echo "   .mdc ファイルに以下を追加:"
    echo "   @core_rules.mdc"
    echo "   @rule_selector.mdc"
elif [ "$choice" = "2" ]; then
    echo "   .mdc ファイルに以下を追加:"
    echo "   @core_rules.mdc"
    echo "   @rule_selector.mdc"
    echo "   @defa_framework.mdc"
elif [ "$choice" = "3" ]; then
    echo "   シンプル版を使用する場合:"
    echo "   @core_rules_simple.mdc"
    echo "   @rule_selector_simple.mdc"
    echo ""
    echo "   DEF-A統合版を使用する場合:"
    echo "   @core_rules_defa.mdc"
    echo "   @rule_selector_defa.mdc"
    echo "   @defa_framework.mdc"
fi 