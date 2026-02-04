<!-- Translation completed: 2026-02-04 -->
<!-- Original command: sqrt -->

# sqrt

计算数字的平方根。输入可以是复数或负数。

**语法** | **描述**
---|---
out = sqrt(x); | x的平方根。选择平方根使得对于任何复数x，real(sqrt(x))≥0。虚部imag(sqrt(x))可以是正数或负数，但如果real(sqrt(x))=0，则imag(sqrt(x))≥0。

**示例**

计算数字的平方根：

```lsf
?sqrt(4);
result: 
2 
```

复平面上z = x + iy的平方根函数在(-∞,0]处有分支切割，如下例所示：

```lsf
x = linspace(-1,1,100);
y = linspace(-1,1,100);
X = meshgridx(x,y);
Y = meshgridy(x,y);
image(x,y,real(sqrt(X+1i*Y)),"x", "y","Real part of sqrt(x+iy)");
image(x,y,imag(sqrt(X+1i*Y)),"x", "y","Imaginary part of sqrt(x+iy)");
```

**另请参阅**

[命令列表](List_of_commands.md)、[^](caret.md)
