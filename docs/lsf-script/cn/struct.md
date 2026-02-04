<!-- Translation completed: 2026-02-03 -->
<!-- Original command: struct -->

# struct

创建结构数组。任何数据类型(如矩阵、字符串、数据集)都可以添加到结构数组中。

自Lumerical 2019b R4版本起，用户也可以使用大括号声明方法来声明结构数组。

**语法** | **描述**
---|---
`a = {"one" : "fish", "two" : "fish", "red" : "fish", "blue" : "fish"}` | 创建并初始化结构数组。
`a = struct;` | 创建结构数组。
`a.a = "string";` | 向结构数组添加字符串字段。
`a.b = matrix(5,5);` | 向结构数组添加5×5矩阵字段。

**示例**

结构可以快速创建和初始化，如下所示：

```
C = {"a" : [1, 4, 9],
     "b" : "a string",
     "d" : matrix(5, 5),
     "e" : getresult("monitor", "T")};
```

上述结构数组也可以以更冗长的方式声明：

```
C = struct;
C.a = [1, 4, 9];
C.b = "a string";
C.d = matrix(5,5);
C.e = getresult("monitor","T");
```

两个结构数组等价，将产生相同的输出：

```
?C;
Struct with fields:
a
b
d
e

?C.a;
result: 
1 4 9

?C.a(2);
result: 
4

?C.b;
a string

?C.d;
result: 
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

?C.e;
T vs lambda/f
```

当两个或多个对象共享相同参数时，可以对它们全部使用"struct"：

```
    addrect;
    props = struct;
    props.x = 1e-6;
    props.y = 2e-6;
    setnamed("rectangle",props);
    addprofile;
    set(props);
```

在上面的示例中，几何体"rectangle"和分析监视器具有相同的x和y值，因此可以使用给定的"x,y"的"struct"在setnamed和/或set中应用它们。

"struct"也可用于直接设置属性：

```
 addcircle( {"name":"c1","x": 1e-6,"y": 2e-6,"radius":0.5e-6});
 mystruct = {"name":"c2","x":-1e-6,"y":-2e-6,"radius":0.5e-6};
 addcircle(mystruct);
```

上述脚本将创建位于第一和第三象限的两个圆形"c1"和"c2"，半径相同。

**参见**

[Datasets](Datasets.md), [matrixdataset](matrixdataset.md), [rectilineardataset](rectilineardataset.md), [cell](cell.md), [isfield](isfield.md), [getfield](getfield.md), [setfield](setfield.md), [isstruct](isstruct.md)
