<!-- Translation completed: 2026-02-04 -->
<!-- Original command: besselj -->

# besselj

**语法** | **描述**
---|---
out=besselj(nu, z); | "nu" is the order and "z" could be an 数组. Both nu and z need to be 实部.

**示例**

This 示例 shows how to obtain the first order Bessel 函数 of the first kind of the 数组 z. 
    >z = 0.2:0.2:1;
    >?besselj(1,z);
    result: 
    0.0995008 
    0.196027 
    0.286701 
    0.368842 
    0.440051     

This 示例 shows how to obtain the first order Bessel 函数 of the first kind of the 数组 z. 
    >z = 0.2:0.2:1;
    >?besselj(1,z);
    result: 
    0.0995008 
    0.196027 
    0.286701 
    0.368842 
    0.440051     

**另请参阅**

[ bessely ](/hc/en-us/articles/360034926953-bessely) ,  [ besseli ](/hc/en-us/articles/360034926973-besseli) ,  [ besselk ](/hc/en-us/articles/360034406774-besselk)
