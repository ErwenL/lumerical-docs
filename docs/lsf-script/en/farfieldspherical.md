# farfieldspherical

Interpolates far field data (3D simulations) from E(ux,uy) to spherical coordinates E(theta,phi) 1D array. The far field projections functions generally return the projection as a function of ux,uy (direction cosines). farfieldspherical can be used to interpolate this data into the more common units of theta, phi. See the farfield3d documentation for information on interpreting ux, uy, na, nb for various monitor orientations.

**Syntax** |  **Description**  
---|---  
out = farfieldspherical( E2, ux, uy, theta, phi); |  Interpolate far field data to spherical coordinates. The output has a size of (MxN,1)  
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
E2 |  required |  |  matrix |  E field data from farfield3d  
ux |  required |  |  vector |  ux data from farfieldux. Note that the result should be a vector, so it is sufficient to perform the farfieldux script command for only 1 frequency point.  
uy |  required |  |  vector |  uy data from farfielduy. Note that the result should be a vector, so it is sufficient to perform the farfieldux script command for only 1 frequency point.  
theta |  required |  |  vector |  theta vector, in degrees. Must have length M or 1.  
phi |  required |  |  vector |  phi vector, in degrees. Must have length N or 1.  
  
**Example**

Create a plot of the E2_far vs theta, for phi=0.
    
    
    m="Monitor1";  # Monitor name
    res = 201;    # projection resolution
    E2 = farfield3d(m,1,res,res);
    ux = farfieldux(m,1,res,res);
    uy = farfielduy(m,1,res,res);
    theta = linspace(-90,90,100); 
    phi = 0;
    plot(theta, farfieldspherical(E2,ux,uy,theta,phi) ,"theta", "E^2", "E^2 at phi=0");

Interpolate field data to a grid of theta and phi angles.
    
    
    theta = linspace(-90,90,10);
    phi = linspace(0,45,11);
    Theta = meshgridx(theta,phi);
    Phi = meshgridy(theta,phi);
    E2_angle = farfieldspherical(E2,ux,uy,Theta,Phi);  
    E2_angle = reshape(E2_angle, [length(theta), length(phi)]);  
    image(theta, phi, E2_angle, "theta","phi","E2");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfieldux ](/hc/en-us/articles/360034410134-farfieldux) , [ farfielduy ](/hc/en-us/articles/360034410154-farfielduy) , [ Far field projections - Direction unit vector coordinates ](/hc/en-us/articles/360034394294-FFP-Direction-unit-vector-coordinates) , [ meshgridx ](/hc/en-us/articles/360034409334-meshgridx) , [ meshgridy ](/hc/en-us/articles/360034929673-meshgridy)
