#!/usr/bin/env python3
"""
Cursor User Rules Test Script
ユーザールールの機能をテストするためのスクリプト
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class RulesTester:
    def __init__(self, rules_dir: str = "rules"):
        self.rules_dir = Path(rules_dir)
        self.test_results = []
        
    def test_rule_selector(self) -> Dict:
        """ルールセレクターの機能をテスト"""
        print("🔍 ルールセレクターのテストを開始...")
        
        results = {
            "passed": 0,
            "failed": 0,
            "tests": []
        }
        
        # テストケース
        test_cases = [
            {
                "question": "Reactでユーザー登録フォームを作成したい",
                "expected_domain": "フロントエンド",
                "expected_rules": ["frontend_rules", "core_rules"]
            },
            {
                "question": "Node.jsでRESTful APIを設計したい",
                "expected_domain": "バックエンド", 
                "expected_rules": ["backend_rules", "core_rules"]
            },
            {
                "question": "Jestでユニットテストを書く方法",
                "expected_domain": "テスト",
                "expected_rules": ["testing_rules", "core_rules"]
            },
            {
                "question": "プロジェクトのアーキテクチャ設計について",
                "expected_domain": "全般・設計",
                "expected_rules": ["core_rules"]
            }
        ]
        
        for test_case in test_cases:
            result = self._test_question_analysis(test_case)
            results["tests"].append(result)
            
            if result["passed"]:
                results["passed"] += 1
            else:
                results["failed"] += 1
                
        return results
    
    def _test_question_analysis(self, test_case: Dict) -> Dict:
        """個別の質問分析テスト"""
        question = test_case["question"]
        expected_domain = test_case["expected_domain"]
        expected_rules = test_case["expected_rules"]
        
        # キーワードベースの簡易分析
        detected_domain = self._analyze_question_domain(question)
        detected_rules = self._get_expected_rules(detected_domain)
        
        passed = (
            detected_domain == expected_domain and 
            set(detected_rules) == set(expected_rules)
        )
        
        return {
            "question": question,
            "expected_domain": expected_domain,
            "detected_domain": detected_domain,
            "expected_rules": expected_rules,
            "detected_rules": detected_rules,
            "passed": passed
        }
    
    def _analyze_question_domain(self, question: str) -> str:
        """質問から技術領域を判定"""
        question_lower = question.lower()
        
        # フロントエンド判定
        frontend_keywords = ["react", "vue", "angular", "svelte", "typescript", "javascript", "html", "css", "コンポーネント", "ui", "ux"]
        if any(keyword in question_lower for keyword in frontend_keywords):
            return "フロントエンド"
        
        # バックエンド判定
        backend_keywords = ["node.js", "python", "java", "go", "api", "サーバー", "データベース", "postgresql", "mysql", "mongodb"]
        if any(keyword in question_lower for keyword in backend_keywords):
            return "バックエンド"
        
        # テスト判定
        test_keywords = ["jest", "テスト", "tdd", "bdd", "ユニットテスト", "e2e", "統合テスト"]
        if any(keyword in question_lower for keyword in test_keywords):
            return "テスト"
        
        return "全般・設計"
    
    def _get_expected_rules(self, domain: str) -> List[str]:
        """技術領域から期待されるルールファイルを取得"""
        rule_mapping = {
            "フロントエンド": ["frontend_rules", "core_rules"],
            "バックエンド": ["backend_rules", "core_rules"],
            "テスト": ["testing_rules", "core_rules"],
            "全般・設計": ["core_rules"]
        }
        return rule_mapping.get(domain, ["core_rules"])
    
    def test_rule_files_exist(self) -> Dict:
        """ルールファイルの存在確認"""
        print("📁 ルールファイルの存在確認...")
        
        results = {
            "passed": 0,
            "failed": 0,
            "missing_files": []
        }
        
        expected_files = [
            "simple/core_rules.mdc",
            "simple/frontend_rules.mdc", 
            "simple/backend_rules.mdc",
            "simple/testing_rules.mdc",
            "simple/rule_selector.mdc",
            "defa/core_rules.mdc",
            "defa/frontend_rules.mdc",
            "defa/backend_rules.mdc", 
            "defa/testing_rules.mdc",
            "defa/rule_selector.mdc",
            "defa/defa_framework.mdc",
            "defa/error_handling_rules.mdc",
            "defa/prompt_templates.mdc",
            "defa/team_collaboration_rules.mdc"
        ]
        
        for file_path in expected_files:
            full_path = self.rules_dir / file_path
            if full_path.exists():
                results["passed"] += 1
            else:
                results["failed"] += 1
                results["missing_files"].append(file_path)
                
        return results
    
    def test_rule_content_quality(self) -> Dict:
        """ルールファイルの内容品質をテスト"""
        print("📝 ルールファイルの内容品質をチェック...")
        
        results = {
            "passed": 0,
            "failed": 0,
            "issues": []
        }
        
        # 全ての.mdcファイルをチェック
        for mdc_file in self.rules_dir.rglob("*.mdc"):
            try:
                content = mdc_file.read_text(encoding='utf-8')
                issues = self._check_content_quality(content, str(mdc_file))
                
                if not issues:
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                    results["issues"].extend(issues)
                    
            except Exception as e:
                results["failed"] += 1
                results["issues"].append(f"{mdc_file}: 読み込みエラー - {e}")
                
        return results
    
    def _check_content_quality(self, content: str, filename: str) -> List[str]:
        """ルールファイルの内容品質をチェック"""
        issues = []
        
        # 基本的な品質チェック
        if len(content.strip()) == 0:
            issues.append(f"{filename}: 空のファイル")
            
        if not content.startswith("#"):
            issues.append(f"{filename}: ヘッダーコメントが不足")
            
        # 日本語の使用確認
        if not re.search(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]', content):
            issues.append(f"{filename}: 日本語の説明が不足")
            
        # 構造的な要素の確認
        if not re.search(r'##\s*\[', content):
            issues.append(f"{filename}: セクション構造が不明確")
            
        return issues
    
    def run_all_tests(self) -> Dict:
        """全てのテストを実行"""
        print("🚀 ユーザールールの総合テストを開始...\n")
        
        all_results = {
            "rule_selector": self.test_rule_selector(),
            "file_existence": self.test_rule_files_exist(),
            "content_quality": self.test_rule_content_quality()
        }
        
        # 結果サマリー
        total_passed = sum(result["passed"] for result in all_results.values())
        total_failed = sum(result["failed"] for result in all_results.values())
        
        print(f"\n📊 テスト結果サマリー:")
        print(f"✅ 成功: {total_passed}")
        print(f"❌ 失敗: {total_failed}")
        print(f"📈 成功率: {total_passed/(total_passed+total_failed)*100:.1f}%")
        
        return all_results

def main():
    """メイン実行関数"""
    tester = RulesTester()
    results = tester.run_all_tests()
    
    # 詳細結果の表示
    print("\n📋 詳細結果:")
    
    for test_name, result in results.items():
        print(f"\n{test_name.upper()}:")
        if "tests" in result:
            for test in result["tests"]:
                status = "✅" if test["passed"] else "❌"
                print(f"  {status} {test['question']}")
                if not test["passed"]:
                    print(f"    期待: {test['expected_domain']} -> {test['expected_rules']}")
                    print(f"    実際: {test['detected_domain']} -> {test['detected_rules']}")
        
        if "missing_files" in result and result["missing_files"]:
            print(f"  ❌ 不足ファイル:")
            for file in result["missing_files"]:
                print(f"    - {file}")
                
        if "issues" in result and result["issues"]:
            print(f"  ❌ 品質問題:")
            for issue in result["issues"]:
                print(f"    - {issue}")

if __name__ == "__main__":
    main() 