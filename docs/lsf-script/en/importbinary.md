# importbinary

Import binary data (1s and 0s) over an entire volume from a file. The object will be
present wherever the binary data is 1 and not when it is 0. This command only applies to
import primitives. The function returns 1 if the data is successfully imported. Example
script files showing how to use these functions can be found in the Online Help. See the
User Guide, Structures section.

| **Syntax**                                                            | **Description**                                                                                                   |
| --------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| out = importbinary(filename,file_units,x0,y0,z0,reverse_index_order); | Import binary data from filename in three dimensional simulations. All arguments after the filename are optional. |

| **Parameter**       | **Default value** | **Type** | **Description**                                                                                                                                                                                                                                                                 |
| ------------------- | ----------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filename            | required          | string   | name of the file with binary data to import. May contain complete path to file, or path relative to current working directory                                                                                                                                                   |
| file_units          | "m"               | string   | The optional string argument file_units can be "m", "cm, "mm", "microns" or "nm" to specify the units in the file.                                                                                                                                                              |
| x0                  | 0                 | number   | The optional arguments x0, y0 and z0 specify the data origin in the global coordinates of the Graphical Layout Editor. For example, if you defined your volume with respect to a particular point in space, for example (0,0,-5) microns, then you should set z0 to -5 microns. |
| y0                  | 0                 | number   |                                                                                                                                                                                                                                                                                 |
| z0                  | 0                 | number   |                                                                                                                                                                                                                                                                                 |
| reverse_index_order | 0                 | number   | The optional argument reverse_index_order can be set to 1 to reverse how the indices are interpreted in the file. It is best to verify the correct setting with a graphical import before using the script command.                                                             |

## Note: Imported binary object boundaries The boundary of the import binary object is positioned between the vertices where the material is present and the vertices where the material is not present. The shape of this implied boundary can be complex, and the viewport does not show the full detail. The boundary can be moved closer to vertices where the material is present by increasing the "binary threshold" property of the import object. To confirm the boundary that will be used in the simulation by the solver, use an index monitor.

**Example**

Please refer to the
[importing spatial binary example](https://optics.ansys.com/hc/en-us/articles/360034382754-Import-object-Binary-spatial-data)
for details.

**See Also**

[Manipulating objects](../lsf-script-commands-alphabetical.md),
[importbinary2](./importbinary2.md)
