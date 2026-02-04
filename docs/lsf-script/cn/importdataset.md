<!--
Translation from English documentation
Original command: importdataset
Translation date: 2026-02-04 22:50:00
-->

# importdataset

This 命令 可以 为 used 到 import 一个 rectilinear 或 unstructured dataset into 一个 仿真 对象.

**语法** |  **描述**  
---|---  
importdataset("文件名") |  Imports 该 dataset 从 该 specified Matlab 文件 在 该 current working directory. The 对象 到 load 数据 into 必须 为 选中的.  
importdataset(电荷) |  Imports 该 数据 从 该 specified dataset 在 该 脚本 workspace. The dataset 可以 为 loaded 从 一个 Matlab 文件 到 该 脚本 workspace 使用 该 [ matlabload ](/hc/en-us/articles/360034408034-matlabload) 命令. The 对象 到 load 数据 into 必须 为 选中的.  
  
There 是 several cases 其中 此 命令 可以 为 used

1\. Import 数据 into 一个 grid attribute (数据 could 为 从 电荷 监视器 或 temperature 监视器 在 Finite Element IDE).

2\. Import doping 数据 into 一个 选中的 'import doping' 对象.

3\. Import optical generation 数据 into 一个 选中的 'import generation' 对象.

4\. Import field 数据 到 一个 import 源 (FDTD).

5\. Import field 数据 到 一个 端口 对象 (FDTD 和 MODE).

The 命令 可以 为 used 在 two ways. The dataset 可以 为 saved inside 一个 matlab (.mat) 文件 该 可以 为 called 到 load 该 数据 或, 该 命令 可以 directly call 该 dataset 从 该 脚本 workspace 到 load it into 该 仿真 对象. In both cases, 该 dataset need 到 have 该 following 属性:

**Data** |  **Simulation 对象** |  **Dataset 类型** |  **Name 用于 variables defining coordinate 数据** |  **Name 用于 variables defining actual 数据**  
---|---|---|---|---  
Liquid crystal orientation (3 元素 unit 向量) |  'lc orientation' grid attribute |  Rectilinear |  x, y, z |  u  
Rotation angles 在 radians |  'permittivity rotation' grid attribute |  Rectilinear |  x, y, z |  theta, phi, psi  
Unitary transform 矩阵 (3x3 tensor) |  '矩阵 transform' grid attribute |  Rectilinear |  x, y, z |  U  
Charge density |  'np density' grid attribute |  Unstructured |  x, y, z, C |  n, p  
Doping profile |  'Import doping' 对象 |  Unstructured 或 rectangular |  x, y, z, C (unstructured); x, y, z (rectangular) |  N  
Optical generation rate |  Import generation' 对象 |  Rectangular |  x, y, z |  G  
Temperature 在 Kelvin |  'temperature' grid attribute |  Unstructured |  x, y, z, elements (see [ Dataset builder ](/hc/en-us/articles/360034901713-Dataset-builder) 用于 more information) |  N  
E 和 H field 数据 |  Import 源 在 FDTD |  Rectilinear |  x, y, z, f (optional) (see [ Sources - Import ](/hc/en-us/articles/360034383014-Sources-Import) 用于 more information) |  E (required), H (optional)  
E 和 H field 数据 |  Port 在 MODE EME 求解器 (note 该 only 1 mode 可以 为 imported at 一个 时间 用于 each 端口) |  Rectilinear |  x,y,z (see [ Impoting arbitrary 源 fields ](/hc/en-us/articles/360034396394-Importing-arbitrary-源-fields) 用于 more information) |  E, H  
  
**示例**

This example shows 如何 到 import 一个 unstructured dataset '电荷' 到 该 'np Density' grid attribute.
    
    
    select("np density");
    importdataset("device_data.mat");

It 是 also equivalent 到 该 method below.
    
    
    select("np Density");
    matlabload("device_data.mat");
    importdataset(电荷);

**参见**

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ cleardataset ](/hc/en-us/articles/360034929393-cleardataset) , [ matlabload ](/hc/en-us/articles/360034408034-matlabload) , [ Mach Zehnder ](https://apps.lumerical.com/pn_phase_shifter.html) , [ Import/export np Density ](/hc/en-us/articles/360034382494-Charge-to-index-conversion) , [ addgridattribute ](/hc/en-us/articles/360034404674-addgridattribute) , [ unstructureddataset ](/hc/en-us/articles/360034929933-unstructureddataset)
