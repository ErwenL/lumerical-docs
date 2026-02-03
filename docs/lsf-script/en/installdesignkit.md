# installdesignkit

Installs a design kit file to the Design Kits folder.

**Syntax** |  **Description**  
---|---  
installdesignkit(filename, path, overwrite); |  Installs a design kit file named ‘filename.cml’ and directs its contents to a user defined ‘path’. The design kit will be available in the element library ‘Design kits’ folder. If ‘overwrite’ is true, it will overwrite an existing design kit with the same name, if ‘overwrite’ is false, it will ask the user for confirmation before overwriting.  
  
**Example**
    
    
    #installs the "dk.cml" library to the Design Kits folder
    installdesignkit("dk.cml", "C:/Users/xxx", true);

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ packagedesignkit ](/hc/en-us/articles/360034407514-packagedesignkit) , [ enabledesignkit ](/hc/en-us/articles/360034927633-enabledesignkit) , [ disabledesignkit ](/hc/en-us/articles/360034407474-disabledesignkit) , [ uninstalldesignkit ](/hc/en-us/articles/360034407554-uninstalldesignkit) , [ importschematic ](/hc/en-us/articles/360034407434-importschematic) , [ exportschematic ](/hc/en-us/articles/360034927573-exportschematic) , [ customlibrary ](/hc/en-us/articles/360034407254-customlibrary) , [ exportlib ](/hc/en-us/articles/360034927673-exportlib)
