# rm

Deletes a file. A path can be specified.

| **Syntax**                       | **Description**                                                      |
| -------------------------------- | -------------------------------------------------------------------- |
| del("filename"); rm("filename"); | Deletes the file "filename". This function does not return any data. |

**Note** : This command cannot be used while in
[safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**Examples**

Deletes a file.

```
del("project_name.fsp") # deletes the file in the current working directory
del("C:\Downloads\project_name.fsp") # deletes the file in a path specified
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ delete ](./delete.md) ,
[ rm ](./rm.md)
