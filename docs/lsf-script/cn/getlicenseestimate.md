<!-- Translation completed: 2026-02-04 -->
<!-- Original command: getlicenseestimate -->

# getlicenseestimate

**语法** | **描述**
---|---
out = getlicenseestimate(“solver”, “resource”); | 返回 a structure outlining the feature license and amount of license required dictated by a given 求解器 specified and the resource. The resource 参数 should either be a 字符串 indicating the row 数字 in the Resource Configuration window (starting at 1), or a 字符串 indicating the name of the resource. If duplicate names are present, the first one is returned. The 输出 structures are specified below.
feature | The name of the license feature required as specified by the [List of licensed features by product.](https://optics.ansys.com/hc/en-us/articles/360052724713-List-of-licensed-features-by-product)
sharedlicense | Only returned for standard licenses. Indicates whether the selected resource can use standard license sharing. The result is 0 if standard license sharing cannot be used, and 1 if it can be.
single | Indicates the required licenses for a single 仿真 ran on the selected resource as a 字符串. For standard license, a 数字 is returned indicating the 数字 of the license feature required. For enterprise license, a 字符串 is returned indicating the 数字 of Ansys HPC workgroup increments or packs required.
sweep | Indicates the required licenses for a 参数 sweep ran on the selected resource as a 字符串. For standard license, a 数字 is returned indicating the 数字 of the license feature required. For enterprise license, a 字符串 is returned indicating the 数字 of Ansys HPC workgroup increments or packs required.
smcount | Only returned for GPU resources. This 场 indicates 数字 of streaming microprocessors **you have entered** for this resource. The 数字 of SMs for your GPU can be obtained using [gpuspecs](https://optics.ansys.com/hc/en-us/articles/34669049884947-gpuspecs-脚本-命令).

**示例**

A FDTD resource named “Local Host” is setup as the first row in the resource configuration window, with standard license, and with processes = 16, threads =1, and capacity =4.
    #Obtain 输出 structure  
    lic_struct=getlicenseestimate("FDTD","1");   
    ?lic_struct.feature; #This 返回 lum_fdtd_solve, the FDTD license feature needed  
    ?lic_struct.sharedlicense; #This 返回 0, because there are more than 32 cores, and standard license sharing is only supported up to 32 cores.  
    ?lic_struct.single; #This 返回 1, because only 1 license is needed to run a single 仿真 of 16 cores.  
    ?lic_struct.sweep; #This 返回 4, because 4 concurrent simulations of 16 cores each requires 4 lum_fdtd_solve licenses.
A FDTD resource named “Local Host” is setup as the first row in the resource configuration window, with enterprise license, and with processes = 16, threads =1, and capacity =4.
    lic_struct=getlicenseestimate("FDTD","Local Host");   
    ?lic_struct.feature; #This 返回 ‘1 lumerical_solve’, meaning that 1 lumerical_solve license feature is needed in addition to all other requirements.  
    ?lic_struct.single; #This 返回 ‘12 anshpc OR 2 anshpc_pack’, matching the results on the Ansys HPC Licensing Calculator  
    ?lic_struct.sweep; #This 返回 ‘72 anshpc OR 6 anshpc_pack’, matching the results on the Ansys HPC Licensing Calculator

A FDTD resource named “Local Host” is setup as the first row in the resource configuration window, with standard license, and with processes = 16, threads =1, and capacity =4.
    #Obtain 输出 structure  
    lic_struct=getlicenseestimate("FDTD","1");   
    ?lic_struct.feature; #This 返回 lum_fdtd_solve, the FDTD license feature needed  
    ?lic_struct.sharedlicense; #This 返回 0, because there are more than 32 cores, and standard license sharing is only supported up to 32 cores.  
    ?lic_struct.single; #This 返回 1, because only 1 license is needed to run a single 仿真 of 16 cores.  
    ?lic_struct.sweep; #This 返回 4, because 4 concurrent simulations of 16 cores each requires 4 lum_fdtd_solve licenses.
A FDTD resource named “Local Host” is setup as the first row in the resource configuration window, with enterprise license, and with processes = 16, threads =1, and capacity =4.
    lic_struct=getlicenseestimate("FDTD","Local Host");   
    ?lic_struct.feature; #This 返回 ‘1 lumerical_solve’, meaning that 1 lumerical_solve license feature is needed in addition to all other requirements.  
    ?lic_struct.single; #This 返回 ‘12 anshpc OR 2 anshpc_pack’, matching the results on the Ansys HPC Licensing Calculator  
    ?lic_struct.sweep; #This 返回 ‘72 anshpc OR 6 anshpc_pack’, matching the results on the Ansys HPC Licensing Calculator

**另请参阅**

[Ansys optics solve, accelerator, and Ansys HPC license consumption, ](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)[islicensestandard](https://optics.ansys.com/hc/en-us/articles/41005466140691-islicensestandard-Script-command)[, ](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)[getlicenseestimateallactiveresources](https://optics.ansys.com/hc/en-us/articles/41005384196627-getlicenseestimateallactiveresources-Script-command)
