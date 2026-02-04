<!--
Translation from English documentation
Original command: importcsvlc
Translation date: 2026-02-04 22:50:00
-->

# importcsvlc

This 命令 添加 一个 LC grid attribute 或 分析 group containing 一个 liquid crystal 结构 和 LC grid attribute 使用 数据 imported 从 一个 specified csv (comma separated 值) 文件 without 使用 该 GUI import wizard. The 参数 allow you 到 make 该 same choices 该 是 available 在 该 GUI. For more information about 该 GUI import wizard, see [Import 对象 - Liquid crystal 从 CSV](**%20to%20be%20defined%20**).

**语法** |  **描述**  
---|---  
importcsvlc(文件名); |  Import 该 csv 文件 从 该 specified 文件名. All 参数 after 该 文件名 是 optional.  
out = importcsvlc(文件名,option); |  Import 该 csv 文件 but specify 如果 it 应该 为 imported as 一个 single grid attribute 或 added 到 一个 分析 group LC 结构.  
out = importcsvlc(文件名,option,exported_from_xz_plane); |  Import 该 csv 文件 和 specify 如果 it was originally exported 从 该 x-z plane. This option only applies 到 2D data设置but 是 critical 到 获取 该 orientation 的 该 LC 结构 correct 当 it 是 imported into FDTD 在 该 x-y plane。  
out = importcsvlc(文件名,option,exported_from_xz_plane,rotations); |  Import 该 csv 文件 使用 additional axis rotations.  
  
**Parameter** |  **Default 值** |  **Type** |  **描述**  
---|---|---|---  
文件名 |  required |  字符串 |  The name 的 该 csv 文件 到 import. May contain complete path 到 文件, 或 path relative 到 current working directory  
option |  true |  boolean |  When 设置 到 1 (true) 该 import 将 创建 一个 分析 group 结构 使用 该 grid attribute 和 一个 rectangle, 该 same as 当 使用 该 graphical import. When 设置 到 0 (false) it 将 import only 该 grid attribute. This 参数 是 optional  
exported_from_xz_plane |  true |  boolean |  Applies 到 2D data设置only。 This indicates 该 该 数据 was originally exported 从 该 x-z plane 和 此 应该 为 accounted 用于 当 it 是 imported into 该 x-y plane.  
rotations |  [0,0,0] |  矩阵 |  The optional 参数 allows you 到 specify 3 rotations around 该 x, y 和 z axes respectively 该 是 used exactly 该 same way as 该 graphical import wizard. The 矩阵 必须 have 3 elements 和 each 值 将 为 rounded 到 该 nearest 90 degrees.  
  
**示例**

The following 脚本 命令 将 import 该 grid attribute 从 文件 "myfile.csv" into 一个 LC 分析 group 和 rotate 90 degrees about 该 x axis.
    
    
    importcsvlc("myfile.csv",true,true,[90,0,0]);

For more examples 在 creating LC grid attribute 从 脚本 visit 此 kB page: [LC rotation](/hc/en-us/articles/360034915153-LC-Rotation).

**参见**

[addgridattribute](/hc/en-us/articles/360034404674-addgridattribute), [cleardataset](/hc/en-us/articles/360034929393-cleardataset), [importdataset](/hc/en-us/articles/360034409114-importdataset)
