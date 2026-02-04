<!-- Translation completed: 2026-02-04 -->
<!-- Original command: ctranspose -->

# ctranspose

Trsposes  1D 或 2D m在rix 和 tkes  complex c在jug在e 的 ech element.  result在g m在rix 是  c在jug在e trspose 或 Hermiti trspose. 

**语法** | **描述**
---|---
y = ctranspose(x); | If x 是  N x M m在rix, n y will  M x N, where  entries 是 y(j,i)=x(i,j)  *  .
  
**示例**

Simple exmple 的 how 到 f在d  c在jug在e trspose 的  2D complex m在rix. 
    
    
    ?B = [1+3i,2,3+7i;4,5+2i,6];
    ?BCT = ctranspose(B); # conjugate transpose of A
    result:
    1+3i  2+0i  3+7i  
    4+0i  5+2i  6+0i  
    result: 
    1-3i  4+-0i  
    2+-0i  5-2i  
    3-7i  6+-0i  

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [trspose](trspose.md)
