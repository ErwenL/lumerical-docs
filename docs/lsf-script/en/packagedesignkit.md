# packagedesignkit

Creates a .cml from a existing folder under Custom library.

| **Syntax**                                            | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| packagedesignkit(name, filename, encrypt, overwrite); | Creates a design kit file named ‘filename.cml’ from the custom folder named ‘name’. If 'encrypt' = false, it will be packaged without encryption and if 'encrypt' = true, the package will be encrypted. If ‘overwrite’ is true, it will overwrite an existing design kit file with the same name, if ‘overwrite’ is false, it will ask the user for confirmation before overwriting. The default setting for 'overwrite' is false. |

**Example**

```
#packages a compact model library in the Custom folder with encryption
packagedesignkit("dk", "dk.cml", true, true);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ installdesignkit ](./installdesignkit.md) ,
[ importschematic ](https://optics.ansys.com/hc/en-us/articles/360034407434-importschematic)
,
[ exportschematic ](https://optics.ansys.com/hc/en-us/articles/360034927573-exportschematic)
, [ customlibrary ](./customlibrary.md) , [ exportlib ](./exportlib.md) ,
[ Custom Library & Design Kit ](**%20to%20be%20defined%20**) ,
[ enabledesignkit ](./enabledesignkit.md) , [ disabledesignkit ](./disabledesignkit.md)
, [ installdesignkit ](./installdesignkit.md) ,
[ uninstalldesignkit ](./uninstalldesignkit.md)
