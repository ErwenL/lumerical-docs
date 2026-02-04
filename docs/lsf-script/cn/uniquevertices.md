<!-- Translation: uniquevertices -->
<!-- Date: 2026-02-03 -->
<!-- Original: uniquevertices -->

# uniquevertices

给定一个顶点矩阵，返回一个值差异大于指定容差的唯一顶点矩阵。

**语法** | **说明**
---|---
out=uniquevertices(vertexTable, absTolerance); | 返回值差异大于指定容差的矩阵的唯一元素。vertexTable是一个Mx2或Mx3矩阵，absTolerance是容差的大小。

**示例**

这是一个简单的示例，展示此命令的工作原理。


    # 定义一个具有三个3D顶点的矩阵：
    vtx = [0,0,0; 1,0,0; 1,1,0; 1,1,0.09];
    ?uniquevertices(vtx, 0.1); # 对于这个容差，最后两个顶点被认为是相同的
    ?uniquevertices(vtx, 0.01); # 当容差减小时，最后两个顶点被区分开
    result: 
    0  0  0   
    1  0  0   
    1  1  0   
    result: 
    0  0  0   
    1  0  0   
    1  1  0   
    1  1  0.09   

**参见**

[命令列表](./360037228834.md), [unique](./unique.md)
