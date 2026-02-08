# farfieldangle

Returns the vector of angles, in degrees, corresponding to the data from farfield2d for a 2D simulation. Used for 2D simulations. This is required because the farfield2d does not use a set of linearly spaced angles for the projection. It is often useful to re-interpolate the data onto a set of linearly spaced angles using the interp or spline functions.

**Syntax** |  **Description**  
---|---  
theta = farfieldangle( "mname", f, n, index); |  Returns the matrix of angles corresponding to the data in farfield2d  
theta = farfieldangle( dataset, f, n, index); | Returns the matrix of angles corresponding to the data in farfield2d  
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
mname |  required |  |  string |  Name of the monitor from which far field is calculated  
dataset | required |  | dataset |  Rectilinear dataset containing both E and H  
f |  optional |  1 |  vector |  Index of the desired frequency point. This can be a single number or a vector. If f is a vector, the second dimension of theta will match the length of the vector of frequency points. Multithreaded projection was introduced since R2016b.  
n |  optional |  2000 |  number |  The number of points in the far field.  
index |  optional |  value at monitor center |  number |  The index of the material to use for the projection.  
  
**Example**

This example plots the far field projection of a 1D monitor called monitor. In this example the second frequency point is projected. If the monitor only contains data at one frequency, the second argument is not required. For the example of far field projection of a rectilinear dataset see [farfield2d](/hc/en-us/articles/360034410074-farfield2d). 
    
    
    E2=farfield2d("monitor",2,501);
    theta=farfieldangle("monitor",2,501);
    plot(theta,E2,"angle (deg)","|E|^2 far field"); 

For additional examples see [ Far field projection ](/hc/en-us/articles/360034914713) .

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfieldvector2d ](/hc/en-us/articles/360034930633-farfieldvector2d) , [ farfieldpolar2d ](/hc/en-us/articles/360034410094-farfieldpolar2d) , [ interp ](/hc/en-us/articles/360034925893-interp) , [ spline ](/hc/en-us/articles/360034405794-spline)
