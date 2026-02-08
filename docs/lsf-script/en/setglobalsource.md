# setglobalsource

Sets global source properties. This command will return an error in analysis mode.

| **Syntax**                         | **Description**                                                                                     |
| ---------------------------------- | --------------------------------------------------------------------------------------------------- |
| ?setglobalsource;                  | Returns a list of the global source properties                                                      |
| setglobalsource("property",value); | Set the global source property named "property" to a value. This function does not return any data. |

**Example**

Set the global start wavelength to 400nm, then confirm value was set properly.

```
setglobalsource("wavelength start",400e-9);
?getglobalsource("wavelength start");
result: 
4e-007 
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md) ,
[ setglobalmonitor ](./setglobalmonitor.md) ,
[ getglobalmonitor ](./getglobalmonitor.md) , [ getglobalsource ](./getglobalsource.md)
