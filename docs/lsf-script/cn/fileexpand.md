# fileexpand

通过替换任何环境变量来扩展文件名。

**语法** | **描述**
---|---
fileexpand(filename); | 通过替换任何环境变量（由 setsetting 定义）来扩展文件名。

### 示例

扩展包含变量 LOCAL 的文件名。

```powershell
?getsetting;
LOCAL=C:\Users
?fileexpand("$LOCAL\data.txt");
```

**另请参阅**

[命令列表](../命令列表.md)、[setsetting](./setsetting.md)