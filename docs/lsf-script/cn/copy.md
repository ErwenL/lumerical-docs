<!-- Translation completed: 2026-02-04 -->
<!-- Original command: copy -->

# copy

创建选中对象的副本。复制的对象通常是相同的（相同的名称、位置等）。对于必须具有唯一名称的对象，将在名称后附加"_1"。

**语法** | **描述**
---|---
copy; | 复制选中的对象。
copy(dx); | 与copy;相同，但指定了dx的移动。
copy(dx,dy); | 与copy;相同，但指定了dx、dy的移动。
copy(dx,dy,dz); | 与copy;相同，但指定了dx、dy、dz的移动。

**示例**

创建名为substrate的对象的副本。副本将位于原始对象的y方向1um处。

```lsf
addrect;
set("name","substrate");
select("substrate");
copy(0, 1e-6,0);
```

**另请参阅**

[命令列表](List_of_commands.md)、[move](move.md)、[select](select.md)、[cp](cp.md)、[copytoclipboard](copytoclipboard.md)
