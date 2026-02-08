# updatemodes

Updates the mode profile(s) of selected mode expansion monitor If there are no mode
profiles stored in the mode expansion monitor, then the mode with the highest effective
index will be selected. If mode profiles are already stored in the mode expansion
monitor, then the modes with the best overlap with the old modes will be selected. Note
that the mode expansion monitor must be selected before running this command.

| **Syntax**                | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| updatemodes;              | Updates mode profile of the selected mode expansion monitor. Returns 1 if the update was successful and -1 if not.                                                                                                                                                                                                                                                                                                                                                       |
| updatemodes(mode_number); | Updates the mode expansion monitor and selects the desired mode numbers. For example, updatemodes(1:10); will calculate the 10 modes with the highest refractive index. Please note that making this call will force a recalculation of a modes, even if the same modes have previously been calculated. In addition, making this call will force the mode selection method to become "user select". This optional argument was introduced in FDTD 8.6.3 and MODE 6.5.3. |

## NOTE: Saving simulation files before using updatesourcemode If you have a script file which updates the simulation mesh, then you should use the [save script command](./save.md) before updating the source mode. This will ensure that the mesh has been updated before the new mode is calculated.

## NOTE: overlap The fraction of electromagnetic fields that overlap between the two modes is given by the expression below. It is also the fraction of power from mode2 that can propagate in mode1. For more information, please see [overlap script command](./overlap.md). $$ \\text { overlap }=\\operatorname{Re}\\left\[\\frac{\\left(\\int \\vec{E}_{1} \\times \\vec{H}_{2}^{*} \\cdot d \\vec{S}\\right)\\left(\\int \\vec{E}_{2} \\times \\vec{H}_{1}^{*} \\cdot d \\vec{S}\\right)}{\\int \\vec{E}_{1} \\times \\vec{H}_{1}^{*} \\cdot d \\vec{S}}\\right\] \\frac{1}{\\operatorname{Re}\\left(\\int \\vec{E}_{2} \\times \\vec{H}_{2}^{*} \\cdot d \\vec{S}\\right)} $$

**Example**

See the example in the [addmodeexpansion](./addmodeexpansion.md) script function

**See Also**

[Manipulating objects](../lsf-script-commands-alphabetical.md), [addmode](./addmode.md),
[addmodeexpansion](./addmodeexpansion.md), [clearsourcedata](./clearsourcedata.md),
[clearmodedata](./clearmodedata.md), [getresult](./getresult.md),
[overlap](./overlap.md), [expand](./expand.md), [seteigensolver](./seteigensolver.md),
[geteigensolver](./geteigensolver.md), [updatesourcemode](./updatesourcemode.md)
