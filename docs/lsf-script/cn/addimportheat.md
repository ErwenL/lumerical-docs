<!--
Translation from English documentation
Original command: addimportheat
Translation date: 2026-02-04 22:49:29
-->

# addimportheat

添加 一个 heat 源 到 该 Finite Element IDE 仿真 环境 其中 该 profile 的 该 heat 源 可以 为 imported 从 一个 external 源. For 该 CHARGE 求解器, 该 import heat 源 only 获取 applied 如果 该 "temperature dependence" 是 设置 到 "coupled."

**语法** |  **描述**  
---|---  
addimportheat; |  添加 一个 import primitive 到 define 一个 heat 源. This format 的 该 命令 是 only application 当 only one 求解器 是 present/active 在 该 model tree. This 函数 does not 返回 any 数据. If multiple solvers 是 present 那么 use 该 second 或 fourth format.  
addimportheat("solver_name"); |  This format 的 该 命令 将 添加 一个 import heat 源 到 该 求解器 defined 通过 该 参数. The "求解器 name" 将 为 either “CHARGE” 或 “HEAT.”  
addimportheat(struct_data); |  Adds an import primitive to define a heat source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
addimportheat("solver_name", struct_data); |  This format of the command will add a temperature monitor to the solver defined by the argument. The "solver name" will be either “CHARGE” or “HEAT.” Adds an import primitive to define a heat source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example.  This function does not return any data.  
  
Once 该 import heat 源 是 created, 该 数据 可以 为 imported 从 一个 matlab (.mat) 文件 使用 该 GUI 或 通过 assigning 一个 dataset 到 该 对象 使用 该 [ importdataset ](/hc/en-us/articles/360034409114-importdataset) 脚本 命令. The dataset 可以 为 在 rectilinear 或 unstructured (finite-元素) format.

**示例**

The following 脚本 命令 将 添加 一个 import heat 源 到 该 HEAT 求解器 region 和 将 load 一个 analytic 3D heat 数据 into it.
    
    
    addimportheat("HEAT");
    设置("name","Pin"); 
    # 创建 coordinate vectors 和 3D 矩阵 用于 heat input
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    Q = 矩阵(11,2,101) + 1e15;  # assume 该 heat input 是 1e15 W/m^3 everywhere 
    # 创建 dataset
    heat = rectilineardataset("Pin",x,y,z);
    heat.addparameter("一个",1);  # 添加 一个 dummy 参数
    heat.addattribute("Q",Q); 
    # load 数据 into 源
    select("HEAT::Pin"); 
    importdataset(heat);

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ addemasolver ](/hc/en-us/articles/360034409254-linspace) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ select ](/hc/en-us/articles/360034928593-select) , [ importdataset ](/hc/en-us/articles/360034409114-importdataset) , [ adduniformheat ](/hc/en-us/articles/360034924313-adduniformheat) , [ addimporttemperature ](/hc/en-us/articles/360034924273-addimporttemperature)
