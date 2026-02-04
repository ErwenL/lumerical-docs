<!--
Translation from English documentation
Original command: []
Translation date: 2026-02-03
-->

# []

按元素指定矩阵元素。

**命令** |  **描述**
---|---
x = [u11,...,u1N; u21,...,u2N; uM1,...,uMN]  |  创建 N×M 矩阵。列用分号分隔。行中的元素用逗号分隔。条目可以是标量或兼容维度的矩阵。

**示例**

    ?x=[1,2;3,4;5,6];
    result:
    1 2
    3 4
    5 6
    ?x(1:3,1);
    result:
    1
    3
    5
    a=matrix(2,2,2);
    a(1,1)=1;
    a(2,2)=2;
    b=a+1;
    ?c=[a,b];
    result(i,j,1):
    1 0 2 1
    0 2 1 3
    result(i,j,2):
    0 0 1 1
    0 0 1 1

**相关命令**

- [List of commands](./List-of-commands.md)
- [linspace](./linspace.md)
- [matrix](./matrix.md)
- [Accessing and assigning matrix elements](./Accessing-and-assigning-matrix-elements.md)
