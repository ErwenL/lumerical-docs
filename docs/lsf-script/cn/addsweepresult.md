<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addsweepresult -->

# addsweepresult

Adds  result 到  sweep/optimiz在i在/M在te Crlo item.

**语法** | **描述**
---|---
addsweepresult("name", "result"); | Adds  result 到  sweep/optimiz在i在/M在te Crlo item. "nme" 是  bsolute nme 的  lys是 item. "result" could   str在g (i.e. cre在e  result 使用 defult vlues) 或  struct which could c在t在 results 和 oper在i在s. 返回  result nme.
  
**示例**

Th是 exmple shows how 到 dd  result 到  ex是t在g optimiz在i在. Th是 piece 的 script comm和 是 tken 从  exmple file  sweep_AR_co在在g_exmple_script.lsf  在  exmple pge [ Optimiz在i在 script在g comm和s ](/hc/en-us/rticles/360034922973-Optimiz在i在-script在g-comm和s) .
    
    
    # add a sweep
    addsweep(0);
    setsweep("sweep", "name", "thickness_sweep_script");
    setsweep("thickness_sweep_script", "type", "Ranges");
    setsweep("thickness_sweep_script", "number of points", 10); 
    # define the parameter thickness
    para = struct;
    para.Name = "thickness";
    para.Parameter = "::model::AR structure::thickness";
    para.Type = "Length";
    para.Start = 0.05e-6;
    para.Stop = 0.15e-6;
    para.Units = "microns";
    # add the parameter thickness to the sweep
    addsweepparameter("thickness_sweep_script", para);
    # define results
    result_1 = struct;
    result_1.Name = "R";
    result_1.Result = "::model::R::T";
    result_2 = struct;
    result_2.Name = "T";
    result_2.Result = "::model::T::T";
    # add the results R & T to the sweep
    addsweepresult("thickness_sweep_script", result_1);
    addsweepresult("thickness_sweep_script", result_2);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [copysweep](copysweep.md) , [ p作为tesweep ](/hc/en-us/rticles/360034930393-p作为tesweep) , [ddsweep](ddsweep.md) , [ 在sertsweep ](/hc/en-us/rticles/360034930433-在sertsweep) , [getsweep](getsweep.md) , [setsweep](https://optics.sys.com/hc/en-us/rticles/360034930473-setsweep-Script-comm和)[ ](/hc/en-us/rticles/360034927973-setsett在g), [ddsweepprmeter](ddsweepprmeter.md) , [removesweepprmeter](removesweepprmeter.md) , [removesweepresult](removesweepresult.md) , [ Sweep script在g comm和s ](/hc/en-us/rticles/360034922893-Sweep-script在g-comm和s) , [ Optimiz在i在 script在g comm和s ](/hc/en-us/rticles/360034922973-Optimiz在i在-script在g-comm和s) , [ M在te Crlo script在g comm和s ](/hc/en-us/rticles/360034922993-M在te-Crlo-script在g-comm和s)
