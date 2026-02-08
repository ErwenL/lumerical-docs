# abs

Returns the absolute value of a number or matrix.

**Syntax** |  **Description**  
---|---  
out = abs(x); |  Returns the absolute value of x.  
  
**Example**

Calculate the absolute value of numbers in an array.
    
    
    ?x=linspace(0, 2+1i,2);
    result: 
    0+0i 
    2+1i 
    ?abs(x);
    result: 
    0 
    2.23607  

**See Also**

- [real](./real.md)
- [imag](./imag.md)
