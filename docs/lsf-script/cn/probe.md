# probe

在指定元素的指定端口放置探针分析仪。

**语法** | **描述**
---|---
probe ("name","port"); | 在给定元素名称的给定端口放置探针分析仪。

**示例**

```powershell
#向原理图编辑器添加直波导元件，并向其"端口 2"添加探针
addelement("Straight Waveguide");
probe("WGD_1", "port 2");
```

**另请参阅**

[命令列表](../%E5%91%BD%E4%BB%A4%E5%88%97%E8%A1%A8.md)、[library](./library.md)、[addtolibrary](./addtolibrary.md)、[saveelement](./saveelement.md)
