# !

Is the logical NOT operator. If a value is 0, then NOT returns 1. For all other values, NOT returns 0. NOT(A) is equivalent to A==0, where == is the comparison operator. 

**Syntax** |  **Description**  
---|---  
out = !a;  |  applies logical NOT operator to a   
out = ~a;  |  applies logical NOT operator to a   
  
**Examples**

This example shows the usage of the "!" and "~" operator. 
    
    
    a=1;
    ?!a; #output of not operator
    result: 
    0 
    a=0;
    ?~a; #output of not operator
    result: 
    1 
    a=3;
    ?~a; #output of not operator
    result: 
    0 
    if (!fileexists("filename.fsp")) { 
     save("filename.fsp");
    } 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ == ](/hc/en-us/articles/360034930893--) , [ != ](/hc/en-us/articles/360034930913--) , , [ = ](/hc/en-us/articles/360034930933--) , , , [ & ](/hc/en-us/articles/360034930973--) , [ and ](/hc/en-us/articles/360034410354-and) , [ | ](/hc/en-us/articles/360034410374--) , [ or ](/hc/en-us/articles/360034930993-or) , [ ! ](/hc/en-us/articles/360034931013--) , [ ~ ](/hc/en-us/articles/360034931033--)
