# farfieldpolar3d

The function farfieldpolar3d is similar to farfield3d, but it returns the complex electric fields, rather than field intensity. The data is returned as matrix of NxMx3 (if one frequency point is projected) or NxMx3xP (if more than 1 frequency point is projected), where N and M are spatial indices, the third index refers to E  r  , E  θ  and E  φ  , in spherical coordinates, and P is the number of frequency points. The components E  r  , E  θ  and E  φ  are the complex components of the electric field vector. See the farfield3d documentation for information on interpreting ux, uy, na, nb for various monitor orientations.

Note: When viewing far fields from the GUI with the visualizer, three Attributes are available: E2, Ep, Es. E2 corresponds to |E|^2, Ep to Etheta, and Es to Ephi.

**Syntax** |  **Description**  
---|---  
out = farfieldpolar3d( "mname",...); |  Returns the spherical complex electric fields. Same arguments as farfield3d.  
out = farfieldpolar3d( dataset,...); |  Returns the spherical complex electric fields. Same arguments as farfield3d.  
  
**Example**

See example in the [farfield3d ](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d) function description.

**See Also**

[ List of commands ](https://optics.ansys.com/hc/en-us/articles/360037228834) , [ farfield3d ](https://optics.ansys.com/hc/en-us/articles/360034930693-farfield3d) , [ farfieldvector3d ](https://optics.ansys.com/hc/en-us/articles/360034410114-farfieldvector3d) , [ Far field projections - Field polarization ](https://optics.ansys.com/hc/en-us/articles/360034914753-FFP-Field-polarization)
