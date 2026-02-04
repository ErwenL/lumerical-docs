<!--
Translation from English documentation
Original command: atan2
Translation date: 2026-02-04 22:49:36
-->

# atan2

计算 该 inverse trigonometric tangent 函数 (arctangent) 的 y/x, returning 该 angle 在 该 correct quadrant. Angle units 是 在 radians. The 函数 是 defined 用于 real 值 only. 

**语法** |  **描述**  
---|---  
out = atan2(y,x);  |  x,y 必须 为 real. The range 的 atan2 是 -  π  到  π  .   
  
**示例**

Plot atan2(y,x) 用于 -  π  ≤ theta≤  π  . 
    
    
    theta=linspace(-pi,pi,1000);
    x=cos(theta);
    y=sin(theta);
    plot(theta*180/pi,atan2(y,x)*180/pi,"theta (deg)","atan2(y,x) (deg)","atan2(y,x)");
    plot(y/x,atan2(y,x)*180/pi,"y/x","atan2(y,x) (deg)","atan2(y,x)");

计算 atan2 at (1,1) 和 (1,-1). The angle 是 converted 到 degrees. 
    
    
    ?atan2(1,1)*180/pi;
    result: 
    45 
    ?atan2(1,-1)*180/pi;
    result: 
    135 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ atan ](/hc/en-us/articles/360034405594-atan) , [ tan ](/hc/en-us/articles/360034925433-tan)
