# adduserprop

Adds a custom user property to a structure or analysis group.

| **Syntax**                                 | **Description**                                                                                                                                                                                                                                                                                    |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| adduserprop("property name", type, value); | Adds a user property to a selected structure group. The name is set to "property name". The type is an integer from 0 to 6. The corresponding variable types are 0 - number 1 - Text 2 - Length 3 - Time 4 - Frequency 5 - Material 6 - Matrix The value of the new user property is set to value. |

**Example**

Create a structure group. Add a user property named "radius" and set up the script in
the structure group to add two circles to the group and set their radius to the value of
the user property "radius". Note that the myscript string uses the escape character \\n
for new line and " for double quotes within the string.

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

An example for analysis group

```
addanalysisgroup;
adduserprop("y span",2,5e-6);
myscript =" #begin
y_span = %y span%;
addpower;
set('x',0);
set('y',0);
set('z',0);
set('y span',y_span);
"; #end
set('setup script',myscript);
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) ,
[ addstructuregroup ](./addstructuregroup.md) , [ runsetup ](./runsetup.md)
