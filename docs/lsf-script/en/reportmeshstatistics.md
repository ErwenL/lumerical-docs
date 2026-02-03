# reportmeshstatistics

Returns statistical information about the mesh grid of the simulation. This command can be used to compare the size and the quality of different mesh grids between different simulations or solvers. The script can only be applied to tetrahedral (3D) and triangular (2D) meshes and thus does not apply to 1D simulations. 

**Syntax** |  **Description**  
---|---  
out = reportmeshstatistics(mesh,ID);  |  Returns statistical information about the mesh grid of the simulation.   
  
**Parameter** |  |  **Default value** |  **Type** |  **Description**  
---|---|---|---|---  
mesh  |  required  |  |  unstructured data set  |  An unstructured data set including the finite element mesh grid   
ID  |  optional  |  An array of all the available domain IDs  |  array of integers  |  An array of integer numbers including the domain IDs (indices) of the elements of the mesh that the report should be restricted to   
out  |  |  |  struct  |  The output includes attributes that provide information such as numElements (total number of elements in the grid), numFaces (total number of faces in the grid), numVertices (total number of vertices in the grid), elementSizeMeasure (an array of values of insphere or incircle radius in SI units for all the elements in the grid which can be used as a measure of the size of each element) and elementQualityMeasure (an array of values of minimum dihedral angle in degrees for all the elements in the grid which can be used as a measure of the quality of each element)   
  
**Examples**

This example obtains the mesh grid from 'grid' attribute of the DGTD solver and stores the statistics related to that mesh and displays the number of faces in the mesh grid. Note that the mesh grid has to be formed before running this example. 
    
    
    grid=getresult("DGTD","grid");
    out=reportmeshstatistics(grid);
    ?out.numFaces;
    

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , 
