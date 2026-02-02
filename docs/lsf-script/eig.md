# eig

Finds the eigenvalue and/or eigenvector of a matrix. The matrix has to be square. 

**Syntax** |  **Description**  
---|---  
out = eig(A);  out = eig(A, 1);  |  Returns the eigenvalues of matrix A.   
out = eig(A, 2);  |  Returns the eigenvectors of matrix A.   
out = eig(A, 3);  |  Returns both the eigenvalues and eigenvectors of matrix A.   
  
**Example**

A simple example showing the different options for the results from the eigenvalue calculation. 
    
    
    A = [ 1, 2; 2, 4];
    ?eig(A);
    result: 
    0 
    5 
    ?eig(A,1);
    result: 
    0 
    5 
    ?eig(A,2);
    result: 
    -0.894427 -0.447214 
    0.447214 -0.894427 
    ?eig(A,3);
    result(i,j,1):
    0 0 
    0 5 
    result(i,j,2):
    -0.894427 -0.447214 
    0.447214 -0.894427 
     

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ = ](/hc/en-us/articles/360034929513--) , [ == ](/hc/en-us/articles/360034930893--) , [ != ](/hc/en-us/articles/360034930913--) , [ <= ](/hc/en-us/articles/360034410314--) , [ >= ](/hc/en-us/articles/360034930933--) , [ < ](/hc/en-us/articles/360034410334--) , [ > ](/hc/en-us/articles/360034930953--) , [ & ](/hc/en-us/articles/360034930973--) , [ and ](/hc/en-us/articles/360034410354-and) , [ | ](/hc/en-us/articles/360034410374--) , [ or ](/hc/en-us/articles/360034930993-or) , [ ! ](/hc/en-us/articles/360034931013--) , [ ~ ](/hc/en-us/articles/360034931033--) , [ mult ](/hc/en-us/articles/360034925813-mult) , [ permute ](/hc/en-us/articles/360034925853-permute) , [ reshape ](/hc/en-us/articles/360034925873-reshape) , [ inv ](/hc/en-us/articles/360034405754-inv)
