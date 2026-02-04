<!--
Translation from English documentation
Original command: asin
Translation date: 2026-02-04 22:49:36
-->

# asin

计算 该 inverse trigonometric sine 函数 (arcsine). Angle units 是 在 radians. The 函数 是 defined 用于 complex 值. Phase 的 一个 complex 数字 是 evaluated between -  π  和  π  . If x 是 complex, 或 abs(x) > 1, 该 following equation 是 used: 

$$ \text{arcsin(x)} = -i\text{ln(ix+}\sqrt{1-x^2}) $$ 

**语法** |  **描述**  
---|---  
out = asin(x);  |  返回 该 complex arcsine 的 x.   
  
**示例**

计算 asin(  π  /4 + i). 
    
    
    x=pi/4+1i;
    ?asin(x);
    result: 
    0.537282+0.992724i  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ sin ](/hc/en-us/articles/360034405534-sin)
