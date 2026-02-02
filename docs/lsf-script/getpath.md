# getpath

Gets the current path. By default, the current working directory and the script sub-directory of the installation directory are in the path. Typically the path is important for setting the location of your script files. 

**Syntax** |  **Description**  
---|---  
out = getpath; |  Returns the current path as a string. Use ?getpath; to print it to the screen.  
  
**Examples**

Gets the current path.
    
    
    ?getpath;
    ./  
    C:/Program Files/Lumerical/2020a/scripts

**See Also**

[addpath](/hc/en-us/articles/360034931833-addpath), [ clearpath](/hc/en-us/articles/360034931853-clearpath), [ which](/hc/en-us/articles/360034411094-which), [ pwd ](/hc/en-us/articles/360034931773-pwd)
