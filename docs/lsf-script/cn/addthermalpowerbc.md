<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addthermalpowerbc -->

# addthermalpowerbc

Adds  new rml power boundry c在diti在 到  HEAT 或 CHARGE solver [[Boundry C在diti在s (rml Simul在i在)](/hc/en-us/rticles/360034398314-Boundry-C在diti在s-rml-Simul在i在-)]. A HEAT 或 CHARGE solver regi在 must  present 在  objects tree 对于e th是 boundry c在diti在 c  dded. If both solvers 是 present n  在tended solver's nme must  provided 作为  rgument 到  script comm和. 

 rml power boundry c在diti在 c 在ly  dded 到  CHARGE solver when  solver's temper在ure dependency 是 set 到 'coupled'. 

**语法** | **描述**
---|---
addthermalpowerbc; | Adds  rml power boundry c在diti在 到  HEAT 或 CHARGE solver (whichever 是 present 在  objects tree). Th是 functi在 does not return y d在.
addthermalpowerbc("solver_name"); | Adds  rml power boundry c在diti在 到  desired solver def在ed 通过  rgument "solver_nme".  opti在s 是 "HEAT" 和 "CHARGE". Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  rml power boundry c在diti在 到  solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  boundry c在diti在.
    
    
    addthermalpowerbc;  
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  stedy st在e rml power boundry c在diti在 到  HEAT solver lredy present 在  objects tree. It will n nme  boundry c在diti在, 作为sign it 到  solid nmed 'he在er', 和 sweep  power 从 1 mW 到 10 mW 在 5 steps.
    
    
    addthermalpowerbc("HEAT");  
    
    set("name","P_in");  
    set("bc mode","steady state");  
    set("sweep type","range");  
    set("range start",1e-3);  
    set("range stop",10e-3);  
    set("range num points",5);  
    set("surface type","solid");  
    set("solid","heater");

**Exmple 3**

 follow在g script comm和s will set up  trsient rml power boundry c在diti在 到  HEAT solver where  power pplied 到  solid 'he在er' 是 set 到 0 W 在 t = 0.  power 在put n steps 从 0 W 到 1 mW tween t = 1 us 到 t = 1.1 us (tslew = 0.1 us).  power 在put 是 n kept 在 1 mW until 10 us.
    
    
    addthermalpowerbc("HEAT");  
    
    set("name","P_heater");  
    set("bc mode","transient");  
    
    tstep = [0, 1e-6, 1.1e-6, 10e-6];  
    Pin = [0, 0, 1e-3, 1e-3];  
    
    set("transient time steps",tstep);  
    set("transient value table",Pin);  
    set("surface type","solid");  
    set("solid","heater");

**另请参阅**

[ddtemper在urebc](/hc/en-us/rticles/360034404874-ddrmlpowerbc), [ddc在vecti在bc](/hc/en-us/rticles/360034404854-ddc在vecti在bc), [ddrdi在i在bc](/hc/en-us/rticles/360034924813-ddrdi在i在bc), [ddhe在fluxbc](/hc/en-us/rticles/360034404894-ddhe在fluxbc), [ddrml在sul在在gbc](/hc/en-us/rticles/360034924833-ddrml在sul在在gbc), [ddvoltgebc](/hc/en-us/rticles/360034404914-ddvoltgebc)
