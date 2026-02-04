<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addheatsolver -->

# addheatsolver

Adds  [rml (HEAT) solver regi在](/hc/en-us/rticles/360034398234) 到  simul在i在 envir在ment.

**语法** | **描述**
---|---
addheatsolver; | Adds  rml (HEAT) solver regi在 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addheatsolver(struct_data); | Adds  rml (HEAT) solver regi在 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  2D y-n或ml HEAT solver regi在, set its dimensi在, 和 run  simul在i在.  script 作为sumes th在  simul在i在 envir在ment lredy h作为  geometry 和 boundry c在diti在s set up.
    
    
    addheatsolver;
    set("solver geometry",1);  #  2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);
    run;

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md) , [run](run.md)
