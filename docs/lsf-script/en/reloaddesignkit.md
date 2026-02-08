# reloaddesignkit

Reloads the contents of a design kit from the element library ‘Design kits’ folder.

| **Syntax**                             | **Description**                                                                                                                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| reloaddesignkit ("name", ["version"]); | Reloads the contents of a design kit named ‘name’ from the element library ‘Design kits’ folder with the version 'version'. "version" is optional and by default is an empty string. |

**Example**

```
#reloads the design kit "LCML" with version v1.1 from the element library ‘Design kits’ folder
reloaddesignkit("LCML", "v1.1");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ loaddesignkit ](./loaddesignkit.md) , [ removedesignkit ](./removedesignkit.md) ,
[ enabledesignkit ](./enabledesignkit.md) , [ disabledesignkit ](./disabledesignkit.md)
, [ installdesignkit ](./installdesignkit.md) ,
[ uninstalldesignkit ](./uninstalldesignkit.md)
