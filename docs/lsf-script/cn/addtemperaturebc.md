<!--
Translation from English documentation
Original command: addtemperaturebc
Translation date: 2026-02-04 22:49:30
-->

# addtemperaturebc

添加 一个 新的 temperature 边界条件 到 该 HEAT 或 CHARGE 求解器 [[Boundary Conditions (Thermal Simulation)](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-)]. A HEAT 或 CHARGE 求解器 region 必须 为 present 在 该 对象 tree before 此 边界条件 可以 为 added. If both solvers 是 present 那么 该 intended 求解器's name 必须 为 provided as 一个 参数 到 该 脚本 命令. 

The temperature 边界条件 可以 only 为 added 到 该 CHARGE 求解器 当 该 求解器's temperature dependency 是 设置 到 'coupled'. 

**语法** |  **描述**  
---|---  
addtemperaturebc; |  添加 一个 temperature 边界条件 到 该 HEAT 或 CHARGE 求解器 (whichever 是 present 在 该 对象 tree). This 函数 does not 返回 any 数据.  
addtemperaturebc("solver_name"); |  添加 一个 temperature 边界条件 到 该 desired 求解器 defined 通过 该 参数 "solver_name". The options 是 "HEAT" 和 "CHARGE". This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 temperature 边界条件 到 该 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 边界条件.
    
    
    addtemperaturebc;  
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 steady state temperature 边界条件 到 该 HEAT 求解器 already present 在 该 对象 tree. It 将 那么 name 该 边界条件, assign it 到 该 -z 仿真 boundary, 和 sweep 该 temperature 从 300 K 到 400 K 在 5 steps.
    
    
    addtemperaturebc("HEAT");  
    
    设置("name","T_bottom");  
    设置("bc mode","steady state");  
    设置("sweep 类型","range");  
    设置("range start",300);  
    设置("range stop",400);  
    设置("range num points",5);  
    设置("surface 类型","仿真 region");  
    设置("z最小值",1);

**示例 3**

The following 脚本 commands 将 设置 up 一个 transient temperature 边界条件 到 该 HEAT 求解器 其中 该 temperature 是 300 K at t = 0 该 steps 到 400 K between t = 1 us 和 1.1 us (tslew = 0.1 us) 和 remains at 400 K until t = 10 us. The temperature 边界条件 是 assigned 到 一个 surfaces 使用 surface id = 15 和 20.
    
    
    addtemperaturebc("HEAT");  
    
    设置("name","T_trans");  
    设置("bc mode","transient");  
    
    tstep = [0, 1e-6, 1.1e-6, 10e-6];  
    Temp = [300, 300, 400, 400];  
    
    设置("transient 时间 steps",tstep);  
    设置("transient 值 table",Temp);  
    设置("surface 类型","surface");  
    设置("surfaces",[15, 20]);

**参见**

[addconvectionbc](/hc/en-us/articles/360034404854-addconvectionbc), [addradiationbc](/hc/en-us/articles/360034924813-addradiationbc), [addthermalpowerbc](/hc/en-us/articles/360034404874-addthermalpowerbc), [addheatfluxbc](/hc/en-us/articles/360034404894-addheatfluxbc), [addthermalinsulatingbc](/hc/en-us/articles/360034924833-addthermalinsulatingbc), [addvoltagebc](/hc/en-us/articles/360034404914-addvoltagebc)
