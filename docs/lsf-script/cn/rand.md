<!--
Translation from English documentation
Original command: rand
Translation date: 2026-02-03
-->

# rand

生成一个介于 0 和 1 之间的均匀分布随机数。要重置生成器种子，请使用 `randreset` 命令。

**语法** | **描述**
---|---
out = rand; | 生成一个介于 0 和 1 之间的均匀分布随机数。
out = rand(min,max); | 生成一个介于 min 和 max 之间的随机数。默认情况下，min 和 max 分别为 0 和 1。
out = rand(min,max,option); | option = 1：输出为介于 min 和 max 之间的双精度数（默认）。option = 2：输出为介于 min 和 max 之间的整数。

**示例**

`rand` 输出的简单示例：

```lsf
?rand;
```
结果：
```
0.528733
```

```lsf
?rand(0,10,1);
```
结果：
```
9.33399
```

```lsf
?rand(0,10,2);
```
结果：
```
5
```

使用 Box-Muller 变换的极坐标形式生成两个高斯随机数（Y1 和 Y2）：

```lsf
# 选择均值和方差
mean_value = 0;
variance_value = 1;
w=1;
for(0;(w>1)|(w==1);0){ # 当 w>=1 时循环
  x1 = 2*rand - 1;
  x2 = 2*rand - 1;
  w = x1^2 + x2^2;
}
w = sqrt( (-2*log( w ) ) / w );
y1 = x1 * w;
y2 = x2 * w;
?Y1 = mean_value + sqrt(variance_value) * y1;
?Y2 = mean_value + sqrt(variance_value) * y2;
```
结果：
```
0.198101
-2.05023
```

**另请参见**

- [命令列表](./command_list.md)
- [randreset](./randreset.md)
- [randmatrix](./randmatrix.md)
- [randn](./randn.md)
