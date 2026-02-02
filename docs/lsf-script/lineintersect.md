# lineintersect

Returns the intersection points of two lines in the x-y plane. Note that the intersection point does not have to lie on the segments that define the lines. Use the command linecross to determine if the line segments actually cross . 

Line segments are contained in a single matrix of dimension 2*Nx2, where there are N line segments. For example, the matrix L = [ 0,0; 1,1; 0,0; 0,1]; represents two lines segments, one from (0,0) to (1,1) and another from (0,0) to (0,1). 

**Syntax** |  **Description**  
---|---  
out = lineintersect(L1,L2);  |  Returns the intersection of the lines represented by the segments in L1 and L2. L1 and L2 must have the same size (2*Nx2 for N line segments). The result is a sequence of x,y points in the form Nx2 representing the pairwise intersections of the N lines. There are special cases when 

  * The lines are parallel. In this case, the position returned is (1.#INF,b). The presence of 1.#INF can be tested using the script command finite. The value of b is 0 if the lines coincide and 1 if they do not. 
  * The points in a segment are degenerate, i.e., the same. In this case, the position returned is (1.#INF,b), where b is 0, 1 or 2 if both line segments are degenerate, the first is degenerate, or the second is degenerate, respectively. 

  
  
**Example**

In this first example L1 and L2 are two sets of segments; the result is a 2x2 matrix where the first row is the intersection between the first segments in each set and the second row is the intersection between the second segments in each set. 
    
    
    L1 = [ 0,0; 1,1; 0,10; 1,10];
    L2 = [ 0,1; 1,0; 5,0; 5,1];
    ?lineintersect(L1,L2);
    result: 
    0.5  0.5  
    5  10  

The second example shows the output in the special cases when the lines do not intersect, when they coincide or when the segments are degenerate. 
    
    
    L1 = [ 0,0; 1,1];
    L2 = [ 1,0; 2,1]; #L2 is parallel to L1
    L3 = [ 3,3; 3,3]; #The points in L3 are degenerate
    ?lineintersect(L1,L1);
    ?lineintersect(L1,L2);
    ?lineintersect(L3,L3);
    ?lineintersect(L3,L1);
    ?lineintersect(L2,L3);
    result: 
    1.#INF  1  
    result: 
    1.#INF  0  
    result: 
    1.#INF  0  
    result: 
    1.#INF  1
    result: 
    1.#INF  2    

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ linecross ](/hc/en-us/articles/360034406154-linecross) , [ finite ](/hc/en-us/articles/360034926453-finite)
