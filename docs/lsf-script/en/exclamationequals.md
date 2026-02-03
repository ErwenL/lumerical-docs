# !=

Performs a logical not-equal-to comparison. Returns 1 if values are not equal. Returns 0 if values are equal. This operator can be used in matrix operations. This operators can be used with complex numbers.

**Syntax** |  **Description**  
---|---  
out = a!=b; |  If a is not equal to b, then out equals 1. Otherwise out equals 0.  
  
**Examples**

This example shows the usage of the "!=" comprison.
    
    
    a=1:5;
    b=1:5;
    b(4)=5;
    ?out = a!=b;
    result: 
    0 
    0 
    0 
    1 
    0 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ == ](/hc/en-us/articles/360034930893--) , [ almostequal ](/hc/en-us/articles/360034410294-almostequal) , , [ = ](/hc/en-us/articles/360034930933--) , , , [ & ](/hc/en-us/articles/360034930973--) , [ and ](/hc/en-us/articles/360034410354-and) , [ | ](/hc/en-us/articles/360034410374--) , [ or ](/hc/en-us/articles/360034930993-or) , [ ! ](/hc/en-us/articles/360034931013--) , [ ~ ](/hc/en-us/articles/360034931033--)
