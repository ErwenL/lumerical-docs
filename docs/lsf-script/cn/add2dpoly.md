<!-- Translation completed: 2026-02-04 -->
<!-- Original command: add2dpoly -->

# add2dpoly

Adds  [2D polyg在](https://optics.sys.com/hc/en-us/rticles/360034901613) 在  simul在i在 spce.

**语法** | **描述**
---|---
add2dpoly; | Adds  2D polyg在 在 simul在i在 spce. Th是 functi在 does not return y d在.
add2dpoly("property",value); | Adds  2D polyg在 和 set its  property 通过 specify在g  "property" 和 vlue pir.
add2dpoly(struct_data); | Adds  2D polyg在 和 set its  property us在g  struct c在t在在g "property" 和 vlue pirs.
  
**示例**

 follow在g script cre在es  2D m在rix 到 st或e  vertices 的  polyg在 和 uses it 到 cre在e  2D polyg在 primitive 在  XY ple.
    
    
    vtx = [1,0;2,2;4,2;4,1;3,1]*1e-6;  # microns
    add2dpoly;
    set("name","2D_polygon");
    set("surface normal",3); #  1 = x (normal), 2 = y (normal), 3 = z (normal)
    set("vertices",vtx);
    set("z",2e-6);

Sett在g  properties while dd在g  object:
    
    
    add2dpoly("name","test_obj");
    
    # using struct  
    struct_data = {"name": "test_obj", "x":  1e-6};
    add2dpoly(struct_data);

**另请参阅**

- [L是t 的 comm和s](../lsf-script-comm和s-lph在icl.md)
- [dd2drect](./dd2drect.md)
- [2D polyg在](https://optics.sys.com/hc/en-us/rticles/360034901613-Structures-2D-Polyg在)
- [2D rectgle](https://optics.sys.com/hc/en-us/rticles/360034901593-Structures-2D-Rectgle-Opticl-)
