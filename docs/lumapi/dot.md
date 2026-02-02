# `dot` - 向量点积

## 概述

`dot` 命令用于计算两个向量的点积（标量积）。在 Lumerical 脚本中，该命令支持实数向量、复数向量以及高维数组的点积运算。点积是向量分析、电磁场计算和光学仿真中的基本数学工具。

主要功能：
- **向量点积**：计算两个向量的标量积
- **复数点积**：支持复数向量的点积（使用第一个向量的共轭）
- **多维数组点积**：沿指定轴计算数组的点积
- **张量收缩**：支持高维张量的收缩运算
- **物理量计算**：用于计算功率、能量、通量等物理量

典型应用：
- 电磁场功率计算（E·D, H·B）
- 坡印廷矢量计算（E×H 的点积）
- 向量投影和夹角计算
- 正交性检验
- 模式重叠积分计算
- 张量运算和收缩

## 语法

### LSF 语法
```lumerical
dot(a, b);           # 返回向量 a 和 b 的点积
dot(a, b, axis);     # 沿指定轴计算点积
dot(result, a, b);   # 将点积结果存储到 result
```

### Python API
```python
session.dot(a, b)           # 返回向量 a 和 b 的点积
session.dot(a, b, axis)     # 沿指定轴计算点积
session.dot(result, a, b)   # 将点积结果存储到 result
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `a` | array | 第一个向量或数组。 | 是 |
| `b` | array | 第二个向量或数组。 | 是 |
| `axis` | integer | 计算点积的轴（对于多维数组）。默认值：最后一个轴。 | 否 |
| `result` | variable | 存储结果的变量名称。 | 否 |

## 配置属性

`dot` 命令通常不通过 `set` 命令配置属性，但点积行为受以下因素影响：

| 相关属性 | 类型 | 默认值 | 描述 |
|----------|------|--------|------|
| `conjugate first` | bool | true | 对于复数向量，是否对第一个向量取共轭。 |
| `normalize` | bool | false | 是否在计算前对向量进行归一化。 |
| `precision` | number | 1e-12 | 数值精度（用于判断向量长度是否为零）。 |
| `broadcast` | bool | true | 是否允许广播操作。 |
| `output type` | string | "auto" | 输出数据类型："auto"（自动），"real"（实数），"complex"（复数）。 |

## 使用示例

### 示例 1：基本点积操作
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("基本点积操作演示...")

# 实数向量点积
a = np.array([1.0, 2.0, 3.0])
b = np.array([4.0, 5.0, 6.0])
dot_result = fdtd.dot(a, b)
print(f"实数点积: a·b = {dot_result}")
print(f"验证 (NumPy): {np.dot(a, b)}")

# 复数向量点积
c = np.array([1+2j, 3+4j, 5+6j])
d = np.array([2+1j, 4+3j, 6+5j])
dot_complex = fdtd.dot(c, d)
print(f"\n复数点积: c·d = {dot_complex}")
print(f"验证 (NumPy 共轭点积): {np.vdot(c, d)}")  # vdot 使用第一个向量的共轭

# 不同长度向量（错误处理）
try:
    short_vec = np.array([1, 2])
    long_vec = np.array([1, 2, 3])
    fdtd.dot(short_vec, long_vec)
except Exception as e:
    print(f"\n长度不匹配错误: {e}")

# 高维点积
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
# 沿最后一个轴（默认）点积：对每行进行点积
dot_matrix = fdtd.dot(matrix1, matrix2)
print(f"\n矩阵点积（沿最后一个轴）:")
print(f"矩阵1:\n{matrix1}")
print(f"矩阵2:\n{matrix2}")
print(f"点积结果: {dot_matrix}")
print(f"形状: {dot_matrix.shape}")

# 沿指定轴点积
matrix3 = np.array([[1, 2, 3], [4, 5, 6]])
matrix4 = np.array([[7, 8, 9], [10, 11, 12]])
dot_axis0 = fdtd.dot(matrix3, matrix4, axis=0)  # 沿第0轴（列）点积
dot_axis1 = fdtd.dot(matrix3, matrix4, axis=1)  # 沿第1轴（行）点积
print(f"\n沿轴点积:")
print(f"沿 axis=0: {dot_axis0}")
print(f"沿 axis=1: {dot_axis1}")

# 存储结果到变量
fdtd.eval("dot_result = 0;")
fdtd.dot("dot_result", a, b)
result_var = fdtd.get("dot_result")
print(f"\n存储结果: a·b = {result_var}")
```

### 示例 2：电磁场物理量计算
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("电磁场物理量计算演示...")

class ElectromagneticCalculator:
    """电磁场计算器"""
    
    def __init__(self, session):
        self.session = session
    
    def calculate_poynting_vector(self, E_field, H_field):
        """计算坡印廷矢量 S = E × H"""
        
        print(f"计算坡印廷矢量...")
        print(f"  电场形状: {E_field.shape}")
        print(f"  磁场形状: {H_field.shape}")
        
        # 假设 E_field 和 H_field 是三维向量场 (Nx×Ny×Nz×3)
        # 这里简化演示：计算点积相关的量
        
        # 计算能量密度：E·D + H·B（假设线性介质，D=εE, B=μH）
        # 简化：假设 ε=μ=1
        energy_density = np.zeros_like(E_field[..., 0])
        
        # 对于每个位置，计算点积
        for i in range(E_field.shape[-1]):
            energy_density += E_field[..., i] * E_field[..., i] + \
                             H_field[..., i] * H_field[..., i]
        
        print(f"  能量密度范围: [{np.min(energy_density):.3e}, {np.max(energy_density):.3e}]")
        return energy_density
    
    def calculate_power_flow(self, E_field, H_field, normal_vector):
        """计算通过表面的功率流：∫(E × H)·dA"""
        
        print(f"计算功率流...")
        
        # 假设 E_field, H_field 是表面上的场分布
        # normal_vector 是表面法向量
        
        # 计算坡印廷矢量：S = E × H
        # 简化：只计算点积 S·n
        
        # 创建坡印廷矢量（三维）
        S_x = E_field[..., 1] * H_field[..., 2] - E_field[..., 2] * H_field[..., 1]
        S_y = E_field[..., 2] * H_field[..., 0] - E_field[..., 0] * H_field[..., 2]
        S_z = E_field[..., 0] * H_field[..., 1] - E_field[..., 1] * H_field[..., 0]
        
        # 计算法向分量
        if normal_vector.ndim == 1:
            # 常数法向量
            S_normal = (S_x * normal_vector[0] + 
                       S_y * normal_vector[1] + 
                       S_z * normal_vector[2])
        else:
            # 位置相关法向量
            S_normal = (S_x * normal_vector[..., 0] + 
                       S_y * normal_vector[..., 1] + 
                       S_z * normal_vector[..., 2])
        
        # 积分（简单求和）
        total_power = np.sum(S_normal)
        
        print(f"  总功率流: {total_power:.3e}")
        print(f"  法向分量范围: [{np.min(S_normal):.3e}, {np.max(S_normal):.3e}]")
        
        return total_power, S_normal
    
    def calculate_mode_overlap(self, mode1, mode2):
        """计算模式重叠积分：∫(E1*·E2 + H1*·H2)dV"""
        
        print(f"计算模式重叠积分...")
        
        # 假设 mode1, mode2 是包含 E 和 H 场的字典
        E1 = mode1.get('E', np.zeros((10, 10, 3)))
        H1 = mode1.get('H', np.zeros((10, 10, 3)))
        E2 = mode2.get('E', np.zeros((10, 10, 3)))
        H2 = mode2.get('H', np.zeros((10, 10, 3)))
        
        # 计算重叠积分
        overlap = 0.0
        
        # 对每个分量计算点积并求和
        for i in range(3):
            # E 场重叠（使用第一个场的共轭）
            E_overlap = np.sum(np.conj(E1[..., i]) * E2[..., i])
            # H 场重叠
            H_overlap = np.sum(np.conj(H1[..., i]) * H2[..., i])
            
            overlap += E_overlap + H_overlap
        
        # 归一化
        norm1 = self.calculate_mode_norm(mode1)
        norm2 = self.calculate_mode_norm(mode2)
        
        normalized_overlap = overlap / (np.sqrt(norm1 * norm2))
        
        print(f"  重叠积分: {overlap:.6g}")
        print(f"  模式1范数: {norm1:.6g}")
        print(f"  模式2范数: {norm2:.6g}")
        print(f"  归一化重叠: {normalized_overlap:.6g}")
        
        return normalized_overlap
    
    def calculate_mode_norm(self, mode):
        """计算模式范数：∫(|E|² + |H|²)dV"""
        
        E = mode.get('E', np.zeros((10, 10, 3)))
        H = mode.get('H', np.zeros((10, 10, 3)))
        
        norm = 0.0
        
        for i in range(3):
            norm += np.sum(np.abs(E[..., i])**2) + np.sum(np.abs(H[..., i])**2)
        
        return norm
    
    def calculate_energy(self, field, epsilon=1.0, mu=1.0):
        """计算场能量：½∫(ε|E|² + μ|H|²)dV"""
        
        print(f"计算场能量...")
        
        if isinstance(field, dict) and 'E' in field and 'H' in field:
            E = field['E']
            H = field['H']
            
            energy_E = 0.0
            energy_H = 0.0
            
            for i in range(3):
                energy_E += np.sum(np.abs(E[..., i])**2)
                energy_H += np.sum(np.abs(H[..., i])**2)
            
            total_energy = 0.5 * (epsilon * energy_E + mu * energy_H)
            
            print(f"  电场能量: {0.5*epsilon*energy_E:.3e}")
            print(f"  磁场能量: {0.5*mu*energy_H:.3e}")
            print(f"  总能量: {total_energy:.3e}")
            
            return total_energy
        else:
            # 标量场能量
            energy = 0.5 * np.sum(np.abs(field)**2)
            print(f"  标量场能量: {energy:.3e}")
            return energy
    
    def calculate_flux(self, vector_field, surface_normal):
        """计算通量：∫(F·n)dA"""
        
        print(f"计算通量...")
        print(f"  向量场形状: {vector_field.shape}")
        
        # 假设 vector_field 是 (Nx, Ny, Nz, 3) 或 (Nx, Ny, 3)
        # surface_normal 是法向量
        
        # 计算点积 F·n
        if vector_field.ndim == 4:  # 三维场
            flux_density = (vector_field[..., 0] * surface_normal[0] +
                          vector_field[..., 1] * surface_normal[1] +
                          vector_field[..., 2] * surface_normal[2])
        elif vector_field.ndim == 3:  # 二维场
            flux_density = (vector_field[..., 0] * surface_normal[0] +
                          vector_field[..., 1] * surface_normal[1])
        
        # 积分（求和）
        total_flux = np.sum(flux_density)
        
        print(f"  通量密度范围: [{np.min(flux_density):.3e}, {np.max(flux_density):.3e}]")
        print(f"  总通量: {total_flux:.3e}")
        
        return total_flux, flux_density

# 创建电磁场计算器
em_calc = ElectromagneticCalculator(fdtd)

# 生成测试电磁场数据
print("\n生成测试电磁场数据...")
np.random.seed(42)

# 创建二维网格
x = np.linspace(-1, 1, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)

# 创建电场（TE 模式：Ez 分量）
Ez = np.exp(-(X**2 + Y**2) / 0.2) * np.exp(1j * 10 * X)  # 复数场
Ex = 0.1 * Y * Ez  # 小的 x 分量
Ey = -0.1 * X * Ez  # 小的 y 分量

# 创建磁场（从电场计算，假设平面波）
Hx = -Ey  # 简化关系
Hy = Ex
Hz = np.zeros_like(Ez)

# 组合成向量场
E_field = np.stack([Ex, Ey, Ez], axis=-1)  # (50, 50, 3)
H_field = np.stack([Hx, Hy, Hz], axis=-1)

print(f"电场形状: {E_field.shape}")
print(f"磁场形状: {H_field.shape}")

# 创建模式数据
mode1 = {
    'E': E_field,
    'H': H_field
}

# 创建略有不同的模式2
mode2 = {
    'E': E_field * np.exp(1j * 0.1) * (1 + 0.05 * np.random.randn(*E_field.shape)),
    'H': H_field * np.exp(1j * 0.1) * (1 + 0.05 * np.random.randn(*H_field.shape))
}

# 执行各种计算
print("\n" + "="*50)
print("电磁场物理量计算结果")
print("="*50)

# 1. 能量密度计算
energy_density = em_calc.calculate_poynting_vector(E_field.real, H_field.real)

# 2. 功率流计算（假设表面法向为 z 方向）
normal_vector = np.array([0, 0, 1])
total_power, S_normal = em_calc.calculate_power_flow(E_field.real, H_field.real, normal_vector)

# 3. 模式重叠计算
overlap = em_calc.calculate_mode_overlap(mode1, mode2)
print(f"\n模式重叠: {overlap:.6f} (1.0 表示完全相同)")

# 4. 场能量计算
energy = em_calc.calculate_energy(mode1, epsilon=1.0, mu=1.0)

# 5. 通量计算（使用坡印廷矢量作为向量场）
# 计算坡印廷矢量
S_x = E_field[..., 1].real * H_field[..., 2].real - E_field[..., 2].real * H_field[..., 1].real
S_y = E_field[..., 2].real * H_field[..., 0].real - E_field[..., 0].real * H_field[..., 2].real
S_z = E_field[..., 0].real * H_field[..., 1].real - E_field[..., 1].real * H_field[..., 0].real

S_vector = np.stack([S_x, S_y, S_z], axis=-1)

flux, flux_density = em_calc.calculate_flux(S_vector, normal_vector)
print(f"\n坡印廷矢量通量: {flux:.3e} (应与功率流一致)")

# 6. 验证能量守恒（简化）
print(f"\n能量守恒检查:")
print(f"  计算的总功率: {total_power:.3e}")
print(f"  计算的场能量: {energy:.3e}")
# 注意：在时谐场中，功率和能量通过频率相关

print("\n电磁场计算完成!")
```

### 示例 3：几何和投影计算
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("几何和投影计算演示...")

class GeometryCalculator:
    """几何计算器"""
    
    def __init__(self, session):
        self.session = session
    
    def calculate_angle_between_vectors(self, v1, v2, degrees=True):
        """计算两个向量之间的夹角"""
        
        print(f"计算向量夹角...")
        print(f"  向量1: {v1}, 长度: {np.linalg.norm(v1):.3f}")
        print(f"  向量2: {v2}, 长度: {np.linalg.norm(v2):.3f}")
        
        # 计算点积
        dot_product = self.session.dot(v1, v2)
        
        # 计算长度
        norm1 = np.sqrt(self.session.dot(v1, v1))
        norm2 = np.sqrt(self.session.dot(v2, v2))
        
        # 避免除零
        if norm1 == 0 or norm2 == 0:
            print("  警告: 零长度向量")
            return None
        
        # 计算余弦值
        cos_theta = dot_product / (norm1 * norm2)
        
        # 限制在 [-1, 1] 范围内（处理数值误差）
        cos_theta = max(-1.0, min(1.0, cos_theta))
        
        # 计算角度
        angle_rad = np.arccos(cos_theta)
        
        if degrees:
            angle = np.degrees(angle_rad)
            print(f"  夹角: {angle:.2f}°")
        else:
            angle = angle_rad
            print(f"  夹角: {angle:.3f} rad")
        
        return angle, cos_theta
    
    def calculate_projection(self, vector, onto_vector):
        """计算向量在另一个向量上的投影"""
        
        print(f"计算向量投影...")
        
        # 计算点积
        dot_product = self.session.dot(vector, onto_vector)
        
        # 计算投影长度平方
        onto_norm_sq = self.session.dot(onto_vector, onto_vector)
        
        if onto_norm_sq == 0:
            print("  警告: 投影向量长度为零")
            return np.zeros_like(vector), 0.0
        
        # 投影标量
        projection_scalar = dot_product / onto_norm_sq
        
        # 投影向量
        projection_vector = projection_scalar * onto_vector
        
        # 垂直分量
        perpendicular = vector - projection_vector
        
        # 验证正交性
        orthogonality_check = self.session.dot(projection_vector, perpendicular)
        print(f"  投影标量: {projection_scalar:.3f}")
        print(f"  投影长度: {np.linalg.norm(projection_vector):.3f}")
        print(f"  垂直分量长度: {np.linalg.norm(perpendicular):.3f}")
        print(f"  正交性检查（应接近零）: {orthogonality_check:.2e}")
        
        return projection_vector, perpendicular, projection_scalar
    
    def check_orthogonality(self, vectors, tolerance=1e-10):
        """检查一组向量的正交性"""
        
        print(f"检查正交性...")
        print(f"  向量数量: {len(vectors)}")
        
        n = len(vectors)
        orthogonality_matrix = np.zeros((n, n))
        
        for i in range(n):
            for j in range(n):
                dot = self.session.dot(vectors[i], vectors[j])
                orthogonality_matrix[i, j] = dot
                
                if i == j:
                    norm_sq = dot
                    print(f"  向量 {i} 长度平方: {norm_sq:.3f}")
        
        print(f"  点积矩阵:")
        for i in range(n):
            row = "  ".join([f"{orthogonality_matrix[i, j]:.2e}" for j in range(n)])
            print(f"    [{row}]")
        
        # 检查正交性
        is_orthogonal = True
        for i in range(n):
            for j in range(n):
                if i != j and abs(orthogonality_matrix[i, j]) > tolerance:
                    is_orthogonal = False
                    print(f"  向量 {i} 和 {j} 不正交: 点积 = {orthogonality_matrix[i, j]:.2e}")
        
        if is_orthogonal:
            print("  所有向量相互正交")
        
        # 检查正交归一
        is_orthonormal = is_orthogonal
        for i in range(n):
            if abs(orthogonality_matrix[i, i] - 1.0) > tolerance:
                is_orthonormal = False
                print(f"  向量 {i} 不是单位向量: 长度 = {np.sqrt(orthogonality_matrix[i, i]):.3f}")
        
        if is_orthonormal:
            print("  所有向量构成正交归一基")
        
        return orthogonality_matrix, is_orthogonal, is_orthonormal
    
    def gram_schmidt_orthogonalization(self, vectors, normalize=True):
        """执行 Gram-Schmidt 正交化"""
        
        print(f"执行 Gram-Schmidt 正交化...")
        print(f"  输入向量数量: {len(vectors)}")
        
        orthogonal_vectors = []
        
        for i, v in enumerate(vectors):
            print(f"\n  处理向量 {i}:")
            
            # 开始当前向量
            u = v.copy()
            
            # 减去在所有之前向量上的投影
            for j, w in enumerate(orthogonal_vectors):
                print(f"    减去在向量 {j} 上的投影")
                
                # 计算投影标量
                dot = self.session.dot(u, w)
                w_norm_sq = self.session.dot(w, w)
                
                if w_norm_sq > 0:
                    projection_scalar = dot / w_norm_sq
                    u = u - projection_scalar * w
                    
                    # 验证与 w 的正交性
                    new_dot = self.session.dot(u, w)
                    print(f"      与向量 {j} 的点积: {new_dot:.2e} (应接近零)")
            
            # 检查结果是否为零向量
            u_norm_sq = self.session.dot(u, u)
            if u_norm_sq < 1e-20:
                print(f"    结果为零向量，跳过")
                continue
            
            # 可选归一化
            if normalize:
                u_norm = np.sqrt(u_norm_sq)
                u = u / u_norm
                print(f"    归一化后长度: {np.linalg.norm(u):.6f}")
            else:
                print(f"    长度: {np.sqrt(u_norm_sq):.6f}")
            
            orthogonal_vectors.append(u)
        
        print(f"\n  正交化完成，得到 {len(orthogonal_vectors)} 个正交向量")
        
        # 验证结果
        self.check_orthogonality(orthogonal_vectors)
        
        return orthogonal_vectors
    
    def calculate_vector_triple_product(self, a, b, c):
        """计算向量三重积：a·(b×c)"""
        
        print(f"计算向量三重积 a·(b×c)...")
        
        # 使用标量三重积公式
        # a·(b×c) = b·(c×a) = c·(a×b)
        
        # 计算叉积 b×c
        cross_bc = np.array([
            b[1]*c[2] - b[2]*c[1],
            b[2]*c[0] - b[0]*c[2],
            b[0]*c[1] - b[1]*c[0]
        ])
        
        # 计算点积
        triple_product = self.session.dot(a, cross_bc)
        
        print(f"  结果: {triple_product:.6f}")
        
        # 验证循环对称性
        cross_ca = np.array([
            c[1]*a[2] - c[2]*a[1],
            c[2]*a[0] - c[0]*a[2],
            c[0]*a[1] - c[1]*a[0]
        ])
        triple_product2 = self.session.dot(b, cross_ca)
        
        cross_ab = np.array([
            a[1]*b[2] - a[2]*b[1],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]
        ])
        triple_product3 = self.session.dot(c, cross_ab)
        
        print(f"  验证循环对称性:")
        print(f"    a·(b×c): {triple_product:.6f}")
        print(f"    b·(c×a): {triple_product2:.6f}")
        print(f"    c·(a×b): {triple_product3:.6f}")
        print(f"    差异: {abs(triple_product-triple_product2):.2e}, {abs(triple_product-triple_product3):.2e}")
        
        return triple_product
    
    def calculate_parallelepiped_volume(self, a, b, c):
        """计算平行六面体体积：|a·(b×c)|"""
        
        print(f"计算平行六面体体积...")
        
        triple_product = self.calculate_vector_triple_product(a, b, c)
        volume = abs(triple_product)
        
        print(f"  体积: {volume:.6f}")
        
        # 几何解释
        area_base = np.linalg.norm(np.cross(b, c))
        height = volume / area_base if area_base > 0 else 0
        
        print(f"  底面积: {area_base:.6f}")
        print(f"  高度: {height:.6f}")
        
        return volume
    
    def calculate_tetrahedron_volume(self, a, b, c):
        """计算四面体体积：|a·(b×c)|/6"""
        
        print(f"计算四面体体积...")
        
        triple_product = self.calculate_vector_triple_product(a, b, c)
        volume = abs(triple_product) / 6.0
        
        print(f"  四面体体积: {volume:.6f}")
        
        return volume

# 创建几何计算器
geom_calc = GeometryCalculator(fdtd)

# 测试向量
print("\n创建测试向量...")
v1 = np.array([1.0, 0.0, 0.0])
v2 = np.array([0.0, 1.0, 0.0])
v3 = np.array([0.0, 0.0, 1.0])
v4 = np.array([1.0, 1.0, 0.0])
v5 = np.array([0.5, 0.5, 1.0])
v6 = np.array([1.0, 2.0, 3.0])
v7 = np.array([4.0, 5.0, 6.0])

# 1. 计算夹角
print("\n" + "="*50)
print("向量夹角计算")
print("="*50)

angle1, cos1 = geom_calc.calculate_angle_between_vectors(v1, v2)
angle2, cos2 = geom_calc.calculate_angle_between_vectors(v1, v4)
angle3, cos3 = geom_calc.calculate_angle_between_vectors(v6, v7)

# 2. 投影计算
print("\n" + "="*50)
print("向量投影计算")
print("="*50)

proj1, perp1, scalar1 = geom_calc.calculate_projection(v6, v1)
proj2, perp2, scalar2 = geom_calc.calculate_projection(v6, v4)

# 3. 正交性检查
print("\n" + "="*50)
print("正交性检查")
print("="*50)

vectors_ortho = [v1, v2, v3]
vectors_non_ortho = [v1, v4, v5]

print("测试1: 正交向量组 (v1, v2, v3)")
ortho_matrix1, is_ortho1, is_orthonormal1 = geom_calc.check_orthogonality(vectors_ortho)

print("\n测试2: 非正交向量组 (v1, v4, v5)")
ortho_matrix2, is_ortho2, is_orthonormal2 = geom_calc.check_orthogonality(vectors_non_ortho)

# 4. Gram-Schmidt 正交化
print("\n" + "="*50)
print("Gram-Schmidt 正交化")
print("="*50)

vectors_to_orthogonalize = [
    np.array([1.0, 1.0, 0.0]),
    np.array([1.0, 0.0, 1.0]),
    np.array([0.0, 1.0, 1.0]),
    np.array([1.0, 1.0, 1.0])
]

orthogonal_vectors = geom_calc.gram_schmidt_orthogonalization(vectors_to_orthogonalize, normalize=True)

# 5. 向量三重积和平行六面体体积
print("\n" + "="*50)
print("向量三重积和体积计算")
print("="*50)

# 测试向量
a = np.array([1.0, 0.0, 0.0])
b = np.array([0.0, 2.0, 0.0])
c = np.array([0.0, 0.0, 3.0])

triple_product = geom_calc.calculate_vector_triple_product(a, b, c)
volume_parallelepiped = geom_calc.calculate_parallelepiped_volume(a, b, c)
volume_tetrahedron = geom_calc.calculate_tetrahedron_volume(a, b, c)

# 验证：对于正交向量 a,b,c，体积应为 |a||b||c|
expected_volume = 1.0 * 2.0 * 3.0
print(f"\n验证正交平行六面体体积:")
print(f"  计算值: {volume_parallelepiped:.6f}")
print(f"  理论值: {expected_volume:.6f}")
print(f"  误差: {abs(volume_parallelepiped - expected_volume):.2e}")

# 6. 共线性和共面性测试
print("\n" + "="*50)
print("共线性和共面性测试")
print("="*50)

# 共线向量
colinear1 = np.array([1.0, 2.0, 3.0])
colinear2 = np.array([2.0, 4.0, 6.0])  # 2 * colinear1

# 计算夹角
angle_colinear, cos_colinear = geom_calc.calculate_angle_between_vectors(colinear1, colinear2)
print(f"共线向量夹角: {angle_colinear:.2f}° (应为 0°)")

# 共面向量测试
coplanar1 = np.array([1.0, 0.0, 0.0])
coplanar2 = np.array([0.0, 1.0, 0.0])
coplanar3 = np.array([1.0, 1.0, 0.0])  # 在 xy 平面内

triple_coplanar = geom_calc.calculate_vector_triple_product(coplanar1, coplanar2, coplanar3)
print(f"\n共面向量三重积: {triple_coplanar:.6f} (应为 0)")

# 非共面向量
non_coplanar = np.array([0.0, 0.0, 1.0])
triple_non_coplanar = geom_calc.calculate_vector_triple_product(coplanar1, coplanar2, non_coplanar)
print(f"非共面向量三重积: {triple_non_coplanar:.6f} (应为 1)")

print("\n几何计算完成!")
```

### 示例 4：张量运算和高级应用
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

print("张量运算和高级应用演示...")

class TensorOperations:
    """张量运算工具"""
    
    def __init__(self, session):
        self.session = session
    
    def tensor_dot_product(self, A, B, axes=None):
        """计算张量点积（收缩）"""
        
        print(f"计算张量点积...")
        print(f"  张量A形状: {A.shape}")
        print(f"  张量B形状: {B.shape}")
        
        if axes is None:
            # 默认：沿最后一个轴和第一个轴收缩
            axes = ((-1,), (0,))
        
        # 使用 einsum 表示法简化
        # 构建 einsum 表达式
        if len(axes) == 2 and len(axes[0]) == 1 and len(axes[1]) == 1:
            # 简单情况：一个轴的收缩
            axis_a = axes[0][0] % A.ndim
            axis_b = axes[1][0] % B.ndim
            
            # 构建 einsum 表达式
            letters = 'abcdefghijklmnopqrstuvwxyz'
            a_labels = list(letters[:A.ndim])
            b_labels = list(letters[A.ndim:A.ndim+B.ndim])
            
            # 标记要收缩的轴
            contraction_label = 'z'  # 新标签
            
            a_labels[axis_a] = contraction_label
            b_labels[axis_b] = contraction_label
            
            # 构建表达式
            einsum_expr = f"{''.join(a_labels)},{''.join(b_labels)}->{''.join([l for l in a_labels if l != contraction_label] + [l for l in b_labels if l != contraction_label])}"
            
            print(f"  Einsum 表达式: {einsum_expr}")
            
            try:
                result = np.einsum(einsum_expr, A, B)
            except:
                # 回退到手动计算
                print(f"  Einsum 失败，使用手动计算")
                result = self._manual_tensor_dot(A, B, axis_a, axis_b)
        else:
            # 复杂情况：使用手动实现
            result = self._manual_tensor_dot_general(A, B, axes)
        
        print(f"  结果形状: {result.shape}")
        
        return result
    
    def _manual_tensor_dot(self, A, B, axis_a, axis_b):
        """手动计算张量点积（简单情况）"""
        
        # 沿指定轴计算点积
        # 对于每个切片，计算点积
        
        # 重新排列轴，使收缩轴在最后
        A_axes = list(range(A.ndim))
        A_axes.remove(axis_a)
        A_axes.append(axis_a)
        A_transposed = np.transpose(A, A_axes)
        
        B_axes = list(range(B.ndim))
        B_axes.remove(axis_b)
        B_axes.insert(0, axis_b)
        B_transposed = np.transpose(B, B_axes)
        
        # 重塑为矩阵
        A_2d = A_transposed.reshape(-1, A.shape[axis_a])
        B_2d = B_transposed.reshape(B.shape[axis_b], -1)
        
        # 矩阵乘法
        result_2d = A_2d @ B_2d
        
        # 重塑回适当形状
        result_shape = A_transposed.shape[:-1] + B_transposed.shape[1:]
        result = result_2d.reshape(result_shape)
        
        # 转回原始轴顺序（除了收缩的轴）
        # 这里简化：返回重塑后的结果
        
        return result
    
    def _manual_tensor_dot_general(self, A, B, axes):
        """手动计算张量点积（通用情况）"""
        
        # 简化实现：使用 NumPy 的 tensordot
        try:
            result = np.tensordot(A, B, axes=axes)
            return result
        except:
            print("  tensordot 失败，使用更简单的方法")
            
            # 极端简化：只处理二维情况
            if A.ndim == 2 and B.ndim == 2:
                return self.session.dot(A, B, axis=1)
            else:
                raise ValueError("复杂张量收缩需要 NumPy 的 tensordot 功能")
    
    def calculate_stress_tensor(self, strain_tensor, elasticity_tensor):
        """计算应力张量：σ_ij = C_ijkl ε_kl"""
        
        print(f"计算应力张量...")
        
        # 简化：假设各向同性材料
        # 对于 3D，使用 Voigt 记号
        
        if strain_tensor.shape == (3, 3):
            # 3×3 应变张量
            # 使用各向同性胡克定律：σ = 2μ ε + λ tr(ε) I
            
            # 假设 Lamé 参数
            mu = 1.0  # 剪切模量
            lam = 1.0  # Lamé 第一参数
            
            # 迹
            trace_epsilon = np.trace(strain_tensor)
            
            # 计算应力
            stress_tensor = 2 * mu * strain_tensor + lam * trace_epsilon * np.eye(3)
            
            print(f"  应变张量:")
            print(strain_tensor)
            print(f"  应力张量:")
            print(stress_tensor)
            
            return stress_tensor
        else:
            raise ValueError(f"不支持的应变张量形状: {strain_tensor.shape}")
    
    def calculate_permittivity_tensor(self, epsilon_diag, rotation_matrix=None):
        """计算介电常数张量"""
        
        print(f"计算介电常数张量...")
        
        # 创建对角张量
        if isinstance(epsilon_diag, (list, tuple, np.ndarray)):
            epsilon_diag = np.array(epsilon_diag)
        
        if epsilon_diag.ndim == 1:
            # 对角元素
            epsilon_tensor = np.diag(epsilon_diag)
        else:
            epsilon_tensor = epsilon_diag
        
        print(f"  对角介电张量:")
        print(epsilon_tensor)
        
        # 应用旋转（如果需要）
        if rotation_matrix is not None:
            print(f"  应用旋转矩阵...")
            print(rotation_matrix)
            
            # 旋转张量：ε' = R ε R^T
            epsilon_rotated = rotation_matrix @ epsilon_tensor @ rotation_matrix.T
            
            print(f"  旋转后介电张量:")
            print(epsilon_rotated)
            
            return epsilon_rotated
        else:
            return epsilon_tensor
    
    def calculate_optical_activity(self, E_field, chirality_tensor):
        """计算光学活性（旋光性）"""
        
        print(f"计算光学活性...")
        
        # 简化模型：旋光性与 E·(χ·E) 相关
        # 其中 χ 是 chirality tensor
        
        # 计算 χ·E
        if chirality_tensor.ndim == 3:
            # 三维 chirality tensor
            chi_E = np.zeros_like(E_field)
            for i in range(3):
                for j in range(3):
                    for k in range(3):
                        chi_E[i] += chirality_tensor[i, j, k] * E_field[j] * E_field[k]
        else:
            # 简化：使用标量 chirality
            chi_E = chirality_tensor * E_field
        
        # 计算点积 E·(χ·E)
        optical_activity = self.session.dot(E_field, chi_E)
        
        print(f"  光学活性: {optical_activity:.6f}")
        
        return optical_activity
    
    def calculate_raman_tensor(self, polarizability, normal_modes):
        """计算拉曼张量"""
        
        print(f"计算拉曼张量...")
        
        # 简化：拉曼强度与 |e_i·α·e_s|² 成正比
        # 其中 α 是极化率张量，e_i 和 e_s 是入射和散射偏振
        
        if polarizability.ndim != 2 or polarizability.shape[0] != polarizability.shape[1]:
            raise ValueError("极化率必须是方阵")
        
        results = []
        
        for mode in normal_modes:
            # 计算投影
            # 简化：假设入射和散射偏振相同
            projection = self.session.dot(mode, self.session.dot(polarizability, mode))
            
            # 强度
            intensity = abs(projection)**2
            
            results.append({
                'mode': mode,
                'projection': projection,
                'intensity': intensity
            })
            
            print(f"  模式 {mode}: 投影={projection:.3f}, 强度={intensity:.3f}")
        
        return results
    
    def calculate_effective_medium(self, materials, volume_fractions):
        """计算有效介质性质"""
        
        print(f"计算有效介质性质...")
        
        # 简化：使用 Maxwell-Garnett 近似
        # 对于球形颗粒
        
        if len(materials) != len(volume_fractions):
            raise ValueError("材料和体积分数数量不匹配")
        
        # 假设材料性质是介电常数
        epsilons = materials
        fractions = np.array(volume_fractions)
        
        # 归一化体积分数
        fractions = fractions / np.sum(fractions)
        
        # 主机材料（体积分数最大的）
        host_idx = np.argmax(fractions)
        eps_host = epsilons[host_idx]
        
        # 计算有效介电常数（简化）
        eps_eff = 0.0
        for eps, f in zip(epsilons, fractions):
            # Clausius-Mossotti 关系简化
            eps_eff += f * (eps - eps_host) / (eps + 2*eps_host)
        
        eps_eff = eps_host * (1 + 2*eps_eff) / (1 - eps_eff)
        
        print(f"  主机介电常数: {eps_host:.3f}")
        print(f"  体积分数: {fractions}")
        print(f"  有效介电常数: {eps_eff:.3f}")
        
        return eps_eff

# 创建张量运算工具
tensor_tools = TensorOperations(fdtd)

# 测试张量数据
print("\n创建测试张量数据...")

# 1. 矩阵点积测试
print("\n" + "="*50)
print("矩阵点积测试")
print("="*50)

A = np.random.rand(3, 4)
B = np.random.rand(4, 5)

print(f"矩阵 A (3×4):")
print(A)
print(f"\n矩阵 B (4×5):")
print(B)

# 使用 dot 命令（矩阵乘法）
C_dot = fdtd.dot(A, B)  # 应该执行矩阵乘法
print(f"\ndot 命令结果 (3×5):")
print(C_dot)

# 验证（NumPy）
C_numpy = A @ B
print(f"\nNumPy 验证:")
print(C_numpy)
print(f"最大差异: {np.max(np.abs(C_dot - C_numpy)):.2e}")

# 2. 高阶张量收缩
print("\n" + "="*50)
print("高阶张量收缩测试")
print("="*50)

# 创建 3阶张量
T1 = np.random.rand(2, 3, 4)
T2 = np.random.rand(4, 5, 6)

print(f"张量 T1 形状: {T1.shape}")
print(f"张量 T2 形状: {T2.shape}")

# 沿 T1 的最后一个轴和 T2 的第一个轴收缩
try:
    T_contracted = tensor_tools.tensor_dot_product(T1, T2, axes=((-1,), (0,)))
    print(f"收缩后形状: {T_contracted.shape}")
    
    # 验证（使用 NumPy 的 tensordot）
    T_numpy = np.tensordot(T1, T2, axes=((-1,), (0,)))
    print(f"NumPy tensordot 形状: {T_numpy.shape}")
    print(f"最大差异: {np.max(np.abs(T_contracted - T_numpy)):.2e}")
except Exception as e:
    print(f"张量收缩失败: {e}")

# 3. 物理张量应用
print("\n" + "="*50)
print("物理张量应用测试")
print("="*50)

# 应变张量（对称）
strain = np.array([
    [0.01, 0.005, 0.0],
    [0.005, 0.02, 0.0],
    [0.0, 0.0, -0.01]
])

print(f"应变张量:")
print(strain)

stress = tensor_tools.calculate_stress_tensor(strain, None)
print(f"\n计算得到的应力张量:")
print(stress)

# 验证：对于各向同性材料，应力-应变关系
print(f"\n验证各向同性关系:")
print(f"  σ_xx = 2μ ε_xx + λ (ε_xx + ε_yy + ε_zz)")
print(f"        = 2×1×0.01 + 1×(0.01+0.02-0.01) = {stress[0, 0]:.4f}")

# 4. 介电张量
print("\n" + "="*50)
print("介电张量测试")
print("="*50)

# 单轴晶体（如方解石）
epsilon_diag = np.array([2.2, 2.2, 1.5])  # no, ne, ne
epsilon_tensor = tensor_tools.calculate_permittivity_tensor(epsilon_diag)

# 创建旋转矩阵（绕 z 轴旋转 45°）
theta = np.pi / 4
Rz = np.array([
    [np.cos(theta), -np.sin(theta), 0],
    [np.sin(theta), np.cos(theta), 0],
    [0, 0, 1]
])

epsilon_rotated = tensor_tools.calculate_permittivity_tensor(epsilon_diag, Rz)

# 5. 拉曼张量模拟
print("\n" + "="*50)
print("拉曼张量模拟")
print("="*50)

# 简化极化率张量（对称）
alpha = np.array([
    [10.0, 1.0, 0.5],
    [1.0, 8.0, 0.3],
    [0.5, 0.3, 6.0]
])

# 振动模式（归一化向量）
modes = [
    np.array([1, 0, 0]),  # x 方向
    np.array([0, 1, 0]),  # y 方向
    np.array([0, 0, 1]),  # z 方向
    np.array([1, 1, 0]) / np.sqrt(2),  # xy 平面
    np.array([1, 1, 1]) / np.sqrt(3)   # 体对角线
]

raman_results = tensor_tools.calculate_raman_tensor(alpha, modes)

# 6. 有效介质计算
print("\n" + "="*50)
print("有效介质计算测试")
print("="*50)

# 两种材料的混合物
material_eps = [2.0, 8.0]  # 介电常数
volume_frac = [0.7, 0.3]   # 体积分数

eps_eff = tensor_tools.calculate_effective_medium(material_eps, volume_frac)

# 验证界限（Wiener 界限）
eps_min = 1.0 / (0.7/2.0 + 0.3/8.0)  # 串联界限
eps_max = 0.7*2.0 + 0.3*8.0          # 并联界限

print(f"\n有效介电常数界限验证:")
print(f"  计算值: {eps_eff:.3f}")
print(f"  Wiener 下界（串联）: {eps_min:.3f}")
print(f"  Wiener 上界（并联）: {eps_max:.3f}")
print(f"  是否在界限内: {eps_min <= eps_eff <= eps_max}")

print("\n张量运算演示完成!")
```

### 示例 5：数值验证和性能测试
```python
import lumapi
import numpy as np
import time

fdtd = lumapi.FDTD()

print("数值验证和性能测试演示...")

class DotProductBenchmark:
    """点积性能测试"""
    
    def __init__(self, session):
        self.session = session
    
    def benchmark_dot_vs_numpy(self, sizes=[10, 100, 1000, 5000]):
        """比较 dot 命令与 NumPy 的性能"""
        
        print("点积性能比较测试...")
        print("大小 | Lumerical dot 时间 | NumPy dot 时间 | 比值 | 最大误差")
        print("-"*70)
        
        results = []
        
        for size in sizes:
            # 生成随机向量
            a = np.random.rand(size)
            b = np.random.rand(size)
            
            # Lumerical dot 测试
            start_lum = time.time()
            result_lum = self.session.dot(a, b)
            time_lum = time.time() - start_lum
            
            # NumPy dot 测试
            start_np = time.time()
            result_np = np.dot(a, b)
            time_np = time.time() - start_np
            
            # 误差
            error = abs(result_lum - result_np)
            
            print(f"{size:5d} | {time_lum:8.6f}s | {time_np:8.6f}s | {time_lum/time_np:6.2f} | {error:.2e}")
            
            results.append({
                'size': size,
                'time_lum': time_lum,
                'time_np': time_np,
                'ratio': time_lum / time_np,
                'error': error
            })
        
        return results
    
    def benchmark_matrix_multiplication(self, sizes=[10, 50, 100, 200]):
        """比较矩阵乘法性能"""
        
        print("\n矩阵乘法性能比较测试...")
        print("大小 | Lumerical dot 时间 | NumPy @ 时间 | 比值 | 最大误差")
        print("-"*70)
        
        results = []
        
        for size in sizes:
            # 生成随机矩阵
            A = np.random.rand(size, size)
            B = np.random.rand(size, size)
            
            # Lumerical dot 测试（矩阵乘法）
            start_lum = time.time()
            C_lum = self.session.dot(A, B)
            time_lum = time.time() - start_lum
            
            # NumPy @ 测试
            start_np = time.time()
            C_np = A @ B
            time_np = time.time() - start_np
            
            # 误差
            max_error = np.max(np.abs(C_lum - C_np))
            
            print(f"{size:5d} | {time_lum:8.6f}s | {time_np:8.6f}s | {time_lum/time_np:6.2f} | {max_error:.2e}")
            
            results.append({
                'size': size,
                'time_lum': time_lum,
                'time_np': time_np,
                'ratio': time_lum / time_np,
                'max_error': max_error
            })
        
        return results
    
    def test_numerical_accuracy(self, test_cases):
        """测试数值精度"""
        
        print("\n数值精度测试...")
        print("测试用例 | Lumerical 结果 | NumPy 结果 | 相对误差 | 通过")
        print("-"*70)
        
        results = []
        
        for i, (a, b, description) in enumerate(test_cases):
            # 计算点积
            result_lum = self.session.dot(a, b)
            result_np = np.dot(a, b) if hasattr(a, 'shape') else a * b
            
            # 计算相对误差
            if abs(result_np) > 1e-15:
                rel_error = abs(result_lum - result_np) / abs(result_np)
            else:
                rel_error = abs(result_lum - result_np)
            
            # 检查是否通过（相对误差 < 1e-10）
            passed = rel_error < 1e-10
            
            print(f"{description:20} | {result_lum:12.6e} | {result_np:12.6e} | {rel_error:8.2e} | {'✓' if passed else '✗'}")
            
            results.append({
                'case': description,
                'result_lum': result_lum,
                'result_np': result_np,
                'rel_error': rel_error,
                'passed': passed
            })
        
        return results
    
    def test_edge_cases(self):
        """测试边界情况"""
        
        print("\n边界情况测试...")
        
        test_cases = [
            # (a, b, description)
            (np.array([]), np.array([]), "空向量"),
            (np.array([0]), np.array([0]), "零标量"),
            (np.array([1e-20]), np.array([1e20]), "极小 × 极大"),
            (np.array([1e20]), np.array([1e20]), "大数"),
            (np.array([1e-20]), np.array([1e-20]), "小数"),
            (np.array([float('inf')]), np.array([1]), "无穷大"),
            (np.array([float('nan')]), np.array([1]), "NaN"),
            (np.array([1+2j]), np.array([3+4j]), "复数标量"),
        ]
        
        results = []
        
        for a, b, desc in test_cases:
            try:
                result = self.session.dot(a, b)
                print(f"{desc:15} -> 结果: {result}")
                results.append((desc, result, "成功"))
            except Exception as e:
                print(f"{desc:15} -> 错误: {e}")
                results.append((desc, None, str(e)))
        
        return results
    
    def test_memory_usage(self, max_size=10000, step=1000):
        """测试内存使用情况"""
        
        print(f"\n内存使用测试（最大大小: {max_size}）...")
        print("大小 | 成功 | 时间 | 备注")
        print("-"*50)
        
        results = []
        
        for size in range(step, max_size + 1, step):
            try:
                # 创建大向量
                a = np.random.rand(size)
                b = np.random.rand(size)
                
                # 测量时间
                start = time.time()
                result = self.session.dot(a, b)
                elapsed = time.time() - start
                
                print(f"{size:5d} | ✓ | {elapsed:.3f}s | 成功")
                results.append((size, True, elapsed, "成功"))
                
            except MemoryError:
                print(f"{size:5d} | ✗ | - | 内存不足")
                results.append((size, False, None, "内存不足"))
                break
            except Exception as e:
                print(f"{size:5d} | ✗ | - | 错误: {e}")
                results.append((size, False, None, str(e)))
                break
        
        return results

# 创建性能测试工具
benchmark = DotProductBenchmark(fdtd)

# 1. 点积性能比较
print("="*70)
print("点积性能比较")
print("="*70)

vector_results = benchmark.benchmark_dot_vs_numpy([10, 100, 1000, 5000, 10000])

# 2. 矩阵乘法性能比较
print("\n" + "="*70)
print("矩阵乘法性能比较")
print("="*70)

matrix_results = benchmark.benchmark_matrix_multiplication([10, 50, 100, 200, 300])

# 3. 数值精度测试
print("\n" + "="*70)
print("数值精度测试")
print("="*70)

accuracy_cases = [
    (np.array([1.0, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), "正交向量"),
    (np.array([1.0, 0.0, 0.0]), np.array([1.0, 0.0, 0.0]), "相同向量"),
    (np.array([1.0, 2.0, 3.0]), np.array([4.0, 5.0, 6.0]), "随机向量"),
    (np.array([1e-10, 2e-10]), np.array([3e10, 4e10]), "极端范围"),
    (np.array([1.0, 2.0]), np.array([3.0]), "广播测试"),
    (np.array([1+2j, 3+4j]), np.array([5+6j, 7+8j]), "复数向量"),
    (np.array([1.0]), np.array([2.0]), "标量"),
]

accuracy_results = benchmark.test_numerical_accuracy(accuracy_cases)

# 4. 边界情况测试
print("\n" + "="*70)
print("边界情况测试")
print("="*70)

edge_results = benchmark.test_edge_cases()

# 5. 内存使用测试
print("\n" + "="*70)
print("内存使用测试")
print("="*70)

memory_results = benchmark.test_memory_usage(max_size=20000, step=5000)

# 6. 总结
print("\n" + "="*70)
print("性能测试总结")
print("="*70)

# 分析向量点积结果
if vector_results:
    avg_ratio = np.mean([r['ratio'] for r in vector_results])
    print(f"点积平均速度比 (Lumerical/NumPy): {avg_ratio:.2f}")
    if avg_ratio > 1:
        print(f"  NumPy 平均快 {avg_ratio:.2f} 倍")
    else:
        print(f"  Lumerical 平均快 {1/avg_ratio:.2f} 倍")

# 分析矩阵乘法结果
if matrix_results:
    avg_ratio_matrix = np.mean([r['ratio'] for r in matrix_results])
    print(f"矩阵乘法平均速度比 (Lumerical/NumPy): {avg_ratio_matrix:.2f}")
    if avg_ratio_matrix > 1:
        print(f"  NumPy 平均快 {avg_ratio_matrix:.2f} 倍")
    else:
        print(f"  Lumerical 平均快 {1/avg_ratio_matrix:.2f} 倍")

# 分析数值精度
if accuracy_results:
    passed_cases = sum(1 for r in accuracy_results if r['passed'])
    total_cases = len(accuracy_results)
    print(f"数值精度: {passed_cases}/{total_cases} 个测试用例通过")
    
    if passed_cases < total_cases:
        failed = [r['case'] for r in accuracy_results if not r['passed']]
        print(f"  失败的用例: {failed}")

# 分析边界情况
if edge_results:
    successful_cases = sum(1 for r in edge_results if r[2] == "成功")
    total_edge_cases = len(edge_results)
    print(f"边界情况: {successful_cases}/{total_edge_cases} 个用例成功执行")

print("\n性能测试完成!")
```

## 注意事项

1. **复数点积约定**：Lumerical 的 `dot` 命令对于复数向量使用第一个向量的共轭，即 `dot(a,b) = sum(conj(a_i) * b_i)`。这与数学和物理中的标准内积定义一致。

2. **数组形状要求**：对于向量点积，两个向量必须长度相同。对于多维数组点积，沿指定轴的维度必须匹配。

3. **数值精度**：浮点数点积可能存在舍入误差，特别是对于长度相差很大的向量。使用双精度可以提高精度。

4. **内存使用**：对于大型数组，点积操作可能需要大量内存。考虑分块计算或使用稀疏矩阵技术。

5. **广播行为**：当数组形状不完全匹配但可广播时，`dot` 命令可能执行广播操作。理解广播规则以避免意外结果。

6. **轴参数**：`axis` 参数控制沿哪个轴计算点积。默认沿最后一个轴，这与 NumPy 的 `dot` 和 `tensordot` 行为一致。

7. **性能优化**：对于重复的点积计算，考虑预计算或使用更高效的算法（如分块、并行化）。

8. **物理单位**：在物理计算中，确保向量具有兼容的单位。点积结果的单位是两个向量单位的乘积。

9. **几何解释**：点积的几何意义包括向量投影、夹角余弦和长度计算。理解这些几何意义有助于正确应用。

10. **错误处理**：零长度向量、NaN 或 Inf 值可能导致意外结果。在关键应用中加入适当的检查和错误处理。

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 所有向量和数组操作 |
| MODE Solutions | ✅ 完全支持 | 所有向量和数组操作 |
| DEVICE | ✅ 完全支持 | 所有向量和数组操作 |
| INTERCONNECT | ✅ 完全支持 | 所有向量和数组操作 |

## 相关命令

- `cross` - 向量叉积
- `multiply` - 数组乘法（元素级）
- `add` - 数组加法
- `subtract` - 数组减法
- `norm` - 向量范数（与点积相关：norm² = dot(v,v)）
- `angle` - 计算向量夹角（基于点积）
- `project` - 向量投影
- `matrix` - 创建矩阵
- `tensordot` - 张量收缩（更通用的点积）