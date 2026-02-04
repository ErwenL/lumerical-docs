<!--
Translation from English documentation
Original command: tecplotread
Translation date: 2026-02-04 22:50:15
-->

# tecplotread

Imports 数据 从 Tecplot formatted 文件 (text).

**语法** |  **描述**  
---|---  
? tecplotread('文件名.dat'); |  List all zones ( domains) 在 该 数据 文件.  
? tecplotread('文件名.dat','zonename'); |  List all 的 该 数据 fields associated 使用 该 zone.  
out = tecplotread('文件名.dat','zonename','dataname'); |  Retrieve 该 数据 as 一个 数组  
  
**示例**

The following example shows 如何 该 tecplotread 命令 可以 为 used 到 import 数据 从 这些 files into CHARGE. Special field “FETriangle” represents 该 triangulation 和 X 和 Y coordinates 的 mesh 是 treated as node 数据. Names 和 units depend 在 original 数据 源 but we 必须 转换 units 到 SI (m). 

The first part 的 该 tecplot_import_diode.lsf 文件 reads 该 数据 从 该 example_diode_tecplot.dat 文件. The following two lines 在 该 脚本 reads 在 该 names 的 该 zones 和 该 数据 available 在 该 zones 的 该 tecplot 文件. 
    
    
    文件名 = 'example_diode_tecplot.dat';  
    zonename = 'Silicon';  
    ?"Available zones: " + tecplotread(文件名);  
    ?"Data 在 zone " + zonename + ": " + tecplotread(文件名,zonename);

The next few lines read 在 该 information about 该 finite 元素 grid. Here t 是 该 connectivity 矩阵 和 x, y 是 该 vertex matrices. Notice 该 coordinate 数据 是 converted 从 units 的 micron 到 meter.
    
    
    t = tecplotread(文件名,zonename,'FETriangle');  
    x = 1e-6*tecplotread(文件名,zonename,'X [um]'); # 转换 到 SI 从 um 到 m  
    y = 1e-6*tecplotread(文件名,zonename,'Y [um]'); # 转换 到 SI, invert

The following lines 那么 read 该 doping 数据.
    
    
    NA_name = 'NA [1/cm3]';  
    ND_name = 'ND [1/cm3]';  
    NA = 1e6*tecplotread(文件名,zonename,NA_name); # 转换 到 SI (cm^-3 -- m^-3)  
    ND = 1e6*tecplotread(文件名,zonename,ND_name); # 转换 到 SI (cm^-3 -- m^-3)

After reading 该 数据, 该 code 创建 unstructured data设置用于 该 doping 数据 和 创建 geometries 和 import doping 对象。 The same task 可以 为 performed 使用 该 [Dataset builder](/hc/en-us/articles/360034901713-Dataset-builder) 在 CHARGE once 该 数据 has been imported.

**参见**

[system](/hc/en-us/articles/360034410894-system), [matlabload](/hc/en-us/articles/360034408034-matlabload), [h5read](/hc/en-us/articles/360034407214-h5read)
