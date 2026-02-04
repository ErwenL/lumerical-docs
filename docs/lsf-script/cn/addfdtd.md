<!-- Translation completed: 2026-02-04 -->
<!-- Original command: addfdtd -->

# addfdtd

添加FDTD求解器区域到仿真环境。求解器区域的范围决定了FDTD中的仿真体积。

**语法** | **描述**
---|---
addfdtd; | 添加FDTD求解器区域到仿真环境。此函数不返回任何数据。
addfdtd(struct_data); | 添加FDTD求解器区域并使用包含"property"和value对的struct设置其属性。有关示例，请参阅[struct](struct.md)脚本命令页面。此函数不返回任何数据。

**示例**

以下脚本命令将添加3D FDTD求解器区域，设置其维度并运行仿真。脚本假设仿真环境已经设置了几何体和光源/监视器。

```lsf
addfdtd;
set("dimension",2);  # 1 = 2D, 2 = 3D
set("x",0);
set("x span",2e-6);
set("y",0);
set("y span",5e-6);
set("z",0);
set("z span",10e-6);
run;
```

**另请参阅**

[命令列表](List_of_commands.md)、[set](set.md)、[run](run.md)
