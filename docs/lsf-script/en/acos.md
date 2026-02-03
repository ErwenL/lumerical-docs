# acos

Calculates the inverse trigonometric cosine function (arccosine). Angle units are in radians. The function is defined for complex values. Phase of a complex number is evaluated between - π and π . If x is complex, or abs(x) > 1, the following equation is used:

$$ \text{acos}(x) = -i\ln(x+i\sqrt{1-x^2}) $$

**Syntax** |  **Description**  
---|---  
out = acos(x); |  Returns the complex arccosine of x.  
  
**Example**

Calculate acos( π /4 + i).
    
    
    x=pi/4+1i;
    ?acos(x);
    result: 
    1.03351-0.992724i

**See Also**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [cos](./cos.md)
