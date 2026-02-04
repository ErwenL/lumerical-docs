<!-- Translated: 2024-01-XX by AI Assistant -->
<!-- Status: Initial translation -->
<!-- Review needed: Technical terms, consistency check -->

# runsweep

运行参数扫描或优化任务。

**语法** | **描述**  
---|---  
runsweep; | 运行所有扫描和优化任务。在 FDTD 中，这将使用 CPU 模式运行任务。  
runsweep("taskname"); | 仅运行名为 taskname 的扫描或优化。在 FDTD 中，这将使用 CPU 模式运行扫描或优化。  
runsweep("resource_type"); | 仅限 FDTD，使用指定的 resource_type 运行所有扫描和优化任务，"GPU" 或 "CPU"  
runsweep("taskname","resource_type"); | 仅限 FDTD，使用指定的 resource_type 运行名为 taskname 的扫描或优化，"CPU" 或 "GPU"。  

使用 [Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical) 时，

**语法** | **描述**  
---|---  
runsweep("taskname","resource_type", "burst", burst_settings); | 使用特定类型的资源运行单个参数扫描。如果扫描使用的求解器不支持 Ansys Cloud Burst Compute，则返回错误：

- taskname：要运行的扫描名称
- resource_type：要运行的资源类型，"CPU" 或 "GPU"
- burst_settings：可选，用于当前任务提交的设置结构。结构字段应与从 [getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command) 获得的结果相匹配。如果留空，使用默认设置。

runsweep("type","burst", burst_settings); | 使用指定的资源类型运行所有扫描。设置将应用于所有扫描。如果列表中的扫描不支持 Ansys Cloud Burst Compute，则返回错误：

- type：要运行的资源类型，"CPU" 或 "GPU"
- burst_settings：可选，用于当前任务提交的设置结构。结构字段应与从 [getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command) 获得的结果相匹配。如果留空，使用默认设置。

**示例**

```
runsweep;
runsweep("thickness_sweep");
```

**另见**

[run](run.md), [getsweepdata](getsweepdata.md), [addjob](addjob.md), [runjobs](runjobs.md), [参数扫描](https://optics.ansys.com/hc/en-us/articles/360034922873-Parameter-sweeps)
