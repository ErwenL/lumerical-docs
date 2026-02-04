<!--
Translation from English documentation
Original command: addplane
Translation date: 2026-02-04 09:10:55
-->

# addplane

向仿真环境中添加平面波源。

## 适用于FDTD和MODE

**语法** |  **描述**  
---|---  
addplane; |  向仿真环境中添加平面波源。此函数不返回任何数据。  
addplane(struct_data); |  添加平面波源，并使用包含"属性"和值对的struct设置其属性。此函数不返回任何数据。  
   
**示例**

以下脚本命令将在仿真环境中添加一个将沿负z方向传播的平面波源。脚本将设置源的尺寸（和位置）并定义频率范围。
    
    
    addplane;
    set("injection axis","z");
    set("direction","backward");
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",3e-6);
    set("wavelength start",0.3e-6);
    set("wavelength stop",1.2e-6);

## 适用于DGTD：

向有限元IDE中的'DGTD'求解器添加平面波源。此命令要求对象树中存在DGTD求解器区域。

**语法** |  **描述**  
---|---  
addplane; |  向'DGTD'求解器添加平面波源。此函数不返回任何数据。  
   
**示例1**

以下脚本命令将向对象树中已存在的'DGTD'求解器添加平面波源，并打印其所有属性的名称。
    
    
    addplane;?set;

**示例2**

以下脚本命令将向'DGTD'求解器添加平面波源，更改其名称并设置其属性。然后脚本将名为"2D rectangle"的实体设置为注入表面。
    
    
    addplane; 
    set("name","plane_wave");# set the propagation directionset("direction definition","axis");set("direction","backward");set("angle theta",30);set("angle phi",60);
    # set the polarization angleset("polarization angle",90);
    # set the injection surfaceset("surface type","solid");set("solid","2D rectangle");

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
* [addplane](https://optics.ansys.com/hc/en-us/articles/360034924413-addplane)
* [addgaussian](https://optics.ansys.com/hc/en-us/articles/360034404434-addgaussian)
* [addtfsf](https://optics.ansys.com/hc/en-us/articles/360034404454-addtfsf)
* [adddgtdsolver](https://optics.ansys.com/hc/en-us/articles/360034925013-adddgtdsolver)
