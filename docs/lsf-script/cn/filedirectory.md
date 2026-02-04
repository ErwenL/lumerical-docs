# filedirectory

从字符串中获取文件目录。

**语法** | **描述**
---|---
out = filedirectory( "location/filename.ext" ); | 以字符串形式返回文件目录。

**示例**

从完整文件名中分离出文件目录。

```powershell
?filedirectory("C:\Users\myname\Documents\FDTD Files\test.fsp");
C:/Users/myname/Documents/FDTD Files
```

**另请参阅**

[命令列表](../命令列表.md)、[currentfilename](./currentfilename.md)、[getpath](./getpath.md)、[which](./which.md)、[pwd](./pwd.md)、[fileextension](./fileextension.md)、[filebasename](./filebasename.md)