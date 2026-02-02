# `divide` - 数组除法

## 概述

`divide` 命令用于执行数组或矩阵的除法运算。在 Lumerical 脚本中，该命令支持元素级除法、矩阵除法以及标量与数组的除法。它是数值计算、数据分析和仿真后处理的基本工具。

主要功能：
- **元素级除法**：对两个相同形状的数组进行逐元素除法
- **标量除法**：将数组的每个元素除以标量
- **矩阵除法**：执行矩阵除法（等价于乘以逆矩阵）
- **复数除法**：支持复数数组的除法
- **广播操作**：支持不同形状数组的广播除法

典型应用：
- 仿真结果归一化
- 传输矩阵计算
- 场分布比率分析
- 数据预处理
- 误差计算

## 语法

### LSF 语法
```lumerical
divide(a, b);           # 返回 a ÷ b 的结果
divide(a, b, c);        # 返回 a ÷ b ÷ c 的结果
divide(result, a, b);   # 将 a ÷ b 的结果存储到 result
```

### Python API
```python
session.divide(a, b)           # 返回 a ÷ b 的结果
session.divide(a, b, c)        # 返回 a ÷ b ÷ c 的结果
session.divide(result, a, b)   # 将 a ÷ b 的结果存储到 result
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `a` | number/array | 被除数（分子）。 | 是 |
| `b` | number/array | 除数（分母）。 | 是 |
| `c` | number/array | 额外的除数（可选）。 | 否 |
| `result` | variable | 存储结果的变量名称。 | 否 |

## 配置属性

`divide` 命令通常不通过 `set` 命令配置属性，但除法行为受以下因素影响：

| 相关属性 | 类型 | 默认值 | 描述 |
|----------|------|--------|------|
| `matrix division` | bool | false | 是否使用矩阵除法（而非元素级除法）。 |
| `broadcast` | bool | true | 是否允许广播操作。 |
| `divide by zero` | string | "inf" | 除零处理："inf"（无穷大），"nan"（非数字），"error"（报错）。 |
| `precision` | number | 1e-12 | 数值精度（用于判断是否为零）。 |

## 使用示例

### 示例 1：基本除法操作
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("基本除法操作演示...")

# 标量除法
a = 10.0
b = 2.5
result = fdtd.divide(a, b)
print(f"标量除法: {a} ÷ {b} = {result}")

# 数组元素级除法
arr1 = np.array([1.0, 4.0, 9.0, 16.0])
arr2 = np.array([1.0, 2.0, 3.0, 4.0])
result_arr = fdtd.divide(arr1, arr2)
print(f"数组除法: {arr1} ÷ {arr2} = {result_arr}")

# 标量与数组除法
scalar = 2.0
result_scalar_arr = fdtd.divide(arr1, scalar)
print(f"标量除数组: {arr1} ÷ {scalar} = {result_scalar_arr}")

# 数组与标量除法（倒数）
result_arr_scalar = fdtd.divide(scalar, arr1)
print(f"数组除标量: {scalar} ÷ {arr1} = {result_arr_scalar}")

# 多参数除法
c = 2.0
result_multi = fdtd.divide(a, b, c)
print(f"多参数除法: {a} ÷ {b} ÷ {c} = {result_multi}")

# 存储结果到变量
fdtd.eval("result_var = 0;")
fdtd.divide("result_var", 100, 4)
result_var = fdtd.get("result_var")
print(f"存储结果: 100 ÷ 4 = {result_var}")
```

### 示例 2：矩阵和数组运算
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("矩阵和数组运算演示...")

# 创建测试矩阵
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]], dtype=float)

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]], dtype=float)

print("矩阵1:")
print(matrix1)
print("\n矩阵2:")
print(matrix2)

# 元素级矩阵除法
elementwise_division = fdtd.divide(matrix1, matrix2)
print("\n元素级矩阵除法:")
print(elementwise_division)

# 验证元素级除法
expected_elementwise = matrix1 / matrix2
print("\n验证（NumPy 计算）:")
print(expected_elementwise)
print(f"最大差异: {np.max(np.abs(elementwise_division - expected_elementwise))}")

# 标量除矩阵
scalar = 2.0
scalar_division = fdtd.divide(matrix1, scalar)
print(f"\n标量除矩阵 (÷{scalar}):")
print(scalar_division)

# 矩阵除标量（求倒数）
inverse_scalar_division = fdtd.divide(scalar, matrix1)
print(f"\n矩阵除标量 ({scalar}÷):")
print(inverse_scalar_division)

# 广播操作：矩阵除向量
vector = np.array([1, 2, 3], dtype=float)
broadcast_division = fdtd.divide(matrix1, vector)
print("\n广播操作 - 矩阵除向量:")
print(broadcast_division)
print("形状:", broadcast_division.shape)

# 广播操作：向量除矩阵
broadcast_division2 = fdtd.divide(vector.reshape(3, 1), matrix1)
print("\n广播操作 - 向量除矩阵:")
print(broadcast_division2)
print("形状:", broadcast_division2.shape)

# 复数数组除法
complex1 = np.array([1+2j, 3+4j, 5+6j])
complex2 = np.array([2+1j, 4+3j, 6+5j])
complex_division = fdtd.divide(complex1, complex2)
print("\n复数数组除法:")
print(f"  被除数: {complex1}")
print(f"  除数: {complex2}")
print(f"  结果: {complex_division}")

# 验证复数除法
expected_complex = complex1 / complex2
print(f"  验证: {expected_complex}")
print(f"  最大差异: {np.max(np.abs(complex_division - expected_complex))}")
```

### 示例 3：仿真数据处理
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("仿真数据处理演示...")

class SimulationDataProcessor:
    """仿真数据处理工具"""
    
    def __init__(self, session):
        self.session = session
    
    def normalize_data(self, data, reference):
        """归一化数据（除以参考值）"""
        
        print(f"数据归一化...")
        print(f"  数据形状: {data.shape}")
        print(f"  参考形状: {reference.shape}")
        
        # 执行除法归一化
        normalized = self.session.divide(data, reference)
        
        # 计算统计信息
        if isinstance(normalized, np.ndarray):
            stats = {
                'min': np.min(normalized),
                'max': np.max(normalized),
                'mean': np.mean(normalized),
                'std': np.std(normalized),
                'median': np.median(normalized)
            }
            
            print(f"  归一化统计:")
            for key, value in stats.items():
                print(f"    {key}: {value:.6g}")
        
        return normalized
    
    def calculate_transmission(self, output_power, input_power):
        """计算传输系数"""
        
        print(f"计算传输系数...")
        print(f"  输出功率: 形状={output_power.shape}, 范围=[{np.min(output_power):.3g}, {np.max(output_power):.3g}]")
        print(f"  输入功率: 形状={input_power.shape}, 范围=[{np.min(input_power):.3g}, {np.max(input_power):.3g}]")
        
        # 传输系数 = 输出功率 / 输入功率
        transmission = self.session.divide(output_power, input_power)
        
        # 转换为 dB
        transmission_db = 10 * np.log10(np.abs(transmission))
        
        return transmission, transmission_db
    
    def calculate_reflection(self, reflected_power, input_power):
        """计算反射系数"""
        
        print(f"计算反射系数...")
        
        # 反射系数 = 反射功率 / 输入功率
        reflection = self.session.divide(reflected_power, input_power)
        
        # 转换为 dB
        reflection_db = 10 * np.log10(np.abs(reflection))
        
        return reflection, reflection_db
    
    def calculate_efficiency(self, useful_power, total_power):
        """计算效率"""
        
        print(f"计算效率...")
        
        # 效率 = 有用功率 / 总功率
        efficiency = self.session.divide(useful_power, total_power)
        
        # 转换为百分比
        efficiency_percent = efficiency * 100
        
        return efficiency, efficiency_percent
    
    def analyze_field_enhancement(self, field_with_structure, field_without_structure):
        """分析场增强"""
        
        print(f"分析场增强...")
        
        # 场增强 = 有结构时的场 / 无结构时的场
        field_enhancement = self.session.divide(field_with_structure, field_without_structure)
        
        # 计算增强因子（幅度平方）
        enhancement_factor = np.abs(field_enhancement)**2
        
        # 找到最大增强位置
        max_enhancement = np.max(enhancement_factor)
        max_position = np.unravel_index(np.argmax(enhancement_factor), enhancement_factor.shape)
        
        print(f"  最大场增强: {np.sqrt(max_enhancement):.3f}× (强度增强: {max_enhancement:.3f}×)")
        print(f"  最大增强位置: {max_position}")
        
        return field_enhancement, enhancement_factor
    
    def calculate_error(self, measured, simulated, method='relative'):
        """计算误差"""
        
        print(f"计算误差 ({method})...")
        
        if method == 'relative':
            # 相对误差 = |测量值 - 仿真值| / |测量值|
            error = self.session.divide(np.abs(measured - simulated), np.abs(measured))
        elif method == 'absolute':
            # 绝对误差 = |测量值 - 仿真值|
            error = np.abs(measured - simulated)
        elif method == 'percentage':
            # 百分比误差 = |测量值 - 仿真值| / |测量值| × 100%
            relative = self.session.divide(np.abs(measured - simulated), np.abs(measured))
            error = relative * 100
        else:
            raise ValueError(f"未知误差计算方法: {method}")
        
        return error

# 创建处理器
processor = SimulationDataProcessor(fdtd)

# 生成模拟仿真数据
print("\n生成模拟仿真数据...")
np.random.seed(42)  # 可重复性

# 模拟场数据
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

# 无结构时的场（高斯分布）
field_without = np.exp(-(X**2 + Y**2) / 10)

# 有结构时的场（高斯分布 + 扰动）
field_with = field_without * (1 + 0.5 * np.exp(-((X-2)**2 + (Y-1)**2) / 2) +
                              0.3 * np.exp(-((X+1)**2 + (Y+2)**2) / 3))

print(f"场数据形状: {field_with.shape}")

# 模拟功率数据
frequencies = np.linspace(150, 200, 51)  # THz
input_power = np.ones_like(frequencies) * 1e-3  # 1 mW 恒定输入
output_power = input_power * (0.8 + 0.1 * np.sin(2*np.pi*frequencies/50))  # 带波纹的输出
reflected_power = input_power * (0.1 + 0.05 * np.cos(2*np.pi*frequencies/40))  # 反射功率

print(f"频率点: {len(frequencies)}")
print(f"频率范围: {frequencies[0]:.1f} - {frequencies[-1]:.1f} THz")

# 执行各种计算
print("\n" + "="*50)
print("仿真数据处理结果")
print("="*50)

# 1. 场增强分析
field_enhancement, enhancement_factor = processor.analyze_field_enhancement(field_with, field_without)

# 2. 传输系数计算
transmission, transmission_db = processor.calculate_transmission(output_power, input_power)

print(f"\n传输系数统计:")
print(f"  平均传输: {np.mean(transmission):.3f} ({np.mean(transmission_db):.2f} dB)")
print(f"  最小传输: {np.min(transmission):.3f} ({np.min(transmission_db):.2f} dB)")
print(f"  最大传输: {np.max(transmission):.3f} ({np.max(transmission_db):.2f} dB)")

# 3. 反射系数计算
reflection, reflection_db = processor.calculate_reflection(reflected_power, input_power)

print(f"\n反射系数统计:")
print(f"  平均反射: {np.mean(reflection):.3f} ({np.mean(reflection_db):.2f} dB)")
print(f"  最小反射: {np.min(reflection):.3f} ({np.min(reflection_db):.2f} dB)")
print(f"  最大反射: {np.max(reflection):.3f} ({np.max(reflection_db):.2f} dB)")

# 4. 效率计算
# 有用功率 = 输出功率
# 总功率 = 输入功率
efficiency, efficiency_percent = processor.calculate_efficiency(output_power, input_power)

print(f"\n效率统计:")
print(f"  平均效率: {np.mean(efficiency):.3f} ({np.mean(efficiency_percent):.1f}%)")
print(f"  最小效率: {np.min(efficiency):.3f} ({np.min(efficiency_percent):.1f}%)")
print(f"  最大效率: {np.max(efficiency):.3f} ({np.max(efficiency_percent):.1f}%)")

# 5. 误差计算（模拟测量数据）
measured_power = output_power * (1 + 0.05 * np.random.randn(len(output_power)))  # 添加5%噪声
error_relative = processor.calculate_error(measured_power, output_power, 'relative')
error_percentage = processor.calculate_error(measured_power, output_power, 'percentage')

print(f"\n误差分析:")
print(f"  平均相对误差: {np.mean(error_relative):.4f}")
print(f"  最大相对误差: {np.max(error_relative):.4f}")
print(f"  平均百分比误差: {np.mean(error_percentage):.2f}%")
print(f"  最大百分比误差: {np.max(error_percentage):.2f}%")

# 6. 数据归一化示例
reference_power = np.max(output_power)  # 以最大输出功率为参考
normalized_power = processor.normalize_data(output_power, reference_power)

print(f"\n归一化验证:")
print(f"  归一化后范围: [{np.min(normalized_power):.3f}, {np.max(normalized_power):.3f}]")
print(f"  理论最大值应为: 1.0")
print(f"  实际最大值: {np.max(normalized_power):.6f}")
print(f"  差异: {abs(1.0 - np.max(normalized_power)):.6f}")

# 7. 计算功率守恒
total_output = output_power + reflected_power  # 忽略其他损耗
power_conservation = processor.divide(total_output, input_power)

print(f"\n功率守恒检查:")
print(f"  平均输出/输入比: {np.mean(power_conservation):.4f}")
print(f"  理想值应为: 1.0 (无损耗)")
print(f"  平均损耗: {(1 - np.mean(power_conservation))*100:.2f}%")

print("\n仿真数据处理完成!")
```

### 示例 4：高级数学运算
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("高级数学运算演示...")

class AdvancedMathOperations:
    """高级数学运算工具"""
    
    def __init__(self, session):
        self.session = session
    
    def matrix_division(self, A, B, method='elementwise'):
        """矩阵除法"""
        
        print(f"执行矩阵除法 (方法: {method})...")
        print(f"  矩阵A形状: {A.shape}")
        print(f"  矩阵B形状: {B.shape}")
        
        if method == 'elementwise':
            # 元素级除法（要求相同形状）
            if A.shape != B.shape:
                raise ValueError("元素级除法要求矩阵形状相同")
            
            result = self.session.divide(A, B)
            
        elif method == 'left':
            # 左除：A \ B = A⁻¹B
            # 对于标量/对角矩阵简化实现
            if A.ndim == 1 or (A.ndim == 2 and A.shape[0] == A.shape[1]):
                # 假设A是对角矩阵或可逆
                try:
                    A_inv = np.linalg.inv(A)
                    result = A_inv @ B
                except np.linalg.LinAlgError:
                    print("  警告: 矩阵A不可逆，使用伪逆")
                    A_pinv = np.linalg.pinv(A)
                    result = A_pinv @ B
            else:
                raise ValueError("左除要求A为方阵或可处理矩阵")
            
        elif method == 'right':
            # 右除：A / B = AB⁻¹
            if B.ndim == 1 or (B.ndim == 2 and B.shape[0] == B.shape[1]):
                try:
                    B_inv = np.linalg.inv(B)
                    result = A @ B_inv
                except np.linalg.LinAlgError:
                    print("  警告: 矩阵B不可逆，使用伪逆")
                    B_pinv = np.linalg.pinv(B)
                    result = A @ B_pinv
            else:
                raise ValueError("右除要求B为方阵或可处理矩阵")
            
        else:
            raise ValueError(f"未知矩阵除法方法: {method}")
        
        return result
    
    def calculate_gradient(self, field, dx=1.0, dy=1.0):
        """计算场梯度（使用有限差分）"""
        
        print(f"计算场梯度...")
        print(f"  场形状: {field.shape}")
        
        # 使用中心差分计算梯度
        grad_x = np.zeros_like(field)
        grad_y = np.zeros_like(field)
        
        # x方向梯度
        if field.shape[0] > 2:
            grad_x[1:-1, :] = self.session.divide(field[2:, :] - field[:-2, :], 2*dx)
            # 边界使用前向/后向差分
            grad_x[0, :] = self.session.divide(field[1, :] - field[0, :], dx)
            grad_x[-1, :] = self.session.divide(field[-1, :] - field[-2, :], dx)
        
        # y方向梯度
        if field.shape[1] > 2:
            grad_y[:, 1:-1] = self.session.divide(field[:, 2:] - field[:, :-2], 2*dy)
            # 边界使用前向/后向差分
            grad_y[:, 0] = self.session.divide(field[:, 1] - field[:, 0], dy)
            grad_y[:, -1] = self.session.divide(field[:, -1] - field[:, -2], dy)
        
        # 计算梯度幅度
        grad_magnitude = np.sqrt(grad_x**2 + grad_y**2)
        
        return grad_x, grad_y, grad_magnitude
    
    def calculate_divergence(self, field_x, field_y, dx=1.0, dy=1.0):
        """计算散度"""
        
        print(f"计算散度...")
        print(f"  field_x形状: {field_x.shape}")
        print(f"  field_y形状: {field_y.shape}")
        
        if field_x.shape != field_y.shape:
            raise ValueError("场分量形状必须相同")
        
        # 使用中心差分计算散度
        divergence = np.zeros_like(field_x)
        
        # x方向导数
        if field_x.shape[0] > 2:
            dfx_dx = np.zeros_like(field_x)
            dfx_dx[1:-1, :] = self.session.divide(field_x[2:, :] - field_x[:-2, :], 2*dx)
            # 边界
            dfx_dx[0, :] = self.session.divide(field_x[1, :] - field_x[0, :], dx)
            dfx_dx[-1, :] = self.session.divide(field_x[-1, :] - field_x[-2, :], dx)
        
        # y方向导数
        if field_x.shape[1] > 2:
            dfy_dy = np.zeros_like(field_y)
            dfy_dy[:, 1:-1] = self.session.divide(field_y[:, 2:] - field_y[:, :-2], 2*dy)
            # 边界
            dfy_dy[:, 0] = self.session.divide(field_y[:, 1] - field_y[:, 0], dy)
            dfy_dy[:, -1] = self.session.divide(field_y[:, -1] - field_y[:, -2], dy)
        
        # 散度 = ∂Fx/∂x + ∂Fy/∂y
        divergence = dfx_dx + dfy_dy
        
        return divergence
    
    def calculate_curl(self, field_x, field_y, dx=1.0, dy=1.0):
        """计算旋度（2D）"""
        
        print(f"计算旋度...")
        
        if field_x.shape != field_y.shape:
            raise ValueError("场分量形状必须相同")
        
        # 旋度 = ∂Fy/∂x - ∂Fx/∂y
        curl = np.zeros_like(field_x)
        
        # ∂Fy/∂x
        if field_y.shape[0] > 2:
            dfy_dx = np.zeros_like(field_y)
            dfy_dx[1:-1, :] = self.session.divide(field_y[2:, :] - field_y[:-2, :], 2*dx)
            # 边界
            dfy_dx[0, :] = self.session.divide(field_y[1, :] - field_y[0, :], dx)
            dfy_dx[-1, :] = self.session.divide(field_y[-1, :] - field_y[-2, :], dx)
        
        # ∂Fx/∂y
        if field_x.shape[1] > 2:
            dfx_dy = np.zeros_like(field_x)
            dfx_dy[:, 1:-1] = self.session.divide(field_x[:, 2:] - field_x[:, :-2], 2*dy)
            # 边界
            dfx_dy[:, 0] = self.session.divide(field_x[:, 1] - field_x[:, 0], dy)
            dfx_dy[:, -1] = self.session.divide(field_x[:, -1] - field_x[:, -2], dy)
        
        # 旋度
        curl = dfy_dx - dfx_dy
        
        return curl
    
    def calculate_laplacian(self, field, dx=1.0, dy=1.0):
        """计算拉普拉斯算子"""
        
        print(f"计算拉普拉斯算子...")
        
        laplacian = np.zeros_like(field)
        
        # 使用五点差分格式
        if field.shape[0] > 2 and field.shape[1] > 2:
            # x方向二阶导数
            d2f_dx2 = np.zeros_like(field)
            d2f_dx2[1:-1, :] = self.session.divide(
                field[2:, :] - 2*field[1:-1, :] + field[:-2, :],
                dx**2
            )
            
            # y方向二阶导数
            d2f_dy2 = np.zeros_like(field)
            d2f_dy2[:, 1:-1] = self.session.divide(
                field[:, 2:] - 2*field[:, 1:-1] + field[:, :-2],
                dy**2
            )
            
            # 拉普拉斯算子 = ∂²f/∂x² + ∂²f/∂y²
            laplacian = d2f_dx2 + d2f_dy2
            
            # 处理边界（简单复制内部值）
            laplacian[0, :] = laplacian[1, :]
            laplacian[-1, :] = laplacian[-2, :]
            laplacian[:, 0] = laplacian[:, 1]
            laplacian[:, -1] = laplacian[:, -2]
        
        return laplacian
    
    def solve_poisson(self, source, dx=1.0, dy=1.0, max_iter=1000, tolerance=1e-6):
        """使用松弛法求解泊松方程"""
        
        print(f"求解泊松方程...")
        print(f"  源项形状: {source.shape}")
        print(f"  网格间距: dx={dx}, dy={dy}")
        print(f"  最大迭代: {max_iter}, 容差: {tolerance}")
        
        # 初始化解
        phi = np.zeros_like(source)
        
        # 迭代求解
        for iteration in range(max_iter):
            phi_old = phi.copy()
            
            # 使用五点差分格式更新内部点
            phi[1:-1, 1:-1] = 0.25 * (
                phi_old[2:, 1:-1] + phi_old[:-2, 1:-1] +
                phi_old[1:-1, 2:] + phi_old[1:-1, :-2] -
                dx**2 * source[1:-1, 1:-1]
            )
            
            # 计算收敛误差
            error = np.max(np.abs(phi - phi_old))
            
            if iteration % 100 == 0:
                print(f"  迭代 {iteration}: 最大误差 = {error:.6g}")
            
            if error < tolerance:
                print(f"  在 {iteration} 次迭代后收敛")
                break
        
        if iteration == max_iter - 1:
            print(f"  达到最大迭代次数，最终误差 = {error:.6g}")
        
        return phi

# 创建高级数学工具
math_tools = AdvancedMathOperations(fdtd)

# 创建测试数据
print("\n创建测试数据...")

# 1. 矩阵测试
A = np.array([[4, 2],
              [1, 3]], dtype=float)
B = np.array([[2, 4],
              [1, 2]], dtype=float)

print("矩阵A:")
print(A)
print("\n矩阵B:")
print(B)

# 矩阵除法
print("\n" + "="*50)
print("矩阵除法测试")
print("="*50)

# 元素级除法
elementwise_result = math_tools.matrix_division(A, B, 'elementwise')
print("\n元素级除法结果:")
print(elementwise_result)

# 左除（A \ B = A⁻¹B）
try:
    left_division = math_tools.matrix_division(A, B, 'left')
    print("\n左除结果 (A⁻¹B):")
    print(left_division)
    
    # 验证
    A_inv = np.linalg.inv(A)
    expected_left = A_inv @ B
    print("\n验证 (NumPy):")
    print(expected_left)
    print(f"最大差异: {np.max(np.abs(left_division - expected_left)):.6g}")
except Exception as e:
    print(f"\n左除失败: {e}")

# 右除（A / B = AB⁻¹）
try:
    right_division = math_tools.matrix_division(A, B, 'right')
    print("\n右除结果 (AB⁻¹):")
    print(right_division)
    
    # 验证
    B_inv = np.linalg.inv(B)
    expected_right = A @ B_inv
    print("\n验证 (NumPy):")
    print(expected_right)
    print(f"最大差异: {np.max(np.abs(right_division - expected_right)):.6g}")
except Exception as e:
    print(f"\n右除失败: {e}")

# 2. 场分析测试
print("\n" + "="*50)
print("场分析测试")
print("="*50)

# 创建测试场
x = np.linspace(-5, 5, 51)
y = np.linspace(-5, 5, 51)
X, Y = np.meshgrid(x, y)

# 创建向量场：F = (x, y)
F_x = X
F_y = Y

# 创建标量场：f = x² + y²
f = X**2 + Y**2

print(f"标量场 f 形状: {f.shape}")
print(f"向量场 F_x 形状: {F_x.shape}")
print(f"向量场 F_y 形状: {F_y.shape}")

# 计算梯度
grad_x, grad_y, grad_mag = math_tools.calculate_gradient(f, dx=x[1]-x[0], dy=y[1]-y[0])

print(f"\n梯度分析:")
print(f"  ∂f/∂x 范围: [{np.min(grad_x):.3f}, {np.max(grad_x):.3f}]")
print(f"  ∂f/∂y 范围: [{np.min(grad_y):.3f}, {np.max(grad_y):.3f}]")
print(f"  梯度幅度范围: [{np.min(grad_mag):.3f}, {np.max(grad_mag):.3f}]")

# 验证梯度：对于 f = x² + y²，梯度应为 (2x, 2y)
expected_grad_x = 2 * X
expected_grad_y = 2 * Y

grad_error_x = np.max(np.abs(grad_x - expected_grad_x))
grad_error_y = np.max(np.abs(grad_y - expected_grad_y))

print(f"\n梯度验证:")
print(f"  ∂f/∂x 最大误差: {grad_error_x:.6g}")
print(f"  ∂f/∂y 最大误差: {grad_error_y:.6g}")

# 计算散度
divergence = math_tools.calculate_divergence(F_x, F_y, dx=x[1]-x[0], dy=y[1]-y[0])

print(f"\n散度分析:")
print(f"  ∇·F 范围: [{np.min(divergence):.3f}, {np.max(divergence):.3f}]")
print(f"  ∇·F 平均值: {np.mean(divergence):.3f}")

# 验证散度：对于 F = (x, y)，散度应为 2
expected_divergence = 2 * np.ones_like(divergence)
div_error = np.max(np.abs(divergence - expected_divergence))

print(f"  散度验证误差: {div_error:.6g}")
print(f"  理论值: 2.0")
print(f"  计算平均值: {np.mean(divergence):.6g}")

# 计算旋度
curl = math_tools.calculate_curl(F_x, F_y, dx=x[1]-x[0], dy=y[1]-y[0])

print(f"\n旋度分析:")
print(f"  ∇×F 范围: [{np.min(curl):.3f}, {np.max(curl):.3f}]")
print(f"  ∇×F 平均值: {np.mean(curl):.3f}")

# 验证旋度：对于 F = (x, y)，旋度应为 0
expected_curl = np.zeros_like(curl)
curl_error = np.max(np.abs(curl - expected_curl))

print(f"  旋度验证误差: {curl_error:.6g}")
print(f"  理论值: 0.0")
print(f"  计算平均值: {np.mean(curl):.6g}")

# 计算拉普拉斯算子
laplacian = math_tools.calculate_laplacian(f, dx=x[1]-x[0], dy=y[1]-y[0])

print(f"\n拉普拉斯算子分析:")
print(f"  ∇²f 范围: [{np.min(laplacian):.3f}, {np.max(laplacian):.3f}]")
print(f"  ∇²f 平均值: {np.mean(laplacian):.3f}")

# 验证拉普拉斯算子：对于 f = x² + y²，∇²f = 4
expected_laplacian = 4 * np.ones_like(laplacian)
laplacian_error = np.max(np.abs(laplacian - expected_laplacian))

print(f"  拉普拉斯算子验证误差: {laplacian_error:.6g}")
print(f"  理论值: 4.0")
print(f"  计算平均值: {np.mean(laplacian):.6g}")

# 3. 泊松方程求解
print("\n" + "="*50)
print("泊松方程求解测试")
print("="*50)

# 创建源项：对于解 φ = sin(πx)sin(πy)，源项应为 -2π² sin(πx)sin(πy)
x_poisson = np.linspace(0, 1, 31)
y_poisson = np.linspace(0, 1, 31)
Xp, Yp = np.meshgrid(x_poisson, y_poisson)

dx_poisson = x_poisson[1] - x_poisson[0]
dy_poisson = y_poisson[1] - y_poisson[0]

# 精确解
phi_exact = np.sin(np.pi * Xp) * np.sin(np.pi * Yp)

# 源项
source = -2 * np.pi**2 * phi_exact

print(f"泊松问题设置:")
print(f"  网格: {Xp.shape[0]} × {Xp.shape[1]}")
print(f"  间距: dx={dx_poisson:.3f}, dy={dy_poisson:.3f}")
print(f"  源项范围: [{np.min(source):.3f}, {np.max(source):.3f}]")

# 求解泊松方程
phi_solution = math_tools.solve_poisson(source, dx_poisson, dy_poisson, 
                                       max_iter=2000, tolerance=1e-6)

# 计算误差
solution_error = np.max(np.abs(phi_solution - phi_exact))
solution_rms = np.sqrt(np.mean((phi_solution - phi_exact)**2))

print(f"\n求解结果:")
print(f"  最大误差: {solution_error:.6g}")
print(f"  RMS误差: {solution_rms:.6g}")
print(f"  解的范围: [{np.min(phi_solution):.3f}, {np.max(phi_solution):.3f}]")
print(f"  精确解范围: [{np.min(phi_exact):.3f}, {np.max(phi_exact):.3f}]")

# 归一化解（泊松方程解可以相差一个常数）
phi_normalized = phi_solution / np.max(phi_solution)
phi_exact_normalized = phi_exact / np.max(phi_exact)

normalized_error = np.max(np.abs(phi_normalized - phi_exact_normalized))
print(f"  归一化后最大误差: {normalized_error:.6g}")

print("\n高级数学运算演示完成!")
```

### 示例 5：数值稳定性和特殊处理
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("数值稳定性和特殊处理演示...")

class NumericalStability:
    """数值稳定性工具"""
    
    def __init__(self, session):
        self.session = session
        self.epsilon = 1e-12  # 机器精度
    
    def safe_divide(self, numerator, denominator, default=0.0, epsilon=None):
        """安全除法（避免除零）"""
        
        if epsilon is None:
            epsilon = self.epsilon
        
        # 确保是数组
        numerator = np.asarray(numerator)
        denominator = np.asarray(denominator)
        
        # 创建掩码：分母接近零的位置
        mask_near_zero = np.abs(denominator) < epsilon
        
        # 执行除法
        result = self.session.divide(numerator, denominator)
        
        # 处理除零情况
        if np.any(mask_near_zero):
            if isinstance(default, (int, float)):
                result[mask_near_zero] = default
            else:
                # default 可能是数组
                default_arr = np.asarray(default)
                if default_arr.shape == result.shape:
                    result[mask_near_zero] = default_arr[mask_near_zero]
                else:
                    result[mask_near_zero] = 0.0
        
        return result, mask_near_zero
    
    def calculate_snr(self, signal, noise, method='power'):
        """计算信噪比"""
        
        print(f"计算信噪比 (方法: {method})...")
        
        signal = np.asarray(signal)
        noise = np.asarray(noise)
        
        if method == 'power':
            # SNR = 10 log10(信号功率 / 噪声功率)
            signal_power = np.mean(np.abs(signal)**2)
            noise_power = np.mean(np.abs(noise)**2)
            
            # 安全除法
            snr_ratio, mask = self.safe_divide(signal_power, noise_power, default=float('inf'))
            snr_db = 10 * np.log10(snr_ratio)
            
        elif method == 'amplitude':
            # SNR = 20 log10(信号幅度 / 噪声幅度)
            signal_amplitude = np.sqrt(np.mean(np.abs(signal)**2))
            noise_amplitude = np.sqrt(np.mean(np.abs(noise)**2))
            
            snr_ratio, mask = self.safe_divide(signal_amplitude, noise_amplitude, default=float('inf'))
            snr_db = 20 * np.log10(snr_ratio)
            
        elif method == 'peak':
            # 使用峰值
            signal_peak = np.max(np.abs(signal))
            noise_rms = np.sqrt(np.mean(np.abs(noise)**2))
            
            snr_ratio, mask = self.safe_divide(signal_peak, noise_rms, default=float('inf'))
            snr_db = 20 * np.log10(snr_ratio)
            
        else:
            raise ValueError(f"未知 SNR 计算方法: {method}")
        
        print(f"  信号统计: 均值={np.mean(signal):.3g}, 标准差={np.std(signal):.3g}")
        print(f"  噪声统计: 均值={np.mean(noise):.3g}, 标准差={np.std(noise):.3g}")
        print(f"  SNR: {snr_db:.2f} dB (比值: {snr_ratio:.3g})")
        
        return snr_db, snr_ratio
    
    def calculate_contrast_ratio(self, high_value, low_value):
        """计算对比度"""
        
        print(f"计算对比度...")
        
        high_value = np.asarray(high_value)
        low_value = np.asarray(low_value)
        
        # 对比度 = 高值 / 低值
        contrast, mask = self.safe_divide(high_value, low_value, default=float('inf'))
        
        # 转换为 dB
        contrast_db = 10 * np.log10(contrast)
        
        print(f"  高值范围: [{np.min(high_value):.3g}, {np.max(high_value):.3g}]")
        print(f"  低值范围: [{np.min(low_value):.3g}, {np.max(low_value):.3g}]")
        print(f"  对比度范围: [{np.min(contrast):.3g}, {np.max(contrast):.3g}]")
        print(f"  对比度(dB)范围: [{np.min(contrast_db):.2f}, {np.max(contrast_db):.2f}]")
        
        return contrast, contrast_db
    
    def normalize_by_max(self, data, epsilon=None):
        """按最大值归一化"""
        
        print(f"按最大值归一化...")
        
        data = np.asarray(data)
        
        # 找到最大值
        max_val = np.max(np.abs(data))
        
        # 安全除法
        normalized, mask = self.safe_divide(data, max_val, default=0.0, epsilon=epsilon)
        
        print(f"  最大值: {max_val:.6g}")
        print(f"  归一化后范围: [{np.min(normalized):.6g}, {np.max(normalized):.6g}]")
        
        return normalized, max_val
    
    def normalize_by_sum(self, data, epsilon=None):
        """按总和归一化"""
        
        print(f"按总和归一化...")
        
        data = np.asarray(data)
        
        # 计算总和
        total = np.sum(data)
        
        # 安全除法
        normalized, mask = self.safe_divide(data, total, default=0.0, epsilon=epsilon)
        
        print(f"  总和: {total:.6g}")
        print(f"  归一化后总和: {np.sum(normalized):.6g} (应为1.0)")
        
        return normalized, total
    
    def calculate_relative_error(self, measured, reference, method='absolute'):
        """计算相对误差（处理零参考值）"""
        
        print(f"计算相对误差 (方法: {method})...")
        
        measured = np.asarray(measured)
        reference = np.asarray(reference)
        
        if method == 'absolute':
            # 绝对误差
            error = np.abs(measured - reference)
            
        elif method == 'relative':
            # 相对误差 = |测量值 - 参考值| / |参考值|
            error, mask = self.safe_divide(
                np.abs(measured - reference),
                np.abs(reference),
                default=0.0  # 当参考值为0时，误差为0（或定义为0）
            )
            
        elif method == 'percentage':
            # 百分比误差
            relative, mask = self.safe_divide(
                np.abs(measured - reference),
                np.abs(reference),
                default=0.0
            )
            error = relative * 100
            
        else:
            raise ValueError(f"未知误差计算方法: {method}")
        
        # 统计
        error_stats = {
            'mean': np.mean(error),
            'std': np.std(error),
            'max': np.max(error),
            'min': np.min(error),
            'median': np.median(error),
            'rms': np.sqrt(np.mean(error**2))
        }
        
        print(f"  误差统计:")
        for key, value in error_stats.items():
            print(f"    {key}: {value:.6g}")
        
        return error, error_stats
    
    def handle_extreme_values(self, data, threshold=1e-10, replacement=0.0):
        """处理极端值（接近零的值）"""
        
        print(f"处理极端值...")
        print(f"  阈值: {threshold}")
        print(f"  替换值: {replacement}")
        
        data = np.asarray(data)
        
        # 找到接近零的值
        near_zero = np.abs(data) < threshold
        count_near_zero = np.sum(near_zero)
        
        if count_near_zero > 0:
            print(f"  找到 {count_near_zero} 个接近零的值 ({count_near_zero/data.size*100:.1f}%)")
            
            # 创建处理后的数据
            processed = data.copy()
            processed[near_zero] = replacement
            
            # 统计变化
            change_stats = {
                'original_mean': np.mean(data),
                'processed_mean': np.mean(processed),
                'original_std': np.std(data),
                'processed_std': np.std(processed),
                'max_change': np.max(np.abs(processed - data))
            }
            
            print(f"  处理前后统计:")
            print(f"    均值: {change_stats['original_mean']:.6g} → {change_stats['processed_mean']:.6g}")
            print(f"    标准差: {change_stats['original_std']:.6g} → {change_stats['processed_std']:.6g}")
            print(f"    最大变化: {change_stats['max_change']:.6g}")
            
            return processed, near_zero, change_stats
        else:
            print(f"  没有找到接近零的值")
            return data, near_zero, None

# 创建数值稳定性工具
stability = NumericalStability(fdtd)

# 测试数据
print("\n创建测试数据...")
np.random.seed(123)

# 包含零和接近零值的数据
data_with_zeros = np.array([1.0, 2.0, 0.0, 4.0, 1e-15, -1e-16, 5.0, 0.0, 3.0])
divisor_with_zeros = np.array([2.0, 1.0, 1.0, 0.0, 2.0, 2.0, 1e-14, 3.0, 1.0])

print("被除数:", data_with_zeros)
print("除数:", divisor_with_zeros)

# 1. 安全除法测试
print("\n" + "="*50)
print("安全除法测试")
print("="*50)

result_safe, mask_zero = stability.safe_divide(data_with_zeros, divisor_with_zeros, default=np.nan)

print("安全除法结果:")
for i, (num, den, res, mask) in enumerate(zip(data_with_zeros, divisor_with_zeros, result_safe, mask_zero)):
    status = " (除零)" if mask else ""
    print(f"  {num:.2e} ÷ {den:.2e} = {res:.2e}{status}")

# 2. 直接除法（对比）
print("\n直接除法结果（可能包含无穷大或NaN）:")
try:
    result_direct = fdtd.divide(data_with_zeros, divisor_with_zeros)
    print(result_direct)
except Exception as e:
    print(f"  直接除法出错: {e}")

# 3. 信噪比计算
print("\n" + "="*50)
print("信噪比计算测试")
print("="*50)

# 创建信号和噪声
t = np.linspace(0, 1, 1000)
signal = np.sin(2 * np.pi * 10 * t)  # 10 Hz 正弦波
noise_weak = 0.1 * np.random.randn(len(t))  # 弱噪声
noise_strong = 1.0 * np.random.randn(len(t))  # 强噪声
noise_zero = np.zeros_like(t)  # 零噪声

print("测试1: 弱噪声")
snr_weak_db, snr_weak_ratio = stability.calculate_snr(signal, noise_weak, 'power')

print("\n测试2: 强噪声")
snr_strong_db, snr_strong_ratio = stability.calculate_snr(signal, noise_strong, 'power')

print("\n测试3: 零噪声（理论上 SNR 无穷大）")
snr_zero_db, snr_zero_ratio = stability.calculate_snr(signal, noise_zero, 'power')

# 4. 对比度计算
print("\n" + "="*50)
print("对比度计算测试")
print("="*50)

high_values = np.array([10.0, 100.0, 1000.0, 1e6])
low_values = np.array([1.0, 0.1, 1e-6, 0.0])  # 包含零

contrast, contrast_db = stability.calculate_contrast_ratio(high_values, low_values)

print("\n详细对比度:")
for i, (high, low, c, c_db) in enumerate(zip(high_values, low_values, contrast, contrast_db)):
    if low == 0:
        print(f"  {high:.2e} ÷ {low:.2e} = ∞ ({c_db:.1f} dB)")
    else:
        print(f"  {high:.2e} ÷ {low:.2e} = {c:.2e} ({c_db:.1f} dB)")

# 5. 归一化测试
print("\n" + "="*50)
print("归一化测试")
print("="*50)

# 创建包含零和负值的数据
test_data = np.array([0.0, 1.0, -2.0, 3.0, -4.0, 5.0, 0.0, -1e-10, 1e-10])

print("原始数据:", test_data)

# 按最大值归一化
normalized_max, max_val = stability.normalize_by_max(test_data, epsilon=1e-12)
print("\n按最大值归一化结果:", normalized_max)

# 按总和归一化
normalized_sum, total = stability.normalize_by_sum(test_data, epsilon=1e-12)
print("\n按总和归一化结果:", normalized_sum)
print(f"验证总和: {np.sum(normalized_sum):.6g}")

# 6. 误差计算测试
print("\n" + "="*50)
print("误差计算测试")
print("="*50)

# 创建测量值和参考值
measured_data = np.array([1.01, 2.05, 0.99, 4.02, 0.0])
reference_data = np.array([1.00, 2.00, 1.00, 4.00, 0.0])

print("测量值:", measured_data)
print("参考值:", reference_data)

# 绝对误差
error_abs, stats_abs = stability.calculate_relative_error(measured_data, reference_data, 'absolute')

# 相对误差
error_rel, stats_rel = stability.calculate_relative_error(measured_data, reference_data, 'relative')

# 百分比误差
error_pct, stats_pct = stability.calculate_relative_error(measured_data, reference_data, 'percentage')

print("\n误差对比:")
for i, (meas, ref, e_abs, e_rel, e_pct) in enumerate(zip(measured_data, reference_data, error_abs, error_rel, error_pct)):
    if ref == 0:
        print(f"  [{i}] {meas:.3f} vs {ref:.3f}: 绝对误差={e_abs:.3f}, 相对误差={e_rel:.3f} (参考值为零)")
    else:
        print(f"  [{i}] {meas:.3f} vs {ref:.3f}: 绝对误差={e_abs:.3f}, 相对误差={e_rel:.3f}, 百分比误差={e_pct:.2f}%")

# 7. 极端值处理
print("\n" + "="*50)
print("极端值处理测试")
print("="*50)

# 创建包含极端值的数据
extreme_data = np.array([1.0, 1e-12, -1e-13, 2.0, 1e-15, -1e-20, 3.0, 0.0, 1e-10])

print("原始数据:", extreme_data)

processed_data, near_zero_mask, change_stats = stability.handle_extreme_values(
    extreme_data, 
    threshold=1e-12,
    replacement=0.0
)

print("\n处理后的数据:", processed_data)

print("\n数值稳定性和特殊处理演示完成!")
```

## 注意事项

1. **除零处理**：`divide` 命令对除零的处理取决于 Lumerical 设置。通常返回 `inf`（无穷大）或 `nan`（非数字）。

2. **数值精度**：浮点数除法可能存在数值误差，特别是对于非常小或非常大的数字。

3. **矩阵除法**：`divide` 默认执行元素级除法。对于矩阵除法（如求解线性方程组），可能需要使用 `inv` 或 `pinv` 命令。

4. **复数支持**：`divide` 完全支持复数运算，遵循标准的复数除法规则。

5. **广播规则**：当数组形状不同时，`divide` 遵循广播规则。确保理解广播行为以避免意外结果。

6. **性能考虑**：对于大型数组，除法操作可能消耗大量内存和计算资源。

7. **数据类型**：除法操作可能改变数据类型（如整数除法产生浮点数）。

8. **并行计算**：对于非常大的数组，考虑使用并行计算或分块处理。

9. **数值稳定性**：在除法前检查分母是否接近零，避免数值不稳定。

10. **单位一致性**：在物理计算中，确保被除数和除数具有兼容的单位。

## 错误处理

使用 `divide` 命令时可能遇到的常见错误及其解决方案：

### 1. 除零错误
- **错误信息**: `"Division by zero"` 或结果包含 `inf`/`nan`
- **原因**: 分母为零或接近零
- **解决方案**:
  ```lumerical
  // 安全除法：检查分母是否为零
  function safe_divide(numerator, denominator, default_value=0)
      if (abs(denominator) < 1e-12) {
          return default_value;
      } else {
          return divide(numerator, denominator);
      }
  end
  
  // 使用安全除法
  result = safe_divide(a, b);
  ```

### 2. 形状不匹配错误
- **错误信息**: `"Array dimensions must agree"`
- **原因**: 数组形状不兼容，且无法广播
- **解决方案**:
  ```lumerical
  // 检查并调整数组形状
  function broadcast_divide(a, b)
      // 获取形状
      size_a = size(a);
      size_b = size(b);
      
      // 如果标量，广播
      if (length(size_a) == 1 && size_a(1) == 1) {
          // a 是标量
          result = b;
          for (i = 1:length(b)) {
              result(i) = a / b(i);
          }
          return result;
      } elseif (length(size_b) == 1 && size_b(1) == 1) {
          // b 是标量
          result = a;
          for (i = 1:length(a)) {
              result(i) = a(i) / b;
          }
          return result;
      } else {
          // 尝试 reshape 或报错
          ? "错误: 数组形状不兼容";
          return 0;
      }
  end
  ```

### 3. 数据类型错误
- **错误信息**: `"Invalid data type"`
- **原因**: 输入参数不是数值类型
- **解决方案**:
  ```lumerical
  // 类型检查和转换
  function checked_divide(a, b)
      // 转换为数值类型
      if (!isnumeric(a)) {
          a = str2num(a);
      }
      if (!isnumeric(b)) {
          b = str2num(b);
      }
      
      // 检查转换是否成功
      if (isnan(a) || isnan(b)) {
          ? "错误: 无法转换为数值类型";
          return nan;
      }
      
      return divide(a, b);
  end
  ```

### 4. 内存不足错误
- **错误信息**: `"Out of memory"`
- **原因**: 数组太大，超出可用内存
- **解决方案**:
  ```lumerical
  // 分块处理大数组
  function chunked_divide(a, b, chunk_size=1000)
      total_size = length(a);
      result = zeros(total_size);
      
      for (i = 1:chunk_size:total_size) {
          end_idx = min(i + chunk_size - 1, total_size);
          chunk_a = a(i:end_idx);
          chunk_b = b(i:end_idx);
          result(i:end_idx) = divide(chunk_a, chunk_b);
          ? "处理块 " + num2str(i) + " 到 " + num2str(end_idx);
      }
      
      return result;
  end
  ```

### 5. 数值溢出/下溢
- **错误信息**: `"Numerical overflow"` 或结果异常大/小
- **原因**: 分子或分母的值极端，超出浮点范围
- **解决方案**:
  ```lumerical
  // 数值稳定的除法
  function stable_divide(a, b)
      // 缩放以避免溢出
      scale = 1.0;
      max_val = max(abs(a), abs(b));
      
      if (max_val > 1e100) {
          scale = 1e-100;
      } elseif (max_val < 1e-100) {
          scale = 1e100;
      }
      
      a_scaled = a * scale;
      b_scaled = b * scale;
      
      return divide(a_scaled, b_scaled) / scale;
  end
  ```

### 6. Python API 错误处理示例
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def safe_divide_python(a, b, default=np.nan):
    """安全的除法函数"""
    try:
        # 尝试除法
        result = fdtd.divide(a, b)
        
        # 检查无效值
        if np.any(np.isinf(result)):
            print("警告: 结果包含无穷大")
            result = np.where(np.isinf(result), default, result)
        
        if np.any(np.isnan(result)):
            print("警告: 结果包含 NaN")
            result = np.where(np.isnan(result), default, result)
        
        return result
        
    except ZeroDivisionError:
        print("错误: 除零错误")
        if np.isscalar(a) and np.isscalar(b):
            return default
        else:
            shape = np.broadcast(a, b).shape
            return np.full(shape, default)
    
    except ValueError as e:
        print(f"值错误: {e}")
        # 尝试广播
        try:
            a_arr = np.asarray(a)
            b_arr = np.asarray(b)
            result = np.divide(a_arr, b_arr)
            return result
        except:
            raise e
    
    except Exception as e:
        print(f"未知错误: {e}")
        raise

# 使用示例
a = np.array([1.0, 2.0, 3.0])
b = np.array([0.0, 1.0, 2.0])  # 包含零

result = safe_divide_python(a, b, default=0.0)
print(f"安全除法结果: {result}")
```

### 7. 调试建议
1. **检查输入值**: 打印输入数组的形状、范围和数据类型
2. **逐步计算**: 将复杂除法分解为简单步骤
3. **验证结果**: 使用替代方法验证除法结果
4. **监控内存**: 对大数组操作监控内存使用
5. **异常处理**: 使用 try-catch 块包装关键操作

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 所有数组操作 |
| MODE Solutions | ✅ 完全支持 | 所有数组操作 |
| DEVICE | ✅ 完全支持 | 所有数组操作 |
| INTERCONNECT | ✅ 完全支持 | 所有数组操作 |

## 相关命令

- `multiply` - 数组乘法
- `add` - 数组加法
- `subtract` - 数组减法
- `inv` - 矩阵求逆
- `pinv` - 伪逆矩阵
- `matrix` - 创建矩阵
- `abs` - 绝对值（用于除法后的幅度）
- `real` - 实部（复数除法）
- `imag` - 虚部（复数除法）
- `conj` - 共轭（复数除法）

## 版本历史

| 版本 | 日期 | 修改说明 |
|------|------|----------|
| 1.0 | 2026-01-31 | 初始版本，包含基本除法操作和示例 |
| 1.1 | 2026-01-31 | 添加错误处理章节、版本历史和参考 |
| 1.2 | 2026-01-31 | 完善数值稳定性和高级应用示例 |

## 参考

1. Lumerical Script Language Reference - Mathematical Operations
2. Lumerical Python API Documentation - `divide()` Method
3. Numerical Recipes: The Art of Scientific Computing - Division Algorithms
4. IEEE 754 Floating-Point Arithmetic Standard
5. NumPy Documentation - Division and Broadcasting Rules

---

*最后更新: 2026-01-31*  
*文档版本: 1.2*