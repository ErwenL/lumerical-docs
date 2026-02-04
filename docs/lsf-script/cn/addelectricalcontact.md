<!--
Translation from English documentation
Original command: addelectricalcontact
Translation date: 2026-02-04 22:49:04
-->

# addelectricalcontact

添加 一个 新的 electrical contact 边界条件 到 该 CHARGE 求解器 [ [ Boundary Conditions (Electrical Simulation) ](/hc/en-us/articles/360034918833-Boundary-Conditions-Electrical-Simulation-) ]. A CHARGE 求解器 region 必须 为 present 在 该 对象 tree before 一个 electrical contact 边界条件 可以 为 added.

**语法** |  **描述**  
---|---  
addelectricalcontact; |  添加 一个 electrical contact 边界条件 到 该 CHARGE 求解器. This 函数 does not 返回 any 数据.  
  
**示例 1**

The following 脚本 commands 将 添加 一个 electrical contact 边界条件 到 该 求解器 already present 在 该 对象 tree 和 print all available 属性 的 该 边界条件.
    
    
    addelectricalcontact;
    ?设置;

**示例 2**

The following 脚本 commands 将 创建 一个 electrical 边界条件 使用 一个 fixed steady state voltage assigned 到 一个 solid named cathode. The 对象 tree 必须 already have 一个 CHARGE 求解器 和 一个 geometry named 'cathode' present.
    
    
    addelectricalcontact;
    设置("name","cathode");
    设置("bc mode","steady state");
    设置("sweep 类型","single");
    设置("voltage",0.2);  # setting 该 voltage 到 0.2 V
    设置("surface 类型","solid");
    设置("solid","cathode");

**示例 3**

The following 脚本 commands 将 创建 一个 steady state electrical contact 边界条件 named cathode 和 apply 一个 voltage sweep over 一个 predefined 设置 的 voltages. The 对象 tree 必须 already have 一个 CHARGE 求解器 和 一个 geometry named 'cathode' present.
    
    
    addelectricalcontact;
    设置("name","cathode");
    设置("bc mode","steady state");
    设置("sweep 类型","值");
    V = [0, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6];
    设置("值 table",V);
    设置("surface 类型","solid");
    设置("solid","cathode");

**示例 4**

The following 脚本 commands 将 设置 up 一个 transient electrical contact 边界条件 其中 该 voltage 是 0 V at t = 0, steps 到 1 V between t = 10 ps 和 100 ps (tslew = 90 ps), 和 remains at 1 V until t = 500 ps. The 边界条件 是 assigned 到 一个 solid named cathode.
    
    
    addelectricalcontact;
    设置("name","cathode_trans");
    设置("bc mode","transient");
    tstep = [0, 10e-12, 100e-12, 500e-12];
    V = [0, 0, 1, 1];
    设置("transient voltage 时间 steps",tstep);
    设置("transient voltage table",V);
    设置("surface 类型","solid");
    设置("solid","cathode");

**参见**

[ addsurfacerecombinationbc ](/hc/en-us/articles/360034404814-addsurfacerecombinationbc)
