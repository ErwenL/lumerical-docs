# getlicenseestimateallactiveresources

Obtain the number of licenses needed to run a parameter sweep on all active resources.

Syntax  |  Description   
---|---  
out = getlicenseestimateallactiveresources(“solver”, “resource_type”); |  Returns a string indicating the number of licenses required to run parameter sweep on all active resources specified by the resource_type parameter. If none is specified, defaults to “CPU”:

  * For FDTD, the parameter can either be “CPU” or “GPU”.
  * For all other solvers, the parameter can only be “CPU”.

  
  
**Example**

Two FDTD CPU resources are set up with enterprise license. The first resource has process = 16, threads =1, and capacity =4. The second resource has process = 8, threads =1, and capacity = 3.
    
    
    ?getlicenseestimateallactiveresources("FDTD","CPU");   
    #Returns ‘1 lumerical_solve AND (104 anshpc OR 9 anshpc_pack),’ indicating the number of HPC packs needed to run parameter sweep on both resources.

**See Also**

[Ansys optics solve, accelerator, and Ansys HPC license consumption](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption), [getlicenseestimate](https://optics.ansys.com/hc/en-us/articles/41005222267923-getlicenseestimate-Script-command), [islicensestandard](https://optics.ansys.com/hc/en-us/articles/41005466140691-islicensestandard-Script-command)
