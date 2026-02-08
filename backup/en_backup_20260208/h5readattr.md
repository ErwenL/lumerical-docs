# h5readattr

Reads attributes from an HDF5 file. 

**Syntax** |  **Description**  
---|---  
attr = h5readattr("filename", "attr_path", "attr_name");  |  Reads the attribute named "attr_name" at the location "attr_path" within the HDF5 file named "filename."   
  
**Parameter** |  **Type** |  **Description**  
---|---|---  
filename  |  string  |  name of the HDF5 file.   
attr_path  |  string  |  name (path) of the dataset or group to which the attribute belongs to.   
attr_name  |  string  |  name of the attribute to be read.   
  
**Examples**
    
    
    filename = "samplefile.h5";
    A = h5info(filename);
    attr_path = A.Groups{1}.Name;
    attr_name = A.Groups{1}.Attributes{1}.Name;
    attr = h5readattr(filename, attr_path, attr_name);

**See Also**

[ h5info ](/hc/en-us/articles/360034927413-h5info) , [ h5read ](/hc/en-us/articles/360034407214-h5read) , [ Reading HDF5 files ](/hc/en-us/articles/360034936913-HDF5-files)
