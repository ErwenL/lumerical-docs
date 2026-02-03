# importnk2

Imports the refractive index (n and k) over an entire volume or surface from script variables. This command only applies to import primitives. The function returns 1 if the data is successfully imported. It is possible to import anisotropic nk data.

**Syntax** |  **Description**  
---|---  
out = importnk2(n,x,y,z); |  Import n (and k) data from script variables in three dimensional simulations, n can be complex. All arguments are required. n must be of dimension NxMxP or NxMxPx3 with N >= 2, M >= 2 and P >= 2.  
  
**Parameter** |  **Default value** |  **Type** |  **Description**  
---|---|---|---  
n |  required |  matrix |  The refractive index. If it is complex-valued, then the imaginary part is interpreted as k. For isotropic material, this should be an NxMxP matrix in three dimensions and an NxMx2 matrix in two dimensions. For anisotropic material, this should be an NxMxPx3 matrix in three dimensions and an NxMx2x3 matrix in two dimensions.  
x |  required |  matrix |  If n is an NxMxP matrix, then x should have dimension Nx1. For two dimensional simulation, if n is an NxMx2 matrix then x should have dimension Nx1. Values of x must be uniformly spaced.  
y |  required |  matrix |  If n is an NxMxP matrix, then y should have dimension Mx1. For two dimensional simulation, if n is an NxMx2 matrix then y should have dimension Mx1. Values of y must be uniformly spaced.  
z |  required |  matrix |  If n is an NxMxP matrix, then z should have dimension Px1. For two dimensional simulation, if n is an NxMx2 matrix then z should have dimension 2x1. Values of z must be uniformly spaced.  
  
**Example**

[Import object - Spatial (n,k) data](/hc/en-us/articles/360034901993-Import-object-Spatial-n-k-data)

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [importnk](/hc/en-us/articles/360034408674-importnk)
