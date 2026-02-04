<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getlicenseestimateallactiveresources -->

# getlicenseestimateallactiveresources

**示例**

Two FDTD CPU resources are set up with enterprise license. The first resource has process = 16, threads =1, and capacity =4. The second resource has process = 8, threads =1, and capacity = 3.
    ?getlicenseestimateallactiveresources("FDTD","CPU");   
    #返回 ‘1 lumerical_solve AND (104 anshpc OR 9 anshpc_pack),’ indicating the 数字 of HPC packs needed to run 参数 sweep on both resources.

Two FDTD CPU resources are set up with enterprise license. The first resource has process = 16, threads =1, and capacity =4. The second resource has process = 8, threads =1, and capacity = 3.
    ?getlicenseestimateallactiveresources("FDTD","CPU");   
    #返回 ‘1 lumerical_solve AND (104 anshpc OR 9 anshpc_pack),’ indicating the 数字 of HPC packs needed to run 参数 sweep on both resources.

**另请参阅**

[Ansys optics solve, accelerator, and Ansys HPC license consumption](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption), [getlicenseestimate](https://optics.ansys.com/hc/en-us/articles/41005222267923-getlicenseestimate-Script-command), [islicensestandard](https://optics.ansys.com/hc/en-us/articles/41005466140691-islicensestandard-Script-command)
