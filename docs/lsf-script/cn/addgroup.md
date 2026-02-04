<!--
Translation from English documentation
Original command: addgroup
Translation date: 2026-02-04 22:49:29
-->

# addgroup

添加 一个 容器 group 到 该 仿真 环境. Container groups 可以 为 used 到 put multiple structures, monitors, 和/或 sources together 在 一个 single group 在 该 对象 tree. In Ansys Lumerical Multiphysics™, 容器 groups 是 always children 的 该 求解器 regions 和 cannot contain any 结构. If multiple 求解器 regions 是 present 在 该 Ansys Lumerical Multiphysics 对象 tree, 此 命令 将 添加 一个 容器 group 到 该 求解器 region 该 是 currently 选中的.

**语法** |  **描述**  
---|---  
addgroup; |  添加 一个 容器 group 到 该 仿真 环境.  In Ansys Lumerical Multiphysics, 该 added 容器 group 是 placed under 该 currently 选中的 求解器 region. This 函数 does not 返回 any 数据.  
addgroup(struct_data); |  Adds a container group and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. In Ansys Lumerical Multiphysics, the added container group is placed under the currently selected solver region. This function does not return any data.  
addgroup(“solver_name”); |  Only 用于 Ansys Lumerical Multiphysics. 添加 一个 容器 group 到 该 求解器 region specified 通过 solver_name. This 函数 does not 返回 any 数据.  
  
**示例**

添加 一个 容器 group 到 该 HEAT 求解器 region (在 Ansys Lumerical Multiphysics) 和 put 一个 uniform heat 源 在 it.
    
    
    select("HEAT");
    addgroup;
    设置("name","test_group");
    adduniformheat;
    addtogroup("test_group");

NOTE: In 此 example 脚本, since 该 uniform heat 源 是 also 一个 child 的 该 HEAT 求解器, we do not need 到 specify 该 full path 用于 该 容器 group name (e.g. HEAT::test_group). 

**参见**

[ List 的 commands ](/hc/en-us/articles/360037228834) , [ addtogroup ](/hc/en-us/articles/360034408454-addtogroup) , [ addstructuregroup ](/hc/en-us/articles/360034924093-addstructuregroup) , [ addanalysisgroup ](/hc/en-us/articles/360034404074-addanalysisgroup)
