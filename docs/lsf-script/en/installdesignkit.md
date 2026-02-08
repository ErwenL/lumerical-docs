# installdesignkit

Installs a design kit file to the Design Kits folder.

| **Syntax**                                   | **Description**                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| installdesignkit(filename, path, overwrite); | Installs a design kit file named ‘filename.cml’ and directs its contents to a user defined ‘path’. The design kit will be available in the element library ‘Design kits’ folder. If ‘overwrite’ is true, it will overwrite an existing design kit with the same name, if ‘overwrite’ is false, it will ask the user for confirmation before overwriting. |

**Example**

```
#installs the "dk.cml" library to the Design Kits folder
installdesignkit("dk.cml", "C:/Users/xxx", true);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ packagedesignkit ](./packagedesignkit.md) , [ enabledesignkit ](./enabledesignkit.md)
, [ disabledesignkit ](./disabledesignkit.md) ,
[ uninstalldesignkit ](./uninstalldesignkit.md) ,
[ importschematic ](https://optics.ansys.com/hc/en-us/articles/360034407434-importschematic)
,
[ exportschematic ](https://optics.ansys.com/hc/en-us/articles/360034927573-exportschematic)
, [ customlibrary ](./customlibrary.md) , [ exportlib ](./exportlib.md)
