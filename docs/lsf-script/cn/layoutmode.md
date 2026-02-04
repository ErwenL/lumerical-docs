<!--
Translation from English documentation
Original command: layoutmode
Translation date: 2026-02-03
-->

# layoutmode

此脚本命令可用于确定模拟文件当前处于布局模式还是分析模式。重要的是在打开项目文件后立即使用此命令检查状态，以避免在后续操作中遇到错误（如果文件不在所需模式下）。

**语法** |  **描述**
---|---
?layoutmode;  |  如果处于布局模式（INTERCONNECT 为设计模式），则返回 1；如果处于分析模式，则返回 0。

**示例**

以下脚本命令将首先加载名为 "test.fsp" 的项目文件。脚本的目的是向现有几何体添加新矩形。但是，如果文件处于分析模式，则 "addrect" 命令将产生错误。为避免这种情况，脚本命令 "layoutmode" 首先用于确定文件的状态。然后使用 "if/else" 语句：如果文件已处于布局模式，则直接添加矩形；或者如果文件处于分析模式，则先切换到布局模式后再添加矩形。

    load("test.fsp");
    status = layoutmode;

    if (status == 1) {
       addrect;
    }
    else {
       switchtolayout;
       addrect;
    }

**相关命令**

- [List of commands](./List-of-commands.md)
- [switchtolayout](./switchtolayout.md)
- [designmode](./designmode.md)
