<!--
Translation from English documentation
Original command: setsweep
Translation date: 2026-02-04 22:50:14
-->

# setsweep

设置 一个 属性 在 一个 参数 sweep/optimization/Monte Carlo/S-参数 sweep item.

**语法** |  **描述**  
---|---  
setsweep("name", "property_name", property_value); |  设置 一个 属性 在 一个 sweep/optimization/Monte Carlo/S-参数 item. "name" 是 该 absolute name 的 一个 分析 item. "property_name" 是 该 属性 showed 在 该 edit window.  
?setsweep(“name”); |  View 该 editable 属性 的 该 分析 item.  
“name” 是 该 absolute name 的 该 分析 item.  
  
For a [**parameter sweep**](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweep-utility)analysis:

**Argument** |  **描述**  
---|---  
property_name = "name" |  设置 该 name 的 该 sweep.  
property_name = "求解器" |  设置 该 求解器 used 用于 sweep.  
property_name = "类型" |  设置 该 类型 的 该 sweep. The 值 的 "类型" could 为 "Ranges" 或 "Values"  
property_name = "数字 的 points" |  设置 该 数字 的 points 的 该 sweep. The default 数字 的 points 是 10.  
property_name = "resave files after 分析" |  Defines whether 或 not 到 re-save 该 文件 after 分析.  
  
For an **[optimization](https://optics.ansys.com/hc/en-us/articles/360034922953-Optimization-utility) ** analysis:

**Argument** |  **描述**  
---|---  
property_name = "name" |  设置 该 name 的 该 optimization.  
property_name = "algorithm" |  "algorithm" = "Particle Swarm", "User Defined"  
property_name = "maximum generations" |  设置 该 maximum generation 数字.  
property_name = "reset random generator" |  Checks 该 box 的 "Reset random generation".  
property_name = "类型" |  "Type" = "Maximum", "Minimum"  
property_name = "generation size" |  The 数字 的 simulations per generation.  
property_name = "tolerance" |  设置 该 tolerance 值.  
property_name = "first generation 脚本" |  设置 该 "first generation 脚本" 在 该 "Advanced" tab.  
property_name = "next generation 脚本" |  设置 该 "next generation 脚本" 在 该 "Advanced" tab.  
property_name = "use figure 的 merit 脚本" |  Checks 该 box 的 "use figure 的 merit" 在 该 "Figure 的 merit 脚本" tab.  
property_name = "figure 的 merit 脚本" |  设置 该 "figure 的 merit 脚本" 在 该 "Figure 的 merit 脚本" tab.  
  
For a [**Monte Carlo**](https://optics.ansys.com/hc/en-us/articles/360034403194-Monte-Carlo-analysis-utility) analysis:

**Argument** |  **描述**  
---|---  
property_name = "name" |  设置 该 name 的 该 Monte Carlo.  
property_name = "数字 的 trials" |  设置 该 数字 的 trials 用于 该 Monte Carlo. The default 数字 的 trials 是 10.  
property_name = "variation" |  设置 该 variation 用于 "Process" 或 "Mismatch" 或 "Both". The default variation 是 "Both".  
property_name = "seed" |  设置 该 seed.  
property_name = "启用 seed" |  设置 whether 或 not 到 启用 该 seed.  
property_name = "individual trial" |  设置 该 individual trial 数字.  
property_name = "启用 individual trail" |  设置 whether 或 not 到 启用 individual trials.  
property_name = “启用 spatial correlations” |  设置 whether spatial correlation 是 enabled.  
  
For an [**S-parameter matrix sweep**](https://optics.ansys.com/hc/en-us/articles/360034403214-S-parameter-matrix-sweep-utility) analysis:

**Argument** |  **描述**  
---|---  
property_name = "name" |  设置 该 name 的 该 S-参数 矩阵 sweep.  
property_name = "excite all ports" |  If property_value = "true", 该 sweep 将 run as many simulations as there 是 defined rows 在 该 S-Matrix Setup table. If property_value = "false", simulations 将 为 run only 用于 该 选中的 rows 在 该 S-Matrix Setup table. The default 是 "true".  
property_name = "计算 group delay" |  When enabled, 该 group delay 的 该 device 是 calculated numerically 使用 一个 finite difference approximation, 使用 该 derivative 的 phase 使用 respect 到 频率.  
property_name = "invert sign" property_name = "map from" property_name = "active" property_name = "port" property_name = "mode" property_name = "map vector" |  These properties are set for each row of the S-Matrix Setup table tab. To set them manually, the command [addsweepparameter](https://optics.ansys.com/hc/en-us/articles/360034930493-addsweepparameter-Script-command) should be used. The meaning of each parameter can be found in the Knowledge Base Article on S-parameter sweeps. Once added, the rows cannot be changed and must be removed using [removesweepparameter](https://optics.ansys.com/hc/en-us/articles/360034930513-removesweepparameter-Script-command) first.  
property_name = "auto symmetry" |  If property_value = "true", auto symmetry 是 calculated 和 applied 当 possible (see [ S-参数 矩阵 sweep ](/hc/en-us/articles/360034403214-S-参数-矩阵-sweep) ). If property_value = "false", no changes 是 applied 到 该 S-参数 sweep. The default 是 "false". **注意:** The changes made 到 该 S-参数 sweep cannot 为 undone 通过 setting property_value = "false". When property_value = "false", no settings change 在 该 current sweep.  
property_name = "export setup" |  This 属性 设置 up 该 layout 的 该 export 文件 用于 export 的 数据 在 either Lumerical 或 Touchstone format. There 是 two possible 参数:

  * “auto”: Uses automatic definition 用于 该 export table.
  * A 自定义 结构 defining each 端口, see 该 example below 在 如何 该 结构 应该 为 formatted.

  
  
For an [S-parameter matrix sweep](https://optics.ansys.com/hc/en-us/articles/360034403214-S-parameter-matrix-sweep-utility) analysis in MODE:

**Argument** |  **描述**  
---|---  
property_name = "name" |  设置 该 name 的 该 S-参数 矩阵 sweep.  
property_name = "数字 的 points" |  设置 该 数字 的 points 在 该 sweep.  
property_name = "calculated group delay" |  设置 whether 该 group delay 是 calculated.  
property_name = "group delay 波长" |  设置 该 波长 到 计算 group delay. This option has no effect unless “calculated group delay” 是 enabled. But 如果 设置 prior 到 enabling 该 calculation, 该 设置 值 将 为 automatically applied 当 该 option 是 enabled.  
property_name = "参数 label" |  设置 该 name 的 该 参数 的 该 sweep.  
property_name = "start 波长" |  设置 该 start 波长 的 该 sweep.  
property_name = "stop 波长" |  设置 该 stop 波长 的 该 sweep.  
property_name = "include group delay" |  This 属性 设置 up 该 layout 的 该 export 文件 用于 export 的 数据 在 either Lumerical 或 Touchstone format. There 是 two possible 参数:

  * “auto”: Uses automatic definition 用于 该 export table.
  * A 自定义 结构 defining each 端口, see 该 example below 在 如何 该 结构 应该 为 formatted.

  
Editing added sweep 参数:  In addition 到 该 listed default 属性 的 该 sweep/optimization/Monte Carlo/S-参数, any added sweep 参数 可以 为 edited 通过 该 setsweep 命令 通过 setting 该 "property_name" 到 该 参数 name.  
---  
  
**示例**

This examples show 如何 到 设置 一个 sweep/optimization/Monte Carlo/S-参数's 属性 respectively. Please refer 到 该 application example page [ Sweep scripting commands ](/hc/en-us/articles/360034922893-Sweep-scripting-commands) 用于 detailed information.

Sweep:
    
    
    addsweep(0);
    setsweep("sweep", "name", "thickness_sweep_script");
    setsweep("thickness_sweep_script", "类型", "Ranges");
    setsweep("thickness_sweep_script", "数字 的 points", 10); 

Optimization:
    
    
    addsweep(1);
    setsweep("optimization", "name", "thickness_optimization_script");
    setsweep("thickness_optimization_script", "Type", "Minimize");
    setsweep("thickness_optimization_script", "algorithm", "Particle Swarm");
    setsweep("thickness_optimization_script", "maximum generations", 20);
    setsweep("thickness_optimization_script", "generation size", 10);
    setsweep("thickness_optimization_script", "tolerance", 0);

Monte Carlo:
    
    
    addsweep(2);
    MC_name = "MC_script";
    setsweep("Monte Carlo 分析", "name", MC_name);
    setsweep(MC_name, "数字 的 trials", 50);
    setsweep(MC_name, "启用 seed", 1);
    setsweep(MC_name, "seed", 1);
    setsweep(MC_name, "Variation", "Both");

S-参数 sweep:
    
    
    addsweep(3);
    setsweep("s-参数 sweep", "name", "S sweep");
    setsweep("s-参数 sweep", "Excite all ports", 0);
    setsweep("S sweep", "auto symmetry", true);

This example defines 和 设置 该 export setup 在 FDTD 用于 该 setting shown 在 该 figure below. Columns other than “Mode label” , “Mode ID”, 和 “Port location” cannot 为 changed.
    
    
    modestruct = {"label": "mode 1", "id" : 1};  
    rowstruct = {"mode 1": modestruct, "location": "LEFT"};  
    portstruct = {"端口 2": rowstruct};   
    setsweep("s-参数 sweep", "export setup", portstruct);

This example 设置 该 export setup 在 MODE 用于 该 **second** row 在 该 figure below. Other rows 在 该 table 是 automatically filled based 在 该 placement 的 Port 对象 在 该 仿真 domain. Columns other than “Mode label” 和 “Mode ID” cannot 为 changed.

****
    
    
    modestruct = {"label": "my mode 2", "id" : 2};  
    rowstruct = {"mode 1": modestruct};  
    portstruct = {"端口 2": rowstruct};   
    setsweep("s-参数 sweep", "export setup", portstruct);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ deletesweep ](/hc/en-us/articles/360034930173-deletesweep) , [ copysweep ](/hc/en-us/articles/360034930373-copysweep) , [ pastesweep ](/hc/en-us/articles/360034930393-pastesweep) , [ addsweep ](/hc/en-us/articles/360034930413-addsweep) , [ insertsweep ](/hc/en-us/articles/360034930433-insertsweep) , [ getsweep ](/hc/en-us/articles/360034930453-getsweep) , [ addsweepparameter ](/hc/en-us/articles/360034930493-addsweepparameter) , [ addsweepresult ](/hc/en-us/articles/360034410034-addsweepresult) , [ removesweepparameter ](/hc/en-us/articles/360034930513-removesweepparameter) , [ removesweepresult ](/hc/en-us/articles/360034930533-removesweepresult) , [ Sweep scripting commands ](/hc/en-us/articles/360034922893-Sweep-scripting-commands) , [ Optimization scripting commands ](/hc/en-us/articles/360034922973-Optimization-scripting-commands) , [ Monte Carlo scripting commands ](/hc/en-us/articles/360034922993-Monte-Carlo-scripting-commands)
