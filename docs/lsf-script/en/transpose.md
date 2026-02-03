# transpose

Transposes a 1D or 2D matrix. 

**Syntax** |  **Description**  
---|---  
y = transpose(x);  |  If x is an N x M matrix, then y will be M x N, where the entries are y(j,i)=x(i,j).   
  
**Example**

Simple example of how to transpose a 2D matrix. 
    
    
    ?A = [1,2,3;4,5,6];
    ?AT = transpose(A); # transpose of A
    result:
    1  2  3  
    4  5  6  
    result: 
    1  4  
    2  5  
    3  6  

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ ctranspose ](/hc/en-us/articles/360034405894-ctranspose) , [ reshape ](/hc/en-us/articles/360034925873-reshape) , [ flip ](/hc/en-us/articles/360034925833-flip) , [ permute ](/hc/en-us/articles/360034925853-permute) , [ size ](/hc/en-us/articles/360034405654-size)
