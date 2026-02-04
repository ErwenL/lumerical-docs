<!--
Translation from English documentation
Original command: lineintersect
Translation date: 2026-02-03
-->

# lineintersect

返回 x-y 平面中两条线的交点。请注意，交点不必位于定义线的线段上。使用 linecross 命令来确定线段是否实际相交。

线段包含在维度为 2*Nx2 的单个矩阵中，其中 N 是线段的数量。例如，矩阵 L = [0,0; 1,1; 0,0; 0,1] 表示两条线段，一条从 (0,0) 到 (1,1)，另一条从 (0,0) 到 (0,1)。

**语法** |  **描述**
---|---
out = lineintersect(L1,L2);  |  返回由 L1 和 L2 中的线段表示的线的交点。L1 和 L2 必须具有相同的大小（对于 N 条线段为 2*Nx2）。结果是以 Nx2 形式表示的 x,y 点序列，表示 N 条线的成对相交。有以下特殊情况：

  * 线是平行的。在这种情况下，返回的位置为 (1.#INF,b)。可以使用脚本命令 finite 测试 1.#INF 的存在。如果线重合，则 b 的值为 0；如果不重合，则 b 的值为 1。
  * 线段中的点是退化的（即相同的）。在这种情况下，返回的位置为 (1.#INF,b)，如果两条线段都退化，则 b 为 0、1 或 2；如果第一条退化，则 b 为 1；如果第二条退化，则 b 为 2。

**示例**

在第一个示例中，L1 和 L2 是两组线段；结果是一个 2x2 矩阵，其中第一行是每组中第一条线段的交点，第二行是每组中第二条线段的交点。

    L1 = [ 0,0; 1,1; 0,10; 1,10];
    L2 = [ 0,1; 1,0; 5,0; 5,1];
    ?lineintersect(L1,L2);
    result:
    0.5  0.5
    5  10

第二个示例显示了线不相交、重合或线段退化时的特殊情况下的输出。

    L1 = [ 0,0; 1,1];
    L2 = [ 1,0; 2,1]; #L2 平行于 L1
    L3 = [ 3,3; 3,3]; #L3 中的点是退化的
    ?lineintersect(L1,L1);
    ?lineintersect(L1,L2);
    ?lineintersect(L3,L3);
    ?lineintersect(L3,L1);
    ?lineintersect(L2,L3);
    result:
    1.#INF  1
    result:
    1.#INF  0
    result:
    1.#INF  0
    result:
    1.#INF  1
    result:
    1.#INF  2

**相关命令**

- [List of commands](./List-of-commands.md)
- [linecross](./linecross.md)
- [finite](./finite.md)
