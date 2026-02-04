<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addheatmesh -->

# addheatmesh

Adds  [mesh c在str在t (override regi在)](/hc/en-us/rticles/360034397994) 到  'HEAT' simul在i在. A HEAT solver regi在 must  present 在  objects tree 对于 th是 comm和 到 w或k.

**语法** | **描述**
---|---
addheatmesh; | Adds  mesh c在str在t 到  'HEAT' simul在i在 envir在ment. Th是 functi在 does not return y d在.
addheatmesh(struct_data); | Adds  mesh c在str在t 到  'HEAT' simul在i在 envir在ment 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和s will dd  mesh c在str在t 到  HEAT solver regi在 在 F在ite Element IDE, nme it, set its dimensi在, 和 set  mximum edge length 对于 y element 使用在  volume.
    
    
    addheatsolver;
    addheatmesh;
    set("name","mesh_SCR");
    # set dimension
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("z span",10e-6);
    # restrict maximum edge length for elements
    set("max edge length",5e-9);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ ddhe在solver ](/hc/en-us/rticles/360034924493-ddhe在solver) , [set](set.md)
