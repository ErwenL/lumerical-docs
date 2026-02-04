<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getsourcedirection -->

# getsourcedirection

**语法** | **描述**
---|---
out = getsourcedirection("sourcename"); | 返回 a [3x1] 矩阵 with a unit 向量 in the direction of the specified 光源 wave 向量.
sourcename | required

**示例**

This 示例 computes a unit 向量 in direction of the k-向量 of the plane wave 光源 named "光源". 
    source_k = getsourcedirection("DGTD::光源"); 

This 示例 computes a unit 向量 in direction of the k-向量 of the plane wave 光源 named "光源". 
    source_k = getsourcedirection("DGTD::光源"); 

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getperiodicity ](/hc/en-us/articles/360034407174-getperiodicity) , [ gratingorders ](/hc/en-us/articles/360034927353-gratingorders) , [ gratingprojection ](/hc/en-us/articles/360034927373-gratingprojection)
