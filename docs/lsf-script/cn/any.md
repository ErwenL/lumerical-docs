<!--
Translation from English documentation
Original command: any
Translation date: 2026-02-04 22:49:36
-->

# any

返回 1 如果 any 的 该 specified 矩阵 entries 是 nonzero 和 返回 0 otherwise. 

**语法** |  **描述**  
---|---  
out = any(A);  |  Will 返回 1 如果 any 的 该 A 矩阵 entries 是 nonzero 和 将 返回 0 otherwise.   
out = any(A,n);  |  n 是 一个 optional 参数 到 analyze entries 在 一个 specific 维度   
  
**示例 #1**

The following 是 一个 simple example showing 如何 到 use 此 命令. 
    
    
    一个 = [0,0,3,0];
    b = [1,3;6,0.1];
    d = [0;0;0;0];
    ?any(一个);
    ?any(b);
    ?any(d);
    result:
    1
    result:
    1  
    result: 
    0  
    ?any(一个,1);
    result: 
    0  
    0  
    1  
    0 

**参见**

[ all ](/hc/en-us/articles/360034406334-all) , [ almostequal ](/hc/en-us/articles/360034410294-almostequal)
