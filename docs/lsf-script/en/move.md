# move

Moves selected objects.

| **Syntax**      | **Description**                                                         |
| --------------- | ----------------------------------------------------------------------- |
| move(dx);       | In 2D or 3D, move by dx                                                 |
| move(dx,dy);    | In 2D or 3D, move by dx and dy. This function does not return any data. |
| move(dx,dy,dz); | In 3D, move by dx, dy, and dz. In 2D, dz will be ignored.               |

**Example**

Moves the object named substrate 1um in the z direction.

```
addrect;
set("name","substrate");
select("substrate");
move(0, 1e-6,0); 
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) , [ copy ](./copy.md) ,
[ select ](./select.md)
