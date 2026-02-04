<!--
Translation from English documentation
Original command: setglobalmonitor
Translation date: 2026-02-03
-->

# setglobalmonitor

设置全局监视器属性。此命令在分析模式下将返回错误。

**语法** | **描述**
---|----
?setglobalmonitor; | 返回全局监视器属性的列表。
setglobalmonitor("property",value); | 将名为"property"的全局监视器属性设置为 value。此函数不返回任何数据。

**示例**

将全局监视频率点数设置为 11，然后确认值已正确设置。

```lsf
setglobalmonitor("frequency points",11);
?getglobalmonitor("frequency points");
result:
11
```

**另请参见**

- [set](./set.md)
- [getglobalmonitor](./getglobalmonitor.md)
- [setglobalsource](./setglobalsource.md)
- [getglobalsource](./getglobalsource.md)
