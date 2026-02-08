# permute

This function is a more general version of the transpose function. It allows matrix dimensions to be rearranged as needed. 

**Syntax** |  **Description**  
---|---  
out = permute(A, [i,j,k, ...])  |  Returns a matrix with the same elements as A but with rearranged dimensions i,j,k, etc.   
  
**Example**

The permute function can do the same as the transpose function. 
    
    
    ?A=[1,2,3;4,5,6];
    ?B=permute(A,[1,2]); # do nothing
    ?B=permute(A,[2,1]); # swap rows and columns. same as transpose
    ?B=transpose(A);   # transpose function, for comparison
    result: 
    1 2 3 
    4 5 6 
    result: 
    1 2 3 
    4 5 6 
    result: 
    1 4 
    2 5 
    3 6 
    result: 
    1 4 
    2 5 
    3 6 

However, the permute function is more general and allows for additional operations. 
    
    
    A=matrix(2,3,4);
    A(1:2,1:3,1) = [1, 2, 3; 4, 5, 6];
    A(1:2,1:3,2) = [7, 8, 9; 10,11,12];
    A(1:2,1:3,3) = [13,14,15;16,17,18];
    A(1:2,1:3,4) = [19,20,21;22,23,24];
    ?A;
    ?B=permute(A,[1,2,3]);  # do nothing
    ?B=permute(A,[3,2,1]);  # transpose 1st and 3rd dimension
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
    result(i,j,1):
    1 2 3 
    7 8 9 
    13 14 15 
    19 20 21 
    result(i,j,2):
    4 5 6 
    10 11 12 
    16 17 18 
    22 23 24 
    result: 
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ = ](/hc/en-us/articles/360034929513--) , [ == ](/hc/en-us/articles/360034930893--) , [ != ](/hc/en-us/articles/360034930913--) , [ <= ](/hc/en-us/articles/360034410314--) , [ >= ](/hc/en-us/articles/360034930933--) , [ < ](/hc/en-us/articles/360034410334--) , [ > ](/hc/en-us/articles/360034930953--) , [ & ](/hc/en-us/articles/360034930973--) , [ and ](/hc/en-us/articles/360034410354-and) , [ | ](/hc/en-us/articles/360034410374--) , [ or ](/hc/en-us/articles/360034930993-or) , [ ! ](/hc/en-us/articles/360034931013--) , [ ~ ](/hc/en-us/articles/360034931033--) , [ eig ](/hc/en-us/articles/360034925793-eig) , [ reshape ](/hc/en-us/articles/360034925873-reshape) , [ mult ](/hc/en-us/articles/360034925813-mult) , [ inv ](/hc/en-us/articles/360034405754-inv) , [ flip ](/hc/en-us/articles/360034925833-flip) , [ transpose ](/hc/en-us/articles/360034925973-transpose) , [ size ](/hc/en-us/articles/360034405654-size)
