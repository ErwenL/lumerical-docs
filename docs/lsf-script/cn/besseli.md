<!-- Translation completed: 2026-02-04 -->
<!-- Original command: besseli -->

# besseli

**语法** | **描述**
---|---
out=besseli(nu, z); | "nu" is the order and "z" could be an 数组. Both nu and z need to be 实部.

**示例**

This 示例 shows how to obtain the modified Bessel 函数 of the first kind of the 数组 z (for first order). 
    z = 0.2:0.2:1;
    ?besseli(1,z);
    result: 
    0.100501 
    0.204027 
    0.313704 
    0.432865 
    0.565159      

This 示例 shows how to obtain the modified Bessel 函数 of the first kind of the 数组 z (for first order). 
    z = 0.2:0.2:1;
    ?besseli(1,z);
    result: 
    0.100501 
    0.204027 
    0.313704 
    0.432865 
    0.565159      

**另请参阅**

[ bessely ](/hc/en-us/articles/360034926953-bessely) ,  [ besselj ](/hc/en-us/articles/360034406754-besselj) ,  [ besselk ](/hc/en-us/articles/360034406774-besselk)
