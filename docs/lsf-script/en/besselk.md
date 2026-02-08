# besselk

Computes the modified Bessel function of the second kind.

| **Syntax**          | **Description**                                                             |
| ------------------- | --------------------------------------------------------------------------- |
| out=besselk(nu, z); | "nu" is the order and "z" could be an array. Both nu and z need to be real. |

**Example**

This example shows how to obtain the modified Bessel function of the second kind of the
array z (for first order).

```
>z = 0.2:0.2:1;
>?besselk(1,z);
result: 
4.77597 
2.18435 
1.30283 
0.861782 
0.601907     
```

**See Also**

[ bessely ](./bessely.md) , [ besseli ](./besseli.md) , [ besselj ](./besselj.md)
