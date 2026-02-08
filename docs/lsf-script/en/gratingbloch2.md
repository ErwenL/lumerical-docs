# gratingbloch2

Returns the bloch vector (k in_1 and k in_2 ) used in the grating calculation. This
corresponds to the bloch vector setting in the simulation region. gratingbloch1 gives
the bloch vector for the first dimension (2D and 3D). gratingbloch2 gives the bloch
vector for the 2nd dimension (3D only). See the grating function documentation for
information on interpreting N, M, ux, uy for various monitor orientations.

| **Syntax**                                | **Description**                     |
| ----------------------------------------- | ----------------------------------- |
| out = gratingbloch2( "monitorname", ...); | Same arguments as grating function. |

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ grating ](./grating.md)
, [ gratingbloch1 ](./gratingbloch1.md)
