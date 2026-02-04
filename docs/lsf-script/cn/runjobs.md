<!-- Translated: 2024-01-XX by AI Assistant -->
<!-- Status: Initial translation -->
<!-- Review needed: Technical terms, consistency check -->

# runjobs

运行任务管理器队列中的所有仿真。脚本执行将暂停，直到所有仿真成功完成，然后继续执行。如果发生错误，脚本将不会继续执行。

适用于 Ansys Lumerical FDTD™、Ansys Lumerical MODE™、Ansys Lumerical Multiphysics™ 和 Ansys Lumerical INTERCONNECT™

**语法** | **描述**  
---|---  
runjobs; | 为现有（活动的）求解器运行任务队列中的任务。使用资源管理器中指定的计算机资源和并行设置。  
runjobs("solver", option); | 为指定求解器运行任务队列中的任务。option=0：以单进程模式仅使用本地计算机运行任务。option=1：使用资源管理器中指定的计算机资源和并行设置运行任务（默认）。  

使用 [Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical) 时，

**语法** | **描述**  
---|---  
runjobs("solver", "resource_type", "burst", burst_settings); | 使用 Ansys Cloud Burst Compute™ for Lumerical 为指定求解器运行任务队列中的任务：

- solver：求解器名称，目前仅支持 "FDTD"
- resource_type：仿真运行类型，"CPU" 或 "GPU"
- burst_settings：用于当前任务提交的设置结构。结构字段应与从 getresource 获得的结果相匹配。"queue" 字段必须在此结构中指定。任何留空的字段使用默认设置。

**示例**

以下脚本代码演示如何使用 addjob 和 runjobs 脚本命令进行参数扫描。初始 for 循环为扫描中的每个点创建一个仿真文件，并将仿真添加到任务队列中。接下来，runjobs 命令将运行任务队列中的所有仿真。如果资源管理器中配置了多个计算机资源，则仿真将并发运行。当所有仿真完成后，第二个 for 循环用于重新加载每个仿真文件并进行所需的分析。

```
# 创建 10 个仿真文件并添加到任务队列
newproject;
addvarfdtd;
adddipole;
addcircle;
rad=linspace(1e-6,10e-6,10);
for(i=1:10) {
setnamed("circle","radius",rad(i));
save("temp_"+num2str(i));
addjob(currentfilename);
}

# 运行任务队列中的所有任务
runjobs;

# 加载每个仿真并进行所需的分析
for(i=1:10) {
 load("temp_"+num2str(i));
 ...
}
```

**另见**

[run](run.md), [runsweep](runsweep.md), [addjob](addjob.md), [clearjobs](clearjobs.md), [listjobs](listjobs.md), [save](save.md), [load](load.md)
