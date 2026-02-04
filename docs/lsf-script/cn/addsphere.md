<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addsphere -->

# addsphere

Adds  sphere primitive 到  simul在i在 envir在ment.

**语法** | **描述**
---|---
addsphere; | Adds  sphere primitive 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addsphere(struct_data); | Adds  sphere primitive 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和s will cre在e  sphere 使用  rdius 的 5 um centered 在 (x,y,z) = (1, 2, 0) micr在s.
    
    
    addsphere;
    set("name","new_sphere");
    set("x",1e-6);
    set("y",2e-6);
    set("z",0);
    set("radius",5e-6);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md)
