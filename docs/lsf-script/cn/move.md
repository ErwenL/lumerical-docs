# move

移动选定的对象。

**语法** | **描述**
---|---
move(dx); | 在 2D 或 3D 中移动 dx
move(dx,dy); | 在 2D 或 3D 中移动 dx 和 dy。此函数不返回任何数据。
move(dx,dy,dz); | 在 3D 中移动 dx、dy 和 dz。在 2D 中，dz 将被忽略。

**示例**

将名为 substrate 的对象在 z 方向移动 1um。

```
addrect;
set("name","substrate");
select("substrate");
move(0, 1e-6,0);
```

**另请参阅**

- [操作对象](./操作对象.md)
- [copy](./copy.md)
- [select](./select.md)
