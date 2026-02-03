# almostequal

Performs an almost-equal comparison. When using floating point numbers (rather than integers), two values that are meant to be equal may not be exactly equal due to rounding errors that are always present in floating point calculations. In such cases, the  almostequal  function can be useful. For complex numbers, A and B, almostequal  function returns true only when both the real and imaginary parts, evaluated separately, are true.

**Syntax** |  **Description**  
---|---  
out = almostequal(A, B); |  Returns 1 if |A - B| is less than or equal to |A + B|/2*1e-15. Returns 0 otherwise.  
out = almostequal(A, B, relative diff); |  Returns 1 if |A - B| is less than or equal to |A + B|/2 times relative diff. Returns 0 otherwise.  
out = almostequal(A, B, relative diff, absolute diff); |  Returns 1 if |A - B| is less than or equal to |A + B|/2 times relative diff or if |A - B| is less than or equal to absolute diff. Returns 0 otherwise.  
  
**Examples**

This example shows the usage of the  almostequal  function.
    
    
    A=[1,2];
    B=[1,1];
    ?almostequal(A,B);
    result: 
    1 0 
    ?almostequal(A,B,0.01,2);
    result: 
    1 1 
     
    ?almostequal(1,2,1);
    result: 
    1   

**See Also**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ = ](https://optics.ansys.com/hc/en-us/articles/360034929513--) , [ == ](https://optics.ansys.com/hc/en-us/articles/360034930893--) , [ != ](https://optics.ansys.com/hc/en-us/articles/360034930913--) , [ <= ](https://optics.ansys.com/hc/en-us/articles/360034410314--) , [ >= ](https://optics.ansys.com/hc/en-us/articles/360034930933--) , [ < ](https://optics.ansys.com/hc/en-us/articles/360034410334--) , [ > ](https://optics.ansys.com/hc/en-us/articles/360034930953--) , [ & ](https://optics.ansys.com/hc/en-us/articles/360034930973--) , [ and ](https://optics.ansys.com/hc/en-us/articles/360034410354-and) , [ | ](https://optics.ansys.com/hc/en-us/articles/360034410374--) , [ or ](https://optics.ansys.com/hc/en-us/articles/360034930993-or) , [ ! ](https://optics.ansys.com/hc/en-us/articles/360034931013--) , [ ~ ](https://optics.ansys.com/hc/en-us/articles/360034931033--)
