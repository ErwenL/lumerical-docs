<!-- Translation completed: 2026-02-04 -->
<!-- Original command: bessely -->

# bessely

**语法** | **描述**
---|---
out=bessely(nu, z); | "nu" is the order and "z" could be an 数组. Both nu and z need to be 实部.

**示例**

This 示例 shows how to obtain the first order Bessel 函数 of the second kind of the 数组 z.
    >z = 0.2:0.2:1;
    >?bessely(1,z);
    result: 
    -3.32382 
    -1.78087 
    -1.26039 
    -0.978144 
    -0.781213     

This 示例 shows how to obtain the first order Bessel 函数 of the second kind of the 数组 z.
    >z = 0.2:0.2:1;
    >?bessely(1,z);
    result: 
    -3.32382 
    -1.78087 
    -1.26039 
    -0.978144 
    -0.781213     

**另请参阅**

[ besselj](/hc/en-us/articles/360034406754-besselj), [ besseli](/hc/en-us/articles/360034926973-besseli), [ besselk](/hc/en-us/articles/360034406774-besselk)
