<!-- Translation completed: 2026-02-03 -->
<!-- Original command: stlimport -->

# stlimport

从指定的STL文件加载几何结构，添加一个结构到仿真环境中。

**语法** | **描述**
---|---
`stlimport(filename,scalingFactor, vertexRadius,debugFlag);` | 从指定的STL类型CAD文件添加一个新结构。此函数不返回任何数据。

| 参数 | | 默认值 | 类型 | 描述
|---|---|---|---|---
| `filename` | 必需 | | 字符串 | STL CAD文件的名称。
| `scalingFactor` | 可选 | `1e-6` | 数值 | STL文件不包含单位。导入到Lumerical软件时，默认单位为微米。如需使用纳米单位，将scaling_factor设为1e-9。
| `vertexRadius` | 可选 | `1e-12` | 长度(单位:m) | 顶点可能由多个三角形共享，因此同一个顶点可能因不同三角形而被多次加载。vertexRadius是两个顶点被认为不同顶点的最小距离。
| `debugFlag` | 可选 | `false` | 布尔值 | 如果为true，以下数据将输出到脚本提示符：-输入顶点数(文件中顶点总数) -三角形数(三角形总数) -过滤后的顶点数(唯一顶点数) -顶点碰撞数(输入顶点数减去过滤后的顶点数) -无效三角形数 -预期顶点碰撞数。如果无效三角形数大于0，尝试调整vertexRadius参数后重新导入对象。注意：如果STL文件中有大量三角形，当debugFlag设为true时，脚本函数运行时间可能更长。

**示例**

以下脚本命令可用于基于本KB页面提供的.stl文件创建3D几何结构：[ Import - STL ](Import-STL.md)。

```
filename = "stlimport_assembly.stl";
stlimport(filename);
set("material","Si (Silicon)");
```

**参见**

[命令列表](List_of_commands.md), [set](set.md), [readstltriangles](readstltriangles.md)
