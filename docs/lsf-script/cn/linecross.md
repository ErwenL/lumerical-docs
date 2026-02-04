<!--
Translation from English documentation
Original command: linecross
Translation date: 2026-02-03
-->

# linecross

确定 x-y 平面中的两条线段是否相交。

线段包含在维度为 2*Nx2 的单个矩阵中，其中 N 是线段的数量。例如，矩阵 L = [0,0; 1,1; 0,0; 0,1] 表示两条线段，一条从 (0,0) 到 (1,1)，另一条从 (0,0) 到 (0,1)。

**语法** |  **描述**
---|---
out = linecross(L1,L2);  |  返回维度为 N 的数组，确定 L1 中的 N 条线段和 L2 中的 N 条线段是否相交；比较按 lineintersect 命令中的方式进行成对比较。L1 和 L2 必须具有相同的大小（对于 N 条线段为 2*Nx2）。如果线段不相交，则输出数组中的元素为 0；如果相交则为 1；如果一条线段的端点接触另一条则为 0.5。重合且接触的线段也返回 0.5。

**示例**

以下示例说明了 linecross 函数的不同结果：

    L1 = [ 0,0; 1,1; 0,0; 1,1 ];
    L2 = [ 0,1; 1,0; 2,2; 3,3 ];
    ?linecross(L1,L2);
    result:
    1
    0
    L1 = [ 0,0; 1,1 ];
    L2 = [ 0.5,0.5; 0,1 ]; # L2 的起点接触 L1
    ?linecross(L1,L2);
    result:
    0.5
    L1 = [ 0,0; 1,1 ];
    L2 = [ 1,1; 2,2 ]; # L1 的终点与 L2 的起点相同
    ?linecross(L1,L2);
    result:
    0.5
    L1 = [ 0,0; 1,1 ];
    ?linecross(L1,L1);
    result:
    0.5

**相关命令**

- [List of commands](./List-of-commands.md)
- [lineintersect](./lineintersect.md)
- [finite](./finite.md)
