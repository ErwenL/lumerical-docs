# addanalysisgroup

Adds an [analysis group](/hc/en-us/articles/360034382454) to the simulation environment. Analysis groups are container objects that can contain any simulation object and associated script functions which can be used to create customize data analysis.

**Syntax** |  **Description**  
---|---  
addanalysisgroup; |  Adds an analysis group to the simulation environment. This function does not return any data.  
addanalysisgroup(struct_data); |  Adds an analysis group and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

Add an analysis group and put a time monitor in it.
    
    
    addanalysisgroup;
    set("name","group");
    addtime;
    addtogroup("group");

To learn more about how to use analysis groups go to this page: [ Using Analysis Groups ](/hc/en-us/articles/360034382454-Analysis-Groups) .

Note: To add a pre-defined analysis group from the object library, use the [ addobject ](/hc/en-us/articles/360034404094-addobject) command.  
---  
  
**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ addtogroup ](/hc/en-us/articles/360034408454-addtogroup) , [ adduserprop ](/hc/en-us/articles/360034928733-adduserprop) , [ runanalysis ](/hc/en-us/articles/360034409874-runanalysis) , [ getresult ](/hc/en-us/articles/360034409854-getresult) , [ addobject ](/hc/en-us/articles/360034404094-addobject)
