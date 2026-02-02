# createsphericalsurface

Creates a triangulated spherical surface or a segmented circular arc. It can be used to define the far-field points for a far field projection as these are often specified using a spherical surface (3D simulations) or a circular arc (2D simulations). 

**Syntax** |  **Description**  
---|---  
out = createsphericalsurface([theta1,theta2],[phi1,phi2], [X,Y,Z],radius,lmax);  |  Creates an unstructured data set with a triangulated surface or a segmented arc. Their dimensions are specified by the input angles, orientation axis and radius. The coarseness of the triangulation (or line segmentation) is specified as the maximum separation between adjacent points. The output data set contains the IDs of each element (triangles or lines) and the corresponding areas (only for triangles).   
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
theta1  |  optional  |  0  |  number  |  Starting value of the elevation angle (theta) range in radians with respect to the reference axis.   
theta2  |  optional  |  pi  |  number  |  End value of the elevation angle (theta) range in radians with respect to the reference axis.   
phi1  |  optional  |  0  |  number  |  Starting value of the azimuthal angle (phi) range in radians with respect to the reference axis.   
phi2  |  optional  |  2*pi  |  number  |  End value of the azimuthal angle (phi) range in radians with respect to the reference axis.   
[X,Y,Z]  |  optional  |  [0,0,1]  |  vector  |  Orientation axis: [1,0,0] for X-axis, [0,1,0] for Y-axis and [0,0,1] for Z-axis.   
radius  |  optional  |  1  |  number  |  Radius of the sphere or arc to be created in meters.   
lmax  |  optional  |  0.2  |  number  |  Maximum separation between two adjacent data points on far field location in meters.   
  
**Example 1**

This example creates a spherical surface and performs a far field projection using the near field data from a surface monitor named "monitor". 
    
    
    surf = createsphericalsurface([0,pi/4],[0,2*pi],[0,0,1],1,0.1);
    E_near = getresult("DGTD::monitor","fields");
    E_far = near2far(E_near,surf);
    visualize(E_far); 

**Example 2**

This example creates an arc (in the XZ plane) and performs a far field projection using the near field data from a line monitor called "monitor" (also in the XZ plane). 
    
    
    surf = createsphericalsurface([pi/2,pi/2],[pi,2*pi],[0,1,0],1,0.1);
    E_near = getresult("DGTD::monitor","fields");
    E_far = near2far(E_near,surf);
    visualize(E_far); 

**See Also**

[ near2far ](/hc/en-us/articles/360034930753-near2far) , [ List of commands ](/hc/en-us/articles/360037228834) , 
