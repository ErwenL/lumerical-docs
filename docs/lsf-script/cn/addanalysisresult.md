<!--
Translation from English documentation
Original command: addanalysisresult
Translation date: 2026-02-04 22:46:39
-->

# addanalysisresult

添加 a new result to an analysis group 对象. 

**语法** |  **描述**  
---|---  
addanalysisresult("A");  |  添加 a new result called "A" to an analysis group.   
  
**示例**

添加 a result variable "A" for output. It must be calculated inside the analysis group. 
    
    
    addanalysisgroup;
    设置("name","group");
    addanalysisresult("A"); # "A" is a result variable inside the analysis group. 

**参见**

- [Manipulating 对象](../lsf-脚本-commands-alphabetical.md)
- [addstructuregroup](./addstructuregroup.md)
- [runsetup](./runsetup.md)
- [addanalysisgroup](./addanalysisgroup.md)
