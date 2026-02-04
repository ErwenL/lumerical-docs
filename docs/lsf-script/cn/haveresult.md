<!--
Translation from English documentation
Original command: haveresult
Translation date: 2026-02-03
-->

# haveresult

用于检查模拟对象（如监视器）是否有结果。

注意：此命令与 havedata 类似，但旨在与 getresult 命令配合使用，而非 getdata。

**语法** |  **描述**
---|---
haveresult;  |  如果任何模拟对象当前有任何结果，则返回 1。
haveresult("name");  |  如果 "name" 有任何结果，则返回 1；否则返回 0。
haveresult("name","data");  |  如果 "name" 有名为 "data" 的结果，则返回 1；否则返回 0。

**示例**

以下示例显示了运行模拟后调用 ?getresult 时的输出。有几个监视器和可用结果的源。

    ?getresult;
    time
    T
    R
    ModeSource
    ?haveresult;  # check if results are available
    result:
    1
    ?haveresult("T"); # check if 'T' has any results
    result:
    1
    ?haveresult("TT"); # check if 'TT' has any results
    result:
    0
    ?haveresult("T","E"); # check if 'T' has a result named 'E'
    result:
    1

**相关命令**

- [List of commands](./List-of-commands.md)
- [getresult](./getresult.md)
- [havedata](./havedata.md)
- [getdata](./getdata.md)
- [copydcard](./copydcard.md)
- [cleardcard](./cleardcard.md)
- [workspace](./workspace.md)
- [havesweepdata](./havesweepdata.md)
