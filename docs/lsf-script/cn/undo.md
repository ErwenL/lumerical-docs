<!-- Translated: 2026-02-03 -->
<!-- Original: undo -->

# undo

撤销最后一条修改任何对象的命令，您可以撤销最后 5 条命令。

**语法** | **描述**
---| ---
undo; | 撤销最后一条修改对象命令。此函数不返回任何数据。

**示例**

如果您手动添加一些对象或像这样在提示符中逐行输入命令

```lsf
addplane;
addrect;
addring;
addcircle;
addpower;
addfdtd;
```

然后输入 undo 5 次或更多次，它将只删除最后 5 个对象。第一个添加的平面波源被保留。

如果输入 redo 5 次或更多次，它将只恢复最后 5 个对象。

**另见**

[操作对象](./manipulating-objects.md)、[redo](./redo.md)、[historyon](./historyon.md)、[historyoff](./historyoff.md)
