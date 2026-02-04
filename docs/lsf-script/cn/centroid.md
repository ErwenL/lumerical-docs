<!-- Translation completed: 2026-02-04 -->
<!-- Original command: centroid -->

# centroid

**语法** | **描述**
---|---
out = centroid(V); | 返回 the center of mass of V, assuming uniform density. The 输出 is a 2x1 矩阵 representing the x and y positions.

**示例**

计算 the centroid of a square of side 长度 1: 
    V = [ 0,0; 1,0; 1,1; 0,1];
    ?centroid(V);
    result: 
    0.5 0.5

计算 the centroid of a square of side 长度 1: 
    V = [ 0,0; 1,0; 1,1; 0,1];
    ?centroid(V);
    result: 
    0.5 0.5

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ polyarea ](/hc/en-us/articles/360034926213-polyarea) , [ polyintersect ](/hc/en-us/articles/360034926233-polyintersect) , [ inpoly ](/hc/en-us/articles/360034926253-inpoly) , [ polygrow ](/hc/en-us/articles/360034406094-polygrow) , [ polyand ](/hc/en-us/articles/360034926293-polyand) , [ polyor ](/hc/en-us/articles/360034406114-polyor) , [ polydiff ](/hc/en-us/articles/360034926313-polydiff) , [ polyxor ](/hc/en-us/articles/360034406134-polyxor)
