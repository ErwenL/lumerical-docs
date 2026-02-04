<!--
Translation from English documentation
Original command: seteigensolver
Translation date: 2026-02-03
-->

# seteigensolver

FDTD 和 MODE 中的模式光源、模式扩展监视器和端口，以及 EME 中的每个独立单元都有嵌入式本征求解器。此脚本命令可以在不使用图形界面的情况下设置本征求解器的属性。

使用此命令更改嵌入式本征求解器的任何值将自动使任何现有的模式数据失效。这意味着在使用此命令后，基于与前一个模式的重叠计算的新更新将失败。因此，请在调用 updatesourcemode 或 updatemodes 之前先调用此命令。

**语法** | **描述**
---|----
?seteigensolver; | 返回嵌入式本征求解器属性的列表。
seteigensolver("property",value); | 这将设置当前选中对象的本征求解器属性。Value 可以是数字或字符串。此函数不返回任何数据。

**示例**

1. 更改模式扩展计算的曲率半径，并计算前 10 个模式，这些模式随后可用于模式扩展。请在 MODE 中使用 varFDTD 求解器打开环形谐振器示例中的 ring_resonator2.lms：

```lsf
select("expansion");

seteigensolver("bent waveguide",true);
seteigensolver("bend radius",10e-6);
updatemodes(1:10);
```

2. 在 EME 中更改单元 1 的试探模式数量：

```lsf
select("EME::Cells::cell_1");
seteigensolver("number of trial modes",25);
```

另请参见 addmodeexpansion 和 addport 脚本函数中的示例。

**另请参见**

- [addmode](./addmode.md)
- [addmodeexpansion](./addmodeexpansion.md)
- [addport](./addport.md)
- [clearsourcedata](./clearsourcedata.md)
- [clearmodedata](./clearmodedata.md)
- [clearportmodedata](./clearportmodedata.md)
- [expand](./expand.md)
- [geteigensolver](./geteigensolver.md)
- [updatemodes](./updatemodes.md)
- [updatesourcemode](./updatesourcemode.md)
- [updateportmodes](./updateportmodes.md)
