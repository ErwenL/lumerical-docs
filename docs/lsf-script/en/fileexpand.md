# fileexpand

Expands a file name by replacing any environmental variables.

| **Syntax**            | **Description**                                                                       |
| --------------------- | ------------------------------------------------------------------------------------- |
| fileexpand(filename); | Expands a file name by replacing any environmental variables (defined by setsetting). |

### Example

Expand a filename containing the variable LOCAL

```
?getsetting;
LOCAL=C:\Users
?fileexpand("$LOCAL\data.txt");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ setsetting ](./setsetting.md)
