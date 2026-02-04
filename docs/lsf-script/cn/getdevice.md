<!--
Translation from English documentation
Original command: getdevice
Translation date: 2026-02-04 22:49:59
-->

# getdevice

Returns the type of device used to run the simulation in the [FDTD Resource Selection Group](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface#run_simulation_group). This command can only be used if there is an FDTD simulation region present.

**语法** |  **描述**  
---|---  
out=getdevice; | 返回 该 currently 选中的 类型 的 device used 到 run 该 仿真. The returned 值 是 either “CPU” 或 “GPU”.   
  
**参见**

[addresource](https://optics.ansys.com/hc/en-us/articles/360034410734-addresource), [setresource](https://optics.ansys.com/hc/en-us/articles/360034410754-setresource), [deleteresource](https://optics.ansys.com/hc/en-us/articles/360034410794-deleteresource), [getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command), [run](https://optics.ansys.com/hc/en-us/articles/360034931333-run-Script-command), [setdevice](https://optics.ansys.com/hc/en-us/articles/42996468347667-setdevice-Script-command)
