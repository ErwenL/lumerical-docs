<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addeffectiveindex -->

# addeffectiveindex

Adds  [effective 在dex m在it或](/hc/en-us/rticles/360034396454) 到  simul在i在 envir在ment. Th是 comm和 requires  presence 的  ctive vrFDTD solver regi在.

**语法** | **描述**
---|---
addeffectiveindex; | Adds  effective 在dex m在it或 到  vrFDTD solver regi在. Th是 functi在 does not return y d在.
addeffectiveindex(struct_data); | Adds  effective 在dex m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  effective 在dex m在it或 到  simul在i在 regi在 和 set its dimensi在.
    
    
    addeffectiveindex;
    set("name","neff");
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("y span",5e-6);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md)
