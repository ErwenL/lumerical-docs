<!--
Translation from English documentation
Original command: addfieldregion
Translation date: 2026-02-03 23:48:57
-->

# addfieldregion

向仿真环境中添加一个[field region object](https://optics.ansys.com/hc/en-us/articles/36967414684947-Field-Region-Simulation-object)（场区域对象）。场区域对象与lumopt一起使用，有关更多信息，请参阅知识库文章[Getting started with lumopt](https://optics.ansys.com/hc/en-us/articles/360050995394-Getting-Started-with-lumopt-Python-API)。

**Syntax** |  **Description**  
---|---  
addfieldregion; |  向仿真环境中添加一个场区域对象。此函数不返回任何数据。  
addfieldregion(struct_data); |  添加一个场区域对象，并使用包含"属性"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**参见**

- [set](./set.md)
- [addplane](./addplane.md)
- [addgaussian](./addgaussian.md)
- [addtfsf](./addtfsf.md)
- [adddipole](./adddipole.md)
- [adddftmonitor](./adddftmonitor.md)
