<!--
Translation from English documentation
Original command: addgroup
Translation date: 2026-02-03 23:53:22
-->

# addgroup

向仿真环境中添加一个容器组。容器组可用于将多个结构、监视器和/或源放在对象树中的单个组中。在Ansys Lumerical Multiphysics™中，容器组始终是求解器区域的子级，不能包含任何结构。如果Ansys Lumerical Multiphysics对象树中存在多个求解器区域，此命令将向当前选定的求解器区域添加容器组。

**Syntax** |  **Description**  
---|---  
addgroup; |  向仿真环境中添加一个容器组。在Ansys Lumerical Multiphysics中，添加的容器组放置在当前选定的求解器区域下。此函数不返回任何数据。  
addgroup(struct_data); |  添加一个容器组，并使用包含"属性"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。在Ansys Lumerical Multiphysics中，添加的容器组放置在当前选定的求解器区域下。此函数不返回任何数据。  
addgroup(“solver_name”); |  Only for Ansys Lumerical Multiphysics. Adds a container group to the solver region specified by solver_name. This function does not return any data.  
  
**示例**

向HEAT求解器区域（在Ansys Lumerical Multiphysics中）添加一个容器组，并在其中放置一个均匀热源。
    
    
    select("HEAT");
    addgroup;
    set("name","test_group");
    adduniformheat;
    addtogroup("test_group");

注意：在此示例脚本中，由于均匀热源也是HEAT求解器的子级，我们不需要为容器组名称指定完整路径（例如HEAT::test_group）。

**参见**

- [addtogroup](./addtogroup.md)
- [addstructuregroup](./addstructuregroup.md)
- [addanalysisgroup](./addanalysisgroup.md)
