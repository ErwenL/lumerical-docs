<!--
Translation from English documentation
Original command: inpoly
Translation date: 2026-02-04 22:50:01
-->

# inpoly

Determines 如果 一个 point 是 inside 或 outside 一个 polygon. The 函数 是 vectorized so it 可以 为 used 到 创建 一个 mesh 的 一个 polygon. 

The polygon vertices 是 contained 在 一个 single 矩阵 的 维度 Nx2 (或 2xN), 其中 N >= 3 是 该 数字 的 vertices. The 维度 2 corresponds 到 该 x,y positions. For example, 一个 square 的 side 长度 1 可以 为 described 通过 V = [ 0,0; 1,0; 1,1; 0,1] 或 V = [ 0,1,1,0;0,0,1,1]. 

**语法** |  **描述**  
---|---  
out = inpoly(V,x,y);  |  返回 一个 矩阵 的 该 same 维度 的 x 使用 1 如果 该 对应的 point 是 inside 该 polygon 和 0 otherwise. The matrices x 和 y 必须 have 该 same 长度, 或 one 的 them 可以 为 一个 singleton.   
  
**示例**

The following example shows 如何 到 identify 该 points 在 一个 mesh 该 是 inside 一个 polygon. 
    
    
    V = [ 0,0; 1,0; 1,1; 0,1];
    x = linspace(-4,4,100);
    y = linspace(-4,4,100);
    X = meshgridx(x,y);
    Y = meshgridy(x,y);
    image(x,y,inpoly(V,X,Y),"x","y");

The generated image 是: 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ polyarea ](/hc/en-us/articles/360034926213-polyarea) , [ centroid ](/hc/en-us/articles/360034406074-centroid) , [ polyintersect ](/hc/en-us/articles/360034926233-polyintersect) , [ polygrow ](/hc/en-us/articles/360034406094-polygrow) , [ polyand ](/hc/en-us/articles/360034926293-polyand) , [ polyor ](/hc/en-us/articles/360034406114-polyor) , [ polydiff ](/hc/en-us/articles/360034926313-polydiff) , [ polyxor ](/hc/en-us/articles/360034406134-polyxor) , [ meshgridx ](/hc/en-us/articles/360034409334-meshgridx) , [ meshgridy ](/hc/en-us/articles/360034929673-meshgridy)
