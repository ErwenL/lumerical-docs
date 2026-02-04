<!--
Translation from English documentation
Original command: removesweepresult
Translation date: 2026-02-03
-->

# removesweepresult

从扫描/优化/Monte Carlo 项中删除结果。

**语法** | **描述**
---|---
removesweepresult("name", "result_name"); | 从扫描/优化/Monte Carlo 项中删除结果。"name" 是分析项的绝对名称。

**示例**

此示例展示了如何从扫描中删除结果。请从[参数扫描](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)页面下载示例文件。

```lsf
removesweepresult("thickness_sweep", "T");
```

**另请参见**

- [命令列表](./command_list.md)
- [copysweep](./copysweep.md)
- [pastesweep](./pastesweep.md)
- [addsweep](./addsweep.md)
- [insertsweep](./insertsweep.md)
- [getsweep](./getsweep.md)
- [setsweep](./setsweep.md)
- [addsweepparameter](./addsweepparameter.md)
- [addsweepresult](./addsweepresult.md)
- [removesweepparameter](./removesweepparameter.md)
