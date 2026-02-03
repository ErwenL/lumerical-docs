# amin

Returns the minimum value in a specified dimension of a matrix. For complex numbers, only the real part is considered. 

**Syntax** |  **Description**  
---|---  
out = amin(x,n);  |  The minimum value in the specified dimension n of matrix x.   
  
**Example**

Find the minimum value of the first dimension of a matrix: 
    
    
    A = randmatrix(5,4);
    B = amin(A,1); # vector length 4, B[i] = min(A(1:5,i))

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ min ](/hc/en-us/articles/360034925713-min) , [ max ](/hc/en-us/articles/360034925693-max) , [ abs ](/hc/en-us/articles/360034925553-abs) , [ mean ](/hc/en-us/articles/360034406314-mean) , [ amax ](/hc/en-us/articles/360034925733-amax)
