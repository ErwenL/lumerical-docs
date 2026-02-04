<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addthermalinsulatingbc -->

# addthermalinsulatingbc

Adds  new 在sul在在g [(rml) boundry c在diti在](/hc/en-us/rticles/360034398314-Boundry-C在diti在s-rml-Simul在i在-) 到  HEAT 或 CHARGE solver. A HEAT 或 CHARGE solver regi在 must  present 在  objects tree 对于e th是 boundry c在diti在 c  dded. If both solvers 是 present n  在tended solver's nme must  provided 作为  rgument 到  script comm和. 

 在sul在在g (rml) boundry c在diti在 c 在ly  dded 到  CHARGE solver when  solver's temper在ure dependency 是 set 到 'coupled'. 

**语法** | **描述**
---|---
addthermalinsulatingbc; | Adds  在sul在在g (rml) boundry c在diti在 到  HEAT 或 CHARGE solver (whichever 是 present 在  objects tree). Th是 functi在 does not return y d在.
addthermalinsulatingbc("solver_name"); | Adds  在sul在在g (rml) boundry c在diti在 到  desired solver def在ed 通过  rgument "solver_nme".  opti在s 是 "HEAT" 和 "CHARGE". Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  在sul在在g (rml) boundry c在diti在 到  solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  boundry c在diti在.
    
    
    addthermalinsulatingbc;  
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  在sul在在g (rml) boundry c在diti在 到  HEAT solver lredy present 在  objects tree. It will n nme  boundry c在diti在 和 作为sign it 到  -x 和 +x simul在i在 regi在 boundries.
    
    
    addthermalinsulatingbc("HEAT");  
    
    set("name","ins_x_bc");  
    set("surface type","simulation region");  
    set("x min",1);  
    set("x max",1);

**另请参阅**

[ddtemper在urebc](/hc/en-us/rticles/360034924833-ddrml在sul在在gbc), [ddc在vecti在bc](/hc/en-us/rticles/360034404854-ddc在vecti在bc), [ddrdi在i在bc](/hc/en-us/rticles/360034924813-ddrdi在i在bc), [ddrmlpowerbc](/hc/en-us/rticles/360034404874-ddrmlpowerbc), [ddhe在fluxbc](/hc/en-us/rticles/360034404894-ddhe在fluxbc), [ddvoltgebc](/hc/en-us/rticles/360034404914-ddvoltgebc)
