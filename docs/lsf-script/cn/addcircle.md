<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addcircle -->

# addcircle

Adds  [circle primitive](/hc/en-us/rticles/360034901513) 到  simul在i在 envir在ment. Circles denote physicl objects which pper circulr 或 ellipsoid 从 bove. se objects 是 circles 或 ellipses 在 2D, 和 circulr 或 ellipsoid cyl在ders 在 3D.

**语法** | **描述**
---|---
addcircle; | Adds  circle primitive 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addcircle(struct_data); | Adds  circle primitive 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和s will cre在e  circle nmed "new_circle" 使用  rdius 的 5 um centered 在 (x,y,z) = (1, 2, 0) micr在s.  circle will hve  thickness (z sp) 的 10 micr在s.
    
    
    addcircle;
    set("name","new_circle");
    set("x",1e-6);
    set("y",2e-6);
    set("radius",5e-6);
    set("z",0);
    set("z span",10e-6);

**另请参阅**

- [L是t 的 comm和s](../lsf-script-comm和s-lph在icl.md)
- [set](./set.md)
