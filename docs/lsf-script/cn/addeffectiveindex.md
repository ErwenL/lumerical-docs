<!--
Translation from English documentation
Original command: addeffectiveindex
Translation date: 2026-02-03 22:36:29
-->

# addeffectiveindex

向仿真环境中添加一个 [有效折射率监视器](/hc/en-us/articles/360034396454)。此命令要求存在活动的 varFDTD 求解器区域。

**Syntax** |  **Description**  
---|---  
addeffectiveindex; |  向 varFDTD 求解器区域添加一个有效折射率监视器。此函数不返回任何数据。  
addeffectiveindex(struct_data); |  添加一个有效折射率监视器，并使用包含“属性”和值对的结构体设置其属性。有关示例，请参阅 [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) 脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将向仿真区域添加一个有效折射率监视器，并设置其尺寸。
    
    
    addeffectiveindex;
    set("name","neff");
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("y span",5e-6);

**参见**

- [set](./set.md)
