<!--
Translator: Claude
Translation Date: 2026-02-03
Status: Completed
-->
# smithchart

在史密斯圆图上绘制阻抗值。用于归一化的默认阻抗为50欧姆；这可以在创建图表后在绘图设置中进行修改。

**语法** | **描述**
---|---
out = smithchart(Z); | 在史密斯圆图中创建一条曲线，使用数组Z中的阻抗值。数组Z必须是NX1或1XN形式。
out = smithchart(Z1,Z2,Z3); | 在史密斯圆图中创建三条曲线，使用数组Z1、Z2和Z3中的阻抗值。每个数组必须是NX1或1XN形式，但它们可以具有不同的维度。
out = smithchart(Z, "title", "aspect ratio", norm_Z); | 创建具有标题、给定宽高比和归一化阻抗norm_Z的史密斯圆图。宽高比必须是字符串，可以是"1:1"或"fill scene"。

**示例**

创建简单的史密斯圆图

```
Z1 = 50*(3+1i*linspace(-50,50,101)); # re(Z) = 3 圆
Z2 = 50*(linspace(0,50,101)+0.75i); # im(Z) = 0.75 线
smithchart(Z1,Z2,"史密斯圆图示例", "1:1", 50); # 归一化阻抗 50 欧姆
#也可以使用setplot设置绘图属性：
smithchart(Z1,Z2);
setplot("title", "史密斯圆图示例");
setplot("aspect ratio", "1:1");
setplot("normalized impedance", 50);
```

下图显示了示例代码的输出。

**另请参阅**

[ 命令列表 ](command-list.html), [ polar ](polar.html), [ setplot ](setplot.html)
