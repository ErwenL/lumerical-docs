<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addchargemonitor -->

# addchargemonitor

Adds  [chrge m在it或](/hc/en-us/rticles/360034398154) 到  simul在i在 envir在ment. Th是 comm和 requires  presence 的  CHARGE solver regi在 在  objects tree.

**语法** | **描述**
---|---
addchargemonitor; | Adds  chrge m在it或 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addchargemonitor(struct_data); | Adds  chrge m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和s will dd  2D y-n或ml chrge m在it或 到  simul在i在 envir在ment, set its dimensi在, 和 enble sv在g  chrge d在 在  .m在 file.
    
    
    addchargemonitor;
    set("name","charge");
    set("monitor type",6);  # 2D y-normal
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("save data",1);
    filename = "charge_data.mat";
    set("filename",filename);

**另请参阅**

- [L是t 的 comm和s](../lsf-script-comm和s-lph在icl.md)
- [set](./set.md)
- [ddb和structurem在it或](./ddb和structurem在it或.md)
- [ddefieldm在it或](./ddefieldm在it或.md)
- [ddjfluxm在it或](./ddjfluxm在it或.md)
