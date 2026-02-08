# addring

Adds a ring primitive to the simulation environment.

| **Syntax**            | **Description**                                                                                                                                                                                                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addring;              | Adds a ring primitive to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addring(struct_data); | Adds a ring primitive and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will create a half-ring named "new_ring" with an inner
radius of 5 um and an outer radius of 7 um centered at (x,y,z) = (1, 2, 0) microns. The
ring will have a thickness (z span) of 10 microns.

```
addring;  
set("name","new_ring");  
set("x",1e-6);  
set("y",2e-6);  
set("inner radius",5e-6);  
set("outer radius",7e-6);  
set("z",0);  
set("z span",10e-6);  
set("theta start",0);  
set("theta stop",180);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md)
