# linecross

Determines if two line segments in the x-y plane cross each other.

Line segments are contained in a single matrix of dimension 2\*Nx2, where there are N
line segments. For example, the matrix L = [ 0,0; 1,1; 0,0; 0,1]; represents two lines
segments, one from (0,0) to (1,1) and another from (0,0) to (0,1).

| **Syntax**              | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| out = linecross(L1,L2); | Returns an array of dimension N which determines if the N line segments in L1 and the N line segments in L2 cross; the comparison is done pairwise as in the lineintersect command. L1 and L2 must have the same size (2\*Nx2 for N line segments). The elements in the output array are 0 if the segments do not cross, 1 if they cross and 0.5 if the endpoint of one segment touches the other. Line segments that are coincident and touch also return a value of 0.5 |

**Example**

The following examples illustrate the different outcomes of the linecross function:

```
L1 = [ 0,0; 1,1; 0,0; 1,1 ];
L2 = [ 0,1; 1,0; 2,2; 3,3 ];
?linecross(L1,L2);
result: 
1  
0
L1 = [ 0,0; 1,1 ];
L2 = [ 0.5,0.5; 0,1 ]; # The start point of L2 touches L1
?linecross(L1,L2);
result: 
0.5 
L1 = [ 0,0; 1,1 ];
L2 = [ 1,1; 2,2 ]; # The end point of L1 is the same as the start point of L2
?linecross(L1,L2);
result: 
0.5 
L1 = [ 0,0; 1,1 ];
?linecross(L1,L1);
result: 
0.5
```

**See Also**

[ List of commands ](../lsf-script-commands-alphabetical.md) ,
[ lineintersect ](./lineintersect.md) , [ finite ](./finite.md)
