<!--
Translation from English documentation
Original command: addthermalpowerbc
Translation date: 2026-02-04 22:49:36
-->

# addthermalpowerbc

添加 一个 新的 thermal power 边界条件 到 该 HEAT 或 CHARGE 求解器 [[Boundary Conditions (Thermal Simulation)](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-)]. A HEAT 或 CHARGE 求解器 region 必须 为 present 在 该 对象 tree before 此 边界条件 可以 为 added. If both solvers 是 present 那么 该 intended 求解器's name 必须 为 provided as 一个 参数 到 该 脚本 命令. 

The thermal power 边界条件 可以 only 为 added 到 该 CHARGE 求解器 当 该 求解器's temperature dependency 是 设置 到 'coupled'. 

**语法** |  **描述**  
---|---  
addthermalpowerbc; |  添加 一个 thermal power 边界条件 到 该 HEAT 或 CHARGE 求解器 (whichever 是 present 在 该 对象 tree). This 函数 does not 返回 any 数据.  
addthermalpowerbc("solver_name"); |  添加 一个 thermal power 边界条件 到 该 desired 求解器 defined 通过 该 参数 "solver_name". The options 是 "HEAT" 和 "CHARGE". This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 thermal power 边界条件 到 该 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 边界条件.
    
    
    addthermalpowerbc;  
    ?设置;

**示例 2**

The following 脚本 commands 将 添加 一个 steady state thermal power 边界条件 到 该 HEAT 求解器 already present 在 该 对象 tree. It 将 那么 name 该 边界条件, assign it 到 该 solid named 'heater', 和 sweep 该 power 从 1 mW 到 10 mW 在 5 steps.
    
    
    addthermalpowerbc("HEAT");  
    
    设置("name","P_in");  
    设置("bc mode","steady state");  
    设置("sweep 类型","range");  
    设置("range start",1e-3);  
    设置("range stop",10e-3);  
    设置("range num points",5);  
    设置("surface 类型","solid");  
    设置("solid","heater");

**示例 3**

The following 脚本 commands 将 设置 up 一个 transient thermal power 边界条件 到 该 HEAT 求解器 其中 该 power applied 到 该 solid 'heater' 是 设置 到 0 W at t = 0. The power input 那么 steps 从 0 W 到 1 mW between t = 1 us 到 t = 1.1 us (tslew = 0.1 us). The power input 是 那么 kept at 1 mW until 10 us.
    
    
    addthermalpowerbc("HEAT");  
    
    设置("name","P_heater");  
    设置("bc mode","transient");  
    
    tstep = [0, 1e-6, 1.1e-6, 10e-6];  
    Pin = [0, 0, 1e-3, 1e-3];  
    
    设置("transient 时间 steps",tstep);  
    设置("transient 值 table",Pin);  
    设置("surface 类型","solid");  
    设置("solid","heater");

**参见**

[addtemperaturebc](/hc/en-us/articles/360034404874-addthermalpowerbc), [addconvectionbc](/hc/en-us/articles/360034404854-addconvectionbc), [addradiationbc](/hc/en-us/articles/360034924813-addradiationbc), [addheatfluxbc](/hc/en-us/articles/360034404894-addheatfluxbc), [addthermalinsulatingbc](/hc/en-us/articles/360034924833-addthermalinsulatingbc), [addvoltagebc](/hc/en-us/articles/360034404914-addvoltagebc)
