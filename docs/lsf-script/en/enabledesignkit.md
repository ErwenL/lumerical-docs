# enabledesignkit

Enables a design kit in the Design Kits folder.

| **Syntax**                            | **Description**                                                                                                                                                   |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enabledesignkit("name", ["version"]); | Enables a design kit that is already installed to the Design Kit folder with the version number "version". The "version" is optional, default is an empty string. |

**Example**

```
#enables the design kit "LCML" with version v1.1 from the element library ‘Design kits’ folder
enabledesignkit("LCML", "v1.1");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ removedesignkit ](./removedesignkit.md) , [ reloaddesignkit ](./reloaddesignkit.md) ,
[ loaddesignkit ](./loaddesignkit.md) , [ disabledesignkit ](./disabledesignkit.md) ,
[ installdesignkit ](./installdesignkit.md) ,
[ uninstalldesignkit ](./uninstalldesignkit.md)
