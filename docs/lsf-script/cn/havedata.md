<!--
Translation from English documentation
Original command: havedata
Translation date: 2026-02-03
-->

# havedata

用于检查模拟对象（如监视器）是否有数据。此命令与 haveresult 类似，但旨在与 getdata 命令配合使用，而非 getresult。

**语法** |  **描述**
---|---
havedata;  |  如果任何模拟对象有原始数据，则返回 1；如果没有任何模拟对象有原始数据，则返回 0。
havedata("name");  |  如果 "name" 有原始数据，则返回 1；如果没有原始数据，则返回 0。
havedata("name","data");  |  如果 "name" 有名为 "data" 的原始数据，则返回 1；如果没有该数据，则返回 0。

**示例**

以下示例显示了运行模拟后调用 ?getdata 时的输出。模拟中有一个监视器组，该组具有分析脚本文件和至少一个结果参数。在运行分析脚本之前，监视器组没有数据；运行后，监视器组有存储在结果参数中的数据。

    ?getdata;
    local sources:
     source2
    local monitors:
     monitor group
    ?havedata("monitor group");
    result:
    0
    runanalysis("monitor group");
    ?havedata("monitor group");
    result:
    1

**相关命令**

- [List of commands](./List-of-commands.md)
- [getdata](./getdata.md)
- [haveresult](./haveresult.md)
- [getresult](./getresult.md)
- [copydcard](./copydcard.md)
- [cleardcard](./cleardcard.md)
- [workspace](./workspace.md)
- [havesweepdata](./havesweepdata.md)
