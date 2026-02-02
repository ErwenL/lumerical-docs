# reshape

Reshapes the matrix A to have a given size i,j,k.The product of the specified dimensions, i*j*k*..., must be the same as that of the original matrix A. 

**Syntax** |  **Description**  
---|---  
out = reshape(A, [i,j,k, ...])  |  Returns an array with the same elements as A but reshaped to have the size i by j by k by ...   
  
**Example**

Simple example showing how to reshape a 2D matrix. 
    
    
    ?A=[1,2,3;4,5,6];
    ?B=reshape(A,[2,3]); # do nothing
    ?B=reshape(A,[3,2]); # reshape to 3 rows, 2 columns
    ?B=reshape(A,[1,6]); # create single row vector
    ?B=transpose(A);   # transpose function, for comparison
    result: 
    1 2 3 
    4 5 6 
    result: 
    1 2 3 
    4 5 6 
    result: 
    1 5 
    4 3 
    2 6 
    result: 
    1 4 2 5 3 6 
    result: 
    1 4 
    2 5 
    3 6 

Matrices of higher dimensionality can also be reshaped. 
    
    
    A=matrix(2,3,4);
    A(1:2,1:3,1) = [1, 2, 3; 4, 5, 6];
    A(1:2,1:3,2) = [7, 8, 9; 10,11,12];
    A(1:2,1:3,3) = [13,14,15;16,17,18];
    A(1:2,1:3,4) = [19,20,21;22,23,24];
    ?A;
    ?B=reshape(A,[6,4]);   # reshape to 2D matrix
    ?B=reshape(A,[1,2*3*4]); # reshape all data into a single row vector
    B=permute(A,[2,1,3]);   # transpose 1st & 2nd dimension
    ?C=reshape(B,[1,2*3*4]); # then reshape to a single row vector
    result(i,j,1):
    1 2 3 
    4 5 6 
    result(i,j,2):
    7 8 9 
    10 11 12 
    result(i,j,3):
    13 14 15 
    16 17 18 
    result(i,j,4):
    19 20 21 
    22 23 24 
    result: 
    1 7 13 19 
    4 10 16 22 
    2 8 14 20 
    5 11 17 23 
    3 9 15 21 
    6 12 18 24 
    result: 
    1 4 2 5 3 6 7 10 8 11 9 12 13 16 14 17 15 18 19 22 20 23 21 24 
    result: 
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ = ](/hc/en-us/articles/360034929513--) , [ == ](/hc/en-us/articles/360034930893--) , [ != ](/hc/en-us/articles/360034930913--) , [ <= ](/hc/en-us/articles/360034410314--) , [ >= ](/hc/en-us/articles/360034930933--) , [ < ](/hc/en-us/articles/360034410334--) , [ > ](/hc/en-us/articles/360034930953--) , [ & ](/hc/en-us/articles/360034930973--) , [ and ](/hc/en-us/articles/360034410354-and) , [ | ](/hc/en-us/articles/360034410374--) , [ or ](/hc/en-us/articles/360034930993-or) , [ ! ](/hc/en-us/articles/360034931013--) , [ ~ ](/hc/en-us/articles/360034931033--) , [ eig ](/hc/en-us/articles/360034925793-eig) , [ permute ](/hc/en-us/articles/360034925853-permute) , [ mult ](/hc/en-us/articles/360034925813-mult) , [ inv ](/hc/en-us/articles/360034405754-inv) , [ flip ](/hc/en-us/articles/360034925833-flip) , [ transpose ](/hc/en-us/articles/360034925973-transpose) , [ size ](/hc/en-us/articles/360034405654-size)
