# addlayerbuilder

Adds a layer builder object to the simulation environment.

| **Syntax**                    | **Description**                                                                                                                                                                                                                                                                    |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| addlayerbuilder;              | Adds a layer builder object to the simulation environment. This function does not return any data.                                                                                                                                                                                 |
| addlayerbuilder(struct_data); | Adds a layer builder object and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data. |

**Example**

The following script commands will create a layer builder object and add two layers to
it.

```
addlayerbuilder;
# Layer 1: 100 nm layer of silver
addlayer("layer_1");
setlayer("layer_1","thickness",100e-9);
setlayer("layer_1","pattern material","Ag (Silver) - CRC");
# Layer 2: 500 nm layer of silicon
addlayer("layer_2");
setlayer("layer_2","thickness",500e-9);
setlayer("layer_2","pattern material","Si ("Si (Silicon) - Palik");
```

**See Also**

[ addlayer ](./addlayer.md) , [ getlayerlist ](./getlayerlist.md) ,
[ setlayer ](./setlayer.md) , [ loadgdsfile ](./loadgdsfile.md) ,
[ getcelllist ](./getcelllist.md) , [ getlayerlist ](./getlayerlist.md) ,
[ setlayer](./setlayer.md),
[loadprocessfile](https://support.lumerical.com/hc/en-us/articles/360058330814),
[saveprocessfile](https://support.lumerical.com/hc/en-us/articles/360060152573)
