# eye - 创建单位矩阵

## 概述

`eye` 命令用于创建单位矩阵（对角线上为 1，其他位置为 0 的方阵）。这是线性代数和矩阵运算中的基本操作，常用于初始化、数学变换和算法实现。

### 数学定义
单位矩阵 \( I_n \) 是一个 \( n \times n \) 的方阵，满足：
\[
I_n[i,j] = \begin{cases} 
1 & \text{if } i = j \\
0 & \text{if } i \neq j 
\end{cases}
\]

### 主要特性
1. **数学恒等性**: 任何矩阵 \( A \) 与单位矩阵相乘保持不变：\( A \times I = I \times A = A \)
2. **数值稳定性**: 单位矩阵的条件数为 1，是最稳定的矩阵
3. **内存效率**: 作为特殊矩阵，Lumerical 可能采用稀疏存储
4. **初始化用途**: 常用于算法初始化、坐标系变换、滤波器设计等

### 典型应用场景
1. **线性系统求解**: 初始化线性方程组的系数矩阵
2. **坐标变换**: 作为旋转、缩放矩阵的基础
3. **滤波器设计**: 数字信号处理中的单位冲激响应
4. **算法初始化**: 优化算法、机器学习算法的初始参数
5. **测试验证**: 验证矩阵运算的正确性

## 语法

### Lumerical 脚本语言（LSF）
```lumerical
# 基本语法
eye(n);                    # 创建 n×n 单位矩阵
eye(m, n);                 # 创建 m×n 矩阵，主对角线为 1
eye(m, n, k);              # 创建 m×n 矩阵，第 k 条对角线为 1

# 简单示例
I3 = eye(3);               # 3×3 单位矩阵
I23 = eye(2, 3);           # 2×3 矩阵，主对角线为 1
I_shift = eye(4, 4, 1);    # 4×4 矩阵，第一条上对角线为 1
```

### Python API (Lumapi)
```python
# 基本调用
session.eye(n)             # 创建 n×n 单位矩阵
session.eye(m, n)          # 创建 m×n 矩阵，主对角线为 1  
session.eye(m, n, k)       # 创建 m×n 矩阵，第 k 条对角线为 1

# 返回类型
# 返回 Lumerical 矩阵对象，可通过 getdata() 获取为 numpy 数组
import numpy as np

# 创建 3×3 单位矩阵
I3 = session.eye(3)
I3_data = session.getdata("I3")  # 获取为 numpy 数组

# 或者直接使用 eval 获取数值
I3_np = np.array(session.eval("eye(3);"))
```

## 参数

| 参数 | 类型 | 必需 | 默认值 | 描述 |
|------|------|------|--------|------|
| `m` | 整数 | 否 | `n` | 矩阵的行数。如果省略，使用 `n` 的值 |
| `n` | 整数 | 是 | 无 | 矩阵的列数（如果 `m` 省略，则为方阵维度） |
| `k` | 整数 | 否 | `0` | 对角线索引：`0` 为主对角线，正数为上对角线，负数为下对角线 |

### 对角线索引说明
- `k = 0`: 主对角线（默认）
- `k > 0`: 第 k 条上对角线
- `k < 0`: 第 k 条下对角线

## 返回值

`eye` 命令返回一个 Lumerical 矩阵对象，可以用于后续的矩阵运算、数据获取或进一步处理。

### 返回值类型

| 调用方式 | 返回值类型 | 说明 |
|----------|------------|------|
| **LSF 脚本** | 矩阵变量 | 返回一个矩阵对象，存储在指定的变量中 |
| **Python API** | 字符串（矩阵名称） | 返回矩阵在 Lumerical 环境中的名称，需要使用 `getdata()` 获取实际数据 |

### 返回值使用示例

#### Lumerical 脚本语言（LSF）
```lumerical
// eye 命令直接返回矩阵对象
I = eye(3);      // I 现在是 3×3 单位矩阵

// 使用返回的矩阵
?size(I);        // 显示矩阵维度：3 3
?I;              // 显示矩阵内容

// 矩阵运算
A = rand(3,3);   // 随机矩阵
result = A * I;  // 单位矩阵乘法：A × I = A
?max(abs(result - A));  // 应接近 0（数值误差范围内）
```

#### Python API (Lumapi)
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# eye 命令返回矩阵名称
matrix_name = fdtd.eye(4)
print(f"创建的矩阵名称: {matrix_name}")

# 获取实际数据
matrix_data = fdtd.getdata(matrix_name)
print(f"矩阵维度: {matrix_data.shape}")
print(f"矩阵类型: {type(matrix_data)}")

# 验证是单位矩阵
def is_identity(matrix, tolerance=1e-12):
    """检查矩阵是否接近单位矩阵"""
    n, m = matrix.shape
    if n != m:
        return False
    return (np.allclose(np.diag(matrix), 1.0) and 
            np.allclose(matrix - np.diag(np.diag(matrix)), 0.0, atol=tolerance))

# 检查
if is_identity(matrix_data):
    print("✓ 成功创建单位矩阵")
else:
    print("✗ 创建的矩阵不是单位矩阵")
```

### 返回值处理技巧

1. **立即使用返回的矩阵**：
   ```python
   # 创建并立即使用单位矩阵
   I_name = session.eye(3)
   session.eval(f"A = rand(3,3);")
   session.eval(f"result = getdata(\"{I_name}\") * getdata(\"A\");")
   ```

2. **批量创建单位矩阵**：
   ```python
   def create_identity_matrices(sizes):
       """批量创建不同尺寸的单位矩阵"""
       matrix_names = []
       for n in sizes:
           name = session.eye(n)
           matrix_names.append(name)
       return matrix_names
   
   # 使用示例
   sizes = [2, 3, 5, 8]
   names = create_identity_matrices(sizes)
   print(f"创建的矩阵: {names}")
   ```

3. **错误处理**：
   ```python
   try:
       matrix_name = session.eye(-1)  # 无效参数
   except ValueError as e:
       print(f"参数错误: {e}")
   except RuntimeError as e:
       print(f"运行时错误: {e}")
   ```

## 使用示例

### 示例 1：基本单位矩阵操作
```python
import lumapi
import numpy as np

# 创建会话
session = lumapi.FDTD()

print("=== 基本单位矩阵操作示例 ===")

# 1. 创建 3×3 单位矩阵
I3 = session.eye(3)
I3_data = session.getdata("I3")
print(f"3×3 单位矩阵:\n{I3_data}")
print(f"形状: {I3_data.shape}")
print(f"迹（trace）: {np.trace(I3_data)}")  # 应该为 3

# 2. 验证单位矩阵性质
A = np.random.rand(3, 3)  # 随机 3×3 矩阵
A_eye = A @ I3_data       # 矩阵乘法
eye_A = I3_data @ A

print(f"\n随机矩阵 A:\n{A}")
print(f"\nA × I = A (验证): {np.allclose(A_eye, A)}")
print(f"I × A = A (验证): {np.allclose(eye_A, A)}")

# 3. 创建矩形矩阵
I23 = session.eye(2, 3)
I23_data = session.getdata("I23")
print(f"\n2×3 矩阵（主对角线为 1）:\n{I23_data}")
print(f"形状: {I23_data.shape}")

# 4. 带偏移的对角线
I_shift = session.eye(4, 4, 1)  # 第一条上对角线为 1
I_shift_data = session.getdata("I_shift")
print(f"\n4×4 矩阵，第一条上对角线为 1:\n{I_shift_data}")

# 5. 负偏移对角线
I_neg = session.eye(5, 5, -2)   # 第二条下对角线为 1  
I_neg_data = session.getdata("I_neg")
print(f"\n5×5 矩阵，第二条下对角线为 1:\n{I_neg_data}")
```

### 示例 2：线性系统求解中的应用
```python
import lumapi
import numpy as np

session = lumapi.FDTD()

print("=== 线性系统求解应用示例 ===")

# 1. 使用单位矩阵构建正则化项
n = 4
A = np.random.randn(n, n)  # 随机系数矩阵
b = np.random.randn(n, 1)   # 随机右侧向量

# 创建单位矩阵（通过 Lumerical）
I = session.eye(n)
I_data = session.getdata("I")

# 添加正则化项 λI 提高数值稳定性
lambda_reg = 0.1
A_reg = A + lambda_reg * I_data

# 求解线性系统 Ax = b
try:
    x = np.linalg.solve(A_reg, b)
    print(f"系数矩阵 A:\n{A}")
    print(f"正则化参数 λ: {lambda_reg}")
    print(f"正则化后矩阵 A + λI:\n{A_reg}")
    print(f"解 x:\n{x.flatten()}")
    
    # 验证残差
    residual = np.linalg.norm(A @ x - b)
    print(f"原始残差 ||Ax - b||: {residual:.6e}")
    
    reg_residual = np.linalg.norm(A_reg @ x - b)
    print(f"正则化残差 ||(A+λI)x - b||: {reg_residual:.6e}")
    
except np.linalg.LinAlgError as e:
    print(f"求解失败: {e}")

# 2. 构建块对角矩阵
print("\n=== 构建块对角矩阵 ===")
block_sizes = [2, 3, 2]  # 三个块的大小

# 创建块对角矩阵：diag(I1, I2, I3)
block_matrices = []
for i, size in enumerate(block_sizes):
    block = session.eye(size)
    block_data = session.getdata(f"block_{i}")
    block_matrices.append(block_data)

# 手动构建块对角矩阵（Lumerical 中没有直接的 blkdiag 函数）
total_size = sum(block_sizes)
block_diag = np.zeros((total_size, total_size))

row_start = 0
col_start = 0
for block in block_matrices:
    r, c = block.shape
    block_diag[row_start:row_start+r, col_start:col_start+c] = block
    row_start += r
    col_start += c

print(f"块对角矩阵（块大小 {block_sizes}）:")
print(f"总维度: {total_size}×{total_size}")
print(f"矩阵:\n{block_diag}")

# 3. 单位矩阵用于坐标变换
print("\n=== 坐标变换示例 ===")
# 定义旋转矩阵（绕 z 轴旋转 45 度）
theta = np.pi / 4  # 45 度
Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])

# 创建 3×3 单位矩阵作为参考
I3 = session.eye(3)
I3_data = session.getdata("I3")

print(f"参考单位矩阵 I:\n{I3_data}")
print(f"旋转矩阵 R_z(45°):\n{Rz}")
print(f"旋转矩阵性质验证:")
print(f"  R^T × R = I: {np.allclose(Rz.T @ Rz, I3_data)}")
print(f"  det(R) = 1: {np.allclose(np.linalg.det(Rz), 1.0)}")

# 应用旋转
point = np.array([1, 0, 0]).reshape(-1, 1)
point_rotated = Rz @ point
print(f"\n点 [1, 0, 0] 旋转 45° 后: {point_rotated.flatten()}")
```

### 示例 3：在光学仿真中的应用
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("=== 光学仿真中的应用示例 ===")

# 1. 创建偏振 Jones 矩阵
print("1. 偏振光学中的 Jones 矩阵")

# 创建单位矩阵作为参考
I2 = fdtd.eye(2)
I2_data = fdtd.getdata("I2")

# 定义常见偏振器的 Jones 矩阵
# 线性偏振器（水平）
J_horizontal = np.array([[1, 0], [0, 0]])

# 线性偏振器（垂直）  
J_vertical = np.array([[0, 0], [0, 1]])

# 右旋圆偏振器
J_rcp = 0.5 * np.array([[1, 1j], [-1j, 1]])

print(f"单位矩阵（无偏振变化）:\n{I2_data}")
print(f"水平偏振器:\n{J_horizontal}")
print(f"垂直偏振器:\n{J_vertical}")
print(f"右旋圆偏振器:\n{J_rcp}")

# 验证偏振器性质
E_in = np.array([1, 1])  # 45° 线偏振输入

E_hor = J_horizontal @ E_in
E_ver = J_vertical @ E_in
E_rcp = J_rcp @ E_in

print(f"\n输入电场 (45° 线偏振): {E_in}")
print(f"通过水平偏振器后: {E_hor}, 强度: {np.abs(E_hor).sum():.3f}")
print(f"通过垂直偏振器后: {E_ver}, 强度: {np.abs(E_ver).sum():.3f}")
print(f"通过右旋偏振器后: {E_rcp}, 强度: {np.abs(E_rcp).sum():.3f}")

# 2. 创建波导模式耦合矩阵
print("\n2. 波导模式耦合矩阵")

num_modes = 4
# 创建单位矩阵表示无耦合情况
I_modes = fdtd.eye(num_modes)
I_modes_data = fdtd.getdata("I_modes")

# 添加模式耦合（简化的耦合矩阵）
kappa = 0.1  # 耦合系数
C = I_modes_data.copy()

# 添加相邻模式间的耦合
for i in range(num_modes - 1):
    C[i, i+1] = kappa
    C[i+1, i] = kappa

print(f"模式数量: {num_modes}")
print(f"无耦合单位矩阵:\n{I_modes_data}")
print(f"带耦合的矩阵 (κ={kappa}):\n{C}")

# 计算模式振幅演化（简化的耦合模理论）
z = 1.0  # 传播距离
U = np.linalg.matrix_power(C, 10)  # 近似传播算符
print(f"传播算符 U(z={z}):\n{U}")

# 3. 创建光学传输矩阵
print("\n3. 多层膜传输矩阵")

num_layers = 5
# 每层的传输矩阵（简化，假设为单位矩阵）
layer_matrices = []
for i in range(num_layers):
    # 实际上每层会有不同的传输矩阵
    # 这里用单位矩阵加微小扰动模拟
    M = fdtd.eye(2)
    M_data = fdtd.getdata(f"M_{i}")
    
    # 添加微小扰动模拟实际层
    perturbation = 0.01 * np.random.randn(2, 2)
    M_perturbed = M_data + perturbation
    
    layer_matrices.append(M_perturbed)

# 计算总传输矩阵（矩阵连乘）
M_total = np.eye(2)
for M in layer_matrices:
    M_total = M_total @ M

print(f"层数: {num_layers}")
print(f"总传输矩阵:\n{M_total}")
print(f"行列式: {np.linalg.det(M_total):.6f}")  # 应该接近 1（无损耗）

# 验证互易性（对于无源系统）
print(f"满足互易性 M^T = M^-1: {np.allclose(M_total.T, np.linalg.inv(M_total))}")
```

### 示例 4：信号处理和滤波器设计
```python
import lumapi
import numpy as np
import matplotlib.pyplot as plt

session = lumapi.FDTD()

print("=== 信号处理和滤波器设计示例 ===")

# 1. 创建数字滤波器系数矩阵
print("1. 数字滤波器设计")

filter_order = 4
# 创建单位矩阵用于构建状态空间表示
I_state = session.eye(filter_order)
I_state_data = session.getdata("I_state")

# 构建 IIR 滤波器的状态空间表示（简化）
# 系统: x[n+1] = A x[n] + B u[n], y[n] = C x[n] + D u[n]

# A 矩阵（状态转移矩阵）- 接近单位矩阵但稍有变化
A = 0.95 * I_state_data  # 轻微衰减

# B 矩阵（输入矩阵）
B = np.ones((filter_order, 1))

# C 矩阵（输出矩阵）
C = np.random.randn(1, filter_order)

# D 矩阵（直接传递项）
D = np.array([[0.1]])

print(f"滤波器阶数: {filter_order}")
print(f"状态矩阵 A:\n{A}")
print(f"输入矩阵 B:\n{B}")
print(f"输出矩阵 C:\n{C}")
print(f"直接项 D:\n{D}")

# 验证系统稳定性（A 的特征值在单位圆内）
eigenvalues = np.linalg.eigvals(A)
print(f"\n系统矩阵 A 的特征值: {eigenvalues}")
print(f"最大特征值幅度: {np.max(np.abs(eigenvalues)):.4f}")
print(f"系统稳定: {np.all(np.abs(eigenvalues) < 1)}")

# 2. 创建卷积核（图像处理）
print("\n2. 图像处理卷积核")

# 创建单位脉冲响应（离散 Delta 函数）
kernel_size = 5
delta_kernel = session.eye(kernel_size)
delta_kernel_data = session.getdata("delta_kernel")

# 创建高斯模糊核（近似）
sigma = 1.0
x = np.arange(kernel_size) - kernel_size // 2
gaussian_kernel = np.exp(-x**2 / (2 * sigma**2))
gaussian_kernel_2d = np.outer(gaussian_kernel, gaussian_kernel)
gaussian_kernel_2d = gaussian_kernel_2d / gaussian_kernel_2d.sum()

print(f"卷积核大小: {kernel_size}×{kernel_size}")
print(f"单位脉冲核（Delta 函数）:")
print(delta_kernel_data)
print(f"\n高斯模糊核 (σ={sigma}):")
print(gaussian_kernel_2d)

# 3. 创建自相关矩阵
print("\n3. 信号自相关矩阵")

signal_length = 8
# 创建单位矩阵用于构建 Toeplitz 矩阵
I_base = session.eye(signal_length)
I_base_data = session.getdata("I_base")

# 创建简单的自相关序列
r = np.exp(-0.5 * np.arange(signal_length))  # 指数衰减

# 构建 Toeplitz 自相关矩阵
R = np.zeros((signal_length, signal_length))
for i in range(signal_length):
    for j in range(signal_length):
        R[i, j] = r[np.abs(i - j)]

print(f"信号长度: {signal_length}")
print(f"自相关序列 r: {r}")
print(f"自相关矩阵 R (Toeplitz):")
print(R)

# 验证性质：R 应该是对称正定矩阵
print(f"\n矩阵性质验证:")
print(f"  对称性: {np.allclose(R, R.T)}")
print(f"  正定性: {np.all(np.linalg.eigvals(R) > 0)}")

# 与单位矩阵比较
print(f"  与单位矩阵的差异范数: {np.linalg.norm(R - I_base_data):.6f}")
```

### 示例 5：高级数值算法应用
```python
import lumapi
import numpy as np
from scipy import linalg

session = lumapi.FDTD()

print("=== 高级数值算法应用示例 ===")

# 1. 矩阵分解初始化
print("1. QR 和 SVD 分解初始化")

n = 5
# 创建单位矩阵作为基准
I = session.eye(n)
I_data = session.getdata("I")

# 生成随机矩阵
A = np.random.randn(n, n)

# QR 分解
Q, R = linalg.qr(A)
print(f"随机矩阵 A:\n{A}")
print(f"\nQR 分解:")
print(f"Q 矩阵（正交）:\n{Q}")
print(f"R 矩阵（上三角）:\n{R}")

# 验证正交性：Q^T Q = I
QTQ = Q.T @ Q
print(f"\n验证 Q^T Q = I:")
print(f"Q^T Q:\n{QTQ}")
print(f"与单位矩阵的最大差异: {np.max(np.abs(QTQ - I_data)):.6e}")

# SVD 分解
U, s, Vh = linalg.svd(A)
print(f"\nSVD 分解:")
print(f"奇异值: {s}")
print(f"条件数: {s[0]/s[-1]:.4f}")

# 2. 迭代法求解线性系统
print("\n2. 迭代法求解（雅可比法）")

# 创建对角占优矩阵
n_iter = 6
A_iter = np.random.randn(n_iter, n_iter)
# 使矩阵对角占优
A_iter = A_iter + 10 * np.eye(n_iter)

b_iter = np.random.randn(n_iter)

# 雅可比迭代法：x^{(k+1)} = D^{-1}(b - (L+U)x^{(k)})
# 其中 D 是 A 的对角线部分，L+U 是非对角线部分

D = np.diag(np.diag(A_iter))
LU = A_iter - D
D_inv = np.diag(1 / np.diag(D))

x = np.zeros(n_iter)  # 初始猜测
I_jacobi = np.eye(n_iter)

max_iter = 100
tolerance = 1e-10

print(f"系数矩阵 A (对角占优):")
print(A_iter)
print(f"右侧向量 b: {b_iter}")

for k in range(max_iter):
    x_new = D_inv @ (b_iter - LU @ x)
    
    error = np.linalg.norm(x_new - x)
    if error < tolerance:
        print(f"迭代收敛于 {k+1} 次迭代，误差: {error:.6e}")
        break
    
    x = x_new

# 验证解
residual = np.linalg.norm(A_iter @ x - b_iter)
print(f"最终残差: {residual:.6e}")
print(f"解 x: {x}")

# 3. 特征值问题
print("\n3. 特征值问题与单位矩阵的关系")

# 创建对称正定矩阵
n_eig = 4
A_sym = np.random.randn(n_eig, n_eig)
A_sym = A_sym @ A_sym.T  # 使对称正定

# 计算特征值和特征向量
eigvals, eigvecs = linalg.eig(A_sym)

print(f"对称矩阵 A:\n{A_sym}")
print(f"特征值: {eigvals}")
print(f"特征向量矩阵 V:\n{eigvecs}")

# 验证特征分解：A = V Λ V^{-1}
Lambda = np.diag(eigvals)
A_reconstructed = eigvecs @ Lambda @ linalg.inv(eigvecs)

print(f"\n特征分解验证:")
print(f"重构矩阵与原始矩阵的最大差异: {np.max(np.abs(A_reconstructed - A_sym)):.6e}")

# 验证特征向量正交性：V^T V = I
VTV = eigvecs.T @ eigvecs
print(f"特征向量正交性 V^T V = I:")
print(f"与单位矩阵的最大差异: {np.max(np.abs(VTV - np.eye(n_eig))):.6e}")

# 4. 矩阵指数和动力学系统
print("\n4. 矩阵指数和连续系统")

# 连续系统：dx/dt = A x
A_cont = np.array([[-1, 2], [-2, -1]])  # 稳定系统

# 计算矩阵指数：exp(A*t)
t = 1.0
# 使用级数展开近似：exp(A) ≈ I + A + A^2/2! + A^3/3! + ...

I_exp = np.eye(2)
expA_approx = I_exp.copy()
term = I_exp.copy()

for k in range(1, 10):
    term = term @ A_cont * t / k
    expA_approx += term

# 使用 scipy 精确计算
expA_exact = linalg.expm(A_cont * t)

print(f"连续系统矩阵 A:\n{A_cont}")
print(f"时间 t = {t}")
print(f"近似矩阵指数 (10 项级数):\n{expA_approx}")
print(f"精确矩阵指数 (scipy):\n{expA_exact}")
print(f"近似误差: {np.linalg.norm(expA_approx - expA_exact):.6e}")

# 验证系统稳定性
eigvals_cont = linalg.eigvals(A_cont)
print(f"\n系统矩阵 A 的特征值: {eigvals_cont}")
print(f"实部最大特征值: {np.max(np.real(eigvals_cont)):.4f}")
print(f"系统稳定（所有特征值实部 < 0）: {np.all(np.real(eigvals_cont) < 0)}")
```

## 注意事项

### 1. 数值精度
- 单位矩阵的对角线元素在双精度浮点中应精确为 1.0
- 非对角线元素应精确为 0.0（可能存在微小的数值误差）
- 对于大矩阵，考虑内存使用和计算效率

### 2. 内存考虑
- \( n \times n \) 单位矩阵需要存储 \( n^2 \) 个元素
- Lumerical 可能对单位矩阵使用特殊存储（稀疏表示）
- 大型矩阵（>1000×1000）可能需要显著内存

### 3. 性能优化
- 对于重复使用的单位矩阵，考虑缓存结果
- 使用适当的数据类型（浮点数 vs 整数）
- 考虑使用稀疏矩阵格式处理大型单位矩阵

### 4. 应用建议
- 在算法初始化时使用单位矩阵作为默认值
- 验证矩阵运算时使用单位矩阵作为参考
- 在坐标变换中，单位矩阵表示恒等变换

### 5. 错误处理
- 维度参数应为正整数
- 过大的维度可能导致内存不足
- 对角线索引 k 应满足 |k| < min(m, n)

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| **FDTD Solutions** | 完全支持 | 用于矩阵运算和数学计算 |
| **MODE Solutions** | 完全支持 | 用于模式分析和数学计算 |
| **DEVICE** | 完全支持 | 用于电路分析和数学计算 |
| **INTERCONNECT** | 完全支持 | 用于网络分析和数学计算 |

## 相关命令

- [`ones`](./ones.md) - 创建全 1 矩阵
- [`zeros`](./zeros.md) - 创建全 0 矩阵  
- [`matrix`](./matrix.md) - 创建通用矩阵
- [`diag`](./diag.md) - 创建对角矩阵或提取对角线
- [`rand`](./rand.md) - 创建随机矩阵

## 最佳实践

### 1. 高效创建大型单位矩阵
```python
def create_large_identity(n, sparse=True):
    """高效创建大型单位矩阵"""
    if sparse and n > 100:
        # 对于大型矩阵，使用稀疏表示
        session.eval(f"I = speye({n});")  # 稀疏单位矩阵
    else:
        # 对于小型矩阵，使用标准方法
        session.eye(n)
    
    return session.getdata("I")

# 使用示例
I_large = create_large_identity(1000, sparse=True)
```

### 2. 单位矩阵验证
```python
def verify_identity(matrix, tolerance=1e-12):
    """验证矩阵是否接近单位矩阵"""
    n, m = matrix.shape
    
    if n != m:
        return False  # 不是方阵
    
    # 检查对角线元素是否为 1
    diag_diff = np.abs(np.diag(matrix) - 1.0)
    if np.any(diag_diff > tolerance):
        return False
    
    # 检查非对角线元素是否为 0
    matrix_no_diag = matrix.copy()
    np.fill_diagonal(matrix_no_diag, 0)
    off_diag_max = np.max(np.abs(matrix_no_diag))
    
    return off_diag_max < tolerance

# 使用示例
I_test = session.eye(5)
I_data = session.getdata("I_test")
is_identity = verify_identity(I_data)
print(f"矩阵是单位矩阵: {is_identity}")
```

### 3. 块单位矩阵构造
```python
def block_diagonal_identity(block_sizes):
    """构造块对角单位矩阵"""
    total_size = sum(block_sizes)
    result = np.zeros((total_size, total_size))
    
    row_start = 0
    col_start = 0
    
    for size in block_sizes:
        # 创建单位矩阵块
        block = np.eye(size)
        result[row_start:row_start+size, col_start:col_start+size] = block
        
        row_start += size
        col_start += size
    
    return result

# 使用示例
block_sizes = [2, 3, 2]
I_block = block_diagonal_identity(block_sizes)
print(f"块对角单位矩阵（块大小 {block_sizes}）:")
print(I_block)
```

## 错误处理

### 常见错误类型

| 错误类型 | 原因 | 解决方案 |
|----------|------|----------|
| **参数类型错误** | 输入参数不是整数 | 使用 `int()` 转换参数，确保输入为整型 |
| **参数范围错误** | 矩阵维度为负数或零 | 检查参数范围，确保 n, m ≥ 1 |
| **内存不足错误** | 请求的矩阵维度太大 | 减少矩阵维度，使用稀疏矩阵或分块处理 |
| **数值精度错误** | 浮点误差导致对角线元素不完全为1 | 使用容差比较，避免直接相等比较 |
| **名称冲突错误** | 矩阵名称与现有变量冲突 | 使用唯一变量名，或先检查变量是否存在 |

### Python 错误处理示例

```python
import lumapi

fdtd = lumapi.FDTD()

def safe_eye(n, m=None, k=0):
    """安全的 eye 命令包装器，包含错误处理"""
    try:
        # 参数验证
        if not isinstance(n, int) or n <= 0:
            raise ValueError(f"维度 n 必须是正整数，收到: n={n}")
        
        if m is not None:
            if not isinstance(m, int) or m <= 0:
                raise ValueError(f"维度 m 必须是正整数，收到: m={m}")
        
        if not isinstance(k, int):
            raise ValueError(f"对角线索引 k 必须是整数，收到: k={k}")
        
        # 内存检查（简单启发式）
        max_dim = max(n, m if m is not None else n)
        if max_dim > 10000:
            raise MemoryError(f"请求的矩阵维度 {max_dim} 可能过大")
        
        # 执行 eye 命令
        if m is None:
            matrix_name = fdtd.eye(n)
        elif k == 0:
            matrix_name = fdtd.eye(n, m)
        else:
            matrix_name = fdtd.eye(n, m, k)
        
        # 验证结果
        if not matrix_name or not isinstance(matrix_name, str):
            raise RuntimeError("eye 命令未返回有效的矩阵名称")
        
        print(f"成功创建矩阵: {matrix_name} (维度: {n}×{m if m else n})")
        return matrix_name
        
    except ValueError as e:
        print(f"参数错误: {e}")
        return None
        
    except MemoryError as e:
        print(f"内存错误: {e}")
        print("建议：使用稀疏矩阵或减少矩阵维度")
        return None
        
    except RuntimeError as e:
        print(f"运行时错误: {e}")
        return None
        
    except Exception as e:
        print(f"未知错误: {type(e).__name__} - {e}")
        return None

# 使用示例
# 正常情况
I3 = safe_eye(3)
if I3:
    print(f"矩阵创建成功: {I3}")

# 错误情况
I_error = safe_eye(-1)  # 无效参数
if not I_error:
    print("预期中的错误处理")

# 大型矩阵（警告）
I_large = safe_eye(5000)  # 可能触发内存警告
```

### LSF 脚本错误处理

```lumerical
// LSF 脚本中的错误处理函数
function safe_eye(n, m, k)
{
    // 参数验证
    if (!isnumber(n) || n <= 0) {
        throw("错误: 参数 n 必须是正数");
    }
    
    if (isdefined(m)) {
        if (!isnumber(m) || m <= 0) {
            throw("错误: 参数 m 必须是正数");
        }
    }
    
    if (isdefined(k)) {
        if (!isnumber(k)) {
            throw("错误: 参数 k 必须是数字");
        }
    }
    
    // 尝试创建单位矩阵
    try {
        if (!isdefined(m)) {
            I = eye(n);
        } else if (!isdefined(k)) {
            I = eye(n, m);
        } else {
            I = eye(n, m, k);
        }
        
        // 验证矩阵维度
        dim = size(I);
        if (length(dim) != 2 || dim(1) <= 0 || dim(2) <= 0) {
            throw("错误: 创建的矩阵维度无效");
        }
        
        ?"成功创建单位矩阵，维度: " + num2str(dim(1)) + "×" + num2str(dim(2));
        return I;
        
    } catch (e) {
        ?"创建单位矩阵失败: " + e;
        return [];
    }
}

// 使用示例
I1 = safe_eye(3);        // 正常情况
I2 = safe_eye(-1);       // 错误情况
I3 = safe_eye(2, 3, 0);  // 矩形矩阵

// 清理
if (isempty(I2)) {
    ?"I2 创建失败（符合预期）";
}
```

## 故障排除

### 常见问题
1. **内存不足**: 减少矩阵维度或使用稀疏矩阵
2. **数值误差**: 非对角线元素不为零（浮点误差）
3. **性能问题**: 大型矩阵操作缓慢，考虑优化算法

### 调试建议
- 首先测试小矩阵验证功能
- 检查输入参数类型和范围
- 验证输出矩阵的维度和数值
- 使用 `getdata()` 获取 numpy 数组进行进一步分析

## 版本历史

| 版本 | 日期 | 修改内容 | 修改人 |
|------|------|----------|--------|
| 1.0 | 2025-01-31 | 初始版本，包含基本语法、参数说明和示例 | 文档整理团队 |
| 1.1 | 2026-01-31 | 添加返回值章节，完善错误处理，添加版本历史 | AI Agent C |

---

*文档版本：1.0 | 最后更新：2025-01-31*