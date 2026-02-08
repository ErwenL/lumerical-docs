# exportnetlist

Export a netlist for the current circuit.

| **Syntax**                                                                                | **Description**                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| exportnetlist; exportnetlist (filename); exportnetlist (element,filename,overwrite=true); | Export a netlist for the current circuit. ‘filename’ is the output netlist name, ‘element’ is the compound element to be exported. If ‘overwrite’ is true, any existing netlist file with the same name as ‘filename’ will be overwritten. If ‘element’ is not provided, the currently selected compound element will be exported, otherwise the root element will be exported. |

### Example

```
>exportnetlist;
>exportnetlist("circuit.spi");
```

### See Also

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ importnetlist ](./importnetlist.md)
