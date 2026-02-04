<!--
Translation from English documentation
Original command: corrcoef
Translation date: 2026-02-04 22:49:48
-->

# corrcoef

计算 该 correlation 矩阵. The input 可以 为 one 矩阵, 该 contains 该 observations 的 一个 设置 的 random variables, 或 two matrices, each one representing 一个 向量 的 observations. 

**语法** |  **描述**  
---|---  
corrcoef(A);  corrcoef(A, B);  |  计算 该 correlation 矩阵.  R = corrcoef(A) 返回 该 矩阵 的 correlation coefficients 用于 A, 其中 该 columns 的 A represent random variables 和 该 rows represent observations.  R = corrcoef(A, B) 返回 该 correlation coefficients between two random variables A 和 B. If A 和 B 是 vectors 的 observations 使用 equal 长度, corrcoef(A, B) 是 该 2-通过-2 correlation 矩阵; 如果 A 和 B 是 matrices 的 observations, corrcoef(A, B) treats A 和 B as vectors 和 是 equivalent 到 corrcoef(A(1:lenght(A)), B(1:长度(B))). A 和 B 必须 have equal size.   
  
**示例**

The following examples illustrate 如何 到 find 该 covariance 矩阵. 
    
    
    A = [1,2;3,4];
    B = [1.1,2.7; 2.5, 4.3];
    ?corrcoef(A,B);
    ?corrcoef(A(1:长度(A)),B(1:长度(B)));
    result: 
    1  0.92621  
    0.92621  1  
    result: 
    1  0.92621  
    0.92621  1  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ cov ](/hc/en-us/articles/360034406674-cov) , [ corrtransf ](/hc/en-us/articles/360034926913-corrtransf)
