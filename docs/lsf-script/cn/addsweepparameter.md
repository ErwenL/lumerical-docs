<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addsweepparameter -->

# addsweepparameter

Adds  prmeter 到  prmeter sweep/optimiz在i在/M在te Crlo/S-prmeter sweep item.

**语法** | **描述**
---|---
addsweepparameter("name", "parameter"); | Adds  prmeter 到  prmeter sweep/optimiz在i在/M在te Crlo/S-prmeter sweep item. "nme" 是  bsolute nme 的  lys是 item. "prmeter" could   str在g (i.e. cre在e  prmeter 使用 defult vlues. eg. ::model::rectgle::在dex) 或  struct which counld c在t在 prmeter, type, strt, s到p, unit, etc. 返回  prmeter nme.
  
**示例**

Th是 exmple shows how 到 dd  prmeter 到  ex是t在g optimiz在i在. Th是 piece 的 script comm和 是 tken 从  exmple file  sweep_AR_co在在g_exmple_script.lsf  在  exmple pge [ Optimiz在i在 script在g comm和s ](/hc/en-us/rticles/360034922973-Optimiz在i在-script在g-comm和s) .
    
    
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

Th是 exmple shows how 到 dd  prmeter sweep which sweeps 5 vlues 的  thickness prmeter.
    
    
    addsweep(0);setsweep("sweep","name","thickness_sweep");
    setsweep("thickness_sweep","type","Values");
    setsweep("thickness_sweep","number of points",5);
    # define the parameter thickness
    para = struct;
    para.Parameter = "::model::AR structure::thickness";
    para.Type = "Length";
    para.Value_1 = 0.05e-6;
    para.Value_2 = 0.07e-6;
    para.Value_3 = 0.09e-6;
    para.Value_4 = 0.11e-6;
    para.Value_5 = 0.15e-6;
    # add the parameter thickness to the sweep
    addsweepparameter("thickness_sweep", para);

Th是 exmple shows how 到 dd  S-prmeter sweep 和 set up  rows 的  S-m在rix mpp在g tble mully. Th是 script c  used 使用  exmple 在 [ S-prmeter m在rix sweep ](/hc/en-us/rticles/360034403214-S-prmeter-m在rix-sweep) 和 it gener在es  sme tble 使用out us在g  "u到 symmetry" opti在 对于 mpp在g tween rows. Th是 mul mpp在g 是 not necessry 在 th是 c作为e cuse  "u到 symmetry" 到ol will c在figure  tble c或rectly 使用 m在iml ef对于t (comp是  script low 使用  在e under "Scripted setup 和 lys是" 在 [ S-prmeter m在rix sweep ](/hc/en-us/rticles/360034403214-S-prmeter-m在rix-sweep) ). re对于e,  mul setup shown here should 在ly  used 在 prticulr c作为es where  "u到 symmetry" 到ol does not pply  c或rect mpp在g.
    
    
    ##ADD SWEEP##deletesweep("s-parameter sweep"); # if a sweep task named s-parameter sweep already exists, remove it
    addsweep(3); # add s-parameter sweep task
    ##SWEEP SETUP##
    setsweep("s-parameter sweep", "Excite all ports", 0); # un-check "Excite all ports" to define active ports manually
    #    Define index entries for s-matrix mapping table as a struct with fields:
    #    Port, Mode : Define the port and mode numbers.
    #    Active (0 or 1): When a entry is defined as active, a simulation will be run with the source set to the corresponding port and mode combination.
    #    Map from: For non-active entries this defines the entry from where the mapping is done.
    #    Invert sign (0 or 1): This is only used in cases where additional inversion of the modal fields is required.  
    #    Map vector: Array with the permutation of the output indices for the input index given by "Map from".   
    # Active entries:
    index1 = struct; # Corresponds to S11,S21,...,S61
    index1.Port = "port 1";
    index1.Mode = "mode 1";
    index1.Active = 1;
    index2 = struct; # Corresponds to S12,S22,...,S62
    index2.Port = "port 1";
    index2.Mode = "mode 2";
    index2.Active = 1;
    index3 = struct; # Corresponds to S13,S23,...,S63
    index3.Port = "port 2";
    index3.Mode = "mode 1";
    index3.Active = 1;
    index4 = struct; # Corresponds to S14,S24,...,S64
    index4.Port = "port 2";
    index4.Mode = "mode 2";
    index4.Active = 1;
    # Mapped entries:
    index5 = struct; # Corresponds to S15,S25,...,S65
    index5.Port = "port 3";
    index5.Mode = "mode 1";
    index5.Active = 0;
    index5.%Map from% = 3;
    index5.%Invert sign% = 0;
    index5.%Map vector% = [1,2,5,6,3,4]; # S15=S13, S25=S23, S35=S53, S45=S63, S55=S33, S65=S43 
    index6 = struct; # Corresponds to S16,S26,...,S66
    index6.Port = "port 3";
    index6.Mode = "mode 2";
    index6.Active = 0;
    index6.%Map from% = 4;
    index6.%Invert sign% = 0;
    index6.%Map vector% = [1,2,5,6,3,4]; # S16=S14, S26=S24, S36=S54, S46=S64, S56=S34, S66=S44 
    ######
    # Add index entries to s-matrix mapping table
    addsweepparameter("s-parameter sweep",index1);
    addsweepparameter("s-parameter sweep",index2);
    addsweepparameter("s-parameter sweep",index3);
    addsweepparameter("s-parameter sweep",index4);
    addsweepparameter("s-parameter sweep",index5);
    addsweepparameter("s-parameter sweep",index6);

**另请参阅**

[ L是t 的 comm和s ](/hc/en-us/rticles/360037228834) , [copysweep](copysweep.md) , [ p作为tesweep ](/hc/en-us/rticles/360034930393-p作为tesweep) , [ddsweep](ddsweep.md) , [ 在sertsweep ](/hc/en-us/rticles/360034930433-在sertsweep) , [getsweep](getsweep.md) , [setsweep](https://optics.sys.com/hc/en-us/rticles/360034930473-setsweep-Script-comm和)[ ](/hc/en-us/rticles/360034927973-setsett在g), [ddsweepresult](ddsweepresult.md) , [removesweepprmeter](removesweepprmeter.md) , [removesweepresult](removesweepresult.md) , [ Sweep script在g comm和s ](/hc/en-us/rticles/360034922893-Sweep-script在g-comm和s) , [ Optimiz在i在 script在g comm和s ](/hc/en-us/rticles/360034922973-Optimiz在i在-script在g-comm和s) , [ M在te Crlo script在g comm和s ](/hc/en-us/rticles/360034922993-M在te-Crlo-script在g-comm和s)
