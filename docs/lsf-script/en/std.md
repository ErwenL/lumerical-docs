# std

Returns the standard deviation of the all entries of the specified matrix. The standard deviation of a set of N numbers X = [x  1  ,...,x  N  ] is defined as 

$$ \sigma=\sqrt{\frac{1}{N} \sum_{i=1}^{N}\left(x_{i}-\mu\right)^{2}} $$ 

where  μ  is the mean of X. 

**Syntax** |  **Description**  
---|---  
out = std(A);  |  Will return the standard deviation of matrix A, over all dimensions.   
  
**Example**

These are some simple examples showing how to use this command. 
    
    
    a =[1,2,3,4,5];
    ?std(a);
    result: 
    1.41421 
    b =[1,2,3,4,5;5,4,3,2,1;1,4,2,5,8];
    ?std(b);
    ?sqrt(sum((b-mean(b))^2)/length(b)); # Compare with equivalent calculation using sum and mean
    result: 
    1.88562
    result: 
    1.88562  
    d = randmatrix(3,3,3);
    ?d;
    result(i,j,1):
    0.345988 0.84698 0.271889 
    0.471725 0.316874 0.982971 
    0.374981 0.456099 0.2978 
    result(i,j,2):
    0.739189 0.761315 0.5009 
    0.567278 0.839442 0.890164 
    0.19599 0.397656 0.0274667 
    result(i,j,3):
    0.994629 0.531327 0.626759 
    0.572588 0.194067 0.657613 
    0.0505081 0.843043 0.197851
     
    ?std(d);
    result: 
    0.274514

**See Also**

[ var ](/hc/en-us/articles/360034406354-var) , [ mean ](/hc/en-us/articles/360034406314-mean) , [ sum ](/hc/en-us/articles/360034405694-sum) , [ length ](/hc/en-us/articles/360034925653-length)
