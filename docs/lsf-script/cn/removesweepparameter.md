<!--
Translation from English documentation
Original command: removesweepparameter
Translation date: 2026-02-03
-->

# removesweepparameter

从参数扫描/优化/Monte Carlo/S-parameter 扫描项中删除参数。

**语法** | **描述**
---|---
removesweepparameter("name", "parameter_name"); | 从参数扫描/优化/Monte Carlo/S-parameter 扫描项中删除参数。"name" 是分析项的绝对名称。"parameter_name" 是参数名称。

**示例**

此示例展示了如何从扫描中删除参数。请从[参数扫描](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)页面下载示例文件。

```lsf
removesweepparameter("thickness_sweep", "thickness");
```

此示例展示了如何从 S-parameter 矩阵扫描的 s-matrix 映射表中删除第二行。

```lsf
removesweepparameter("s-parameter sweep",2);
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
- [removesweepresult](./removesweepresult.md)
