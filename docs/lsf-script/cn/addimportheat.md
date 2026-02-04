<!--
Translation from English documentation
Original command: addimportheat
Translation date: 2026-02-04 00:50:40
-->

# addimportheat

向有限元IDE仿真环境添加一个热源，其中热源的分布可以从外部源导入。对于CHARGE求解器，仅当"temperature dependence"设置为"coupled"时，导入热源才会生效。

**Syntax** |  **Description**  
---|---  
addimportheat; |  添加导入图元以定义热源。此命令格式仅在模型树中只有一个求解器存在/激活时适用。此函数不返回任何数据。如果存在多个求解器，则使用第二或第四种格式。  
addimportheat("solver_name"); |  此命令格式将向参数定义的求解器添加导入热源。"solver name"可以是"CHARGE"或"HEAT"。  
addimportheat(struct_data); |  添加导入图元以定义热源，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
addimportheat("solver_name", struct_data); |  此命令格式将向参数定义的求解器添加温度监视器。"solver name"可以是"CHARGE"或"HEAT"。添加导入图元以定义热源，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
创建导入热源后，可以通过GUI从matlab（.mat）文件导入数据，或使用[importdataset](/hc/en-us/articles/360034409114-importdataset)脚本命令将数据集分配给对象。数据集可以是矩形数据集或非结构化（有限元）格式。

**示例**

以下脚本命令将向HEAT求解器区域添加导入热源，并加载分析3D热数据。
    
    
    addimportheat("HEAT");
    set("name","Pin"); 
    # create coordinate vectors and 3D matrix for heat input
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    Q = matrix(11,2,101) + 1e15;  # assume the heat input is 1e15 W/m^3 everywhere 
    # create dataset
    heat = rectilineardataset("Pin",x,y,z);
    heat.addparameter("a",1);  # add a dummy parameter
    heat.addattribute("Q",Q); 
    # load data into source
    select("HEAT::Pin"); 
    importdataset(heat);

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [addemasolver](./addemasolver.md)
- [rectilineardataset](./rectilineardataset.md)
- [select](./select.md)
- [importdataset](./importdataset.md)
- [adduniformheat](./adduniformheat.md)
- [addimporttemperature](./addimporttemperature.md)
