<!--
Translation from English documentation
Original command: addindex
Translation date: 2026-02-04 00:57:14
-->

# addindex

向仿真环境添加一个折射率监视器。在MODE中，需要存在活动的varFDTD区域才能使此命令生效。

**Syntax** |  **Description**  
---|---  
addindex; |  向仿真环境添加折射率监视器。此函数不返回任何数据。  
addindex(struct_data); |  添加折射率监视器，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将向仿真区域添加一个2D y-normal折射率监视器并设置其尺寸。
    
    
    addindex;
    set("name","index_monitor");
    set("monitor type",2);  # 2D y-normal
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("z",10e-6);
    set("z span",5e-6);

在FDTD中，如果存在求解器区域，折射率监视器会自动保存结果而无需运行仿真。以下脚本命令将在上述脚本之后添加求解器区域，并可视化折射率预览。
    
    
    addfdtd;
    n = getresult("index_monitor","index preview");
    visualize(n);

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [addfdtd](./addfdtd.md)
- [addvarfdtd](./addvarfdtd.md)
- [getresult](./getresult.md)
- [visualize](./visualize.md)
