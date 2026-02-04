<!--
Translation from English documentation
Original command: addimportgen
Translation date: 2026-02-04 00:34:59
-->

# addimportgen

向仿真环境添加一个（光学）生成区域，其中生成分布已导入有限元IDE。此命令要求对象树中存在CHARGE求解器区域。

**Syntax** |  **Description**  
---|---  
addimportgen; |  向仿真环境添加导入生成对象。此函数不返回任何数据。  
addimportgen(struct_data); |  添加导入生成对象，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
创建导入生成对象后，可以通过GUI从matlab（.mat）文件导入光学生成数据，或使用[importdataset](/hc/en-us/articles/360034409114-importdataset)脚本命令将数据集分配给对象。.mat文件必须包含一个3D矩阵G，其中包含矩形网格上的生成数据以及三个坐标向量x、y、z。数据集可以是矩形数据集或非结构化数据集。

**示例**

以下脚本命令将向CHARGE求解器区域添加导入生成对象，并加载分析3D光学生成数据。
    
    
    addimportgen;
    set("name","gen_opt");
    set("x",0);
    set("y",0);
    set("z",0);
    # create coordinate vectors and 3D matrix for doping profile
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    G = matrix(11,2,101) + 1e27;  # assume uniform generation rate of 1e21 /cm3 (1e27 /m3)
    # create dataset
    gen = rectilineardataset("gen",x,y,z);
    gen.addparameter("a",1);  # add a dummy parameter
    gen.addattribute("G",G);
    # load data into doping object
    select("CHARGE::gen_opt");  
    importdataset(gen);

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [linspace](./linspace.md)
- [rectilineardataset](./rectilineardataset.md)
- [select](./select.md)
- [importdataset](./importdataset.md)
- [addbulkgen](./addbulkgen.md)
- [adddeltachargesource](./adddeltachargesource.md)
