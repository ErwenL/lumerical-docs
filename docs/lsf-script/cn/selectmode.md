<!--
Translation from English documentation
Original command: selectmode
Translation date: 2026-02-03
-->

# selectmode

从模式列表中选择一个模式。模拟中找到的所有模式都根据其有效指数编号，并在 Eigensolver 分析窗口的模式列表中显示。

**语法** | **描述**
---|---
selectmode(N); | 从模式列表中选择第 N 个模式。
selectmode([N]); | 从标量矩阵参数中选择模式；可以通过在 [N] 中列出多个元素来选择多个模式，例如 [1,2,3]。
selectmode(name); | 选择所需的模式，其中 name 是包含模式名称的字符串。模式命名为 mode1、mode2、..modeN。此形式的命令与 [bestoverlap](./bestoverlap.md) 函数兼容。

**示例**

这两个命令都选择列表中的第三个模式：

```lsf
selectmode(3);
selectmode("mode3");
```

选择第 3、5 和 6 个模式。

```lsf
selectmode([3,5,6]);
```

选择第 2 到 5 个模式以及第 8 个模式。

```lsf
selectmode([[2:5];8]);
```

此命令选择具有与名为 "reference" 的 D-card 最佳重叠的模式。

```lsf
selectmode(bestoverlap("reference"));
```

**另请参见**

- [命令列表](./command_list.md)
- [setanalysis](./setanalysis.md)
- [mesh](./mesh.md)
- [findmodes](./findmodes.md)
- [frequencysweep](./frequencysweep.md)
- [bestoverlap](./bestoverlap.md)
