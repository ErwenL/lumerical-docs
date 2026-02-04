<!--
Translation from English documentation
Original command: set
Translation date: 2026-02-03
-->

# set

设置当前选中对象的属性。

请注意，当求解器处于分析模式时，大多数对象无法修改。在这种情况下，此命令将返回错误。

**语法** | **描述**
---|---
?set; | 返回可使用 set 命令更改的选中对象的属性列表。
set("property",value); | 这将设置当前选中对象的属性，包括下拉菜单和复选框。它不能用于设置组中选中对象的值。Value 可以是数字或字符串。此函数不返回任何数据。
set(struct); | 可以使用结构体代替 "property"-value 参数对。
set("property",value,i); | 当选择多个对象时，此形式可用于设置第 i 个选中对象的属性。它不能用于设置组中选中对象的值。对象按其位于对象树中的位置排序。最上方的选中对象被赋予索引 1，索引号随着向下遍历树而增加。

**示例**

将任何具有名为 radius 的属性的选中对象（球体、环、圆）的半径设置为 1e-6。

```lsf
set("radius",1e-6);
```

将所有选中对象的 name 属性设置为 reflection。

```lsf
set("name","reflection");
```

将复选框设置为 0 以取消选中。设置为 1 以选中。

```lsf
set("check box label name",0);  # 取消选择复选框
```

禁用对象。

```lsf
set("enabled",0);
```

将 x min 边界条件设置为下拉菜单中的第一个选项。

```lsf
set("x min bc",1);
```

将 x min 边界条件设置为字符串 "PML"。

```lsf
set("x min bc","PML");
```

设置 FDTD 区域的 PML 配置文件。

```lsf
set("pml profile", 2);
```

为单个边界设置 PML 配置文件。

```lsf
set("same settings on all boundaries",0);
set("pml profile", [1,1,2,1,1,1]); # 将 y min bc 设置为 "stabilized"，所有其他 bc 设置为 "standard"
```

为所有名为 "circle" 的对象的半径增加 2 微米。

```lsf
select("circle");
for (i=1:getnumber) {
 rad=get("radius",i);
 set("radius",rad+2e-6,i);
}
```

设置和获取多边形对象的顶点。我们创建一个半径为 1um 的八边形。

```lsf
addpoly;
theta=linspace(0,2*pi,9);
theta=theta(1:8);
x=cos(theta)*1e-6;
y=sin(theta)*1e-6;
V=[x,y];
set("vertices",V);
?get("vertices");
```

结果：
```
1e-006 0
7.07107e-007 7.07107e-007
6.12323e-023 1e-006
-7.07107e-007 7.07107e-007
-1e-006 1.22465e-022
-7.07107e-007 -7.07107e-007
-1.83697e-022 -1e-006
7.07107e-007 -7.07107e-007
```

查看矩形的属性列表。

```lsf
addrect;
?get;
```

结果（部分）：
```
alpha
color opacity
detail
enabled
first axis
...
```

使用结构体作为输入来设置名为 "rectangle" 的当前选中对象的坐标和尺寸：

```lsf
coordinates = {"x" : -3e-7,
               "x span" : 1e-6,
               "y" : 5e-6,
               "y span" : 1e-5,
               "z" : 1e-7,
               "z span" : 2.2e-7};

set(coordinates);
```

**注意**

在 INTERCONNECT 中，必须在 set 命令中使用固定标准单位输入元件属性值。在某些情况下，标准单位与属性视图中的默认单位不同。以下是一个设置 ONA 中心频率的示例。中心频率的默认单位是 THz，而标准单位是 Hz，使用 set 命令时，值需要以 Hz 为单位：

```lsf
select("ONA");
set("center frequency", 193.1e12);
```

要查找元件属性的标准单位，请在知识页面上打开元件的帮助页面，查看默认单位列。对于默认单位和标准单位不同的情况，会包含一个注释。例如，参见 [ONA](https://optics.ansys.com/hc/en-us/articles/360036617973) 的中心频率。

**另请参见**

- [get](./get.md)
- [setnamed](./setnamed.md)
- [setmaterial](./setmaterial.md)
- [addmaterial](./addmaterial.md)
- [haveproperty](./haveproperty.md)
- [runsetup](./runsetup.md)
- [runanalysis](./runanalysis.md)
