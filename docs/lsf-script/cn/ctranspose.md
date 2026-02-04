<!--
Translation from English documentation
Original command: ctranspose
Translation date: 2026-02-04 22:49:48
-->

# ctranspose

Transposes 一个 1D 或 2D 矩阵 和 takes 该 complex conjugate 的 each 元素. The resulting 矩阵 是 该 conjugate transpose 或 Hermitian transpose. 

**语法** |  **描述**  
---|---  
y = ctranspose(x);  |  If x 是 一个 N x M 矩阵, 那么 y 将 为 M x N, 其中 该 entries 是 y(j,i)=x(i,j)  *  .   
  
**示例**

Simple example 的 如何 到 find 该 conjugate transpose 的 一个 2D complex 矩阵. 
    
    
    ?B = [1+3i,2,3+7i;4,5+2i,6];
    ?BCT = ctranspose(B); # conjugate transpose 的 A
    result:
    1+3i  2+0i  3+7i  
    4+0i  5+2i  6+0i  
    result: 
    1-3i  4+-0i  
    2+-0i  5-2i  
    3-7i  6+-0i  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ transpose ](/hc/en-us/articles/360034925973-transpose)
