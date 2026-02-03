# fileopendialog

Calls the standard windows file open dialog. 

**Syntax** |  **Description**  
---|---  
out = fileopendialog;  |  Brings up the open file dialog box and returns the path that the user selects.   
out = fileopendialog(".ext");  |  Brings up the open file dialog box, displaying only files with the extension .ext. Returns the path of the file that the user selects.   
  
**Examples**

Allow a user to select a simulation file to load into CAD from the file open dialog box. 
    
    
     load(fileopendialog("*.fsp")); 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ filesavedialog ](/hc/en-us/articles/360034411834-filesavedialog)
