# exportimage

导出当前电路原理图的图像。

**语法** | **描述**
---|---
exportimage(filename); | 导出当前电路原理图的图像。如果文件扩展名为 'png' 或无扩展名，将创建 PNG（便携式网络图形）文件。如果文件扩展名为 'svg'，将创建 SVG（可缩放矢量图形）文件。

**示例**

```powershell
exportimage("schematic.png");
```

**另请参阅**

[命令列表](../命令列表.md)