# setlayer

Sets the properties of the specified layer of the selected layer builder object. There
needs to be a layer builder object selected.

| **Syntax**                                                 | **Description**                                                                |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------ |
| setlayer("layer name", "property name", "property value"); | Sets the properties of a specified layer of the selected layer builder object. |

**Example**

```
setlayer("abc","thickness",0.5e-6);
setlayer("abc","background material","Ag (Silver) - CRC");
setlayer("abc","layer number", "(2:0 and 3:0) or 1:0"); # generate the patterns corresponding to layer 1:0 plus the overlap of layers 2:0 and 3:0.
setlayer("abc","pattern material","Ag (Silver) - CRC");
setlayer("abc","name","abc123"); # change the name of "abc" to "abc123".
```

Please refer
[ this example ](https://optics.ansys.com/hc/en-us/articles/360034382394-Layer-builder)
for more details.

**See Also**

[ addlayerbuilder ](./addlayerbuilder.md) , [ getlayerlist ](./getlayerlist.md) ,
[ setlayer ](./setlayer.md) , [ loadgdsfile ](./loadgdsfile.md) ,
[ addlayer ](./addlayer.md) , [ getcelllist ](./getcelllist.md) ,
[ getlayerlist ](./getlayerlist.md)
