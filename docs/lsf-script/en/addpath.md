# addpath

Adds a directory to the path.

This can be helpful when your script and simulation files are located in different directories. Your current working directory will typically be set to the location of your simulation files. addpath can be used to add the location of your script files to the path, which makes it possible to call those scripts without providing the full path each time. 

**Syntax** |  **Description**  
---|---  
addpath("directory"); |  Adds a directory to the path. This function does not return any data.  
  
**Examples**

Adds a second directory to the path.
    
    
    ?getpath;
    ./  
    C:/Program Files/Lumerical/2020a/scripts
    addpath("C:/demo");
    ?getpath;
    ./  
    C:/Program Files/Lumerical/2020a/scripts  
    C:/demo

Clears the path.
    
    
    clearpath;
    ?getpath;
    ./

**See Also**

[ getpath](/hc/en-us/articles/360034411054-getpath), [ which](/hc/en-us/articles/360034411094-which), [ pwd](/hc/en-us/articles/360034931773-pwd), [ clearpath ](/hc/en-us/articles/360034931853-clearpath)
