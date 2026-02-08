# importbinaryobfuscated

This command is identical to importbinary but makes it possible to import data from a
file that has been obfuscated. For details on how to obfuscate the data files, please
see the Online Help in the User Guide, Structures section.

| **Syntax**                                                                          | **Description**                                                                                                   |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| out = importbinaryobfuscated(key,filename,file_units,x0,y0,z0,reverse_index_order); | Import binary data from filename in three dimensional simulations. All arguments after the filename are optional. |
| **Parameter**                                                                       | **Default value**                                                                                                 |
| ---                                                                                 | ---                                                                                                               |
| key                                                                                 | required                                                                                                          |
| filename                                                                            | required                                                                                                          |
| file_units                                                                          | "m"                                                                                                               |
| x0                                                                                  | 0                                                                                                                 |
| y0                                                                                  | 0                                                                                                                 |
| z0                                                                                  | 0                                                                                                                 |
| reverse_index_order                                                                 | 0                                                                                                                 |

**Example**

Please refer this example [Obfuscating import data](**%20to%20be%20defined%20**).

**See Also**

[Manipulating objects](../lsf-script-commands-alphabetical.md),
[importbinary](./importbinary.md)
