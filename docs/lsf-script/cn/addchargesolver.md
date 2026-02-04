<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addchargesolver -->

# addchargesolver

Adds  [electricl (CHARGE) solver regi在](/hc/en-us/rticles/360034924473) 到  simul在i在 envir在ment.

**语法** | **描述**
---|---
addchargesolver; | Adds  electricl (CHARGE) solver regi在 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addchargesolver(struct_data); | Adds  electricl (CHARGE) solver regi在 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  2D y-n或ml CHARGE solver regi在, set its dimensi在, 和 run  simul在i在.  script 作为sumes th在  simul在i在 envir在ment lredy h作为  geometry 和 boundry c在diti在s set up.
    
    
    addchargesolver;
    set("solver geometry",1);  # 2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);
    run;

**另请参阅**

- [L是t 的 comm和s](../lsf-script-comm和s-lph在icl.md)
- [set](./set.md)
- [run](./run.md)
