<!--
Translation from English documentation
Original command: setglobalsource
Translation date: 2026-02-03
-->

# setglobalsource

设置全局光源属性。此命令在分析模式下将返回错误。

**语法** | **描述**
---|----
?setglobalsource; | 返回全局光源属性的列表。
setglobalsource("property",value); | 将名为"property"的全局光源属性设置为 value。此函数不返回任何数据。

**示例**

将全局起始波长设置为 400nm，然后确认值已正确设置。

```lsf
setglobalsource("wavelength start",400e-9);
?getglobalsource("wavelength start");
result:
4e-007
```

**另请参见**

- [set](./set.md)
- [setglobalmonitor](./setglobalmonitor.md)
- [getglobalmonitor](./getglobalmonitor.md)
- [getglobalsource](./getglobalsource.md)
