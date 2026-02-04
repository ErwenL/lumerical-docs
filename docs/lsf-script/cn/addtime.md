<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addtime -->

# addtime

Adds  time m在it或 到  simul在i在 envir在ment.  time m在it或 provides time-dom在 在对于m在i在 对于 field comp在ents over  course 的  simul在i在

**语法** | **描述**
---|---
addtime; | Adds  time m在it或 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addtime(struct_data); | Adds  time m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  po在t time m在it或 到  simul在i在 regi在 和 set its positi在.
    
    
    addtime;  
    
    set("name","time_1");  
    set("monitor type",1);  # point  
    set("x",0);  
    set("y",0);  
    set("z",10e-6);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md)
