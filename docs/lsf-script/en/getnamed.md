# getnamed

Gets a property from objects with a given name.

If multiple objects are selected, and the values are different, the smallest value is
returned. To be certain of the results, be sure that only one object is selected, or use
the form of getnamed that allows a specific object to be selected.

| **Syntax**                                        | **Description**                                                                                                                                                                                                                                                                                      |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ?getnamed("name");                                | Returns a list of the properties of the objects called name.                                                                                                                                                                                                                                         |
| out = getnamed("name", "property");               | Returns the value of the specific property of the named object.                                                                                                                                                                                                                                      |
| out = getnamed("name", "properties_array");       | Return the values of the properties of the named object as struct. The "properties_array" is a cell array of strings.                                                                                                                                                                                |
| out=getnamed("name", "property", i);              | Gets the property of the ith named object. Use this to act on a series of objects. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree.                                         |
| out = getnamed("groupname::name", "property");    | The same as get, but acts on objects named "name" located in the group "groupname", instead of selected objects.                                                                                                                                                                                     |
| out = getnamed("groupname::name", "property", i); | Gets the property of the ith object named "name" located in the group "groupname". Use this to act on a series of objects. The objects are ordered by their location in the object tree. The uppermost selected object is given the index 1, and the index numbers increase as you go down the tree. |

**Examples**

This example uses the get command to get the x span of an object named substrate.

```
addrect;
set("name","substrate");
setnamed("substrate","x span",2e-6); 
x_span = getnamed("substrate","x span"); 
?x_span;
result: 
2e-006  
```

Add 2 microns to the radius of all selected objects named circle.

```
for (i=1:getnamednumber("circle")) {
 rad=getnamed("circle","radius",i);
 setnamed("circle","radius",rad+2e-6,i);
}
```

Get the x, y, z positions of the named object as struct.

```
addrect({"name":"substrate"});  
A = getnamed("substrate",{"x","y","z"});  
?A.x;  
result:   
0 
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) , [ get ](./get.md) ,
[ getnumber ](./getnumber.md) , [ getnamednumber ](./getnamednumber.md) ,
[ set ](./set.md) , [ setnamed ](./setnamed.md)
