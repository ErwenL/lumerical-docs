# exportsweep

将 S 参数扫描任务的 S 参数结果导出为 .dat 文件，该文件可由 INTERCONNECT 中的 [光学 N 端口 S 参数](**%20to%20be%20defined\**) 元素加载。

**语法** | **描述**
---|---
exportsweep("sweep_name","filename","format"); | 将指定 S 参数扫描任务的 S 参数结果导出为 .dat 文件，文件名在当前工作目录中指定。"format" 可以是 "lumerical" 或 "touchstone" 格式，如果未指定则使用 "lumerical" 格式。"touchstone" 格式为 v1.1 版本。如果频率范围内的最大无源性大于 1.03，或频率范围内的最大互易性误差超过 0.03，则在导出数据时会在脚本提示中显示警告消息。如果已存在同名文件，现有文件将被覆盖。此函数不返回任何数据。

请注意，Touchstone v1.1 格式无法处理不同的模式，因此"端口"数量实际上是有效端口的数量（端口/模式组合）。

**示例**

以下代码可用于将 S 参数数据导出为名为 s_params.s4p 的 Touchstone 文件。

```powershell
exportsweep("s-parameter sweep","s_params.s4p", "touchstone");
```

**另请参阅**

[addsweep](./addsweep.md)、[runsweep](./runsweep.md)、[getsweepresult](./getsweepresult.md)、[S 参数矩阵扫描](**%20to%20be%20defined\**)