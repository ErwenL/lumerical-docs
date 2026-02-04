<!--
Translation from English documentation
Original command: besselk
Translation date: 2026-02-04 22:49:36
-->

# besselk

Computes 该 modified Bessel 函数 的 该 second kind. 

**语法** |  **描述**  
---|---  
out=besselk(nu, z);  |  "nu" 是 该 order 和 "z" could 为 一个 数组. Both nu 和 z need 到 为 real.   
  
**示例**

This example shows 如何 到 obtain 该 modified Bessel 函数 的 该 second kind 的 该 数组 z (用于 first order). 
    
    
    >z = 0.2:0.2:1;
    >?besselk(1,z);
    result: 
    4.77597 
    2.18435 
    1.30283 
    0.861782 
    0.601907     

**参见**

[ bessely ](/hc/en-us/articles/360034926953-bessely) ,  [ besseli ](/hc/en-us/articles/360034926973-besseli) ,  [ besselj ](/hc/en-us/articles/360034406754-besselj)
