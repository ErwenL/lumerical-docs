# conv2

Returns the Convolution of two 2-dimensional arrays.

| **Syntax**            | **Description**                                                                                                                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = conv2(A,B,mode) | Computes the convolution of two 2-d dimensional matrices A and B. mode = 'full': computes the full convolution of A and B. 'same': computes the central part of the full convolution, result matrix C is restricted to the size of A, |

**Example**

In the following example, we computes the 'full' and 'same' convolution results of
matrices A and B:

```
matA = [-5;-4;-3;-2;-1;0;1;2;3;4;5]*pi;
matB = [-3,-2,-1,0];
matCFull = conv2(matA, matB, 'full');
matCSame = conv2(matA, matB, 'same');
>?matCFull;
result: 
47.1239  31.4159  15.708  0  
37.6991  25.1327  12.5664  0  
28.2743  18.8496  9.42478  0  
18.8496  12.5664  6.28319  0  
9.42478  6.28319  3.14159  0  
0  0  0  0  
-9.42478  -6.28319  -3.14159  0  
-18.8496  -12.5664  -6.28319  0  
-28.2743  -18.8496  -9.42478  0  
-37.6991  -25.1327  -12.5664  0  
-47.1239  -31.4159  -15.708  0   
>?matCSame;
result: 
15.708  
12.5664  
9.42478  
6.28319  
3.14159  
0  
-3.14159  
-6.28319  
-9.42478  
-12.5664  
-15.708 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ integrate ](./integrate.md) , [ integrate2 ](./integrate2.md) , [ max ](./max.md) ,
[ min ](./min.md) , [ interp ](./interp.md) , [ find ](./find.md) ,
[ pinch ](./pinch.md) , [ round ](./round.md) , [ getdata ](./getdata.md) ,
[ sum ](./sum.md) , [ length ](./length.md)
