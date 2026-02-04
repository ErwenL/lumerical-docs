<!--
Translation from English documentation
Original command: loaddesignkit
Translation date: 2026-02-03
-->

# loaddesignkit

加载设计套件并将其内容定向到用户定义的路径。

**语法** |  **描述**
---|---
loaddesignkit ("name", "path");  |  加载名为"name"的设计套件并将其内容定向到用户定义的"path"。设计套件将在元素库的"设计套件"文件夹中可用。

**示例**

    #loads the design kit "dk" and direct its contents to the path "C:/Users/xxx"
    loaddesignkit("dk", "C:/Users/xxx");

**相关命令**

- [List of commands](./List-of-commands.md)
- [removedesignkit](./removedesignkit.md)
- [reloaddesignkit](./reloaddesignkit.md)
- [enabledesignkit](./enabledesignkit.md)
- [disabledesignkit](./disabledesignkit.md)
- [installdesignkit](./installdesignkit.md)
- [uninstalldesignkit](./uninstalldesignkit.md)
