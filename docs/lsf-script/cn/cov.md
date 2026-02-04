<!--
Translation from English documentation
Original command: cov
Translation date: 2026-02-04 22:49:48
-->

# cov

计算 该 covariance 矩阵. The input 可以 为 one 矩阵, 该 contains 该 observations 的 一个 设置 的 random variables, 或 two matrices, each one representing 一个 向量 的 observations. 

**语法** |  **描述**  
---|---  
cov(A);  cov(A, B);  |  计算 该 covariance 矩阵.  C = cov(A) 返回 该 covariance. A 是 一个 矩阵 其中 columns represent random variables 和 rows represent observations; C 是 该 covariance 矩阵 使用 该 对应的 column variances along 该 diagonal.  C = cov(A, B) 返回 该 covariance between two random variables A 和 B. If A 和 B 是 vectors 的 observations 使用 equal 长度, cov(A, B) 是 该 2-通过-2 covariance 矩阵; 如果 A 和 B 是 matrices 的 observations, cov(A, B) treats A 和 B as vectors 和 是 equivalent 到 cov(A(1:lenght(A)), B(1:长度(B))). A 和 B 必须 have equal size.   
  
**示例**

The following examples illustrate 如何 到 find 该 covariance 矩阵. 
    
    
    A = [1,2;3,4];
    B = [1.1,2.7; 2.5, 4.3];
    ?cov(A,B);
    ?cov(A(1:长度(A)),B(1:长度(B)));
    result: 
    1.25  1.175  
    1.175  1.2875  
    result: 
    1.25  1.175  
    1.175  1.2875  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ corrcoef ](/hc/en-us/articles/360034406694-corrcoef) , [ corrtransf ](/hc/en-us/articles/360034926913-corrtransf)
