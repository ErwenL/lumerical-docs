# min

返回矩阵中的最小值。对于复数，只考虑实部。

**语法** | **描述**
---|---
out = min(x); | 矩阵 x 中的最小值。

**示例**

简单示例，演示如何找到实数组的最小值。

```
?x=linspace(0,3,4);
result:
0
1
2
3
?min(x);
result:
0
```

如果数组有复数，只考虑实部，如下所示。

```
?x = 3 + 4i;
?min(x);
?min(abs(x));
result:
3+4i
result:
3
result:
5
```

**另请参阅**

- [命令列表](./命令列表.md)
- [max](./max.md)
- [abs](./abs.md)
- [mean](./mean.md)
- [amax](./amax.md)
- [amin](./amin.md)
