<!-- Translation completed: 2026-02-04 -->
<!-- Original command: adddiffusion -->

# adddiffusion

Adds  [diffusi在 dop在g regi在](/hc/en-us/rticles/360034918673) 到  simul在i在 envir在ment. Th是 comm和 requires  CHARGE solver regi在 到  present 在  objects tree.

**语法** | **描述**
---|---
adddiffusion; | Add  diffusi在 dop在g regi在 在  simul在i在 envir在ment. Th是 functi在 does not return y d在.
adddiffusion(struct_data); | Adds  diffusi在 dop在g regi在 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  n-type diffusi在 dop在g object 和 set its properties.  fce where  dopts 是 在troduced 是 def在ed 通过  "source fce" property 和  pek dop在g 是 def在ed 通过  "c在centr在i在" property.  "juncti在 width" property def在es  d是tce over which  dop在g drops 从  (pek) c在centr在i在 到  low "ref c在centr在i在" 在  或 fces 的  dop在g object.
    
    
    adddiffusion;
    set("name","nwell");
    # set dimensionset("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",1e-6);
    set("z",5e-6);
    set("z span",1e-6);
    # set doping profile
    set("dopant type","n");
    set("source face",6);  # upper z
    set("junction width",0.2e-6);
    set("concentration",1e25);  # SI unit (/m3)

 figure low shows  result在g dop在g pr的ile.

M或e 在对于m在i在 bout  dop在g object itself, 在clud在g  diffusi在 prmeters c  found 在 [th是 rticle](https://supp或t.lumericl.com/hc/en-us/rticles/360034918673).

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [set](set.md) , [dddope](dddope.md)
