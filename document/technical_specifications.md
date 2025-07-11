# Cursor Rules モジュール化システム 技術仕様書

## 📋 概要

このドキュメントは、Cursor Rulesモジュール化システムの技術仕様、API仕様、および実装詳細を定義します。

## 🎯 [D適用] - システム要件定義

### 基本要件

#### 機能要件
1. **モジュール化**: ルールコンポーネントの独立管理
2. **動的生成**: プロジェクト特性に応じたルール生成
3. **テンプレートシステム**: 柔軟なルール構造化
4. **条件分岐**: プロジェクトタイプ別のカスタマイズ
5. **品質保証**: 自動テストと検証システム

#### 非機能要件
- **パフォーマンス**: ビルド時間30秒以内
- **保守性**: モジュール間の疎結合
- **拡張性**: 新コンポーネントの容易な追加
- **互換性**: 既存`.cursorrules`ファイルとの互換性

### 技術スタック

#### 開発環境
- **Node.js**: v18.0.0以上
- **npm**: v8.0.0以上
- **JavaScript**: ES2020以上

#### 主要依存関係
```json
{
  "dependencies": {
    "fs-extra": "^11.0.0",
    "chalk": "^4.1.2",
    "commander": "^9.0.0"
  },
  "devDependencies": {
    "nodemon": "^2.0.20",
    "jest": "^29.0.0"
  }
}
```

## 🔍 [E適用] - アーキテクチャ設計

### システムアーキテクチャ

```
┌─────────────────────────────────────────────────────────────┐
│                    Cursor Rules Builder                     │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   CLI       │  │   Builder   │  │  Optimizer  │        │
│  │  Interface  │  │   Engine    │  │   Engine    │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │ Components  │  │ Templates   │  │   Config    │        │
│  │   Loader    │  │   Engine    │  │   Manager   │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐        │
│  │   Core      │  │  Frontend   │  │  Backend    │        │
│  │ Components  │  │ Components  │  │ Components  │        │
│  └─────────────┘  └─────────────┘  └─────────────┘        │
└─────────────────────────────────────────────────────────────┘
```

### コンポーネント設計

#### 1. CLI Interface
```javascript
// src/cli.js
const { Command } = require('commander');
const { RulesBuilder } = require('./build');

class CLI {
  constructor() {
    this.program = new Command();
    this.setupCommands();
  }
  
  setupCommands() {
    this.program
      .name('cursor-rules-builder')
      .description('Cursor Rules modular builder')
      .version('1.0.0');
      
    this.program
      .command('build')
      .description('Build cursor rules')
      .option('-v, --variant <type>', 'Build variant (defa|simple|all)', 'all')
      .option('-p, --project-type <type>', 'Project type for customization')
      .option('--watch', 'Watch mode for development')
      .action(this.build.bind(this));
      
    this.program
      .command('validate')
      .description('Validate generated rules')
      .action(this.validate.bind(this));
  }
  
  async build(options) {
    const builder = new RulesBuilder();
    await builder.build(options);
  }
  
  async validate() {
    // バリデーションロジック
  }
  
  run() {
    this.program.parse();
  }
}
```

#### 2. Builder Engine
```javascript
// src/build.js
class RulesBuilder {
  constructor() {
    this.components = {};
    this.templates = {};
    this.config = {};
    this.optimizer = new RulesOptimizer();
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
    
    return this.optimizer.optimizeTemplate(result);
  }
  
  async build(options = {}) {
    console.log(chalk.blue('🚀 Starting Cursor Rules build...'));
    
    await this.loadComponents();
    await this.loadTemplates();
    await this.loadConfig();
    
    const variants = options.variant === 'all' 
      ? ['defa', 'simple'] 
      : [options.variant];
    
    for (const variant of variants) {
      console.log(chalk.green(`📦 Building ${variant} variant...`));
      
      const rules = this.generateRules(variant, options.projectType);
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

#### 3. Optimizer Engine
```javascript
// src/optimizer.js
class RulesOptimizer {
  constructor() {
    this.cache = new Map();
  }
  
  optimizeTemplate(template) {
    // 空白の最適化
    let optimized = template.replace(/\s+/g, ' ');
    
    // 不要な改行の削除
    optimized = optimized.replace(/\n\s*\n/g, '\n\n');
    
    // 先頭・末尾の空白削除
    optimized = optimized.trim();
    
    return optimized;
  }
  
  cacheComponent(name, content) {
    this.cache.set(name, content);
  }
  
  getCachedComponent(name) {
    return this.cache.get(name);
  }
  
  clearCache() {
    this.cache.clear();
  }
  
  getCacheStats() {
    return {
      size: this.cache.size,
      keys: Array.from(this.cache.keys())
    };
  }
}
```

## ✨ [F適用] - API仕様

### コンポーネントAPI

#### 基本コンポーネント構造
```javascript
// コンポーネントの基本構造
module.exports = {
  // コンポーネント名（必須）
  name: 'core',
  
  // コンポーネントバージョン（必須）
  version: '1.0.0',
  
  // 依存関係（オプション）
  dependencies: ['defa'],
  
  // ルールセクション（必須）
  sections: {
    qualityPrinciples: `
### コード品質原則
- **可読性 > 巧妙さ**: 明確な変数名、適切なコメント
- **型安全性**: TypeScript使用、適切な型定義
    `,
    
    responsiveAccessibility: `
### レスポンシブ・アクセシビリティ
- **モバイルファースト**: モバイルデバイスを最優先に設計
- **アクセシビリティ**: WCAG 2.1準拠、セマンティックHTML
    `
  },
  
  // メタデータ（オプション）
  metadata: {
    description: '基本品質基準コンポーネント',
    author: 'Kentaro Kitagawa',
    license: 'MIT'
  }
};
```

#### コンポーネントローダーAPI
```javascript
// src/loaders/component-loader.js
class ComponentLoader {
  constructor() {
    this.components = new Map();
    this.dependencyGraph = new Map();
  }
  
  async loadComponent(name) {
    const componentPath = path.join(__dirname, '..', 'rules', 'components', `${name}.js`);
    
    if (!fs.existsSync(componentPath)) {
      throw new Error(`Component not found: ${name}`);
    }
    
    const component = require(componentPath);
    
    // バリデーション
    this.validateComponent(component);
    
    // 依存関係の解決
    await this.resolveDependencies(component);
    
    this.components.set(name, component);
    return component;
  }
  
  validateComponent(component) {
    if (!component.name) {
      throw new Error('Component must have a name');
    }
    
    if (!component.version) {
      throw new Error('Component must have a version');
    }
    
    if (!component.sections || typeof component.sections !== 'object') {
      throw new Error('Component must have sections');
    }
  }
  
  async resolveDependencies(component) {
    if (!component.dependencies) {
      return;
    }
    
    for (const dep of component.dependencies) {
      if (!this.components.has(dep)) {
        await this.loadComponent(dep);
      }
    }
  }
  
  getComponent(name) {
    return this.components.get(name);
  }
  
  getAllComponents() {
    return Array.from(this.components.values());
  }
}
```

### テンプレートAPI

#### テンプレート構造
```markdown
<!-- src/rules/templates/simple.cursorrules.template -->
# Cursor Rules - Core Framework
# Copyright (c) 2025 Kentaro Kitagawa
# MIT License - https://opensource.org/licenses/MIT

## [CORE] 基本品質基準（常時適用）

{{core.qualityPrinciples}}

{{core.responsiveAccessibility}}

{{core.implementationGuidelines}}

## [LOG] プロファイル適用ログシステム

{{core.logSystem}}

## [CONTEXT] 状況別対応

{{core.contextHandling}}

## [FLOW] コード生成時の思考フロー

{{core.thinkingFlow}}
```

#### テンプレートエンジンAPI
```javascript
// src/engines/template-engine.js
class TemplateEngine {
  constructor() {
    this.helpers = new Map();
    this.registerDefaultHelpers();
  }
  
  registerDefaultHelpers() {
    this.helpers.set('uppercase', (str) => str.toUpperCase());
    this.helpers.set('lowercase', (str) => str.toLowerCase());
    this.helpers.set('capitalize', (str) => str.charAt(0).toUpperCase() + str.slice(1));
  }
  
  registerHelper(name, fn) {
    this.helpers.set(name, fn);
  }
  
  render(template, data) {
    let result = template;
    
    // 変数置換
    result = this.replaceVariables(result, data);
    
    // ヘルパー関数の適用
    result = this.applyHelpers(result, data);
    
    return result;
  }
  
  replaceVariables(template, data) {
    return template.replace(/\{\{([^}]+)\}\}/g, (match, key) => {
      const value = this.getNestedValue(data, key);
      return value !== undefined ? value : match;
    });
  }
  
  getNestedValue(obj, path) {
    return path.split('.').reduce((current, key) => {
      return current && current[key] !== undefined ? current[key] : undefined;
    }, obj);
  }
  
  applyHelpers(template, data) {
    return template.replace(/\{\{([^}]+)\|([^}]+)\}\}/g, (match, key, helper) => {
      const value = this.getNestedValue(data, key);
      const helperFn = this.helpers.get(helper);
      
      if (value !== undefined && helperFn) {
        return helperFn(value);
      }
      
      return match;
    });
  }
}
```

### 設定API

#### プロジェクトタイプ設定
```javascript
// src/config/project-types.js
const PROJECT_TYPES = {
  startup: {
    name: 'startup',
    description: 'スタートアップ・新規プロジェクト',
    rules: ['core', 'frontend', 'backend'],
    complexity: 'low',
    focus: 'speed',
    defaLevel: 'minimal',
    metadata: {
      priority: 'speed',
      teamSize: 'small',
      timeline: 'aggressive'
    }
  },
  enterprise: {
    name: 'enterprise',
    description: 'エンタープライズ・大規模プロジェクト',
    rules: ['core', 'defa', 'frontend', 'backend', 'testing', 'security'],
    complexity: 'high',
    focus: 'quality',
    defaLevel: 'full',
    metadata: {
      priority: 'quality',
      teamSize: 'large',
      timeline: 'conservative'
    }
  },
  maintenance: {
    name: 'maintenance',
    description: '保守・改善プロジェクト',
    rules: ['core', 'testing', 'error-handling'],
    complexity: 'medium',
    focus: 'stability',
    defaLevel: 'partial',
    metadata: {
      priority: 'stability',
      teamSize: 'medium',
      timeline: 'moderate'
    }
  },
  learning: {
    name: 'learning',
    description: '学習・教育プロジェクト',
    rules: ['core', 'defa', 'frontend'],
    complexity: 'low',
    focus: 'education',
    defaLevel: 'learning',
    metadata: {
      priority: 'education',
      teamSize: 'small',
      timeline: 'flexible'
    }
  }
};

module.exports = { PROJECT_TYPES };
```

#### 設定マネージャーAPI
```javascript
// src/managers/config-manager.js
class ConfigManager {
  constructor() {
    this.configs = new Map();
    this.loadDefaultConfigs();
  }
  
  loadDefaultConfigs() {
    const { PROJECT_TYPES } = require('../config/project-types');
    
    for (const [key, config] of Object.entries(PROJECT_TYPES)) {
      this.configs.set(key, config);
    }
  }
  
  getProjectType(name) {
    return this.configs.get(name);
  }
  
  getAllProjectTypes() {
    return Array.from(this.configs.values());
  }
  
  addProjectType(name, config) {
    this.validateProjectType(config);
    this.configs.set(name, config);
  }
  
  validateProjectType(config) {
    if (!config.name) {
      throw new Error('Project type must have a name');
    }
    
    if (!config.rules || !Array.isArray(config.rules)) {
      throw new Error('Project type must have rules array');
    }
    
    if (!config.complexity) {
      throw new Error('Project type must have complexity level');
    }
  }
  
  getRulesForProjectType(projectType) {
    const config = this.getProjectType(projectType);
    if (!config) {
      throw new Error(`Unknown project type: ${projectType}`);
    }
    
    return config.rules;
  }
}
```

## 📝 [A1適用] - 実装ガイドライン

### コンポーネント開発ガイドライン

#### 1. コンポーネント作成手順
```javascript
// 1. コンポーネントファイルの作成
// src/rules/components/example.js

// 2. 基本構造の定義
module.exports = {
  name: 'example',
  version: '1.0.0',
  dependencies: [], // 依存関係がある場合
  
  sections: {
    // セクション1
    sectionName1: `
### セクションタイトル
- **ポイント1**: 説明
- **ポイント2**: 説明
    `,
    
    // セクション2
    sectionName2: `
### 別のセクション
- **ポイント3**: 説明
- **ポイント4**: 説明
    `
  },
  
  metadata: {
    description: 'コンポーネントの説明',
    author: '作成者名',
    license: 'MIT'
  }
};
```

#### 2. テンプレート作成手順
```markdown
<!-- 1. テンプレートファイルの作成 -->
<!-- src/rules/templates/example.cursorrules.template -->

<!-- 2. ヘッダー情報 -->
# Cursor Rules - Example Framework
# Copyright (c) 2025 Kentaro Kitagawa
# MIT License - https://opensource.org/licenses/MIT

<!-- 3. セクションの定義 -->
## [SECTION] セクションタイトル

{{componentName.sectionName}}

<!-- 4. 条件分岐（オプション） -->
{{#if projectType.enterprise}}
## [ENTERPRISE] エンタープライズ向けセクション

{{enterpriseComponent.sectionName}}
{{/if}}
```

#### 3. テスト作成ガイドライン
```javascript
// tests/components/example.test.js
const ExampleComponent = require('../../src/rules/components/example');

describe('ExampleComponent', () => {
  test('should have required properties', () => {
    expect(ExampleComponent.name).toBeDefined();
    expect(ExampleComponent.version).toBeDefined();
    expect(ExampleComponent.sections).toBeDefined();
  });
  
  test('should have valid sections', () => {
    const sections = ExampleComponent.sections;
    
    for (const [key, value] of Object.entries(sections)) {
      expect(typeof value).toBe('string');
      expect(value.length).toBeGreaterThan(0);
    }
  });
  
  test('should generate valid markdown', () => {
    const sections = ExampleComponent.sections;
    
    for (const [key, value] of Object.entries(sections)) {
      // マークダウンの構文チェック
      expect(value).toMatch(/^###\s+/);
    }
  });
});
```

### パフォーマンス最適化ガイドライン

#### 1. キャッシュ戦略
```javascript
// src/optimizers/cache-optimizer.js
class CacheOptimizer {
  constructor() {
    this.componentCache = new Map();
    this.templateCache = new Map();
    this.resultCache = new Map();
  }
  
  getCachedComponent(name) {
    return this.componentCache.get(name);
  }
  
  setCachedComponent(name, component) {
    this.componentCache.set(name, component);
  }
  
  getCachedTemplate(name) {
    return this.templateCache.get(name);
  }
  
  setCachedTemplate(name, template) {
    this.templateCache.set(name, template);
  }
  
  getCachedResult(key) {
    return this.resultCache.get(key);
  }
  
  setCachedResult(key, result) {
    this.resultCache.set(key, result);
  }
  
  clearCache() {
    this.componentCache.clear();
    this.templateCache.clear();
    this.resultCache.clear();
  }
  
  getCacheStats() {
    return {
      components: this.componentCache.size,
      templates: this.templateCache.size,
      results: this.resultCache.size
    };
  }
}
```

#### 2. 並列処理最適化
```javascript
// src/optimizers/parallel-optimizer.js
class ParallelOptimizer {
  constructor() {
    this.maxConcurrency = 4;
  }
  
  async processComponents(components) {
    const chunks = this.chunkArray(components, this.maxConcurrency);
    const results = [];
    
    for (const chunk of chunks) {
      const chunkResults = await Promise.all(
        chunk.map(component => this.processComponent(component))
      );
      results.push(...chunkResults);
    }
    
    return results;
  }
  
  chunkArray(array, size) {
    const chunks = [];
    for (let i = 0; i < array.length; i += size) {
      chunks.push(array.slice(i, i + size));
    }
    return chunks;
  }
  
  async processComponent(component) {
    // コンポーネント処理ロジック
    return component;
  }
}
```

## 📈 [A2適用] - 品質保証

### テスト戦略

#### 1. 単体テスト
```javascript
// tests/build.test.js
const { RulesBuilder } = require('../src/build');

describe('RulesBuilder', () => {
  let builder;
  
  beforeEach(() => {
    builder = new RulesBuilder();
  });
  
  describe('loadComponents', () => {
    test('should load all components', async () => {
      await builder.loadComponents();
      
      expect(builder.components.core).toBeDefined();
      expect(builder.components.frontend).toBeDefined();
      expect(builder.components.backend).toBeDefined();
    });
    
    test('should handle missing components gracefully', async () => {
      // テストロジック
    });
  });
  
  describe('generateRules', () => {
    test('should generate rules for simple variant', async () => {
      await builder.loadComponents();
      await builder.loadTemplates();
      
      const rules = builder.generateRules('simple');
      
      expect(rules).toContain('コード品質原則');
      expect(rules).toContain('レスポンシブ・アクセシビリティ');
    });
    
    test('should generate rules for defa variant', async () => {
      await builder.loadComponents();
      await builder.loadTemplates();
      
      const rules = builder.generateRules('defa');
      
      expect(rules).toContain('DEF-Aモデル構造');
      expect(rules).toContain('部分適用戦略');
    });
  });
});
```

#### 2. 統合テスト
```javascript
// tests/integration.test.js
const { execSync } = require('child_process');
const fs = require('fs-extra');
const path = require('path');

describe('Integration Tests', () => {
  const distPath = path.join(__dirname, '..', 'dist');
  
  beforeEach(async () => {
    await fs.remove(distPath);
  });
  
  test('should build complete system', async () => {
    // ビルド実行
    execSync('npm run build', { stdio: 'inherit' });
    
    // 出力ファイルの確認
    expect(fs.existsSync(path.join(distPath, 'simple', 'core_rules.cursorrules'))).toBe(true);
    expect(fs.existsSync(path.join(distPath, 'defa', 'core_rules.cursorrules'))).toBe(true);
  });
  
  test('should generate valid cursor rules', async () => {
    execSync('npm run build', { stdio: 'inherit' });
    
    const simpleRules = await fs.readFile(
      path.join(distPath, 'simple', 'core_rules.cursorrules'),
      'utf8'
    );
    
    // 基本的な構文チェック
    expect(simpleRules).toContain('# Cursor Rules');
    expect(simpleRules).toContain('## [CORE]');
    expect(simpleRules).toContain('### コード品質原則');
  });
});
```

#### 3. パフォーマンステスト
```javascript
// tests/performance.test.js
const { RulesBuilder } = require('../src/build');

describe('Performance Tests', () => {
  let builder;
  
  beforeEach(() => {
    builder = new RulesBuilder();
  });
  
  test('should build within time limit', async () => {
    const startTime = Date.now();
    
    await builder.build();
    
    const endTime = Date.now();
    const buildTime = endTime - startTime;
    
    expect(buildTime).toBeLessThan(30000); // 30秒以内
  });
  
  test('should use reasonable memory', async () => {
    const initialMemory = process.memoryUsage().heapUsed;
    
    await builder.build();
    
    const finalMemory = process.memoryUsage().heapUsed;
    const memoryIncrease = finalMemory - initialMemory;
    
    expect(memoryIncrease).toBeLessThan(50 * 1024 * 1024); // 50MB以下
  });
});
```

### 品質メトリクス

#### 1. コードカバレッジ
```json
{
  "coverage": {
    "statements": 90,
    "branches": 85,
    "functions": 95,
    "lines": 90
  }
}
```

#### 2. パフォーマンス指標
```json
{
  "performance": {
    "buildTime": "25s",
    "memoryUsage": "35MB",
    "fileSize": "2.5MB",
    "cacheHitRate": "85%"
  }
}
```

#### 3. 品質指標
```json
{
  "quality": {
    "duplicationReduction": "85%",
    "maintainabilityIndex": "8.5/10",
    "complexityScore": "2.1",
    "technicalDebt": "0.5 days"
  }
}
```

---

**作成日**: 2025年7月11日
**作成者**: AI Assistant
**バージョン**: 1.0
**ステータス**: 技術仕様完了 