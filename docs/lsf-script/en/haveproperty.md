# haveproperty

Returns the number of selected objects with a particular property.

| **Syntax**                      | **Description**                                                     |
| ------------------------------- | ------------------------------------------------------------------- |
| out = haveproperty("property"); | Returns the number of selected objects with the specified property. |

**Example**

Add a circle and a rectangle. Use haveproperty to show that both objects have the
property 'x', but only one has the property 'radius'.

```
addcircle;
addrect;
selectall;
?haveproperty("x");
?haveproperty("radius");
result:2
result:
1 
```

**See Also**

[ Manipulating objects ](../lsf-script-commands-alphabetical.md) , [ get ](./get.md) ,
[ set ](./set.md)
