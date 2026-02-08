# hidecategory

Hides all properties of a given ‘category' of a given ‘element’.

| **Syntax**                           | **Description**                                                                                                                                                                                                                        |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| hidecategory(element,category,hide); | Hides all properties of a given ‘category' of a given ‘element’. The argument 'hide' is a boolean value. If ‘hide’ is true the category is invisible, if 'hide' is false the category is visible. The default value of ‘hide’ is true. |

**Example**

```
addelement("CW Laser");
hidecategory("CWL_1","Polarization", true);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ hideproperty ](./hideproperty.md) , [ protectproperty ](./protectproperty.md) ,
[ annotateproperty ](./annotateproperty.md) ,
[ ispropertyactive ](./ispropertyactive.md)
