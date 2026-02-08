# getglobalsource

Sets global monitor properties. This command will return an error in analysis mode.

| **Syntax**                   | **Description**                                |
| ---------------------------- | ---------------------------------------------- |
| getglobalsource;             | Returns a list of the global source properties |
| getglobalsource("property"); | Returns the value of the requested property.   |

**Example**

Set the global start wavelength to 400nm, then confirm value was set properly.

```
setglobalsource("wavelength start",400e-9);
?getglobalsource("wavelength start");
result: 
4e-007 
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) , [ get ](./get.md) ,
[ setglobalmonitor ](./setglobalmonitor.md) ,
[ getglobalmonitor ](./getglobalmonitor.md) , [ setglobalsource ](./setglobalsource.md)
