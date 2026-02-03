# layoutmode

This script command can be used to determine whether the simulation file is currently in LAYOUT mode or in ANALYSIS mode. It is important to use this command to check the status of the project file once it is opened to avoid running into an error during the subsequent operations if the file is not in the desired mode. 

**Syntax** |  **Description**  
---|---  
?layoutmode;  |  Returns 1 if in LAYOUT mode (DESIGN mode for INTERCONNECT), and 0 if in ANALYSIS mode.   
  
**Example**

The following script commands will first load a project file named "test.fsp". The aim of the script is to add a new rectangle to the existing geometry. However, if the file is in ANALYSIS mode then the "addrect" command will create an error. To avoid this, the script command "layoutmode" is first used to determine the status of the file. Then an "if/else" statement is used to add the rectangle directly if the file is already in LAYOUT mode or to add the rectangle after switching to LAYOUT mode first if the file is in ANALYSIS mode. 
    
    
    load("test.fsp");  
    status = layoutmode;  
    
    if (status == 1) {  
        addrect;  
    }  
    else {  
        switchtolayout;  
        addrect;  
    }

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ switchtolayout ](/hc/en-us/articles/360034923993-switchtolayout) , [ designmode ](/hc/en-us/articles/360034924053-designmode)
