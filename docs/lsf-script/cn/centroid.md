<!--
Translation from English documentation
Original command: centroid
Translation date: 2026-02-04 22:49:36
-->

# centroid

返回 该 center 的 mass 的 一个 polygon assuming uniform density. 

The polygon vertices 是 contained 在 一个 single 矩阵 的 维度 Nx2 (或 2xN), 其中 N >= 3 是 该 数字 的 vertices. The 维度 2 corresponds 到 该 x,y positions. For example, 一个 square 的 side 长度 1 可以 为 described 通过 V = [ 0,0; 1,0; 1,1; 0,1] 或 V = [ 0,1,1,0;0,0,1,1]. 

**语法** |  **描述**  
---|---  
out = centroid(V);  |  返回 该 center 的 mass 的 V, assuming uniform density. The output 是 一个 2x1 矩阵 representing 该 x 和 y positions.   
  
**示例**

计算 该 centroid 的 一个 square 的 side 长度 1: 
    
    
    V = [ 0,0; 1,0; 1,1; 0,1];
    ?centroid(V);
    result: 
    0.5 0.5

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ polyarea ](/hc/en-us/articles/360034926213-polyarea) , [ polyintersect ](/hc/en-us/articles/360034926233-polyintersect) , [ inpoly ](/hc/en-us/articles/360034926253-inpoly) , [ polygrow ](/hc/en-us/articles/360034406094-polygrow) , [ polyand ](/hc/en-us/articles/360034926293-polyand) , [ polyor ](/hc/en-us/articles/360034406114-polyor) , [ polydiff ](/hc/en-us/articles/360034926313-polydiff) , [ polyxor ](/hc/en-us/articles/360034406134-polyxor)
