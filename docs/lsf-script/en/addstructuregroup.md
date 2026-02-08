# addstructuregroup

Adds a structure group to the simulation environment. Structure groups are very
convenient when you want to parametrize your design. You can define different parameters
for the structure group and use the "setup" script to create your geometry (along with
monitors and/or sources) according to those parameter values.

| **Syntax**                      | **Description**                                                                                                                                                                                                                                                               |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addstructuregroup;              | Adds a structure group to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addstructuregroup(struct_data); | Adds a structure group and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

Add a structure group and put a rectangle in it.

```
addstructuregroup;
set("name","group");
addrect;
addtogroup("group");
```

Create a structure group. Add a user property named "radius" and set up the script in
the structure group to add two circles to the group and set their radius to the value of
the user property "radius".

```
addstructuregroup;
adduserprop("radius",2,0.5e-6);
myscript =      "addcircle; \n";
myscript = myscript + "copy(1e-6); \n";
myscript = myscript + "selectall; \n";
myscript = myscript + "set(\"radius\",radius);";
set("name","dimer");
set("script",myscript); 
```

NOTE: The "myscript" string in the script above uses the escape character \\n for new
line and " for double quotes within the string.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ addtogroup ](./addtogroup.md) , [ adduserprop ](./adduserprop.md) ,
[ addgroup ](./addgroup.md) , [ addanalysisgroup ](./addanalysisgroup.md) ,
[ set ](./set.md)
