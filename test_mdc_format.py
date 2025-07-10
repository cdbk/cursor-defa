#!/usr/bin/env python3
"""
MDC Format Validation Script
mdcファイルがmdcフォーマットに適合しているかをチェックするスクリプト
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class MDCFormatValidator:
    def __init__(self, rules_dir: str = "rules"):
        self.rules_dir = Path(rules_dir)
        
    def validate_mdc_format(self) -> Dict:
        """mdcファイルのフォーマットを検証"""
        print("🔍 MDCフォーマット検証を開始...")
        
        results = {
            "passed": 0,
            "failed": 0,
            "format_issues": [],
            "file_reports": {}
        }
        
        for mdc_file in self.rules_dir.rglob("*.mdc"):
            try:
                content = mdc_file.read_text(encoding='utf-8')
                validation_result = self._validate_single_file(content, str(mdc_file))
                results["file_reports"][str(mdc_file)] = validation_result
                
                if validation_result["is_valid"]:
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                    results["format_issues"].extend(validation_result["issues"])
                    
            except Exception as e:
                results["failed"] += 1
                results["format_issues"].append(f"{mdc_file}: 読み込みエラー - {e}")
                
        return results
    
    def _validate_single_file(self, content: str, filename: str) -> Dict:
        """単一ファイルのmdcフォーマットを検証"""
        issues = []
        
        # 1. ヘッダー構造の確認
        if not self._check_header_structure(content):
            issues.append("ヘッダー構造が不正です")
        
        # 2. セクション構造の確認
        if not self._check_section_structure(content):
            issues.append("セクション構造が不正です")
        
        # 3. マーカーシステムの確認
        if not self._check_marker_system(content):
            issues.append("マーカーシステムが不完全です")
        
        # 4. ログシステムの確認
        if not self._check_log_system(content):
            issues.append("ログシステムが不完全です")
        
        # 5. コードブロックの確認
        if not self._check_code_blocks(content):
            issues.append("コードブロックの形式が不正です")
        
        # 6. 日本語と英語の混在確認
        if not self._check_language_mix(content):
            issues.append("日本語と英語の混在が不適切です")
        
        # 7. 構造的一貫性の確認
        if not self._check_structural_consistency(content):
            issues.append("構造的一貫性が不足しています")
        
        return {
            "is_valid": len(issues) == 0,
            "issues": issues,
            "content_length": len(content),
            "sections_count": len(re.findall(r'##\s*\[', content))
        }
    
    def _check_header_structure(self, content: str) -> bool:
        """ヘッダー構造の確認"""
        lines = content.split('\n')
        
        # 最初の行が#で始まるか
        if not lines[0].startswith('# '):
            return False
        
        # Copyright行の確認
        copyright_pattern = r'Copyright.*Kentaro Kitagawa'
        if not re.search(copyright_pattern, content, re.IGNORECASE):
            return False
        
        # MIT License行の確認
        license_pattern = r'MIT License'
        if not re.search(license_pattern, content, re.IGNORECASE):
            return False
        
        return True
    
    def _check_section_structure(self, content: str) -> bool:
        """セクション構造の確認"""
        # [CORE], [LOG], [CONTEXT]などのセクションが存在するか
        required_sections = [
            r'##\s*\[CORE\]',
            r'##\s*\[LOG\]',
            r'##\s*\[CONTEXT\]'
        ]
        
        for section in required_sections:
            if not re.search(section, content):
                return False
        
        # セクションが適切な階層構造になっているか
        sections = re.findall(r'##\s*\[([^\]]+)\]', content)
        if len(sections) < 3:  # 最低3つのセクションが必要
            return False
        
        return True
    
    def _check_marker_system(self, content: str) -> bool:
        """マーカーシステムの確認"""
        # 絵文字マーカーが定義されているか
        emoji_markers = re.findall(r'[🎯🔍✨📝📈🧠🌸🔄⚖️📊🎯🤖💎🧪🎭🔍]', content)
        if len(emoji_markers) < 5:  # 最低5つのマーカーが必要
            return False
        
        # マーカーが適切に説明されているか
        marker_explanations = re.findall(r'\[.*適用\]', content)
        if len(marker_explanations) < 3:
            return False
        
        return True
    
    def _check_log_system(self, content: str) -> bool:
        """ログシステムの確認"""
        # ログ出力のテンプレートが定義されているか
        log_templates = [
            r'Profile Applied',
            r'Applied Rules',
            r'Decision Rationale',
            r'Cognitive Elements'
        ]
        
        for template in log_templates:
            if not re.search(template, content, re.IGNORECASE):
                return False
        
        return True
    
    def _check_code_blocks(self, content: str) -> bool:
        """コードブロックの確認"""
        # コードブロックが適切に囲まれているか
        code_blocks = re.findall(r'```[\w]*\n(.*?)\n```', content, re.DOTALL)
        
        # 少なくとも1つのコードブロックが必要
        if len(code_blocks) == 0:
            return False
        
        # コードブロック内に適切な内容があるか
        for block in code_blocks:
            if len(block.strip()) < 10:  # 最低10文字の内容が必要
                return False
        
        return True
    
    def _check_language_mix(self, content: str) -> bool:
        """日本語と英語の混在確認"""
        # 日本語文字の存在確認
        japanese_chars = re.findall(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]', content)
        if len(japanese_chars) < 50:  # 最低50文字の日本語が必要
            return False
        
        # 英語の存在確認
        english_words = re.findall(r'\b[a-zA-Z]+\b', content)
        if len(english_words) < 20:  # 最低20個の英語単語が必要
            return False
        
        return True
    
    def _check_structural_consistency(self, content: str) -> bool:
        """構造的一貫性の確認"""
        # 見出しレベルの一貫性
        headers = re.findall(r'^(#{1,6})\s+(.+)$', content, re.MULTILINE)
        
        if len(headers) < 5:  # 最低5つの見出しが必要
            return False
        
        # 見出しレベルが適切か（# と ## が主）
        for level, _ in headers:
            if len(level) > 3:  # ### より深いレベルは避ける
                return False
        
        # リスト構造の確認
        list_items = re.findall(r'^\s*[-*+]\s+', content, re.MULTILINE)
        if len(list_items) < 10:  # 最低10個のリストアイテムが必要
            return False
        
        return True
    
    def generate_format_report(self) -> str:
        """フォーマット検証レポートを生成"""
        results = self.validate_mdc_format()
        
        report = []
        report.append("# MDCフォーマット検証レポート")
        report.append("")
        
        # サマリー
        total_files = results["passed"] + results["failed"]
        success_rate = (results["passed"] / total_files * 100) if total_files > 0 else 0
        
        report.append(f"## 📊 検証サマリー")
        report.append(f"- **検証ファイル数**: {total_files}")
        report.append(f"- **合格**: {results['passed']}")
        report.append(f"- **不合格**: {results['failed']}")
        report.append(f"- **成功率**: {success_rate:.1f}%")
        report.append("")
        
        # 詳細レポート
        report.append("## 📋 詳細レポート")
        for filename, file_result in results["file_reports"].items():
            status = "✅" if file_result["is_valid"] else "❌"
            report.append(f"### {status} {filename}")
            report.append(f"- **行数**: {file_result['content_length']}")
            report.append(f"- **セクション数**: {file_result['sections_count']}")
            
            if not file_result["is_valid"]:
                report.append("- **問題点**:")
                for issue in file_result["issues"]:
                    report.append(f"  - {issue}")
            report.append("")
        
        # 改善提案
        if results["format_issues"]:
            report.append("## 🔧 改善提案")
            report.append("以下の問題を修正することを推奨します：")
            report.append("")
            
            issue_counts = {}
            for issue in results["format_issues"]:
                issue_counts[issue] = issue_counts.get(issue, 0) + 1
            
            for issue, count in sorted(issue_counts.items(), key=lambda x: x[1], reverse=True):
                report.append(f"- **{issue}** (発生回数: {count})")
            report.append("")
        
        return "\n".join(report)

def main():
    """メイン実行関数"""
    validator = MDCFormatValidator()
    
    print("🚀 MDCフォーマット検証を開始...\n")
    
    # 検証実行
    results = validator.validate_mdc_format()
    
    # 結果表示
    total_files = results["passed"] + results["failed"]
    success_rate = (results["passed"] / total_files * 100) if total_files > 0 else 0
    
    print(f"📊 検証結果サマリー:")
    print(f"✅ 合格: {results['passed']}")
    print(f"❌ 不合格: {results['failed']}")
    print(f"📈 成功率: {success_rate:.1f}%")
    
    if results["format_issues"]:
        print(f"\n❌ 検出された問題:")
        for issue in results["format_issues"][:10]:  # 最初の10件のみ表示
            print(f"  - {issue}")
        if len(results["format_issues"]) > 10:
            print(f"  ... 他 {len(results['format_issues']) - 10} 件")
    
    # 詳細レポート生成
    report = validator.generate_format_report()
    
    # レポートファイルに保存
    with open("mdc_format_report.md", "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"\n📄 詳細レポートを 'mdc_format_report.md' に保存しました")

if __name__ == "__main__":
    main() 