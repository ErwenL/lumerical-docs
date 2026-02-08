# getglobalmonitor

Sets global monitor properties. This command will return an error in analysis mode.

| **Syntax**                     | **Description**                                 |
| ------------------------------ | ----------------------------------------------- |
| ?getglobalmonitor;             | Returns a list of the global monitor properties |
| ?getglobalmonitor("property"); | Returns the value of the requested property.    |

**Example**

Set the global number of monitored frequency points to 11, then confirm value was set
properly.

```
setglobalmonitor("frequency points",11);
?getglobalmonitor("frequency points");
result: 
11  
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) , [ get ](./get.md) ,
[ setglobalmonitor ](./setglobalmonitor.md) , [ setglobalsource ](./setglobalsource.md)
, [ getglobalsource ](./getglobalsource.md)
