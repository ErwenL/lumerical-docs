<!--
Translation from English documentation
Original command: installdesignkit
Translation date: 2026-02-03
-->

# installdesignkit

将设计套件文件安装到设计套件文件夹。

**语法** |  **描述**
---|---
installdesignkit(filename, path, overwrite); |  安装名为 'filename.cml' 的设计套件文件，并将其内容定向到用户定义的 'path'。设计套件将在元素库的"设计套件"文件夹中可用。如果 'overwrite' 为 true，它将覆盖具有相同名称的现有设计套件；如果 'overwrite' 为 false，它将在覆盖之前询问用户确认。

**示例**

    #installs the "dk.cml" library to the Design Kits folder
    installdesignkit("dk.cml", "C:/Users/xxx", true);

**相关命令**

- [List of commands](./List-of-commands.md)
- [packagedesignkit](./packagedesignkit.md)
- [enabledesignkit](./enabledesignkit.md)
- [disabledesignkit](./disabledesignkit.md)
- [uninstalldesignkit](./uninstalldesignkit.md)
- [importschematic](./importschematic.md)
- [exportschematic](./exportschematic.md)
- [customlibrary](./customlibrary.md)
- [exportlib](./exportlib.md)
