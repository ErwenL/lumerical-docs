# mesh

生成执行后续计算所需的当前结构网格。在 MODE 中，它生成一个名为 "material" 的 d-card，其中包含网格化对象的材料属性。

这相当于在 MODE 的图形用户界面中按 "mesh structure" 按钮，或在有限元 IDE 中按 "Mesh" 按钮。

**语法** | **描述**
---|---
mesh; | 对 FDE、DGTD 或 FEEM 中的当前模拟进行网格划分。在 MODE 中，只能与 FDE 求解器一起使用。在有限元 IDE 中，它对存在的模拟（DGTD 或 FEEM）进行网格划分。
mesh("solver_name"); | 在由参数 "solver_name" 定义的所需求解器中对当前模拟进行网格划分。参数名称仅在有限元 IDE 中受支持，选项为 "DGTD" 和 "FEEM"。

**另请参阅**

- [命令列表](./命令列表.md)
- [setanalysis](./setanalysis.md)
- [mesh](./mesh.md)
- [findmodes](./findmodes.md)
- [frequencysweep](./frequencysweep.md)
- [analysis](./analysis.md)
- [getanalysis](./getanalysis.md)
