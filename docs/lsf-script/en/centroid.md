# centroid

Returns the center of mass of a polygon assuming uniform density.

The polygon vertices are contained in a single matrix of dimension Nx2 (or 2xN), where N
\>= 3 is the number of vertices. The dimension 2 corresponds to the x,y positions. For
example, a square of side length 1 can be described by V = [ 0,0; 1,0; 1,1; 0,1] or V =
[ 0,1,1,0;0,0,1,1].

| **Syntax**         | **Description**                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| out = centroid(V); | Returns the center of mass of V, assuming uniform density. The output is a 2x1 matrix representing the x and y positions. |

**Example**

Calculate the centroid of a square of side length 1:

```
V = [ 0,0; 1,0; 1,1; 0,1];
?centroid(V);
result: 
0.5 0.5
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ polyarea ](./polyarea.md) , [ polyintersect ](./polyintersect.md) ,
[ inpoly ](./inpoly.md) , [ polygrow ](./polygrow.md) , [ polyand ](./polyand.md) ,
[ polyor ](./polyor.md) , [ polydiff ](./polydiff.md) , [ polyxor ](./polyxor.md)
