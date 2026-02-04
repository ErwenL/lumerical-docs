<!--
Translation Status: Completed
Source: docs/lsf-script/en/reportmeshstatistics.md
Last Updated: 2026-02-03
-->

# reportmeshstatistics

返回模拟网格的统计信息。此命令可用于比较不同模拟或求解器之间网格网格的大小和质量。该脚本仅适用于四面体（3D）和三角形（2D）网格，不适用于1D模拟。

**语法** |  **说明**  
---|---  
out = reportmeshstatistics(mesh,ID);  |  返回模拟网格的统计信息。   
  
**参数** |  |  **默认值** |  **类型** |  **说明**  
---|---|---|---|---  
mesh  |  必需  |  |  非结构化数据集  |  包含有限元网格的非结构化数据集   
ID  |  可选  |  所有可用域ID的数组  |  整数数组  |  包含报告中应限制的网格元素域ID（索引）的整数数组   
out  |  |  |  结构体  |  输出包括提供信息的属性，如numElements（网格中的元素总数）、numFaces（网格中的面总数）、numVertices（网格中的顶点总数）、elementSizeMeasure（网格中所有元素的内球或内切圆半径值数组，可用作每个元素大小的度量）和elementQualityMeasure（网格中所有元素的最小二面角度数值数组，可用作每个元素质量的度量）   
  
**示例**

此示例从DGTD求解器的'grid'属性获取网格，并存储与该网格相关的统计信息，显示网格中的面数。请注意，在运行此示例之前必须已经形成网格网格。
    
    
    grid=getresult("DGTD","grid");
    out=reportmeshstatistics(grid);
    ?out.numFaces;
    

**另请参见**
