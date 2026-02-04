<!--
Translation from English documentation
Original command: getposition
Translation date: 2026-02-04 22:50:00
-->

# getposition

获取 该 current horizontal 或 vertical position 的 一个 元素. 

**语法** |  **描述**  
---|---  
out=getposition("元素",”x”);  |  返回 该 current horizontal position 的 一个 元素.   
out=getposition("元素",”y”);  |  返回 该 current vertical position 的 一个 元素.   
  
**示例**

This example 是 到 获取 该 x position 的 一个 元素 named "Waveguide Coupler_1" 
    
    
    ?getposition("Waveguide Coupler_1","x");
    result: 
    1e-006  

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ setposition ](/hc/en-us/articles/360034408534-setposition) , [ getrectangle ](/hc/en-us/articles/360034408554-getrectangle)
