<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addvoltagebc -->

# addvoltagebc

**语法** | **描述**
---|---
addvoltagebc; | Adds a voltage 边界 条件 to the HEAT 求解器. This 函数 does not 返回 any data.

**示例**

The following 脚本 commands will add a voltage 边界 条件 to the CHARGE 求解器 already present in the objects tree and print all available properties of the 边界 条件.
    addvoltagebc;  
    ?set;

The following 脚本 commands will create a voltage 边界 条件 with a fixed steady state voltage assigned to a solid named cathode. The objects tree must already have a HEAT 求解器 and a geometry named 'cathode' present.
    addvoltagebc;  
    set("name","cathode");  
    set("bc 模式","steady state");  
    set("sweep type","single");  
    set("voltage",0.2);  # setting the voltage to 0.2 V  
    set("surface type","solid");  
    set("solid","cathode");

The following 脚本 commands will create a steady state voltage 边界 条件 named cathode and apply a voltage sweep over a predefined set of voltages. The objects tree must already have a HEAT 求解器 and a geometry named 'cathode' present.
    addvoltagebc;  
    set("name","cathode");  
    set("bc 模式","steady state");  
    set("sweep type","值");  
    V = [0, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6];  
    set("值 table",V);  
    set("surface type","solid");  
    set("solid","cathode");

The following 脚本 commands will set up a transient voltage 边界 条件 where the voltage is 0 V at t = 0, steps to 1 V between t = 1 us and 1.001 us (tslew = 1 ns), and remains at 1 V until t = 10 us. The 边界 条件 is assigned to a solid named cathode.
    addvoltagebc;  
    set("name","cathode_trans");  
    set("bc 模式","transient");  
    tstep = [0, 1e-6, 1.001e-6, 10e-6];  
    V = [0, 0, 1, 1];  
    set("transient time steps",tstep);  
    set("transient 值 table",V);  
    set("surface type","solid");  
    set("solid","cathode");

The following 脚本 commands will set up a transient voltage 边界 条件 where the voltage is 0 V at t = 0, steps to 1 V between t = 1 us and 1.001 us (tslew = 1 ns), and remains at 1 V until t = 10 us. The 边界 条件 is assigned to a solid named cathode.
    addvoltagebc;  
    set("name","cathode_trans");  
    set("bc 模式","transient");  
    tstep = [0, 1e-6, 1.001e-6, 10e-6];  
    V = [0, 0, 1, 1];  
    set("transient time steps",tstep);  
    set("transient 值 table",V);  
    set("surface type","solid");  
    set("solid","cathode");

**另请参阅**

[addconvectionbc](/hc/en-us/articles/360034404854-addconvectionbc), [addradiationbc](/hc/en-us/articles/360034924813-addradiationbc), [addthermalpowerbc](/hc/en-us/articles/360034404874-addthermalpowerbc), [addheatfluxbc](/hc/en-us/articles/360034404894-addheatfluxbc), [addvoltagebc](/hc/en-us/articles/360034404914-addvoltagebc)
