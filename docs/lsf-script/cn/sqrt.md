<!--
---
**Translation metadata**
- English title: sqrt
- Chinese title: sqrt - 平方根
- Status: Completed
- Translator: AI
- Last updated: 2026-02-03
- Difficulty: Beginner
- Priority: Standard
---
-->

# sqrt

计算数字的平方根。输入可以是复数或负数。

| **语法** | **描述** |
|---|---|
| out = sqrt(x); | x 的平方根。选择平方根使得对于任何复数 x，real(sqrt(x))≥0。虚部 imag(sqrt(x)) 可以为正或负，但如果 real(sqrt(x))=0，则 imag(sqrt(x))≥0。 |

**示例**

计算一个数的平方根。

```
?sqrt(4);
result: 
2 
```

复平面上 z = x + iy 的平方根函数在 (-∞,0] 处有分支切割，如下例所示。

```
x = linspace(-1,1,100);
y = linspace(-1,1,100);
X = meshgridx(x,y);
Y = meshgridy(x,y);
image(x,y,real(sqrt(X+1i*Y)),"x", "y","Real part of sqrt(x+iy)");
image(x,y,imag(sqrt(X+1i*Y)),"x", "y","Imaginary part of sqrt(x+iy)");
```

**另请参见**

[ 命令列表 ](./command_list.md) , [ ^ ](./power.md)
