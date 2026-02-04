<!--
Translation from English documentation
Original command: havesweepdata
Translation date: 2026-02-03
-->

# havesweepdata

检查参数扫描/优化/Monte Carlo 分析是否有数据。类似于脚本命令 havedata。

**语法** |  **描述**
---|---
?havesweepdata;  |  如果有任何扫描、优化或 Monte Carlo 分析有数据，则返回 1。如果数据不可用，则返回 0。
?havesweepdata("name");  |  如果指定的扫描、优化或 Monte Carlo 分析有数据，则返回 1。
?havesweepdata("name","data");  |  如果名为 "name" 的指定扫描、优化或 Monte Carlo 分析有指定的数据 "data"，则返回 1。

**示例**

以下示例显示了 getsweepresult 和 havesweepdata 的输出。请从参数扫描页面下载示例文件并关联文件。

    ?getsweepresult;
    ?havesweepdata("thickness_optimization","fom trend");
    > thickness_sweep
    > thickness_optimization
    > result:
    0

**相关命令**

- [List of commands](./List-of-commands.md)
- [runsweep](./runsweep.md)
- [getsweepdata](./getsweepdata.md)
- [getdata](./getdata.md)
- [havedata](./havedata.md)
