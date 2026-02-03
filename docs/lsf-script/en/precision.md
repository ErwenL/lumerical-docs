# precision

Truncates a number to the precision specified by the user. The precision is specified by the desired number of significant figures used when rounding the number. 

**Syntax** |  **Description**  
---|---  
out = precision (y,p);  |  Truncates y to a user defined precision p. Where p is the number of significant figures.   
  
###  Example 

Show different values of ‘pi’ depending on the user defined precision. 
    
    
    ?pi;
    result: 
    3.14159  
    ?precision(pi,2);
    result: 
    3.1 
    ?precision(pi,3);
    result: 
    3.14 
    ?precision(pi,4);
    result: 
    3.142
    ?precision(pi/100,4);
    result: 
    0.03142 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ round ](/hc/en-us/articles/360034406194-round)
