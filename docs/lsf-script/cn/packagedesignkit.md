# packagedesignkit

从自定义库下的现有文件夹创建 .cml 文件。

**语法** | **描述**
---|---
packagedesignkit(name, filename, encrypt, overwrite); | 从名为 'name' 的自定义文件夹创建名为 'filename.cml' 的设计套件文件。如果 'encrypt' = false，则不会加密打包；如果 'encrypt' = true，则打包将被加密。如果 'overwrite' 为 true，它将覆盖同名的现有设计套件文件；如果 'overwrite' 为 false，它将在覆盖之前询问用户确认。'overwrite' 的默认设置为 false。

**示例**

```
# 使用加密打包自定义文件夹中的紧凑模型库
packagedesignkit("dk", "dk.cml", true, true);
```

**另请参阅**

- [命令列表](./命令列表.md)
- [installdesignkit](./installdesignkit.md)
- [importschematic](./importschematic.md)
- [exportschematic](./exportschematic.md)
- [customlibrary](./customlibrary.md)
- [exportlib](./exportlib.md)
- [自定义库和设计套件](./自定义库和设计套件.md)
- [enabledesignkit](./enabledesignkit.md)
- [disabledesignkit](./disabledesignkit.md)
- [installdesignkit](./installdesignkit.md)
- [uninstalldesignkit](./uninstalldesignkit.md)
