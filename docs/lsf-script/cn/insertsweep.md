<!--
Translation from English documentation
Original command: insertsweep
Translation date: 2026-02-03
-->

# insertsweep

将扫描/优化/Monte Carlo 项目作为现有分析项目的父项插入。现有项目成为新插入扫描的子项。

**语法** |  **描述**
---|---
insertsweep("name"); |  将扫描/优化/Monte Carlo 项目作为父分析项目的子项插入。"name" 是现有分析项目的绝对名称。

**示例**

    addsweep(0);
    insertsweep("sweep");

**相关命令**

- [List of commands](./List-of-commands.md)
- [deletesweep](./deletesweep.md)
- [copysweep](./copysweep.md)
- [pastesweep](./pastesweep.md)
- [addsweep](./addsweep.md)
- [getsweep](./getsweep.md)
- [setsweep](./setsweep.md)
- [addsweepparameter](./addsweepparameter.md)
- [addsweepresult](./addsweepresult.md)
- [removesweepparameter](./removesweepparameter.md)
- [removesweepresult](./removesweepresult.md)
