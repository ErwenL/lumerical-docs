<!--
Translation from English documentation
Original command: isstruct
Translation date: 2026-02-03
-->

# isstruct

脚本命令检查输入是否为结构体。

**语法** |  **描述**
---|---
value= isstruct(input);  |  确定"输入"是否为结构体。如果"输入"是结构体，则返回逻辑 1（true），否则返回逻辑 0（false）。

**示例**

    >x=struct;
    >?isstruct(x);
    result:
    1

**相关命令**

- [issweep](./issweep.md)
- [iscell](./iscell.md)
- [isfield](./isfield.md)
