# protectproperty

Protects the ‘property’ of a given ‘element’.

| **Syntax**                                  | **Description**                                                                                                                                                                                                                     |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| protectproperty (element,property,protect); | Protects the ‘property’ of a given ‘element’. The argument 'protect' is a boolean value. If ‘protect’ is true the property is protected, if 'protect' is false the property is unprotected. The default value of ‘protect' is true. |

**Example**

```
createcompound;
addproperty("COMPOUND_1", "test_property");
protectproperty("COMPOUND_1", "test_property", 1);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ hidecategory ](./hidecategory.md) , [ annotateproperty ](./annotateproperty.md) ,
[ ispropertyactive ](./ispropertyactive.md) , [ hideproperty ](./hideproperty.md)
