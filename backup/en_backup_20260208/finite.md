# finite

Returns 1 (true) if a value is finite. Numbers such as NaN or #1.INF return 0 (false). 

**Syntax** |  **Description**  
---|---  
out = finite(x);  |  Returns a matrix of the same size as x. The values are 1 for values of x that are finite and 0 for values that are NaN.   
  
**Example**

This example shows the different outputs of the finite function. 
    
    
    ?finite([1/0, 2, -3.4]);
    result: 
    0  1  1   

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ lineintersect ](/hc/en-us/articles/360034926333-lineintersect) , [ linecross ](/hc/en-us/articles/360034406154-linecross)
