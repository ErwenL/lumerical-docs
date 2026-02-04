<!--
Translation from English documentation
Original command: addheatsolver
Translation date: 2026-02-04 00:15:35
-->

# addheatsolver

向仿真环境添加一个[热学（HEAT）求解器区域](/hc/en-us/articles/360034398234)。

**Syntax** |  **Description**  
---|---  
addheatsolver; |  向仿真环境添加热学（HEAT）求解器区域。此函数不返回任何数据。  
addheatsolver(struct_data); |  添加热学（HEAT）求解器区域，并使用包含"property"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将添加一个2D y-normal HEAT求解器区域，设置其尺寸，并运行仿真。该脚本假定仿真环境已设置好几何形状和边界条件。
    
    
    addheatsolver;
    set("solver geometry",1);  #  2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);
    run;

**参见**

- [命令列表](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [run](./run.md)
