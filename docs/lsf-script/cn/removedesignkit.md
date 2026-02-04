<!--
Translation from English documentation
Original command: removedesignkit
Translation date: 2026-02-03
-->

# removedesignkit

从元件库 'Design kits' 文件夹中删除现有的设计工具包。

**语法** | **描述**
---|---
removedesignkit("name", ["version"]); | 从元件库 'Design kits' 文件夹中删除名为 'name' 的设计工具包，版本为 'version'。"version" 是可选的，默认为空字符串。

**示例**

```lsf
# 从元件库 'Design kits' 文件夹中删除版本为 v1.1 的设计工具包 "LCML"
removedesignkit("LCML", "v1.1");
```

**另请参见**

- [命令列表](./command_list.md)
- [loaddesignkit](./loaddesignkit.md)
- [reloaddesignkit](./reloaddesignkit.md)
- [enabledesignkit](./enabledesignkit.md)
- [disabledesignkit](./disabledesignkit.md)
- [installdesignkit](./installdesignkit.md)
- [uninstalldesignkit](./uninstalldesignkit.md)
