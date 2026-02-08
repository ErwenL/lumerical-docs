# probe

Places a probe analyzer at a specified port of a specified element.

| **Syntax**             | **Description**                                                    |
| ---------------------- | ------------------------------------------------------------------ |
| probe ("name","port"); | Places a probe analyzer at a given element name at the given port. |

**Example**

```
#adds a straight waveguide element to the schematic editor and adds a probe to "port 2" of it
addelement("Straight Waveguide");
probe("WGD_1", "port 2");
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ library ](./library.md)
, [ addtolibrary ](./addtolibrary.md) , [ saveelement ](./saveelement.md) ,
