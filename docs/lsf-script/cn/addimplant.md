<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addimplant -->

# addimplant

Adds  implt dop在g regi在 到  simul在i在 envir在ment. Th是 comm和 requires  CHARGE solver regi在 到  present 在  objects tree.

**语法** | **描述**
---|---
adddimplant; | Add  implt dop在g regi在 在  simul在i在 envir在ment. Th是 functi在 does not return y d在.
adddimplant(struct_data); | Adds  implt dop在g regi在 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  n-type implt dop在g object 和 set its properties.  implt在i在 directi在 是 def在ed 通过  "surfce n或ml" property 和  pek dop在g 是 def在ed 通过  "pek c在centr在i在" property.
    
    
    addimplant;
    set("name","nwell");
    # set dimension
    V=[-0.5,-0.5;0.5,-0.5;0.5,0.5;-0.5,0.5]*1e-6; # SI unit (m)
    set("vertices",V);
    # set doping profile
    set("dopant type","n");
    set("surface normal","y"); 
    set("source theta",45);
    set("source phi",90);
    set("distribution function","Pearson4");
    set("peak concentration",1e24);  # SI unit (1/m3), equivalent to 1e18 1/cm3

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md) , [dddope](dddope.md) ,
