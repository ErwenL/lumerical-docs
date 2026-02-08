# farfield3dintegrate

Integrates the far field projection over a cone centered at theta0 and phi0, with a width specified by halfangle for 3D simulations. The far field electric field is a function of the direction cosines (ux,uy), but farfield3dintegrate automatically does the change of variables. Similarly, angles are specified in degrees, but converted to radians before the integral is calculated. See the farfield3d documentation for information on interpreting ux, uy, na, nb for various monitor orientations. 

$$ \iint_{\theta, \phi} E^{2}(u x, u y) \sin (\theta) d \theta d \phi $$ 

**Syntax** |  **Description**  
---|---  
out = farfield3dintegrate(E2, ux, uy, halfangle, theta0, phi0);  |  Integrate 3D far field projection data.   
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
E2  |  required  |  |  matrix  |  E field data from farfield3d   
ux  |  required  |  |  vector  |  ux data from farfieldux. Note that the result should be a vector, so it is sufficient to perform the farfieldux script command for only 1 frequency point.   
uy  |  required  |  |  vector  |  uy data from farfielduy. Note that the result should be a vector, so it is sufficient to perform the farfieldux script command for only 1 frequency point.   
halfangle  |  optional  |  90  |  vector  |  Half angle of the integration cone. unit in degrees. must have length L or 1. Half angle should be between 0 to 90 degrees.   
theta0  |  optional  |  0  |  vector  |  Center angle theta of the integration cone. unit in degrees. must have length L or 1. Theta0 should be between 0 to 90 degrees.   
phi0  |  optional  |  0  |  vector  |  Center angle phi of the integration cone. unit in degrees. must have length L or 1. Phi0 should be between 0 to 360 degrees.   
  
**Example**

Calculate the fraction of power from the source that is transmitted into the far field within in a 30 degree cone centered at theta=phi=0. 
    
    
    m="monitor1";
    res = 201;
    E2 = farfield3d(m,1,res,res);
    ux = farfieldux(m,1,res,res);
    uy = farfielduy(m,1,res,res);
    halfangle=30;
    theta0=0;
    phi0=0;
    cone_30 = farfield3dintegrate(E2, ux, uy, halfangle, theta0, phi0); # integrate over 30 degree cone
    total = farfield3dintegrate(E2, ux, uy); # integrate over entire hemisphere
    T   = transmission(m); # fraction of source power transmitted into far field 
    ?cone_30/total;  # fraction of far field power within a 30 degree cone
    ?cone_30/total*T; # fraction of source power transmitted into the far field within a 30 degree cone

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ farfield3d ](/hc/en-us/articles/360034930693-farfield3d) , [ farfieldux ](/hc/en-us/articles/360034410134-farfieldux) , [ farfielduy ](/hc/en-us/articles/360034410154-farfielduy) , [ farfieldspherical ](/hc/en-us/articles/360034410194-farfieldspherical)
