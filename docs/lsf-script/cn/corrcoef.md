<!-- Translation completed: 2026-02-04 -->
<!-- Original command: corrcoef -->

# corrcoef

**语法** | **描述**
---|---
corrcoef(A);  corrcoef(A, B); | 计算 the correlation 矩阵.  R = corrcoef(A) 返回 the 矩阵 of correlation coefficients for A, where the columns of A represent random variables and the rows represent observations.  R = corrcoef(A, B) 返回 the correlation coefficients between two random variables A and B. If A and B are vectors of observations with equal 长度, corrcoef(A, B) is the 2-by-2 correlation 矩阵; if A and B are matrices of observations, corrcoef(A, B) treats A and B as vectors and is equivalent to corrcoef(A(1:lenght(A)), B(1:长度(B))). A and B must have equal 大小.

**示例**

The following 示例 illustrate how to find the covariance 矩阵. 
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

The following 示例 illustrate how to find the covariance 矩阵. 
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

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ cov ](/hc/en-us/articles/360034406674-cov) , [ corrtransf ](/hc/en-us/articles/360034926913-corrtransf)
