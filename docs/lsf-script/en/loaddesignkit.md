# loaddesignkit

Loads a design kit and directs its contents to a user defined path.

| **Syntax**                      | **Description**                                                                                                                                                  |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| loaddesignkit ("name", "path"); | Loads a design kit named ‘name’ and directs its contents to a user defined ‘path’. The design kit will be available in the element library ‘Design kits’ folder. |

**Example**

```
#loads the design kit "dk" and direct its contents to the path "C:/Users/xxx"
loaddesignkit("dk", "C:/Users/xxx");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ removedesignkit ](./removedesignkit.md) , [ reloaddesignkit ](./reloaddesignkit.md) ,
[ enabledesignkit ](./enabledesignkit.md) , [ disabledesignkit ](./disabledesignkit.md)
, [ installdesignkit ](./installdesignkit.md) ,
[ uninstalldesignkit ](./uninstalldesignkit.md)
