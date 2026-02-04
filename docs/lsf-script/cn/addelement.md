<!--
Translation from English documentation
Original command: addelement
Translation date: 2026-02-04 22:49:04
-->

# addelement

添加 一个 元素 从 该 INTERCONNECT 元素 library 到 该 仿真 环境. 

**语法** |  **描述**  
---|---  
addelement("元素");  |  添加 一个 元素 从 该 元素 library.  If no 元素 name 是 given, 此 命令 将 添加 一个 compound 元素 通过 default.  This 函数 does not 返回 any 数据.   
  
**示例**

The following 脚本 commands 将 添加 一个 waveguide coupler 到 该 仿真 环境 和 edit its 属性. 
    
    
    addelement("Waveguide Coupler");
    eleName = "coupler_1";
    设置("name", eleName);
    设置("x position", 0); 
    设置("y position", 0);
    设置("coupling coefficient 1", 0.3);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置)
