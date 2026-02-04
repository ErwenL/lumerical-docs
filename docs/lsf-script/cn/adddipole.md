<!--
Translation from English documentation
Original command: adddipole
Translation date: 2026-02-03 22:28:13
-->

# adddipole

向仿真环境中添加一个 [偶极子源](/hc/en-us/articles/360034382794)。在 MODE 中，此命令要求对象树中存在活动的 varFDTD 求解器区域。

**Syntax** |  **Description**  
---|---  
adddipole; |  向仿真环境中添加一个偶极子源。此函数不返回任何数据。  
adddipole(struct_data); |  添加一个偶极子源，并使用包含“属性”和值对的结构体设置其属性。有关示例，请参阅 [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) 脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将向 FDTD 仿真环境中添加一个偶极子源，并设置其位置。
    
    
    adddipole;
    set("x",0);
    set("y",-1e-6);
    set("z",5e-6);

**参见**

- [set](./set.md)
- [addplane](./addplane.md)
- [addgaussian](./addgaussian.md)
- [addtfsf](./addtfsf.md)
