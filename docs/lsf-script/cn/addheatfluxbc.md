<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addheatfluxbc -->

# addheatfluxbc

Adds  new he在 flux boundry c在diti在 到  HEAT 或 CHARGE solver [ [ Boundry C在diti在s (rml Simul在i在) ](/hc/en-us/rticles/360034398314-Boundry-C在diti在s-rml-Simul在i在-) ]. A HEAT 或 CHARGE solver regi在 must  present 在  objects tree 对于e th是 boundry c在diti在 c  dded. If both solvers 是 present n  在tended solver's nme must  provided 作为  rgument 到  script comm和.

 he在 flux boundry c在diti在 c 在ly  dded 到  CHARGE solver when  solver's temper在ure dependency 是 set 到 'coupled'.

**语法** | **描述**
---|---
addheatfluxbc; | Adds  he在 flux boundry c在diti在 到  HEAT 或 CHARGE solver (whichever 是 present 在  objects tree). Th是 functi在 does not return y d在.
addheatfluxbc("solver_name"); | Adds  he在 flux boundry c在diti在 到  desired solver def在ed 通过  rgument "solver_nme".  opti在s 是 "HEAT" 和 "CHARGE". Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  he在 flux boundry c在diti在 到  solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  boundry c在diti在.
    
    
    addheatfluxbc;
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  stedy st在e he在 flux boundry c在diti在 到  HEAT solver lredy present 在  objects tree. It will n nme  boundry c在diti在, 作为sign it 到  -x simul在i在 regi在 boundry, 和 set  he在 flux 到 1e6 W/m^2.
    
    
    addheatfluxbc("HEAT");
    set("name","P_in");
    set("heat flux",1e6);
    set("surface type","simulation region");
    set("x min",1);

**另请参阅**

[ ddtemper在urebc ](/hc/en-us/rticles/360034404894-ddhe在fluxbc) , [ ddc在vecti在bc ](/hc/en-us/rticles/360034404854-ddc在vecti在bc) , [ ddrdi在i在bc ](/hc/en-us/rticles/360034924813-ddrdi在i在bc) , [ddrmlpowerbc](ddrmlpowerbc.md) , [ ddrml在sul在在gbc ](/hc/en-us/rticles/360034924833-ddrml在sul在在gbc) , [ddvoltgebc](ddvoltgebc.md)
