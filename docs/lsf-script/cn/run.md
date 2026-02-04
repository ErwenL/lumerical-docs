<!--
Translation from English documentation
Original command: run
Translation date: 2026-02-04 22:50:14
-->

# run

Run 该 current 仿真. When 该 仿真 finishes, all 仿真 数据 将 为 saved 到 该 current 仿真 文件. The updated 仿真 文件 将 那么 为 re-loaded 通过 该 GUI. This 函数 does not 返回 any 数据.

For MODE, CHARGE, HEAT, FEEM, DGTD,

**语法** |  **描述**  
---|---  
run; |  Launch 该 仿真 在 parallel mode as defined 在 该 resource manager.  
run(“求解器”); |  Launch 该 仿真 使用 该 specified “求解器” 在 parallel mode as defined 在 该 resource manager.  
  
For FDTD 和 RCWA,

**语法** |  **描述**  
---|---  
run;  
|  Launch the simulation using the resource set in the [run simulation group](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface) of the simulator tab.  
run("求解器"); |  Launch 该 仿真 使用 该 specified “求解器”, 使用 该 resource 设置 在 该 run 仿真 group 的 该 simulator tab.  
run("求解器", "resource_type") |  Launch 该 仿真 使用 求解器 和 resource_type:

  * 求解器: 求解器 name, 可以 为 “FDTD”, “RCWA”
  * resource_type: resource 类型, 可以 为 "CPU", "GPU" 用于 FDTD, 和 “CPU” only 用于 RCWA

This allows to use the specified resource without affecting the CPU/GPU selection set in the [run simulation group](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface) of the simulator tab.  
run("求解器", "resource_type", "resource_name"); |  Launch 该 仿真 使用 求解器, resource_type, 和 使用 一个 specified resource_name:

  * 求解器: 求解器 name, 可以 为 “FDTD”, “RCWA”
  * resource_type: resource 类型, 可以 为 "CPU", "GPU" 用于 FDTD, 和 “CPU” only 用于 RCWA
  * resource_name: resource name, must follow a resource set in the [resource configuration window](https://optics.ansys.com/hc/en-us/articles/360058790674-Resource-configuration-elements-and-controls)

  
run("FDTD", "GPU", "resource_name", CUDA_VISIBLE_DEVICE_values); |  Launch 一个 FDTD GPU 仿真 使用 一个 specified resource_name 和 CUDA_VISIBLE_DEVICE_values:

  * resource_name: resource name, 必须 follow 一个 resource 设置 在 该 resource configuration window
  * CUDA_VISIBLE_DEVICE_values: GPUs 到 为 used specified 通过 该 环境 变量 CUDA_VISIBLE_DEVICE, 可以 为 一个 single 值 或 一个 矩阵 representing multiple GPUs

  
  
For INTERCONNECT,

**语法** |  **描述**  
---|---  
run; |  Launch 该 仿真. The 仿真 将 为 run 使用 该 settings 从 该 first active resource 在 该 resource manager.  
  
When using [Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical),

**语法** |  **描述**  
---|---  
run(“求解器”, “resource_type”, “burst”, burst_settings); |  Submits 该 current burst job:

  * 求解器: Name 的 该 求解器, currently, only “FDTD” 是 supported
  * resource_type: Type 的 仿真 到 run, either “CPU” 或 “GPU”
  * burst_settings: Optional, settings structure to use for the current job submission. The structure fields should match the results obtained from [getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command).

  
  
**示例**

创建 和 run 一个 新的 仿真 在 FDTD.
    
    
    newproject;  # 创建 一个 新的 仿真 文件
    addfdtd;    # 添加 该 FDTD 仿真 region
    adddipole;   # 添加 一个 diopole 源
    run;      # run 该 仿真 在 parallel mode

**参见**

[ runanalysis ](/hc/en-us/articles/360034409874-runanalysis) , [ addjob ](/hc/en-us/articles/360034410714-addjob) , [ runjobs ](/hc/en-us/articles/360034931373-runjobs) , [ save ](/hc/en-us/articles/360034410814-save) , [ load](/hc/en-us/articles/360034410834-load), [FDTD GPU Solver Information](/hc/en-us/articles/17518942465811)
