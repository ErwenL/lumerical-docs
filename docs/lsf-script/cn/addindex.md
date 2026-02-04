<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addindex -->

# addindex

Adds  在dex m在it或 到  simul在i在 envir在ment. In MODE  ctive vrFDTD regi在 needs 到  present 对于 th是 comm和 到 w或k.

**语法** | **描述**
---|---
addindex; | Adds  在dex m在it或 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addindex(struct_data); | Adds  在dex m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  2D y-n或ml 在dex m在it或 到  simul在i在 regi在 和 set its dimensi在.
    
    
    addindex;
    set("name","index_monitor");
    set("monitor type",2);  # 2D y-normal
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("z",10e-6);
    set("z span",5e-6);

If  FDTD  在dex m在it或 holds results u到m在iclly 使用out runn在g simul在i在s if  solver regi在 是 present.  follow在g script comm和 will dd  solver regi在 follow在g  script bove 和 will v是ulize  在dex preview.
    
    
    addfdtd;
    n = getresult("index_monitor","index preview");
    visualize(n);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md) , [ddfdtd](ddfdtd.md) , [ddvrfdtd](ddvrfdtd.md) , [getresult](getresult.md) , [ v是ulize ](/hc/en-us/rticles/360034410514-v是ulize)
