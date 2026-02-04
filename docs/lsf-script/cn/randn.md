<!--
Translation from English documentation
Original command: randn
Translation date: 2026-02-03
-->

# randn

生成一个正态分布的随机数。要重置生成器种子，请使用 `randreset` 命令。

**语法** | **描述**
---|---
out = randn; | 生成一个均值为 0、标准差为 1 的正态分布随机数。
out = randn(mean,stddev); | 生成一个用户定义均值和标准差的正态分布随机数。

**示例**

此示例展示如何创建正态分布的直方图：

```lsf
n = 1000;
y = matrix(n);
mean_val = 1;
std_dev = 0.25;
for (i=1:n){
    y(i) = randn(mean_val, std_dev);
}
histc(y);
```

直方图将类似于以下图形。

**另请参见**

- [命令列表](./command_list.md)
- [randreset](./randreset.md)
- [lognrnd](./lognrnd.md)
- [randnmatrix](./randnmatrix.md)
