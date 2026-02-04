<!--
Translation from English documentation
Original command: getsourcedirection
Translation date: 2026-02-04 22:50:00
-->

# getsourcedirection

返回 一个 unit 向量 在 该 direction 的 该 wave 向量 (或 k-向量) 的 该 specified 源. The unit 向量 has three elements 对应的 到 该 X,Y 和 Z directions. 

**语法** |  **描述**  
---|---  
out = getsourcedirection("sourcename");  |  返回 一个 [3x1] 矩阵 使用 一个 unit 向量 在 该 direction 的 该 specified 源 wave 向量.   
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
sourcename  |  required  |  |  字符串  |  Name 的 该 源.   
  
**示例**

This example computes 一个 unit 向量 在 direction 的 该 k-向量 的 该 plane wave 源 named "源". 
    
    
    source_k = getsourcedirection("DGTD::源"); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ getperiodicity ](/hc/en-us/articles/360034407174-getperiodicity) , [ gratingorders ](/hc/en-us/articles/360034927353-gratingorders) , [ gratingprojection ](/hc/en-us/articles/360034927373-gratingprojection)
