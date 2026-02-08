# getnamednumber

Gets the number of objects with a given name.

| **Syntax**                                | **Description**                                                                                                    |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| out = getnamednumber( "name");            | The same as getnumber, but acts on objects with a specific name, instead of selected objects.                      |
| out = getnamednumber( "groupname::name"); | The same as getnumber, but acts on all objects named "name" in the group "groupname", instead of selected objects. |

**Example**

Add 2 microns to the radius of all selected objects named circle.

```
for (i=1:getnamednumber("circle")) {
 rad=getnamed("circle","radius",i);
 setnamed("circle","radius",rad+2e-6,i);
}
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) , [ get ](./get.md) ,
[ getnamed ](./getnamed.md) , [ getnumber ](./getnumber.md) , [ set ](./set.md) ,
[ setnamed ](./setnamed.md)
