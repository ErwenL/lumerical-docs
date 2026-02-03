# exporthtml

Generates an html file describing an element. 

**Syntax** |  **Description**  
---|---  
exporthtml (element_name)  |  Generates an html file describing a custom element. The file lists the element type, symbol, and the list of properties.  This command works only for elements in the Custom folder or its sub-folders.   
  
**Example**
    
    
    addelement("CW Laser");
    # add element to the Custom folder
    addtolibrary;
    # add element to the sub folder "test_folder" of Custom folder
    addtolibrary("test_folder");
    # export html page the CW Laser element in Custom
    exporthtml("CWL_1");
    # export html page of the CW Laser element in "test_folder"
    exporthtml("test_folder::CWL_1");
    # export html pages of all elements in the "test folder"
    exporthtml("test_folder");

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ newproject ](/hc/en-us/articles/360034931473-newproject)
