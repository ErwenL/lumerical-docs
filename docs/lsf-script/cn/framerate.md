# framerate

绕透视视图旋转并返回帧率。这对于估计图形性能很有用。如果要比较两台计算机的性能，请确保使用完全相同的仿真文件。

**语法** | **描述**
---|---
fr = framerate(num_frames, zoom); | num_frames - 要绘制的帧数 zoom - 透视视图中使用的缩放因子 fr - 完成旋转所需的帧数/墙钟时间。

**示例**

```powershell
framerate(1000,2);
```

**另请参阅**

[操作对象](../操作对象.md)、[setview](./setview.md)、[getview](./getview.md)、[orbit](./orbit.md)