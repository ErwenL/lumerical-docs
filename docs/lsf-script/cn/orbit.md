# orbit

此命令在透视视图中执行结构的椭圆观察轨道。请注意，setview、getview 和 redraw 命令使您能够在自己的脚本文件中创建任何类型的轨道。

**语法** | **描述**
---|---
orbit; | 执行当前透视视图的轨道。
orbit(zoom_factor); | 使用指定的最小缩放因子执行轨道。默认缩放因子为 1.5。
orbit(zoom_factor, frame_rate); | 使用指定的每秒帧数帧率执行轨道。默认帧率为 15。

**示例**

在提示符中输入 orbit，您将看到透视视图正在旋转。

**另请参阅**

- [操作对象](./操作对象.md)
- [setview](./setview.md)
- [getview](./getview.md)
- [framerate](./framerate.md)
