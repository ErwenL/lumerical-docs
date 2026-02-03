# getmeshcontours

Gets information about the contours between different domains in an unstructured (finite-element) dataset. The dataset must contain the "ID" attribute (a unique identified for each domain in the finite-element mesh generated in Finite Element IDE based products). 

**Syntax** |  **Description**  
---|---  
A = getmeshcontours(dataset);  |  Returns information about the contours between different domains of the unstructured dataset named "dataset". The output is provided as a cell array. Each entry is a struct with three fields:  **ID:** An integer ID that is unique for that contour.  **adjacent:** Two integers representing the IDs of the adjacent domains.  **elements:** For 2D, Nx2 array and for 3D, Nx3 array of integers that are the indexes to the vertices for each face on the boundary.   
  
**Examples**

The script commands below will get the contour information for the "grid" dataset (available after calculating the finite-element mesh). 
    
    
    mesh("CHARGE");  # calculate the mesh in Finite Element IDE using the CHARGE solver
    grid = getresult("CHARGE","grid");  # get the mesh information ("grid" dataset)
    contours = getmeshcontours(grid);
    # get the ID of the first contour
    ID_1 = contours{1}.ID;
    # get the ID of the two adjacent domains (ID = 0 means external boundary) 
    domains_1 = contours{1}.adjacent;
    # get the index of vertices forming the first contour
    vertices_1 = contours{1}.elements;

**See Also**

[ Datasets ](/hc/en-us/articles/360034409554-Datasets) , [ unstructureddataset ](/hc/en-us/articles/360034929933-unstructureddataset) , [ mesh ](/hc/en-us/articles/360034410654-mesh) , [ getresult ](/hc/en-us/articles/360034409854-getresult)
