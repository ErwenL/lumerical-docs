# farfieldexact3d

The three dimension form of farfieldexact2d. This function projects complete complex vector fields to specific locations. It is expected to be correct down to distances on the order of one wavelength. The projections from multiple monitors can be added to create a total far field projection - see [ Projections from a monitor box ](/hc/en-us/articles/360034915613-Projections-from-a-monitor-box) .

farfieldexact3d projects any surface to the grid points defined by the vectors x,y and z. If only E field is returned as the result, the data is returned in a matrix of dimension NxMxKx3 if one frequency point is projected, and NxMxKx3xP if more than one frequency point is projected where N is the length of the vector x, M the length of the vector y, K is the length of the vector z, P is the number of frequency points, and the fourth index represents Ex, Ey, and Ez. Note that N, M and K can be 1, and when they are all 1, the function is the same as farfieldexact. If both E and H fileds are returned, the data is returned as a dataset with the E and H fields packaged with the corresponding x,y,z and frequency/wavelength.

**Syntax** |  **Description**  
---|---  
out = farfieldexact3d( "mname", x, y, z, f, index); |  Projects a given power or field profile monitor to the far field at grid points specified by the vectors x,y,z. Returns E field only.  
out = farfieldexact3d( dataset, x, y, z, f, index); |  Projects a given rectilinear dataset to the far field at grid points specified by the vectors x,y,z. Returns E field only.  
out = farfieldexact3d( "mname", x, y, z, opt); |  Projects a given power or field profile monitor to the far field at grid points specified by the vectors x,y,z. Returns E field or E and H fields. Refer to the table below for the options.  
out = farfieldexact3d( dataset, x, y, z, opt); |  Projects a given rectilinear dataset to the far field at grid points specified by the vectors x,y,z. Returns E field or E and H fields. Refer to the table below for the options.  
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
mname |  required |  |  string |  name of the monitor from which far field is calculated  
x |  required |  |  vector |  x coordinates of the grid points where far field is calculated  
y |  required |  |  vector |  y coordinates of the grid points where far field is calculated  
z |  required |  |  vector |  z coordinates of the grid points where far field is calculated  
f |  optional | 1 |  vector |  Index of the desired frequency point. This can be a single number or a vector. Multithreaded projection was introduced since R2016b.  
index |  optional | value at monitor centre |  number |  The index of the material to use for the projection.  
opt |  optional |  |  struct |  the 'opt' parameter includes the following options: "field": This parameter is optional. It defines the return field, can either be "E" or "E and H". "f": This parameter is optional. It defines the index of the desired frequency point. This can be a single number or a vector. Multi-threaded projection was introduced since R2016b. "index": This parameter is optional. It defines the index of the material to use for the projection.  
  
[[Note:]] When using a dataset, the default value of the refractive index is 1.

**Example**

This 3D example calculates the far field electric field intensity on a 2mm x 2mm image plane located a distance of z=+1.5mm from the simulation region. For the example of far field projection of a rectilinear dataset see [farfield3d](/hc/en-us/articles/360034930693-farfield3d). 
    
    
    mname="trans";    # Monitor name
    num=25;       # resolution
    # define far field plane to image fields
    x=linspace(-1e-3,1e-3,num); 
    y=x;
    z=1.5e-3;
    # compute far field
    E=farfieldexact3d(mname,x,y,z,{"field":"E"}); 
    # select component
    Ex=pinch(E,4,1); 
    Ey=pinch(E,4,2);
    Ez=pinch(E,4,3);
    # image intensity
    E2= abs(Ex)^2 + abs(Ey)^2 + abs(Ez)^2;
    image(x*1e3,y*1e3,E2,"x (mm)","y (mm)","Electric field at z=1.5mm from source"); 

The following example shows how farfieldexact and farfieldexact3d output data differently.

When x=[1 2], y=[1 2], z=[0],

farfieldexact: The result is a 2*3 matrix. First dimension is position;second is field component. This calculates the far field at the positions [1,1,0] and [2,2,0] .

farfielexact3d: The result is a 2*2*1*3 matrix. First three dimensions are positions; the fourth dimension is field component. This calculates the far field at the positions [x,y,z] = [1,1,0], [1,2,0], [2,1,0], [2,2,0].
    
    
    x=1:2;
    y=1:2;
    z=0;
    m="monitor";
    E_far=farfieldexact3d(m,x,y,z,{"field":"E"});
    ?size(E_far);
     result: 
     2 2 1 3  

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfieldexact2d ](/hc/en-us/articles/360034410234-farfieldexact2d) , [ farfieldexact ](/hc/en-us/articles/360034410214-farfieldexact)
