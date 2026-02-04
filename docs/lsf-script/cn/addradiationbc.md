<!--
Translation from English documentation
Original command: addradiationbc
Translation date: 2026-02-04 22:49:29
-->

# addradiationbc

添加 一个 新的 radiation 边界条件 到 该 HEAT 或 CHARGE 求解器 [ [ Boundary Conditions (Thermal Simulation) ](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-) ]. A HEAT 或 CHARGE 求解器 region 必须 为 present 在 该 对象 tree before 此 边界条件 可以 为 added. If both solvers 是 present 那么 该 intended 求解器's name 必须 为 provided as 一个 参数 到 该 脚本 命令.

The radiation 边界条件 可以 only 为 added 到 该 CHARGE 求解器 当 该 求解器's temperature dependency 是 设置 到 'coupled'.

**语法** |  **描述**  
---|---  
addradiationbc; |  添加 一个 radiation 边界条件 到 该 HEAT 或 CHARGE 求解器 (whichever 是 present 在 该 对象 tree). This 函数 does not 返回 any 数据.  
addradiationbc("solver_name"); |  添加 一个 radiation 边界条件 到 该 desired 求解器 defined 通过 该 参数 "solver_name". The options 是 "HEAT" 和 "CHARGE". This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 radiation 边界条件 到 该 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 边界条件.
    
    
    addradiationbc;
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 radiation 边界条件 到 该 HEAT 求解器 already present 在 该 对象 tree. The 边界条件 是 那么 assigned 到 该 interface (surfaces) between silicon 和 air. The ambient temperature 是 设置 到 300 K 和 该 emissivity 是 设置 到 0.9.
    
    
    addradiationbc("HEAT");
    设置("name","radiation_air");
    设置("ambient temperature",300);
    设置("emissivity",0.9);
    设置("surface 类型","材料:材料");
    设置("材料 1","Si (Silicon)");
    设置("材料 2","Air");

NOTE:  The 'materials' folder 在 该 对象 tree 必须 already contain 该 materials used 在 该 脚本 commands 到 设置 up 该 边界条件.  
---  
  
**示例 3**

The following 脚本 commands 将 添加 一个 radiation 边界条件 到 该 HEAT 求解器 already present 在 该 对象 tree. The 边界条件 是 assigned 到 该 top (+z) surface 的 该 仿真 region. The ambient temperature 是 设置 到 300 K 和 该 emissivity 是 设置 到 0.9.
    
    
    addradiationbc("HEAT");
    设置("name","radiation_top");
    设置("ambient temperature",300);
    设置("emissivity",0.9);
    设置("surface 类型","仿真 region");
    设置("z最大值",1);

**参见**

[ addtemperaturebc ](/hc/en-us/articles/360034924813-addradiationbc) , [ addconvectionbc ](/hc/en-us/articles/360034404854-addconvectionbc) , [ addthermalpowerbc ](/hc/en-us/articles/360034404874-addthermalpowerbc) , [ addheatfluxbc ](/hc/en-us/articles/360034404894-addheatfluxbc) , [ addthermalinsulatingbc ](/hc/en-us/articles/360034924833-addthermalinsulatingbc) , [ addvoltagebc ](/hc/en-us/articles/360034404914-addvoltagebc)
