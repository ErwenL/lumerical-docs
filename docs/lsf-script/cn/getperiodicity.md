<!--
Translation from English documentation
Original command: getperiodicity
Translation date: 2026-02-04 22:50:00
-->

# getperiodicity

返回 该 periodicity 向量(s) associated 使用 该 active periodic boundary conditions 在 该 specified 求解器. 

**语法** |  **描述**  
---|---  
out = getperiodicity("solvername");  |  返回 该 periodicity 向量(s) 的 该 system based 在 该 active periodic boundary conditions 在 该 named 求解器. The output 是 一个 [3XN] 矩阵 其中 N 是 该 数字 的 dimensions 该 have active periodic boundary conditions (typically one 或 two).   
  
**Parameter** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
solvername  |  required  |  |  字符串  |  Name 的 该 求解器 从 该 到 extract 该 periodicity 向量(s).   
  
**示例**

This example retrieves 该 periodicity vectors 从 一个 DGTD 仿真 使用 periodic boundary conditions. 
    
    
    period = getperiodicity("DGTD"); 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ getsourcedirection ](/hc/en-us/articles/360034927333-getsourcedirection) , [ gratingorders ](/hc/en-us/articles/360034927353-gratingorders) , [ gratingprojection ](/hc/en-us/articles/360034927373-gratingprojection)
