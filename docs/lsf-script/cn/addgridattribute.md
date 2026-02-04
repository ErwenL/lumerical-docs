<!--
Translation from English documentation
Original command: addgridattribute
Translation date: 2026-02-04 22:49:29
-->

# addgridattribute

添加 一个 grid attribute 对象 到 该 仿真 环境. Grid attribute 对象 include:

  * [Liquid Crystal Rotation](https://optics.ansys.com/hc/en-us/articles/360034915153)
  * [Permittivity Rotation](https://optics.ansys.com/hc/en-us/articles/360034394714)
  * [Matrix Transformation](https://optics.ansys.com/hc/en-us/articles/360034915173)
  * [np Density and Temperature Index Perturbation](https://optics.ansys.com/hc/en-us/articles/360034901753)

**语法** |  **描述**  
---|---  
addgridattribute("类型"); |  添加 一个 grid attribute 对象 到 该 仿真.

  * 类型: Type 的 attribute 到 添加. Options 是 "lc orientation", "permittivity rotation", "矩阵 transform", "np density", 或 "temperature".

This 函数 does not 返回 any 数据.  
addgridattribute("类型",dataset); |  添加 一个 grid attribute 使用 spatially varying 数据.

  * 类型: Type 的 attribute 到 添加. Options 是 "lc orientation", "permittivity rotation", "矩阵 transform", "np density", 或 "temperature".
  * dataset: A dataset containing 该 grid attribute 数据 - see 该 below table 用于 details.

  
Data | Simulation 对象 | Dataset 类型 | Name 用于 variables defining coordinate 数据 | Name 用于 variables defining actual 数据  
---|---|---|---|---  
Liquid crystal orientation (3 元素 unit 向量) |  'lc orientation' grid attribute |  Rectilinear |  x, y, z |  u  
Rotation angles 在 radians |  'permittivity rotation' grid attribute |  Rectilinear |  x, y, z |  theta, phi, psi  
Unitary transform 矩阵 (3x3 tensor) |  '矩阵 transform' grid attribute |  Rectilinear |  x, y, z |  U  
Charge density |  'np density' grid attribute |  Unstructured |  x, y, z, elements (see [ Dataset builder ](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder) for more information) |  n, p  
Temperature in Kelvin |  'temperature' grid attribute |  Unstructured |  x, y, z, elements (see [ Dataset builder ](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder) for more information) |  N  
  
### 示例

The following 脚本 是 一个 excerpt 从  LCD_twist.lsf  在 该 [ Twisted Nematic LCD](**%20to%20be%20defined%20**) application example 该 defines 一个 spatially varying liquid crystal.
    
    
    # define x/y/z
    x = 0;
    y = 0;
    z = linspace(0e-6,5e-6,100);
    X = meshgrid3dx(x,y,z);
    Y = meshgrid3dy(x,y,z);
    Z = meshgrid3dz(x,y,z);
    n = 矩阵(长度(x),长度(y),长度(z),3);
    # define 该 orientation 函数
    n(1:长度(x),1:长度(y),1:长度(z),1) = cos(Z*pi*1e5);
    n(1:长度(x),1:长度(y),1:长度(z),2) = sin(Z*pi*1e5);
    n(1:长度(x),1:长度(y),1:长度(z),3) = Z;
    # 创建 dataset containing orientation vectors 和 position 参数
    LC=rectilineardataset("LC",x,y,z);
    LC.addattribute("u",n);
    # 添加 LC import grid attribute
    addgridattribute("lc orientation",LC);
    setnamed("LC attribute","nz",50); # 设置 resolution

**参见**

[ List of commands](https://optics.ansys.com/hc/en-us/articles/360037228834), [ Datasets](https://optics.ansys.com/hc/en-us/articles/360034409554-Datasets), [ importdataset](https://optics.ansys.com/hc/en-us/articles/360034409114-importdataset), [ cleardataset](https://optics.ansys.com/hc/en-us/articles/360034929393-cleardataset), [ unstructureddataset](https://optics.ansys.com/hc/en-us/articles/360034929933-unstructureddataset), [ Dataset builder](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder), [LC Rotation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034915153), [Permittivity Rotation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034394714), [Matrix Transformation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034915173)
