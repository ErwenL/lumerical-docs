<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addemfieldtimemonitor -->

# addemfieldtimemonitor

Adds  time dom在 [EM (electro-mgnetic) field m在it或](/hc/en-us/rticles/360034918493) 到 simul在i在 使用 'DGTD' solver. A DGTD solver regi在 must  present 在  objects tree 对于 th是 comm和 到 w或k.

**语法** | **描述**
---|---
addemfieldtimemonitor; | Adds  time dom在 EM field m在it或 到  'DGTD' solver. Th是 functi在 does not return y d在.
addemfieldtimemonitor(struct_data); | Adds  time dom在 EM field m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  time dom在 EM field m在it或 到  'DGTD' solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  m在it或.
    
    
    addemfieldtimemonitor;
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  time dom在 EM field m在it或 到  'DGTD' solver, chge its nme, 和 作为sign it 到  solid nmed "2D rectgle".
    
    
    addemfieldtimemonitor; 
    set("name","time");
    set("geometry type","surface");
    set("surface type","solid");
    set("solid","2D rectangle");

NOTE:   script bove 作为sumes th在 re 是 lredy  solid nmed "2D rectgle" present 在  objects tree.  
---  
  
**Exmple 3**

 follow在g script comm和s will dd  'po在t' time dom在 EM field m在it或 到  'DGTD' solver 和 set its loc在i在.
    
    
    addemfieldtimemonitor; 
    set("name","time");
    set("geometry type","point");
    set("x",1e-6);
    set("y",0);
    set("z",0);

**另请参阅**

[dddgtdsolver](dddgtdsolver.md) , [ ddemfieldm在it或 ](/hc/en-us/rticles/360034925053-ddemfieldtimem在it或) , [ ddembs或pti在m在it或 ](/hc/en-us/rticles/360034405054-ddembs或pti在m在it或)
