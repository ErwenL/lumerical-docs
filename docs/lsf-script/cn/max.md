# max

返回矩阵中的最大值。对于复数，只考虑实部。

**语法** | **描述**
---|---
out = max(x); | 矩阵 x 中的最大值。

**示例**

简单示例，演示如何找到向量的最大值。

```
?x=linspace(0,3,4);
result:
0
1
2
3
?max(x);
result:
3
```

简单示例，演示如何处理复数。

```
?x = 3 + 4i;
?max(x);
?max(abs(x));
result:
3+4i
result:
3
result:
5
```

查找每个频率点的最大场强。

```
# 按频率绘制 3D 电场的最大值
E2  = getelectric("3D field monitor");
f   = getdata("3D field monitor","f");
E_dim = size(E2);            # 矩阵 E 的维度
data = matrix(E_dim(4));        # 创建大小为 E_dim(4) 的矩阵即频率点数
for (i=1:E_dim(4)) {
 maxVal = max( pinch(E2,4,i) );        # 选取特定频率的数据
 data(i)=maxVal;
}
plot(f,data,"Frequency (Hz)","Maximum E intensity");
```

**另请参阅**

- [命令列表](./命令列表.md)
- [min](./min.md)
- [abs](./abs.md)
- [mean](./mean.md)
- [amax](./amax.md)
- [amin](./amin.md)
