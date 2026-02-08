# exportview

This command captures your simulation setup as shown in the specified view and exports
it as a static image into \*png file. This script command is an alternative to the view
export available from the GUI menu in your Lumerical tools.

| **Syntax**                                    | **Description**                                                                                                                                                                               |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| exportview("filename");                       | Captures the current scene in the default "perspective" view and saves it as filename.png.                                                                                                    |
| exportview("example_filename","perspective"); | Optional: Captures the scene in the specified view. The options are:XY, XZ, YZ, perspective Note: This optional argument is not available in Finite Element IDE since it offers only one view |

**Example**

Type in exportview("ring_modulator_v2_XY","XY"); in prompt to save the current XY view
of your simulation as "ring_modulator_v2_XY.png" in the current path.

**See Also**

[orbit](./orbit.md), [setview](./setview.md)
