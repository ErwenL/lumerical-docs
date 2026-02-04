# addmodelmaterial

<!-- 翻译说明：本文档已被人工翻译为中文，如有错误请指正 -->
<!-- Translation metadata: manually_translated=true, reviewer=none, last_updated=2026-02-04 -->

向对象树中的"materials"文件夹添加一个空材料模型。然后可以为该材料分配不同的属性（电气、热学或光学）。创建后，该材料可以分配给任何几何体，并可在使用CHARGE、HEAT或DGTD求解器的仿真中使用。

**语法** | **说明**
---|---
addmodelmaterial; | 在Finite Element IDE的对象树中的"materials"文件夹中添加一个新材料。此函数不返回任何数据。
addmodelmaterial(struct_data); | 向"materials"添加新材料并使用包含"property"和value对的struct设置其属性。参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面的示例。此函数不返回任何数据。

**示例**

以下脚本命令将在Finite Element IDE的对象树中添加一个新材料，为其命名，并使用光学材料数据库中的材料模型为其分配光学属性。然后脚本将使用电气/热材料数据库中的适当材料模型为同一材料添加电气和热属性。


    addmodelmaterial;
    set("name","silicon");
    addmaterialproperties("EM","Si (Silicon) - Palik");
    select("materials::silicon");
    addmaterialproperties("CT","Si (Silicon)");
    select("materials::silicon");
    addmaterialproperties("HT","Si (Silicon)");

注意：一旦将材料属性分配给材料模型，选择就会更改为相应的属性。因此，在为其添加新属性之前，必须重新选择材料模型。

---

**另请参阅**

[addmaterialproperties](/hc/en-us/articles/360034924933-addmaterialproperties)
