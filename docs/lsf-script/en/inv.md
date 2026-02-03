# inv

Calculates the inverse of a matrix. The matrix has to be invertible.

**Syntax** |  **Description**  
---|---  
out = inv(A) |  Returns the inverse of matrix A.  
out = inv(A, tol); |  Returns the Moore-Penrose pseudoinverse of matrix A, with a tolerance of "tol".  
  
**Examples**

Invert a matrix and multiply by original matrix to get the identity.
    
    
    A= [ 1, 2; 3, 4];
    B= inv(A);
    ?mult(B,A);  # This should return the identity matrix
    result: 
    1 0 
    0 1  

Derive the Moore-Penrose pseudoinverse of the same matrix, with a tolerance of 0.1.
    
    
    ?C = inv(A, 0.1);  
    result:   
    0.0426428 0.0963963   
    0.0605104 0.136787 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ = ](/hc/en-us/articles/360034929513--) , [ == ](/hc/en-us/articles/360034930893--) , [ != ](/hc/en-us/articles/360034930913--) , [ <= ](/hc/en-us/articles/360034410314--) , [ >= ](/hc/en-us/articles/360034930933--) , [ < ](/hc/en-us/articles/360034410334--) , [ > ](/hc/en-us/articles/360034930953--) , [ & ](/hc/en-us/articles/360034930973--) , [ and ](/hc/en-us/articles/360034410354-and) , [ | ](/hc/en-us/articles/360034410374--) , [ or ](/hc/en-us/articles/360034930993-or) , [ ! ](/hc/en-us/articles/360034931013--) , [ ~ ](/hc/en-us/articles/360034931033--) , [ eig ](/hc/en-us/articles/360034925793-eig) , [ mult](/hc/en-us/articles/360034925813-mult), [solve](/hc/en-us/articles/360041139833)
