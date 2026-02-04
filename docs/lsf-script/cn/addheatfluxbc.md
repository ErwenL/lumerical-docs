<!--
Translation from English documentation
Original command: addheatfluxbc
Translation date: 2026-02-04 22:49:29
-->

# addheatfluxbc

添加 一个 新的 heat flux 边界条件 到 该 HEAT 或 CHARGE 求解器 [ [ Boundary Conditions (Thermal Simulation) ](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-) ]. A HEAT 或 CHARGE 求解器 region 必须 为 present 在 该 对象 tree before 此 边界条件 可以 为 added. If both solvers 是 present 那么 该 intended 求解器's name 必须 为 provided as 一个 参数 到 该 脚本 命令.

The heat flux 边界条件 可以 only 为 added 到 该 CHARGE 求解器 当 该 求解器's temperature dependency 是 设置 到 'coupled'.

**语法** |  **描述**  
---|---  
addheatfluxbc; |  添加 一个 heat flux 边界条件 到 该 HEAT 或 CHARGE 求解器 (whichever 是 present 在 该 对象 tree). This 函数 does not 返回 any 数据.  
addheatfluxbc("solver_name"); |  添加 一个 heat flux 边界条件 到 该 desired 求解器 defined 通过 该 参数 "solver_name". The options 是 "HEAT" 和 "CHARGE". This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 heat flux 边界条件 到 该 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 边界条件.
    
    
    addheatfluxbc;
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 steady state heat flux 边界条件 到 该 HEAT 求解器 already present 在 该 对象 tree. It 将 那么 name 该 边界条件, assign it 到 该 -x 仿真 region boundary, 和 设置 该 heat flux 到 1e6 W/m^2.
    
    
    addheatfluxbc("HEAT");
    设置("name","P_in");
    设置("heat flux",1e6);
    设置("surface 类型","仿真 region");
    设置("x最小值",1);

**参见**

[ addtemperaturebc ](/hc/en-us/articles/360034404894-addheatfluxbc) , [ addconvectionbc ](/hc/en-us/articles/360034404854-addconvectionbc) , [ addradiationbc ](/hc/en-us/articles/360034924813-addradiationbc) , [ addthermalpowerbc ](/hc/en-us/articles/360034404874-addthermalpowerbc) , [ addthermalinsulatingbc ](/hc/en-us/articles/360034924833-addthermalinsulatingbc) , [ addvoltagebc ](/hc/en-us/articles/360034404914-addvoltagebc)
