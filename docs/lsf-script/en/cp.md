# cp

Copies a file. The copy can be created in a specified path.

| **Syntax**                         | **Description**                                                             |
| ---------------------------------- | --------------------------------------------------------------------------- |
| cp("file1","file2");               | Makes a copy of file1 called file2. This function does not return any data. |
| cp("path1\\file1","path2\\file2"); | Copies file1 in path1 to file2 in path2.                                    |

**Note** : This command cannot be used while in
[safe mode](https://optics.ansys.com/hc/en-us/articles/360044709054-Running-script-in-safe-mode "https://optics.ansys.com/hc/en-us/articles/360044709054-running-script-in-safe-mode").

**Examples**

Makes a copy of "myscript.lsf" in c:\\working called "temp.lsf".

```
cp("c:\myscript.lsf","c:\working\temp.lsf");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ mv ](./mv.md) ,
[ pwd ](./pwd.md) , [ copy (objects) ](./copy.md)
