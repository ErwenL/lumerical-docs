# quadtet

Calculates the numerical integral of data on a 3D finite element mesh.

| **Syntax**                | **Description**                                                       |
| ------------------------- | --------------------------------------------------------------------- |
| out = quadtet(tet,vtx,u); | outputs a scalar, the integral of u on the finite element mesh, where |

- tet: the connectivity array, Mx4, containing row entries that index the four vertices
  of M tetrahedra
- vtx: the vertex array, Nx3, containing row entries of (x,y,z) pairs that locate the N
  vertex points
- u: the data on the finite element mesh (Nx1)

**Example**

The following is a simple example that shows how to calculate the approximate integral
of u on a finite element mesh.

```
# define 8 vertex points in the shape of a cube
# point[#1;#2;#3;#4;#5;#6;#7;#8]
vtx = [1,0,0; 0,0,0; 0,1,0; 1,1,0; 1,0,1; 0,0,1; 0,1,1; 1,1,1];
# make six tetrahedrals from the 8 vertex points, volume=1/6
tet = [1,2,4,8; 1,2,5,8; 2,5,6,8; 2,3,7,8; 2,6,7,8; 2,3,4,8];
# Define result values at each vertex point
# point #1,#2,#3,#4,#5,#6,#7,#8
u=[4, 3.5, 3, 2.5, 2, 1.5, 1, 0.5];
# the result of this integral should be 2.16667
?I = quadtet(tet,vtx,u);
result: 
2.16667 
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ interptri ](./interptri.md) , [ quadtri ](./quadtri.md)
