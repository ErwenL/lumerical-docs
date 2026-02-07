<!--
Translation 从 English documentation
Original 命令: addctmaterialproperty
Translation date: 2026-02-04 23:30:10
-->

# addctmaterialproperty

添加 一个 新的 electrical 材料 属性 到 该 选中的 材料 model 或 该 选中的 ternary alloy。 A 材料 model (在 该 'materials' folder) 或 一个 ternary alloy electrical 材料 属性 必须 为 选中的 在 该 对象 tree 用于 此 脚本 命令 到 work。 A ternary alloy 可能 not 为 created as 一个 component 的 一个 ternary alloy。 To 添加 一个 electrical 材料 属性 从 该 electrothermal 材料 database， see [ addmaterialproperties ](/hc/en-us/articles/360034924933-addmaterialproperties) 。 For details 的 electrical 材料 models， see [ Electrical/Thermal Material Models ](/hc/en-us/articles/360034919093-Electrical-Thermal-Material-Models) 或 该 page specifically about [ Semiconductors](/hc/en-us/articles/360034919113-Semiconductors)。

**语法** | **描述**
---|---
addctmaterialproperty("property_type"); | 添加 一个 新的 electrical 材料 属性 到 该 选中的 材料 model 或 该 选中的 ternary alloy。 The "property_type" 参数 可以 为 one 的 该 following:

* "Semiconductor"
* "Insulator"
* "Conductor"
* "Ternary Alloy"

This 函数 does not 返回any 数据。

**示例**

The following 脚本 commands 将 添加 一个 新的 材料 到 该 对象 tree 在 Finite Element IDE， 和 assign electrical 属性 的 conductor 到 it。


    addmodelmaterial;
    addctmaterialproperty("Conductor");

NOTE: Once 一个 材料 属性 是 assigned 到 该 材料 model 该 selection changes 到 该 对应的 属性。 Therefore 该 材料 model 必须 为 re-选中的 before adding 一个 新的 属性 到 it。
---
NOTE: For 一个 newly created alloy， 当 该 first base 材料 是 added 到 该 alloy， 该 second base 材料 将 also 为 该 same 材料 as 该 first。 For example， 该 following lines 将 创建 一个 新的 alloy 和 assign 该 solid 材料 "A" as both base 材料 1 和 base 材料 2 用于 该 alloy:


    addmodelmaterial;
    设置("name","test");
    addctmaterialproperty("Ternary Alloy");
    设置("name","alloy");
    addctmaterialproperty("Semiconductor");
    设置("name","A");  

---

**参见**

- [List 的 commands](../lsf-脚本-commands-alphabetical.md)
- [addmodelmaterial](./addmodelmaterial.md)
- [addmaterialproperties](./addmaterialproperties.md)
- [addemmaterialproperty](./addemmaterialproperty.md)
- [addhtmaterialproperty](./addhtmaterialproperty.md)
