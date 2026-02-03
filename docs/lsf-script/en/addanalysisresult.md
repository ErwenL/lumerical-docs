# addanalysisresult

Adds a new result to an analysis group object. 

**Syntax** |  **Description**  
---|---  
addanalysisresult("A");  |  Adds a new result called "A" to an analysis group.   
  
**Example**

Add a result variable "A" for output. It must be calculated inside the analysis group. 
    
    
    addanalysisgroup;
    set("name","group");
    addanalysisresult("A"); # "A" is a result variable inside the analysis group. 

**See Also**

- [Manipulating objects](../lsf-script-commands-alphabetical.md)
- [addstructuregroup](./addstructuregroup.md)
- [runsetup](./runsetup.md)
- [addanalysisgroup](./addanalysisgroup.md)
