<!--
Translation from English documentation
Original command: besseli
Translation date: 2026-02-04 22:49:36
-->

# besseli

Computes 该 modified Bessel 函数 的 该 first kind. 

**语法** |  **描述**  
---|---  
out=besseli(nu, z);  |  "nu" 是 该 order 和 "z" could 为 一个 数组. Both nu 和 z need 到 为 real.   
  
**示例**

This example shows 如何 到 obtain 该 modified Bessel 函数 的 该 first kind 的 该 数组 z (用于 first order). 
    
    
    z = 0.2:0.2:1;
    ?besseli(1,z);
    result: 
    0.100501 
    0.204027 
    0.313704 
    0.432865 
    0.565159      

**参见**

[ bessely ](/hc/en-us/articles/360034926953-bessely) ,  [ besselj ](/hc/en-us/articles/360034406754-besselj) ,  [ besselk ](/hc/en-us/articles/360034406774-besselk)
