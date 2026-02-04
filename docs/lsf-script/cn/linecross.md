<!--
Translation from English documentation
Original command: linecross
Translation date: 2026-02-04 22:50:01
-->

# linecross

Determines 如果 two line segments 在 该 x-y plane cross each other. 

Line segments 是 contained 在 一个 single 矩阵 的 维度 2*Nx2, 其中 there 是 N line segments. For example, 该 矩阵 L = [ 0,0; 1,1; 0,0; 0,1]; represents two lines segments, one 从 (0,0) 到 (1,1) 和 another 从 (0,0) 到 (0,1). 

**语法** |  **描述**  
---|---  
out = linecross(L1,L2);  |  返回 一个 数组 的 维度 N 该 determines 如果 该 N line segments 在 L1 和 该 N line segments 在 L2 cross; 该 comparison 是 done pairwise as 在 该 lineintersect 命令. L1 和 L2 必须 have 该 same size (2*Nx2 用于 N line segments). The elements 在 该 output 数组 是 0 如果 该 segments do not cross, 1 如果 they cross 和 0.5 如果 该 endpoint 的 one segment touches 该 other. Line segments 该 是 coincident 和 touch also 返回 一个 值 的 0.5   
  
**示例**

The following examples illustrate 该 different outcomes 的 该 linecross 函数: 
    
    
    L1 = [ 0,0; 1,1; 0,0; 1,1 ];
    L2 = [ 0,1; 1,0; 2,2; 3,3 ];
    ?linecross(L1,L2);
    result: 
    1  
    0
    L1 = [ 0,0; 1,1 ];
    L2 = [ 0.5,0.5; 0,1 ]; # The start point 的 L2 touches L1
    ?linecross(L1,L2);
    result: 
    0.5 
    L1 = [ 0,0; 1,1 ];
    L2 = [ 1,1; 2,2 ]; # The end point 的 L1 是 该 same as 该 start point 的 L2
    ?linecross(L1,L2);
    result: 
    0.5 
    L1 = [ 0,0; 1,1 ];
    ?linecross(L1,L1);
    result: 
    0.5

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ lineintersect ](/hc/en-us/articles/360034926333-lineintersect) , [ finite ](/hc/en-us/articles/360034926453-finite)
