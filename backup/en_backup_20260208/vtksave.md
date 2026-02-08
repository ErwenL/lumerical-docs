# vtksave

Saves a Lumerical dataset into the VTK format. The command only saves rectilinear and unstructured datasets. The “filename” will have .vtr appended for rectilinear dataset, .vtu appended for unstructured dataset. The freely available data visualization program Paraview can then be used to create sophisticated plots of your data. 

**Syntax** |  **Description**  
---|---  
vtksave(“filename”, dataset);  |  Save the dataset in vtk file of the name specified.   
  
**Examples**

The following simple example gets the result E, a rectilinear dataset and saves into the VTK format. 
    
    
    E = getresult("monitor2", "E");
    vtksave("beam.vtr", E);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ datasets ](/hc/en-us/articles/360034409554-Datasets) , [ rectilineardataset ](/hc/en-us/articles/360034409474-rectilineardataset) , [ matlabsave ](/hc/en-us/articles/360034928113-matlabsave) , [ Advanced visualizations with ParaView ](/hc/en-us/articles/360034416774-Paraview)
