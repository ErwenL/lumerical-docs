# exportlib

导出 Custom 文件夹中 CML 的 .lib 文件。

**语法** | **描述**
---|---
exportlib(name, path, overwrite); | 导出 Custom 文件夹中 CML 的 .lib 文件。name：Custom 中的 CML 名称；path：导出 .lib 文件的保存路径。如果未提供 path，则使用当前工作目录；overwrite：布尔值，指示如果文件存在是否覆盖。

**示例**

```powershell
# 导出 "dk.cml" 的 ".lib" 文件
exportlib("dk.cml", "C:/Users/xxx", true);
```

**另请参阅**

[命令列表](../命令列表.md)、[packagedesignkit](./packagedesignkit.md)、[installdesignkit](./installdesignkit.md)、[importschematic](./importschematic.md)、[exportschematic](./exportschematic.md)、[customlibrary](./customlibrary.md)、[ Custom Library & Design Kit ](**%20to%20be%20defined%20**)