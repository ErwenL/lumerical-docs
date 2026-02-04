<!--
Translation from English documentation
Original command: addport_lparenINTERCONNECTrparen
Translation date: 2026-02-04 22:49:29
-->

# addport (INTERCONNECT)

添加 一个 端口 到 一个 compound/脚本 元素 (注意 该 此 命令 does not apply 用于 primitive elements). This topic addresses 该  addport  命令 在 INTERCONNECT - 用于 information about 该 FDTD 命令, see [ addport (FDTD) ](/hc/en-us/articles/360034924793-addport) . 

**语法** |  **描述**  
---|---  
addport("元素", "端口", "类型", "数据", "position", "location");  |  添加 一个 新的 端口 到 该 元素 使用 该 specified 属性.  返回 该 name 的 该 端口 该 是 created.   
**Property** |  |  **Default 值** |  **Type** |  **描述**  
---|---|---|---|---  
元素  |  required  |  |  字符串  |  Name 的 该 元素 到 添加 一个 端口 到.   
端口  |  required  |  |  字符串  |  Name 的 该 端口 到 添加. The named 将 为 modified 如果 there 是 already 一个 端口 的 该 same name.   
类型  |  required  |  |  字符串  |  The 类型 的 端口 到 添加. The options 是: Bidirectional, Input, Output, Analyzer Input   
数据  |  required  |  |  字符串  |  The 类型 的 数据 用于 该 端口. The options 是: Variant, Optical Signal, Electrical Signal, Digital Signal   
position  |  optional  |  |  字符串  |  Position 的 该 端口. The options 是: Top, Bottom, Left, Right   
location  |  optional  |  |  数字  |  location 的 该 端口, within 该 range [0, 1].   
  
**示例**

Open 此 example 文件  compound_element.icp  从 [ Compound Elements ](**%20to%20be%20defined%20**) 和 input 该 following 脚本 
    
    
    disconnect("Optical Network Analyzer","input 1","Compound Element","端口 2");
    disconnect("Optical Network Analyzer","output","Compound Element","端口 1");
    removeport("Compound Element","端口 1"); #delete 该 端口
    addport("Compound Element","端口 1","input","optical Signal"); #添加 端口

**参见**

[ Manipulating 对象 ](/hc/en-us/articles/360037228834) , [ removeport ](/hc/en-us/articles/360034929293-removeport)
