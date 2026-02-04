<!--
Translation from English documentation
Original command: setexpression
Translation date: 2026-02-03
-->

# setexpression

脚本命令将所选元件的指定属性设置为指定的表达式。

**语法** | **描述**
---|----
setexpression(name,p,expr); | 将元件'name'的属性'p'设置为表达式'expr'。

**示例**

要为名为"Straight Waveguide_1"的波导设置标签为温度"%Temp%"，请使用以下脚本：

```lsf
setexpression("Straight Waveguide_1","temperature","%Temp%");
```

**另请参见**

- [autoarrange](./autoarrange.md)
- [addproperty](./addproperty.md)
- [createcompound](./createcompound.md)
