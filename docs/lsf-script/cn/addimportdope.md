<!--
Translation from English documentation
Original command: addimportdope
Translation date: 2026-02-04 00:28:59
-->

# addimportdope

向仿真环境添加一个[掺杂区域](/hc/en-us/articles/360034398054)，可用于加载自定义掺杂分布。自定义掺杂分布可以通过脚本分析创建，也可以从其他来源（如工艺仿真）导入。此命令要求对象树中存在CHARGE求解器区域。

**Syntax** |  **Description**  
---|---  
addimportdope; |  向仿真环境添加导入掺杂区域。此函数不返回任何数据。  
addimportdope(struct_data); |  添加导入掺杂区域，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
创建导入掺杂对象后，可以通过GUI从matlab（.mat）文件导入掺杂数据，或使用[importdataset](/hc/en-us/articles/360034409114-importdataset)脚本命令将数据集分配给对象。数据集可以是矩形数据集或非结构化数据集。可以使用[数据集构建器](/hc/en-us/articles/360034901713-Dataset-builder)从其他工具（如工艺仿真）将掺杂数据导入求解器工作空间。

**示例**

以下脚本命令将向CHARGE求解器区域添加导入掺杂对象，并加载分析3D掺杂数据。
    
    
    addimportdope;
    set("name","pepi");
    set("x",0);
    set("y",0);
    set("z",0);
    # create coordinate vectors and 3D matrix for doping profile
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    N = matrix(11,2,101) + 1e21;  # assume uniform doping concentration of 1e15 /cm3 (1e21 /m3)
    # create dataset
    doping = rectilineardataset("dope",x,y,z);
    doping.addparameter("a",1);  # add a dummy parameter
    doping.addattribute("N",N);
    # load data into doping object
    select("CHARGE::pepi");
    importdataset(doping);

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [linspace](./linspace.md)
- [rectilineardataset](./rectilineardataset.md)
- [select](./select.md)
- [importdataset](./importdataset.md)
- [adddope](./adddope.md)
- [adddiffusion](./adddiffusion.md)
