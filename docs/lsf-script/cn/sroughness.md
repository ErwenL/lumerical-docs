<!--
---
**Translation metadata**
- English title: sroughness
- Chinese title: sroughness - 粗糙表面生成
- Status: Completed
- Translator: AI
- Last updated: 2026-02-03
- Difficulty: Advanced
- Priority: Standard
---
-->

# sroughness

返回包含由 RMS 振幅表征的粗糙表面的矩阵。

| **语法** | **描述** |
|---|---|
| out= sroughness(x_span, y_span, sigma_rms, corr_x, corr_y, seed); | 返回包含由 RMS 振幅 'sigma_rms' 和相关长度 'corr_x' 与 'corr_y' 表征的粗糙表面的矩阵。粗糙度是通过在由 'x_span' 和 'y_span' 定义的 K 空间中创建随机值矩阵来生成的。对该矩阵应用高斯滤波器，然后使用傅里叶变换将矩阵转换回实空间。由于傅里叶变换的设置方式，粗糙度将以 x、y 跨度为周期重复。这对某些应用很方便，特别是使用周期性边界条件时。参数 'seed' 定义了用于生成表面的随机种子值。 |

**示例**

这是使用 sroughness 创建的粗糙表面的简单示例：

```
x_span = 400e-6;
y_span = 400e-6;
sigma_rms = 0.3;
corr_length_x = 40e-6;
corr_length_y = 40e-6;
seed_process = 1;
# 计算 x 和 y 方向上的点数
Nx = 100;
Ny = 100;
# 初始化所需变量
x_wafer = linspace(-x_span/2,x_span/2,Nx);
y_wafer = linspace(-y_span/2,y_span/2,Ny);
neff_xy_wafer = sroughness( x_wafer, y_wafer, sigma_rms, corr_length_x, corr_length_y, seed_process );
image(x_wafer/1e-6, y_wafer/1e-6, neff_xy_wafer, "x (um)", "y(um)", "Rough surface");
```

**另请参见**

[ 命令列表 ](./command_list.md) , [ length ](./length.md) , [ substring ](./substring.md) , [ findstring ](./findstring.md) , [ replace ](./replace.md) , [ str2num ](./str2num.md) , [ num2str ](./num2str.md) , [ splitstring ](./splitstring.md) , [ lower ](./lower.md) , [ upper ](./upper.md)
