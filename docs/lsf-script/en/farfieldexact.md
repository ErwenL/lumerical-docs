# farfieldexact

Projects complete complex vector fields to specific locations. It is expected to be correct down to distances on the order of one wavelength. The projections from multiple monitors can be added to create a total far field projection - see [ Projections from a monitor box ](/hc/en-us/articles/360034915613-Projections-from-a-monitor-box) .

farfieldexact projects any surface fields to a series of points defined by vector lists. The x,y, z coordinates of each evaluation point are taken element-by-element from the vector lists. i.e., the i-th point in a 2D simulation would be at [x(i),y(i)]. This command can return either the E field or the E and H fields of the projection.

3D

Vectors lists x,y,z must have the same length L or be length 1. When only the E field is returned, the data is returned in a matrix of dimension Lx3. The first index represents positions defined by one element from each of x,y, z. [x(i),y(i),z(i)]; the second index represents Ex, Ey, and Ez. When both E and H fields are returned, the data is returned as a dataset with the E and H fields packaged with the corresponding x,y,z and frequency/wavelength.

2D

Vector lists x, y must have the same length L or be length 1. When only the E field is returned, the data is returned in the form of a matrix that is of dimension Lx3. The first index represents positions defined by one element from each of x,y. [x(i),y(i)]; The second index represents Ex, Ey, and Ez. When both E and H fields are returned, the data is returned as a dataset with the E and H fields packaged with the corresponding x,y, and frequency/wavelength.

**Syntax** |  **Description**  
---|---  
out = farfieldexact("mname", x, y, f, index); |  2D far field exact projection. Returns E field only.  
out = farfieldexact(dataset, x, y, f, index); |  2D far field exact projection. Returns E field only.  
out = farfieldexact("mname", x, y, opt); |  2D far field exact projection. Returns E field or E and H fields. Refer to the following table for the options.  
out = farfieldexact(dataset, x, y, opt); |  2D far field exact projection. Returns E field or E and H fields. Refer to the following table for the options.  
out = farfieldexact("mname", x, y, z, f, index); |  3D far field exact projection. Returns E field only.  
out = farfieldexact(dataset, x, y, z, f, index); |  3D far field exact projection. Returns E field only.  
out = farfieldexact("mname", x, y, z, opt); |  3D far field exact projection. Returns E field or E and H fields. Refer to the following table for the options  
out = farfieldexact(dataset, x, y, z, opt); |  3D far field exact projection. Returns E field or E and H fields. Refer to the following table for the options  
  
**Parameter** |  **Default** |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
mname |  required |  |  string |  name of the monitor from which far field is calculated  
dataset |  required |  |  dataset |  Rectilinear dataset containing both E and H  
x |  required |  |  vector |  x coordinates of points where far field is calculated. must have length L or 1.  
y |  required |  |  vector |  y coordinates of points where far field is calculated. must have length L or 1.  
z |  required |  |  vector |  z coordinates of points where far field is calculated. must have length L or 1.  
f |  optional | 1 |  vector | Index of the desired frequency point. This can be a single number or a vector. Multithreaded projection was introduced since R2016b.  
index |  optional | value at monitor centre |  number |  The index of the material to use for the projection.  
opt |  optional |  |  struct |  the 'opt' parameter includes the following options: "field": This parameter is optional. It defines the return field, can either be "E" or "E and H". "f": This parameter is optional. It defines the index of the desired frequency point. This can be a single number or a vector. Multi-threaded projection was introduced since R2016b. "index": This parameter is optional. It defines the index of the material to use for the projection.  
  
[[Note:]] When using a dataset, the default value of the refractive index is 1.

**Example**

This example shows how to calculate |E|^2 and |H|^2 on a straight line at y=0, z=1, for x from -1 to 1 meters. For the example of far field projection of a rectilinear dataset see [farfield3d](/hc/en-us/articles/360034930693-farfield3d). 
    
    
    # Define far field position vector
    res=100;
    x=linspace(-1,1,res);
    y=0;
    z=1;
    # do far field projection
    E_H_far=farfieldexact("monitor",x,y,z,{"field":"E and H", "f":1});
    E_far = E_H_far.E;
    H_far = E_H_far.H;
    E2_far = sum(abs(E_far)^2,2); # E2 = |Ex|^2 + |Ey|^2 + |Ez|^2
    H2_far = sum(abs(H_far)^2,2); # H2 = |Hx|^2 + |Hy|^2 + |Hz|^2
    # plot results
    plot(x,E2_far,"x","y","|E|^2 on line at y=0, z=1");
    plot(x,H2_far,"x","y","|H|^2 on line at y=0, z=1");

This example shows how to sum the results from a box of monitors (typically surrounding a scattering particle).

Note: See the online section on [ Far field projections ](/hc/en-us/articles/360034914713) for more information on why a negative sign is required on some terms.
    
    
    phi = linspace(0,360,201);
    E2_xy = matrix(length(phi));
    E2_yz = matrix(length(phi));
    x = -sin(phi*pi/180);
    y = cos(phi*pi/180);
    z = 0;
    temp = farfieldexact("x2",x,y,z,{"field":"E"}) + farfieldexact("y2",x,y,z,{"field":"E"}) + farfieldexact("z2",x,y,z,{"field":"E"})
       - farfieldexact("x1",x,y,z,{"field":"E"}) - farfieldexact("y1",x,y,z,{"field":"E"}) - farfieldexact("z1",x,y,z,{"field":"E"});
    E2_xy = sum(abs(temp)^2,2); # E2 = |Ex|^2 + |Ey|^2 + |Ez|^2
    plot(phi, E2_xy,"Phi (deg)","|E|^2","in XY plane");

The following example shows how farfieldexact and farfieldexact3d output data differently.

When x=[1 2], y=[1 2], z=[0],

farfieldexact: The result is a 2*3 matrix. First dimension is position;second is field component. This calculates the far field at the positions [1,1,0] and [2,2,0] .

farfielexact3d: The result is a 2*2*1*3 matrix. First three dimensions are positions; the fourth dimension is field component. This calculates the far field at the positions [x,y,z] = [1,1,0], [1,2,0], [2,1,0], [2,2,0].
    
    
    x=1:2;
    y=1:2;
    z=0;
    m="monitor";
    E_far=farfieldexact(m,x,y,z,{"field":"E"});
    ?size(E_far);
     result: 
     2 3 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfieldexact2d ](/hc/en-us/articles/360034410234-farfieldexact2d) , [ farfieldexact3d ](/hc/en-us/articles/360034930733-farfieldexact3d)
