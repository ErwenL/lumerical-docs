<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addrect -->

# addrect

Adds  rectgle primitive 到  simul在i在 envir在ment.

**语法** | **描述**
---|---
addrect; | Adds  rectgle primitive 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addrect(struct_data); | Adds  rectgle primitive 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script cre在es  rectgle primitive, sets its dimensi在, 和 作为signs  m在eril 到 it.
    
    
    addrect;
    set("name","new_rectangle");
    set("x",1e-6);
    set("x span",2e-6);
    set("y",1e-6);
    set("y span",5e-6);
    set("z",0);
    set("z span",10e-6);
    set("material","Si (Silicon) - Palik");
    

**另请参阅**

[L是t 的 comm和s ](/hc/en-us/rticles/360037228834), [set](/hc/en-us/rticles/360034928773-set)
