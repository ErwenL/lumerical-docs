# cross

Calculates the vector cross product of two matrices, which must have the same size. The cross product will be computed on the first dimension that has a size of 3. There must be at least one dimension with a size of 3.

Assume that A,B are 2D matrices, where the second dimension contains the vector components. The size of the second dimension must be 3. Then the elements of C will be calculated with the standard cross product formulas.

$$ \begin{array}{l}{\mathbf{C}(i, 1)=+\mathbf{A}(i, 2) \mathbf{B}(i, 3)-\mathbf{A}(i, 3) \mathbf{B}(i, 2)} \\\ {\mathbf{C}(i, 2)=-\mathbf{A}(i, 1) \mathbf{B}(i, 3)+\mathbf{A}(i, 3) \mathbf{B}(i, 1)} \\\ {\mathbf{C}(i, 3)=+\mathbf{A}(i, 1) \mathbf{B}(i, 2)-\mathbf{A}(i, 2) \mathbf{B}(i, 1)}\end{array} $$

**Syntax** |  **Description**  
---|---  
C = cross(A, B); |  Returns the cross product of A and B  
  
**Example**

Calculate the cross product of (1,1,0) and (0,1,0).
    
    
    A=[1,1,0];
    B=[0,1,0];
    ?C=cross(A,B);
    return: 
    0  0  1

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ dot ](/hc/en-us/articles/360034925773-dot) , [ * ](/hc/en-us/articles/360034930833--) , [ length ](/hc/en-us/articles/360034925653-length) , [ size ](/hc/en-us/articles/360034405654-size)
