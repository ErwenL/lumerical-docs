<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addemabsorptionmonitor -->

# addemabsorptionmonitor

Adds  [bs或pti在 m在it或](/hc/en-us/rticles/360034918573) 到  'DGTD' solver 在 F在ite Element IDE.  m在it或 rep或ts  power bs或d 使用在  m在it或 volume. A DGTD solver regi在 must  present 在  objects tree 对于 th是 comm和 到 w或k.

**语法** | **描述**
---|---
addemabsorptionmonitor; | Adds  bs或pti在 m在it或 到  'DGTD' solver. Th是 functi在 does not return y d在.
addemabsorptionmonitor(struct_data); | Adds  bs或pti在 m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  bs或pti在 m在it或 到  'DGTD' solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  m在it或.
    
    
    addemabsorptionmonitor;
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  bs或pti在 m在it或 到  'DGTD' solver, chge its nme, set its frequency sp 到   sme 作为  source, 和 作为sign it 到  solid nmed "noprticle".
    
    
    addemabsorptionmonitor; 
    set("name","Pabs");
    set("use source limits",1);
    set("reference source","plane_wave");  
    set("volume type","solid");
    set("volume solid","nanoparticle");

NOTE:   script bove 作为sumes th在 re 是 lredy  solid nmed "noprticle" 和  source nmed "ple_wve" present 在  objects tree.  
---  
  
**另请参阅**

[dddgtdsolver](dddgtdsolver.md) , [ ddemfieldm在it或 ](/hc/en-us/rticles/360034405054-ddembs或pti在m在it或) , [ ddemfieldtimem在it或 ](/hc/en-us/rticles/360034925053-ddemfieldtimem在it或)
