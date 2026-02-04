<!-- Translation completed: 2026-02-04 -->
<!-- Original command: besselk -->

# besselk

**语法** | **描述**
---|---
out=besselk(nu, z); | "nu" is the order and "z" could be an 数组. Both nu and z need to be 实部.

**示例**

This 示例 shows how to obtain the modified Bessel 函数 of the second kind of the 数组 z (for first order). 
    >z = 0.2:0.2:1;
    >?besselk(1,z);
    result: 
    4.77597 
    2.18435 
    1.30283 
    0.861782 
    0.601907     

This 示例 shows how to obtain the modified Bessel 函数 of the second kind of the 数组 z (for first order). 
    >z = 0.2:0.2:1;
    >?besselk(1,z);
    result: 
    4.77597 
    2.18435 
    1.30283 
    0.861782 
    0.601907     

**另请参阅**

[ bessely ](/hc/en-us/articles/360034926953-bessely) ,  [ besseli ](/hc/en-us/articles/360034926973-besseli) ,  [ besselj ](/hc/en-us/articles/360034406754-besselj)
