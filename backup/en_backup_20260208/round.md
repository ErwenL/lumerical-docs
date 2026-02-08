# round

Rounds a number to the nearest integer. 

**Syntax** |  **Description**  
---|---  
out = round(x);  |  Rounds x to the nearest integer.   
  
**Example**

Example output from round function. 
    
    
    ?x=[1.49,-1.49,1.5,1.55,-1.55];
    ?round(x);
    result: 
    1.49  -1.49  1.5  1.55  -1.55  
    result: 
    1  -1  2  2  -2   

This example shows how to use round to help implement the mod function. 
    
    
    mod_dividend= 10;
    mod_divisor = 3;
    mod_temp1=mod_dividend/mod_divisor;
    mod_temp2=round(mod_temp1);
    if (mod_temp1 >= mod_temp2) {
     mod_remainder= round( (mod_temp1 - mod_temp2)*mod_divisor );
    } else {
     mod_remainder= round( (1+mod_temp1 - mod_temp2)*mod_divisor );
    } 
    ?mod_remainder;
    result: 
    1      

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ floor ](/hc/en-us/articles/360034926353-floor) , [ ceil ](/hc/en-us/articles/360034406174-ceil) , [ mod ](/hc/en-us/articles/360034926373-mod)
