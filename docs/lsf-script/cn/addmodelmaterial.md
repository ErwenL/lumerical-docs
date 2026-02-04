<!--
Translation from English documentation
Original command: addmodelmaterial
Translation date: 2026-02-04 22:49:29
-->

# addmodelmaterial

添加 一个 empty 材料 model 到 该 'materials' folder 在 该 对象 tree. Different 属性 (electrical, thermal, 或 optical) 可以 那么 为 assigned 到 该 材料. Once created 该 材料 可以 为 assigned 到 any geometry 和 为 used 在 simulations 使用 该 CHARGE, HEAT, 或 DGTD solvers.

**语法** |  **描述**  
---|---  
addmodelmaterial; |  添加 一个 新的 材料 到 该 'materials' folder 在 该 对象 tree 在 Finite Element IDE. This 函数 does not 返回 any 数据.  
addmodelmaterial(struct_data); |  Adds a new material to the 'materials' and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**示例**

The following 脚本 commands 将 添加 一个 新的 材料 到 该 对象 tree 在 Finite Element IDE, name it, 和 assign optical 属性 到 it 使用 一个 材料 model 在 该 optical 材料 database. The 脚本 将 那么 添加 electrical 和 thermal 属性 到 该 same 材料 使用 一个 appropriate 材料 model 在 该 electrical/thermal 材料 database.
    
    
    addmodelmaterial;
    设置("name","silicon");
    addmaterialproperties("EM","Si (Silicon) - Palik");
    select("materials::silicon");
    addmaterialproperties("CT","Si (Silicon)");
    select("materials::silicon");
    addmaterialproperties("HT","Si (Silicon)");

NOTE:  Once 一个 材料 属性 是 assigned 到 该 材料 model 该 selection changes 到 该 对应的 属性. Therefore 该 材料 model 必须 为 re-选中的 before adding 一个 新的 属性 到 it.  
---  
  
**参见**

[ addmaterialproperties ](/hc/en-us/articles/360034924933-addmaterialproperties)
