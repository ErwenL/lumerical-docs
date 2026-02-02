# `copyopt` - 复制优化设置

## 概述

`copyopt` 命令用于复制优化设置和状态。在 Lumerical 的优化工具中，该命令允许用户复制优化对象的配置、参数、约束条件以及当前优化状态，便于创建相似的优化任务、备份优化设置或在不同项目间迁移优化配置。

该命令特别适用于需要运行多个相似优化、比较不同优化算法或保存优化进度的情况。

## 语法

### LSF 语法
```lumerical
copyopt(source_optimization);                     # 复制优化设置
copyopt(source_optimization, destination_name);   # 复制优化设置并指定新名称
```

### Python API
```python
session.copyopt(source_optimization)                     # 复制优化设置
session.copyopt(source_optimization, destination_name)   # 复制优化设置并指定新名称
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `source_optimization` | string | 要复制的源优化对象的名称。 | 是 |
| `destination_name` | string | 新优化对象的名称。如果省略，Lumerical 会自动生成一个名称。 | 可选 |

## 配置属性

`copyopt` 命令会复制优化对象的所有配置属性，包括：

| 属性类别 | 包含内容 |
|----------|----------|
| **优化算法设置** | 算法类型（梯度、随机、遗传算法等）、收敛条件、最大迭代次数 |
| **优化参数** | 设计变量、初始值、上下界、步长 |
| **目标函数** | 目标定义、权重、归一化方法 |
| **约束条件** | 线性/非线性约束、等式/不等式约束 |
| **状态信息** | 当前迭代次数、最佳结果、收敛历史 |
| **高级设置** | 并行计算选项、灵敏度分析设置、网格更新设置 |

## 返回值

`copyopt` 命令没有返回值。成功执行后，会创建指定优化对象的副本。如果命令失败（例如源优化对象不存在或名称冲突），Lumerical 会抛出错误。

在 Python API 中，`session.copyopt()` 通常返回 `None`。成功复制不返回任何值，失败时抛出异常。

## 错误处理

### 常见错误

1. **源优化对象不存在错误**
   ```python
   # 错误：源优化对象 "nonexistent_opt" 不存在
   fdtd.copyopt("nonexistent_opt")
   ```
   解决方案：使用 `hasexisting` 命令先检查优化对象是否存在。

2. **名称冲突错误**
   ```python
   # 错误：目标名称 "existing_opt" 已存在
   fdtd.copyopt("source_opt", "existing_opt")
   ```
   解决方案：使用不同的名称，或先删除现有优化对象。

3. **优化对象被锁定错误**
   ```python
   # 错误：优化对象正在运行或被锁定
   fdtd.copyopt("running_opt")
   ```
   解决方案：等待优化完成或停止优化。

4. **内存不足错误**
   ```python
   # 错误：复制复杂优化时内存不足
   fdtd.copyopt("large_opt")
   ```
   解决方案：关闭不必要的优化对象，增加可用内存。

### Python 错误处理示例
```python
import lumapi

try:
    fdtd = lumapi.FDTD()
    
    # 创建优化对象
    fdtd.addopt("source_opt", type="gradient", max_iter=100)
    fdtd.addvar("source_opt", "param", initial=0.5, min=0.1, max=1.0)
    
    # 成功复制
    fdtd.copyopt("source_opt", "copied_opt")
    print("优化设置复制成功")
    
    # 尝试复制不存在的优化对象
    fdtd.copyopt("nonexistent_opt", "new_opt")
    
except lumapi.LumApiError as e:
    error_str = str(e).lower()
    
    if "source" in error_str and "not found" in error_str:
        print("错误: 源优化对象不存在")
    elif "name" in error_str and "already exists" in error_str:
        print("错误: 目标名称已存在")
    elif "locked" in error_str or "running" in error_str:
        print("错误: 优化对象被锁定或正在运行")
    elif "memory" in error_str or "out of" in error_str:
        print("错误: 内存不足")
    else:
        print(f"Lumerical API 错误: {e}")
        
except Exception as e:
    print(f"一般错误: {e}")
```

## 使用示例

### 示例 1：基本优化设置复制

#### LSF 脚本
```lumerical
# 创建优化对象
addopt("original_opt",
       type: "gradient",           # 梯度优化算法
       max iter: 100,              # 最大迭代次数
       min change: 1e-6,           # 最小变化量
       min iter: 10);               # 最小迭代次数

# 添加设计变量
addvar("original_opt", "width", 
       initial: 0.5,               # 初始值 0.5 μm
       min: 0.2,                   # 最小值 0.2 μm
       max: 1.0);                   # 最大值 1.0 μm

addvar("original_opt", "height",
       initial: 0.22,
       min: 0.1,
       max: 0.5);

# 添加目标函数
addgoal("original_opt", "max_transmission",
        analysis: "FDTD",
        target: "maximize");        # 最大化传输率

?"原始优化设置:";
?"  算法类型: " + get("original_opt", "type");
?"  最大迭代次数: " + num2str(get("original_opt", "max iter"));
?"  设计变量数量: " + num2str(length(get("original_opt", "variables")));

# 复制优化设置
copyopt("original_opt", "copied_opt");

?"复制优化设置完成。";
?"新优化对象 'copied_opt' 的变量:";

# 检查复制结果
variables = get("copied_opt", "variables");
for (i = 1; i <= length(variables); i = i + 1) {
    var = variables(i);
    ?"  变量: " + get(var, "name") + 
      ", 初始值: " + num2str(get(var, "initial")) + 
      ", 范围: [" + num2str(get(var, "min")) + ", " + num2str(get(var, "max")) + "]";
}
```

#### Python API
```python
import lumapi

fdtd = lumapi.FDTD()

# 创建优化对象
fdtd.addopt("original_opt",
            type="gradient",           # 梯度优化算法
            max_iter=100,              # 最大迭代次数
            min_change=1e-6,           # 最小变化量
            min_iter=10)               # 最小迭代次数

# 添加设计变量
fdtd.addvar("original_opt", "width", 
            initial=0.5,               # 初始值 0.5 μm
            min=0.2,                   # 最小值 0.2 μm
            max=1.0)                   # 最大值 1.0 μm

fdtd.addvar("original_opt", "height",
            initial=0.22,
            min=0.1,
            max=0.5)

# 添加目标函数
fdtd.addgoal("original_opt", "max_transmission",
             analysis="FDTD",
             target="maximize")        # 最大化传输率

print("原始优化设置:")
opt_props = fdtd.get("original_opt")
print(f"  算法类型: {opt_props.get('type', '未知')}")
print(f"  最大迭代次数: {opt_props.get('max_iter', '未知')}")
print(f"  设计变量数量: {len(opt_props.get('variables', []))}")

# 复制优化设置
fdtd.copyopt("original_opt", "copied_opt")

print("\n复制优化设置完成。")
print("新优化对象 'copied_opt' 的变量:")

# 检查复制结果
copied_props = fdtd.get("copied_opt")
variables = copied_props.get('variables', [])
for var in variables:
    print(f"  变量: {var.get('name', '未知')}, "
          f"初始值: {var.get('initial', '未知')}, "
          f"范围: [{var.get('min', '未知')}, {var.get('max', '未知')}]")
```

### 示例 2：复制优化设置用于不同场景
```python
import lumapi

fdtd = lumapi.FDTD()

def create_waveguide_optimization(name, target_wavelength):
    """创建波导优化设置"""
    
    # 添加优化对象
    fdtd.addopt(name,
                type="genetic",        # 遗传算法
                population_size=50,    # 种群大小
                max_generations=200,   # 最大代数
                crossover_rate=0.8,    # 交叉率
                mutation_rate=0.1)     # 变异率
    
    # 波导宽度变量
    fdtd.addvar(name, "wg_width",
                initial=0.5,
                min=0.2,
                max=1.0,
                step=0.01)
    
    # 波导高度变量
    fdtd.addvar(name, "wg_height",
                initial=0.22,
                min=0.1,
                max=0.5,
                step=0.01)
    
    # 目标：在目标波长处最大化传输率
    fdtd.addgoal(name, f"transmission_{target_wavelength}",
                 analysis="FDTD",
                 target="maximize",
                 wavelength=target_wavelength)
    
    # 约束：波导宽高比
    fdtd.addconstraint(name, "aspect_ratio",
                       expression="wg_width / wg_height",
                       min=1.5,
                       max=3.0)
    
    return name

# 创建第一个优化（针对 1.55 μm）
print("创建 1.55 μm 波导优化...")
opt_1550 = create_waveguide_optimization("opt_1550", 1.55)

# 复制优化设置用于 1.31 μm
print("\n复制优化设置用于 1.31 μm...")
fdtd.copyopt("opt_1550", "opt_1310")

# 修改复制后的优化设置
fdtd.set("opt_1310", "name", "Waveguide_Optimization_1310nm")

# 更新目标波长
fdtd.setgoal("opt_1310", "transmission_1.55", 
             wavelength=1.31,
             name="transmission_1.31")

print("\n优化设置比较:")
for opt_name in ["opt_1550", "opt_1310"]:
    props = fdtd.get(opt_name)
    goals = props.get('goals', [])
    target_wavelength = "未知"
    
    for goal in goals:
        if 'wavelength' in goal:
            target_wavelength = goal['wavelength']
            break
    
    print(f"  {opt_name}:")
    print(f"    算法: {props.get('type', '未知')}")
    print(f"    目标波长: {target_wavelength} μm")
    print(f"    变量数量: {len(props.get('variables', []))}")
    print(f"    约束数量: {len(props.get('constraints', []))}")
```

### 示例 3：优化过程备份和恢复
```python
import lumapi
import time

class OptimizationManager:
    """优化管理器，支持备份和恢复"""
    
    def __init__(self, session):
        self.session = session
        self.backup_prefix = "backup_"
    
    def create_optimization(self, name, config):
        """创建优化"""
        print(f"创建优化: {name}")
        
        # 添加优化对象
        self.session.addopt(name, **config.get('optimization', {}))
        
        # 添加变量
        for var in config.get('variables', []):
            self.session.addvar(name, **var)
        
        # 添加目标
        for goal in config.get('goals', []):
            self.session.addgoal(name, **goal)
        
        # 添加约束
        for constraint in config.get('constraints', []):
            self.session.addconstraint(name, **constraint)
        
        return name
    
    def backup_optimization(self, source_name, backup_suffix=""):
        """备份优化设置"""
        backup_name = f"{self.backup_prefix}{source_name}{backup_suffix}"
        
        # 复制优化设置
        self.session.copyopt(source_name, backup_name)
        
        # 添加备份时间戳
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        self.session.set(backup_name, "backup_timestamp", timestamp)
        
        print(f"  已备份到: {backup_name} (时间: {timestamp})")
        return backup_name
    
    def restore_optimization(self, backup_name, new_name=None):
        """恢复优化设置"""
        if not backup_name.startswith(self.backup_prefix):
            print(f"错误: {backup_name} 不是备份文件")
            return None
        
        # 确定恢复后的名称
        if new_name is None:
            # 移除备份前缀
            new_name = backup_name[len(self.backup_prefix):]
        
        # 复制备份到新名称
        self.session.copyopt(backup_name, new_name)
        
        print(f"  已从 {backup_name} 恢复到 {new_name}")
        return new_name
    
    def list_backups(self, pattern="backup_*"):
        """列出所有备份"""
        self.session.eval(f"backups = ?{pattern};")
        backups = self.session.get("backups")
        self.session.clear("backups")
        
        return backups if backups else []

# 使用示例
fdtd = lumapi.FDTD()
manager = OptimizationManager(fdtd)

# 优化配置
opt_config = {
    'optimization': {
        'type': 'gradient',
        'max_iter': 50,
        'min_change': 1e-5
    },
    'variables': [
        {'name': 'radius', 'initial': 0.5, 'min': 0.1, 'max': 1.0, 'step': 0.01},
        {'name': 'period', 'initial': 0.7, 'min': 0.3, 'max': 1.2, 'step': 0.01}
    ],
    'goals': [
        {'name': 'efficiency', 'analysis': 'FDTD', 'target': 'maximize'}
    ],
    'constraints': [
        {'name': 'size_limit', 'expression': 'radius * 2 + period', 'max': 2.5}
    ]
}

# 创建优化
opt_name = manager.create_optimization("photonic_crystal_opt", opt_config)

print("\n运行优化（模拟）...")
# 模拟优化运行
for i in range(5):
    print(f"  迭代 {i+1}/5")
    time.sleep(0.1)
    
    # 每2次迭代备份一次
    if (i + 1) % 2 == 0:
        backup_suffix = f"_iter{i+1}"
        manager.backup_optimization(opt_name, backup_suffix)

print("\n所有备份:")
backups = manager.list_backups()
for backup in backups:
    props = fdtd.get(backup)
    timestamp = props.get('backup_timestamp', '未知')
    print(f"  {backup}: 备份时间 {timestamp}")

# 恢复到特定备份
print("\n恢复到第4次迭代的备份...")
restored_name = manager.restore_optimization("backup_photonic_crystal_opt_iter4", 
                                           "restored_opt")

# 比较优化状态
print("\n优化状态比较:")
for name in [opt_name, restored_name]:
    props = fdtd.get(name)
    print(f"  {name}:")
    print(f"    类型: {props.get('type', '未知')}")
    print(f"    最大迭代: {props.get('max_iter', '未知')}")
    print(f"    备份时间: {props.get('backup_timestamp', '无')}")
```

### 示例 4：多目标优化复制
```python
import lumapi

fdtd = lumapi.FDTD()

def setup_multi_objective_optimization(name):
    """设置多目标优化"""
    
    # 创建优化对象
    fdtd.addopt(name,
                type="pareto",          # 帕累托优化
                max_iter=200,
                population_size=100)
    
    # 设计变量：MZI 臂长差
    fdtd.addvar(name, "delta_L",
                initial=10,             # 初始臂长差 10 μm
                min=0,                  # 最小臂长差
                max=50,                 # 最大臂长差
                step=0.1)
    
    # 设计变量：耦合系数
    fdtd.addvar(name, "kappa",
                initial=0.5,            # 初始耦合系数
                min=0.1,                # 最小耦合系数
                max=0.9,                # 最大耦合系数
                step=0.01)
    
    # 目标1：在 1.55 μm 处最大化传输率
    fdtd.addgoal(name, "transmission_1550",
                 analysis="FDTD",
                 target="maximize",
                 wavelength=1.55,
                 weight=0.6)            # 权重 0.6
    
    # 目标2：在 1.31 μm 处最小化传输率（用于滤波）
    fdtd.addgoal(name, "transmission_1310",
                 analysis="FDTD",
                 target="minimize",
                 wavelength=1.31,
                 weight=0.4)            # 权重 0.4
    
    # 目标3：最小化器件尺寸
    fdtd.addgoal(name, "device_size",
                 analysis="parametric",
                 target="minimize",
                 expression="delta_L * 2",  # 近似器件尺寸
                 weight=0.2)
    
    # 约束：自由光谱范围 (FSR)
    fdtd.addconstraint(name, "fsr_constraint",
                       expression="c / (2 * delta_L * neff)",  # FSR 公式
                       min=10,           # 最小 FSR 10 nm
                       unit="nm")
    
    return name

# 设置第一个多目标优化
print("设置 MZI 滤波器优化...")
mzi_opt = setup_multi_objective_optimization("mzi_filter_opt")

# 复制优化设置用于不同应用
print("\n复制优化设置用于不同场景:")

# 场景1：高速调制器优化（不同权重）
fdtd.copyopt("mzi_filter_opt", "modulator_opt")
fdtd.setgoal("modulator_opt", "transmission_1550", weight=0.8)   # 更注重 1.55 μm
fdtd.setgoal("modulator_opt", "transmission_1310", weight=0.1)   # 不太注重 1.31 μm
fdtd.setgoal("modulator_opt", "device_size", weight=0.1)         # 不太注重尺寸
print("  1. 调制器优化：速度优先")

# 场景2：紧凑型滤波器优化（强调尺寸）
fdtd.copyopt("mzi_filter_opt", "compact_filter_opt")
fdtd.setgoal("compact_filter_opt", "transmission_1550", weight=0.3)
fdtd.setgoal("compact_filter_opt", "transmission_1310", weight=0.3)
fdtd.setgoal("compact_filter_opt", "device_size", weight=0.4)    # 更注重尺寸
print("  2. 紧凑滤波器优化：尺寸优先")

# 场景3：宽带优化（不同波长）
fdtd.copyopt("mzi_filter_opt", "broadband_opt")
fdtd.setgoal("broadband_opt", "transmission_1550", wavelength=1.55, weight=0.4)
fdtd.setgoal("broadband_opt", "transmission_1310", wavelength=1.31, weight=0.4)
# 添加第三个波长目标
fdtd.addgoal("broadband_opt", "transmission_1490",
             analysis="FDTD",
             target="maximize",
             wavelength=1.49,
             weight=0.2)
print("  3. 宽带优化：多波长平衡")

# 比较所有优化设置
print("\n优化设置比较:")
optimizations = ["mzi_filter_opt", "modulator_opt", "compact_filter_opt", "broadband_opt"]

for opt_name in optimizations:
    props = fdtd.get(opt_name)
    goals = props.get('goals', [])
    
    print(f"\n{opt_name}:")
    print(f"  算法: {props.get('type', '未知')}")
    print(f"  目标数量: {len(goals)}")
    
    total_weight = sum(goal.get('weight', 0) for goal in goals)
    print(f"  总权重: {total_weight:.2f}")
    
    for goal in goals:
        name = goal.get('name', '未知')
        target = goal.get('target', '未知')
        weight = goal.get('weight', 0)
        wavelength = goal.get('wavelength', 'N/A')
        print(f"    目标: {name}, 方向: {target}, 权重: {weight:.2f}, 波长: {wavelength}")
```

### 示例 5：优化参数扫描模板
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def create_optimization_template(template_name, base_config):
    """创建优化模板"""
    
    # 创建模板优化
    fdtd.addopt(template_name, **base_config['optimization'])
    
    # 添加模板变量（使用占位符）
    for var_template in base_config['variable_templates']:
        fdtd.addvar(template_name, **var_template)
    
    # 添加模板目标
    for goal_template in base_config['goal_templates']:
        fdtd.addgoal(template_name, **goal_template)
    
    return template_name

def generate_from_template(template_name, param_sets):
    """从模板生成多个优化实例"""
    
    generated_opts = []
    
    for i, params in enumerate(param_sets):
        # 新优化名称
        new_name = f"{template_name}_instance_{i}"
        
        # 复制模板
        fdtd.copyopt(template_name, new_name)
        
        # 应用参数
        for param_name, param_value in params.items():
            if param_name.startswith("var_"):
                # 变量参数
                var_name = param_name[4:]  # 去掉 "var_" 前缀
                fdtd.setvar(new_name, var_name, param_value)
            elif param_name.startswith("goal_"):
                # 目标参数
                goal_name = param_name[5:]  # 去掉 "goal_" 前缀
                fdtd.setgoal(new_name, goal_name, **param_value)
            else:
                # 优化参数
                fdtd.set(new_name, param_name, param_value)
        
        generated_opts.append(new_name)
        print(f"  生成优化实例: {new_name}")
    
    return generated_opts

# 定义优化模板
template_config = {
    'optimization': {
        'type': 'gradient',
        'max_iter': 100,
        'min_change': 1e-6
    },
    'variable_templates': [
        {'name': 'width', 'initial': 0.5, 'min': 0.2, 'max': 1.0, 'step': 0.01},
        {'name': 'height', 'initial': 0.22, 'min': 0.1, 'max': 0.5, 'step': 0.01},
        {'name': 'length', 'initial': 10, 'min': 5, 'max': 20, 'step': 0.1}
    ],
    'goal_templates': [
        {'name': 'transmission', 'analysis': 'FDTD', 'target': 'maximize', 'weight': 1.0}
    ]
}

print("创建优化模板...")
template = create_optimization_template("waveguide_opt_template", template_config)

# 定义参数扫描
print("\n生成参数扫描优化实例:")

param_sets = [
    # 实例1：标准波导
    {
        'var_width': 0.5,
        'var_height': 0.22,
        'goal_transmission': {'wavelength': 1.55, 'weight': 1.0}
    },
    # 实例2：窄波导（高对比度）
    {
        'var_width': 0.3,
        'var_height': 0.22,
        'goal_transmission': {'wavelength': 1.55, 'weight': 1.0}
    },
    # 实例3：宽波导（多模）
    {
        'var_width': 0.8,
        'var_height': 0.22,
        'goal_transmission': {'wavelength': 1.55, 'weight': 0.7},
        'goal_mode_purity': {'analysis': 'FDE', 'target': 'maximize', 'weight': 0.3}
    },
    # 实例4：不同波长目标
    {
        'var_width': 0.5,
        'var_height': 0.22,
        'goal_transmission': {'wavelength': 1.31, 'weight': 1.0},
        'max_iter': 150  # 更多迭代
    }
]

# 生成优化实例
instances = generate_from_template(template, param_sets)

print(f"\n总共生成了 {len(instances)} 个优化实例。")
print("实例列表:", instances)

# 验证生成结果
print("\n实例验证:")
for instance in instances:
    props = fdtd.get(instance)
    vars = props.get('variables', [])
    goals = props.get('goals', [])
    
    print(f"\n{instance}:")
    print(f"  变量: {[v.get('name') for v in vars]}")
    print(f"  目标: {[g.get('name') for g in goals]}")
    print(f"  最大迭代: {props.get('max_iter', '默认')}")
```

## 注意事项

1. **优化状态**：`copyopt` 会复制优化的当前状态，包括迭代次数、最佳结果等。如果只想复制设置而不复制状态，可能需要在新优化中重置状态。

2. **对象依赖性**：优化可能依赖于其他对象（如仿真设置、材料定义等）。复制优化设置不会自动复制这些依赖对象。

3. **名称冲突**：如果目标名称已存在，`copyopt` 可能会覆盖现有优化。建议在复制前检查名称可用性。

4. **性能影响**：复制包含大量变量、目标和约束的复杂优化可能会影响性能。

5. **版本兼容性**：优化设置可能依赖于特定版本的 Lumerical。在不同版本间复制优化设置时，可能需要调整某些参数。

6. **与 `saveopt` 的区别**：`copyopt` 在内存中复制优化，而 `saveopt` 将优化设置保存到文件。`copyopt` 更适合在同一会话中快速创建相似优化。

7. **参数继承**：所有优化参数都会被复制，包括高级设置和算法特定参数。复制后可能需要调整某些参数以适应新场景。

8. **验证复制结果**：复制后建议验证新优化的设置是否正确，特别是变量范围、约束条件和目标权重。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 支持所有优化功能 |
| MODE Solutions | ✅ 完全支持 | 支持所有优化功能 |
| DEVICE | ✅ 完全支持 | 支持所有优化功能 |
| INTERCONNECT | ✅ 完全支持 | 支持所有优化功能 |

## 相关命令

- `addopt` - 添加优化对象
- `addvar` - 添加优化变量
- `addgoal` - 添加优化目标
- `addconstraint` - 添加优化约束
- `setopt` - 设置优化属性
- `runopt` - 运行优化
- `saveopt` - 保存优化设置到文件
- `loadopt` - 从文件加载优化设置

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含基本语法和示例 |
| 1.1 | 2026-01-31 | 添加返回值、错误处理章节、版本历史和参考 |

## 参考

1. Lumerical Script Language Reference - copyopt 命令
2. Lumerical Python API Documentation - session.copyopt() 方法
3. Lumerical Optimization User Guide - 优化设置复制最佳实践

---

*最后更新: 2026-01-31*  
*文档版本: 1.1*