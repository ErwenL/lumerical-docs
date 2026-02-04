<!--
Translation from English documentation
Original command: addfdtd
Translation date: 2026-02-03 23:45:10
-->

# addfdtd

向仿真环境中添加一个[FDTD求解器区域](/hc/en-us/articles/360034382534)。求解器区域的范围决定了FDTD中的仿真体积/面积。

**Syntax** |  **Description**  
---|---  
addfdtd; |  向仿真环境中添加一个FDTD求解器区域。此函数不返回任何数据。  
addfdtd(struct_data); |  添加一个FDTD求解器区域，并使用包含"属性"和值对的结构体设置其属性。有关示例，请参阅[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。  
  
**示例**

以下脚本命令将添加一个3D FDTD求解器区域，设置其维度，并运行仿真。该脚本假设仿真环境已设置好几何结构和源/监视器。
    
    
    addfdtd;
    set("dimension",2);  #  1 = 2D, 2 = 3D
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("z span",10e-6);
    run;

**参见**

- [set](./set.md)
- [run](./run.md)
