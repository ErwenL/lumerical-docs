<!-- Translation completed: 2026-02-04 -->
<!-- Original command: corrtransf -->

# corrtransf

**语法** | **描述**
---|---
corrtransf(A); | 计算 the transformation 矩阵 to generate multiple sequences of correlated random variables given a correlation 矩阵 A.

**示例**

This is a simple 示例 of the 命令. 
    A = [1,2;3,4];
    ?corrtransf(cov(A));
    result: 
    -1  -1  
    -4.09555e-009  4.09555e-009 

This is a simple 示例 of the 命令. 
    A = [1,2;3,4];
    ?corrtransf(cov(A));
    result: 
    -1  -1  
    -4.09555e-009  4.09555e-009 

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ cov ](/hc/en-us/articles/360034406674-cov) , [ corrcoef ](/hc/en-us/articles/360034406694-corrcoef)
