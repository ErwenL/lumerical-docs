<!--
Translation from English documentation
Original command: addfde
Translation date: 2026-02-03 23:05:16
-->

# addfde

向MODE仿真环境中添加一个[Finite Difference Eigenmode (FDE) solver region object](/hc/en-us/articles/360034916973)（有限差分本征模求解器区域对象）。

**Syntax** |  **Description**  
---|---  
addfde; |  向仿真环境中添加一个FDE求解器区域。此函数不返回任何数据。  
addfde(struct_data); |  添加一个FDE求解器区域，并使用包含"属性"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将在XY平面上添加一个FDE求解器区域并计算本征模。
    
    
    addfde;
    set("solver type",3);  
    set("x",0);  
    set("x span",2e-6);  
    set("y",0);  
    set("y span",5e-6);  
    set("z",0);
    findmodes;

**参见**

- [set](./set.md)
- [findmodes](./findmodes.md)
- [addvarfdtd](./addvarfdtd.md)
- [addeme](./addeme.md)
