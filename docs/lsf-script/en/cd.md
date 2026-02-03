# cd

Changes the directory. The directory is where the file is saved by default. 

**Syntax** |  **Description**  
---|---  
cd;  |  Opens a window to browse to a directory.  This function does not return any data.   
cd("directory");  |  Changes the working directory to "directory". Whenever you open an fsp file or run a script file, it will set the working directory to the directory of the file opened.   
  
**Examples**

Moves to the subdirectory "data". 
    
    
    ?pwd;
    C:\demo
    path=pwd;
    cd(path+"\data");
    ?pwd;
    C:\demo\data

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ pwd ](/hc/en-us/articles/360034931773-pwd)
