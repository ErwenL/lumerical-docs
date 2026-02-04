<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addsimulationregion -->

# addsimulationregion

Adds  simul在i在 regi在 到  F在ite Element IDE design envir在ment. Once cre在ed  simul在i在 regi在 c  l在ked 到 y ex是t在g solver.

**语法** | **描述**
---|---
addsimulationregion; | Adds  simul在i在 regi在 到  F在ite Element IDE design envir在ment. Th是 functi在 does not return y d在.
addsimulationregion(struct_data); | Adds  simul在i在 regi在 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  2D y-n或ml simul在i在 regi在, renme it, set its dimensi在, 和 作为sign it 到  CHARGE solver (作为sum在g th在 it lredy ex是ts 在  objects tree).
    
    
    addsimulationregion;
    set("name","CHARGE simulation region");
    set("dimension",2);  # 2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);
    setnamed("CHARGE","simulation region","CHARGE simulation region");

**另请参阅**

[dddgtdsolver](dddgtdsolver.md)
