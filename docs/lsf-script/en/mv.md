# mv

Moves a file to a new location. Path can be specified.

**Syntax** |  **Description**  
---|---  
mv("file1","file2"); |  Moves file1 to file2. This function does not return any data.  
mv("path1\file1","path2\file2"); |  Moves file1 in path1 to file2 in path2.  
  
**Note** : This command cannot be used while in [safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**Examples**

Moves "myscript.lsf" to c:\working and renames it "temp.lsf".
    
    
    mv("c:\myscript.lsf","c:\working\temp.lsf");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ cp ](/hc/en-us/articles/360034931573-cp) , [ pwd ](/hc/en-us/articles/360034931773-pwd)
