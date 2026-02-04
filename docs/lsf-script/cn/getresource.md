<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getresource -->

# getresource

**语法** | **描述**
---|---
out=getresource("solver", resource_num, "property"); | 返回 the current setting for properties of the available resources in resource manager for the specified 求解器. The "求解器" 参数 is used to select the 求解器 from which the resource is being selected. The "求解器" 参数 is not supported by INTERCONNECT. resource_num is the 数字 of the desired resource (row 数字 in resource manager) and is optional. If not specified, the 命令 will 返回 the 数字 of resources currently available for the specified 求解器. "property" is the desired property of the resource and is optional. If not specified, the 命令 will 返回 a list of all properties available for the resource.
out=getresource("burst"); | 返回 a structure containing burst settings. The fields of the 输出 structure are described below.
out = getresource(“burst”,”accounts”); | 返回 a list of available burst accounts to choose from.
out = getresource(“burst”, “name”, “resource_type”); | 返回 a list of available queues for the account specified by the 参数 name.
account | Current account name.
download | Whether or not to download the results after 仿真 completion. This is 0 if the results are not downloaded, and 1 if the results are downloaded. The results can be downloaded from [Ansys Engineering Portal](https://portal.ansys.com/) if automatic download is disabled.
jobMonitoring | Whether or not job monitoring from the GUI is enabled. This result 0 if you are not monitoring the job in the GUI. An Ansys Engineering Portal link to the job is provided in the 脚本 prompt when you submit a job without monitoring.
name | Name of the current Ansys Cloud Burst Compute job.
queue | Name of the queue to be used for the job. By default, this will be 空 to indicate that a queue will be automatically selected.

**示例**

This 示例 will 返回 the 数字 of processes currently set for the second resource of the DGTD 求解器 in Finite 元素 IDE
    out=getresource("DGTD",2,"processes");

This 示例 will 返回 the 数字 of processes currently set for the second resource of the DGTD 求解器 in Finite 元素 IDE
    out=getresource("DGTD",2,"processes");

**另请参阅**

[addresource](/hc/en-us/articles/360034410734-addresource), [setresource](/hc/en-us/articles/360034410754-setresource), [deleteresource](/hc/en-us/articles/360034410794-deleteresource)
