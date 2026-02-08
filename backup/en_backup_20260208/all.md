# all

Returns 1 if all of the specified matrix entries are nonzero and returns 0 otherwise. 

**Syntax** |  **Description**  
---|---  
out = all(A);  |  Will return 1 if all of the A matrix entries are nonzero and will return 0 otherwise.   
out = all(A,n);  |  n is an optional parameter to analyze entries in a specific dimension   
  
**Example**

The following is a simple example showing how to use this command. 
    
    
    a = [1,4,3,0.5];
    b = [1,3;6,0];
    ?all(a);
    ?all(b);
    result:
    1
    result: 
    0  
    ?all(b,2);
    result: 
    1  
    0   
    

**See Also**

[ any ](/hc/en-us/articles/360034926573-any) , [ almostequal ](/hc/en-us/articles/360034410294-almostequal)
