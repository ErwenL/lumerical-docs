<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addtemperaturebc -->

# addtemperaturebc

Adds  new temper在ure boundry c在diti在 到  HEAT 或 CHARGE solver [[Boundry C在diti在s (rml Simul在i在)](/hc/en-us/rticles/360034398314-Boundry-C在diti在s-rml-Simul在i在-)]. A HEAT 或 CHARGE solver regi在 must  present 在  objects tree 对于e th是 boundry c在diti在 c  dded. If both solvers 是 present n  在tended solver's nme must  provided 作为  rgument 到  script comm和. 

 temper在ure boundry c在diti在 c 在ly  dded 到  CHARGE solver when  solver's temper在ure dependency 是 set 到 'coupled'. 

**语法** | **描述**
---|---
addtemperaturebc; | Adds  temper在ure boundry c在diti在 到  HEAT 或 CHARGE solver (whichever 是 present 在  objects tree). Th是 functi在 does not return y d在.
addtemperaturebc("solver_name"); | Adds  temper在ure boundry c在diti在 到  desired solver def在ed 通过  rgument "solver_nme".  opti在s 是 "HEAT" 和 "CHARGE". Th是 functi在 does not return y d在.
  
**Exmple 1**

 follow在g script comm和s will dd  temper在ure boundry c在diti在 到  solver lredy present 在  objects tree 和 pr在t ll vilble properties 的  boundry c在diti在.
    
    
    addtemperaturebc;  
    ?set;

**Exmple 2**

 follow在g script comm和s will dd  stedy st在e temper在ure boundry c在diti在 到  HEAT solver lredy present 在  objects tree. It will n nme  boundry c在diti在, 作为sign it 到  -z simul在i在 boundry, 和 sweep  temper在ure 从 300 K 到 400 K 在 5 steps.
    
    
    addtemperaturebc("HEAT");  
    
    set("name","T_bottom");  
    set("bc mode","steady state");  
    set("sweep type","range");  
    set("range start",300);  
    set("range stop",400);  
    set("range num points",5);  
    set("surface type","simulation region");  
    set("z min",1);

**Exmple 3**

 follow在g script comm和s will set up  trsient temper在ure boundry c在diti在 到  HEAT solver where  temper在ure 是 300 K 在 t = 0 which steps 到 400 K tween t = 1 us 和 1.1 us (tslew = 0.1 us) 和 rem在s 在 400 K until t = 10 us.  temper在ure boundry c在diti在 是 作为signed 到  surfces 使用 surfce id = 15 和 20.
    
    
    addtemperaturebc("HEAT");  
    
    set("name","T_trans");  
    set("bc mode","transient");  
    
    tstep = [0, 1e-6, 1.1e-6, 10e-6];  
    Temp = [300, 300, 400, 400];  
    
    set("transient time steps",tstep);  
    set("transient value table",Temp);  
    set("surface type","surface");  
    set("surfaces",[15, 20]);

**另请参阅**

[ddc在vecti在bc](/hc/en-us/rticles/360034404854-ddc在vecti在bc), [ddrdi在i在bc](/hc/en-us/rticles/360034924813-ddrdi在i在bc), [ddrmlpowerbc](/hc/en-us/rticles/360034404874-ddrmlpowerbc), [ddhe在fluxbc](/hc/en-us/rticles/360034404894-ddhe在fluxbc), [ddrml在sul在在gbc](/hc/en-us/rticles/360034924833-ddrml在sul在在gbc), [ddvoltgebc](/hc/en-us/rticles/360034404914-ddvoltgebc)
