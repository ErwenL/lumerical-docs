# setnamed

Likes the set command, except that the object name must be specified. This command will
return an error in analysis mode.

| **Syntax**                                        | **Description**                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ?setnamed("name");                                | Returns a list of the properties of the objects called name.                                                                                                                                                                                                                                                                  |
| setnamed("name", "property", value);              | The same as set, but acts on objects with a specific name, instead of selected objects.                                                                                                                                                                                                                                       |
| setnamed("name", struct);                         | A struct can be accepted in place of "property"-value pair of arguments.                                                                                                                                                                                                                                                      |
| setnamed("name", "property", value,i);            | This form can be used to set the property of the ith named object when multiple objects have the same name. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree.                                         |
| setnamed("groupname::name", "property", value);   | The same as set, but acts on objects within the group named "groupname" that are named "name", instead of selected objects.                                                                                                                                                                                                   |
| setnamed("groupname::name", "property", value,i); | This form can be used to set the property of the ith object with the name "name" in the group "groupname" when multiple objects have the same name. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree. |

**Examples**

Set the radius of the object called "circle" to 10nm:

```
setnamed("circle","radius",10e-9); 
```

Add 2 microns to the radius of all selected objects named circle:

```
for (i=1:getnamednumber("circle")) {
 rad=getnamed("circle","radius",i);
 setnamed("circle","radius",rad+2e-6,i);
}
```

Use struct as an input to set the coordinates and dimensions of an object called
"rectangle":

```
coordinates = {"x" : -3e-7,  
               "x span" : 1e-6,  
               "y" : 5e-6,  
               "y span" : 1e-5,  
               "z" : 1e-7,  
               "z span" : 2.2e-7};  
  
setnamed("rectangle", coordinates);
```

**Notes**

In INTERCONNECT, the element property value must be entered in the setnamed command
using the fixed standard unit. In some cases, the standard unit is different from the
default unit in the Property View. Following is an example of setting the ONA center
frequency. The center frequency default unit is THz, while the standard unit is Hz, and
when using the setnamed command, the value needs to be in Hz:

```
setnamed("ONA", "center frequency", 193.1e12); 
```

To find the standard unit for an element property, open the element's help page on the
Knowledge Page, and look at the Default unit column. A note is included for cases where
the default and standard units differ. For example, see the center frequency of the
[ ONA ](**%20to%20be%20defined%20**) .

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) , [ set ](./set.md) ,
[ get ](./get.md) , [ getnamed ](./getnamed.md) ,
[ getnamednumber ](./getnamednumber.md)
