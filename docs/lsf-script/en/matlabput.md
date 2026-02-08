# matlabput

Copies a variable from Lumerical's Script Workspace to the MATLAB workspace. The
resulting variable in the MATLAB workspace will have the same name as in Lumerical, and
will overwrite any existing variable with the same name. If the variable does not exist
in the Lumerical workspace, the command will return an error.

For more information, please see the matlab command description.

| **Syntax**                     | **Description**                                                                                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| matlabput(var1, var2,...varN); | The arguments to this command are one or more variable names that exist in the Lumerical variable workspace. This function does not return any data. |

**Examples**

See the examples in the [ matlab ](./matlab.md) function description.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ matlab ](./matlab.md) ,
[ matlabget ](./matlabget.md)
