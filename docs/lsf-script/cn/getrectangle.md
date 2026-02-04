<!--
Translation from English documentation
Original command: getrectangle
Translation date: 2026-02-04 22:50:00
-->

# getrectangle

获取 该 width 或 height 的 一个 元素 rectangle. 

**语法** |  **描述**  
---|---  
out=getrectangle ("元素",”w”);  |  返回 该 width 的 一个 元素 rectangle.   
out=getrectangle ("元素",”h”);  |  返回 该 height 的 一个 元素 rectangle.   
  
**示例**

To 获取 该 x position 的 一个 waveguide 元素 named "Straight Waveguide_1" use 该 following 脚本 
    
    
    ?getrectangle("Straight Waveguide_1","w") ;
    result: 
    1e-006 

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ setrectangle ](/hc/en-us/articles/360034928833-setrectangle) , [ getposition ](/hc/en-us/articles/360034928853-getposition)
