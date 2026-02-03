# conv2

Returns the Convolution of two 2-dimensional arrays. 

**Syntax** |  **Description**  
---|---  
out = conv2(A,B,mode)  |  Computes the convolution of two 2-d dimensional matrices A and B.  mode =  'full': computes the full convolution of A and B.  'same': computes the central part of the full convolution, result matrix C is restricted to the size of A,   
  
**Example**

In the following example, we computes the 'full' and 'same' convolution results of matrices A and B: 
    
    
    matA = [-5;-4;-3;-2;-1;0;1;2;3;4;5]*pi;
    matB = [-3,-2,-1,0];
    matCFull = conv2(matA, matB, 'full');
    matCSame = conv2(matA, matB, 'same');
    >?matCFull;
    result: 
    47.1239  31.4159  15.708  0  
    37.6991  25.1327  12.5664  0  
    28.2743  18.8496  9.42478  0  
    18.8496  12.5664  6.28319  0  
    9.42478  6.28319  3.14159  0  
    0  0  0  0  
    -9.42478  -6.28319  -3.14159  0  
    -18.8496  -12.5664  -6.28319  0  
    -28.2743  -18.8496  -9.42478  0  
    -37.6991  -25.1327  -12.5664  0  
    -47.1239  -31.4159  -15.708  0   
    >?matCSame;
    result: 
    15.708  
    12.5664  
    9.42478  
    6.28319  
    3.14159  
    0  
    -3.14159  
    -6.28319  
    -9.42478  
    -12.5664  
    -15.708 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ integrate ](/hc/en-us/articles/360034405814-integrate) , [ integrate2 ](/hc/en-us/articles/360034405834-integrate2) , [ max ](/hc/en-us/articles/360034925693-max) , [ min ](/hc/en-us/articles/360034925713-min) , [ interp ](/hc/en-us/articles/360034925893-interp) , [ find ](/hc/en-us/articles/360034405874-find) , [ pinch ](/hc/en-us/articles/360034405674-pinch) , [ round ](/hc/en-us/articles/360034406194-round) , [ getdata ](/hc/en-us/articles/360034409834-getdata) , [ sum ](/hc/en-us/articles/360034405694-sum) , [ length ](/hc/en-us/articles/360034925653-length)
