# mod

Finds the modulus after division. 

**Syntax** |  **Description**  
---|---  
out = mod(x,y);  |  Returns x - n*y where n = floor(x/y) if y is not equal to 0. The input x can be a real array or a real scalar, while y must be a real scalar.  The following are true by convention:  mod(x,0) = x  mod(x,x) = 0   
  
**Example**

Find the modulus of a matrix after dividing each element by a scalar: 
    
    
    ?A=[1,2;3,4];
    ?mod(A,2);
    result: 
    1  2  
    3  4  
    result: 
    1  0  
    1  0

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ floor ](/hc/en-us/articles/360034926353-floor) , [ ceil ](/hc/en-us/articles/360034406174-ceil)
