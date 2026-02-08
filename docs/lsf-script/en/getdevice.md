# getdevice

Returns the type of device used to run the simulation in the
[FDTD Resource Selection Group](https://optics.ansys.com/hc/en-us/articles/36952912384403-Ansys-Lumerical-FDTD-Modern-User-Interface#run_simulation_group).
This command can only be used if there is an FDTD simulation region present.

| **Syntax**     | **Description**                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| out=getdevice; | Returns the currently selected type of device used to run the simulation. The returned value is either “CPU” or “GPU”. |

**See Also**

[addresource](./addresource.md), [setresource](./setresource.md),
[deleteresource](./deleteresource.md),
[getresource](https://optics.ansys.com/hc/en-us/articles/360034931353-getresource-Script-command),
[run](https://optics.ansys.com/hc/en-us/articles/360034931333-run-Script-command),
[setdevice](https://optics.ansys.com/hc/en-us/articles/42996468347667-setdevice-Script-command)
