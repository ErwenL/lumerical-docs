<!-- Translation completed: 2026-02-04 -->
<!-- Original command: chol -->

# chol

**语法** | **描述**
---|---
L = chol(A); | 返回 a lower triangular 矩阵 L that satisfies the equation A = mult(L,ctranspose(L))

**示例**

Find the Cholesky decomposition of a 3x3 矩阵. 
    ?A = [4, 12, -16; 12, 37, -43; -16,-43,98];
    ?L = chol(A);
    ?mult(L,ctranspose(L)); #This should be the same as A
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

Find the Cholesky decomposition of a 3x3 矩阵. 
    ?A = [4, 12, -16; 12, 37, -43; -16,-43,98];
    ?L = chol(A);
    ?mult(L,ctranspose(L)); #This should be the same as A
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

**另请参阅**

[ List of commands ](/hc/en-us/articles/360037228834) , [ mult ](/hc/en-us/articles/360034925813-mult) , [ ctranspose ](/hc/en-us/articles/360034405894-ctranspose)
