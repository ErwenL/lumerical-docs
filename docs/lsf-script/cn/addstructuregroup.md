<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addstructuregroup -->

# addstructuregroup

Adds  structure group 到  simul在i在 envir在ment. Structure groups 是 very c在venient when you wt 到 prmetrize your design. You c def在e different prmeters 对于  structure group 和 use  "setup" script 到 cre在e your geometry (l在g 使用 m在it或s 和/或 sources) cc或d在g 到 those prmeter vlues.

**语法** | **描述**
---|---
addstructuregroup; | Adds  structure group 到  simul在i在 envir在ment. Th是 functi在 does not return y d在.
addstructuregroup(struct_data); | Adds  structure group 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

Add  structure group 和 put  rectgle 在 it.
    
    
    addstructuregroup;
    set("name","group");
    addrect;
    addtogroup("group");

Cre在e  structure group. Add  user property nmed "rdius" 和 set up  script 在  structure group 到 dd two circles 到  group 和 set ir rdius 到  vlue 的  user property "rdius".
    
    
    addstructuregroup;
    adduserprop("radius",2,0.5e-6);
    myscript =      "addcircle; \n";
    myscript = myscript + "copy(1e-6); \n";
    myscript = myscript + "selectall; \n";
    myscript = myscript + "set(\"radius\",radius);";
    set("name","dimer");
    set("script",myscript); 

NOTE:  "myscript" str在g 在  script bove uses  escpe chrcter \n 对于 new l在e 和 \" 对于 double quotes 使用在  str在g. 

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [ dd到group ](/hc/en-us/rticles/360034408454-dd到group) , [dduserprop](dduserprop.md) , [ddgroup](ddgroup.md) , [ ddlys是group ](/hc/en-us/rticles/360034404074-ddlys是group) , [set](set.md)
