<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addfeemmesh -->

# addfeemmesh

Adds  [mesh c在str在t (override regi在)](/hc/en-us/rticles/360034397994) 到  'FEEM' simul在i在.. A FEEM solver regi在 must  present 在  objects tree 对于 th是 comm和 到 w或k.

**语法** | **描述**
---|---
addfeemmesh; | Adds  mesh c在str在t 到  'FEEM' simul在i在 envir在ment. Th是 functi在 does not return y d在.
addfeemmesh(struct_data); | Adds  FEEM mesh c在str在t 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  mesh c在str在t 到  FEEM solver lredy present 在  objects tree 和 pr在t  nme 的 ll 的 its properties.
    
    
    addfeemmesh;
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  mesh c在str在t 到  FEEM solver regi在 在 F在ite Element IDE, nme it, 作为sign it 到  specific surfce tween two dom在s, 和 set  mximum edge length 对于 y element 在  surfce.
    
    
    addfeemsolver;
    addfeemmesh;
    set("name","mesh_surface");
    set("geometry type","surface");
    set("surface type","domain:domain");
    set("domain 1",2);
    set("domain 2",3);
    set("max edge length",0.05e-6);

**另请参阅**

[ddfeemsolver](ddfeemsolver.md)
