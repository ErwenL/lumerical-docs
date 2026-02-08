# addtolibrary

Adds the selected element to the currently selected folder under Custom library.

| **Syntax**                      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addtolibrary ("name", replace); | Adds an element to the currently selected folder under Custom library. The "name" specified is the custom folder name. If no folder named as specified, a new folder will be generated under the Custom library. The "replace" is a boolean value. If "replace" is true, the element in the Custom library with the same name will be replaced; if "replace" is false, a warning message will pop up to get further action for replacing the element with the same name or not. The default value for "replace" is false. |

**Eample**

```
#adds the selected element to the folder "folder1" under Custom library
addtolibrary("folder1", true);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ library ](./library.md)
, [ customlibrary ](./customlibrary.md)
