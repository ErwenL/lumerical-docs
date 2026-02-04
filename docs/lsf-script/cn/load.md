<!--
Translation from English documentation
Original command: load
Translation date: 2026-02-03
-->

# load

加载模拟项目文件。如果模拟已运行，该文件也将包含模拟结果。

**语法** |  **描述**
---|---
load(filename);  |  加载模拟文件。此函数不返回任何数据。

**示例**

加载模拟项目文件。

    filename="simulation.fsp";
    load(filename); # load the file in the current working directory
    load("C:\Downloads\project_name.fsp") # load the file in a path specified

**相关命令**

- [List of commands](./List-of-commands.md)
- [loaddata](./loaddata.md)
- [save](./save.md)
- [savedata](./savedata.md)
- [savedcard](./savedcard.md)
- [fileexists](./fileexists.md)
- [dir](./dir.md)
