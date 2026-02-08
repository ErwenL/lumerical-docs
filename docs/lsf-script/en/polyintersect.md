# polyintersect

Determines if two polygons intersect.

The polygon vertices are contained in a single matrix of dimension Nx2 (or 2xN), where N
\>= 3 is the number of vertices. The dimension 2 corresponds to the x,y positions. For
example, a square of side length 1 can be described by V = [ 0,0; 1,0; 1,1; 0,1] or V =
[ 0,1,1,0;0,0,1,1].

| **Syntax**                  | **Description** |
| --------------------------- | --------------- |
| out = polyintersect(V1,V2); | Returns         |

- 0 if the polygons do not overlap
- 0.5 if the polygons touch
- 1 if they overlap
- 2 if one polygon completely encloses the other

**Example**

The following example illustrates the different possible intersection situations for two
polygons:

```
V1 = [ 0,0; 1,0; 1,1; 0,1];
V2 = [ 0,0; 2,0; 2,2; 0,1];
?polyintersect(V1,V2);
result: 
2 
?polyintersect(V1,V2+0.5); #Shift V2 to the right by 0.5
result: 
1 
?polyintersect(V1,V2+1); #Shift V2 to the right by 1
result: 
0.5 
?polyintersect(V1,V2+2); #Shift V2 to the right by 2
result: 
0
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ polyarea ](./polyarea.md) , [ centroid ](./centroid.md) , [ inpoly ](./inpoly.md) ,
[ polygrow ](./polygrow.md) , [ polyand ](./polyand.md) , [ polyor ](./polyor.md) ,
[ polydiff ](./polydiff.md) , [ polyxor ](./polyxor.md)
