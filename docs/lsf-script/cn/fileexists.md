# fileexists

检查文件是否存在。必须指定文件扩展名（即 .fsp、.lms 等）。默认情况下，将搜索整个路径。

**语法** | **描述**
---|---
out = fileexists("filename"); | 如果文件存在返回 1，如果文件不存在返回 0。
out = fileexists("c:\temp\file.txt"); | 搜索不在路径中的文件

**示例**

在打开文件之前检查文件是否存在。

```powershell
filename="simulation.fsp";
if (fileexists(filename)) {
    load(filename);
}
```

如果仿真项目文件存在，则加载它。首先检查当前目录，然后检查上一级目录。

```powershell
filename="simulation.fsp";
if (fileexists(file)) {
    load(filename);
} else {
    file = "../"+file;
    if (fileexists(file)) {
        load(filename);
    } else {
        ?"File not found.";
    }
}
```

**另请参阅**

[命令列表](../命令列表.md)、[getpath](./getpath.md)、[which](./which.md)、[pwd](./pwd.md)、[load](./load.md)、[loaddata](./loaddata.md)、[write](./write.md)、[readdata](./readdata.md)、[currentfilename](./currentfilename.md)、[rm](./rm.md)、[exist](./exist.md)