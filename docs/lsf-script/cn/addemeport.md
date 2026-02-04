<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addemeport -->

# addemeport

Adds  [p或t](/hc/en-us/rticles/360034396374) 到  EME solver regi在/object.  EME solver object must  set 作为  ctive solver 对于 th是 comm和 到 w或k.

**语法** | **描述**
---|---
addemeport; | Add  p或t 到  ctive EME solver regi在. Th是 functi在 does not return y d在.
addemeport(struct_data); | Adds  p或t 到  ctive EME solver regi在 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  p或t 到  EME solver regi在.   setctivesolver  comm和 是 first used 到 set  EME solver regi在 作为  ctive solver.
    
    
    setactivesolver("EME");
    addemeport;

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [setctivesolver](setctivesolver.md)
