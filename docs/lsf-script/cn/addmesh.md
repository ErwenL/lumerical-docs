<!--
Translation from English documentation
Original command: addmesh
Translation date: 2026-02-04 01:04:21
-->

# addmesh

向仿真环境中添加网格覆盖区域。网格覆盖区域可用于控制特定区域内的网格大小。在有限元IDE中，此命令要求对象树中存在CHARGE求解器区域。

**语法** |  **描述**  
---|---  
addmesh; |  向仿真环境中添加网格覆盖区域。在有限元IDE中，此命令添加仅适用于'CHARGE'求解器的电学网格。此函数不返回任何数据。  
addmesh(struct_data); |  向仿真环境中添加网格覆盖区域，并使用包含"属性"和值对的struct设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。在有限元IDE中，此命令添加仅适用于'CHARGE'求解器的电学网格。此函数不返回任何数据。  
   
**示例**

以下脚本命令将在FDTD中添加网格覆盖区域，为其命名，设置其尺寸，并设置网格约束。网格对象将设置为仅限制X方向的网格。
    
    
    addmesh;
    set("name","mesh_waveguide");
    # set dimension
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("z span",10e-6);
    # enable in X direction and disable in Y,Z directions
    set("override x mesh",1);
    set("override y mesh",0);
    set("override z mesh",0);
    # restrict mesh by defining maximum step size
    set("set maximum mesh step",1);
    set("dx",5e-9);

**参见**

* [命令列表](https://optics.ansys.com/hc/en-us/articles/360037228834)
* [set](https://optics.ansys.com/hc/en-us/articles/360034928773-set)
