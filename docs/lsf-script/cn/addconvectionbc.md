<!--
Translation from English documentation
Original command: addconvectionbc
Translation date: 2026-02-03 04:43:53
-->

# addconvectionbc

向 HEAT 或 CHARGE 求解器添加新的对流边界条件 [ [ 边界条件（热仿真） ](/hc/en-us/articles/360034398314-Boundary-Conditions-Thermal-Simulation-) ]。在添加此边界条件之前，对象树中必须存在 HEAT 或 CHARGE 求解器区域。如果两个求解器都存在，则必须将目标求解器的名称作为脚本命令的参数提供。

仅当求解器的温度依赖性设置为 '耦合' 时，才能向 CHARGE 求解器添加对流边界条件。

**Syntax** |  **Description**  
---|---  
addconvectionbc; |  向 HEAT 或 CHARGE 求解器添加对流边界条件（以对象树中存在的求解器为准）。此函数不返回任何数据。  
addconvectionbc("solver_name"); |  向由参数 "solver_name" 定义的所需求解器添加对流边界条件。选项为 "HEAT" 和 "CHARGE"。此函数不返回任何数据。  
  
**Example 1**

以下脚本命令将向对象树中已存在的求解器添加对流边界条件，并打印边界条件的所有可用属性。
    
    
    addconvectionbc;
    ?set;

**Example 2**

以下脚本命令将向对象树中已存在的 HEAT 求解器添加对流边界条件。然后将该边界条件分配给硅和空气之间的界面（表面）。模型设置为常数 h（对流换热系数），h 的值设置为 10 W/m^2-K。环境温度设置为 300 K。
    
    
    addconvectionbc("HEAT");
    set("name","conv_air");
    set("convection model","constant");
    set("ambient temperature",300);
    set("h convection",10);
    set("surface type","material:material");
    set("material 1","Si (Silicon)");
    set("material 2","Air");

注意：对象树中的 'materials' 文件夹必须已包含脚本命令中用于设置边界条件的材料。  
---  
  
**Example 3**

以下脚本命令将向对象树中已存在的 HEAT 求解器添加对流边界条件。该边界条件分配给硅和空气之间的界面（表面）。模型设置为强制对流。流体材料根据材料组合自动选择，长度尺度、流体速度和环境温度由脚本设置。
    
    
    addconvectionbc("HEAT");
    set("name","conv_air");
    set("convection model","forced");
    set("ambient temperature",300);
    set("length scale",1e-3);  # 1 mm
    set("fluid velocity",100);  # m/sec
    set("surface type","material:material");
    set("material 1","Si (Silicon)");
    set("material 2","Air");

**Example 4**

以下脚本命令将向对象树中已存在的 HEAT 求解器添加对流边界条件。该边界条件分配给仿真区域的顶部（+z）表面。模型设置为常数 h（对流换热系数），h 的值设置为 100 W/m^2-K。环境温度设置为 300 K。
    
    
    addconvectionbc("HEAT");
    set("name","conv_top");
    set("convection model","constant");
    set("ambient temperature",300);
    set("h convection",100);
    set("surface type","simulation region");
    set("z max",1);
 
**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [addtemperaturebc](./addtemperaturebc.md)
- [addradiationbc](./addradiationbc.md)
- [addthermalpowerbc](./addthermalpowerbc.md)
- [addheatfluxbc](./addheatfluxbc.md)
- [addthermalinsulatingbc](./addthermalinsulatingbc.md)
- [addvoltagebc](./addvoltagebc.md)
