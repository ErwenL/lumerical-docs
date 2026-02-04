<!--
Translation from English documentation
Original command: loaddata
Translation date: 2026-02-03
-->

# loaddata

从 Lumerical 数据文件 (ldf) 文件加载工作区变量或 d-card 数据。如果存在任何与文件中名称相同的当前变量，当前值将被覆盖。此命令将自动检测 .ldf 文件是否包含 d-card 或脚本工作区数据，并分别将它们加载到 d-card 堆栈或脚本工作区中。

**语法** |  **描述**
---|---
loaddata("filename"); |  从指定文件读取脚本变量数据或 d-card 数据。此函数不返回任何数据。注意：此函数将检查当前工作目录中的文件。如果要读取的文件位于其他目录中，请指定完整路径或更改当前工作目录。

**示例**

加载名为 mydata.ldf 的文件。然后使用工作区和 getdata 命令查看已创建的工作区变量或 d-card。

    filename="mydata";
    loaddata(filename);
    ?workspace;     # view workspace variables
    ?getdata;     # view d-cards (generally the complete set of data from a monitor)

**相关命令**

- [List of commands](./List-of-commands.md)
- [savedata](./savedata.md)
- [savedcard](./savedcard.md)
- [workspace](./workspace.md)
- [load](./load.md)
- [fileexists](./fileexists.md)
