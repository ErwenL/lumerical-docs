# corrtransf

Calculates the transformation matrix to generate multiple sequences of correlated random variables. 

**Syntax** |  **Description**  
---|---  
corrtransf(A);  |  Calculate the transformation matrix to generate multiple sequences of correlated random variables given a correlation matrix A.   
  
**Example**

This is a simple example of the command. 
    
    
    A = [1,2;3,4];
    ?corrtransf(cov(A));
    result: 
    -1  -1  
    -4.09555e-009  4.09555e-009 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ cov ](/hc/en-us/articles/360034406674-cov) , [ corrcoef ](/hc/en-us/articles/360034406694-corrcoef)
