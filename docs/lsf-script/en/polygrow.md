# polygrow

Expand or shrink a polygon. Resulting polygons will have the same number of vertices and the same order as polygon V. Consider using polyclean before using polygrow.

The polygon vertices are contained in a single matrix of dimension Nx2 (or 2xN), where N \\(\ge\\) 3 is the number of vertices. The dimension 2 corresponds to the x and y positions. For example, a square of side length 1 can be described by V = [ 0,0; 1,0; 1,1; 0,1] or V = [ 0,1,1,0;0,0,1,1].

**Syntax** |  **Description**  
---|---  
polygrow(V, delta, {"tolerance": tol_value, "legacy": true/false}) |  Returns the vertices of a new polygon that has grown by delta. To shrink a polygon, use delta< 0.

  * For vertices in counter-clockwise order and delta > 0, edges are moved to their right by delta (positive to expand, negative to shrink)
  * Tolerance is used to identify seams (which are not grown) and bowtie-vertices (which are pinned in place). Set the legacy option to 'true' to skip this check.
  * An attempt is made to prevent self-intersection at sharp corners.
  * Value delta can be either scalar or matrix (result will be either a polygon or a cell-array of polygons)

  
  
**Example**

The following example shows the vertices of a square of side length 1 expanded by 0.1 on all sides with the tolerance of 1e-15. Setting the 'legacy' value to 'false' allows identifying seams and bowtie-vertices.
    
    
    V = [ 0,0; 1,0; 1,1; 0,1];  
    ?polygrow(V, 0.1, {"tolerance": 1e-15, "legacy": false});  
      
    result:   
    -0.1 -0.1   
     1.1 -0.1   
     1.1  1.1   
    -0.1  1.1 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [polyclean](/hc/en-us/articles/360046557133) , [polyarea ](/hc/en-us/articles/360034926213-polyarea) , [ centroid ](/hc/en-us/articles/360034406074-centroid) , [ polyintersect ](/hc/en-us/articles/360034926233-polyintersect) , [ inpoly ](/hc/en-us/articles/360034926253-inpoly) , [ polyand ](/hc/en-us/articles/360034926293-polyand) , [ polyor ](/hc/en-us/articles/360034406114-polyor) , [ polydiff ](/hc/en-us/articles/360034926313-polydiff) , [ polyxor ](/hc/en-us/articles/360034406134-polyxor)
