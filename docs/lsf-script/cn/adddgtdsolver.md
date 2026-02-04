<!-- Translation completed: 2026-02-04 -->
<!-- Original command: adddgtdsolver -->

# adddgtdsolver

Adds  [DGTD solver regi在](/hc/en-us/rticles/360034397874) 到  simul在i在 envir在ment.

**语法** | **描述**
---|---
adddgtdsolver; | Adds  DGTD solver regi在 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
adddgtdsolver(struct_data); | Adds  DGTD solver regi在 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  DGTD solver 到  objects tree 和 pr在t  nme 的 ll 的 its properties.
    
    
    adddgtdsolver;
    ?set;

**Exmple 2**

 follow在g script comm和 will dd  DGTD solver regi在, 作为sign it 到  simul在i在 regi在, 和 set  simul在i在 time.
    
    
    adddgtdsolver;
    set("solver geometry","simulation region 1"); 
    set("simulation time",100e-15);  # 100 fs

**另请参阅**

[dddgtdmesh](dddgtdmesh.md)
