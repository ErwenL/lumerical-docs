<!--
Translation from English documentation
Original command: conv2
Translation date: 2026-02-04 22:49:48
-->

# conv2

返回 该 Convolution 的 two 2-dimensional arrays. 

**语法** |  **描述**  
---|---  
out = conv2(A,B,mode)  |  Computes 该 convolution 的 two 2-d dimensional matrices A 和 B.  mode =  'full': computes 该 full convolution 的 A 和 B.  'same': computes 该 central part 的 该 full convolution, result 矩阵 C 是 restricted 到 该 size 的 A,   
  
**示例**

In 该 following example, we computes 该 'full' 和 'same' convolution results 的 matrices A 和 B: 
    
    
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

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ integrate ](/hc/en-us/articles/360034405814-integrate) , [ integrate2 ](/hc/en-us/articles/360034405834-integrate2) , [ max ](/hc/en-us/articles/360034925693-max) , [ min ](/hc/en-us/articles/360034925713-min) , [ interp ](/hc/en-us/articles/360034925893-interp) , [ find ](/hc/en-us/articles/360034405874-find) , [ pinch ](/hc/en-us/articles/360034405674-pinch) , [ round ](/hc/en-us/articles/360034406194-round) , [ getdata ](/hc/en-us/articles/360034409834-getdata) , [ sum ](/hc/en-us/articles/360034405694-sum) , [ 长度 ](/hc/en-us/articles/360034925653-长度)
