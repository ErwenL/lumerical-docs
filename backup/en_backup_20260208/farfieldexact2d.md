# farfieldexact2d

This function projects complete complex vector fields to specific locations. It is expected to be correct down to distances on the order of one wavelength. The projections from multiple monitors can be added to create a total far field projection - see [ Projections from a monitor box ](/hc/en-us/articles/360034915613-Projections-from-a-monitor-box) .

farfieldexact2d projects any surface to the grid points defined by the vectors x, y. If only E field is returned as the result, the data is returned in the form of a matrix that is of dimension NxMxPx3 where N is the length of the x vector, M is the length of the y vector, P is the number of frequency points, and the final index represents Ex, Ey, and Ez. Note that N and M can be 1; when they are both 1, the function is the same as farfieldexact. If both E and H fileds are returned, the data is returned as a dataset with the E and H fields packaged with the corresponding x,y, and frequency/wavelength.

**Syntax** |  **Description**  
---|---  
out = farfieldexact2d( "mname", x, y, f, index); |  Projects a given power or field profile monitor to the far field at grid points specified by the vectors x,y. Returns E field only.  
out = farfieldexact2d( dataset, x, y, f, index); |  Projects a given rectilinear dataset to the far field at grid points specified by the vectors x,y. Returns E field only.  
out = farfieldexact2d( "mname", x, y, opt); |  Projects a given power or field profile monitor to the far field at grid points specified by the vectors x,y. Returns E filed or E and H fields. Refer to the following table for the options.  
out = farfieldexact2d( dataset, x, y, opt); |  Projects a given rectilinear dataset to the far field at grid points specified by the vectors x,y. Returns E filed or E and H fields. Refer to the following table for the options.  
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
mname |  required |  |  string |  name of the monitor from which far field is calculated.  
dataset |  required |  |  dataset |  Rectilinear dataset containing both E and H  
x |  required |  |  vector |  x coordinates of the grid points where far field is calculated.  
y |  required |  |  vector |  y coordinates of the grid points where far field is calculated.  
f |  optional | 1 |  vector |  Index of the desired frequency point. This can be a single number or a vector. Multithreaded projection was introduced since R2016b.  
index |  optional | index at monitor center |  number |  The index of the material to use for the projection.  
opt |  optional |  |  struct |  the 'opt' parameter includes the following options: "field": This parameter is optional. It defines the return field, can either be "E" or "E and H". "f": This parameter is optional. It defines the index of the desired frequency point. This can be a single number or a vector. Multi-threaded projection was introduced since R2016b. "index": This parameter is optional. It defines the index of the material to use for the projection.  
  
[[Note:]] When using a dataset, the default value of the refractive index is 1.

**Example**

See example in farfieldexact3d function description.

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfieldexact3d ](/hc/en-us/articles/360034930733-farfieldexact3d) , [ farfieldexact ](/hc/en-us/articles/360034410214-farfieldexact)
