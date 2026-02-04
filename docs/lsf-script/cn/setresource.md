# setresource

> **原文**: setresource  
> **翻译日期**: 2026-02-03  
> **翻译状态**: ✅ 已完成

为指定求解器设置资源管理器中可用资源的属性。

| **语法** | **说明** |
| --- | --- |
| setresource("solver", resource_num, "property", "value"); | 为指定求解器设置资源管理器中可用资源的属性。"solver"参数用于选择要从中选择资源的求解器。INTERCONNECT不支持"solver"参数。resource_num是所需资源的编号（资源管理器中的行号）。如果未指定，该命令将返回指定求解器当前可用的资源数量。"property"是资源的所需属性，"value"是要为指定属性设置的值。 |

**注意**：在安全模式下运行脚本时，不能使用此命令设置mpi可执行文件。

**示例**

此示例将DGTD求解器的第二个资源的进程数设置为4：

```
setresource("DGTD",2,"processes","4");
```

**相关命令**

[addresource](./addresource.md), [deleteresource](./deleteresource.md), [getresource](./getresource.md)
