<!-- Translation: updateportmodes -->
<!-- Date: 2026-02-03 -->
<!-- Original: updateportmodes -->

# updateportmodes

在FDTD或MODE的EME求解器中选择所选端口对象中指定的模式，或更新已选择的端口模式。模式由特征求解器模式列表中的模式编号指定。有关FDTD中端口的更多信息，请参见[Ports](./ports.md)。

**语法** | **说明**
---|---
updateportmodes(modes_to_select); | 在所选端口对象中选择指定的模式。如果模式更新成功，此函数返回1；如果更新模式时出错，则返回-1。
updateportmodes; | 更新所选模式端口的模式分布。

**示例**

以下展示了可用于指定要选择模式列表的不同语法。


    # 选择第二个模式
    updateportmodes(2);
    # 选择前10个模式
    updateportmodes(1:10);
    # 选择模式1、2、3、9。注意，列表中指定的第一个模式
    # 如果端口被选为源端口，将用作默认源模式。
    updateportmodes([2,1,3,9]);
    # 更新已选择的模式
    updateportmodes;

以下脚本添加一个FDTD仿真区域和端口，然后设置端口的名称，并选择端口模式和源模式。


    # 添加对象
    addfdtd; # 添加FDTD仿真区域
    addport; # 添加端口
    # 设置端口
    set("name","input_port"); # 设置端口名称
    seteigensolver("bent waveguide",true); # 设置求解器以查找弯曲波导的模式
    seteigensolver("bend radius",10e-6); # 将弯曲半径设置为10 um
    updateportmodes(1:2); # 选择端口的前2个模式
    # 选择端口的第二个模式作为源模式
    select("FDTD::ports"); # 选择端口组
    set("source port","input_port");
    set("source mode","mode 2");

**参见**

[Ports](./ports.md), [addport](./addport.md), [set](./set.md), [geteigensolver](./geteigensolver.md), [seteigensolver](./seteigensolver.md), [clearportmodedata](./clearportmodedata.md)
