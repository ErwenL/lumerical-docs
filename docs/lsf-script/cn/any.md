<!-- Translation completed: 2026-02-04 -->
<!-- Original command: any -->

# any

**语法** | **描述**
---|---
out = any(A); | Will 返回 1 if any of the A 矩阵 entries are nonzero and will 返回 0 otherwise.
out = any(A,n); | n is an optional 参数 to analyze entries in a specific 维度

**示例**

The following is a simple 示例 showing how to use this 命令. 
    a = [0,0,3,0];
    b = [1,3;6,0.1];
    d = [0;0;0;0];
    ?any(a);
    ?any(b);
    ?any(d);
    result:
    1
    result:
    1  
    result: 
    0  
    ?any(a,1);
    result: 
    0  
    0  
    1  
    0 

The following is a simple 示例 showing how to use this 命令. 
    a = [0,0,3,0];
    b = [1,3;6,0.1];
    d = [0;0;0;0];
    ?any(a);
    ?any(b);
    ?any(d);
    result:
    1
    result:
    1  
    result: 
    0  
    ?any(a,1);
    result: 
    0  
    0  
    1  
    0 

**另请参阅**

[ all ](/hc/en-us/articles/360034406334-all) , [ almostequal ](/hc/en-us/articles/360034410294-almostequal)
