# adddeltachargesource

Adds a [delta optical generation source](/hc/en-us/articles/360034398094) to the simulation environment. This command requires a CHARGE solver region to be present in the objects tree.

**Syntax** |  **Description**  
---|---  
adddeltachargesource; |  Add a delta optical generation source to the simulation environment. This function does not return any data.  
adddeltachargesource(struct_data); |  Adds a delta optical generation source and set its property using a struct containing "property" and value pairs. See the [struct](https://optics.ansys.com/hc/en-us/articles/360034409574-struct-Script-command) script command page for an example. This function does not return any data.  
  
**Example**

The following script commands will add a delta optical generation source, set its location, and set the generation rate by defining a net electron-hole-pair current (/sec).
    
    
    adddeltachargesource;
    set("name","delta");
    set("x",0);
    set("y",0);
    set("z",5e-6);
    set("source type",2);  #  ehp current
    set("ehp current",1e12);  # net ehp current I_ehp = e*1e12 Amp

**See Also**

- [List of commands](./list-of-commands.md)
- [set](./set.md)
- [addimportgen](./addimportgen.md)
- [addbulkgen](./addbulkgen.md)
