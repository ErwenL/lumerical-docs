<!--
Translation from English documentation
Original command: lineintersect
Translation date: 2026-02-04 22:50:01
-->

# lineintersect

返回 该 intersection points 的 two lines 在 该 x-y plane. 注意 该 该 intersection point does not have 到 lie 在 该 segments 该 define 该 lines. Use 该 命令 linecross 到 determine 如果 该 line segments actually cross . 

Line segments 是 contained 在 一个 single 矩阵 的 维度 2*Nx2, 其中 there 是 N line segments. For example, 该 矩阵 L = [ 0,0; 1,1; 0,0; 0,1]; represents two lines segments, one 从 (0,0) 到 (1,1) 和 another 从 (0,0) 到 (0,1). 

**语法** |  **描述**  
---|---  
out = lineintersect(L1,L2);  |  返回 该 intersection 的 该 lines represented 通过 该 segments 在 L1 和 L2. L1 和 L2 必须 have 该 same size (2*Nx2 用于 N line segments). The result 是 一个 sequence 的 x,y points 在 该 form Nx2 representing 该 pairwise intersections 的 该 N lines. There 是 special cases 当 

  * The lines 是 parallel. In 此 case, 该 position returned 是 (1.#INF,b). The 存在 的 1.#INF 可以 为 tested 使用 该 脚本 命令 finite. The 值 的 b 是 0 如果 该 lines coincide 和 1 如果 they do not. 
  * The points 在 一个 segment 是 degenerate, i.e., 该 same. In 此 case, 该 position returned 是 (1.#INF,b), 其中 b 是 0, 1 或 2 如果 both line segments 是 degenerate, 该 first 是 degenerate, 或 该 second 是 degenerate, respectively. 

  
  
**示例**

In 此 first example L1 和 L2 是 two 设置 的 segments; 该 result 是 一个 2x2 矩阵 其中 该 first row 是 该 intersection between 该 first segments 在 each 设置 和 该 second row 是 该 intersection between 该 second segments 在 each 设置. 
    
    
    L1 = [ 0,0; 1,1; 0,10; 1,10];
    L2 = [ 0,1; 1,0; 5,0; 5,1];
    ?lineintersect(L1,L2);
    result: 
    0.5  0.5  
    5  10  

The second example shows 该 output 在 该 special cases 当 该 lines do not intersect, 当 they coincide 或 当 该 segments 是 degenerate. 
    
    
    L1 = [ 0,0; 1,1];
    L2 = [ 1,0; 2,1]; #L2 是 parallel 到 L1
    L3 = [ 3,3; 3,3]; #The points 在 L3 是 degenerate
    ?lineintersect(L1,L1);
    ?lineintersect(L1,L2);
    ?lineintersect(L3,L3);
    ?lineintersect(L3,L1);
    ?lineintersect(L2,L3);
    result: 
    1.#INF  1  
    result: 
    1.#INF  0  
    result: 
    1.#INF  0  
    result: 
    1.#INF  1
    result: 
    1.#INF  2    

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ linecross ](/hc/en-us/articles/360034406154-linecross) , [ finite ](/hc/en-us/articles/360034926453-finite)
