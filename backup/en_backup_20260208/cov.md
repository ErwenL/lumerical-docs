# cov

Calculates the covariance matrix. The input can be one matrix, which contains the observations of a set of random variables, or two matrices, each one representing a vector of observations. 

**Syntax** |  **Description**  
---|---  
cov(A);  cov(A, B);  |  Calculate the covariance matrix.  C = cov(A) returns the covariance. A is a matrix where columns represent random variables and rows represent observations; C is the covariance matrix with the corresponding column variances along the diagonal.  C = cov(A, B) returns the covariance between two random variables A and B. If A and B are vectors of observations with equal length, cov(A, B) is the 2-by-2 covariance matrix; if A and B are matrices of observations, cov(A, B) treats A and B as vectors and is equivalent to cov(A(1:lenght(A)), B(1:length(B))). A and B must have equal size.   
  
**Example**

The following examples illustrate how to find the covariance matrix. 
    
    
    A = [1,2;3,4];
    B = [1.1,2.7; 2.5, 4.3];
    ?cov(A,B);
    ?cov(A(1:length(A)),B(1:length(B)));
    result: 
    1.25  1.175  
    1.175  1.2875  
    result: 
    1.25  1.175  
    1.175  1.2875  

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ corrcoef ](/hc/en-us/articles/360034406694-corrcoef) , [ corrtransf ](/hc/en-us/articles/360034926913-corrtransf)
