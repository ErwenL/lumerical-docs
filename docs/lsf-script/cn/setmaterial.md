<!--
---
title: setmaterial
command_type: property
---
-->

# setmaterial

设置材料数据库中材料的属性。此命令只能编辑未被写保护的材料属性。

**语法** | **描述**
---|---
`?setmaterial("materialname");` | 显示可修改的指定材料的属性名称。
`setmaterial("materialname", "propertyname", newvalue);` | 将名为"**propertyname**"的材料的属性设置为新值。参数newvalue可以是数字或字符串。参数"**propertyname**"和"**materialname**"必须与正确的字符串完全匹配。例如，`setmaterial("Si", "Mesh order", 4);` 会将材料"Si"的"mesh order"属性设置为4。
`setmaterial("materialname", **_struct_**);` | 使用[struct](struct.md)同时更新多个材料属性。键对应相应的"propertyname"，值设置为新值。

**使用结构体的示例**

```
# 创建一种材料
setmaterial(addmaterial("(n,k) Material"), "name", "myMaterial");

# 设置材料属性
setmaterial("myMaterial", {"Refractive Index": 1.3, "Imaginary Refractive Index": 1.5});
```

**导电材料示例**

此示例添加一种新的导电材料，将名称设置为"myMaterial"，各向异性设置为"Diagonal"，并为材料设置介电常数和电导率属性。

```
A = [4; 5; 6];
B = [1; 2; 3];
temp = addmaterial("Conductive");
setmaterial(temp, "name", "myMaterial");
setmaterial("myMaterial", "Anisotropy", 1); # 启用对角各向异性
setmaterial("myMaterial", "Permittivity", A);
setmaterial("myMaterial", "Conductivity", B);
```

**采样数据材料示例**

此示例演示如何创建新的采样数据材料。

采样数据矩阵必须有2列（各向同性材料）或4列（各向异性材料）。第一列是频率向量，单位为Hz。接下来的列是复值介电常数。

如果您有折射率数据（而不是介电常数），请记住介电常数就是折射率的平方。

```
f = linspace(1000e12, 300e12, 30);  # 频率向量
eps = 2 + 1i * (1e6 / (2 * pi * f * eps0)); # 创建示例介电常数向量
sampledData = [f, eps];  # 将f和eps收集到一个矩阵中
matName = "My material";
temp = addmaterial("Sampled data");
setmaterial(temp, "name", matName);  # 重命名材料
setmaterial(matName, "max coefficients", 2);  # 设置系数数量
setmaterial(matName, "sampled data", sampledData); # 加载采样数据矩阵
```

**折射率扰动材料示例**

此示例演示如何创建新的折射率扰动材料。

折射率扰动材料可以为"np Density"和/或"Temperature"定义折射率扰动。

对于"np Density"折射率扰动：
* "np density model"：接受整数值或字符串值[0, 1, 2]、'Drude'、'Soref and Bennet'或'Custom'
* 对于模型类型"Custom"："n sensitivity table"和"p sensitivity table"接受矩阵参数

对于"Temperature"折射率扰动：
* 对于模型类型"Linear sensitivity"：用户需要为'Tref'、'dn/dt'和'dk/dt'设置单独的值
* 对于模型类型"Table of values"："temperature sensitivity table"接受矩阵参数

```
nSensitivity = [1.5, 1.5e-3, 1.5e-3;  1.6, 1.6e-3, 1.6e-3; 1.7, 1.7e-3, 1.7e-3];
pSensitivity = [1, 1e-3, 1e-3;  1.2, 1.2e-3, 1.2e-3; 1.4, 1.4e-3, 1.4e-3];
matName = "May material";
temp = addmaterial("Index perturbation");
setmaterial(temp, "name", matName);
setmaterial(matName, "np density model", "Custom"); # 使用"Custom"模型类型
setmaterial(matName, "n sensitivity table", nSensitivity); # 设置n敏感度表
setmaterial(matName, "p sensitivity table", pSensitivity); # 设置p敏感度表
```

可以使用命令行定义材料的颜色。下面显示了一个示例。这些脚本命令将创建材料、定义材料颜色，并将该材料分配给矩形以显示颜色变化。

新颜色值矩阵中的4个元素分别代表颜色的红色、绿色、蓝色和alpha通道。这些元素可以设置为0到1之间的值，代表从0到255的最大值。Alpha定义不透明度，设置为0表示透明，1表示纯色。例如，[1;0;0;1]是纯色红色，[0;1;0;1]是纯色绿色，[0;0;1;1]是纯色蓝色。可以使用在线颜色选择工具找到更多的颜色通道值。

注意，颜色不透明度也可以在结构对象中通过覆盖材料属性来定义。

```
mymaterial = addmaterial("PEC");
setmaterial(mymaterial, "name", "test_material");
setmaterial("test_material", "color", [1; 0.6; 0.4; 0.3]); # R、G、B、alpha通道
addrect;
set("material", "test_material");
set("override color opacity from material database", 0);
```

**另请参阅**

- [命令列表](list-of-commands.md), [addmaterial](addmaterial.md), [deletematerial](deletematerial.md), [getmaterial](getmaterial.md), [getindex](getindex.md), [getfdtdindex](getfdtdindex.md), [导入任意色散材料](importing-arbitrary-dispersive-material.md)
