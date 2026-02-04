<!--
Translation from English documentation
Original command: addtemperaturemonitor
Translation date: 2026-02-04 22:49:30
-->

# addtemperaturemonitor

添加 一个 temperature 监视器 到 该 Finite Element IDE 仿真 环境. The 监视器 可以 only 为 added 如果 该 仿真 环境 already has 一个 'HEAT' 或 'CHARGE' (或 both) 求解器 present.

**语法** |  **描述**  
---|---  
addtemperaturemonitor; |  添加 一个 temperature 监视器 到 该 仿真 环境. This format 的 该 命令 是 only application 当 only one 求解器 是 present 在 该 model tree. This 函数 does not 返回 any 数据. If multiple solvers 是 present 那么 use 该 second format  
addtemperaturemonitor("solver_name"); |  This format 的 该 命令 将 添加 一个 temperature 监视器 到 该 求解器 defined 通过 该 参数. The "求解器 name" 将 为 either “CHARGE” 或 “HEAT.” For 该 CHARGE 求解器, 该 temperature 监视器 only works 如果 该 "temperature dependence" 是 设置 到 "non-isothermal" 或 "coupled."  
addtemperaturemonitor(struct_data); |  Adds a temperature monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This format of the command is only application when only one solver is present in the model tree. This function does not return any data.  
addtemperaturemonitor("solver_name", struct_data); |  This format of the command will add a temperature monitor to the solver defined by the argument. The "solver name" will be either “CHARGE” or “HEAT.” Adds a temperature monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example.  This function does not return any data.  
  
**示例**

The following 脚本 命令 将 添加 一个 2D y-normal temperature 监视器 到 该 CHARGE 求解器 region 和 设置 its 维度.
    
    
    addtemperaturemonitor("CHARGE");  
    
    设置("name","Tmap");  
    设置("监视器 类型",6);  # 2D y-normal  
    设置("x",0);  
    设置("x跨度",2e-6);  
    设置("y",0);  
    设置("z",0);  
    设置("z跨度",10e-6);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ 设置 ](/hc/en-us/articles/360034928773-设置) , [ addheatfluxmonitor ](/hc/en-us/articles/360034404414-addheatfluxmonitor)
