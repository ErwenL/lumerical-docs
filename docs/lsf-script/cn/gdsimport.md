<!--
Translation from English documentation
Original command: gdsimport
Translation date: 2026-02-04 22:49:49
-->

# gdsimport

This 命令 imports 一个 单元格 从 一个 .gds 文件 into 该 layout 环境. This 是 equivalent 到 performing 一个 GDSII import through 该 FILE->IMPORT menu. See 该 Layout editor reference guide 在 [ GDSII import ](/hc/en-us/articles/360034901933-Import-和-export-GDSII) 用于 more information.

**语法** |  **描述**  
---|---  
n = gdsimport("文件名", "cellname", layer); |  Imports 该 specified layer 从 该 specified 单元格 在 该 specified 文件 into 该 current 仿真 环境. The 对象 created 将 have their 材料 设置 到 一个 对象 defined dielectric. In 3D, 该 2D geometric 数据 将 为 extruded 到 default 值 在 该 Z 维度. The optional returned 值, n, 是 该 数字 的 对象 该 were imported 从 该 gds 文件.  
n = gdsimport("文件名", "cellname", layer, "材料"); |  Same as 该 above 命令, but 该 材料 的 该 imported 对象 将 为 设置 到 该 值 specified.  
n = gdsimport("文件名", "cellname", layer, "材料", zmin, zmax); |  This form 的 该 命令 是 only allowed 在 3D layouts. The behavior 是 该 same as 该 above 命令, but 该 structures 将 为 extruded 在 该 Z 维度 到 该 specified z最小值 和 z最大值 值  
  
**Parameter** |  **Type** |  **描述**  
---|---|---  
文件名 |  字符串 |  name 的 该 GDSII 文件 到 import. It 可以 contain 一个 complete path 到 文件, 或 path relative 到 该 current working directory.  
cellname |  字符串 |  name 的 该 单元格 到 import 从 该 GDSII 文件.  
layer |  数字 或 字符串 |  该 layer 数字 从 该 GDSII 文件 到 import. If only elements matching 一个 certain 数据 类型 是 desired, 此 可以 为 specified 通过 使用 一个 字符串 的 该 form: "6:2" 其中 该 desired layer 是 6 和 该 desired 数据 类型 是 2.  
材料 |  字符串 |  一个 valid name 的 一个 材料 在 your current layout 环境. Partial names 的 materials 可以 为 matched starting at 该 beginning 的 该 字符串. For example, "Al (3" would match "Al (300nm)".  
zmin |  数字 |  该 minimum z 值 用于 extruding 2D GDSII 数据 into 3D 对象  
zmax |  数字 |  该 maximum z 值 用于 extruding 2D GDSII 数据 into 3D 对象  
  
## 示例:

This 命令 imports "cell_1", 在 该 first layer 在 该  GDS_export.gds  文件, 使用 一个 specified 材料, z最小值 和 z最大值 assigned. For more examples, please visit 该 Layout editor reference guide 在 [ GDSII import ](/hc/en-us/articles/360034901933-Import-和-export-GDSII) .
    
    
    gdsimport("GDS_export.gds", "cell_1", 1, "Ag (Silver) - CRC", 0, 1e-6);

**参见**

[ List of commands ](/hc/en-us/articles/360037228834) , [ setnamed ](/hc/en-us/articles/360034928793-setnamed) , [ fileexists ](/hc/en-us/articles/360034931633-fileexists) , [ gdsopen](/hc/en-us/articles/360034927093-gdsopen), [gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
