# findpeaks

返回矩阵中峰的位置。峰（或局部最大值）定义为大于其最近邻的数据点。

**语法** | **描述**
---|---
out = findpeaks(y); | 返回 y 中最大值的峰的位置。y 的长度必须至少为 2。如果数据中未找到峰，则返回 1。
findpeaks(y,n); | 返回包含数据中找到的最大的 n 个峰位置的矩阵。返回值从大到小排序。返回的矩阵始终为 nX1 维。如果找到的峰少于 n 个，则返回矩阵的其余值为 1。

**示例**

以下示例计算数据集中两个最大峰的位置。

```powershell
x=linspace(-20,20,1000);
y=x*cos(x);
?pos=findpeaks(y,2);
plot(x,y);
?"largest peak is at x=" + num2str(x(pos(1)));
?"largest peak height is y=" + num2str(y(pos(1)));
?"2nd largest peak is at x=" + num2str(x(pos(2)));
?"2nd largest peak height is y=" + num2str(y(pos(2)));
result:
973
107
largest peak is at x=18.9189
largest peak height is y=18.8734
2nd largest peak is at x=-15.7558
2nd largest peak height is y=15.7378
```

**另请参阅**

[命令列表](../命令列表.md)、[find](./find.md)