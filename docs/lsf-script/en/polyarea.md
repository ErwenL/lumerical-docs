# polyarea

Returns the area of a polygon. The area is positive if the vertices are defined in a counter-clockwise direction, and negative if the vertices are defined in a clockwise direction. 

The polygon vertices are contained in a single matrix of dimension Nx2 (or 2xN), where N >= 3 is the number of vertices. The dimension 2 corresponds to the x,y positions. For example, a square of side length 1 can be described by V = [ 0,0; 1,0; 1,1; 0,1] or V = [ 0,1,1,0;0,0,1,1]. 

**Syntax** |  **Description**  
---|---  
out = polyarea(V);  |  Returns the area of V. The sign of the area indicates if V is defined in a counter-clockwise (positive) or clockwise (negative) direction.   
  
**Example**

Calculate the area of a square of side length 1: 
    
    
    V = [ 0,0; 1,0; 1,1; 0,1];
    ?polyarea(V);
    result:
    1

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ centroid ](/hc/en-us/articles/360034406074-centroid) , [ polyintersect ](/hc/en-us/articles/360034926233-polyintersect) , [ inpoly ](/hc/en-us/articles/360034926253-inpoly) , [ polygrow ](/hc/en-us/articles/360034406094-polygrow) , [ polyand ](/hc/en-us/articles/360034926293-polyand) , [ polyor ](/hc/en-us/articles/360034406114-polyor) , [ polydiff ](/hc/en-us/articles/360034926313-polydiff) , [ polyxor ](/hc/en-us/articles/360034406134-polyxor)
