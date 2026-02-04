<!--
Translation from English documentation
Original command: addimporttemperature
Translation date: 2026-02-04 00:55:21
-->

# addimporttemperature

向CHARGE求解器添加一个导入温度源（仅适用于非等温输运）。导入温度对象可用于为非等温仿真导入温度分布图。要使此命令生效，对象树中必须存在CHARGE求解器区域。

**Syntax** |  **Description**  
---|---  
addimporttemperature; |  向CHARGE求解器添加导入温度源。仅当"temperature dependence"设置为"non-isothermal"时，此源才会生效。此函数不返回任何数据。  
addimporttemperature(struct_data); |  添加导入温度源，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
创建导入温度源后，可以通过GUI从matlab（.mat）文件导入数据，或使用[importdataset](/hc/en-us/articles/360034409114-importdataset)脚本命令将数据集分配给对象。数据集可以是矩形数据集或非结构化（有限元）格式。

**示例**

以下脚本命令将添加导入温度源，并加载分析3D温度数据。
    
    
    addimporttemperature;
    set("name","Tmap");
    # create coordinate vectors and 3D matrix for temperature map
    x = linspace(0,1e-6,11);
    y = linspace(-1e-6,1e-6,2);
    z = linspace(0,2e-6,101);
    T = matrix(11,2,101) + 400;  # assume the temperature is 400 K everywhere
    # create dataset
    temperature = rectilineardataset("temp",x,y,z);
    temperature.addparameter("a",1);  # add a dummy parameter
    temperature.addattribute("T",T);
    # load data into source
    select("CHARGE::Tmap"); 
    importdataset(temperature);

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [linspace](./linspace.md)
- [rectilineardataset](./rectilineardataset.md)
- [select](./select.md)
- [importdataset](./importdataset.md)
- [addimportheat](./addimportheat.md)
