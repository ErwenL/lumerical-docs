<!--
Translation from English documentation
Original command: addtriangle
Translation date: 2026-02-04 22:49:36
-->

# addtriangle

添加 一个 3 vertex, triangle shaped polygon primitive 到 该 仿真 环境.

**语法** |  **描述**  
---|---  
addtriangle; |  添加 一个 triangle primitive 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addtriangle(struct_data); |  Adds a triangle primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 创建 一个 triangle primitive 和 设置 该 coordinates 的 its three corners 使用 一个 2D 矩阵.
    
    
    vtx = [1,0;2,2;4,0]*1e-6;  # 微米  
    
    addtriangle;  
    设置("name","new_triangle");  
    设置("vertices",vtx);  
    设置("z跨度",2e-6);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ addpoly ](/hc/en-us/articles/360034404174-addpoly) , [ 设置 ](/hc/en-us/articles/360034928773-设置)
