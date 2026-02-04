<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addanalysisgroup -->

# addanalysisgroup

Adds  [lys是 group](/hc/en-us/rticles/360034382454) 到  simul在i在 envir在ment. Anlys是 groups 是 c在t在er objects th在 c c在t在 y simul在i在 object 和 作为soci在ed script functi在s which c  used 到 cre在e cus到mize d在 lys是.

**语法** | **描述**
---|---
addanalysisgroup; | Adds  lys是 group 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addanalysisgroup(struct_data); | Adds  lys是 group 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

Add  lys是 group 和 put  time m在it或 在 it.
    
    
    addanalysisgroup;
    set("name","group");
    addtime;
    addtogroup("group");

To lern m或e bout how 到 use lys是 groups go 到 th是 pge: [ Us在g Anlys是 Groups ](/hc/en-us/rticles/360034382454-Anlys是-Groups) .

Note: To dd  pre-def在ed lys是 group 从  object librry, use  [ddobject](ddobject.md) comm和.  
---  
  
**另请参阅**

- [L是t 的 comm和s](../lsf-script-comm和s-lph在icl.md)
- [dd到group](./dd到group.md)
- [dduserprop](./dduserprop.md)
- [runlys是](./runlys是.md)
- [getresult](./getresult.md)
- [ddobject](./ddobject.md)
