# clear

Clears all or specified stored workspace variables. This will not clear any simulation
data stored in d-cards. The variables c, pi, eps0, mu0 will be reset to their default
values.

| **Syntax**              | **Description**                                                         |
| ----------------------- | ----------------------------------------------------------------------- |
| clear;                  | Clears all workspace variables. This function does not return any data. |
| clear(var1, var2, ...); | Clears only the workspace variables with the specified names.           |

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ cleardcard ](./cleardcard.md) , [ clearfunctions ](./clearfunctions.md) ,
[ clearexcept ](./clearexcept.md)
