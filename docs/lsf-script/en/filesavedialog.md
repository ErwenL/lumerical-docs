# filesavedialog

Calls the standard windows file save dialog. 

**Syntax** |  **Description**  
---|---  
out = filesavedialog;  |  Brings up the save file dialog box and returns the path that the user selects.   
out = filesavedialog(".ext");  |  Brings up the save file dialog box, displaying only files with the extension .ext. Returns the path of the file that the user selects.   
  
**Examples**

Save the current simulation to a path chosen by the user. 
    
    
     save(filesavedialog("*.fsp")); 

###  **See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ fileopendialog ](/hc/en-us/articles/360034932433-fileopendialog)
