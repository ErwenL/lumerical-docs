<!--
Translation from English documentation
Original command: addheatfluxbc
Translation date: 2026-02-03 23:55:57
-->

# addheatfluxbc

向HEAT或CHARGE求解器添加一个新的热通量边界条件[[Boundary Conditions (Thermal Simulation)](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-)]。在添加此边界条件之前，对象树中必须存在HEAT或CHARGE求解器区域。如果两个求解器都存在，则必须将目标求解器的名称作为脚本命令的参数提供。

只有当求解器的温度依赖性设置为'coupled'时，热通量边界条件才能添加到CHARGE求解器。

**Syntax** |  **Description**  
---|---  
addheatfluxbc; |  向HEAT或CHARGE求解器（对象树中存在的那个）添加热通量边界条件。此函数不返回任何数据。  
addheatfluxbc("solver_name"); |  向由参数"solver_name"定义的所需求解器添加热通量边界条件。选项为"HEAT"和"CHARGE"。此函数不返回任何数据。  
  
**示例1**

以下脚本命令将向对象树中已存在的求解器添加热通量边界条件，并打印边界条件的所有可用属性。
    
    
    addheatfluxbc;
    ?set;

**示例2**

以下脚本命令将向对象树中已存在的HEAT求解器添加稳态热通量边界条件。然后命名边界条件，将其分配给-x仿真区域边界，并将热通量设置为1e6 W/m^2。
    
    
    addheatfluxbc("HEAT");
    set("name","P_in");
    set("heat flux",1e6);
    set("surface type","simulation region");
    set("x min",1);

**参见**

- [addtemperaturebc](./addtemperaturebc.md)
- [addconvectionbc](./addconvectionbc.md)
- [addradiationbc](./addradiationbc.md)
- [addthermalpowerbc](./addthermalpowerbc.md)
- [addthermalinsulatingbc](./addthermalinsulatingbc.md)
- [addvoltagebc](./addvoltagebc.md)
