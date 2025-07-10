#!/usr/bin/env python3
"""
Detailed Cursor User Rules Test Script
ユーザールールの詳細な機能テスト
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional

class DetailedRulesTester:
    def __init__(self, rules_dir: str = "rules"):
        self.rules_dir = Path(rules_dir)
        
    def test_rule_structure(self) -> Dict:
        """ルールファイルの構造をテスト"""
        print("🏗️ ルールファイルの構造テスト...")
        
        results = {
            "passed": 0,
            "failed": 0,
            "issues": []
        }
        
        for mdc_file in self.rules_dir.rglob("*.mdc"):
            try:
                content = mdc_file.read_text(encoding='utf-8')
                issues = self._check_rule_structure(content, str(mdc_file))
                
                if not issues:
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                    results["issues"].extend(issues)
                    
            except Exception as e:
                results["failed"] += 1
                results["issues"].append(f"{mdc_file}: 構造チェックエラー - {e}")
                
        return results
    
    def _check_rule_structure(self, content: str, filename: str) -> List[str]:
        """ルールファイルの構造をチェック"""
        issues = []
        
        # 必須セクションの確認
        required_sections = [
            r'#\s*Cursor\s+Rules',
            r'##\s*\[',
            r'Copyright',
            r'MIT\s+License'
        ]
        
        for section in required_sections:
            if not re.search(section, content, re.IGNORECASE):
                issues.append(f"{filename}: 必須セクション '{section}' が見つかりません")
        
        # セクション構造の確認
        sections = re.findall(r'##\s*\[([^\]]+)\]', content)
        if not sections:
            issues.append(f"{filename}: セクション定義が見つかりません")
        
        # コードブロックの確認
        code_blocks = re.findall(r'```[\w]*\n(.*?)\n```', content, re.DOTALL)
        if not code_blocks:
            issues.append(f"{filename}: コードブロックが見つかりません")
            
        return issues
    
    def test_rule_content_coverage(self) -> Dict:
        """ルール内容の網羅性をテスト"""
        print("📚 ルール内容の網羅性テスト...")
        
        results = {
            "passed": 0,
            "failed": 0,
            "coverage_report": {}
        }
        
        # 各ルールファイルの内容を分析
        for mdc_file in self.rules_dir.rglob("*.mdc"):
            try:
                content = mdc_file.read_text(encoding='utf-8')
                coverage = self._analyze_content_coverage(content, str(mdc_file))
                results["coverage_report"][str(mdc_file)] = coverage
                
                if coverage["score"] >= 0.7:  # 70%以上のカバレッジ
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                    
            except Exception as e:
                results["failed"] += 1
                results["coverage_report"][str(mdc_file)] = {"error": str(e)}
                
        return results
    
    def _analyze_content_coverage(self, content: str, filename: str) -> Dict:
        """ルール内容の網羅性を分析"""
        coverage = {
            "total_lines": len(content.split('\n')),
            "code_blocks": len(re.findall(r'```[\w]*\n(.*?)\n```', content, re.DOTALL)),
            "sections": len(re.findall(r'##\s*\[', content)),
            "examples": len(re.findall(r'例|example|サンプル', content, re.IGNORECASE)),
            "keywords": len(re.findall(r'[\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FAF]', content)),
            "score": 0
        }
        
        # スコア計算
        score = 0
        if coverage["total_lines"] > 50:
            score += 0.2
        if coverage["code_blocks"] > 0:
            score += 0.2
        if coverage["sections"] > 2:
            score += 0.2
        if coverage["examples"] > 0:
            score += 0.2
        if coverage["keywords"] > 100:
            score += 0.2
            
        coverage["score"] = score
        return coverage
    
    def test_rule_consistency(self) -> Dict:
        """ルール間の一貫性をテスト"""
        print("🔄 ルール間の一貫性テスト...")
        
        results = {
            "passed": 0,
            "failed": 0,
            "inconsistencies": []
        }
        
        # 全てのルールファイルを読み込み
        rule_contents = {}
        for mdc_file in self.rules_dir.rglob("*.mdc"):
            try:
                content = mdc_file.read_text(encoding='utf-8')
                rule_contents[str(mdc_file)] = content
            except Exception as e:
                results["inconsistencies"].append(f"{mdc_file}: 読み込みエラー - {e}")
        
        # 一貫性チェック
        inconsistencies = self._check_rule_consistency(rule_contents)
        results["inconsistencies"].extend(inconsistencies)
        
        if not inconsistencies:
            results["passed"] += 1
        else:
            results["failed"] += 1
            
        return results
    
    def _check_rule_consistency(self, rule_contents: Dict[str, str]) -> List[str]:
        """ルール間の一貫性をチェック"""
        inconsistencies = []
        
        # 共通のキーワードやパターンをチェック
        common_patterns = [
            r'Copyright.*2025.*Kentaro Kitagawa',
            r'MIT License',
            r'##\s*\[',
            r'```[\w]*\n'
        ]
        
        for pattern in common_patterns:
            files_with_pattern = []
            files_without_pattern = []
            
            for filename, content in rule_contents.items():
                if re.search(pattern, content, re.IGNORECASE):
                    files_with_pattern.append(filename)
                else:
                    files_without_pattern.append(filename)
            
            if files_without_pattern and files_with_pattern:
                inconsistencies.append(
                    f"パターン '{pattern}' の一貫性がありません: "
                    f"含むファイル {len(files_with_pattern)}個, "
                    f"含まないファイル {len(files_without_pattern)}個"
                )
        
        return inconsistencies
    
    def test_rule_effectiveness(self) -> Dict:
        """ルールの実効性をテスト"""
        print("🎯 ルールの実効性テスト...")
        
        results = {
            "passed": 0,
            "failed": 0,
            "effectiveness_scores": {}
        }
        
        # テストケースでルールの実効性を評価
        test_scenarios = [
            {
                "name": "フロントエンド開発",
                "question": "Reactでコンポーネントを作成する方法",
                "expected_rules": ["frontend_rules", "core_rules"]
            },
            {
                "name": "バックエンド開発", 
                "question": "Node.jsでAPIエンドポイントを実装する",
                "expected_rules": ["backend_rules", "core_rules"]
            },
            {
                "name": "テスト実装",
                "question": "Jestでユニットテストを書く",
                "expected_rules": ["testing_rules", "core_rules"]
            },
            {
                "name": "エラーハンドリング",
                "question": "エラー処理のベストプラクティス",
                "expected_rules": ["error_handling_rules", "core_rules"]
            }
        ]
        
        for scenario in test_scenarios:
            effectiveness = self._evaluate_rule_effectiveness(scenario)
            results["effectiveness_scores"][scenario["name"]] = effectiveness
            
            if effectiveness["score"] >= 0.8:
                results["passed"] += 1
            else:
                results["failed"] += 1
                
        return results
    
    def _evaluate_rule_effectiveness(self, scenario: Dict) -> Dict:
        """ルールの実効性を評価"""
        question = scenario["question"]
        expected_rules = scenario["expected_rules"]
        
        # 簡易的な実効性評価
        effectiveness = {
            "question": question,
            "expected_rules": expected_rules,
            "detected_rules": self._get_expected_rules(self._analyze_question_domain(question)),
            "score": 0
        }
        
        # スコア計算
        if set(effectiveness["detected_rules"]) == set(expected_rules):
            effectiveness["score"] = 1.0
        elif any(rule in effectiveness["detected_rules"] for rule in expected_rules):
            effectiveness["score"] = 0.5
        else:
            effectiveness["score"] = 0.0
            
        return effectiveness
    
    def _analyze_question_domain(self, question: str) -> str:
        """質問から技術領域を判定"""
        question_lower = question.lower()
        
        if any(keyword in question_lower for keyword in ["react", "vue", "angular", "コンポーネント", "ui"]):
            return "フロントエンド"
        elif any(keyword in question_lower for keyword in ["node.js", "api", "サーバー", "エンドポイント"]):
            return "バックエンド"
        elif any(keyword in question_lower for keyword in ["jest", "テスト", "ユニットテスト"]):
            return "テスト"
        elif any(keyword in question_lower for keyword in ["エラー", "エラーハンドリング"]):
            return "エラーハンドリング"
        
        return "全般・設計"
    
    def _get_expected_rules(self, domain: str) -> List[str]:
        """技術領域から期待されるルールファイルを取得"""
        rule_mapping = {
            "フロントエンド": ["frontend_rules", "core_rules"],
            "バックエンド": ["backend_rules", "core_rules"],
            "テスト": ["testing_rules", "core_rules"],
            "エラーハンドリング": ["error_handling_rules", "core_rules"],
            "全般・設計": ["core_rules"]
        }
        return rule_mapping.get(domain, ["core_rules"])
    
    def run_detailed_tests(self) -> Dict:
        """詳細テストを実行"""
        print("🚀 ユーザールールの詳細テストを開始...\n")
        
        all_results = {
            "structure": self.test_rule_structure(),
            "coverage": self.test_rule_content_coverage(),
            "consistency": self.test_rule_consistency(),
            "effectiveness": self.test_rule_effectiveness()
        }
        
        # 結果サマリー
        total_passed = sum(result["passed"] for result in all_results.values())
        total_failed = sum(result["failed"] for result in all_results.values())
        
        print(f"\n📊 詳細テスト結果サマリー:")
        print(f"✅ 成功: {total_passed}")
        print(f"❌ 失敗: {total_failed}")
        if total_passed + total_failed > 0:
            print(f"📈 成功率: {total_passed/(total_passed+total_failed)*100:.1f}%")
        
        return all_results

def main():
    """メイン実行関数"""
    tester = DetailedRulesTester()
    results = tester.run_detailed_tests()
    
    # 詳細結果の表示
    print("\n📋 詳細テスト結果:")
    
    for test_name, result in results.items():
        print(f"\n{test_name.upper()}:")
        
        if "issues" in result and result["issues"]:
            print(f"  ❌ 問題点:")
            for issue in result["issues"][:5]:  # 最初の5件のみ表示
                print(f"    - {issue}")
            if len(result["issues"]) > 5:
                print(f"    ... 他 {len(result['issues']) - 5} 件")
        
        if "coverage_report" in result:
            print(f"  📊 カバレッジレポート:")
            for filename, coverage in list(result["coverage_report"].items())[:3]:
                if "error" not in coverage:
                    print(f"    {filename}: スコア {coverage['score']:.2f}")
        
        if "effectiveness_scores" in result:
            print(f"  🎯 実効性スコア:")
            for scenario, score in result["effectiveness_scores"].items():
                print(f"    {scenario}: {score['score']:.2f}")

if __name__ == "__main__":
    main() 