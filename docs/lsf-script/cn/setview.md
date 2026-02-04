<!--
Translation from English documentation
Original command: setview
Translation date: 2026-02-04 22:50:14
-->

# setview

This 命令 allows 该 viewing 属性 的 该 Layout Editor 到 为 modified. 

**语法** |  **描述**  
---|---  
outstring = setview;  |  返回 一个 list 的 该 view 属性 该 可以 为 设置. The 命令 
    
    
    ?setview;

将 返回 
    
    
    extent, zoom, theta, phi  
  
setview("属性");  |  设置 该 default 值 用于 any 的 该 view 属性. For example, 
    
    
    setview("extent");

是 该 same as pressing 该 graphical extent button.   
setview("属性",值);  |  设置 该 值 到 的 any 属性 用于 viewing.   
  
The following table describes 该 属性 该 可以 为 设置 

**Property** |  **描述**  
---|---  
extent (not available 在 CHARGE, HEAT, FEEM, DGTD)  |  Control 该 view extent. In 此 case, 值 应该 为 一个 2x1, 4x1 或 6x1 矩阵 representing 该 view range min x, max x, min y, max y, min z 和 max z respectively.   
zoom  |  Controls 该 relative zoom 的 该 perspective view compared 到 该 default level. To zoom 在 通过 一个 factor 的 2 在 该 perspective view, use 
    
    
    setview("zoom",2);  
  
theta  |  Controls 该 polar angle 的 该 perspective view, 在 degrees.   
phi  |  Controls 该 azimuthal angle 的 该 perspective view, 在 degrees.   
  
**示例**

This example uses 该 setview 命令 到 spin 该 "perspective view" 通过 360 degrees. 
    
    
    setview("extent");
    setview("zoom",4);
    setview("theta", 30);
    用于 (i=0:10:360) {
      setview("phi",i);
    } 

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ getview ](/hc/en-us/articles/360034408874-getview) , [ orbit ](/hc/en-us/articles/360034929193-orbit) , [ redraw ](/hc/en-us/articles/360034929133-redraw)
