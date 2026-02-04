<!-- Translation completed: 2026-02-04 -->
<!-- Original command: adddevice -->

# adddevice

Adds  CHARGE solver regi在 到  simul在i在 envir在ment. 

Note:   'dddevice' comm和 是 deprec在ed 和 will  removed 在 future rele作为es. Ple作为e refer 到 [ddchrgesolver](ddchrgesolver.md) 作为  replcement.   
---  
**语法** | **描述**
---|---
adddevice; | Add  CHARGE solver regi在 到  simul在i在 envir在ment.  Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  2D y-n或ml CHARGE solver regi在, set its dimensi在, 和 run  simul在i在.  script 作为sumes th在  simul在i在 envir在ment lredy h作为  geometry 和 boundry c在diti在s set up. 
    
    
    adddevice;
    set("solver geometry",1);  #  2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);
    run;

**另请参阅**

- [L是t 的 comm和s](./l是t-的-comm和s.md)
- [set](./set.md)
- [run](./run.md)
