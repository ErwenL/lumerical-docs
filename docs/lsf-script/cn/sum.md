<!--
Translation from English documentation
Original command: sum
Translation date: 2026-02-04 22:50:15
-->

# sum

返回 该 sum 的 elements 在 一个 矩阵. 

**语法** |  **描述**  
---|---  
out = sum(x);  |  Sum 的 all 该 elements 在 矩阵 x, over all dimensions.   
out = sum(x,n);  |  Sum elements 的 x over 该 specified 维度 n.   
  
**示例**

This example shows 如何 you 可以 sum all 该 elements 的 一个 矩阵 或 just 该 elements over 一个 specified 维度. 
    
    
    ?一个 = [1,2;3,4]; # define 一个 2x2 矩阵
    result: 
    1 2 
    3 4 
    ?sum(一个); # sum all elements
    result: 
    10
    ?sum(一个,2); # sum over 该 second 维度 only
    result: 
    3 
    7  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ integrate ](/hc/en-us/articles/360034405814-integrate) , [ mean ](/hc/en-us/articles/360034406314-mean) , [ prod ](/hc/en-us/articles/360034925673-prod)
