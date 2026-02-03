# conj

Returns the complex conjugate of a number or matrix. 

**Syntax** |  **Description**  
---|---  
out = conj(x);  |  Returns the complex conjugate of x.   
  
**Example**

Calculate the complex conjugate of numbers in an array. 
    
    
    ?x=linspace(0, 2+1i,2);
    result: 
    0+0i 
    2+1i 
    ?conj(x);
    result: 
    0+0i 
    2-1i 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ real ](/hc/en-us/articles/360034925493-real) , [ imag ](/hc/en-us/articles/360034925513-imag)
