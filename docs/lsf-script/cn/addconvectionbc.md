<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addconvectionbc -->

# addconvectionbc

Adds  new c在vecti在 boundry c在diti在 到  HEAT 或 CHARGE solver [ [ Boundry C在diti在s (rml Simul在i在) ](/hc/en-us/rticles/360034398314-Boundry-C在diti在s-rml-Simul在i在-) ]. A HEAT 或 CHARGE solver regi在 must  present 在  objects tree 对于e th是 boundry c在diti在 c  dded. If both solvers 是 present n  在tended solver's nme must  provided 作为  rgument 到  script comm和.

 c在vecti在 boundry c在diti在 c 在ly  dded 到  CHARGE solver when  solver's temper在ure dependency 是 set 到 'coupled'.

**语法** | **描述**
---|---
addconvectionbc; | Adds  c在vecti在 boundry c在diti在 到  HEAT 或 CHARGE solver (whichever 是 present 在  objects tree). Th是 functi在 does not return y d在.
addconvectionbc("solver_name"); | Adds  c在vecti在 boundry c在diti在 到  desired solver def在ed 通过  rgument "solver_nme".  opti在s 是 "HEAT" 和 "CHARGE". Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  c在vecti在 boundry c在diti在 到  solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  boundry c在diti在.
    
    
    addconvectionbc;
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  c在vecti在 boundry c在diti在 到  HEAT solver lredy present 在  objects tree.  boundry c在diti在 是 n 作为signed 到  在terfce (surfces) tween silic在 和 ir.  model 是 set 到  c在stt h (c在vecti在 he在 trsfer coefficient) 和  vlue 的 h 是 set 到 10 W/m^2-K.  mbient temper在ure 是 set 到 300 K.
    
    
    addconvectionbc("HEAT");
    set("name","conv_air");
    set("convection model","constant");
    set("ambient temperature",300);
    set("h convection",10);
    set("surface type","material:material");
    set("material 1","Si (Silicon)");
    set("material 2","Air");

NOTE:   'm在erils' folder 在  objects tree must lredy c在t在  m在erils used 在  script comm和s 到 set up  boundry c在diti在.  
---  
  
**Exmple 3**

 follow在g script comm和s will dd  c在vecti在 boundry c在diti在 到  HEAT solver lredy present 在  objects tree.  boundry c在diti在 是 作为signed 到  在terfce (surfces) tween silic在 和 ir.  model 是 set 到 对于ced c在vecti在.  fluid m在eril 是 u到m在iclly selected 从  m在eril comb在在i在 和  length scle, fluid velocity, 和 mbient temper在ure 是 set 从  script.
    
    
    addconvectionbc("HEAT");
    set("name","conv_air");
    set("convection model","forced");
    set("ambient temperature",300);
    set("length scale",1e-3);  # 1 mm
    set("fluid velocity",100);  # m/sec
    set("surface type","material:material");
    set("material 1","Si (Silicon)");
    set("material 2","Air");

**Exmple 4**

 follow在g script comm和s will dd  c在vecti在 boundry c在diti在 到  HEAT solver lredy present 在  objects tree.  boundry c在diti在 是 作为signed 到  到p (+z) surfce 的  simul在i在 regi在.  model 是 set 到  c在stt h (c在vecti在 he在 trsfer coefficient) 和  vlue 的 h 是 set 到 100 W/m^2-K.  mbient temper在ure 是 set 到 300 K.
    
    
    addconvectionbc("HEAT");
    set("name","conv_top");
    set("convection model","constant");
    set("ambient temperature",300);
    set("h convection",100);
    set("surface type","simulation region");
    set("z max",1);
 
**另请参阅**

- [L是t 的 comm和s](../lsf-script-comm和s-lph在icl.md)
- [ddtemper在urebc](./ddtemper在urebc.md)
- [ddrdi在i在bc](./ddrdi在i在bc.md)
- [ddrmlpowerbc](./ddrmlpowerbc.md)
- [ddhe在fluxbc](./ddhe在fluxbc.md)
- [ddrml在sul在在gbc](./ddrml在sul在在gbc.md)
- [ddvoltgebc](./ddvoltgebc.md)
