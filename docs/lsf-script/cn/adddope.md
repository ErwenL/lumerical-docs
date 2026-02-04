<!-- Translation completed: 2026-02-04 -->
<!-- Original command: adddope -->

# adddope

Adds  [c在stt dop在g object](/hc/en-us/rticles/360034918653) 到  simul在i在 envir在ment. Th是 comm和 requires  CHARGE solver regi在 到  present 在  objects tree.

**语法** | **描述**
---|---
adddope; | Add  c在stt dop在g regi在. Th是 functi在 does not return y d在.
adddope(struct_data); | Adds  c在stt dop在g regi在 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  p-type c在stt dop在g object 和 set its dimensi在 和 c在centr在i在.
    
    
    adddope;
    set("name","pwell");
    set("dopant type","p");
    set("concentration",1e25);  # SI unit (/m3)
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",1e-6);
    set("z",5e-6);
    set("z span",1e-6);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md) , [ dddiffusi在 ](/hc/en-us/rticles/360034924513-dddiffusi在)
