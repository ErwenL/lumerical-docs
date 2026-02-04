# shiftselect

> **原文**: shiftselect  
> **翻译日期**: 2026-02-03  
> **翻译状态**: ✅ 已完成

与select相同，但不取消选择其他当前选定的对象。注意，只有来自同一"组"的对象才能同时被选择。

| **语法** | **说明** |
| --- | --- |
| shiftselect("name"); | 与select("name")相同，但不取消选择当前选定的对象。可用于选择多个对象。此函数不返回任何数据。 |
| shiftselect("group name::name"); | 与select("groupname::name")相同，但不取消选择当前选定的对象。 |

**示例**

添加两个对象，然后选择两者并平移相同的量。

```
addrect;
set("name","substrate");
addring;# ring自动被选中
shiftselect("substrate");# 选择两个对象
move(0, 1e-6,0); # 两者将在y方向平移1e-6;
```

**相关命令**

[操作对象](./360037228834.md), [groupscope](./groupscope.md)
