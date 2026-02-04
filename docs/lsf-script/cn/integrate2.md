<!--
Translation from English documentation
Original command: integrate2
Translation date: 2026-02-03
-->

# integrate2

与标准积分函数非常相似，不同之处在于它忽略单例维度。

正如积分函数描述中所述，对具有单个值（单例维度）的维度进行积分会返回零，因为单个点下的面积为零。在某些情况下，特别是当您不确定哪些维度是单例时，这种行为可能会造成困难。integrate2 函数会自动忽略所有大小为 1 的维度，这避免了由于单例维度导致零值积分的问题。

**语法** |  **描述**
---|---
out = integrate2(A, 1, x1);  |  在矩阵的第一维上对 A 进行积分。x1 是对应的位置向量。
out = integrate2(A, d, x1, x2, ...);  |  计算 A 在指定维度 d 上的积分。d 是包含要积分维度的向量。xi 是 A 的对应于正在执行积分的维度的位置向量。如果任何 xi 向量只有 1 个元素，积分返回 0。例如

  * power = integrate2(A,1:2,x,y) 将在 x-y 曲面上对 A 进行积分。

**示例**

在以下示例中，我们比较积分和积分2命令在处理具有单例维度的矩阵时的行为。

    # create 3D matrix of results: data(x,y,z) where
    # there are 50 'x' sample points, 1 'y' sample points
    # and 40 'z' sample points. This is typical of data
    # from a 2D monitor oriented in the XZ plane.
    x=linspace(-5,5,50);
    y=0;
    z=linspace(-3,3,40);
    X=meshgrid3dx(x,y,z);
    Z=meshgrid3dz(x,y,z);
    data = X^2 + Z^2;
    image(x,z,data,"x","z","data");
    ?integrate2(data, [1,2,3], x,y,z); # Integrate2 ignores singleton dimension, giving non-zero result.
    ?integrate (data, [1,2,3], x,y,z); # Result is zero because of the singleton dimension
    ?integrate (data, [1,3] , x,z ); # Get the same result as integrate2 by integrating over x and z, but not y.
    > result:
    > 680.653
    > result:
    > 0
    > result:
    > 680.653

**相关命令**

- [List of commands](./List-of-commands.md)
- [integrate](./integrate.md)
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
