<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getperiodicity -->

# getperiodicity

**语法** | **描述**
---|---
out = getperiodicity("solvername"); | 返回 the periodicity 向量(s) of the system based on the active periodic 边界 conditions in the named 求解器. The 输出 is a [3XN] 矩阵 where N is the 数字 of 维度 that have active periodic 边界 conditions (typically one or two).
solvername | required

**示例**

This 示例 retrieves the periodicity vectors from a DGTD 仿真 with periodic 边界 conditions. 
    period = getperiodicity("DGTD"); 

This 示例 retrieves the periodicity vectors from a DGTD 仿真 with periodic 边界 conditions. 
    period = getperiodicity("DGTD"); 

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getsourcedirection ](/hc/en-us/articles/360034927333-getsourcedirection) , [ gratingorders ](/hc/en-us/articles/360034927353-gratingorders) , [ gratingprojection ](/hc/en-us/articles/360034927373-gratingprojection)
