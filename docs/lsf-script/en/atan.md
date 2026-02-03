# atan

Calculates the inverse trigonometric tangent function (arctangent). Angle units are in radians. The function is defined for complex values. Phase of a complex number is evaluated between -  π  and  π  . If x is complex, or abs(x) > 1, the following equation is used: 

$$ \text{arctan(x)} = \frac{i}{2}\text{ln}(\frac{i+x}{i-x}) $$ 

**Syntax** |  **Description**  
---|---  
out = atan(x);  |  Returns the complex arctangent of x. The range of atan is -  π  /2 to  π  /2.   
  
**Example**

Plot atan(y/x) for -  π  ≤ theta≤  π  . 
    
    
    theta=linspace(-pi,pi,1000);
    x=cos(theta);
    y=sin(theta);
    plot(theta*180/pi,atan(y/x)*180/pi,"theta (deg)","atan(y/x) (deg)","atan(y/x)");
    plot(y/x,atan(y/x)*180/pi,"y/x","atan(y/x) (deg)","atan(y/x)");

Calculate atan(  π  /4 + i). 
    
    
    x=pi/4+1i;
    ?atan(x);
    result: 
    0.972497+0.50321i 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ atan2 ](/hc/en-us/articles/360034925473-atan2) , [ tan ](/hc/en-us/articles/360034925433-tan)
