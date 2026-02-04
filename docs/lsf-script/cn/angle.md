<!--
Translation from English documentation
Original command: angle
Translation date: 2026-02-04 22:49:36
-->

# angle

返回 该 angle 或 phase 的 一个 complex 数字 或 矩阵 在 radians. 

**语法** |  **描述**  
---|---  
out = angle(x);  |  返回 该 phase 的 x. The phase 是 evaluated between -  π  和  π  .   
  
**示例**

计算 该 phase 的 numbers 在 一个 数组. 
    
    
    ?x=linspace(0, 2+1i,2);
    result: 
    0+0i 
    2+1i 
    ?angle(x)*180/pi;
    result: 
    0 
    26.5651 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ real ](/hc/en-us/articles/360034925493-real) , [ imag ](/hc/en-us/articles/360034925513-imag) , [ unwrap ](/hc/en-us/articles/360034405634-unwrap)
