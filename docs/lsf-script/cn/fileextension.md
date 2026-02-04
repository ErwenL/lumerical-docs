# fileextension

从字符串中获取文件扩展名。

**语法** | **描述**
---|---
out = fileextension( "name.ext"); | 以字符串形式返回文件扩展名。

**示例**

从完整文件名中分离出文件扩展名。

```powershell
?fileextension("C:/Users/myname/Documents/FDTD/myfile.fsp");
fsp
```

使用以下代码检查您正在使用的产品。如果您正在编写将在多个产品之间共享的脚本，这会很有帮助。

```powershell
save("myfile");
if(fileextension(currentfilename)=="fsp") { ?"Using FDTD"; }
if(fileextension(currentfilename)=="lms") { ?"Using MODE"; }
if(fileextension(currentfilename)=="ldev") { ?"Using Finite Element IDE"; }
if(fileextension(currentfilename)=="icp") { ?"Using INTERCONNECT"; }
```

**另请参阅**

[命令列表](../命令列表.md)、[currentfilename](./currentfilename.md)、[getpath](./getpath.md)、[which](./which.md)、[pwd](./pwd.md)、[filedirectory](./filedirectory.md)、[filebasename](./filebasename.md)