# copy

Creates a copy of the selected objects. The copied objects will typically be identical
(same name, position, etc). For some objects that must have a unique name, '\_1' will be
appended to the name.

| **Syntax**      | **Description**                                        |
| --------------- | ------------------------------------------------------ |
| copy;           | Copy the selected objects.                             |
| copy(dx);       | Same as copy; but with a specified move of dx.         |
| copy(dx,dy);    | Same as copy; but with a specified move of dx, dy.     |
| copy(dx,dy,dz); | Same as copy; but with a specified move of dx, dy, dz. |

**Example**

Creates a copy of the object named substrate. The copy will be located 1um in the y
direction from the original object.

```
addrect;
set("name","substrate");
select("substrate");
copy(0, 1e-6,0); 
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) , [ move ](./move.md) ,
[ select ](./select.md) , [ cp (copy files) ](./cp.md) ,
[ copytoclipboard ](./copytoclipboard.md)
