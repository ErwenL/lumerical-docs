# lognrnd

生成对数正态分布的随机数。要重置生成器种子，请使用 randreset 命令。

**语法** | **描述**
---|---
out = lognrnd (mean,stddev); | 生成用户指定均值和标准差的对数正态分布随机数。

**示例**

此示例演示如何创建对数正态分布的直方图。

```
n = 1000;
y = matrix(n);
mean_val = 1;
std_dev = 0.25;
for (i=1:n){
    y(i) = lognrnd(mean_val, std_dev);
}
histc(y);
```

直方图类似下图。

**另请参阅**

- [命令列表](./命令列表.md)
- [randreset](./randreset.md)
- [randn](./randn.md)
- [histc](./histc.md)
