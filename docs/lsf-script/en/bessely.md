# bessely

Computes the Bessel function of the second kind.

| **Syntax**          | **Description**                                                             |
| ------------------- | --------------------------------------------------------------------------- |
| out=bessely(nu, z); | "nu" is the order and "z" could be an array. Both nu and z need to be real. |

**Example**

This example shows how to obtain the first order Bessel function of the second kind of
the array z.

```
>z = 0.2:0.2:1;
>?bessely(1,z);
result: 
-3.32382 
-1.78087 
-1.26039 
-0.978144 
-0.781213     
```

**See Also**

[ besselj](./besselj.md), [ besseli](./besseli.md), [ besselk](./besselk.md)
