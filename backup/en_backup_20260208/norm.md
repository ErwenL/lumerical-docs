# norm

Returns the natural norm of a matrix induced by the L2-norm (spectral norm). For a matrix A this is the square root of the maximum eigenvalue of the matrix product A  H  A, where A  H  is the conjugate transpose of A. 

Note that for a N-dimensional complex vector x = [x  1  ,x  2  ,...,x  N  ] this reduces to the usual norm: 

$$ \|x\|=\sqrt{\sum_{i=1}^{N} x_{i}^{*} x_{i}}=\sqrt{\sum_{i=1}^{N}\left|x_{i}\right|^{2}} $$ 

**Syntax** |  **Description**  
---|---  
out = norm(y);  |  Returns the spectral norm of the matrix y.   
  
**Example**

Find the usual norm of real and complex vectors. 
    
    
    y1=[1,2,3];
    y2=[1+1i,2,3]; #y2 has complex elements
    ?norm(y1);
    ?norm(y2);
    result: 
    3.74166  
    result: 
    3.87298  
    # Confirm the results with the usual definition:
    ?sqrt(sum(conj(y1)*y1));
    ?sqrt(sum(conj(y2)*y2));
    result: 
    3.74166  
    result: 
    3.87298+0i  

Find the usual norm of a complex matrix. 
    
    
    A=[1,2+7i,3;7+3i,0,9];
    ?norm(A);
    ?sqrt(max(eig(mult(ctranspose(A),A)))); # confirm the result using the definition
    result: 
    12.332  
    result: 
    12.332  

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ sqrt ](/hc/en-us/articles/360034925613-sqrt) , [ sum ](/hc/en-us/articles/360034405694-sum) , [ conj ](/hc/en-us/articles/360034925533-conj) , [ max ](/hc/en-us/articles/360034925693-max) , [ eig ](/hc/en-us/articles/360034925793-eig) , [ mult ](/hc/en-us/articles/360034925813-mult) , [ ctranspose ](/hc/en-us/articles/360034405894-ctranspose)
