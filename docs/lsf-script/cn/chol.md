<!--
Translation from English documentation
Original command: chol
Translation date: 2026-02-04 22:49:48
-->

# chol

计算 该 Cholesky lower triangular factorization 或 decomposition. For 一个 given 矩阵 A, chol 返回 一个 lower triangular 矩阵 L such 该 A 是 该 矩阵 product 的 L 和 its conjugate transpose. The 矩阵 A 可以 为 real 或 complex but it 必须 为 Hermitian 和 positive-definite. 

**语法** |  **描述**  
---|---  
L = chol(A);  |  返回 一个 lower triangular 矩阵 L 该 satisfies 该 equation A = mult(L,ctranspose(L))   
  
**示例**

Find 该 Cholesky decomposition 的 一个 3x3 矩阵. 
    
    
    ?A = [4, 12, -16; 12, 37, -43; -16,-43,98];
    ?L = chol(A);
    ?mult(L,ctranspose(L)); #This 应该 为 该 same as A
    result: 
    4  12  -16  
    12  37  -43  
    -16  -43  98  
    result: 
    2+0i  0+0i  0+0i  
    6+0i  1+0i  0+0i  
    -8+0i  5+0i  3+0i  
    result: 
    4+0i  12+0i  -16+0i  
    12+0i  37+0i  -43+0i  
    -16+0i  -43+0i  98+0i  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ mult ](/hc/en-us/articles/360034925813-mult) , [ ctranspose ](/hc/en-us/articles/360034405894-ctranspose)
