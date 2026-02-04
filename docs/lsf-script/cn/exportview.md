# exportview

此命令捕获仿真设置中指定视图显示的内容，并将其导出为静态图像到 png 文件中。此脚本命令是 Lumerical 工具中 GUI 菜单提供的视图导出功能的替代方案。

**语法** | **描述**
---|---
exportview("filename"); | 捕获默认"透视"视图中的当前场景，并将其保存为 filename.png。
exportview("example_filename","perspective"); | 可选：捕获指定视图中的场景。选项包括：XY、XZ、YZ、perspective。注意：此可选参数在有限元 IDE 中不可用，因为它只提供一个视图

**示例**

在提示符中输入 exportview("ring_modulator_v2_XY","XY"); 将当前仿真的 XY 视图保存为 "ring_modulator_v2_XY.png" 到当前路径。

**另请参阅**

[orbit](./orbit.md)、[setview](./setview.md)