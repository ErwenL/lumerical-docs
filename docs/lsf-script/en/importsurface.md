# importsurface

Imports surface data. This command only applies to import primitives. The function
returns 1 if the data is successfully imported. Example script files showing how to use
these functions can be found in the Online Help. See the User Guide, Structures section.

| **Syntax**                                                                | **Description**                                                                                                                     |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| out = importsurface(filename,upper_surface,file_units,x0,y0,z0,invertXY); | Import a surface from the file in the string filename in a three dimensional simulation. All arguments after filename are optional. |
| out = importsurface(filename,upper_surface,file_units,x0,y0,invertXY);    | Import a surface from the file in the string filename in a two dimensional simulation. All arguments after filename are optional.   |

| **Parameter** | **Default value** | **Type** | **Description**                                                                                                                                                                                                                                                               |
| ------------- | ----------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| filename      | required          | string   | name of the file with surface data to import. May contain complete path to file, or path relative to current working directory                                                                                                                                                |
| upper_surface | 1                 | number   | This optional argument should be 1 to import the upper surface and 0 to import the lower surface.                                                                                                                                                                             |
| file_units    | "m"               | string   | The optional string argument file_units can be "m", "cm, "mm", "microns" or "nm" to specify the units in the file.                                                                                                                                                            |
| x0            | 0                 | number   | The optional arguments x0, y0 and z0 specify the data origin in the global coordinates of the Graphical Layout Editor. For example, if you are importing a surface defined by an AFM that is on a slab of Si that ranges from 0 to 2 microns, you should set z0 to 2 microns. |
| y0            | 0                 | number   |                                                                                                                                                                                                                                                                               |
| z0            | 0                 | number   |                                                                                                                                                                                                                                                                               |
| invertXY      | 0                 | number   | The optional argument invertXY can be used to reverse how the x and y axes are read from the file.                                                                                                                                                                            |

**Example**

please refer a complete example:
[Import object - Surfaces](https://optics.ansys.com/hc/en-us/articles/360034901973)

**See Also**

[Manipulating objects](../lsf-script-commands-alphabetical.md),
[importsurface2](./importsurface2.md)
