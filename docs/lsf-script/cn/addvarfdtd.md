<!--
Translation from English documentation
Original command: addvarfdtd
Translation date: 2026-02-04 09:14:55
-->

# addvarfdtd

向MODE仿真环境中添加2.5D varFDTD求解器区域。

**语法** |  **描述**  
---|---  
addvarfdtd; |  添加2.5D varFDTD仿真区域。此函数不返回任何数据。  
addvarfdtd(struct_data); |  添加2.5D varFDTD仿真区域，并使用包含"属性"和值对的struct设置其属性。此函数不返回任何数据。  
   
**示例**

以下脚本命令将向MODE仿真环境中添加2.5D varFDTD求解器区域，设置其尺寸和仿真时间，然后运行仿真。
    
    
    addvarfdtd;  
    
    set("x",0);  
    set("x span",10e-6);  
    set("y",0);  
    set("y span",10e-6);  
    set("z",0);  
    set("z span",1e-6);  
    set("simulation time",5000e-15);  # 5000 fs  
    
    run;

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [run](https://optics.ansys.com/hc/en-us/articles/360034931333-run)
* [addeme](https://optics.ansys.com/hc/en-us/articles/360034404314-addeme)
* [addfde](https://optics.ansys.com/hc/en-us/articles/360034404294-addfde)
