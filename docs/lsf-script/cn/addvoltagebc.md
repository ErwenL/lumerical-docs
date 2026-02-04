<!--
Translation from English documentation
Original command: addvoltagebc
Translation date: 2026-02-04 22:49:36
-->

# addvoltagebc

添加 一个 新的 voltage 边界条件 到 该 HEAT 求解器 [[Boundary Conditions (Thermal Simulation)](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-)]. A HEAT 求解器 region 必须 为 present 在 该 对象 tree before 一个 electrical contact 边界条件 可以 为 added.

**语法** |  **描述**  
---|---  
addvoltagebc; |  添加 一个 voltage 边界条件 到 该 HEAT 求解器. This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 voltage 边界条件 到 该 CHARGE 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 边界条件.
    
    
    addvoltagebc;  
    ?设置;

**示例 2**

The following 脚本 commands 将 创建 一个 voltage 边界条件 使用 一个 fixed steady state voltage assigned 到 一个 solid named cathode. The 对象 tree 必须 already have 一个 HEAT 求解器 和 一个 geometry named 'cathode' present.
    
    
    addvoltagebc;  
    
    设置("name","cathode");  
    设置("bc mode","steady state");  
    设置("sweep 类型","single");  
    设置("voltage",0.2);  # setting 该 voltage 到 0.2 V  
    设置("surface 类型","solid");  
    设置("solid","cathode");

**示例 3**

The following 脚本 commands 将 创建 一个 steady state voltage 边界条件 named cathode 和 apply 一个 voltage sweep over 一个 predefined 设置 的 voltages. The 对象 tree 必须 already have 一个 HEAT 求解器 和 一个 geometry named 'cathode' present.
    
    
    addvoltagebc;  
    
    设置("name","cathode");  
    设置("bc mode","steady state");  
    设置("sweep 类型","值");  
    
    V = [0, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6];  
    设置("值 table",V);  
    
    设置("surface 类型","solid");  
    设置("solid","cathode");

**示例 4**

The following 脚本 commands 将 设置 up 一个 transient voltage 边界条件 其中 该 voltage 是 0 V at t = 0, steps 到 1 V between t = 1 us 和 1.001 us (tslew = 1 ns), 和 remains at 1 V until t = 10 us. The 边界条件 是 assigned 到 一个 solid named cathode.
    
    
    addvoltagebc;  
    
    设置("name","cathode_trans");  
    设置("bc mode","transient");  
    
    tstep = [0, 1e-6, 1.001e-6, 10e-6];  
    V = [0, 0, 1, 1];  
    
    设置("transient 时间 steps",tstep);  
    设置("transient 值 table",V);  
    设置("surface 类型","solid");  
    设置("solid","cathode");

**参见**

[addconvectionbc](/hc/en-us/articles/360034404854-addconvectionbc), [addradiationbc](/hc/en-us/articles/360034924813-addradiationbc), [addthermalpowerbc](/hc/en-us/articles/360034404874-addthermalpowerbc), [addheatfluxbc](/hc/en-us/articles/360034404894-addheatfluxbc), [addvoltagebc](/hc/en-us/articles/360034404914-addvoltagebc)
