# farfieldvector3d

The function farfieldvector3d is similar to farfield3d, but it returns the complex
electric fields, rather than field intensity. The data is returned as matrix of NxMx3
(if one frequency point is projected) or NxMx3xP (if more than 1 frequency point is
projected), where N and M are spatial indices, the third index refers to Ex, Ey and Ez
in spherical coordinates, and P is the number of frequency points. The components Ex, Ey
and Ez are the complex components of the electric field vector. See the farfield3d
documentation for information on interpreting ux, uy, na, nb for various monitor
orientations.

| **Syntax**                            | **Description**                                                              |
| ------------------------------------- | ---------------------------------------------------------------------------- |
| out = farfieldvector3d( "mname",...); | Returns the cartesian complex electric fields. Same arguments as farfield3d. |
| out = farfieldvector3d( dataset,...); | Returns the cartesian complex electric fields. Same arguments as farfield3d. |

**Example**

See example in the [farfield3d](./farfield3d.md) function description.

[Understanding field polarization in far field projections](https://optics.ansys.com/hc/en-us/search/click?data=BAh7DjoHaWRsKwjB0cDTUwA6D2FjY291bnRfaWRpA02AjDoJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSJ2aHR0cHM6Ly9vcHRpY3MuYW5zeXMuY29tL2hjL2VuLXVzL2FydGljbGVzLzM2MDAzNDkxNDc1My1VbmRlcnN0YW5kaW5nLWZpZWxkLXBvbGFyaXphdGlvbi1pbi1mYXItZmllbGQtcHJvamVjdGlvbnMGOwhUOg5zZWFyY2hfaWRJIilkYjc4YzM5Yy1iOWU1LTRjNWUtYjE0NC02MGQzNjA4MGRkYWIGOwhGOglyYW5raQg6C2xvY2FsZUkiCmVuLXVzBjsIVDoKcXVlcnlJIhNmYXJmaWVsZHZlY3RvcgY7CFQ6EnJlc3VsdHNfY291bnRpEg%3D%3D--90007a278d7628d12a8c14265df095c4975dd311)

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ farfield3d ](./farfield3d.md) , [ farfieldpolar3d ](./farfieldpolar3d.md) ,
[ Far field projections - Field polarization ](https://optics.ansys.com/hc/en-us/articles/360034914753-FFP-Field-polarization)
