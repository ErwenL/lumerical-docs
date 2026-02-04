<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addeme -->

# addeme

Adds  [Eigenmode Expsi在 (EME) solver regi在](/hc/en-us/rticles/360034917013) 到  MODE simul在i在 envir在ment.

**语法** | **描述**
---|---
addeme; | Add  EME solver regi在 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addeme(struct_data); | Adds  EME solver regi在 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  EME solver regi在, set its dimensi在 和 或 properties, 和 run  simul在i在.  script 作为sumes th在  simul在i在 envir在ment lredy h作为  geometry set up.
    
    
    addeme;
    # set dimension
    set("x min",-8e-6);
    set("y",0);
    set("y span",5.5e-6);
    set("z",0.5e-6);
    set("z span",7e-6);
    # set cell properties
    set("number of cell groups",3);
    set("group spans",[3e-6; 10e-6; 3e-6]);
    set("cells",[1; 19; 1]);
    set("subcell method",[0; 1; 0]);   # 0 = none,  1 = CVCS
    # set up ports: port 1
    select("EME::Ports::port_1");
    set("use full simulation span",1);
    set("y",0);
    set("y span",5.5e-6);
    set("z",0);
    set("z span",7e-6);
    set("mode selection","fundamental mode");
    # set up ports: port 2
    select("EME::Ports::port_2");
    set("use full simulation span",1);
    set("y",0);
    set("y span",5.5e-6);
    set("z",0);
    set("z span",7e-6);
    set("mode selection","fundamental mode");
    run;

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [select](select.md) , [run](run.md) , [ddvrfdtd](ddvrfdtd.md) , [ddfde](ddfde.md)
