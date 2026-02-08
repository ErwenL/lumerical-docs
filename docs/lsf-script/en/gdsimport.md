# gdsimport

This command imports a cell from a .gds file into the layout environment. This is
equivalent to performing a GDSII import through the FILE->IMPORT menu. See the Layout
editor reference guide on
[ GDSII import ](https://optics.ansys.com/hc/en-us/articles/360034901933-Import-and-export-GDSII)
for more information.

| **Syntax**                                                            | **Description**                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| n = gdsimport("filename", "cellname", layer);                         | Imports the specified layer from the specified cell in the specified file into the current simulation environment. The objects created will have their material set to an object defined dielectric. In 3D, the 2D geometric data will be extruded to default values in the Z dimension. The optional returned value, n, is the number of objects that were imported from the gds file. |
| n = gdsimport("filename", "cellname", layer, "material");             | Same as the above command, but the material of the imported object will be set to the value specified.                                                                                                                                                                                                                                                                                  |
| n = gdsimport("filename", "cellname", layer, "material", zmin, zmax); | This form of the command is only allowed in 3D layouts. The behavior is the same as the above command, but the structures will be extruded in the Z dimension to the specified z min and z max values                                                                                                                                                                                   |

| **Parameter** | **Type**         | **Description**                                                                                                                                                                                                                    |
| ------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filename      | string           | name of the GDSII file to import. It can contain a complete path to file, or path relative to the current working directory.                                                                                                       |
| cellname      | string           | name of the cell to import from the GDSII file.                                                                                                                                                                                    |
| layer         | number or string | the layer number from the GDSII file to import. If only elements matching a certain data type are desired, this can be specified by using a string of the form: "6:2" where the desired layer is 6 and the desired data type is 2. |
| material      | string           | a valid name of a material in your current layout environment. Partial names of materials can be matched starting at the beginning of the string. For example, "Al (3" would match "Al (300nm)".                                   |
| zmin          | number           | the minimum z value for extruding 2D GDSII data into 3D objects                                                                                                                                                                    |
| zmax          | number           | the maximum z value for extruding 2D GDSII data into 3D objects                                                                                                                                                                    |

## Example:

This command imports "cell_1", on the first layer in the GDS_export.gds file, with a
specified material, z min and z max assigned. For more examples, please visit the Layout
editor reference guide on
[ GDSII import ](https://optics.ansys.com/hc/en-us/articles/360034901933-Import-and-export-GDSII)
.

```
gdsimport("GDS_export.gds", "cell_1", 1, "Ag (Silver) - CRC", 0, 1e-6);
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ setnamed ](./setnamed.md) , [ fileexists ](./fileexists.md) ,
[ gdsopen](./gdsopen.md),
[gdsaddstencil](https://optics.ansys.com/hc/en-us/articles/43594268925459-gdsaddstencil-Script-command)
