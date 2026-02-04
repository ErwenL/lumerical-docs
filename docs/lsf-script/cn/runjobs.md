<!--
Translation from English documentation
Original command: runjobs
Translation date: 2026-02-04 22:50:14
-->

# runjobs

Run all simulations 在 该 job manager queue. The 脚本 execution 将 为 paused while 该 jobs run, 那么 resume 当 all 的 该 simulations have completed successfully. If errors occur, 该 脚本 将 not proceed.

For Ansys Lumerical FDTD™, Ansys Lumerical MODE™, Ansys Lumerical Multiphysics™, 和 Ansys Lumerical INTERCONNECT™

**语法** |  **描述**  
---|---  
runjobs; |  Run jobs 在 该 Job queue 用于 existing (active) 求解器. Use 该 computer resources 和 parallel settings 该 是 specified 在 该 Resource Manager.  
runjobs("求解器", option); |  Run jobs 在 该 Job queue 用于 specified 求解器. option=0: run jobs 在 single process mode 使用 only 该 local computer. option=1: run jobs 使用 该 computer resources 和 parallel settings 该 是 specified 在 该 Resource Manager. (default)  
  
When using [Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical),

**语法** |  **描述**  
---|---  
runjobs(“求解器”, “resource_type”, “burst”, burst_settings); |  Run jobs 在 该 job queue 用于 该 specified 求解器 使用 Ansys Cloud Burst Compute™ 用于 Lumerical:

  * 求解器: Name 的 该 求解器, currently, only “FDTD” 是 supported
  * resource_type: Type 的 仿真 到 run, either “CPU” 或 “GPU”
  * burst_settings: Settings 结构 到 use 用于 该 current job submission. The 结构 fields 应该 match 该 results obtained 从 getresource. The “queue” field 必须 为 specified 在 此 结构. Any fields left blank uses default settings.

  
  
**示例**

The following 脚本 code illustrates 如何 到 use 该 addjob 和 runjobs 脚本 commands 到 do 一个 参数 sweep. The initial 用于 loop 创建 一个 仿真 文件 用于 each point 在 该 sweep 和 添加 该 simulations 到 该 job queue. Next, 该 runjobs 命令 将 run all simulations 在 该 job queue. If multiple computer resources 是 configured 在 该 Resource Manager, 那么 simulations 将 run concurrently. When all 的 该 simulations 是 complete, 一个 second 用于 loop 是 used 到 re-load each 仿真 文件 和 do 该 required 分析.
    
    
    # 创建 10 仿真 files 和 添加 them 到 该 job queue
    newproject;
    addvarfdtd;
    adddipole;
    addcircle;
    rad=linspace(1e-6,10e-6,10);
    用于(i=1:10) {
    setnamed("circle","radius",rad(i));
    save("temp_"+num2str(i));
    addjob(currentfilename);
    }
    runjobs;
    # run all jobs 在 该 job queue
    runjobs;
    # load each 仿真 和 do required 分析
    用于(i=1:10) {
     load("temp_"+num2str(i));
     ...
    }

**参见**

[ run ](/hc/en-us/articles/360034931333-run) , [ runsweep ](/hc/en-us/articles/360034931413-runsweep) , [ addjob ](/hc/en-us/articles/360034410714-addjob) , [ clearjobs ](/hc/en-us/articles/360034931393-clearjobs) , [ listjobs ](/hc/en-us/articles/360034410774-listjobs) , [ save ](/hc/en-us/articles/360034410814-save) , [ load ](/hc/en-us/articles/360034410834-load)
