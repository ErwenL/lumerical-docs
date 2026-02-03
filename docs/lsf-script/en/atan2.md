# atan2

Calculates the inverse trigonometric tangent function (arctangent) of y/x, returning the angle in the correct quadrant. Angle units are in radians. The function is defined for real values only. 

**Syntax** |  **Description**  
---|---  
out = atan2(y,x);  |  x,y must be real. The range of atan2 is -  π  to  π  .   
  
**Example**

Plot atan2(y,x) for -  π  ≤ theta≤  π  . 
    
    
    theta=linspace(-pi,pi,1000);
    x=cos(theta);
    y=sin(theta);
    plot(theta*180/pi,atan2(y,x)*180/pi,"theta (deg)","atan2(y,x) (deg)","atan2(y,x)");
    plot(y/x,atan2(y,x)*180/pi,"y/x","atan2(y,x) (deg)","atan2(y,x)");

Calculate atan2 at (1,1) and (1,-1). The angle is converted to degrees. 
    
    
    ?atan2(1,1)*180/pi;
    result: 
    45 
    ?atan2(1,-1)*180/pi;
    result: 
    135 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ atan ](/hc/en-us/articles/360034405594-atan) , [ tan ](/hc/en-us/articles/360034925433-tan)
