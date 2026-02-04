<!--
Translation from English documentation
Original command: addhtmaterialproperty
Translation date: 2026-02-04 22:49:29
-->

# addhtmaterialproperty

添加 一个 新的 thermal 材料 属性 到 该 选中的 材料 model 或 该 选中的 solid alloy. A 材料 model (在 该 'materials' folder) 或 一个 solid alloy thermal 材料 属性 必须 为 选中的 在 该 对象 tree 用于 此 脚本 命令 到 work. A solid alloy 可能 not 为 created as 一个 component 的 一个 solid alloy. To 添加 一个 thermal 材料 属性 从 该 electrothermal 材料 database, see [ addmaterialproperties ](/hc/en-us/articles/360034924933-addmaterialproperties) . For details 的 thermal 材料 models, see [ Electrical/Thermal Material Models ](/hc/en-us/articles/360034919093-Electrical-Thermal-Material-Models) .

**语法** |  **描述**  
---|---  
addhtmaterialproperty("property_type"); |  添加 一个 新的 thermal 材料 属性 到 该 选中的 材料 model 或 该 选中的 solid alloy. The "property_type" 参数 可以 为 one 的 该 following:

  * "Solid"
  * "Solid Alloy"
  * "Fluid"

This 函数 does not 返回 any 数据.  
  
**示例**

The following 脚本 commands 将 添加 一个 新的 材料 到 该 对象 tree 在 Finite Element IDE, 和 assign thermal 属性 的 fluid 到 it.
    
    
    addmodelmaterial;
    addhtmaterialproperty("Fluid");

NOTE:  Once 一个 材料 属性 是 assigned 到 该 材料 model 该 selection changes 到 该 对应的 属性. Therefore 该 材料 model 必须 为 re-选中的 before adding 一个 新的 属性 到 it.  
---  
NOTE:  For 一个 newly created alloy, 当 该 first base 材料 是 added 到 该 alloy, 该 second base 材料 将 also 为 该 same 材料 as 该 first. For example, 该 following lines 将 创建 一个 新的 alloy 和 assign 该 solid 材料 "A" as both base 材料 1 和 base 材料 2 用于 该 alloy:
    
    
    addmodelmaterial;
    设置("name","test");
    addhtmaterialproperty("Solid Alloy");
    设置("name","alloy");
    addhtmaterialproperty("Solid");
    设置("name","A");  
  
---  
  
**参见**

[ addmodelmaterial ](/hc/en-us/articles/360034404974-addmodelmaterial) , [ addmaterialproperties ](/hc/en-us/articles/360034924933-addmaterialproperties) , [ addemmaterialproperty ](/hc/en-us/articles/360034924953-addemmaterialproperty) , [ addctmaterialproperty ](/hc/en-us/articles/360034404994-addctmaterialproperty)
