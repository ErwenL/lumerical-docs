<!--
Translation from English documentation
Original command: corrtransf
Translation date: 2026-02-04 22:49:48
-->

# corrtransf

计算 该 transformation 矩阵 到 generate multiple sequences 的 correlated random variables. 

**语法** |  **描述**  
---|---  
corrtransf(A);  |  计算 该 transformation 矩阵 到 generate multiple sequences 的 correlated random variables given 一个 correlation 矩阵 A.   
  
**示例**

This 是 一个 simple example 的 该 命令. 
    
    
    A = [1,2;3,4];
    ?corrtransf(cov(A));
    result: 
    -1  -1  
    -4.09555e-009  4.09555e-009 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ cov ](/hc/en-us/articles/360034406674-cov) , [ corrcoef ](/hc/en-us/articles/360034406694-corrcoef)
