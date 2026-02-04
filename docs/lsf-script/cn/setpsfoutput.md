<!--
---
title: setpsfoutput
command_type: property
---
-->

# setpsfoutput

指定PSF文件夹的位置，避免在协同仿真中使用网表位置作为参考。

默认情况下，INTERCONNECT使用网表路径创建PSF路径。`setpsfoutput`命令允许用户指定PSF文件夹的位置，而不是使用默认的网表路径。

**语法** | **描述**
---|---
`setpsfoutput("path")` | 指定PSF文件夹的位置。

**示例**

以下脚本命令将导入网表、保存文件并将输出数据保存到3个不同位置的PSF文件夹。

```
static const char* InitScript =
"new;"
"historyoff;"
"setpsfoutput(\"%path3%\");"
"importnetlist(\"%path1%\");"
"save(\"%path2%\");"
"edacosimulation;"
"setnamed('::Root Element','simulation output','psf');"
"runinitialize;";
```

**另请参阅**

- [命令列表](list-of-commands.md), [stlimport](stlimport.md)
