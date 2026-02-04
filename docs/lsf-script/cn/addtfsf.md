<!--
Translation from English documentation
Original command: addtfsf
Translation date: 2026-02-04 09:14:25
-->

# addtfsf

向仿真环境中添加全场散射场（TFSF）源。

**语法** |  **描述**  
---|---  
addtfsf; |  向仿真环境中添加全场散射场源。此函数不返回任何数据。  
addtfsf(struct_data); |  添加全场散射场源，并使用包含"属性"和值对的struct设置其属性。此函数不返回任何数据。  
   
**示例**

以下脚本命令将在FDTD仿真环境中添加一个将沿负z方向传播的平面波源。脚本将设置源的尺寸（和位置）并定义频率范围。
    
    
    addtfsf;  
    
    set("injection axis","z");  
    set("direction","backward");  
    set("x",0);  
    set("x span",2e-6);  
    set("y",0);  
    set("y span",5e-6);  
    set("z",3e-6);  
    set("z span",6e-6);  
    set("wavelength start",0.3e-6);  
    set("wavelength stop",1.2e-6);

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
* [addplane](https://optics.ansys.com/hc/en-us/articles/360034924413-addplane)
* [addgaussian](https://optics.ansys.com/hc/en-us/articles/360034404434-addgaussian)
