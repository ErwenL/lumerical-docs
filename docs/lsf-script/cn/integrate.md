<!--
Translation from English documentation
Original command: integrate
Translation date: 2026-02-03
-->

# integrate

返回矩阵指定维度上的积分。

对单例维度进行积分将返回零（即单个点下的面积为零）。有关替代行为，请参见 integrate2。

**语法** |  **描述**
---|---
out = integrate(A, n, x1);  |  在矩阵的第 n 维上对 A 进行积分。x1 是该维度对应的位置向量。
out = integrate(A, d, x1, x2, ...);  |  计算 A 在指定维度列表 d 上的积分。d 是包含要积分维度的向量。xi 是 A 的对应于正在执行积分的维度的位置向量。例如

  * power = integrate(A,1:2,x,y) 将在 x-y 曲面上对 A 进行积分。

**示例**

在以下示例中，integrate 命令用于对 y=x² 从 0 到 3 进行积分，其中函数在点 x=0,1,2,3 处进行采样。积分函数将从位置向量 x 确定 dx。作为参考，连续函数 y=x² 的积分值为 9。减小 dx 将使这个离散积分趋近于连续结果。

高级说明：这个非常简单的示例中的实际计算将为 0.5*0 + 1*1 + 1*4 + 0.5*9 = 9.5，如下图所示。值得注意的是，第一个和最后一个点的因子为 0.5*dx，因为它们在积分范围的边缘。如果没有对这些点应用 0.5 的因子，积分将从 x=-0.5 到 x=3.5 有效计算。

    ?x=0:3;
    y=x^2;
    ?integrate(y,1,x);
    result:
    0
    1
    2
    3
    result:
    9.5

接下来，我们演示积分函数正确处理非均匀采样。从 0 到 2 的函数部分使用 dx=1 进行评估，而从 2 到 3 使用 dx=0.2。在这种情况下，积分函数将计算 0.5*0 + 1*1 + 0.6*4 + 0.2*4.84 + 0.2*5.76 + 0.2*6.76 + 0.2*7.84 + 0.1*9;

    ?x=[[0:1]; [2:0.2:3]];
    y=x^2;
    ?integrate(y,1,x);
    result:
    0
    1
    2
    2.2
    2.4
    2.6
    2.8
    3
    result:
    9.34

最后，这个示例显示如何通过积分坡印廷向量来计算通过 y 法向监视器传输的功率。要获得传输功率，我们要对坡印廷向量的法向分量的实部 (Py) 进行积分。Py 数据矩阵的大小为 Nx × Ny × Nz × Nf，其中 Nx、Ny、Nz 是每个方向的网格点数。如果监视器是 Y 法向的，则 Ny=1。Nf 是监视器收集的频率点数。在对 X 和 Z 方向进行积分后，我们基本上得到传输功率与频率的 1D 函数。

    Py = getdata("Monitor1","Py");
    x = getdata("Monitor1","x");
    y = getdata("Monitor1","y");
    z = getdata("Monitor1","z");
    f = getdata("Monitor1","f");
    power = 0.5 * integrate( real(Py), [1,3], x,z );

**相关命令**

- [List of commands](./List-of-commands.md)
- [integrate2](./integrate2.md)
- [conv2](./conv2.md)
- [max](./max.md)
- [min](./min.md)
- [interp](./interp.md)
- [find](./find.md)
- [pinch](./pinch.md)
- [round](./round.md)
- [getdata](./getdata.md)
- [sum](./sum.md)
- [length](./length.md)
