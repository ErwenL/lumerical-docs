<!--
Translation from English documentation
Original command: randmatrix
Translation date: 2026-02-03
-->

# randmatrix

初始化一个矩阵。所有元素都是介于 0 和 1 之间的随机数。

**语法** | **描述**
---|---
x = randmatrix(i,j,k,....); | 初始化一个 i x j x k x .... 的矩阵。所有元素都是介于 0 和 1 之间的随机数。

**示例**

```lsf
?x=randmatrix(2,2,2);
```
结果：
```
result(i,j,1):
0.202368 0.503983
0.570605 0.89404
result(i,j,2):
0.740623 0.669118
0.888394 0.295022
```

**另请参见**

- [命令列表](./command_list.md)
- [matrix](./matrix.md)
- [rand](./rand.md)
- [randreset](./randreset.md)
