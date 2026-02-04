<!--
Translation from English documentation
Original command: havesweepresult
Translation date: 2026-02-03
-->

# havesweepresult

检查参数扫描/优化/Monte Carlo/S 参数扫描是否有结果。类似于 haveresult。

**语法** |  **描述**
---|---
?havesweepresult;  |  如果有任何扫描、优化、Monte Carlo 分析或 S 参数扫描有结果，则返回 1。如果数据不可用，则返回 0。
?havesweepresult("name");  |  如果指定的扫描、优化、Monte Carlo 或 S 参数扫描有结果，则返回 1。
?havesweepresult("name","data");  |  如果名为 "name" 的扫描、优化、Monte Carlo 或 S 参数扫描有指定的结果 "data"，则返回 1。

**示例**

以下示例显示了 getsweepresult 和 havesweepdata 的输出。请从参数扫描页面下载示例文件并关联文件。

    ?getsweepresult;
    ?havesweepresult("thickness_optimization","fom trend");
    > thickness_sweep
    > thickness_optimization
    > result:
    1

**相关命令**

- [List of commands](./List-of-commands.md)
- [runsweep](./runsweep.md)
- [getsweepresult](./getsweepresult.md)
- [getresult](./getresult.md)
- [haveresult](./haveresult.md)
