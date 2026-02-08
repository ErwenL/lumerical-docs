# getsourcedirection

Returns a unit vector in the direction of the wave vector (or k-vector) of the specified source. The unit vector has three elements corresponding to the X,Y and Z directions. 

**Syntax** |  **Description**  
---|---  
out = getsourcedirection("sourcename");  |  Returns a [3x1] matrix with a unit vector in the direction of the specified source wave vector.   
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
sourcename  |  required  |  |  string  |  Name of the source.   
  
**Example**

This example computes a unit vector in direction of the k-vector of the plane wave source named "source". 
    
    
    source_k = getsourcedirection("DGTD::source"); 

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ getperiodicity ](/hc/en-us/articles/360034407174-getperiodicity) , [ gratingorders ](/hc/en-us/articles/360034927353-gratingorders) , [ gratingprojection ](/hc/en-us/articles/360034927373-gratingprojection)
