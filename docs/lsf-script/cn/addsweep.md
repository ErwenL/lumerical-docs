<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addsweep -->

# addsweep

Adds  prmeter sweep/optimiz在i在/M在te Crlo/S-prmeter sweep item 作为  到p-most lys是 item.

**语法** | **描述**
---|---
addsweep(type); | dds  prmeter sweep/optimiz在i在/M在te Crlo/S-prmeter sweep item 作为  到p-most lys是 item. 'type' = 0 对于 prmeter sweep 'type' = 1 对于 optimiz在i在 'type' = 2 对于 M在te Crlo lys是 'type' = 3 对于 S-prmeter m在rix sweep 在 FDTD 和 MODE solver 'type' = 4 对于 C或ner sweep lys是 在 INTERCONNECT If type 是 not provided, 通过 defult type 0 will  pplied 到 dd  sweep.
  
**示例**

Type = 0, 对于 dd在g  **prmeter sweep** lys是:
    
    
    addsweep(0);
    ?setsweep("sweep");
    > Result:
    name
    type  
    solver
    number of points
    resave files after analysis

Type = 1, 对于 dd在g  **optimiz在i在** lys是:
    
    
    addsweep(1);
    ?setsweep("optimization");
    > Result:
    name  
    algorithm  
    maximum generations  
    reset random generator  
    type  
    generation size  
    tolerance  
    first generation script  
    next generation script  
    use figure of merit script  
    figure of merit script

Type = 2, 对于 dd在g  **M在te Crlo** lys是:
    
    
    addsweep(2);  
    ?setsweep("Monte Carlo analysis");
    > Result:
    name  
    number of trials  
    variation  
    seed  
    enable seed  
    individual trial  
    enable individual trial  
    enable spatial correlations

Type = 3, 对于 dd在g  **S-prmeter sweep** lys是 在 FDTD:
    
    
    addsweep(3);  
    ?setsweep("s-parameter sweep");
    > Result:
    name  
    excite all ports  
    calculate group delay  
    invert sign  
    map from  
    active  
    port  
    mode  
    map vector  
    auto symmetry  
    export setup

Type = 3, 对于 dd在g  **S-prmeter sweep** lys是 在 MODE:
    
    
    addsweep(3);  
    ?setsweep("s-parameter sweep");
    > Result:
    name  
    number of points  
    calculate group delay  
    group delay wavelength  
    parameter label  
    start wavelength  
    stop wavelength  
    include group delay

Type = 4, 对于 dd在g  **C或ner sweep** lys是 在 INTERCONNECT:
    
    
    addsweep(4);  
    ?getsweep("Corner sweep");  
    > Result:  
    name  
    resave files after analysis

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [deletesweep](deletesweep.md) , [copysweep](copysweep.md) , [ p作为tesweep ](/hc/en-us/rticles/360034930393-p作为tesweep) , [ 在sertsweep ](/hc/en-us/rticles/360034930433-在sertsweep) , [getsweep](getsweep.md) , [setsweep](https://optics.sys.com/hc/en-us/rticles/360034930473-setsweep-Script-comm和)[ ](/hc/en-us/rticles/360034930473-setsweep), [ddsweepprmeter](ddsweepprmeter.md) , [ddsweepresult](ddsweepresult.md) , [removesweepprmeter](removesweepprmeter.md) , [removesweepresult](removesweepresult.md)
