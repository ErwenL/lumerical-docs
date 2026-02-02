# interptet

Interpolates a 3D dataset from a tetrahedral grid to another tetrahedral or a rectilinear grid. The data can be complex.

This function is typically used for resampling data evaluated originally in a finite element mesh (monitor data from CHARGE, for example) to a new rectilinear grid.

[[Note:]] Since 2020a R7, [[interptet]] can interpolate a data set from a tetrahedral to a rectangular grid or to a list of points. The data can be vectorial.  
---  
**Syntax** |  **Description**  
---|---  
out = interptet(tet, vtx, u, xi, yi, zi, extrap_val); out = interptet(tet, vtx, u, xi, yi, zi, extrap_val, "rectilinear"); |  Does a tetrahedral to rectilinear interpolation of a function and outputs a PxQxRxS array of interpolated values, f(xi,yi,zi,p).

  * u is existing data of the finite element mesh (NxS)
  * xi, yi and zi are arrays with length P, Q and R, respectively. They specify the points where u is to be sampled on the rectilinear mesh, in the x-direction, y-direction and z-direction
  * tet is the connectivity array, Mx4, containing row entries that index the 4 vertices of M tetrahedra. Taken from the simulation region
  * vtx is a matrix with the vertices of the tetrahedral mesh, Nx3, containing row entries of (x,y,z) pairs. Taken from the simulation region
  * extrap_val(optional): if an interpolation point is outside of the finite element mesh, the point will be assigned this value (default is Inf)

  
out = interptet(tet, vtx, u, xi, yi, zi, extrap_val, "unstructured");  |  Does a tetrahedral to point cloud interpolation of a function and outputs a PxS array of interpolated values.

  * u is existing data of the finite element mesh (NxS)
  * xi, yi and zi are arrays with length P. They specify the P points where u is to be sampled on
  * tet is the connectivity array, Mx4, containing row entries that index the 4 vertices of M tetrahedra. Taken from the simulation region
  * vtx is a matrix with the vertices of the tetrahedral mesh, Nx3, containing row entries of (x,y,z) pairs. Taken from the simulation region
  * extrap_val(optional): if an interpolation point is outside of the finite element mesh, the point will be assigned this value (default is Inf)

  
  
**Example**

See the example for the interptri script function.

**See Also**

[quadtet](/hc/en-us/articles/360034926633-quadtet), [quadtri](/hc/en-us/articles/360034406394-quadtri), [interptri](/hc/en-us/articles/360034405774-interptri)
