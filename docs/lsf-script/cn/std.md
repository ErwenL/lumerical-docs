<!--
---
**Translation metadata**
- English title: std
- Chinese title: std - 标准差
- Status: Completed
- Translator: AI
- Last updated: 2026-02-03
- Difficulty: Beginner
- Priority: Standard
---
-->

# std

返回指定矩阵所有元素的标准差。N 个数 X = [x₁,...,xₙ] 集合的标准差定义为

$$ \sigma=\sqrt{\frac{1}{N} \sum_{i=1}^{N}\left(x_{i}-\mu\right)^{2}} $$ 

其中 μ 是 X 的平均值。

| **语法** | **描述** |
|---|---|
| out = std(A); | 返回矩阵 A 在所有维度上的标准差。 |

**示例**

这些是显示如何使用此命令的一些简单示例。

```
a =[1,2,3,4,5];
?std(a);
result: 
1.41421 
b =[1,2,3,4,5;5,4,3,2,1;1,4,2,5,8];
?std(b);
?sqrt(sum((b-mean(b))^2)/length(b)); # 与使用 sum 和 mean 的等效计算进行比较
result: 
1.88562
result: 
1.88562  
d = randmatrix(3,3,3);
?d;
result(i,j,1):
0.345988 0.84698 0.271889 
0.471725 0.316874 0.982971 
0.374981 0.456099 0.2978 
result(i,j,2):
0.739189 0.761315 0.5009 
0.567278 0.839442 0.890164 
0.19599 0.397656 0.0274667 
result(i,j,3):
0.994629 0.531327 0.626759 
0.572588 0.194067 0.657613 
0.0505081 0.843043 0.197851
 
?std(d);
result: 
0.274514
```

**另请参见**

[ var ](./var.md) , [ mean ](./mean.md) , [ sum ](./sum.md) , [ length ](./length.md)
