<!--
Translation from English documentation
Original command: addmodesource
Translation date: 2026-02-04 01:07:29
-->

# addmodesource

向2.5D varFDTD仿真环境中添加模式源。此命令要求将varFDTD求解器对象设置为活动求解器。

**语法** |  **描述**  
---|---  
addmodesource; |  向varFDTD求解器区域添加模式源。此函数不返回任何数据。  
addmodesource(struct_data);  |  向varFDTD求解器区域添加模式源，并使用包含"属性"和值对的struct设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
   
**示例**

以下脚本命令将向MODE中的varFDTD求解器区域添加模式源并选择注入轴。
    
    
    addmodesource;
    set("injection axis","x");
    set("x",0);
    set("y",0);
    set("y span",5e-6);

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
* [addvarfdtd](https://optics.ansys.com/hc/en-us/articles/360034924193-addvarfdtd)
* [updatesourcemode](https://optics.ansys.com/hc/en-us/articles/360034408754-updatesourcemode)
