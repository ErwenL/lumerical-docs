# farfielduy

Returns the matrix of uy corresponding to the far field data from farfield3d for a 3D
simulation. See the farfield3d documentation for information on interpreting ux, uy, na,
nb for various monitor orientations.

| **Syntax**                               | **Description**                                                                                                                                                        |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = farfielduy("mname",f,na,nb,index); | See farfield3d help. Arguments are same as for farfield3d. Note that the result is an NxM matrix where N is the spatial index and M is the number of frequency points. |
| out = farfielduy(dataset,f,na,nb,index); | See farfield3d help. Arguments are same as for farfield3d. Note that the result is an NxM matrix where N is the spatial index and M is the number of frequency points. |

**Example**

See example in the [farfield3d](./farfield3d.md) function description.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ farfield3d ](./farfield3d.md) , [ farfieldux ](./farfieldux.md) ,
[ farfieldspherical ](./farfieldspherical.md) , [ farfieldexact ](./farfieldexact.md) ,
[ Far field projections - Direction unit vector coordinates ](https://optics.ansys.com/hc/en-us/articles/360034394294-FFP-Direction-unit-vector-coordinates)
