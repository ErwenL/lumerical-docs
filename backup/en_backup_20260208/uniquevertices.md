# uniquevertices

Given a matrix of vertices, returns a matrix of unique vertices with differences in values larger than a specified tolerance. 

**Syntax** |  **Description**  
---|---  
out=uniquevertices(vertexTable, absTolerance);  |  Returns unique elements of a matrix with differences in values larger than a specified tolerance.  vertexTable is a Mx2 or Mx3 matrix  absTolerance is the magnitude of the tolerance   
  
**Example**

This is a simple example showing how this command works. 
    
    
    # define a matrix with three vertices in 3D:
    vtx = [0,0,0; 1,0,0; 1,1,0; 1,1,0.09];
    ?uniquevertices(vtx, 0.1); # for this tolerance the last two vertices are considered to be the same
    ?uniquevertices(vtx, 0.01); # when the tolerance is decreased the last two vertices are distinguished
    result: 
    0  0  0  
    1  0  0  
    1  1  0  
    result: 
    0  0  0  
    1  0  0  
    1  1  0  
    1  1  0.09  

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ unique ](/hc/en-us/articles/360034406574-unique)
