<!--
Translation from English documentation
Original command: addmaterialproperties
Translation date: 2026-02-04 22:49:29
-->

# addmaterialproperties

添加 一个 (材料) 属性 到 该 选中的 材料 model. A 材料 model (在 该 'materials' folder) 必须 为 选中的 在 该 对象 tree 用于 此 脚本 命令 到 work.

**语法** |  **描述**  
---|---  
addmaterialproperties("material_type","material_name"); |  添加 一个 (材料) 属性 到 该 选中的 材料 model 在 该 对象 tree 在 Finite Element IDE. The 属性 comes 从 one 的 该 材料 databases 在 Finite Element IDE. The "material_type" 参数 selects 该 类型 的 材料 属性 到 为 added. The options 是 "CT" 用于 electrical 属性, "HT" 用于 thermal 属性, 和 "EM" 用于 optical 属性. The "material_name" 参数 defines 该 name 的 该 材料 在 该 appropriate 材料 database whose 属性 将 为 imported. The 函数 does not 返回 any 数据.  
addmaterialproperties("material_type"); |  The "material_type" 参数 selects 该 类型 的 材料 属性 到 为 added. The options 是 "CT" 用于 electrical 属性, "HT" 用于 thermal 属性, 和 "EM" 用于 optical 属性. The 函数 返回 一个 list 的 available 材料 names as 一个 字符串.  
  
**示例**

The following 脚本 commands 将 添加 一个 新的 材料 到 该 对象 tree 在 Finite Element IDE name it, 和 assign optical 属性 到 it 使用 一个 材料 model 在 该 optical 材料 database. The 脚本 将 那么 添加 electrical 和 thermal 属性 到 该 same 材料 使用 一个 appropriate 材料 model 在 该 electrical/thermal 材料 database.
    
    
    addmodelmaterial;
    设置("name","silicon");
    addmaterialproperties("EM","Si (Silicon) - Palik");  # importing 从 optical 材料 database
    select("materials::silicon");
    addmaterialproperties("CT","Si (Silicon)");  # importing 从 electrical 材料 database
    select("materials::silicon");
    addmaterialproperties("HT","Si (Silicon)");  # importing 从 thermal 材料 database

NOTE:  Once 一个 材料 属性 是 assigned 到 该 材料 model 该 selection changes 到 该 对应的 属性. Therefore 该 材料 model 必须 为 re-选中的 before adding 一个 新的 属性 到 it.  
---  
  
**参见**

[ addmodelmaterial ](/hc/en-us/articles/360034404974-addmodelmaterial) , [ addemmaterialproperty ](/hc/en-us/articles/360034924953-addemmaterialproperty) , [ addctmaterialproperty ](/hc/en-us/articles/360034404994-addctmaterialproperty) , [ addhtmaterialproperty ](/hc/en-us/articles/360034924973-addhtmaterialproperty)
