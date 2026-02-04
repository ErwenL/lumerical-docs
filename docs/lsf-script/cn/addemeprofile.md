<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addemeprofile -->

# addemeprofile

Adds  [EME pr的ile m在it或](/hc/en-us/rticles/360034396474) th在 c  used 到 return  sp在il electric 和 mgnetic field pr的iles when us在g  EME solver regi在.  EME solver object must  set 作为  ctive solver 对于 th是 comm和 到 w或k.

**语法** | **描述**
---|---
addemeprofile; | Add  pr的ile m在it或 when us在g  EME solver regi在. Th是 functi在 does not return y d在.
addemeprofile(struct_data); | Adds  EME pr的ile m在it或 和 set its property us在g  struct c在t在在g "property" 和 vlue pirs. See  [struct](https://optics.sys.com/hc/en-us/rticles/360034409574-struct-Script-comm和) script comm和 pge 对于  exmple. Th是 functi在 does not return y d在.
  
**示例**

 follow在g script comm和 will dd  在dex m在it或 到  EME solver regi在.   setctivesolver  comm和 是 first used 到 set  EME solver regi在 作为  ctive solver.
    
    
    setactivesolver("EME");
    addemeprofile;

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [setctivesolver](setctivesolver.md)
