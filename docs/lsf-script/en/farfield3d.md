# farfield3d

Projects a given power or field profile monitor or a rectilinear dataset to the far field in a 3D simulation. The electric field intensity |E|  2  is returned.

**Syntax** |  **Description**  
---|---  
out = farfield3d("mname",f, na, nb, illumination, periodsa, periodsb, index, direction); |  Projects a given power or field profile monitor to the far field. This returns an NxM matrix if 1 frequency point is projected, or a NxMxP matrix if more than 1 frequency point is projected, where N and M correspond to the resolution of the projection (na, and nb), and P corresponds to the number of frequency points projected.  
out = farfield3d(dataset,f, na, nb, illumination, periodsa, periodsb, index, direction); |  Projects a given rectilinear dataset to the far field. This returns an NxM matrix if 1 frequency point is projected, or a NxMxP matrix if more than 1 frequency point is projected, where N and M correspond to the resolution of the projection (na, and nb), and P corresponds to the number of frequency points projected.  
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
mname |  required |  |  string |  Name of the monitor  
dataset |  required |  |  dataset |  Rectilinear dataset containing both E and H  
f |  optional |  1 |  vector |  Index of the desired frequency point. This can be a single number or a vector. Multithreaded projection to allow multiple frequency points to be projected simultaneously was introduced in R2016b.  
na |  optional |  150 |  number |  The number of points in the far field.  
nb |  optional |  150 |  number |  The number of points in the far field.  
illumination |  optional |  1 |  number |  For periodic structures. Gaussian illumination: 1 Plane wave illumination: 2  
periodsa |  optional |  1 |  number |  number of periods to be used for periodic illumination  
periodsb |  optional |  1 |  number |  number of periods to be used for periodic illumination  
index |  optional |  value at monitor center |  number |  The index of the material to use for the projection.  
direction |  optional |  direction of max power flow |  number |  Direction: this can be +1 or -1.  
  
The following table summarizes how to interpret the ux, uy coordinate vectors and periods input properties for various monitor orientations.

**Monitor orientation** |  **Monitor surface normal** |  **'na', 'ux', 'periods a' correspond to** |  **'nb', 'uy', 'periods b' correspond to**  
---|---|---|---  
XY plane |  Z |  x axis |  y axis  
XZ plane |  Y |  x axis |  z axis  
YZ plane |  X |  y axis |  z axis  
  
**Example**

This example images the far field projection of a 2D monitor called monitor. In this example the second frequency point is projected. If the monitor only contains data at one frequency, the second argument is not required.
    
    
    E = farfield3d("monitor",2); 
    ux = farfieldux("monitor",2); 
    uy = farfielduy("monitor",2); 
    image(ux,uy,E,"","","title","polar"); 

The following example images the far field projection of a rectilinear dataset. Here, the dataset is from a 2D monitor.
    
    
    dataset=getresult("monitor", "E");  
    dataset.addattribute("H",getattribute(getresult("monitor","H"),"H"));  
      
    E = farfield3d(dataset,2);   
    ux = farfieldux(dataset,2);   
    uy = farfielduy(dataset,2);   
    image(ux,uy,E,"","","title","polar"); 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ farfield2d ](/hc/en-us/articles/360034410074-farfield2d) , [ farfieldvector3d ](/hc/en-us/articles/360034410114-farfieldvector3d) , [ farfieldpolar3d ](/hc/en-us/articles/360034930713-farfieldpolar3d) , [ farfieldux ](/hc/en-us/articles/360034410134-farfieldux) , [ farfielduy ](/hc/en-us/articles/360034410154-farfielduy) , [ farfieldexact3d ](/hc/en-us/articles/360034930733-farfieldexact3d) , [ farfieldfilter ](/hc/en-us/articles/360034930613-farfieldfilter) , [ farfield3dintegrate ](/hc/en-us/articles/360034410174-farfield3dintegrate)
