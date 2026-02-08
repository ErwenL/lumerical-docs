# workspace

Returns a list of all the currently defined variables in the scripting workspace.

| **Syntax**       | **Description**                                                                                                            |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------- |
| out = workspace; | Returns a string that lists all currently defined variables in the workspace. Use ?workspace; to print this to the screen. |

**Examples**

```
clear;
my_data=4;
result=matrix(2,2);
?workspace;
matrices:
 pi mu0 eps0 my_data result c
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ clear ](./clear.md)
