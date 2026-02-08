# ispropertyactive

Returns true if the property ‘property’ from element ‘element’ is active.

| **Syntax**                               | **Description**                                                           |
| ---------------------------------------- | ------------------------------------------------------------------------- |
| out=ispropertyactive (element,property); | Returns true if the property ‘property’ from element ‘element’ is active. |

**Example**

```
addelement("CW Laser");
?ispropertyactive("CWL_1", "frequency");
result: 
1  
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ hideproperty ](./hideproperty.md) , [ hidecategory ](./hidecategory.md) ,
[ annotateproperty ](./annotateproperty.md)
