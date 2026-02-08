# getlicenseestimate

Checks how many licenses is required to run a given resource and returns the result.

| **Syntax**                                      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = getlicenseestimate(“solver”, “resource”); | Returns a structure outlining the feature license and amount of license required dictated by a given solver specified and the resource. The resource parameter should either be a string indicating the row number in the Resource Configuration window (starting at 1), or a string indicating the name of the resource. If duplicate names are present, the first one is returned. The output structures are specified below. |

The returned structure is specified below.

| Field         | **Description**                                                                                                                                                                                                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| feature       | The name of the license feature required as specified by the [List of licensed features by product.](https://optics.ansys.com/hc/en-us/articles/360052724713-List-of-licensed-features-by-product)                                                                                                                          |
| sharedlicense | Only returned for standard licenses. Indicates whether the selected resource can use standard license sharing. The result is 0 if standard license sharing cannot be used, and 1 if it can be.                                                                                                                              |
| single        | Indicates the required licenses for a single simulation ran on the selected resource as a string. For standard license, a number is returned indicating the number of the license feature required. For enterprise license, a string is returned indicating the number of Ansys HPC workgroup increments or packs required. |
| sweep         | Indicates the required licenses for a parameter sweep ran on the selected resource as a string. For standard license, a number is returned indicating the number of the license feature required. For enterprise license, a string is returned indicating the number of Ansys HPC workgroup increments or packs required.   |
| smcount       | Only returned for GPU resources. This field indicates number of streaming microprocessors **you have entered** for this resource. The number of SMs for your GPU can be obtained using [gpuspecs](https://optics.ansys.com/hc/en-us/articles/34669049884947-gpuspecs-Script-command).                                       |

**Example**

A FDTD resource named “Local Host” is setup as the first row in the resource
configuration window, with standard license, and with processes = 16, threads =1, and
capacity =4.

```
#Obtain output structure  
lic_struct=getlicenseestimate("FDTD","1");   
?lic_struct.feature; #This returns lum_fdtd_solve, the FDTD license feature needed  
?lic_struct.sharedlicense; #This returns 0, because there are more than 32 cores, and standard license sharing is only supported up to 32 cores.  
?lic_struct.single; #This returns 1, because only 1 license is needed to run a single simulation of 16 cores.  
?lic_struct.sweep; #This returns 4, because 4 concurrent simulations of 16 cores each requires 4 lum_fdtd_solve licenses.
```

A FDTD resource named “Local Host” is setup as the first row in the resource
configuration window, with enterprise license, and with processes = 16, threads =1, and
capacity =4.

```
lic_struct=getlicenseestimate("FDTD","Local Host");   
?lic_struct.feature; #This returns ‘1 lumerical_solve’, meaning that 1 lumerical_solve license feature is needed in addition to all other requirements.  
?lic_struct.single; #This returns ‘12 anshpc OR 2 anshpc_pack’, matching the results on the Ansys HPC Licensing Calculator  
?lic_struct.sweep; #This returns ‘72 anshpc OR 6 anshpc_pack’, matching the results on the Ansys HPC Licensing Calculator
```

**See Also**

[Ansys optics solve, accelerator, and Ansys HPC license consumption, ](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)[islicensestandard](https://optics.ansys.com/hc/en-us/articles/41005466140691-islicensestandard-Script-command)[, ](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)[getlicenseestimateallactiveresources](https://optics.ansys.com/hc/en-us/articles/41005384196627-getlicenseestimateallactiveresources-Script-command)
