# packagedesignkit

Creates a .cml from a existing folder under Custom library.

**Syntax** |  **Description**  
---|---  
packagedesignkit(name, filename, encrypt, overwrite); |  Creates a design kit file named ‘filename.cml’ from the custom folder named ‘name’. If 'encrypt' = false, it will be packaged without encryption and if 'encrypt' = true, the package will be encrypted. If ‘overwrite’ is true, it will overwrite an existing design kit file with the same name, if ‘overwrite’ is false, it will ask the user for confirmation before overwriting. The default setting for 'overwrite' is false.  
  
**Example**
    
    
    #packages a compact model library in the Custom folder with encryption
    packagedesignkit("dk", "dk.cml", true, true);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ installdesignkit ](/hc/en-us/articles/360034407534-installdesignkit) , [ importschematic ](/hc/en-us/articles/360034407434-importschematic) , [ exportschematic ](/hc/en-us/articles/360034927573-exportschematic) , [ customlibrary ](/hc/en-us/articles/360034407254-customlibrary) , [ exportlib ](/hc/en-us/articles/360034927673-exportlib) , [ Custom Library & Design Kit ](**%20to%20be%20defined%20**) , [ enabledesignkit ](/hc/en-us/articles/360034927633-enabledesignkit) , [ disabledesignkit ](/hc/en-us/articles/360034407474-disabledesignkit) , [ installdesignkit ](/hc/en-us/articles/360034407534-installdesignkit) , [ uninstalldesignkit ](/hc/en-us/articles/360034407554-uninstalldesignkit)
