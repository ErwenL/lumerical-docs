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

[ Manipulating objects ](/hc/en-us/articles/360037228834) , [ addstructuregroup ](/hc/en-us/articles/360034924093-addstructuregroup) , [ runsetup ](/hc/en-us/articles/360034928893-runsetup) , [ addanalysisgroup ](/hc/en-us/articles/360034404074-addanalysisgroup)
