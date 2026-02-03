# flip

Flips (reverses the order of) a matrix along a given dimension. 

**Syntax** |  **Description**  
---|---  
C = flip(A, dim);  |  Flips the matrix A along the dimension dim.   
  
**Example**

Reverse the order of rows and columns of a 2x3 matrix. 
    
    
    ?A=[1,2,3;4,5,6];
    ?B=flip(A,1); # flip (reverse) order of rows
    ?B=flip(A,2); # flip (reverse) order of columns 
    result: 
    1 2 3 
    4 5 6 
    result: 
    4 5 6 
    1 2 3 
    result: 
    3 2 1 
    6 5 4 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ size ](/hc/en-us/articles/360034405654-size) , [ length ](/hc/en-us/articles/360034925653-length) , [ pinch ](/hc/en-us/articles/360034405674-pinch) , [ transpose ](/hc/en-us/articles/360034925973-transpose) , [ reshape ](/hc/en-us/articles/360034925873-reshape) , [ permute ](/hc/en-us/articles/360034925853-permute)
