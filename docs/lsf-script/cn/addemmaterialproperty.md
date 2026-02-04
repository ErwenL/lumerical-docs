<!--
Translation from English documentation
Original command: addemmaterialproperty
Translation date: 2026-02-03 23:03:35
-->

# addemmaterialproperty

向选定的材料模型添加一个新的光学材料属性。此脚本命令要求对象树中已选定材料模型（在'materials'文件夹中）。要从光学材料数据库添加光学材料属性，请参阅[addmaterialproperties](/hc/en-us/articles/360034924933-addmaterialproperties)。有关光学材料模型的详细信息，请参阅[Optical Material Models](/hc/en-us/articles/360034398454-Optical-Material-Models)。

**Syntax** |  **Description**  
---|---  
addemmaterialproperty("property_type"); | 向选定的材料模型添加一个新的光学材料属性。"property_type"参数可以是以下之一：

  * "Conductive"
  * "Dielectric"
  * "(n,k) Material"
  * "Debye"
  * "Plasma"
  * "Lorentz"
  * "Sampled Data 3D"

此函数不返回任何数据。
  
**示例**

以下脚本命令将在有限元IDE中向对象树添加新材料，并为其分配电介质光学属性。
    
    
    addmodelmaterial;
    addemmaterialproperty("Dielectric");

注意：一旦材料属性被分配给材料模型，选择将更改为相应的属性。因此，在向材料模型添加新属性之前，必须重新选择该材料模型。
---
  
**参见**

- [addmodelmaterial](./addmodelmaterial.md)
- [addmaterialproperties](./addmaterialproperties.md)
- [addctmaterialproperty](./addctmaterialproperty.md)
- [addhtmaterialproperty](./addhtmaterialproperty.md)
