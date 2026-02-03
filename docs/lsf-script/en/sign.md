# sign

Returns the sign of a number. 

**Syntax** |  **Description**  
---|---  
out = sign(data);  |  If data is real:  sign = 0 for data=0  sign = 1 for data>0  sign =-1 for data<0  If data is complex:  sign = 0 for data=0+0i  sign = data/abs(data) for data different from zero   
  
**Example**

Example output from sign function. 
    
    
    # real numbers
    data = [2; 0; -2];
    ?sign(data);
    # complex numbers
    data = [2+2i; 0+0i; -2+0i];
    ?sign(data);
    ?abs( sign(data) ); 
    result: 
    1  
    0  
    -1  
    result: 
    0.707107+0.707107i  
    0+0i  
    -1+0i  
    result: 
    1  
    0  
    1   

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ floor ](/hc/en-us/articles/360034926353-floor) , [ ceil ](/hc/en-us/articles/360034406174-ceil)
