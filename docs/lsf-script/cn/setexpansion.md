<!--
Translation from English documentation
Original command: setexpansion
Translation date: 2026-02-03
-->

# setexpansion

将 DFT 监视器与模式扩展监视器关联。

**语法** | **描述**
---|----
?setexpansion; | 列出所选模式扩展监视器的"扩展监视器"列表中的所有监视器。
setexpansion("name", "dft_monitor"); | 将"dft_monitor"添加到所选模式扩展监视器的"扩展监视器"列表中，并指定名称。

**示例**

请从环形谐振器示例中打开 ring_resonator.fsp 并执行以下操作。

```lsf
?setexpansion;
drop2 ::model::drop2
in ::model::in
through ::model::through
drop ::model::drop
```

它显示了要扩展的所有四个 DFT 监视器。

对于同一文件，输入

```lsf
setexpansion("test", "in");
```

然后 DFT 监视器"in"将以"test"的名称添加到"expansion"监视器的列表中。

输入 removeexpansion("test")，则"test"将从列表中删除。

**另请参见**

- [addmodeexpansion](./addmodeexpansion.md)
- [removeexpansion](./removeexpansion.md)
