# interptri

Interpolates a 2D dataset from a triangular grid to another triangular or a rectilinear grid. The data can be complex.

This function is typically used for resampling data evaluated originally in a finite element mesh (monitor data from DGTD, for example) to a new rectilinear grid.

[[Note:]] A special case involves converting data from elements to vertices and vice-versa. This require additional processing, beyond interptri and is covered in the following article - [Interpolating Between Element and Vertex Datapoints in Finite-element Datasets](/hc/en-us/articles/14259382364563)  
---  
[[Note:]] Since 2020a R7, [[interptri]] can interpolate a data set from a triangular to a rectangular grid or to a list of points. The data can be vectorial.  
---  
**Syntax** |  **Description**  
---|---  
out = interptri(tri, vtx, u, xi, yi, extrap_val); out = interptri(tri, vtx, u, xi, yi, extrap_val, "rectilinear"); |  Does a triangular to rectilinear grid interpolation of a function and outputs a PxQxS array of interpolated values, z(xi,yi,p).

  * u is existing data of the finite element mesh (size NxS)
  * xi and yi are arrays with length P and Q, respectively. They specify the points where u is to be sampled on the rectilinear mesh, in the x-direction and y-direction
  * tri is the connectivity array, Mx3, containing row entries that index the three vertices of M triangles. Taken from the simulation region
  * vtx is a matrix with the vertices of the triangular mesh, Nx2, containing row entries of (x,y) pairs. Taken from the simulation region
  * extrap_val(optional): if an interpolation point is outside of the finite element mesh, the point will be assigned this value (default is Inf)

  
out = interptri(tri, vtx, u, xi, yi, extrap_val, "unstructured"); |  Does a triangular to point cloud interpolation of a function and outputs a PxS array of interpolated values.

  * u is existing data of the finite element mesh (size NxS)
  * xi and yi are arrays with length P. They specify the points where u is to be sampled on
  * tri is the connectivity array, Mx3, containing row entries that index the three vertices of M triangles. Taken from the simulation region
  * vtx is a matrix with the vertices of the triangular mesh, Nx2, containing row entries of (x,y) pairs. Taken from the simulation region
  * extrap_val(optional): if an interpolation point is outside of the finite element mesh, the point will be assigned this value (default is Inf)

  
  
**Example**

This is an example of a script for CHARGE that will resample charge "n" on a rectilinear grid. The example assumes that a simulation has been run in CHARGE with multiple bias voltages. The simulation domain is in the XZ plane. The script will select the charge data for the first bias voltage and resample the charge information on the XZ plane to a new rectilinear grid defined by xrect and zrect. This is just to show how the interptri command will get used. It will not actually plot the results unless you try a similar set of commands with a simulation that has already been run.
    
    
    # Read the charge data
    N = getdata("CHARGE","charge","n");# The dimension of N is [L, 1, bb, 1].
      # "L" is the number of vertices, "bb" is the number of bias points.
    temp = size(N);
    L = temp(1); # get the length of N (this is basically the number of vertices).
    vtx = getdata("CHARGE","charge","vertices"); # dimension is [L, 3]. It stores the x, y, z coordinates of all the vertices.
    tri = getdata("CHARGE","charge","elements");# dimension is [ee, 3]. It stores the index of the 3 vertices for all elements. 
    # "ee" is the total number of triangular elements.
    # Set the array with the x coordinates of the new rectilinear grid:
    xmin = -.1e-6;
    xmax = .1e-6;
    xstep = .001e-6;
    xrect = xmin:xstep:xmax;
    # Set the array with the z coordinates of the new rectilinear grid:
    zmin = -0.8e-6;
    zmax = 0;
    zstep = .001e-6;
    zrect = zmin:zstep:zmax; 
    # Prepare the N array to be used in the interptri command. N should have a dimension of L x 1.
    N = pinch(N); # Removing singleton dimensions.
    N = pinch(N(1:L,1)); # Getting data for just one bias voltage (the first one).
    # Prepare the vtx array to be used in the interptri command. vtx should have a dimension of L x 2.
    vtx = vtx(1:L,[1,3]); # getting only x and z axis information (removing the y data).
    # Creating the rectilinear data using interptri
    N_rect = interptri(tri,vtx,N,xrect,zrect); 
    # Plot data
    image(xrect,zrect,N_rect);

**See Also**

[ quadtri ](/hc/en-us/articles/360034406394-quadtri) , [ interptet ](/hc/en-us/articles/360034926673-interptet) , [ quadtet ](/hc/en-us/articles/360034926633-quadtet)
