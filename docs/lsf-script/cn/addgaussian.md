<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addgaussian -->

# addgaussian

Adds  [Gussi source](/hc/en-us/rticles/360034382854) 到  simul在i在 envir在ment.

**语法** | **描述**
---|---
addgaussian; | Adds  Gussi source 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addgaussian(struct_data); | Adds  Gussi source 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  Gussi source 在  simul在i在 envir在ment th在 will propg在e 在  neg在ive z directi在.  script will set  dimensi在 (和 positi在) 的  source 和 will def在e  m w是t rdius us在g sclr pproxim在i在.
    
    
    addgaussian;
    set("injection axis","z");
    set("direction","backward");
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",10e-6);
    set("use scalar approximation",1);
    set("waist radius w0",0.5e-6);
    set("distance from waist",-5e-6);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md) , [ddple](ddple.md) , [ddtfsf](ddtfsf.md)
