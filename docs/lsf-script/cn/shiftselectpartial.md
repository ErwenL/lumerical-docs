# shiftselectpartial

> **原文**: shiftselectpartial  
> **翻译日期**: 2026-02-03  
> **翻译状态**: ✅ 已完成

与selectpartial相同，但不取消选择其他当前选定的对象。

| **语法** | **说明** |
| --- | --- |
| shiftselectpartial("partialname"); | 与selectpartial("partialname")相同，但不取消选择当前选定的对象。可用于选择多个对象。此函数不返回任何数据。 |
| shiftselectpartial("partialgroupname::partialname"); | 与selectpartial("partialgroupname::partialname")相同，但不取消选择当前选定的对象。可用于选择多个对象。 |

**示例**

选择具有不同部分名称的2个对象。

```
addrect;
set("name","substrate_1");
addrect;
set("name","pattern_1");
unselectall;
shiftselectpartial("substrate");
shiftselectpartial("pattern");
```

**相关命令**

[操作对象](./360037228834.md), [groupscope](./groupscope.md)
