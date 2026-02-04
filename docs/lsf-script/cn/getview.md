<!--
Translation from English documentation
Original command: getview
Translation date: 2026-02-04 22:50:00
-->

# getview

This 命令 allows 该 viewing 属性 的 该 Layout Editor 到 为 retrieved. 

**语法** |  **描述**  
---|---  
outstring = getview;  |  返回 一个 list 的 该 view 属性 该 可以 为 设置. The 命令 
    
    
    ?getview;

将 返回 
    
    
    extent, zoom, theta, phi  
  
out = getview("属性");  |  返回 该 current 值 的 any 的 该 view 属性. For example, 
    
    
    zoom_level = getview("zoom");

将 返回 该 current zoom setting 的 该 perspective view relative 到 该 default level.   
  
注意:  The "extent" 和 "zoom" options 用于 此 命令 是 not available 在 Finite Element IDE.   
---  
  
**示例**

The 属性 该 可以 为 obtained 使用 getview 是 described 在 [ setview ](/hc/en-us/articles/360034929173-setview) . 
    
    
    ?getview;
    extent, zoom, theta, phi

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ setview ](/hc/en-us/articles/360034929173-setview) , [ orbit ](/hc/en-us/articles/360034929193-orbit) , [ redraw ](/hc/en-us/articles/360034929133-redraw)
