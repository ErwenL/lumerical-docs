# farfieldux

Returns the matrix of ux corresponding to the far field data from farfield3d for a 3D simulation. See the farfield3d documentation for information on interpreting ux, uy, na, nb for various monitor orientations.

**Syntax** |  **Description**  
---|---  
out = farfieldux("mname",f,na,nb,index); |  See farfield3d help. Arguments are same as for farfield3d. Note that the result is an NxM matrix where N is the spatial index and M is the number of frequency points.  
out = farfieldux(dataset,f,na,nb,index); |  See farfield3d help. Arguments are same as for farfield3d. Note that the result is an NxM matrix where N is the spatial index and M is the number of frequency points.  
  
**Example**

See example in the [farfield3d](/hc/en-us/articles/360034930693-farfield3d) function description.

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfielduy ](/hc/en-us/articles/360034410154-farfielduy) , [ farfieldspherical ](/hc/en-us/articles/360034410194-farfieldspherical) , [ farfieldexact ](/hc/en-us/articles/360034410214-farfieldexact) , [ Far field projections - Direction unit vector coordinates ](/hc/en-us/articles/360034394294-FFP-Direction-unit-vector-coordinates)
