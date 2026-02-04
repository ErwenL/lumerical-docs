<!--
Translation from English documentation
Original command: addelement
Translation date: 2026-02-03 22:43:00
-->

# addelement

从 INTERCONNECT 元件库向仿真环境中添加一个元件。 

**Syntax** |  **Description**  
---|---  
addelement("element");  |  从元件库添加一个元件。如果未提供元件名称，此命令默认将添加一个复合元件。此函数不返回任何数据。   
  
**示例**

以下脚本命令将向仿真环境中添加一个波导耦合器，并编辑其属性。
    
    
    addelement("Waveguide Coupler");
    eleName = "coupler_1";
    set("name", eleName);
    set("x position", 0); 
    set("y position", 0);
    set("coupling coefficient 1", 0.3);

**参见**

- [set](./set.md)
