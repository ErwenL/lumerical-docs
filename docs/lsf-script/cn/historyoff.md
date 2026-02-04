<!--
Translation from English documentation
Original command: historyoff
Translation date: 2026-02-03
-->

# historyoff

禁用为当前对象树（非 INTERCONNECT）/原理图（INTERCONNECT）拍摄快照（历史记录）以实现撤销重做功能。

在 INTERCONNECT 中运行联合模拟或每次运行大量操作的多个模拟时（例如使用 lumopt），此选项将提高模拟性能。

**语法** |  **描述**
---|---
historyoff; |  禁用为当前对象树（非 INTERCONNECT）/原理图（INTERCONNECT）拍摄快照（历史记录）以实现撤销重做功能。

**示例**

    historyoff;

**相关命令**

- [Manipulating objects](./Manipulating-objects.md)
- [undo](./undo.md)
- [redo](./redo.md)
- [historyon](./historyon.md)
