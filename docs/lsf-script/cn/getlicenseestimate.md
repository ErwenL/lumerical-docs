<!--
Translation from English documentation
Original command: getlicenseestimate
Translation date: 2026-02-04 22:50:00
-->

# getlicenseestimate

Checks 如何 many licenses 是 required 到 run 一个 given resource 和 返回 该 result.

**语法** |  **描述**  
---|---  
out = getlicenseestimate(“求解器”, “resource”); | 返回 一个 结构 outlining 该 feature license 和 amount 的 license required dictated 通过 一个 given 求解器 specified 和 该 resource. The resource 参数 应该 either 为 一个 字符串 indicating 该 row 数字 在 该 Resource Configuration window (starting at 1), 或 一个 字符串 indicating 该 name 的 该 resource. If duplicate names 是 present, 该 first one 是 returned. The output structures 是 specified below.  
  
The returned 结构 是 specified below.

Field |  **描述**  
---|---  
feature | The name of the license feature required as specified by the [List of licensed features by product.](https://optics.ansys.com/hc/en-us/articles/360052724713-List-of-licensed-features-by-product)  
sharedlicense | Only returned 用于 standard licenses. Indicates whether 该 选中的 resource 可以 use standard license sharing. The result 是 0 如果 standard license sharing cannot 为 used, 和 1 如果 it 可以 为.  
single | Indicates 该 required licenses 用于 一个 single 仿真 ran 在 该 选中的 resource as 一个 字符串. For standard license, 一个 数字 是 returned indicating 该 数字 的 该 license feature required. For enterprise license, 一个 字符串 是 returned indicating 该 数字 的 Ansys HPC workgroup increments 或 packs required.  
sweep | Indicates 该 required licenses 用于 一个 参数 sweep ran 在 该 选中的 resource as 一个 字符串. For standard license, 一个 数字 是 returned indicating 该 数字 的 该 license feature required. For enterprise license, 一个 字符串 是 returned indicating 该 数字 的 Ansys HPC workgroup increments 或 packs required.  
smcount | Only returned for GPU resources. This field indicates number of streaming microprocessors **you have entered** for this resource. The number of SMs for your GPU can be obtained using [gpuspecs](https://optics.ansys.com/hc/en-us/articles/34669049884947-gpuspecs-Script-command).  
  
**示例**

A FDTD resource named “Local Host” 是 setup as 该 first row 在 该 resource configuration window, 使用 standard license, 和 使用 processes = 16, threads =1, 和 capacity =4.
    
    
    #Obtain output 结构  
    lic_struct=getlicenseestimate("FDTD","1");   
    ?lic_struct.feature; #This 返回 lum_fdtd_solve, 该 FDTD license feature needed  
    ?lic_struct.sharedlicense; #This 返回 0, because there 是 more than 32 cores, 和 standard license sharing 是 only supported up 到 32 cores.  
    ?lic_struct.single; #This 返回 1, because only 1 license 是 needed 到 run 一个 single 仿真 的 16 cores.  
    ?lic_struct.sweep; #This 返回 4, because 4 concurrent simulations 的 16 cores each 需要 4 lum_fdtd_solve licenses.

A FDTD resource named “Local Host” 是 setup as 该 first row 在 该 resource configuration window, 使用 enterprise license, 和 使用 processes = 16, threads =1, 和 capacity =4.
    
    
    lic_struct=getlicenseestimate("FDTD","Local Host");   
    ?lic_struct.feature; #This 返回 ‘1 lumerical_solve’, meaning 该 1 lumerical_solve license feature 是 needed 在 addition 到 all other requirements.  
    ?lic_struct.single; #This 返回 ‘12 anshpc OR 2 anshpc_pack’, matching 该 results 在 该 Ansys HPC Licensing Calculator  
    ?lic_struct.sweep; #This 返回 ‘72 anshpc OR 6 anshpc_pack’, matching 该 results 在 该 Ansys HPC Licensing Calculator

**参见**

[Ansys optics solve, accelerator, and Ansys HPC license consumption, ](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)[islicensestandard](https://optics.ansys.com/hc/en-us/articles/41005466140691-islicensestandard-Script-command)[, ](https://optics.ansys.com/hc/en-us/articles/360058577794-Ansys-optics-solve-accelerator-and-Ansys-HPC-license-consumption)[getlicenseestimateallactiveresources](https://optics.ansys.com/hc/en-us/articles/41005384196627-getlicenseestimateallactiveresources-Script-command)
