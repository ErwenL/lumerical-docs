# addcustom

<!-- 翻译说明：本文档已被人工翻译为中文，如有错误请指正 -->
<!-- Translation metadata: manually_translated=true, reviewer=none, last_updated=2026-02-04 -->

在仿真环境中添加一个[自定义图元](/hc/en-us/articles/360036620233)。自定义图元是通过方程描述物理对象边界的对象。

**语法** | **说明**
---|---
addcustom; | 在仿真环境中添加一个自定义图元。此函数不返回任何数据。
addcustom(struct_data); | 添加自定义图元并使用包含"property"和value对的struct设置其属性。参见[struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command)脚本命令页面的示例。此函数不返回任何数据。

**示例**

以下脚本命令将在XY平面中创建一个半径为0.5微米的半圆，并沿Z轴拉伸它。


    addcustom;
    set("create 3D object by","extrusion");#  y = sqrt(0.5^2-(x-0.5)^2)
    set("equation 1","sqrt("+num2str(0.5)+"^2-(x-"+num2str(0.5)+")^2)");  
    set("x span",1e-6);
    set("y span",1e-6);
    set("z span",2e-6);

同样的方程可以通过旋转半圆而不是拉伸它来创建半球。


    addcustom;
    set("create 3D object by","revolution");#  y = sqrt(0.5^2-(x-0.5)^2)
    set("equation 1","sqrt("+num2str(0.5)+"^2-(x-"+num2str(0.5)+")^2)");  
    set("x span",1e-6);
    set("y span",1e-6);
    set("z span",2e-6);

**另请参阅**

[命令列表](/hc/en-us/articles/360037228834) , [set](/hc/en-us/articles/360034928773-set)
