<!--
Translation from English documentation
Original command: svd
Translation date: 2026-02-04 22:50:15
-->

# svd

返回 一个 3-单元格 数组 使用 该 singular 值 decomposition 的 一个 矩阵 A. The 命令 supports real 和 complex A. 

**语法** |  **描述**  
---|---  
[U,S,V*] = svd(A);  |  返回 一个 3-单元格 数组 使用 该 singular 值 decomposition 的 矩阵 A. S 是 一个 diagonal 矩阵 的 该 same 维度 as A, 使用 non-negative diagonal elements 在 decreasing order. U 和 V* 是 unitary matrices (V* 是 该 conjugate transpose 的 V). If M = svd(A), 那么 A = mult( M{1}, M{2}, M{3} ).   
  
**示例**

Find 该 single 值 decomposition 的 一个 square 矩阵 A 和 的 一个 rectangular 矩阵 B. 
    
    
    A = [ 1.5, 2,0; -2, 1.5,0; 0,0,1.2];
    M=svd(A);
    ?U = M{1};
    ?S = M{2};
    ?V_ctranspose = M{3};
    ?max(abs( mult(U,S,V_ctranspose)-A)); # 此 应该 为 zero
    result:
    -0.6 0.8 0 
    0.8 0.6 0 
    -0 -0 1 
    result: 
    2.5 0 0 
    0 2.5 0 
    0 0 1.2 
    result: 
    -1 -0 -0 
    0 1 -0 
    0 0 1 
    result: 
    2.22045e-016 
    B = [ 1.5, 2,0; -2, 1.5,0];
    M=svd(B);
    ?U = M{1};
    ?S = M{2};
    ?V_ctranspose = M{3};
    ?max(abs( mult(U,S,V_ctranspose)-B)); # 此 应该 为 zero
    result: 
    -1  4.44089e-017  
    4.44089e-017  1  
    result: 
    2.5  0  0  
    0  2.5  0  
    result: 
    -0.6  -0.8  0  
    -0.8  0.6  0  
    0  0  1  
    result: 
    2.22045e-016  

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ eig ](/hc/en-us/articles/360034925793-eig) , [ ctranspose ](/hc/en-us/articles/360034405894-ctranspose) , [ mult ](/hc/en-us/articles/360034925813-mult)
