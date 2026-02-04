<!--
Translation from English documentation
Original command: reloaddesignkit
Translation date: 2026-02-03
-->

# reloaddesignkit

从元件库 'Design kits' 文件夹重新加载设计工具包的内容。

**语法** | **描述**
---|---
reloaddesignkit ("name", ["version"]); | 从元件库 'Design kits' 文件夹重新加载名为 'name' 的设计工具包的内容，版本为 'version'。"version" 是可选的，默认为空字符串。

**示例**

```lsf
# 从元件库 'Design kits' 文件夹重新加载版本为 v1.1 的设计工具包 "LCML"
reloaddesignkit("LCML", "v1.1");
```

**另请参见**

- [命令列表](./command_list.md)
- [loaddesignkit](./loaddesignkit.md)
- [removedesignkit](./removedesignkit.md)
- [enabledesignkit](./enabledesignkit.md)
- [disabledesignkit](./disabledesignkit.md)
- [installdesignkit](./installdesignkit.md)
- [uninstalldesignkit](./uninstalldesignkit.md)
