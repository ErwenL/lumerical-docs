<!--
Translation from English documentation
Original command: getresource
Translation date: 2026-02-04 22:50:00
-->

# getresource

Returns the current setting for properties of the available resources in resource manager for the specified solver. This command is also used to obtain submittable fields for [Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical).

For all resources except Ansys Cloud Burst Compute™ 用于 Lumerical:

**语法** |  **描述**  
---|---  
out=getresource("求解器", resource_num, "属性"); |  返回 该 current setting 用于 属性 的 该 available resources 在 resource manager 用于 该 specified 求解器. The "求解器" 参数 是 used 到 select 该 求解器 从 该 该 resource 是 being 选中的. The "求解器" 参数 是 not supported 通过 INTERCONNECT. resource_num 是 该 数字 的 该 desired resource (row 数字 在 resource manager) 和 是 optional. If not specified, 该 命令 将 返回 该 数字 的 resources currently available 用于 该 specified 求解器. "属性" 是 该 desired 属性 的 该 resource 和 是 optional. If not specified, 该 命令 将 返回 一个 list 的 all 属性 available 用于 该 resource.   
  
When using [Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical):

**语法** |  **描述**  
---|---  
out=getresource("burst"); |  返回 一个 结构 containing burst settings. The fields 的 该 output 结构 是 described below.  
out = getresource(“burst”,”accounts”);  |  返回 一个 list 的 available burst accounts 到 choose 从.  
out = getresource(“burst”, “name”, “resource_type”); |  返回 一个 list 的 available queues 用于 该 account specified 通过 该 参数 name.  
The queue 类型, as specified 通过 该 resource_type 参数, 可以 either 为 “GPU” 用于 一个 list 的 all GPU queues, 或 “CPU” 用于 一个 list 的 all CPU queues.  
  
The 结构 returned 通过 `getresource("burst")` 是 described below. These 是 该 fields 该 可以 为 modified during job submission.

The settings for Ansys Cloud Burst Compute for Lumerical will be reverted to default after every job submission. As such, the values of each field will be their default values. To modify settings during job submission, see [run](https://optics.ansys.com/hc/en-us/articles/360034931333-run-Script-command) and [runsweep](https://optics.ansys.com/hc/en-us/articles/360034931413-runsweep-Script-command).

**Field** |  **描述**  
---|---  
account | Current account name.  
download | Whether or not to download the results after simulation completion. This is 0 if the results are not downloaded, and 1 if the results are downloaded. The results can be downloaded from [Ansys Engineering Portal](https://portal.ansys.com/) if automatic download is disabled.  
jobMonitoring | Whether 或 not job monitoring 从 该 GUI 是 enabled. This result 0 如果 you 是 not monitoring 该 job 在 该 GUI. An Ansys Engineering Portal link 到 该 job 是 provided 在 该 脚本 prompt 当 you submit 一个 job without monitoring.  
name | Name 的 该 current Ansys Cloud Burst Compute job.  
queue | Name 的 该 queue 到 为 used 用于 该 job. By default, 此 将 为 empty 到 indicate 该 一个 queue 将 为 automatically 选中的.  
You 可以 find 一个 list 的 queues 使用 该 `getresource("burst","name","类型")` 命令 documented above.  
  
**示例**

This example 将 返回 该 数字 的 processes currently 设置 用于 该 second resource 的 该 DGTD 求解器 在 Finite Element IDE
    
    
    out=getresource("DGTD",2,"processes");

**参见**

[addresource](/hc/en-us/articles/360034410734-addresource), [setresource](/hc/en-us/articles/360034410754-setresource), [deleteresource](/hc/en-us/articles/360034410794-deleteresource)
