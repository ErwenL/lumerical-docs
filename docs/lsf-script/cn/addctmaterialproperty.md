<!--
Translation from English documentation
Original command: addctmaterialproperty
Translation date: 2026-02-03 04:55:18
-->

# addctmaterialproperty

向所选材料模型或所选三元合金添加新的电学材料属性。要使此脚本命令正常工作，必须在对象树中选择一个材料模型（位于 'materials' 文件夹中）或三元合金电学材料属性。三元合金不能作为三元合金的组成部分创建。要从电热材料数据库添加电学材料属性，请参阅 [addmaterialproperties](/hc/en-us/articles/360034924933-addmaterialproperties)。有关电学材料模型的详细信息，请参阅 [电学/热学材料模型](/hc/en-us/articles/360034919093-Electrical-Thermal-Material-Models) 或专门关于 [半导体](/hc/en-us/articles/360034919113-Semiconductors) 的页面。

**Syntax** |  **Description**  
---|---  
addctmaterialproperty("property_type"); |  向所选材料模型或所选三元合金添加新的电学材料属性。"property_type" 参数可以是以下之一：

  * "Semiconductor"
  * "Insulator"
  * "Conductor"
  * "Ternary Alloy"

此函数不返回任何数据。  
  
**Example**

以下脚本命令将向 Finite Element IDE 中的对象树添加新材料，并为其分配导体的电学属性。
    
    
    addmodelmaterial;
    addctmaterialproperty("Conductor");

注意：一旦将材料属性分配给材料模型，选择将更改为相应的属性。因此，在向材料模型添加新属性之前，必须重新选择材料模型。  
---  
注意：对于新创建的合金，当第一个基础材料添加到合金时，第二个基础材料也将与第一个材料相同。例如，以下行将创建一个新合金，并将固体材料 "A" 同时分配为合金的基础材料 1 和基础材料 2：
    
    
    addmodelmaterial;
    set("name","test");
    addctmaterialproperty("Ternary Alloy");
    set("name","alloy");
    addctmaterialproperty("Semiconductor");
    set("name","A");  
  
---  
  
**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [addmodelmaterial](./addmodelmaterial.md)
- [addmaterialproperties](./addmaterialproperties.md)
- [addemmaterialproperty](./addemmaterialproperty.md)
- [addhtmaterialproperty](./addhtmaterialproperty.md)
