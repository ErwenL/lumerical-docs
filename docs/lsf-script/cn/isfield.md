<!--
Translation from English documentation
Original command: isfield
Translation date: 2026-02-03
-->

# isfield

脚本命令检查输入是否为字段。

**语法** |  **描述**
---|---
value= isfield(input, field);  |  确定"输入是否包含字段名"field"。如果"输入"包含"field"，则返回逻辑 1（true），否则返回逻辑 0（false）。

**示例**

    >x=struct;
    >x.t=10;
    >?isfield(x,'t');
    result:
    1

**相关命令**

- [issweep](./issweep.md)
- [isstruct](./isstruct.md)
- [iscell](./iscell.md)
- [getfield](./getfield.md)
- [setfield](./setfield.md)
