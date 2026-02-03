# #

Comments script files. Anything after the # character is ignored. 

**Syntax** |  **Description**  
---|---  
x=1; # set x to 1  |  Anything after the # character is ignored.   
  
**Examples**

Add comments to a script file 
    
    
    ################################################
    # this section will calculate power transmission
    T=transmission("Monitor3"); # store transmission in T 

Multi-line comment: To create a multi-line comment, use an if statement as shown below. 
    
    
    if (0) { # if 0, skip these lines. if 1, run these lines. 
    a=1;
    b=2;
    c=a+b;
    }

It is possible to create strings that contain a # symbol. Simply create the string in the usual way, no special actions or escape characters are required. The only confusing point is that the automatic text coloring scheme will change all text beyond the # symbol green. This may look slightly confusing, but it will not cause any errors. 
    
    
    ?"this string contains a # symbol";

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834)
