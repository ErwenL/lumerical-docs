# polyxor

Combines two polygons into one using the Boolean 'xor' operation.

The polygon vertices are contained in a single matrix of dimension Nx2 (or 2xN), where N
\>= 3 is the number of vertices. The dimension 2 corresponds to the x,y positions. For
example, a square of side length 1 can be described by V = [ 0,0; 1,0; 1,1; 0,1] or V =
[ 0,1,1,0;0,0,1,1].

| **Syntax**           | **Description**                                            |
| -------------------- | ---------------------------------------------------------- |
| V3 = polyxor(V1,V2); | Returns a new polygon, V3, that is the 'xor' of V1 and V2. |

**Example**

See example in the polyand function description.

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) , [ polyand ](./polyand.md)
, [ polyor ](./polyor.md) , [ polydiff ](./polydiff.md) , [ polyarea ](./polyarea.md) ,
[ centroid ](./centroid.md) , [ polyintersect ](./polyintersect.md) ,
[ inpoly ](./inpoly.md) , [ polygrow ](./polygrow.md)
