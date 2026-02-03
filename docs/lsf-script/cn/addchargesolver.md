<!--
Translation from English documentation
Original command: addchargesolver
Translation date: 2026-02-03
-->

# addchargesolver

向仿真环境添加[电气（CHARGE）求解器区域](/hc/en-us/articles/360034924473)。

**Syntax** | **Description**
---|---
addchargesolver; | 向仿真环境添加电气（CHARGE）求解器区域。此函数不返回任何数据。
addchargesolver(struct_data); | 添加电气（CHARGE）求解器区域，并使用包含"property"和值对的结构体设置其属性。有关示例，请参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面。此函数不返回任何数据。

**Example**

以下脚本命令将添加2D y法向CHARGE求解器区域，设置其尺寸，并运行仿真。该脚本假设仿真环境已经设置了几何形状和边界条件。

    addchargesolver;
    set("solver geometry",1);  # 2D y-normal
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("z",0);
    set("z span",10e-6);
    run;

**参见**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [run](./run.md)