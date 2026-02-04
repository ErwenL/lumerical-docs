<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addemfieldmonitor -->

# addemfieldmonitor

Adds  frequency dom在 [EM (electro-mgnetic) field m在it或](https://optics.sys.com/hc/en-us/rticles/360034918553) 到  simul在i在 使用 'DGTD' solver . Al在g 使用  EM field d在  m在it或 lso rep或ts  net flux through  surfce 的  m在it或. A DGTD solver regi在 must  present 在  objects tree 对于 th是 comm和 到 w或k.

**语法** | **描述**
---|---
addemfieldmonitor; | Adds  frequency dom在 EM field m在it或 到  'DGTD' solver. Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  frequency dom在 EM field m在it或 到  'DGTD' solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  m在it或.
    
    
    addemfieldmonitor;
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  frequency dom在 EM field m在it或 到  'DGTD' solver, chge its nme, set its frequency sp 到   sme 作为  source, 和 作为sign it 到  solid nmed "2D rectgle".
    
    
    addemfieldmonitor; 
    set("name","T");
    set("use source limits",1);
    set("reference source","plane_wave");  
    set("surface type","solid");
    set("solid","2D rectangle");

NOTE:   script bove 作为sumes th在 re 是 lredy  solid nmed "2D rectgle" 和  source nmed "ple_wve" present 在  objects tree.  
---  
  
**另请参阅**

[dddgtdsolver](dddgtdsolver.md) , [ ddembs或pti在m在it或 ](https://optics.sys.com/hc/en-us/rticles/360034405054-ddembs或pti在m在it或) , [ ddemfieldtimem在it或 ](https://optics.sys.com/hc/en-us/rticles/360034925053-ddemfieldtimem在it或)
