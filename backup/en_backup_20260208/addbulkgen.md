# addbulkgen

Adds a [bulk (optical) generation region](/hc/en-us/articles/360034398074) to the simulation environment. The bulk generation (source) object can be used to create an analytic solar generation profile. This command requires a CHARGE solver region to be present in the objects tree.

**Syntax** |  **Description**  
---|---  
addbulkgen; |  Add a bulk (optical) generation region. This function does not return any data.  
addbulkgen(struct_data); |  Adds a bulk (optical) generation region and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add a bulk generation (source) object to the CHARGE solver region. The object is set up to calculate the solar generation rate in silicon considering the AM1.5G solar spectrum.
    
    
    addbulkgen;
    set("name","solar");# set dimension
    set("x",0);
    set("x span",2e-6);
    set("y",0);
    set("y span",1e-6);
    set("z",5e-6);
    set("z span",1e-6);
    # set parameters for analytic profile
    set("illumination face",6);  #  upper z
    set("spectrum",0);  # AM1.5G
    set("material",0);  # silicon
    set("interface reflection",1);  # air interface

**See Also**

- [List of commands](../lsf-script-commands-alphabetical.md)
- [set](./set.md)
- [addimportgen](./addimportgen.md)
