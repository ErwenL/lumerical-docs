<!--
Translation from English documentation
Original command: setemeanalysis
Translation date: 2026-02-03
-->

# setemeanalysis

设置 MODE 的 EME 分析窗口中的计算参数。

**语法** | **描述**
---|----
?setemeanalysis; | 列出 EME 分析窗口中的所有参数。
setemeanalysis("property", value); | 将名为"property"的参数设置为 value。

**示例**

此代码将显示可以设置的属性，并设置 EME 分析窗口 EME 设置部分中的组跨度列。

```lsf
# 显示可以使用 setemeanalysis 命令设置的属性
?setemeanalysis;

# 将组跨度属性设置为 1 微米（适用于 3 个单元组）
setemeanalysis("group spans",[1e-6;1e-6;1e-6]);
```

此代码将设置、运行并收集分析模式中传播扫描工具的用户 s 矩阵结果。

```lsf
# 设置传播扫描设置
setemeanalysis("propagation sweep",1);
setemeanalysis("parameter","group span 2");
setemeanalysis("start",10e-6);
setemeanalysis("stop",200e-6);
setemeanalysis("number of points",10);

# 运行传播扫描工具
emesweep;

# 获取传播扫描结果
S = getemesweep('S');
```

此代码将设置、运行并导出分析模式中波长扫描工具的用户 s 矩阵结果到名为"s_param"的文件。

```lsf
# 设置波长扫描设置
setemeanalysis("wavelength sweep", 1);
setemeanalysis("start wavelength", 1.5e-6);
setemeanalysis("stop wavelength", 1.6e-6);
setemeanalysis("number of wavelength points", 31);
setemeanalysis("calculate group delays", 1);

# 运行波长扫描工具
emesweep("wavelength sweep");

# 导出波长扫描结果
exportemesweep("s_param");
```

**另请参见**

- [getemeanalysis](./getemeanalysis.md)
- [emesweep](./emesweep.md)
- [exportemesweep](./exportemesweep.md)
