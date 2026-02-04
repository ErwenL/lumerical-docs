# filebasename

从字符串中获取文件名（不含扩展名）。

**语法** | **描述**
---|---
out = filebasename( "location/filename.ext" ); | 以字符串形式返回文件名（不含扩展名）。

**示例**

从完整文件名中分离出文件名（不含扩展名）。

```powershell
?filebasename("C:\Users\myname\Documents\FDTD Files\test.fsp");
test
```

**另请参阅**

[命令列表](../命令列表.md)、[currentfilename](./currentfilename.md)、[getpath](./getpath.md)、[which](./which.md)、[pwd](./pwd.md)、[filedirectory](./filedirectory.md)、[fileextension](./fileextension.md)