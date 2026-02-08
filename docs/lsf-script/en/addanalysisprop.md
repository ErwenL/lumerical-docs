# addanalysisprop

Adds a user defined custom analysis property to the setup user defined in structure and
analysis groups.

| **Syntax**                                     | **Description**                                                                                                                                                                                                                                                                                                             |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addanalysisprop("property name", type, value); | Adds an analysis property to a selected object group. The name is set to "property name". The type is an integer from 0 to 8. The corresponding variable types are: 0 - Number 1 - String 2 - Length 3 - Time 4 - Frequency 5 - Material 6 - Matrix 7 - Cell 8 - Struct The value of the new user property is set to value. |

**Example**

Add a length variable called "Pname" as an analysis property for the analysis group

```
addanalysisgroup;
set("name","group");
addanalysisprop("Pname", 2, 1e-6); # 2 represents Length
```

**See Also**

- [Manipulating objects](../lsf-script-commands-alphabetical.md)
- [addstructuregroup](./addstructuregroup.md)
- [runsetup](./runsetup.md)
- [addanalysisgroup](./addanalysisgroup.md)
- [addanalysisresult](./addanalysisresult.md)
