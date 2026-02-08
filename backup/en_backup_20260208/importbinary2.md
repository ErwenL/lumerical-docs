# importbinary2

Import binary data (1s and 0s) over an entire volume from script variables. The object will be present wherever the binary data is 1 and not when it is 0. This command only applies to import primitives. The function returns 1 if the data is successfully imported. Example script files showing how to use these functions can be found in the Online Help. See the User Guide, Structures section.

**Syntax** |  **Description**  
---|---  
out = importbinary2(binary,x,y,z); |  Import binary data from script variables in three dimensional simulations. All arguments are required.  
**Parameter** |  **Default value** |  **Type** |  **Description**  
---|---|---|---  
binary |  required |  matrix |  The binary data This should be an NxMxP matrix in three dimensions and an NxM matrix in two dimensions. It should have only values of 0 or 1. If other values are present, all non-zero values will be interpreted as 1.  
x |  required |  matrix |  If n is an NxMxP matrix, then x should have dimension Nx1. For two dimensional simulation, if n is an NxM matrix then x should have dimension Nx1. Values of x must be uniformly spaced.  
y |  required |  matrix |  If n is an NxMxP matrix, then y should have dimension Mx1. For two dimensional simulation, if n is an NxM matrix then y should have dimension Mx1. Values of y must be uniformly spaced.  
z |  1 |  number |  If n is an NxMxP matrix, then z should have dimension Px1. Values of z must be uniformly spaced.  
Note: Imported binary object boundaries The boundary of the import binary object is positioned between the vertices where the material is present and the vertices where the material is not present. The shape of this implied boundary can be complex, and the viewport does not show the full detail. The boundary can be moved closer to vertices where the material is present by increasing the "binary threshold" property of the import object. To confirm the boundary that will be used in the simulation by the solver, use an index monitor.  
---  
  
**Example**

Please refer to the [importing spatial binary example](/hc/en-us/articles/360034382754-Import-object-Binary-spatial-data) for details.

**See Also**

[Manipulating objects](/hc/en-us/articles/360037228834), [importbinary](/hc/en-us/articles/360034408734-importbinary)
