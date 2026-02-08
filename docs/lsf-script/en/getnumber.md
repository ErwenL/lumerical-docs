# getnumber

Gets the number of objects that are selected.

| **Syntax**       | **Description**                                  |
| ---------------- | ------------------------------------------------ |
| out = getnumber; | Returns the number of objects that are selected; |

**Example**

Add 2 microns to the radius of all objects named "circle".

```
select("circle");
for (i=1:getnumber) {
 rad=get("radius",i);
 set("radius",rad+2e-6,i);
}
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) , [ get ](./get.md) ,
[ getnamed ](./getnamed.md) , [ getnamednumber ](./getnamednumber.md) ,
[ set ](./set.md)
