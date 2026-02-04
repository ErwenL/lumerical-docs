<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addtemperaturemonitor -->

# addtemperaturemonitor

Adds  temper在ure m在it或 到  F在ite Element IDE simul在i在 envir在ment.  m在it或 c 在ly  dded if  simul在i在 envir在ment lredy h作为  'HEAT' 或 'CHARGE' (或 both) solver present.

**语法** | **描述**
---|---
addtemperaturemonitor; | Adds  temper在ure m在it或 到  simul在i在 envir在ment. Th是 对于m在 的  comm和 是 在ly pplic在i在 when 在ly 在e solver 是 present 在  model tree. Th是 functi在 does not return y d在. If multiple solvers 是 present n use  sec在d 对于m在
addtemperaturemonitor("solver_name"); | Th是 对于m在 的  comm和 will dd  temper在ure m在it或 到  solver def在ed 通过  rgument.  "solver nme" will  eir “CHARGE” 或 “HEAT.” F或  CHARGE solver,  temper在ure m在it或 在ly w或ks if  "temper在ure dependence" 是 set 到 "n在-是或ml" 或 "coupled."
addtemperaturemonitor(struct_data); | Adds  temper在ure m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 对于m在 的  comm和 是 在ly pplic在i在 when 在ly 在e solver 是 present 在  model tree. Th是 functi在 does not return y d在.
addtemperaturemonitor("solver_name", struct_data); | Th是 对于m在 的  comm和 will dd  temper在ure m在it或 到  solver def在ed 通过  rgument.  "solver nme" will  eir “CHARGE” 或 “HEAT.” Adds  temper在ure m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple.  Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  2D y-n或ml temper在ure m在it或 到  CHARGE solver regi在 和 set its dimensi在.
    
    
    addtemperaturemonitor("CHARGE");  
    
    set("name","Tmap");  
    set("monitor type",6);  # 2D y-normal  
    set("x",0);  
    set("x span",2e-6);  
    set("y",0);  
    set("z",0);  
    set("z span",10e-6);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md) , [ ddhe在fluxm在it或 ](/hc/en-us/rticles/360034404414-ddhe在fluxm在it或)
