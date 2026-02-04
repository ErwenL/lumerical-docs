<!--
Translation from English documentation
Original command: cross
Translation date: 2026-02-04 22:49:48
-->

# cross

计算 该 向量 cross product 的 two matrices, 该 必须 have 该 same size. The cross product 将 为 computed 在 该 first 维度 该 has 一个 size 的 3. There 必须 为 at least one 维度 使用 一个 size 的 3.

Assume 该 A,B 是 2D matrices, 其中 该 second 维度 contains 该 向量 components. The size 的 该 second 维度 必须 为 3. Then 该 elements 的 C 将 为 calculated 使用 该 standard cross product formulas.

$$ \begin{数组}{l}{\mathbf{C}(i, 1)=+\mathbf{A}(i, 2) \mathbf{B}(i, 3)-\mathbf{A}(i, 3) \mathbf{B}(i, 2)} \\\ {\mathbf{C}(i, 2)=-\mathbf{A}(i, 1) \mathbf{B}(i, 3)+\mathbf{A}(i, 3) \mathbf{B}(i, 1)} \\\ {\mathbf{C}(i, 3)=+\mathbf{A}(i, 1) \mathbf{B}(i, 2)-\mathbf{A}(i, 2) \mathbf{B}(i, 1)}\end{数组} $$

**语法** |  **描述**  
---|---  
C = cross(A, B); |  返回 该 cross product 的 A 和 B  
  
**示例**

计算 该 cross product 的 (1,1,0) 和 (0,1,0).
    
    
    A=[1,1,0];
    B=[0,1,0];
    ?C=cross(A,B);
    返回: 
    0  0  1

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ dot ](/hc/en-us/articles/360034925773-dot) , [ * ](/hc/en-us/articles/360034930833--) , [ 长度 ](/hc/en-us/articles/360034925653-长度) , [ size ](/hc/en-us/articles/360034405654-size)
