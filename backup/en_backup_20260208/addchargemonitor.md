# addchargemonitor

Adds a [charge monitor](/hc/en-us/articles/360034398154) to the simulation environment. This command requires the presence of a CHARGE solver region in the objects tree.

**Syntax** |  **Description**  
---|---  
addchargemonitor; |  Adds a charge monitor to the simulation environment. This function does not return any data.  
addchargemonitor(struct_data); |  Adds a charge monitor and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add a 2D y-normal charge monitor to the simulation environment, set its dimension, and enable saving the charge data in a .mat file.
    
    
    addchargemonitor;
    set("name","charge");
    set("monitor type",6);  # 2D y-normal
    set("x",0);
    set("x span",5e-6);
    set("y",0);
    set("y span",5e-6);
    set("z",0);
    set("save data",1);
    filename = "charge_data.mat";
    set("filename",filename);

**See Also**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [addbandstructuremonitor](./addbandstructuremonitor.md)
- [addefieldmonitor](./addefieldmonitor.md)
- [addjfluxmonitor](./addjfluxmonitor.md)
