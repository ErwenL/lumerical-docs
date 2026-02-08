# disabledesignkit

Disables a design kit in the Design Kits folder.

| **Syntax**                             | **Description**                                                                                                                                                    |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| disabledesignkit("name", ["version"]); | Disables a design kit that is already installed to the Design Kit folder with the version number "version". The "version" is optional, default is an empty string. |

**Example**

```
#disables the design kit "LCML" with version v1.1 from the element library ‘Design kits’ folder
disabledesignkit("LCML", "v1.1");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ removedesignkit ](./removedesignkit.md) , [ reloaddesignkit ](./reloaddesignkit.md) ,
[ loaddesignkit ](./loaddesignkit.md) , [ enabledesignkit ](./enabledesignkit.md) ,
[ installdesignkit ](./installdesignkit.md) ,
[ uninstalldesignkit ](./uninstalldesignkit.md)
