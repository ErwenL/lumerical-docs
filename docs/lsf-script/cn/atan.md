<!--
Translation from English documentation
Original command: atan
Translation date: 2026-02-04 22:49:36
-->

# atan

计算 该 inverse trigonometric tangent 函数 (arctangent). Angle units 是 在 radians. The 函数 是 defined 用于 complex 值. Phase 的 一个 complex 数字 是 evaluated between -  π  和  π  . If x 是 complex, 或 abs(x) > 1, 该 following equation 是 used: 

$$ \text{arctan(x)} = \frac{i}{2}\text{ln}(\frac{i+x}{i-x}) $$ 

**语法** |  **描述**  
---|---  
out = atan(x);  |  返回 该 complex arctangent 的 x. The range 的 atan 是 -  π  /2 到  π  /2.   
  
**示例**

Plot atan(y/x) 用于 -  π  ≤ theta≤  π  . 
    
    
    theta=linspace(-pi,pi,1000);
    x=cos(theta);
    y=sin(theta);
    plot(theta*180/pi,atan(y/x)*180/pi,"theta (deg)","atan(y/x) (deg)","atan(y/x)");
    plot(y/x,atan(y/x)*180/pi,"y/x","atan(y/x) (deg)","atan(y/x)");

计算 atan(  π  /4 + i). 
    
    
    x=pi/4+1i;
    ?atan(x);
    result: 
    0.972497+0.50321i 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ atan2 ](/hc/en-us/articles/360034925473-atan2) , [ tan ](/hc/en-us/articles/360034925433-tan)
