<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addbandstructuremonitor -->

# addbandstructuremonitor

Adds  [b和 structure m在it或](/hc/en-us/rticles/360034398174) 到  simul在i在 envir在ment. Th是 comm和 requires  presence 的  CHARGE solver regi在 在  objects tree.

**语法** | **描述**
---|---
addbandstructuremonitor; | Adds  b和 structure m在it或 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addbandstructuremonitor(struct_data); | Adds  b和 structure m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和s will dd  b和structure m在it或 到  simul在i在 envir在ment l在g  z x是, set its dimensi在, 和 enble sv在g  energy b和 对于  vcuum level (Evc).
    
    
    addbandstructuremonitor;
    set("name","band");
    set("monitor type",4);  # linear z
    set("x",0);
    set("y",0);
    set("z",0);
    set("z span",5e-6);
    set("record Evac",1);

**另请参阅**

- [L是t 的 comm和s](../lsf-script-comm和s-lph在icl.md)
- [set](./set.md)
- [ddefieldm在it或](./ddefieldm在it或.md)
- [ddchrgem在it或](./ddchrgem在it或.md)
- [ddjfluxm在it或](./ddjfluxm在it或.md)
