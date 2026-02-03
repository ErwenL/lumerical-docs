# polyor

Combines two polygons into one using the Boolean 'or' operation. 

The polygon vertices are contained in a single matrix of dimension Nx2 (or 2xN), where N >= 3 is the number of vertices. The dimension 2 corresponds to the x,y positions. For example, a square of side length 1 can be described by V = [ 0,0; 1,0; 1,1; 0,1] or V = [ 0,1,1,0;0,0,1,1]. 

**Syntax** |  **Description**  
---|---  
V3 = polyor(V1,V2);  |  Returns a new polygon, V3, that is the 'or' of V1 and V2.   
  
**Example**

See example in the polyand function description. 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ polyand ](/hc/en-us/articles/360034926293-polyand) , [ polydiff ](/hc/en-us/articles/360034926313-polydiff) , [ polyxor ](/hc/en-us/articles/360034406134-polyxor) , [ polyarea ](/hc/en-us/articles/360034926213-polyarea) , [ centroid ](/hc/en-us/articles/360034406074-centroid) , [ polyintersect ](/hc/en-us/articles/360034926233-polyintersect) , [ inpoly ](/hc/en-us/articles/360034926253-inpoly) , [ polygrow ](/hc/en-us/articles/360034406094-polygrow)
