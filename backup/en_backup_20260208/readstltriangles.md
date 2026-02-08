# readstltriangles

Imports a matrix of vertex positions from an STL file. 

**Syntax** |  **Description**  
---|---  
out=readstltriangles("filename.stl",scaling_factor);  |  Returns an Mx3 matrix with vertices from all STL triangles from the specified STL file.  scaling_factor: An STL file does not contain unit data. To import data in units of microns, set this value to 1e-6. For nanometers, set this value to 1e-9.   
  
**Example**

The following script command will read the STL file named "sample_file.stl" and save the vertex positions assuming units of micron. 
    
    
    vtx = readstltriangles("sample_file.stl",1e-6);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ stlimport ](/hc/en-us/articles/360034924733-stlimport)
