<!--
Translation from English documentation
Original command: readnportsparameterat
Translation date: 2026-02-03
-->

# readnportsparameterat

使用指定参数值对 [S-Parameter sweep](https://optics.ansys.com/hc/en-us/articles/360036107934-The-S-parameter-sweep) 文件进行插值。

**语法** | **描述**
---|---
M = readnportsparameterat("filename", sweep_param) | 使用样条插值方法对 S-Parameter sweep 文件进行指定参数值的插值。filename：S-Parameter sweep 文件。sweep_param：指定的扫描参数，通常以矩阵格式提供。
M = readnportsparameterat("filename", sweep_param, opt) | 使用 opt 结构体中设置的插值选项对 S-Parameter sweep 文件进行指定参数值的插值。filename：S-Parameter sweep 文件。sweep_param：指定的扫描参数，通常以矩阵格式提供。opt：设置插值选项的结构体。结构体的字段在下面的表格中描述。

选项结构体具有以下字段，每个字段的拼写区分大小写。

**字段** | **描述**
---|---
method | 用于插值的方法。支持以下选项：
| | - spline：样条插值方法，这是默认方法。
| | - Geodesic：大地测量插值方法，确保平滑过渡。选择大地测量插值时，会对用于插值的原始数据点附近的插值点进行相似性检查，如果这些点不够相似，数据太粗糙，将显示警告。此方法不能用于外推。
passivity | 是否在插值前对 s 参数数据强制执行无源性。此字段仅在 "geodesic" 被选为插值方法时影响结果。当数据非无源时，总是显示警告消息。支持以下选项：
| | - enforce：确保 S 矩阵是无源的，确保 s 参数的诱导 2-范数小于 1。这是默认方法。
| | - ignore：忽略 s 参数的无源性并按原样插值。

**注意**：有关如何强制执行无源性的更多信息，请参阅此[知识库](https://optics.ansys.com/hc/en-us/articles/360059772393-S-parameter-passive-workflow-guide#toc_4)文章。

**示例**

以下脚本使用名为 "sweep_param" 的矩阵中定义的指定参数对 S-Parameter 文件 "coupler_s_parameter_sweep.txt" 进行插值。然后这个插值后的 s 参数可以分配给 s 参数元件。

```lsf
# 这里，变量 radius、Lc 和 gap 之前已设置
sweep_param = matrix( 3 );
sweep_param(1)=radius;
sweep_param(2)=Lc;
sweep_param(3)=gap;
?M = readnportsparameterat("coupler_s_parameter_sweep.txt", sweep_param );
```

以下脚本对同一个 S-Parameter 文件进行插值，但使用大地测量选项并忽略无源性。

```lsf
?M = readnportsparameterat("coupler_s_parameter_sweep.txt", sweep_param, {"method":"geodesic", "passivity":"ignore"});
```

**另请参见**

- [convertnportsparametersweep](./convertnportsparametersweep.md)
