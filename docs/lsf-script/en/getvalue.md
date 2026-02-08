# getvalue

Gets an internal value for an element's internal ‘s parameters’.

| **Syntax**                                                                              | **Description**                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value=getvalue("element", "parameter"); value=getvalue("element", "parameter", "type"); | Gets an internal value for an element's internal ‘parameter’. Different from ‘set’ or ‘getnamed’, ‘getvalue’ can have direct access to internal element parameters. ‘type’ allows for variations for a given ‘parameter’. |

**Example**

The following example gets the "s parameter" from the element "SPAR_1".

```
?getvalue("SPAR_1", "s parameters");
Cell array with 3 elements
```

**See Also**

[ setvalue ](./setvalue.md)
