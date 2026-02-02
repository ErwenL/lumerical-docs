# asin

Calculates the inverse trigonometric sine function (arcsine). Angle units are in radians. The function is defined for complex values. Phase of a complex number is evaluated between -  π  and  π  . If x is complex, or abs(x) > 1, the following equation is used: 

$$ \text{arcsin(x)} = -i\text{ln(ix+}\sqrt{1-x^2}) $$ 

**Syntax** |  **Description**  
---|---  
out = asin(x);  |  Returns the complex arcsine of x.   
  
**Example**

Calculate asin(  π  /4 + i). 
    
    
    x=pi/4+1i;
    ?asin(x);
    result: 
    0.537282+0.992724i  

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ sin ](/hc/en-us/articles/360034405534-sin)
