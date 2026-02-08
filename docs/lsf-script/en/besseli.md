# besseli

Computes the modified Bessel function of the first kind.

| **Syntax**          | **Description**                                                             |
| ------------------- | --------------------------------------------------------------------------- |
| out=besseli(nu, z); | "nu" is the order and "z" could be an array. Both nu and z need to be real. |

**Example**

This example shows how to obtain the modified Bessel function of the first kind of the
array z (for first order).

```
z = 0.2:0.2:1;
?besseli(1,z);
result: 
0.100501 
0.204027 
0.313704 
0.432865 
0.565159      
```

**See Also**

[ bessely ](./bessely.md) , [ besselj ](./besselj.md) , [ besselk ](./besselk.md)
