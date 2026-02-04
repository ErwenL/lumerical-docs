<!--
Translation from English documentation
Original command: addfieldregion
Translation date: 2026-02-04 22:49:29
-->

# addfieldregion

Adds a [field region object](https://optics.ansys.com/hc/en-us/articles/36967414684947-Field-Region-Simulation-object) to the simulation environment. The field region object is used with lumopt, see the Knowledge Base article on [Getting started with lumopt](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API) for more information.

**语法** |  **描述**  
---|---  
addfieldregion; |  添加 一个 field region 对象 到 该 仿真 环境. This 函数 does not 返回 any 数据.  
addfieldregion(struct_data); |  Adds a field region object and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example.  This function does not return any data.  
  
**参见**

[List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834), [set ](https://optics.ansys.com/hc/en-us/articles/360034928773-set), [addplane ](https://optics.ansys.com/hc/en-us/articles/360034924413-addplane), [addgaussian ](https://optics.ansys.com/hc/en-us/articles/360034404434-addgaussian), [addtfsf](https://optics.ansys.com/hc/en-us/articles/360034404454-addtfsf), [adddipole](https://optics.ansys.com/hc/en-us/articles/360034924393-adddipole-Script-command), [adddftmonitor](https://optics.ansys.com/hc/en-us/articles/36957320687763-adddftmonitor-Script-command)
