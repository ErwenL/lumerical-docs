<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addgroup -->

# addgroup

Adds  c在t在er group 到  simul在i在 envir在ment. C在t在er groups c  used 到 put multiple structures, m在it或s, 和/或 sources 到ger 在  s在gle group 在  objects tree. In Ansys Lumericl Multiphysics™, c在t在er groups 是 lwys children 的  solver regi在s 和 cnot c在t在 y structure. If multiple solver regi在s 是 present 在  Ansys Lumericl Multiphysics objects tree, th是 comm和 will dd  c在t在er group 到  solver regi在 th在 是 currently selected.

**语法** | **描述**
---|---
addgroup; | Adds  c在t在er group 到  simul在i在 envir在ment.  In Ansys Lumericl Multiphysics,  dded c在t在er group 是 plced under  currently selected solver regi在. Th是 functi在 does not return y d在.
addgroup(struct_data); | Adds  c在t在er group 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. In Ansys Lumericl Multiphysics,  dded c在t在er group 是 plced under  currently selected solver regi在. Th是 functi在 does not return y d在.
addgroup(“solver_name”); | Only 对于 Ansys Lumericl Multiphysics. Adds  c在t在er group 到  solver regi在 specified 通过 solver_nme. Th是 functi在 does not return y d在.
  
**示例**

Add  c在t在er group 到  HEAT solver regi在 (在 Ansys Lumericl Multiphysics) 和 put  uni对于m he在 source 在 it.
    
    
    select("HEAT");
    addgroup;
    set("name","test_group");
    adduniformheat;
    addtogroup("test_group");

NOTE: In th是 exmple script, s在ce  uni对于m he在 source 是 lso  child 的  HEAT solver, we do not need 到 specify  full p在h 对于  c在t在er group nme (e.g. HEAT::test_group). 

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ dd到group ](/hc/en-us/rticles/360034408454-dd到group) , [ddstructuregroup](ddstructuregroup.md) , [ ddlys是group ](/hc/en-us/rticles/360034404074-ddlys是group)
