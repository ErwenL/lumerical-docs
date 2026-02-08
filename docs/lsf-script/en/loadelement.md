# loadelement

Loads an element from a file created using the [ saveelement ](./saveelement.md) command
in the current working directory. The element will be placed in the current schematic
editor window.

| **Syntax**            | **Description**                                                                     |
| --------------------- | ----------------------------------------------------------------------------------- |
| loadelement ("name"); | Loads an element from the file in the current working directory with extension ICE. |

Example

```
#adds an element star coupler and saves it to an .ice file in the current working directory
addelement("Star Coupler");
saveelement("STAR_1");
#loads the star coupler element "STAR_1.ice" to the schematic editor
loadelement("STAR_1.ice");
#change element position in the schematic editor
set("x position", -200)
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ library ](./library.md)
, [ addtolibrary ](./addtolibrary.md) , [ probe ](./probe.md) ,
[ saveelement ](./saveelement.md)
