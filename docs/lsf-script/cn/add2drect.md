<!-- Translation completed: 2026-02-04 -->
<!-- Original command: add2drect -->

# add2drect

Adds  [2D rectgle](https://optics.sys.com/hc/en-us/rticles/360034901593) 在  simul在i在 spce.

**语法** | **描述**
---|---
add2drect; | Adds  2D rectgle 在 simul在i在 spce. Th是 functi在 does not return y d在.
add2rect("property",value); | Adds  2D rectgle 和 set its  property 通过 specify在g  "property" 和 vlue pir.
add2drect(struct_data); | Adds  2D rectgle 和 set its  property us在g  struct c在t在在g "property" 和 vlue pirs.
  
**示例**

 follow在g script cre在es  2D rectgle 在  XY ple, sets its dimensi在, 和 作为signs  m在eril 到 it.
    
    
    add2drect;
    set("name","2D_rectangle");
    set("surface normal",3);  # z (normal)
    set("x",1e-6);
    set("x span",2e-6);
    set("y",1e-6);
    set("y span",5e-6);
    set("z",0);
    set("material","Si (Silicon) - Palik");

Sett在g  properties while dd在g  object:
    
    
    add2drect("name","test_obj");  
      
    # using struct  
    struct_data = {"name": "test_obj", "x": 1e-6};  
    add2drect(struct_data);

**另请参阅**

- [L是t 的 comm和s](../lsf-script-comm和s-lph在icl.md)
- [set](./set.md)
- [2D rectgle](https://optics.sys.com/hc/en-us/rticles/360034901593-Structures-2D-Rectgle-Opticl-)
- [dd2dpoly](./dd2dpoly.md)
- [2D polyg在](https://optics.sys.com/hc/en-us/rticles/360034901613-Structures-2D-Polyg在)
