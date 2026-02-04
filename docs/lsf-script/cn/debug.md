<!--
Translation from English documentation
Original command: debug
Translation date: 2026-02-04 22:49:48
-->

# debug

Opens 该 debug utility window. This 命令 是 useful 用于 debugging purposes. When 此 命令 是 used, 脚本 将 run 到 该 line before 该  debug  命令. Then 用户 可以 start 到 call other commands 到 test commands 该 have been run. Once 该 utility window 是 closed, 该 脚本 lines 将 continue 到 run. Multiple  debug  commands 是 allowed. 

**语法** |  **描述**  
---|---  
debug;  |  Opens 该 debug utility window. This 命令 可以 also 为 used 在 该 分析 脚本.   
  
**示例**

This example shows 如何 到 use 该  debug  命令. This below example shows 一个 error 在 line 3. 
    
    
    x=linspace(1,10,10);
    y=linspace(1,10,5);
    ?x*y;
    Error: prompt line 3: 矩阵 参数 的 * 是 not 该 same size
    x=linspace(1,10,10);
    y=linspace(1,10,5);
    debug; # opens 该 debug utility window.
    ?x*y;

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834)
