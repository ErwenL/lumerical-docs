# which

Returns the full file pathname for the specified file. 

This function can be helpful when you have added several directories to the Lumerical path variable and you want to check which files are being accessed. 

**Syntax** |  **Description**  
---|---  
out = which("filename");  |  Returns the pathname of the file "filename" as a string.  Use ?which("filename"); to display the result to the screen.   
  
**Examples**

Gets the full path and filename of the file results.txt. 
    
    
    file = "results.txt";    # set file name
    write(file,"my data file"); # create file
    ?fullPath = which(file);   # get full name and path
     C:/Program Files/Lumerical/FDTD/scripts/results.txt

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getpath ](/hc/en-us/articles/360034411054-getpath) , [ addpath ](/hc/en-us/articles/360034931833-addpath) , [ pwd ](/hc/en-us/articles/360034931773-pwd) , [ currentfilename ](/hc/en-us/articles/360034931793-currentfilename) , [ fileexists ](/hc/en-us/articles/360034931633-fileexists)
