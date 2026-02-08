# inpoly

Determines if a point is inside or outside a polygon. The function is vectorized so it
can be used to create a mesh of a polygon.

The polygon vertices are contained in a single matrix of dimension Nx2 (or 2xN), where N
\>= 3 is the number of vertices. The dimension 2 corresponds to the x,y positions. For
example, a square of side length 1 can be described by V = [ 0,0; 1,0; 1,1; 0,1] or V =
[ 0,1,1,0;0,0,1,1].

| **Syntax**           | **Description**                                                                                                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = inpoly(V,x,y); | Returns a matrix of the same dimension of x with 1 if the corresponding point is inside the polygon and 0 otherwise. The matrices x and y must have the same length, or one of them can be a singleton. |

**Examples**

The following example shows how to identify the points in a mesh that are inside a
polygon.

```
V = [ 0,0; 1,0; 1,1; 0,1];
x = linspace(-4,4,100);
y = linspace(-4,4,100);
X = meshgridx(x,y);
Y = meshgridy(x,y);
image(x,y,inpoly(V,X,Y),"x","y");
```

The generated image is:

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ polyarea ](./polyarea.md) , [ centroid ](./centroid.md) ,
[ polyintersect ](./polyintersect.md) , [ polygrow ](./polygrow.md) ,
[ polyand ](./polyand.md) , [ polyor ](./polyor.md) , [ polydiff ](./polydiff.md) ,
[ polyxor ](./polyxor.md) , [ meshgridx ](./meshgridx.md) ,
[ meshgridy ](./meshgridy.md)
