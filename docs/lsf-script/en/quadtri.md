# quadtri

Calculates the numerical integral of data collected on a 2D triangle mesh using first order trapezoidal quadrature. 

**Syntax** |  **Description**  
---|---  
out = quadtri(tri,vtx,u,n);  |  Calculates the integral of data collected on triangle mesh. A scalar is returned if the input data corresponds to a scalar quantity and a vector with three components is returned if the input data corresponds to a vector quantity.   
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
tri  |  required  |  |  matrix  |  [Mx3] connectivity matrix for the M triangle elements on the mesh.   
vtx  |  required  |  |  matrix  |  [Nx2] or [Nx3] matrix containing the (x,y,z) coordinates of the N vertices of the mesh. If the matrix has only two columns, the z coordinate is assumed to be zero.   
u  |  required  |  |  matrix  |  [Nx1] or [Nx3] matrix containing the data to be integrated at the location of each vertex. If the matrix is of size [Nx1], the data is assumed to be a scalar quantity. If the matrix is of size [Nx3], the data is assumed to be a vector quantity.   
n  |  optional  |  empty  |  matrix  |  [Mx3] matrix with the surface normal vectors for each of the M triangles on the mesh. The columns correspond to the (x,y,z) components of each vector. This input is required only if the data to be integrated is a vector quantity.   
  
**Example**

The following example finds the approximate integral of u on a finite element mesh. 
    
    
    # define 4 vertices in the shape of a rectangle, 
    #point[#1;#2;#3;#4]
    vtx = [0,0; 4,0; 4,3; 0,3];
    # make two triangles (#1,#2,#4) and (#2,#3,#4) with area = 6
    tri = [1,2,4; 2,3,4];
    # Define result values at each vertex point, 
    #point #1, #2, #3, #4
    u=[4,3,2,0];
    # the result of this integral should be 
    # ((4+3+0)/3 + (3+2+0)/3)*6 = 24
    ?I = quadtri(tri,vtx,u);
    result: 
    24 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ interptri ](/hc/en-us/articles/360034405774-interptri) , [ quadtet ](/hc/en-us/articles/360034926633-quadtet) , [ interptet ](/hc/en-us/articles/360034926673-interptet)
