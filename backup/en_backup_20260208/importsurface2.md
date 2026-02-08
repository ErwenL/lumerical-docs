# importsurface2

Imports surface data from script variables. This command only applies to import primitives. The function returns 1 if the data is successfully imported. Example script files showing how to use these functions can be found in the Online Help. See the User Guide, Structures section.

**Syntax** |  **Description**  
---|---  
out = importsurface2(Z,x,y,upper_surface); |  Import a surface from the variables Z, x and y in three dimensional simulations. The upper_surface argument is optional.  
  
**Parameter** |  **Default value** |  **Type** |  **Description**  
---|---|---|---  
Z |  required |  matrix |  The two dimensional matrix that defines the surface.  
x |  required |  matrix |  If Z is an NxM matrix, then x should have dimension Nx1. For two dimensional simulation, if Y is an Nx1 matrix then x should have dimension Nx1.  
y |  required |  matrix |  If Z is an NxM matrix, then y should have dimension Mx1.  
upper_surface |  1 |  number |  This optional argument should be 1 to import the upper surface and 0 to import the lower surface.  
  
**Example**

please refer a complete example: [Import object - Surfaces](/hc/en-us/articles/360034901973)

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [importsurface](/hc/en-us/articles/360034408654-importsurface)
