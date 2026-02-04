<!--
Translation from English documentation
Original command: addemmaterialproperty
Translation date: 2026-02-04 22:49:29
-->

# addemmaterialproperty

添加 一个 新的 optical 材料 属性 到 该 选中的 材料 model. A 材料 model (在 该 'materials' folder) 必须 为 选中的 在 该 对象 tree 用于 此 脚本 命令 到 work. To 添加 一个 optical 材料 属性 从 该 optical 材料 database, see [ addmaterialproperties ](/hc/en-us/articles/360034924933-addmaterialproperties) . For details 的 optical 材料 models, see [ Optical Material Models ](/hc/en-us/articles/360034398454-Optical-Material-Models) .

**语法** |  **描述**  
---|---  
addemmaterialproperty("property_type"); |  添加 一个 新的 optical 材料 属性 到 该 选中的 材料 model. The "property_type" 参数 可以 为 one 的 该 following:

  * "Conductive"
  * "Dielectric"
  * "(n,k) Material"
  * "Debye"
  * "Plasma"
  * "Lorentz"
  * "Sampled Data 3D"

This 函数 does not 返回 any 数据.  
  
**示例**

The following 脚本 commands 将 添加 一个 新的 材料 到 该 对象 tree 在 Finite Element IDE, 和 assign optical 属性 的 dielectric 到 it.
    
    
    addmodelmaterial;
    addemmaterialproperty("Dielectric");

NOTE:  Once 一个 材料 属性 是 assigned 到 该 材料 model, 该 selection changes 到 该 对应的 属性. Therefore 该 材料 model 必须 为 re-选中的 before adding 一个 新的 属性 到 it.  
---  
  
**参见**

[ addmodelmaterial ](/hc/en-us/articles/360034404974-addmodelmaterial) , [ addmaterialproperties ](/hc/en-us/articles/360034924933-addmaterialproperties) , [ addctmaterialproperty ](/hc/en-us/articles/360034404994-addctmaterialproperty) , [ addhtmaterialproperty ](/hc/en-us/articles/360034924973-addhtmaterialproperty)
