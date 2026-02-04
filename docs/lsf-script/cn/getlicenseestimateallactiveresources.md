<!--
Translation from English documentation
Original command: getlicenseestimateallactiveresources
Translation date: 2026-02-04 22:50:00
-->

# getlicenseestimateallactiveresources

Obtain 该 数字 的 licenses needed 到 run 一个 参数 sweep 在 all active resources.

语法  |  描述   
---|---  
out = getlicenseestimateallactiveresources(“求解器”, “resource_type”); |  返回 一个 字符串 indicating 该 数字 的 licenses required 到 run 参数 sweep 在 all active resources specified 通过 该 resource_type 参数. If none 是 specified, defaults 到 “CPU”:

  * For FDTD, 该 参数 可以 either 为 “CPU” 或 “GPU”.
  * For all other solvers, 该 参数 可以 only 为 “CPU”.

  
  
**示例**

Two FDTD CPU resources 是 设置 up 使用 enterprise license. The first resource has process = 16, threads =1, 和 capacity =4. The second resource has process = 8, threads =1, 和 capacity = 3.
    
    
    ?getlicenseestimateallactiveresources("FDTD","CPU");   
    #返回 ‘1 lumerical_solve AND (104 anshpc OR 9 anshpc_pack),’ indicating 该 数字 的 HPC packs needed 到 run 参数 sweep 在 both resources.

**参见**

[Ansys optics solve, accelerator, and Ansys HPC license consumption](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption), [getlicenseestimate](https://optics.ansys.com/hc/en-us/articles/41005222267923-getlicenseestimate-Script-command), [islicensestandard](https://optics.ansys.com/hc/en-us/articles/41005466140691-islicensestandard-Script-command)
