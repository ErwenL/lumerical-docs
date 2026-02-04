<!--
Translation from English documentation
Original command: addgridattribute
Translation date: 2026-02-03 23:51:33
-->

# addgridattribute

向仿真环境中添加一个网格属性对象。网格属性对象包括：

  * [Liquid Crystal Rotation](https://optics.ansys.com/hc/en-us/articles/360034915153)（液晶旋转）
  * [Permittivity Rotation](https://optics.ansys.com/hc/en-us/articles/360034394714)（介电常数旋转）
  * [Matrix Transformation](https://optics.ansys.com/hc/en-us/articles/360034915173)（矩阵变换）
  * [np Density and Temperature Index Perturbation](https://optics.ansys.com/hc/en-us/articles/360034901753)（np密度和温度折射率扰动）

**Syntax** |  **Description**  
---|---  
addgridattribute("type"); |  向仿真中添加一个网格属性对象。

  * type: 要添加的属性类型。选项包括"lc orientation"、"permittivity rotation"、"matrix transform"、"np density"或"temperature"。

此函数不返回任何数据。
addgridattribute("type",dataset); |  添加具有空间变化数据的网格属性。

  * type: 要添加的属性类型。选项包括"lc orientation"、"permittivity rotation"、"matrix transform"、"np density"或"temperature"。
  * dataset: 包含网格属性数据的数据集 - 详情见下表。

  
Data | Simulation object | Dataset type | Name for variables defining coordinate data | Name for variables defining actual data  
---|---|---|---|---  
Liquid crystal orientation (3 element unit vector) |  'lc orientation' grid attribute |  Rectilinear |  x, y, z |  u  
Rotation angles in radians |  'permittivity rotation' grid attribute |  Rectilinear |  x, y, z |  theta, phi, psi  
Unitary transform matrix (3x3 tensor) |  'matrix transform' grid attribute |  Rectilinear |  x, y, z |  U  
Charge density |  'np density' grid attribute |  Unstructured |  x, y, z, elements (see [ Dataset builder ](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder) for more information) |  n, p  
Temperature in Kelvin |  'temperature' grid attribute |  Unstructured |  x, y, z, elements (see [ Dataset builder ](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder) for more information) |  N  
  
### 示例

以下脚本摘录自[ Twisted Nematic LCD](**%20to%20be%20defined%20**)应用示例中的LCD_twist.lsf文件，该脚本定义了空间变化的液晶。
    
    
    # define x/y/z
    x = 0;
    y = 0;
    z = linspace(0e-6,5e-6,100);
    X = meshgrid3dx(x,y,z);
    Y = meshgrid3dy(x,y,z);
    Z = meshgrid3dz(x,y,z);
    n = matrix(length(x),length(y),length(z),3);
    # define the orientation function
    n(1:length(x),1:length(y),1:length(z),1) = cos(Z*pi*1e5);
    n(1:length(x),1:length(y),1:length(z),2) = sin(Z*pi*1e5);
    n(1:length(x),1:length(y),1:length(z),3) = Z;
    # create dataset containing orientation vectors and position parameters
    LC=rectilineardataset("LC",x,y,z);
    LC.addattribute("u",n);
    # add LC import grid attribute
    addgridattribute("lc orientation",LC);
    setnamed("LC attribute","nz",50); # set resolution

**参见**

- [importdataset](./importdataset.md)
- [cleardataset](./cleardataset.md)
- [unstructureddataset](./unstructureddataset.md)
- [Dataset builder](https://optics.ansys.com/hc/en-us/articles/360034901713-Dataset-builder)
- [LC Rotation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034915153)
- [Permittivity Rotation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034394714)
- [Matrix Transformation grid attribute](https://optics.ansys.com/hc/en-us/articles/360034915173)
