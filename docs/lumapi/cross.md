# `cross` - 向量叉积

## 概述

`cross` 命令用于计算两个三维向量的叉积（向量积）。在 Lumerical 仿真中，向量运算常用于计算电磁场、坡印廷矢量、法线向量、角动量等物理量。叉积运算产生一个垂直于输入向量平面的新向量，其大小等于输入向量构成的平行四边形的面积。

该命令在电磁场分析、光学动量计算、几何法线确定和三维矢量场处理中非常有用。

## 语法

### LSF 语法
```lumerical
result = cross(u, v);               # 计算向量 u 和 v 的叉积
```

### Python API
```python
result = session.cross(u, v)        # 计算向量 u 和 v 的叉积
```

## 参数

| 参数 | 类型 | 描述 | 必需 |
|------|------|------|------|
| `u` | array | 第一个三维向量，格式为 `[ux, uy, uz]`。 | 是 |
| `v` | array | 第二个三维向量，格式为 `[vx, vy, vz]`。 | 是 |

## 返回值

| 类型 | 描述 |
|------|------|
| array | 叉积结果向量，格式为 `[wx, wy, wz]`，其中 `w = u × v`。 |

## 叉积定义

对于两个三维向量：
- `u = [ux, uy, uz]`
- `v = [vx, vy, vz]`

叉积 `w = u × v` 定义为：
```
wx = uy * vz - uz * vy
wy = uz * vx - ux * vz
wz = ux * vy - uy * vx
```

几何意义：
- 方向：垂直于 u 和 v 所在的平面，遵循右手定则
- 大小：|w| = |u| * |v| * sin(θ)，其中 θ 是 u 和 v 之间的夹角
- 物理意义：|w| 等于以 u 和 v 为边的平行四边形的面积

## 使用示例

### 示例 1：基本叉积计算

#### LSF 脚本
```lumerical
# 定义两个向量
u = {1, 0, 0};  # x 方向单位向量
v = {0, 1, 0};  # y 方向单位向量

# 计算叉积
w = cross(u, v);

? "叉积计算:";
? "  u = " + num2str(u);
? "  v = " + num2str(v);
? "  u × v = " + num2str(w);

# 验证结果（应该是 z 方向单位向量）
expected = {0, 0, 1};
? "  期望结果: " + num2str(expected);
error = norm(w - expected);
? "  误差: " + num2str(error);

# 计算向量大小和方向
u_norm = norm(u);
v_norm = norm(v);
w_norm = norm(w);

? "\n向量分析:";
? "  |u| = " + num2str(u_norm);
? "  |v| = " + num2str(v_norm);
? "  |u × v| = " + num2str(w_norm);

# 计算 u 和 v 之间的角度
# 根据叉积大小：|u × v| = |u| * |v| * sin(θ)
sin_theta = w_norm / (u_norm * v_norm);
theta = asin(sin_theta) * 180/pi;
? "  u 和 v 之间的角度: " + num2str(theta) + "° (应该为 90°)";
```

#### Python API
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

# 定义两个向量
u = [1, 0, 0]  # x 方向单位向量
v = [0, 1, 0]  # y 方向单位向量

# 计算叉积
w = fdtd.cross(u, v)

print("叉积计算:")
print(f"  u = {u}")
print(f"  v = {v}")
print(f"  u × v = {w}")

# 验证结果（应该是 z 方向单位向量）
expected = [0, 0, 1]
print(f"  期望结果: {expected}")
print(f"  误差: {np.linalg.norm(np.array(w) - np.array(expected)):.10f}")

# 计算向量大小和方向
u_norm = np.linalg.norm(u)
v_norm = np.linalg.norm(v)
w_norm = np.linalg.norm(w)

print(f"\n向量分析:")
print(f"  |u| = {u_norm:.4f}")
print(f"  |v| = {v_norm:.4f}")
print(f"  |u × v| = {w_norm:.4f}")

# 计算 u 和 v 之间的角度
# 根据叉积大小：|u × v| = |u| * |v| * sin(θ)
sin_theta = w_norm / (u_norm * v_norm)
theta = np.degrees(np.arcsin(sin_theta))
print(f"  u 和 v 之间的角度: {theta:.2f}° (应该为 90°)")
```

### 示例 2：电磁场计算（坡印廷矢量）
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def calculate_poynting_vector(E, H):
    """
    计算坡印廷矢量 S = E × H
    表示电磁能流密度
    """
    return fdtd.cross(E, H)

# 模拟电场和磁场数据（复数向量）
# 假设这是从仿真中获取的场数据
E_field = [1.0 + 0.5j, 0.5 - 0.2j, 0.3 + 0.1j]  # 复电场向量
H_field = [0.2 - 0.1j, 0.8 + 0.3j, 0.1 + 0.05j]  # 复磁场向量

print("电磁场分析:")
print(f"  电场 E = {E_field}")
print(f"  磁场 H = {H_field}")

# 计算瞬时坡印廷矢量（复数叉积）
S_complex = calculate_poynting_vector(E_field, H_field)
print(f"\n复数坡印廷矢量 S = E × H:")
print(f"  S = {S_complex}")

# 计算时间平均坡印廷矢量
# S_avg = 0.5 * Re(E × H*)，其中 H* 是 H 的复共轭
H_conj = [np.conj(h) for h in H_field]  # H 的复共轭
S_avg_complex = fdtd.cross(E_field, H_conj)
S_avg = 0.5 * np.real(S_avg_complex)

print(f"\n时间平均坡印廷矢量 (S_avg = 0.5 * Re(E × H*)):")
print(f"  S_avg = {S_avg}")

# 计算能流大小和方向
S_magnitude = np.linalg.norm(S_avg)
S_direction = S_avg / S_magnitude if S_magnitude > 0 else [0, 0, 0]

print(f"  能流大小: {S_magnitude:.6f} W/m²")
print(f"  能流方向: {S_direction}")

# 计算能量传输效率
# 假设入射能流已知
S_incident = [0, 0, 1.0]  # 假设入射沿 z 方向
incident_power = np.linalg.norm(S_incident)

if incident_power > 0:
    transmission_efficiency = np.dot(S_avg, S_incident) / incident_power**2
    print(f"  传输效率: {transmission_efficiency:.4f}")
    
    # 计算反射和透射系数
    reflection_coefficient = 1 - transmission_efficiency
    print(f"  反射系数: {reflection_coefficient:.4f}")
```

### 示例 3：几何法线和面积计算
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def calculate_surface_normal(p1, p2, p3):
    """
    计算三角形表面的法线向量
    使用两个边的叉积：n = (p2 - p1) × (p3 - p1)
    """
    # 计算两个边向量
    u = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
    v = [p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]]
    
    # 计算叉积（法线向量）
    n = fdtd.cross(u, v)
    
    # 归一化
    norm = np.linalg.norm(n)
    if norm > 0:
        n_normalized = [n[0]/norm, n[1]/norm, n[2]/norm]
    else:
        n_normalized = [0, 0, 0]
    
    return n_normalized, norm

def calculate_polygon_area(vertices):
    """
    计算多边形面积（适用于平面多边形）
    使用三角剖分和叉积方法
    """
    if len(vertices) < 3:
        return 0
    
    # 使用第一个顶点作为参考点
    p1 = vertices[0]
    total_area = 0
    
    for i in range(1, len(vertices) - 1):
        p2 = vertices[i]
        p3 = vertices[i + 1]
        
        # 计算两个边向量
        u = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
        v = [p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]]
        
        # 计算叉积（面积向量的两倍）
        cross_vec = fdtd.cross(u, v)
        
        # 三角形面积 = 0.5 * |u × v|
        triangle_area = 0.5 * np.linalg.norm(cross_vec)
        total_area += triangle_area
    
    return total_area

# 定义三角形顶点
triangle_vertices = [
    [0, 0, 0],    # 顶点1
    [2, 0, 0],    # 顶点2
    [1, 2, 0]     # 顶点3
]

print("三角形几何分析:")
print(f"  顶点:")
for i, vertex in enumerate(triangle_vertices):
    print(f"    p{i+1} = {vertex}")

# 计算法线向量
normal, area_doubled = calculate_surface_normal(*triangle_vertices)
print(f"\n表面法线:")
print(f"  法线向量: {normal}")
print(f"  向量大小: {area_doubled:.4f} (三角形面积的两倍)")

# 计算三角形面积
triangle_area = 0.5 * area_doubled
print(f"  三角形面积: {triangle_area:.4f}")

# 验证面积计算（使用海伦公式）
a = np.linalg.norm(np.array(triangle_vertices[1]) - np.array(triangle_vertices[0]))
b = np.linalg.norm(np.array(triangle_vertices[2]) - np.array(triangle_vertices[1]))
c = np.linalg.norm(np.array(triangle_vertices[0]) - np.array(triangle_vertices[2]))
s = (a + b + c) / 2
area_heron = np.sqrt(s * (s - a) * (s - b) * (s - c))
print(f"  海伦公式验证面积: {area_heron:.4f}")
print(f"  面积误差: {abs(triangle_area - area_heron):.10f}")

# 计算多边形面积（四边形）
quad_vertices = [
    [0, 0, 0],
    [3, 0, 0],
    [3, 2, 0],
    [1, 3, 0]
]

quad_area = calculate_polygon_area(quad_vertices)
print(f"\n四边形面积: {quad_area:.4f}")

# 验证（将四边形分割为两个三角形）
triangle1_area = calculate_polygon_area(quad_vertices[:3])  # 前三个顶点
triangle2_area = calculate_polygon_area([quad_vertices[0], quad_vertices[2], quad_vertices[3]])
print(f"  分割验证面积: {triangle1_area + triangle2_area:.4f}")
```

### 示例 4：角动量和转矩计算
```python
import lumapi
import numpy as np

fdtd = lumapi.FDTD()

def calculate_angular_momentum(position, linear_momentum):
    """
    计算角动量 L = r × p
    其中 r 是位置向量，p 是线动量
    """
    return fdtd.cross(position, linear_momentum)

def calculate_torque(position, force):
    """
    计算转矩 τ = r × F
    其中 r 是位置向量，F 是力
    """
    return fdtd.cross(position, force)

def calculate_magnetic_moment(current_loop):
    """
    计算电流环的磁矩 μ = I * A * n
    其中 I 是电流，A 是面积，n 是法线向量
    对于多边形环：μ = 0.5 * I * Σ(r_i × r_{i+1})
    """
    if len(current_loop) < 3:
        return [0, 0, 0]
    
    # 计算面积向量（叉积和）
    area_vector = [0, 0, 0]
    
    for i in range(len(current_loop)):
        r1 = current_loop[i]
        r2 = current_loop[(i + 1) % len(current_loop)]
        
        # 计算叉积并累加
        cross_product = fdtd.cross(r1, r2)
        area_vector[0] += cross_product[0]
        area_vector[1] += cross_product[1]
        area_vector[2] += cross_product[2]
    
    # 磁矩 μ = 0.5 * I * 面积向量
    I = 1.0  # 电流，A
    magnetic_moment = [0.5 * I * area_vector[0],
                      0.5 * I * area_vector[1],
                      0.5 * I * area_vector[2]]
    
    return magnetic_moment

# 粒子物理示例
print("角动量和转矩计算示例:")

# 定义位置和动量/力
position = [2, 3, 1]          # 位置向量，m
linear_momentum = [0.5, -0.3, 0.8]  # 线动量，kg·m/s
force = [10, -5, 2]           # 力，N

# 计算角动量
L = calculate_angular_momentum(position, linear_momentum)
print(f"\n1. 角动量 L = r × p:")
print(f"  位置 r = {position} m")
print(f"  动量 p = {linear_momentum} kg·m/s")
print(f"  角动量 L = {L} kg·m²/s")

# 计算转矩
τ = calculate_torque(position, force)
print(f"\n2. 转矩 τ = r × F:")
print(f"  位置 r = {position} m")
print(f"  力 F = {force} N")
print(f"  转矩 τ = {τ} N·m")

# 计算角动量和转矩的关系（τ = dL/dt）
# 这里假设一个时间变化
dt = 0.1  # 时间间隔，s
L_new = [L[0] + τ[0]*dt, L[1] + τ[1]*dt, L[2] + τ[2]*dt]
print(f"\n3. 角动量变化 (τ = dL/dt):")
print(f"  初始角动量 L = {L} kg·m²/s")
print(f"  时间间隔 dt = {dt} s")
print(f"  新角动量 L_new = L + τ*dt = {L_new} kg·m²/s")
print(f"  角动量变化 ΔL = {[L_new[0]-L[0], L_new[1]-L[1], L_new[2]-L[2]]} kg·m²/s")

# 电流环磁矩示例
print(f"\n4. 电流环磁矩计算:")

# 定义方形电流环的顶点（在 xy 平面）
current_loop = [
    [0, 0, 0],    # 顶点1
    [0.1, 0, 0],  # 顶点2 (x=10cm)
    [0.1, 0.1, 0],# 顶点3
    [0, 0.1, 0]   # 顶点4
]

μ = calculate_magnetic_moment(current_loop)
print(f"  电流环顶点:")
for i, vertex in enumerate(current_loop):
    print(f"    r{i+1} = {vertex} m")
print(f"  电流 I = 1.0 A")
print(f"  磁矩 μ = {μ} A·m²")

# 计算磁矩大小和方向
μ_magnitude = np.linalg.norm(μ)
μ_direction = [μ[0]/μ_magnitude, μ[1]/μ_magnitude, μ[2]/μ_magnitude] if μ_magnitude > 0 else [0, 0, 0]
print(f"  磁矩大小: {μ_magnitude:.6f} A·m²")
print(f"  磁矩方向: {μ_direction}")

# 计算磁场（在远场近似）
# B = (μ₀/4π) * (3(μ·r̂)r̂ - μ)/r³
μ0 = 4 * np.pi * 1e-7  # 真空磁导率，T·m/A
observation_point = [0, 0, 0.2]  # 观察点，m
r_vec = observation_point
r = np.linalg.norm(r_vec)
r_hat = [r_vec[0]/r, r_vec[1]/r, r_vec[2]/r] if r > 0 else [0, 0, 0]

# 计算 μ·r̂
μ_dot_r = np.dot(μ, r_hat)

# 计算磁场
B = []
for i in range(3):
    B_i = (μ0/(4*np.pi)) * (3 * μ_dot_r * r_hat[i] - μ[i]) / r**3
    B.append(B_i)

print(f"\n  在观察点 {observation_point} m 的磁场:")
print(f"    B = {B} T")
print(f"    |B| = {np.linalg.norm(B):.6e} T")
```

### 示例 5：高级向量分析工具
```python
import lumapi
import numpy as np

class VectorAnalyzer:
    """高级向量分析工具"""
    
    def __init__(self, session):
        self.session = session
    
    def calculate_vector_triple_product(self, a, b, c):
        """计算向量三重积 a × (b × c)"""
        
        # 首先计算 b × c
        b_cross_c = self.session.cross(b, c)
        
        # 然后计算 a × (b × c)
        result = self.session.cross(a, b_cross_c)
        
        return result
    
    def calculate_scalar_triple_product(self, a, b, c):
        """计算标量三重积 a · (b × c)（平行六面体体积）"""
        
        # 计算 b × c
        b_cross_c = self.session.cross(b, c)
        
        # 计算点积 a · (b × c)
        scalar_product = np.dot(a, b_cross_c)
        
        return scalar_product
    
    def check_orthogonality(self, u, v, tolerance=1e-10):
        """检查两个向量是否正交（垂直）"""
        
        # 计算点积
        dot_product = np.dot(u, v)
        
        # 计算叉积大小
        cross_product = self.session.cross(u, v)
        cross_magnitude = np.linalg.norm(cross_product)
        
        # 计算向量大小
        u_magnitude = np.linalg.norm(u)
        v_magnitude = np.linalg.norm(v)
        
        is_orthogonal = abs(dot_product) < tolerance
        
        # 计算角度
        if u_magnitude > 0 and v_magnitude > 0:
            cos_theta = dot_product / (u_magnitude * v_magnitude)
            cos_theta = max(-1, min(1, cos_theta))  # 防止数值误差
            theta = np.degrees(np.arccos(cos_theta))
        else:
            theta = 0
        
        return {
            'orthogonal': is_orthogonal,
            'dot_product': dot_product,
            'cross_magnitude': cross_magnitude,
            'angle_degrees': theta
        }
    
    def check_coplanarity(self, vectors, tolerance=1e-10):
        """检查多个向量是否共面"""
        
        if len(vectors) < 3:
            return {'coplanar': True, 'volume': 0}
        
        # 使用前三个向量计算标量三重积（体积）
        a, b, c = vectors[:3]
        volume = self.calculate_scalar_triple_product(a, b, c)
        
        is_coplanar = abs(volume) < tolerance
        
        # 检查所有向量组合
        all_coplanar = True
        for i in range(len(vectors)):
            for j in range(i+1, len(vectors)):
                for k in range(j+1, len(vectors)):
                    v = self.calculate_scalar_triple_product(vectors[i], vectors[j], vectors[k])
                    if abs(v) > tolerance:
                        all_coplanar = False
                        break
                if not all_coplanar:
                    break
            if not all_coplanar:
                break
        
        return {
            'coplanar': all_coplanar,
            'volume': volume,
            'volume_abs': abs(volume)
        }
    
    def project_vector(self, u, v):
        """将向量 u 投影到向量 v 上"""
        
        v_norm = np.linalg.norm(v)
        if v_norm == 0:
            return [0, 0, 0], [0, 0, 0]
        
        # 计算投影标量
        projection_scalar = np.dot(u, v) / (v_norm**2)
        
        # 计算投影向量
        projection = [projection_scalar * v[0], 
                     projection_scalar * v[1], 
                     projection_scalar * v[2]]
        
        # 计算垂直分量
        perpendicular = [u[0] - projection[0],
                        u[1] - projection[1],
                        u[2] - projection[2]]
        
        return projection, perpendicular
    
    def calculate_rotation_matrix(self, axis, angle_degrees):
        """计算绕轴旋转的旋转矩阵（罗德里格斯公式）"""
        
        # 归一化轴向量
        axis_norm = np.linalg.norm(axis)
        if axis_norm == 0:
            print("错误: 轴向量为零")
            return np.identity(3)
        
        u = [axis[0]/axis_norm, axis[1]/axis_norm, axis[2]/axis_norm]
        
        # 角度转换为弧度
        theta = np.radians(angle_degrees)
        
        # 罗德里格斯公式
        cos_t = np.cos(theta)
        sin_t = np.sin(theta)
        
        # 计算旋转矩阵
        R = np.zeros((3, 3))
        
        R[0, 0] = cos_t + u[0]*u[0]*(1-cos_t)
        R[0, 1] = u[0]*u[1]*(1-cos_t) - u[2]*sin_t
        R[0, 2] = u[0]*u[2]*(1-cos_t) + u[1]*sin_t
        
        R[1, 0] = u[1]*u[0]*(1-cos_t) + u[2]*sin_t
        R[1, 1] = cos_t + u[1]*u[1]*(1-cos_t)
        R[1, 2] = u[1]*u[2]*(1-cos_t) - u[0]*sin_t
        
        R[2, 0] = u[2]*u[0]*(1-cos_t) - u[1]*sin_t
        R[2, 1] = u[2]*u[1]*(1-cos_t) + u[0]*sin_t
        R[2, 2] = cos_t + u[2]*u[2]*(1-cos_t)
        
        return R

# 使用示例
fdtd = lumapi.FDTD()
analyzer = VectorAnalyzer(fdtd)

print("高级向量分析示例:")

# 定义测试向量
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
d = [1, 0, 0]

print(f"测试向量:")
print(f"  a = {a}")
print(f"  b = {b}")
print(f"  c = {c}")
print(f"  d = {d}")

print(f"\n1. 向量三重积 a × (b × c):")
triple_vector = analyzer.calculate_vector_triple_product(a, b, c)
print(f"  a × (b × c) = {triple_vector}")

# 验证向量三重积恒等式：a × (b × c) = b(a·c) - c(a·b)
left_side = triple_vector
right_side = [
    b[0]*np.dot(a, c) - c[0]*np.dot(a, b),
    b[1]*np.dot(a, c) - c[1]*np.dot(a, b),
    b[2]*np.dot(a, c) - c[2]*np.dot(a, b)
]
print(f"  验证恒等式 a × (b × c) = b(a·c) - c(a·b):")
print(f"    左侧: {left_side}")
print(f"    右侧: {right_side}")
print(f"    误差: {np.linalg.norm(np.array(left_side) - np.array(right_side)):.10f}")

print(f"\n2. 标量三重积 a · (b × c) (平行六面体体积):")
scalar_triple = analyzer.calculate_scalar_triple_product(a, b, c)
print(f"  a · (b × c) = {scalar_triple}")
print(f"  绝对值 (体积) = {abs(scalar_triple):.6f}")

print(f"\n3. 正交性检查:")
ortho_check = analyzer.check_orthogonality(a, d)
print(f"  a 和 d 是否正交: {ortho_check['orthogonal']}")
print(f"  点积: {ortho_check['dot_product']:.6f}")
print(f"  叉积大小: {ortho_check['cross_magnitude']:.6f}")
print(f"  角度: {ortho_check['angle_degrees']:.2f}°")

print(f"\n4. 共面性检查:")
vectors_to_check = [a, b, c]  # a, b, c 应该是共面的（因为 c = a + 2b？实际上不共面）
coplanar_check = analyzer.check_coplanarity(vectors_to_check)
print(f"  向量 {[a, b, c]} 是否共面: {coplanar_check['coplanar']}")
print(f"  体积: {coplanar_check['volume']:.6f}")

print(f"\n5. 向量投影:")
projection, perpendicular = analyzer.project_vector(a, d)
print(f"  a 在 d 上的投影: {projection}")
print(f"  a 垂直于 d 的分量: {perpendicular}")

# 验证投影性质
print(f"  验证:")
print(f"    投影 + 垂直分量 = a: {[projection[0]+perpendicular[0], projection[1]+perpendicular[1], projection[2]+perpendicular[2]]}")
print(f"    投影与 d 平行: 点积差 = {abs(np.dot(projection, d) - np.linalg.norm(projection)*np.linalg.norm(d)):.10f}")
print(f"    垂直分量与 d 正交: 点积 = {np.dot(perpendicular, d):.10f}")

print(f"\n6. 旋转矩阵 (绕 z 轴旋转 45°):")
axis = [0, 0, 1]
angle = 45
R = analyzer.calculate_rotation_matrix(axis, angle)
print(f"  旋转矩阵 R(axis={axis}, angle={angle}°):")
for row in R:
    print(f"    {row}")

# 测试旋转
test_vector = [1, 0, 0]
rotated_vector = np.dot(R, test_vector)
print(f"  向量 {test_vector} 旋转后: {rotated_vector}")
print(f"  应该接近: [0.7071, 0.7071, 0.0]")
print(f"  误差: {np.linalg.norm(np.array(rotated_vector) - np.array([0.7071, 0.7071, 0])):.6f}")
```

## 注意事项

1. **向量维度**：`cross` 命令仅适用于三维向量。对于二维向量，需要添加零作为第三个分量。

2. **右手定则**：叉积遵循右手定则：将右手手指从第一个向量弯曲向第二个向量，拇指方向即为叉积方向。

3. **数值精度**：由于浮点运算，叉积计算可能会有微小的数值误差，特别是在向量几乎平行或几乎垂直时。

4. **物理单位**：在物理计算中，确保所有向量使用一致的单位系统。Lumerical 中的默认长度单位是微米（μm）。

5. **复数向量**：`cross` 命令支持复数向量，用于计算复电磁场的叉积。

6. **并行与反并行向量**：如果两个向量平行（夹角 0° 或 180°），它们的叉积为零向量。

7. **与 `dot` 的关系**：`cross` 计算向量积，`dot` 计算标量积。两者结合可以计算各种向量运算。

8. **性能考虑**：对于大量向量对的叉积计算，考虑使用向量化操作以提高性能。

## 错误处理

`cross` 命令可能会遇到以下错误情况，建议进行适当的错误处理：

### 常见错误
1. **维度错误**：输入向量不是三维数组
2. **类型错误**：输入参数不是数值数组
3. **内存不足**：处理大型向量数组时内存不足
4. **数值错误**：浮点溢出或下溢

### Python 错误处理示例
```python
import lumapi

fdtd = lumapi.FDTD()

try:
    # 尝试计算维度错误的向量
    u = [1, 0]  # 二维向量 - 错误
    v = [0, 1, 0]
    w = fdtd.cross(u, v)
    print(f"叉积结果: {w}")
except Exception as e:
    print(f"叉积计算错误: {e}")
    # 提供修复建议
    print("建议: 确保两个输入向量都是三维数组")
    print("修复: u = [1, 0, 0]")
    
    # 修复后重试
    u_fixed = [1, 0, 0]
    w_fixed = fdtd.cross(u_fixed, v)
    print(f"修复后结果: {w_fixed}")
```

### LSF 错误处理示例
```lumerical
# 安全计算叉积
function safe_cross(u, v)
    # 检查输入维度
    if (length(u) != 3) {
        ? "错误: 向量 u 必须是三维向量";
        return {0, 0, 0};
    }
    
    if (length(v) != 3) {
        ? "错误: 向量 v 必须是三维向量";
        return {0, 0, 0};
    }
    
    # 检查数值类型
    if (!isnumeric(u) || !isnumeric(v)) {
        ? "错误: 输入必须是数值向量";
        return {0, 0, 0};
    }
    
    # 计算叉积
    result = cross(u, v);
    
    # 检查结果是否有效
    if (isnan(result(1)) || isnan(result(2)) || isnan(result(3))) {
        ? "警告: 叉积计算产生NaN值";
        return {0, 0, 0};
    }
    
    return result;
end

# 使用安全函数
u = {1, 0};  # 错误的维度
v = {0, 1, 0};
result = safe_cross(u, v);
? "安全叉积结果: " + num2str(result);
```

### 调试建议
1. **验证输入维度**：确保两个向量都是三维数组
2. **检查数值范围**：避免极端数值导致数值不稳定
3. **使用容错处理**：对可能失败的操作提供备用值
4. **记录错误信息**：记录详细的错误信息以便调试

## 产品支持

| 产品 | 支持情况 | 备注 |
|------|----------|------|
| FDTD Solutions | ✅ 完全支持 | 用于电磁场计算 |
| MODE Solutions | ✅ 完全支持 | 用于模式分析和向量运算 |
| DEVICE | ✅ 完全支持 | 用于电气和力学计算 |
| INTERCONNECT | ✅ 完全支持 | 用于信号处理和向量运算 |

## 相关命令

- `dot` - 计算向量点积（标量积）
- `norm` - 计算向量范数（大小）
- `conj` - 计算复共轭（用于复向量）
- `real` - 获取实部
- `imag` - 获取虚部
- `angle` - 计算相位角
- `abs` - 计算绝对值（模）

## 版本历史

| 版本 | 修改 |
|------|------|
| 1.0 | 初始版本，包含基本叉积计算功能 |
| 1.1 | 添加复数向量支持和高级向量分析示例 |
| 1.2 | 扩展错误处理和物理应用示例 |
| 2.0 | 添加LSF脚本示例，完善文档结构 |

## 参考

1. Lumerical Script Language Reference - Cross Command
2. Lumerical Python API Documentation - cross() Method
3. Mathematical Methods for Physics and Engineering
4. Vector Calculus for Electromagnetic Theory

---

*最后更新: 2026-01-31*  
*文档版本: 2.0*