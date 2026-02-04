<!--
Translation from English documentation
Original command: addimplant
Translation date: 2026-02-04 00:24:36
-->

# addimplant

向仿真环境添加一个离子注入掺杂区域。此命令要求对象树中存在CHARGE求解器区域。

**Syntax** |  **Description**  
---|---  
adddimplant; |  在仿真环境中添加离子注入掺杂区域。此函数不返回任何数据。  
adddimplant(struct_data); |  添加离子注入掺杂区域，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将添加一个n型离子注入掺杂对象并设置其属性。注入方向由"surface normal"属性定义，峰值掺杂由"peak concentration"属性定义。
    
    
    addimplant;
    set("name","nwell");
    # set dimension
    V=[-0.5,-0.5;0.5,-0.5;0.5,0.5;-0.5,0.5]*1e-6; # SI unit (m)
    set("vertices",V);
    # set doping profile
    set("dopant type","n");
    set("surface normal","y"); 
    set("source theta",45);
    set("source phi",90);
    set("distribution function","Pearson4");
    set("peak concentration",1e24);  # SI unit (1/m3), equivalent to 1e18 1/cm3

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [adddope](./adddope.md)
