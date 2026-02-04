<!--
Translation from English documentation
Original command: addhtmaterialproperty
Translation date: 2026-02-04 00:17:00
-->

# addhtmaterialproperty

向选定的材料模型或选定的固体合金添加新的热学材料属性。要使此脚本命令生效，必须在对象树中选定一个材料模型（位于'materials'文件夹中）或一个固体合金热学材料属性。固体合金不能作为另一个固体合金的组分创建。要从电热材料数据库添加热学材料属性，请参阅[addmaterialproperties](/hc/en-us/articles/360034924933-addmaterialproperties)。有关热学材料模型的详细信息，请参阅[电气/热学材料模型](/hc/en-us/articles/360034919093-Electrical-Thermal-Material-Models)。

**Syntax** |  **Description**  
---|---  
addhtmaterialproperty("property_type"); |  向选定的材料模型或选定的固体合金添加新的热学材料属性。"property_type"参数可以是以下之一：

  * "Solid"
  * "Solid Alloy"
  * "Fluid"

此函数不返回任何数据。  
  
**示例**

以下脚本命令将在有限元IDE的对象树中添加新材料，并为其分配流体热学属性。
    
    
    addmodelmaterial;
    addhtmaterialproperty("Fluid");

NOTE:  一旦将材料属性分配给材料模型，选择将更改为相应的属性。因此，在向材料模型添加新属性之前，必须重新选择该材料模型。  
---  
NOTE:  对于新创建的合金，当第一种基础材料添加到合金时，第二种基础材料也将与第一种相同。例如，以下行将创建一个新合金，并将固体材料"A"同时分配为该合金的基础材料1和基础材料2：
    
    
    addmodelmaterial;
    set("name","test");
    addhtmaterialproperty("Solid Alloy");
    set("name","alloy");
    addhtmaterialproperty("Solid");
    set("name","A");  
  
---  
  
**参见**

- [addmodelmaterial](./addmodelmaterial.md)
- [addmaterialproperties](./addmaterialproperties.md)
- [addemmaterialproperty](./addemmaterialproperty.md)
- [addctmaterialproperty](./addctmaterialproperty.md)
