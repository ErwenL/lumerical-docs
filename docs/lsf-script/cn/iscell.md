<!--
Translation from English documentation
Original command: iscell
Translation date: 2026-02-03
-->

# iscell

脚本命令检查输入是否为单元格。

**语法** |  **描述**
---|---
value= iscell(input);  |  确定"输入是否为单元格。如果"输入"是单元格，则返回逻辑 1（true），否则返回逻辑 0（false）。

**示例**

    >x=cell(3);
    >?iscell(x);
    result:
    1

**相关命令**

- [issweep](./issweep.md)
- [isstruct](./isstruct.md)
- [isfield](./isfield.md)
