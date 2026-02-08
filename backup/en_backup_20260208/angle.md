# angle

Returns the angle or phase of a complex number or matrix in radians. 

**Syntax** |  **Description**  
---|---  
out = angle(x);  |  Returns the phase of x. The phase is evaluated between -  π  and  π  .   
  
**Example**

Calculate the phase of numbers in an array. 
    
    
    ?x=linspace(0, 2+1i,2);
    result: 
    0+0i 
    2+1i 
    ?angle(x)*180/pi;
    result: 
    0 
    26.5651 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ real ](/hc/en-us/articles/360034925493-real) , [ imag ](/hc/en-us/articles/360034925513-imag) , [ unwrap ](/hc/en-us/articles/360034405634-unwrap)
