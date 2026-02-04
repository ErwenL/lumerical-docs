# farfieldsettings

设置远场计算中"远场设置"窗口可用的参数。要获取远场设置的可用参数，如下所示，右键单击频域场监视器并可视化远场。然后选择"远场设置"。

**语法** | **描述**
---|---
farfieldsettings("property", value); | 设置远场计算的远场滤波器设置。这些设置应用于所有远场投影。值可以是数字或字符串。此函数不返回任何数据。

**示例**

```powershell
farfieldsettings("far field filter",0.2);farfieldsettings("override near field mesh",1);
farfieldsettings("near field samples per wavelength",5);
```

**另请参阅**

[命令列表](../命令列表.md)、[farfield2d](./farfield2d.md)、[farfield3d](./farfield3d.md)、[farfieldfilter](./farfieldfilter.md)、[setanalysis](./setanalysis.md)（用于 FDE 中的远场设置）