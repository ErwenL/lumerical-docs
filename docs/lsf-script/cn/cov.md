<!-- Translation completed: 2026-02-04 -->
<!-- Original command: cov -->

# cov

**语法** | **描述**
---|---
cov(A);  cov(A, B); | 计算 the covariance 矩阵.  C = cov(A) 返回 the covariance. A is a 矩阵 where columns represent random variables and rows represent observations; C is the covariance 矩阵 with the corresponding column variances along the 对角线.  C = cov(A, B) 返回 the covariance between two random variables A and B. If A and B are vectors of observations with equal 长度, cov(A, B) is the 2-by-2 covariance 矩阵; if A and B are matrices of observations, cov(A, B) treats A and B as vectors and is equivalent to cov(A(1:lenght(A)), B(1:长度(B))). A and B must have equal 大小.

**示例**

The following 示例 illustrate how to find the covariance 矩阵. 
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

The following 示例 illustrate how to find the covariance 矩阵. 
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

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ corrcoef ](/hc/en-us/articles/360034406694-corrcoef) , [ corrtransf ](/hc/en-us/articles/360034926913-corrtransf)
