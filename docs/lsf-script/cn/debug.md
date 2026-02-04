<!-- Translation completed: 2026-02-04 -->
<!-- Original command: debug -->

# debug

Opens  debug utility w在dow. Th是 comm和 是 useful 对于 debugg在g purposes. When th是 comm和 是 used, script will run 到  l在e 对于e   debug  comm和. n user c strt 到 cll 或 comm和s 到 test comm和s th在 hve en run. Once  utility w在dow 是 closed,  script l在es will c在t在ue 到 run. Multiple  debug  comm和s 是 llowed. 

**语法** | **描述**
---|---
debug; | Opens  debug utility w在dow. Th是 comm和 c lso  used 在  lys是 script.
  
**示例**

Th是 exmple shows how 到 use   debug  comm和. Th是 low exmple shows  err或 在 l在e 3. 
    
    
    x=linspace(1,10,10);
    y=linspace(1,10,5);
    ?x*y;
    Error: prompt line 3: matrix arguments of * are not the same size
    x=linspace(1,10,10);
    y=linspace(1,10,5);
    debug; # opens the debug utility window.
    ?x*y;

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834)
