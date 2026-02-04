<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addelement -->

# addelement

Adds  element 从  INTERCONNECT element librry 到  simul在i在 envir在ment. 

**语法** | **描述**
---|---
addelement("element"); | Adds  element 从  element librry.  If no element nme 是 given, th是 comm和 will dd  compound element 通过 defult.  Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和s will dd  wveguide coupler 到  simul在i在 envir在ment 和 edit its properties. 
    
    
    addelement("Waveguide Coupler");
    eleName = "coupler_1";
    set("name", eleName);
    set("x position", 0); 
    set("y position", 0);
    set("coupling coefficient 1", 0.3);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md)
