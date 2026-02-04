<!--
Translation from English documentation
Original command: loadelement
Translation date: 2026-02-03
-->

# loadelement

从使用 saveelement 命令在当前工作目录创建的文件加载元素。元素将放置在当前原理图编辑器窗口中。

**语法** |  **描述**
---|---
loadelement ("name");  |  从当前工作目录中扩展名为 ICE 的文件加载元素。

**示例**

    #adds an element star coupler and saves it to an .ice file in the current working directory
    addelement("Star Coupler");
    saveelement("STAR_1");
    #loads the star coupler element "STAR_1.ice" to the schematic editor
    loadelement("STAR_1.ice");
    #change element position in the schematic editor
    set("x position", -200)

**相关命令**

- [List of commands](./List-of-commands.md)
- [library](./library.md)
- [addtolibrary](./addtolibrary.md)
- [probe](./probe.md)
- [saveelement](./saveelement.md)
