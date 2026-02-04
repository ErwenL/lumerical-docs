<!--
Translation from English documentation
Original command: conj
Translation date: 2026-02-04 22:49:48
-->

# conj

返回 该 complex conjugate 的 一个 数字 或 矩阵. 

**语法** |  **描述**  
---|---  
out = conj(x);  |  返回 该 complex conjugate 的 x.   
  
**示例**

计算 该 complex conjugate 的 numbers 在 一个 数组. 
    
    
    ?x=linspace(0, 2+1i,2);
    result: 
    0+0i 
    2+1i 
    ?conj(x);
    result: 
    0+0i 
    2-1i 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ real ](/hc/en-us/articles/360034925493-real) , [ imag ](/hc/en-us/articles/360034925513-imag)
