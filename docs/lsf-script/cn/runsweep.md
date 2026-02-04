<!--
Translation from English documentation
Original command: runsweep
Translation date: 2026-02-04 22:50:14
-->

# runsweep

Runs 一个 参数 sweep 或 optimization task.

**语法** |  **描述**  
---|---  
runsweep; |  Runs all sweeps 和 optimization tasks. In FDTD, 此 将 run tasks 在 CPU mode.  
runsweep("taskname"); |  Runs only 该 sweep 或 optimization named taskname. In FDTD, 此 将 run 该 sweep 或 optimization 在 CPU mode.  
runsweep(“resource_type”); |  FDTD only, runs all sweeps 和 optimization tasks 使用 一个 specified resource_type, either “GPU” 或 “CPU”  
runsweep("taskname",”resource_type”); |  FDTD only, runs 该 sweep 或 optimization named taskname 使用 一个 specified resource_type, either “CPU” 或 “GPU”.  
  
When using [Ansys Cloud Burst Compute™ for Lumerical](https://optics.ansys.com/hc/en-us/articles/39824576734867-Ansys-Cloud-Burst-Compute-for-Lumerical),

**语法** |  **描述**  
---|---  
runsweep(“taskname”,”resource_type”, “burst”, burst_settings); |  Run 一个 single 参数 sweep 使用 一个 specific 类型 的 resource. An error 是 returned 在 该 sweep uses 一个 求解器 该 does not support Ansys Cloud Burst Compute:

  * taskname: Name 的 sweep 到 run
  * resource_type: Type 的 resource 到 run, either “CPU” 或 “GPU”
  * burst_settings: Optional, settings structure to use for the current job submission. The structure fields should match the results obtained from [getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command). If left empty, default settings are used.

  
runsweep(“类型”,”burst”, burst_settings); |  Run all sweeps 使用 该 specified resource 类型. The settings 是 applied 到 all sweeps. An error 是 returned 如果 一个 sweep 在 该 list does not support Ansys Cloud Burst Compute:

  * 类型: Type 的 resource 到 run, either “CPU” 或 “GPU”
  * burst_settings: Optional, settings structure to use for the current job submission. The structure fields should match the results obtained from [getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command). If left empty, default settings are used.

  
  
**示例**
    
    
    runsweep;
    runsweep("thickness_sweep");

**参见**

[ run ](/hc/en-us/articles/360034931333-run) , [ getsweepdata ](/hc/en-us/articles/360034409794-getsweepdata) , [ addjob ](/hc/en-us/articles/360034410714-addjob) , [ runjobs ](/hc/en-us/articles/360034931373-runjobs) , [ 参数 sweeps ](/hc/en-us/articles/360034922873-Parameter-sweeps)
