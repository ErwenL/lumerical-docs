# newproject

Creates a new simulation project file. If there is an existing project file in the GUI, the old project file will not be saved. 

**Syntax** |  **Description**  
---|---  
newproject;  |  Creates a new layout environment.  This function does not return any data.   
  
**Examples**

Creates a new project with the newproject command. 
    
    
    newproject;

However, for FDTD and MODE, users can have more choices: 

For MODE, it can have numerical variables: 

**Syntax** |  **Description**  
---|---  
newproject(option);  |  The options are 

  1. use default file and material database as template 
  2. use current file and material database as template 
  3. open a file browser to select and existing file as a template 

The default option is 1.   
  
**Examples**

Creates a new project with the newproject command. 
    
    
    newproject; 
    newproject(2); # open a template using current file and material database

For FDTD, the variables can be either numerical, or string: 

**Syntax** |  **Description**  
---|---  
newproject(option);  |  The options can be number or string:  1 or 'default': use default file and material database as template  2 or 'RF': use default RF template  3 or 'current': use current file and material database as template  4 or 'existing': open a file browser to select and existing file as a template  The default option is 1. Since most material data in the Material Database is for optical frequencies, open a RF project will not modify the original material data in the material database.   
  
**Examples**

Creates a new project with the newproject command. 
    
    
    newproject; # open a template for optical frequency simulation 
    newproject('RF');# open a template for RF simulation 
    newproject(2); # open a template for RF simulation

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ new ](/hc/en-us/articles/360034931493-new) , [ exit ](/hc/en-us/articles/360034931613-exit)
