<!--
Translation from English documentation
Original command: addmaterialproperties
Translation date: 2026-02-04 01:03:13
-->

# addmaterialproperties

向选中的材料模型添加材料属性。此脚本命令要求对象树中选中一个材料模型（在'materials'文件夹中）。

**语法** |  **描述**  
---|---  
addmaterialproperties("material_type","material_name"); |  向有限元IDE对象树中选中的材料模型添加材料属性。属性来自有限元IDE中的材料数据库之一。"material_type"参数选择要添加的材料属性类型。选项包括："CT"表示电学属性，"HT"表示热学属性，"EM"表示光学属性。"material_name"参数定义相应材料数据库中材料的名称，其属性将被导入。此函数不返回任何数据。  
addmaterialproperties("material_type"); |  "material_type"参数选择要添加的材料属性类型。选项包括："CT"表示电学属性，"HT"表示热学属性，"EM"表示光学属性。此函数以字符串形式返回可用材料名称列表。  
   
**示例**

以下脚本命令将向有限元IDE的对象树中添加新材料，为其命名，并使用光学材料数据库中的材料模型为其分配光学属性。然后，脚本将使用电学/热学材料数据库中的适当材料模型向同一材料添加电学和热学属性。
    
    
    addmodelmaterial;
    set("name","silicon");
    addmaterialproperties("EM","Si (Silicon) - Palik");  # 从光学材料数据库导入
    select("materials::silicon");
    addmaterialproperties("CT","Si (Silicon)");  # 从电学材料数据库导入
    select("materials::silicon");
    addmaterialproperties("HT","Si (Silicon)");  # 从热学材料数据库导入

**注意**：一旦将材料属性分配给材料模型，选择将更改为相应的属性。因此，在向材料模型添加新属性之前，必须重新选择该材料模型。  
---  
   
**参见**

* [addmodelmaterial](https://optics.ansys.com/hc/en-us/articles/360034404974-addmodelmaterial)
* [addemmaterialproperty](https://optics.ansys.com/hc/en-us/articles/360034924953-addemmaterialproperty)
* [addctmaterialproperty](https://optics.ansys.com/hc/en-us/articles/360034404994-addctmaterialproperty)
* [addhtmaterialproperty](https://optics.ansys.com/hc/en-us/articles/360034924973-addhtmaterialproperty)
