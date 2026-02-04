# setsweep

> **原文**: setsweep  
> **翻译日期**: 2026-02-03  
> **翻译状态**: ✅ 已完成

在参数扫描/优化/蒙特卡洛/S参数扫描项中设置属性。

| **语法** | **说明** |
| --- | --- |
| setsweep("name", "property_name", property_value); | 在扫描/优化/蒙特卡洛/S参数项中设置属性。"name"是分析项的绝对名称。"property_name"是在编辑窗口中显示的属性。 |
| ?setsweep("name"); | 查看分析项的可编辑属性。"name"是分析项的绝对名称。 |

对于[参数扫描](./360034922873.md)分析：

| **参数** | **说明** |
| --- | --- |
| property_name = "name" | 设置扫描的名称。 |
| property_name = "solver" | 设置用于扫描的求解器。 |
| property_name = "type" | 设置扫描的类型。"type"的值可以是"Ranges"或"Values" |
| property_name = "number of points" | 设置扫描的点数。默认点数为10。 |
| property_name = "resave files after analysis" | 定义分析后是否重新保存文件。 |

对于[优化](./360034922953.md)分析：

| **参数** | **说明** |
| --- | --- |
| property_name = "name" | 设置优化的名称。 |
| property_name = "algorithm" | "algorithm" = "Particle Swarm", "User Defined" |
| property_name = "maximum generations" | 设置最大代数。 |
| property_name = "reset random generator" | 勾选"重置随机生成"框。 |
| property_name = "type" | "Type" = "Maximum", "Minimum" |
| property_name = "generation size" | 每代的仿真数量。 |
| property_name = "tolerance" | 设置容差值。 |
| property_name = "first generation script" | 在"高级"选项卡中设置"第一代脚本"。 |
| property_name = "next generation script" | 在"高级"选项卡中设置"下一代脚本"。 |
| property_name = "use figure of merit script" | 在"品质因数脚本"选项卡中勾选"使用品质因数"框。 |
| property_name = "figure of merit script" | 在"品质因数脚本"选项卡中设置"品质因数脚本"。 |

对于[蒙特卡洛](./360034403194.md)分析：
| **参数** | **说明** |
| --- | --- |
| property_name = "name" | 设置蒙特卡洛的名称。 |
| property_name = "number of trials" | 设置蒙特卡洛的试验次数。默认试验次数为10。 |
| property_name = "variation" | 设置"Process"或"Mismatch"或"Both"的变化。默认变化为"Both"。 |
| property_name = "seed" | 设置种子。 |
| property_name = "enable seed" | 设置是否启用种子。 |
| property_name = "individual trial" | 设置单个试验号。 |
| property_name = "enable individual trail" | 设置是否启用单个试验。 |
| property_name = "enable spatial correlations" | 设置是否启用空间相关性。 |

对于[S参数矩阵扫描](./360034403214.md)分析：
| **参数** | **说明** |
| --- | --- |
| property_name = "name" | 设置S参数矩阵扫描的名称。 |
| property_name = "excite all ports" | 如果property_value = "true"，扫描将运行与S矩阵设置表中定义的行数一样多的仿真。如果property_value = "false"，则只对S矩阵设置表中选定的行运行仿真。默认值为"true"。 |
| property_name = "calculate group delay" | 启用时，使用相位的导数对频率的有限差分近似数值计算器件的群延迟。 |
| property_name = "invert sign" property_name = "map from" property_name = "active" property_name = "port" property_name = "mode" property_name = "map vector" | 这些属性是为S矩阵设置表选项卡的每一行设置的。要手动设置它们，应该使用[addsweepparameter](./360034930493.md)命令。每个参数的含义可以在关于S参数扫描的知识库文章中找到。一旦添加，行不能被更改，必须先使用[removesweepparameter](./360034930513.md)删除。 |
| property_name = "auto symmetry" | 如果property_value = "true"，则计算并尽可能应用自动对称（参见[S参数矩阵扫描](./360034403214.md)）。如果property_value = "false"，则不更改S参数扫描中的设置。默认值为"false"。注意：对S参数扫描所做的更改不能通过设置property_value = "false"来撤消。当property_value = "false"时，当前扫描中的设置不会改变。 |
| property_name = "export setup" | 此属性设置导出文件的布局，以Lumerical或Touchstone格式导出数据。有两个可能的参数： |

* "auto"：使用自动定义导出表。
* 定义每个端口的自定义结构，请参见下面的示例了解结构应该如何格式化。

对于MODE中的[S参数矩阵扫描](./360034403214.md)分析：
| **参数** | **说明** |
| --- | --- |
| property_name = "name" | 设置S参数矩阵扫描的名称。 |
| property_name = "number of points" | 设置扫描中的点数。 |
| property_name = "calculated group delay" | 设置是否计算群延迟。 |
| property_name = "group delay wavelength" | 设置计算群延迟的波长。除非启用了"计算群延迟"，否则此选项无效。但如果在启用计算之前设置，则在启用选项时将自动应用设置的值。 |
| property_name = "parameter label" | 设置扫描参数的名称。 |
| property_name = "start wavelength" | 设置扫描的起始波长。 |
| property_name = "stop wavelength" | 设置扫描的终止波长。 |
| property_name = "include group delay" | 此属性设置导出文件的布局，以Lumerical或Touchstone格式导出数据。有两个可能的参数： |

* "auto"：使用自动定义导出表。
* 定义每个端口的自定义结构，请参见下面的示例了解结构应该如何格式化。

编辑添加的扫描参数：除了列出的扫描/优化/蒙特卡洛/S参数的默认属性外，任何添加的扫描参数都可以通过将"property_name"设置为参数名来通过setsweep命令编辑。

**示例**

这些示例分别展示了如何设置扫描/优化/蒙特卡洛/S参数的属性。有关详细信息，请参阅应用示例页面[扫描脚本命令](./360034922893.md)。

扫描：
```
addsweep(0);
setsweep("sweep", "name", "thickness_sweep_script");
setsweep("thickness_sweep_script", "type", "Ranges");
setsweep("thickness_sweep_script", "number of points", 10);
```

优化：
```
addsweep(1);
setsweep("optimization", "name", "thickness_optimization_script");
setsweep("thickness_optimization_script", "Type", "Minimize");
setsweep("thickness_optimization_script", "algorithm", "Particle Swarm");
setsweep("thickness_optimization_script", "maximum generations", 20);
setsweep("thickness_optimization_script", "generation size", 10);
setsweep("thickness_optimization_script", "tolerance", 0);
```

蒙特卡洛：
```
addsweep(2);
MC_name = "MC_script";
setsweep("Monte Carlo analysis", "name", MC_name);
setsweep(MC_name, "number of trials", 50);
setsweep(MC_name, "enable seed", 1);
setsweep(MC_name, "seed", 1);
setsweep(MC_name, "Variation", "Both");
```

S参数扫描：
```
addsweep(3);
setsweep("s-parameter sweep", "name", "S sweep");
setsweep("s-parameter sweep", "Excite all ports", 0);
setsweep("S sweep", "auto symmetry", true);
```

此示例在FDTD中定义并设置下图所示设置的导出设置。除"Mode label"、"Mode ID"和"Port location"之外的列不能更改。
```
modestruct = {"label": "mode 1", "id" : 1};
rowstruct = {"mode 1": modestruct, "location": "LEFT"};
portstruct = {"port 2": rowstruct};
setsweep("s-parameter sweep", "export setup", portstruct);
```

此示例在MODE中设置下图所示**第二行**的导出设置。表中的其他行根据仿真域中端口对象的位置自动填充。除"Mode label"和"Mode ID"之外的列不能更改。
```
modestruct = {"label": "my mode 2", "id" : 2};
rowstruct = {"mode 1": modestruct};
portstruct = {"port 2": rowstruct};
setsweep("s-parameter sweep", "export setup", portstruct);
```

**相关命令**

[命令列表](./360037228834.md), [deletesweep](./deletesweep.md), [copysweep](./copysweep.md), [pastesweep](./pastesweep.md), [addsweep](./addsweep.md), [insertsweep](./insertsweep.md), [getsweep](./getsweep.md), [addsweepparameter](./360034930493.md), [addsweepresult](./addsweepresult.md), [removesweepparameter](./360034930513.md), [removesweepresult](./removesweepresult.md), [扫描脚本命令](./360034922893.md), [优化脚本命令](./360034922973.md), [蒙特卡洛脚本命令](./360034922993.md)
