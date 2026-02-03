<!--
Translation from English documentation
Original command: adddeltachargesource
Translation date: 2026-02-03 10:50:10
-->

# adddeltachargesource

向仿真环境中添加一个 [delta optical generation source](/hc/en-us/articles/360034398094)。此命令要求对象树中存在 CHARGE 求解器区域。

**Syntax** |  **Description**  
---|---  
adddeltachargesource; |  向仿真环境中添加一个 delta 光学生成源。此函数不返回任何数据。  
adddeltachargesource(struct_data); |  添加一个 delta 光学生成源，并使用包含“属性”和值对的结构体设置其属性。有关示例，请参阅 [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) 脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将添加一个 delta 光学生成源，设置其位置，并通过定义净电子-空穴对电流（/秒）来设置生成速率。
    
    
    adddeltachargesource;
    set("name","delta");
    set("x",0);
    set("y",0);
    set("z",5e-6);
    set("source type",2);  #  ehp current
    set("ehp current",1e12);  # net ehp current I_ehp = e*1e12 Amp

**参见**

- [List of commands](./list-of-commands.md)
- [set](./set.md)
- [addimportgen](./addimportgen.md)
- [addbulkgen](./addbulkgen.md)
