# matlabget

Copies a variable from the MATLAB workspace to the script variable workspace. The
resulting variable will have the same name as the MATLAB variable, and will overwrite
any existing variable with the same name. If the variable does not exist in MATLAB, the
command will return an error. For more information, please see the matlab command
description.

## Note: Matlab script integration must be enabled in order to use this command. For more information on how to set this up see the [ Matlab script integration ](https://optics.ansys.com/hc/en-us/articles/360034923913-MATLAB-Script-Integration) page.

| **Syntax**                     | **Description**                                                                                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| matlabget(var1, var2,...varN); | The arguments to this command are one or more variable names that refer to variables in the MATLAB workspace. This function does not return any data. |

**Examples**

See the example in the [ matlab ](./matlab.md) function description.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ matlab ](./matlab.md) ,
[ matlabput ](./matlabput.md)
