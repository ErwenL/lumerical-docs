# exportlib

Exports the .lib file for a CML in the Custom folder. 

**Syntax** |  **Description**  
---|---  
exportlib(name, path, overwrite);  |  Exports the .lib file for a CML in the Custom folder.  name, the CML name in Custom  path, where to save the exported .lib file. Use the current working directory if path is not provided.  overwrite, boolean value to indicate whether or not to overwrite the file if it exists.   
  
**Example**
    
    
    #exports the ".lib" file for "dk.cml"
    exportlib("dk.cml", "C:/Users/xxx", true);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ packagedesignkit ](/hc/en-us/articles/360034407514-packagedesignkit) , [ installdesignkit ](/hc/en-us/articles/360034407534-installdesignkit) , [ importschematic ](/hc/en-us/articles/360034407434-importschematic) , [ exportschematic ](/hc/en-us/articles/360034927573-exportschematic) , [ customlibrary ](/hc/en-us/articles/360034407254-customlibrary) , [ Custom Library & Design Kit ](**%20to%20be%20defined%20**)
