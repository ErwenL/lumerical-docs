<!--
Translation from English documentation
Original command: renameport
Translation date: 2026-02-03
-->

# renameport

为复合或脚本元件重命名端口。

**语法** | **描述**
---|---
renameport("element name", "old port name", "new port name"); | 为复合或脚本元件重命名端口。

**示例**

```lsf
#将元件 "COMPOUND_1" 的端口名称 "port 1" 重命名为 "port a"
renameport("COMPOUND_1", "port 1", "port a");
```

**另请参见**

- [命令列表](./command_list.md)
- [packagedesignkit](./packagedesignkit.md)
- [installdesignkit](./installdesignkit.md)
- [importschematic](./importschematic.md)
- [exportschematic](./exportschematic.md)
- [customlibrary](./customlibrary.md)
- [removecustom](./removecustom.md)
- [exportlib](./exportlib.md)
