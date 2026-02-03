# load

Loads a simulation project file. If the simulation has been run, the file will also contain the simulation results. 

**Syntax** |  **Description**  
---|---  
load(filename);  |  Loads the simulation file.  This function does not return any data.   
  
**Examples**

Loads a simulation project file. 
    
    
    filename="simulation.fsp";
    load(filename); # load the file in the current working directory
    load("C:\Downloads\project_name.fsp") # load the file in a path specified

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ loaddata ](/hc/en-us/articles/360034411214-loaddata) , [ save ](/hc/en-us/articles/360034410814-save) , [ savedata ](/hc/en-us/articles/360034411174-savedata) , [ savedcard ](/hc/en-us/articles/360034411154-savedcard) , [ fileexists ](/hc/en-us/articles/360034931633-fileexists) , [ dir ](/hc/en-us/articles/360034410854-dir)
