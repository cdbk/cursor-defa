# Cursor Rules モジュール化実装ロードマップ

## 📋 概要

このドキュメントは、Cursor Rulesのモジュール化システム実装に向けた詳細なロードマップとアクションプランを提供します。

## 🎯 [D適用] - 実装目標の定義

### 主要目標
1. **重複コードの削減**: 現在の`/defa`と`/simple`間の重複を最小化
2. **保守性の向上**: モジュール化による変更の影響範囲の明確化
3. **拡張性の確保**: 新ルール追加の容易性とプロジェクト特性に応じたカスタマイズ
4. **品質保証**: 自動化されたテストと検証システムの構築

### 成功指標
- 重複コードの削減率: 80%以上
- 新ルール追加時間: 50%短縮
- ビルド時間: 30秒以内
- テストカバレッジ: 90%以上

## 🔍 [E適用] - 実装戦略の分析

### 段階的実装アプローチ

#### フェーズ1: 基盤構築（週1-2）
**目標**: 基本的なモジュール化システムの構築

**主要タスク**:
- [ ] プロジェクト構造の設計
- [ ] 基本的なビルドスクリプトの作成
- [ ] 既存ルールの分析とコンポーネント化計画
- [ ] テンプレートシステムの設計

**成果物**:
- プロジェクト構造図
- 基本的なビルドスクリプト
- コンポーネント化計画書

#### フェーズ2: コアコンポーネント実装（週3-4）
**目標**: 主要ルールのコンポーネント化

**主要タスク**:
- [ ] `core_rules`のコンポーネント化
- [ ] `frontend_rules`のコンポーネント化
- [ ] `backend_rules`のコンポーネント化
- [ ] 基本的なテンプレートの作成

**成果物**:
- コアコンポーネント（core.js, frontend.js, backend.js）
- 基本的なテンプレートファイル
- 動作確認済みのビルドシステム

#### フェーズ3: 高度なコンポーネント実装（週5-6）
**目標**: 複雑なルールのコンポーネント化

**主要タスク**:
- [ ] `defa_framework`のコンポーネント化
- [ ] `testing_rules`のコンポーネント化
- [ ] `error_handling_rules`のコンポーネント化
- [ ] 条件分岐システムの実装

**成果物**:
- 高度なコンポーネント（defa.js, testing.js, error-handling.js）
- 条件分岐システム
- プロジェクトタイプ別設定

#### フェーズ4: 統合と最適化（週7-8）
**目標**: システムの統合とパフォーマンス最適化

**主要タスク**:
- [ ] 全コンポーネントの統合
- [ ] パフォーマンス最適化
- [ ] テストシステムの構築
- [ ] ドキュメントの整備

**成果物**:
- 完全なモジュール化システム
- 自動テストシステム
- 包括的なドキュメント

## ✨ [F適用] - 実装計画の統合

### 詳細な実装計画

#### 週1: プロジェクト基盤構築

**Day 1-2: プロジェクト構造設計**
```bash
# プロジェクト構造の作成
mkdir -p src/rules/{components,templates,config}
mkdir -p dist/{defa,simple}
mkdir -p tests
mkdir -p docs
```

**Day 3-4: 基本的なビルドスクリプト**
```javascript
// src/build.js (基本版)
const fs = require('fs-extra');
const path = require('path');

class BasicRulesBuilder {
  constructor() {
    this.components = {};
    this.templates = {};
  }
  
  async loadComponents() {
    // コンポーネント読み込みロジック
  }
  
  async build() {
    console.log('🚀 Starting basic build...');
    // 基本的なビルドロジック
  }
}
```

**Day 5: 既存ルール分析**
- 重複部分の特定
- コンポーネント化対象の選定
- 依存関係の分析

#### 週2: コアコンポーネント実装

**Day 1-2: core.js実装**
```javascript
// src/rules/components/core.js
module.exports = {
  qualityPrinciples: `
### コード品質原則
- **可読性 > 巧妙さ**: 明確な変数名、適切なコメント
- **型安全性**: TypeScript使用、適切な型定義
- **エラーハンドリング**: 適切な例外処理、ユーザーフレンドリーなエラーメッセージ
- **セキュリティ**: 入力検証、XSS対策、SQLインジェクション対策
  `,
  
  responsiveAccessibility: `
### レスポンシブ・アクセシビリティ
- **モバイルファースト**: モバイルデバイスを最優先に設計
- **アクセシビリティ**: WCAG 2.1準拠、セマンティックHTML
- **パフォーマンス**: Core Web Vitals意識、不要な依存関係回避
  `,
  
  implementationGuidelines: `
### 実装方針
- **段階的実装**: 小さなステップで確実に進める
- **検証可能**: テスト可能な形で実装
- **保守性**: 将来の変更に耐える設計
- **日付管理**: システム日付の自動取得・検証による正確性確保
  `
};
```

**Day 3-4: frontend.js実装**
```javascript
// src/rules/components/frontend.js
module.exports = {
  reactGuidelines: `
### React開発ガイドライン
- **関数コンポーネント**: Hooks使用、クラスコンポーネントは非推奨
- **型安全性**: TypeScript使用、適切な型定義
- **状態管理**: 適切な状態管理ライブラリの選択
  `,
  
  stylingGuidelines: `
### スタイリングガイドライン
- **CSS-in-JS**: styled-componentsまたはemotion使用
- **レスポンシブ**: モバイルファーストアプローチ
- **アクセシビリティ**: セマンティックHTML、ARIA属性
  `
};
```

**Day 5: 基本的なテンプレート作成**
```markdown
<!-- src/rules/templates/simple.cursorrules.template -->
# Cursor Rules - Core Framework
# Copyright (c) 2025 Kentaro Kitagawa
# MIT License - https://opensource.org/licenses/MIT

## [CORE] 基本品質基準（常時適用）

{{qualityPrinciples}}

{{responsiveAccessibility}}

{{implementationGuidelines}}

## [LOG] プロファイル適用ログシステム

{{logSystem}}

## [CONTEXT] 状況別対応

{{contextHandling}}

## [FLOW] コード生成時の思考フロー

{{thinkingFlow}}
```

#### 週3: 高度なコンポーネント実装

**Day 1-2: defa.js実装**
```javascript
// src/rules/components/defa.js
module.exports = {
  defaModel: `
## [DEF-A] メタ認知思考フレームワーク（コンパクト版）

### DEF-Aモデル構造
\`\`\`
🎯 [D適用] - Define段階：問題設定・多次元定義
🔍 [E適用] - Explore段階：多視点分析・深層探求
✨ [F適用] - Formulate段階：統合・構造化・最適化
📝 [A1適用] - Act/Apply段階：実行・適用
📈 [A2適用] - Assess/Adjust段階：評価・調整
\`\`\`
  `,
  
  partialApplication: `
### DEF-A部分適用戦略（効率性重視）
- **完全DEF-A適用**: 戦略的質問（Define→Explore→Formulate→Act→Assess）
- **部分DEF-A適用**: 技術実装質問（Formulate→Act→Assess）
- **最小DEF-A適用**: 緊急対応（Actのみ）
- **学習支援適用**: 教育・理解（Explore→Act）
  `
};
```

**Day 3-4: 条件分岐システム実装**
```javascript
// src/config/project-types.js
const PROJECT_TYPES = {
  startup: {
    rules: ['core', 'frontend', 'backend'],
    complexity: 'low',
    focus: 'speed',
    defaLevel: 'minimal'
  },
  enterprise: {
    rules: ['core', 'defa', 'frontend', 'backend', 'testing', 'security'],
    complexity: 'high',
    focus: 'quality',
    defaLevel: 'full'
  },
  maintenance: {
    rules: ['core', 'testing', 'error-handling'],
    complexity: 'medium',
    focus: 'stability',
    defaLevel: 'partial'
  },
  learning: {
    rules: ['core', 'defa', 'frontend'],
    complexity: 'low',
    focus: 'education',
    defaLevel: 'learning'
  }
};

module.exports = { PROJECT_TYPES };
```

**Day 5: テストシステム構築**
```javascript
// tests/build.test.js
const { RulesBuilder } = require('../src/build');

describe('RulesBuilder', () => {
  let builder;
  
  beforeEach(() => {
    builder = new RulesBuilder();
  });
  
  test('should load components correctly', async () => {
    await builder.loadComponents();
    expect(builder.components.core).toBeDefined();
    expect(builder.components.frontend).toBeDefined();
  });
  
  test('should generate rules for startup project', async () => {
    const rules = await builder.generateRules('simple', 'startup');
    expect(rules).toContain('コード品質原則');
    expect(rules).not.toContain('DEF-Aモデル構造');
  });
});
```

#### 週4: 統合と最適化

**Day 1-2: 全コンポーネント統合**
```javascript
// src/build.js (完全版)
const fs = require('fs-extra');
const path = require('path');
const chalk = require('chalk');
const { Command } = require('commander');

class RulesBuilder {
  constructor() {
    this.components = {};
    this.templates = {};
    this.config = {};
  }
  
  async loadComponents() {
    const componentsDir = path.join(__dirname, 'rules', 'components');
    const files = await fs.readdir(componentsDir);
    
    for (const file of files) {
      if (file.endsWith('.js')) {
        const name = path.basename(file, '.js');
        this.components[name] = require(path.join(componentsDir, file));
      }
    }
  }
  
  async loadTemplates() {
    const templatesDir = path.join(__dirname, 'rules', 'templates');
    const files = await fs.readdir(templatesDir);
    
    for (const file of files) {
      if (file.endsWith('.template')) {
        const name = path.basename(file, '.cursorrules.template');
        this.templates[name] = await fs.readFile(
          path.join(templatesDir, file), 
          'utf8'
        );
      }
    }
  }
  
  generateRules(variant, projectType = null) {
    const template = this.templates[variant];
    if (!template) {
      throw new Error(`Template not found for variant: ${variant}`);
    }
    
    const selectedRules = projectType 
      ? this.selectRulesForProject(projectType)
      : this.getDefaultRules(variant);
    
    let result = template;
    for (const [ruleName, ruleContent] of Object.entries(selectedRules)) {
      const placeholder = `{{${ruleName}}}`;
      result = result.replace(new RegExp(placeholder, 'g'), ruleContent);
    }
    
    return result;
  }
  
  async build() {
    console.log(chalk.blue('🚀 Starting Cursor Rules build...'));
    
    await this.loadComponents();
    await this.loadTemplates();
    await this.loadConfig();
    
    const variants = ['defa', 'simple'];
    
    for (const variant of variants) {
      console.log(chalk.green(`📦 Building ${variant} variant...`));
      
      const rules = this.generateRules(variant);
      const outputDir = path.join(__dirname, '..', 'dist', variant);
      
      await fs.ensureDir(outputDir);
      await fs.writeFile(
        path.join(outputDir, 'core_rules.cursorrules'),
        rules
      );
      
      console.log(chalk.green(`✅ ${variant} variant built successfully`));
    }
    
    console.log(chalk.blue('🎉 Build completed!'));
  }
}
```

**Day 3-4: パフォーマンス最適化**
```javascript
// src/optimizer.js
class RulesOptimizer {
  constructor() {
    this.cache = new Map();
  }
  
  optimizeTemplate(template) {
    // テンプレートの最適化
    return template.replace(/\s+/g, ' ').trim();
  }
  
  cacheComponent(name, content) {
    this.cache.set(name, content);
  }
  
  getCachedComponent(name) {
    return this.cache.get(name);
  }
}
```

**Day 5: ドキュメント整備**
- API仕様書の作成
- 使用方法ガイドの作成
- トラブルシューティングガイドの作成

## 📝 [A1適用] - 具体的なアクション

### 即座に開始可能なタスク

#### 1. プロジェクト初期化
```bash
# プロジェクトディレクトリの作成
mkdir -p cursor-rules-modular
cd cursor-rules-modular

# package.jsonの初期化
npm init -y

# 必要な依存関係のインストール
npm install fs-extra chalk commander
npm install --save-dev nodemon jest
```

#### 2. 基本的なディレクトリ構造作成
```bash
# ディレクトリ構造の作成
mkdir -p src/rules/{components,templates,config}
mkdir -p dist/{defa,simple}
mkdir -p tests
mkdir -p docs
```

#### 3. 最初のコンポーネント作成
```javascript
// src/rules/components/core.js
module.exports = {
  qualityPrinciples: `
### コード品質原則
- **可読性 > 巧妙さ**: 明確な変数名、適切なコメント
- **型安全性**: TypeScript使用、適切な型定義
- **エラーハンドリング**: 適切な例外処理、ユーザーフレンドリーなエラーメッセージ
- **セキュリティ**: 入力検証、XSS対策、SQLインジェクション対策
  `
};
```

#### 4. 基本的なビルドスクリプト作成
```javascript
// src/build.js
const fs = require('fs-extra');
const path = require('path');

async function buildRules() {
  console.log('🚀 Starting build...');
  
  // コンポーネントの読み込み
  const core = require('./rules/components/core.js');
  
  // 基本的なルール生成
  const rules = `# Cursor Rules - Core Framework

## [CORE] 基本品質基準（常時適用）

${core.qualityPrinciples}
`;
  
  // 出力
  await fs.ensureDir('./dist/simple');
  await fs.writeFile('./dist/simple/core_rules.cursorrules', rules);
  
  console.log('✅ Build completed!');
}

buildRules().catch(console.error);
```

### 週次マイルストーン

#### 週1マイルストーン
- [ ] プロジェクト基盤の構築完了
- [ ] 基本的なビルドスクリプトの動作確認
- [ ] 最初のコンポーネント（core.js）の実装完了

#### 週2マイルストーン
- [ ] 主要コンポーネント（frontend.js, backend.js）の実装完了
- [ ] 基本的なテンプレートシステムの動作確認
- [ ] 単純なルール生成の成功

#### 週3マイルストーン
- [ ] 高度なコンポーネント（defa.js, testing.js）の実装完了
- [ ] 条件分岐システムの実装完了
- [ ] 基本的なテストシステムの構築完了

#### 週4マイルストーン
- [ ] 全システムの統合完了
- [ ] パフォーマンス最適化の完了
- [ ] 包括的なドキュメントの整備完了

## 📈 [A2適用] - 評価と調整

### 成功指標の測定

#### 技術的指標
- **ビルド時間**: 目標30秒以内
- **テストカバレッジ**: 目標90%以上
- **エラー率**: 目標5%以下
- **パフォーマンス**: メモリ使用量50MB以下

#### 品質指標
- **重複コード削減率**: 目標80%以上
- **新ルール追加時間**: 目標50%短縮
- **保守性スコア**: 目標8/10以上
- **ユーザー満足度**: 目標9/10以上

### 継続的改善計画

#### 短期的改善（1-3ヶ月）
- モジュール化システムの安定化
- パフォーマンスの最適化
- ユーザーフィードバックの収集と反映

#### 中期的改善（3-6ヶ月）
- 高度なカスタマイズ機能の追加
- 自動化の強化
- コミュニティ機能の追加

#### 長期的改善（6ヶ月以上）
- AI支援機能の統合
- 機械学習による最適化
- エコシステムの拡張

### リスク管理

#### 技術的リスク
- **Cursor制約**: 静的ファイル生成の制限
- **互換性**: 既存ルールファイルとの互換性維持
- **パフォーマンス**: ビルド時間の増加

#### 対策
- 段階的移行によるリスク軽減
- 包括的なテストによる品質保証
- パフォーマンス監視と最適化

---

**作成日**: 2025年7月11日
**作成者**: AI Assistant
**バージョン**: 1.0
**ステータス**: 実装計画完了 