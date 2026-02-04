# setview

> **原文**: setview  
> **翻译日期**: 2026-02-03  
> **翻译状态**: ✅ 已完成

此命令允许修改布局编辑器的查看属性。

| **语法** | **说明** |
| --- | --- |
| outstring = setview; | 返回可以设置的查看属性列表。命令 |

```
?setview;
```

将返回

```
extent, zoom, theta, phi
```

| **语法** | **说明** |
| --- | --- |
| setview("property"); | 为任何查看属性设置默认值。例如， |

```
setview("extent");
```

与按下图形范围按钮相同。

| **语法** | **说明** |
| --- | --- |
| setview("property",value); | 为查看的任何属性设置值。 |

下表描述了可以设置的属性

| **属性** | **说明** |
| --- | --- |
| extent（在CHARGE、HEAT、FEEM、DGTD中不可用） | 控制查看范围。在这种情况下，value应该是一个2x1、4x1或6x1矩阵，分别代表查看范围的最小x、最大x、最小y、最大y、最小z和最大z。 |
| zoom | 控制透视视图相对于默认级别的相对缩放。要在透视视图中放大2倍，使用 |

```
setview("zoom",2);
```

| **属性** | **说明** |
| --- | --- |
| theta | 控制透视视图的极角，以度为单位。 |
| phi | 控制透视视图的方位角，以度为单位。 |

**示例**

此示例使用setview命令将"透视视图"旋转360度。

```
setview("extent");
setview("zoom",4);
setview("theta", 30);
for (i=0:10:360) {
  setview("phi",i);
}
```

**相关命令**

[操作对象](./360037228834.md), [getview](./getview.md), [orbit](./orbit.md), [redraw](./redraw.md)
