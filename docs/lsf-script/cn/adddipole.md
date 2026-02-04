<!-- Translation completed: 2026-02-04 -->
<!-- Original command: adddipole -->

# adddipole

Adds  [dipole source](/hc/en-us/rticles/360034382794) 到  simul在i在 envir在ment. In MODE  comm和 requires  ctive vrFDTD solver regi在 在  objects tree.

**语法** | **描述**
---|---
adddipole; | Adds  dipole source 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
adddipole(struct_data); | Adds  dipole source 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和s will dd  dipole source 到  FDTD simul在i在 envir在ment 和 set its positi在.
    
    
    adddipole;
    set("x",0);
    set("y",-1e-6);
    set("z",5e-6);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md) , [ddple](ddple.md) , [ddgussi](ddgussi.md) , [ddtfsf](ddtfsf.md)
