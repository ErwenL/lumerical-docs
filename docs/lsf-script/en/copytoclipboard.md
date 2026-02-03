# copytoclipboard

Copies the selected objects into the system clipboard. Equivalent to 'Ctrl-C'. 

**Syntax** |  **Description**  
---|---  
copytoclipboard;  |  Copies selected objects to the system clipboard   
  
**Examples**

This example shows how to use the copy/paste to clipboard functions to copy an object from a different simulation file into the current simulation file. 
    
    
    # specify file and object names
    current_file = currentfilename;
    template_file = "C:\temp\myObjects.fsp";
    object_name = "my_grating";
    save; #save current file; # save current file
    load(template_file);    # load template file
    select(object_name);    # select object
    copytoclipboard;      # copy object to clipboard
    load(current_file);     # load original file
    pastefromclipboard;     # paste object into file

**See Also**

[ List of commands ](/hc/en-us/articles/360037228834) , [ pastefromclipboard ](/hc/en-us/articles/360034411314-pastefromclipboard) , [ copy ](/hc/en-us/articles/360034408434-copy)
