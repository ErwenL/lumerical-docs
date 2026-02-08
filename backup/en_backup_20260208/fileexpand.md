# fileexpand

Expands a file name by replacing any environmental variables. 

**Syntax** |  **Description**  
---|---  
fileexpand(filename);  |  Expands a file name by replacing any environmental variables (defined by setsetting).   
  
###  Example 

Expand a filename containing the variable LOCAL 
    
    
    ?getsetting;
    LOCAL=C:\Users
    ?fileexpand("$LOCAL\data.txt");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ setsetting ](/hc/en-us/articles/360034927973-setsetting)
