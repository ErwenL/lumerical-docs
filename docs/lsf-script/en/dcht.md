# dcht

Returns the Chebyshev interpolation coefficients. The amplitude of the coefficients
decreases exponentially and the last coefficient offers an estimate of the relative
accuracy of the interpolation.

| **Syntax**            | **Description**                                                                                                                                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| coeff=dcht(f,option); | Returns the Chebyshev interpolation coefficients of a sampled function f. The function f must be sampled on a Chebyshev roots grid. Option: If option=1 is selected, the vector x will not include the endpoints If option=2 is selected, the vector x will include the endpoints |

**Example**

This example shows how to obtain interpolation coefficients from a sampled function:

```
Nc = 15;         # Number of sample points
xmin = 0;
xmax = 1;
x = chpts(xmin,xmax,Nc,1); # Returns Chebyshev roots grid on interval between xmin and xmax
f = exp(1i*2*pi*x);    # Function sampling using Chebyshev grid
coeff = dcht(f,1);     # Get interpolation coefficients
?abs(coeff);
result: 
0.304242  
0.569231  
0.970868  
0.666917  
0.302849  
0.104282  
0.0290919  
0.00684063  
0.00139224  
0.000250007  
4.01899e-005  
5.85025e-006  
7.78278e-007  
9.53372e-008  
1.094e-008      
```

**See Also**

[ chpts ](./chpts.md) , [ chebin ](./chebin.md) , [ icht ](./dcht.md) ,
[ chebpol ](./chebpol.md) , [ chebpol1 ](./chebpol1.md)
