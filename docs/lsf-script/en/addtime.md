# addtime

Adds a time monitor to the simulation environment. The time monitor provides time-domain
information for field components over the course of the simulation

| **Syntax**            | **Description**                                                                                                                                                                                                                                                            |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addtime;              | Adds a time monitor to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addtime(struct_data); | Adds a time monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script command will add a point time monitor to the simulation region and
set its position.

```
addtime;  

set("name","time_1");  
set("monitor type",1);  # point  
set("x",0);  
set("y",0);  
set("z",10e-6);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md)
