<!--
Translation from English documentation
Original command: stlimport
Translation date: 2026-02-04 22:50:15
-->

# stlimport

添加 一个 结构 到 该 仿真 环境 使用 结构 geometry loaded 从 specified STL 文件.

**语法** |  **描述**  
---|---  
stlimport(文件名,scalingFactor, vertexRadius,debugFlag); |  添加 一个 新的 结构 从 specified STL 类型 CAD 文件. This 函数 does not 返回 any 数据.  
  
Parameter |  | Default 值 | Type | 描述  
---|---|---|---|---  
文件名 |  required |  |  字符串 |  Name 的 该 STL CAD 文件.  
scalingFactor |  optional |  1e-6 |  数字 |  An STL 文件 does not contain 一个 unit. When imported 到 Lumerical's software, 该 unit 是 micron 通过 default. To have 该 unit 在 nanometer, 设置 scaling_factor 1e-9.  
vertexRadius |  optional |  1e-12 |  长度 (在 m) |  Vertices 可能 为 shared 通过 multiple triangles so 该 same vertex 可能 为 loaded multiple times 用于 different triangles. The vertexRadius 是 该 minimum distance between two vertices so 该 they 是 considered 到 为 distinct vertices.  
debugFlag |  optional |  false |  boolean |  If true, 该 following 数据 将 为 printed 到 该 脚本 prompt: -Input Vertex Count (total 数字 的 vertices 在 该 文件) -Triangles (total 数字 的 triangles) -Filtered Vertices (数字 的 unique vertices) -Vertex Collisions (Input Vertex Count minus Filtered Vertices) -Invalid Triangles -Expected Vertex Collisions If 该 数字 的 invalid triangles 是 larger than 0, try adjusting 该 vertexRadius 参数 和 importing 该 对象 again. 注意:  If there 是 一个 large 数字 的 triangles 在 该 STL 文件, 该 脚本 函数 可以 take longer 到 run 当 debugFlag 是 设置 到 true.  
  
**示例**

The following 脚本 commands 可以 为 used 到 创建 一个 3D geometry based 在 该 .stl 文件 provided 在 此 KB page: [ Import - STL ](/hc/en-us/articles/360034901953-Import-STL) .
    
    
    文件名 = "stlimport_assembly.stl";
    stlimport(文件名);
    设置("材料","Si (Silicon)");

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ readstltriangles ](/hc/en-us/articles/360034932233-readstltriangles)
