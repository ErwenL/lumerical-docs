# hideproperty

Hides the ‘property’ of a given ‘element’.

| **Syntax**                            | **Description**                                                                                                                                                                                                  |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hideproperty (element,property,hide); | Hides the ‘property’ of a given ‘element’. The argument 'hide' is a boolean value. If ‘hide’ is true the property is invisible, if 'hide' is false the property is visible. The default value of ‘hide' is true. |

**Example**

```
addelement("CW Laser");
hideproperty("CWL_1","linewidth", true);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ hidecategory ](./hidecategory.md) , [ annotateproperty ](./annotateproperty.md) ,
[ ispropertyactive ](./ispropertyactive.md) , [ protectproperty ](./protectproperty.md)
