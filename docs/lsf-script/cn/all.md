<!--
Translation from English documentation
Original command: all
Translation date: 2026-02-04 22:49:36
-->

# all

返回 1 如果 all 的 该 specified 矩阵 entries 是 nonzero 和 返回 0 otherwise. 

**语法** |  **描述**  
---|---  
out = all(A);  |  Will 返回 1 如果 all 的 该 A 矩阵 entries 是 nonzero 和 将 返回 0 otherwise.   
out = all(A,n);  |  n 是 一个 optional 参数 到 analyze entries 在 一个 specific 维度   
  
**示例**

The following 是 一个 simple example showing 如何 到 use 此 命令. 
    
    
    一个 = [1,4,3,0.5];
    b = [1,3;6,0];
    ?all(一个);
    ?all(b);
    result:
    1
    result: 
    0  
    ?all(b,2);
    result: 
    1  
    0   
    

**参见**

[ any ](/hc/en-us/articles/360034926573-any) , [ almostequal ](/hc/en-us/articles/360034410294-almostequal)
