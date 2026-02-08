# mult

Performs matrix multiplication of two or more matrices. The dimensions of the matrices have to match. 

**Syntax** |  **Description**  
---|---  
out = mult(A,B,...)  |  Returns the matrix multiplication of matrices A, B, C ... Dimension of matrices must match; for example, if A is an MxN matrix and B is a NXP matrix, mult(A,B) has dimensions MxP.   
  
**Example**

Find the matrix product of two matrices. 
    
    
    A = [ 1, 2; 2, 4];
    B = [ 2, 5; -1, 3];
    ?mult(A,B);
    result: 
    0 11 
    0 22 
    ?mult(A,B,[1;2]);
    result: 
    22 
    44

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ = ](/hc/en-us/articles/360034929513--) , [ == ](/hc/en-us/articles/360034930893--) , [ != ](/hc/en-us/articles/360034930913--) , [ <= ](/hc/en-us/articles/360034410314--) , [ >= ](/hc/en-us/articles/360034930933--) , [ < ](/hc/en-us/articles/360034410334--) , [ > ](/hc/en-us/articles/360034930953--) , [ & ](/hc/en-us/articles/360034930973--) , [ and ](/hc/en-us/articles/360034410354-and) , [ | ](/hc/en-us/articles/360034410374--) , [ or ](/hc/en-us/articles/360034930993-or) , [ ! ](/hc/en-us/articles/360034931013--) , [ ~ ](/hc/en-us/articles/360034931033--) , [ eig ](/hc/en-us/articles/360034925793-eig) , [ permute ](/hc/en-us/articles/360034925853-permute) , [ reshape ](/hc/en-us/articles/360034925873-reshape) , [ inv ](/hc/en-us/articles/360034405754-inv)
