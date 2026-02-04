# norm

返回由 L2 范数（谱范数）诱导的矩阵的自然范数。对于矩阵 A，这是矩阵乘积 A^H A 的最大特征值的平方根，其中 A^H 是 A 的共轭转置。

请注意，对于 N 维复向量 x = [x_1, x_2, ..., x_N]，这简化为通常的范数：

$$ \|x\|=\sqrt{\sum_{i=1}^{N} x_{i}^{*} x_{i}}=\sqrt{\sum_{i=1}^{N}\left|x_{i}\right|^{2}} $$

**语法** | **描述**
---|---
out = norm(y); | 返回矩阵 y 的谱范数。

**示例**

找到实向量和复向量的通常范数。

```
y1=[1,2,3];
y2=[1+1i,2,3]; #y2 有复元素
?norm(y1);
?norm(y2);
result:
3.74166
result:
3.87298
# 用通常的定义确认结果：
?sqrt(sum(conj(y1)*y1));
?sqrt(sum(conj(y2)*y2));
result:
3.74166
result:
3.87298+0i
```

找到复矩阵的通常范数。

```
A=[1,2+7i,3;7+3i,0,9];
?norm(A);
?sqrt(max(eig(mult(ctranspose(A),A)))); # 用定义确认结果
result:
12.332
result:
12.332
```

**另请参阅**

- [命令列表](./命令列表.md)
- [sqrt](./sqrt.md)
- [sum](./sum.md)
- [conj](./conj.md)
- [max](./max.md)
- [eig](./eig.md)
- [mult](./mult.md)
- [ctranspose](./ctranspose.md)
