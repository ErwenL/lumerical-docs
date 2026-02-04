<!--
Translation from English documentation
Original command: setactivesolver
Translation date: 2026-02-03
-->

# setactivesolver

将指定的求解器设置为活动求解器。例如，这可用于在 MODE 中的 FDE、varFDTD 和 EME 模拟之间切换。

**语法** | **描述**
---|---
?setactivesolver; | 列出所有可能的求解器选项
setactivesolver('solver_name'); | 将指定名称的求解器设置为活动求解器。

**示例**

如果求解器未设置，此命令将添加它。

```lsf
setactivesolver("EME");
?getactivesolver;
```

结果：
```
EME
```

当 "EME" 求解器已经添加时，此命令将将其设置为活动状态；如果尚未添加，此命令将添加此求解器并将其设置为活动状态。

**另请参见**

- [getactivesolver](./getactivesolver.md)
