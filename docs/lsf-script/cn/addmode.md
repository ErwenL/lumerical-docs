<!--
Translation from English documentation
Original command: addmode
Translation date: 2026-02-04 01:05:20
-->

# addmode

为FDTD向仿真环境中添加模式源。对于MODE，向仿真环境中添加本征模（FDE）求解器区域。

**注意**：'addmode'命令在MODE中已弃用，将在未来版本中移除。请参考[addfde](https://optics.ansys.com/hc/en-us/articles/360034404294-addfde)作为替代。  
---  
**语法** |  **描述**  
---|---  
addmode; |  对于FDTD：向仿真环境中添加模式源。此函数不返回任何数据。  
addmode; |  对于MODE：向仿真环境中添加本征模求解器。  
addmode(struct_data); |  添加模式源（在FDTD中使用）或本征模求解器（在MODE中使用），并使用包含"属性"和值对的struct设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
   
**示例**

以下脚本命令将在FDTD中添加模式源并设置其尺寸和注入轴。
    
    
    addmode;
    set("injection axis","x");
    set("x",0);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("z span",10e-6);

以下脚本命令将在MODE中的XY平面上添加本征模（FDE）求解器区域并计算本征模。
    
    
    addmode;
    set("solver type",3);
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    findmodes;

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
* [updatesourcemode](https://optics.ansys.com/hc/en-us/articles/360034408754-updatesourcemode)
* [findmodes](https://optics.ansys.com/hc/en-us/articles/360034405214-findmodes)
