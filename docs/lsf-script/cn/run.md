<!--
Translation Status: Completed
Source: docs/lsf-script/en/run.md
Last Updated: 2026-02-03
-->

# run

运行当前模拟。当模拟完成时，所有模拟数据将保存到当前模拟文件。然后更新后的模拟文件将被GUI重新加载。此函数不返回任何数据。

对于MODE、CHARGE、HEAT、FEEM、DGTD，

**语法** |  **说明**  
---|---  
run; |  以资源管理器中定义的并行模式启动模拟。  
run("solver"); |  使用指定的"solver"以资源管理器中定义的并行模式启动模拟。  
  
对于FDTD和RCWA，

**语法** |  **说明**  
---|---  
run;  
|  使用模拟器选项卡中[运行模拟组](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface)中设置的资源启动模拟。  
run("solver"); |  使用指定的"solver"启动模拟，使用模拟器选项卡中运行模拟组设置的资源。  
run("solver", "resource_type") |  使用solver和resource_type启动模拟：

  * solver：求解器名称，可以是"FDTD"、"RCWA"
  * resource_type：资源类型，对于FDTD可以是"CPU"、"GPU"，对于RCWA只能是"CPU"

这允许使用指定的资源而不影响模拟器选项卡中[运行模拟组](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface)中的CPU/GPU选择。  
run("solver", "resource_type", "resource_name"); |  使用solver、resource_type和指定的resource_name启动模拟：

  * solver：求解器名称，可以是"FDTD"、"RCWA"
  * resource_type：资源类型，对于FDTD可以是"CPU"、"GPU"，对于RCWA只能是"CPU"
  * resource_name：资源名称，必须遵循[资源配置窗口](https://optics.ansys.com/hc/en-us/articles/360058790674-Resource-configuration-elements-and-controls)中设置的资源

  
  
run("FDTD", "GPU", "resource_name", CUDA_VISIBLE_DEVICE_values); |  使用指定的resource_name和CUDA_VISIBLE_DEVICE_values启动FDTD GPU模拟：

  * resource_name：资源名称，必须遵循资源配置窗口中设置的资源
  * CUDA_VISIBLE_DEVICE_values：由环境变量CUDA_VISIBLE_DEVICE指定的要使用的GPU，可以是单个值或表示多个GPU的矩阵

  
  
对于INTERCONNECT，

**语法** |  **说明**  
---|---  
run; |  启动模拟。模拟将使用资源管理器中第一个活动资源的设置运行。  
  
当使用[Ansys Cloud Burst Compute for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical)时，

**语法** |  **说明**  
---|---  
run("solver", "resource_type", "burst", burst_settings); |  提交当前突发作业：

  * solver：求解器名称，目前仅支持"FDTD"
  * resource_type：模拟运行类型，可以是"CPU"或"GPU"
  * burst_settings：可选，用于当前作业提交的结构体设置。结构体字段应与[getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command)获得的结果匹配。

  
  
**示例**

在FDTD中创建并运行新模拟。
    
    
    newproject;    # 创建新模拟文件
    addfdtd;       # 添加FDTD模拟区域
    adddipole;     # 添加偶极子源
    run;           # 以并行模式运行模拟

**另请参见**

- [runanalysis](./runanalysis.md)
- [addjob](./addjob.md)
- [runjobs](./runjobs.md)
- [save](./save.md)
- [load](./load.md)
