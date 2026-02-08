# farfieldvector2d

Projects a given power or field profile monitor or a rectilinear dataset to the far field to a 1 meter radius semi-circle. This is similar to the farfield2d script command except the complex electric fields are returned, rather than field intensity. The data is returned as matrix of NxP if one frequency point is projected, or NxPx3 when multiple frequency points are projected where N is the resolution of the far field projection, P is the number frequency points projected, and the last index refers to Ex, Ey and Ez which are the complex components of the electric field vector in Cartesian coordinates.

**Syntax** |  **Description**  
---|---  
out = farfieldvector2d( "mname",...); |  Returns the Cartesian complex electric fields. Same arguments as farfield2d.  
out = farfieldvector2d( dataset,...); |  Returns the Cartesian complex electric fields. Same arguments as farfield2d.  
  
**Example**

This example plots the amplitude of the Ex component of the far field projection of a 1D monitor called "monitor". In this example the second frequency point is projected. If the monitor only contains data at one frequency, the second argument is not required. For the example of far field projection of a rectilinear dataset see [farfield2d](/hc/en-us/articles/360034410074-farfield2d). 
    
    
    E=farfieldvector2d("monitor",2,501);
    Ex = abs(pinch(E,2,1)); # amplitude of Ex
    theta=farfieldangle("monitor",2,501);
    plot(theta,Ex,"angle (deg)","Ex far field"); 

For additional examples see [ Far field projection ](/hc/en-us/articles/360034914713) .

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfieldpolar2d ](/hc/en-us/articles/360034410094-farfieldpolar2d) , [ farfieldangle ](/hc/en-us/articles/360034930653-farfieldangle)
