<!--
Translation from English documentation
Original command: bessely
Translation date: 2026-02-04 22:49:36
-->

# bessely

Computes 该 Bessel 函数 的 该 second kind.

**语法** |  **描述**  
---|---  
out=bessely(nu, z); |  "nu" 是 该 order 和 "z" could 为 一个 数组. Both nu 和 z need 到 为 real.  
  
**示例**

This example shows 如何 到 obtain 该 first order Bessel 函数 的 该 second kind 的 该 数组 z.
    
    
    >z = 0.2:0.2:1;
    >?bessely(1,z);
    result: 
    -3.32382 
    -1.78087 
    -1.26039 
    -0.978144 
    -0.781213     

**参见**

[ besselj](/hc/en-us/articles/360034406754-besselj), [ besseli](/hc/en-us/articles/360034926973-besseli), [ besselk](/hc/en-us/articles/360034406774-besselk)
