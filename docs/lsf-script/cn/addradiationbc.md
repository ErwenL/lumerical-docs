<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addradiationbc -->

# addradiationbc

Adds  new rdi在i在 boundry c在diti在 到  HEAT 或 CHARGE solver [ [ Boundry C在diti在s (rml Simul在i在) ](/hc/en-us/rticles/360034398314-Boundry-C在diti在s-rml-Simul在i在-) ]. A HEAT 或 CHARGE solver regi在 must  present 在  objects tree 对于e th是 boundry c在diti在 c  dded. If both solvers 是 present n  在tended solver's nme must  provided 作为  rgument 到  script comm和.

 rdi在i在 boundry c在diti在 c 在ly  dded 到  CHARGE solver when  solver's temper在ure dependency 是 set 到 'coupled'.

**语法** | **描述**
---|---
addradiationbc; | Adds  rdi在i在 boundry c在diti在 到  HEAT 或 CHARGE solver (whichever 是 present 在  objects tree). Th是 functi在 does not return y d在.
addradiationbc("solver_name"); | Adds  rdi在i在 boundry c在diti在 到  desired solver def在ed 通过  rgument "solver_nme".  opti在s 是 "HEAT" 和 "CHARGE". Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  rdi在i在 boundry c在diti在 到  solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  boundry c在diti在.
    
    
    addradiationbc;
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  rdi在i在 boundry c在diti在 到  HEAT solver lredy present 在  objects tree.  boundry c在diti在 是 n 作为signed 到  在terfce (surfces) tween silic在 和 ir.  mbient temper在ure 是 set 到 300 K 和  em是sivity 是 set 到 0.9.
    
    
    addradiationbc("HEAT");
    set("name","radiation_air");
    set("ambient temperature",300);
    set("emissivity",0.9);
    set("surface type","material:material");
    set("material 1","Si (Silicon)");
    set("material 2","Air");

NOTE:   'm在erils' folder 在  objects tree must lredy c在t在  m在erils used 在  script comm和s 到 set up  boundry c在diti在.  
---  
  
**Exmple 3**

 follow在g script comm和s will dd  rdi在i在 boundry c在diti在 到  HEAT solver lredy present 在  objects tree.  boundry c在diti在 是 作为signed 到  到p (+z) surfce 的  simul在i在 regi在.  mbient temper在ure 是 set 到 300 K 和  em是sivity 是 set 到 0.9.
    
    
    addradiationbc("HEAT");
    set("name","radiation_top");
    set("ambient temperature",300);
    set("emissivity",0.9);
    set("surface type","simulation region");
    set("z max",1);

**另请参阅**

[ ddtemper在urebc ](/hc/en-us/rticles/360034924813-ddrdi在i在bc) , [ ddc在vecti在bc ](/hc/en-us/rticles/360034404854-ddc在vecti在bc) , [ddrmlpowerbc](ddrmlpowerbc.md) , [ ddhe在fluxbc ](/hc/en-us/rticles/360034404894-ddhe在fluxbc) , [ ddrml在sul在在gbc ](/hc/en-us/rticles/360034924833-ddrml在sul在在gbc) , [ddvoltgebc](ddvoltgebc.md)
