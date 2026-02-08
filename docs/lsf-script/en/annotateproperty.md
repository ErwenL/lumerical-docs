# annotateproperty

Enables ‘property’ annotation on a given ‘element’.

| **Syntax**                                        | **Description**                                                                                                                                                                                 |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out=annotateproperty (element,property,annotate); | Enables ‘property’ annotation on a given ‘element’. If ‘annotate’ is true the property is annotated, if ‘annotate’ is false the annotation is disable. The default value of ‘annotate’ is true. |

**Example**

```
addelement("CW Laser");
annotateproperty("CWL_1", "linewidth", true);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ hideproperty ](./hideproperty.md) , [ hidecategory ](./hidecategory.md) ,
[ ispropertyactive ](./ispropertyactive.md)
