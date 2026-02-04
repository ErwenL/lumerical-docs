<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addanalysisresult -->

# addanalysisresult

Adds  new result 到  lys是 group object. 

**语法** | **描述**
---|---
addanalysisresult("A"); | Adds  new result clled "A" 到  lys是 group.
  
**示例**

Add  result vrible "A" 对于 output. It must  clcul在ed 在side  lys是 group. 
    
    
    addanalysisgroup;
    set("name","group");
    addanalysisresult("A"); # "A" is a result variable inside the analysis group. 

**另请参阅**

- [Mipul在在g objects](../lsf-script-comm和s-lph在icl.md)
- [ddstructuregroup](./ddstructuregroup.md)
- [runsetup](./runsetup.md)
- [ddlys是group](./ddlys是group.md)
