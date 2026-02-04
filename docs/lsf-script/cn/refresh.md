<!--
Translation from English documentation
Original command: refresh
Translation date: 2026-02-03
-->

# refresh

此命令重新加载当前项目。

**语法** | **描述**
---|---
refresh; | 重新加载当前项目。这在更改引用元件的 'library' 属性时特别有用。如果修改了 'library' 属性，引用元件必须手动 '刷新' 或重新加载 - 否则用户将不得不保存并重新加载当前项目。

**示例**

```lsf
>setnamed("WG_1","library","::design kits::pdaflow");
>refresh;
```

**另请参见**

- [命令列表](./command_list.md)
