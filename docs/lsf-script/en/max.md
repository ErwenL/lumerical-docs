# max

Returns the maximum value in a matrix. For complex numbers, only the real part is
considered.

| **Syntax**    | **Description**                |
| ------------- | ------------------------------ |
| out = max(x); | The maximum value in matrix x. |

**Example**

Simple example showing how to find the maximum value of a vector.

```
?x=linspace(0,3,4);
result: 
0 
1 
2 
3 
?max(x);
result: 
3
```

Simple example showing how complex numbers are treated.

```
?x = 3 + 4i;
?max(x);
?max(abs(x));
result: 
3+4i 
result: 
3 
result: 
5 
```

Find the maximum field intensity at each frequency point.

```
# plot the maximum value of an 3D E-field by frequency
E2  = getelectric("3D field monitor");
f   = getdata("3D field monitor","f");
E_dim = size(E2);            # dimensions of matrix E
data = matrix(E_dim(4));        # make a matrix of size E_dim(4) ie. number of freq pts
for (i=1:E_dim(4)) {
 maxVal = max( pinch(E2,4,i) );        # pick out data at a certain freq
 data(i)=maxVal;
}
plot(f,data,"Frequency (Hz)","Maximum E intensity"); 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ min ](./min.md) ,
[ abs ](./abs.md) , [ mean ](./mean.md) , [ amax ](./amax.md) , [ amin ](./amin.md)
